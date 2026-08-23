---
name: routines
description: Create, fire, and manage Claude Code cloud routines (scheduled/API/GitHub-triggered remote agents). Use when asked to set up a recurring remote agent, a webhook-triggered workflow, automate a daily/weekly task in the cloud, schedule a cron job for Claude Code, or anything involving claude.ai/code/scheduled. Triggers on "routine", "schedule a remote agent", "webhook to Claude", "daily/weekly Claude job", "cron routine", or /routines.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, ToolSearch, WebFetch, RemoteTrigger
license: MIT
metadata:
  origin:
    author: "Malachi Rose / Augment Growth"
    note: >-
      The author's own skill, sanitized for publication: account-specific
      environment and connector IDs, default repository, timezone, and personal
      output paths were replaced with placeholders and a discovery step, so the
      skill works on any Claude Code account. Covered by the repository LICENSE.
---

# Routines — Cloud Scheduled Agents

Routines are **saved Claude Code configurations that run on Anthropic-managed cloud infrastructure** — a prompt + repo(s) + connectors, fired on a schedule, HTTP POST, or GitHub event. They keep working when your laptop is closed.

Docs: https://code.claude.com/docs/en/routines
Fire API: https://platform.claude.com/docs/en/api/claude-code/routines-fire
Web UI: https://claude.ai/code/scheduled

**What this skill needs.** Creating and managing routines runs through the `RemoteTrigger` tool. If it isn't available in this session (load it with `ToolSearch` first — it is often deferred), say so plainly rather than improvising: routines can still be created by hand at https://claude.ai/code/scheduled, and everything below about schedules, prompts, tools, and output conventions applies just the same in the web UI. Nothing else in this skill depends on files outside it.

## When to use routines vs other scheduling

| Need | Use |
|------|-----|
| Runs unattended in cloud, survives laptop off | **Routine** (this skill) |
| Runs inside the current REPL session only | `CronCreate` (in-session) |
| Runs on your own machine with local file/MCP access | Desktop scheduled task |
| One-shot reminder later today | `CronCreate` with `recurring: false` |

**Hard constraint**: routines run in Anthropic cloud. They have **no access to**:
- Chrome DevTools MCP (logged-in browser sessions)
- Local files outside the cloned repo
- Local `.env` variables
- Local MCPs, local notes and documents not in the GitHub repo, or anything else on your machine

If the task needs any of those, either adapt it to use WebFetch/WebSearch + API calls (with secrets added to the cloud env), or use a local scheduler instead.

## Canonical creation body (tested, works)

Load `RemoteTrigger` first, then call `{action: "create", body: ...}` with this exact shape:

```json
{
  "name": "DESCRIPTIVE_NAME",
  "cron_expression": "MM HH * * *",
  "enabled": true,
  "job_config": {
    "ccr": {
      "environment_id": "YOUR_ENVIRONMENT_ID",
      "session_context": {
        "model": "claude-sonnet-4-6",
        "sources": [
          {"git_repository": {"url": "https://github.com/OWNER/REPO"}}
        ],
        "allowed_tools": ["Bash", "Read", "Write", "Edit", "Glob", "Grep", "WebFetch", "WebSearch"]
      },
      "events": [
        {
          "data": {
            "uuid": "GENERATE_FRESH_LOWERCASE_V4_UUID",
            "session_id": "",
            "type": "user",
            "parent_tool_use_id": null,
            "message": {
              "role": "user",
              "content": "THE_PROMPT_HERE"
            }
          }
        }
      ]
    }
  }
}
```

### Values you need to fill in

These are per-account, so look them up rather than guessing:

- **`environment_id`** — an ID like `env_01...`. Find it by running `RemoteTrigger({action: "list"})` and reading the `environment_id` off any existing routine, or open https://claude.ai/code/environments and use the Default environment. If the user has none, they create one there first.
- **Repository** — the GitHub repo the routine clones and writes to. Ask the user which one; a routine always needs somewhere to put its output. The Claude GitHub App must have access to it.
- **Model** — `claude-sonnet-4-6` is a sensible default for routines, which are usually research and automation rather than heavy reasoning. Use a larger model when the task genuinely calls for it.

## Cron conventions

- **Cron is UTC**. Work out the user's local timezone, convert, and confirm the local time back to them before creating anything — this is the single easiest thing to get wrong.
- **Minimum interval: 1 hour**. `*/30 * * * *` is rejected.
- **Avoid minute 0 and 30** — every routine on the platform lands on those. Pick an off-minute (`:07`, `:17`, `:43`, `:51`).
- **Stagger multiple daily routines** by 15+ min so they don't compete for resources.

Examples, for a user on US Pacific time during PDT (UTC-7):
- Daily at 8 AM local -> `17 15 * * *`
- Daily at 7 AM local -> `43 14 * * *`
- Sunday 8 PM local -> `7 3 * * 1` (note: Monday UTC because of rollover)
- Every 2 hours -> `13 */2 * * *`

Watch for daylight saving: a fixed UTC cron shifts by an hour in local terms when the clocks change.

## Allowed tools

Pick the smallest set the routine actually needs. Common combos:

| Routine type | Tools |
|--------------|-------|
| Web research / scanning | `Bash, Read, Write, Edit, Glob, Grep, WebFetch, WebSearch` |
| API automation (no code) | `Bash, Read, Write, Edit, WebFetch` |
| Code review / PR work | `Bash, Read, Write, Edit, Glob, Grep` |
| Data pull + report | `Bash, Read, Write, Edit, Glob, Grep, WebFetch` |

Do **not** add MCP tools unless explicitly attached via `mcp_connections`.

## MCP connections

A routine can reach the MCP connectors the account has already authorized (Gmail, Google Calendar, Slack, and others). Each connector has a `connector_uuid` and a URL, both specific to the account — find them by reading `mcp_connections` off an existing routine via `RemoteTrigger({action: "list"})`, or from the connector settings at https://claude.ai/code. Don't invent a UUID; a wrong one fails at run time, not at creation.

To attach, add an `mcp_connections` array to the creation body at the top level:

```json
"mcp_connections": [
  {"connector_uuid": "THE_CONNECTOR_UUID", "name": "Gmail", "permitted_tools": [], "url": "https://gmail.mcp.claude.com/mcp"}
]
```

## UUID generation

Events require a fresh lowercase v4 UUID. Generate one per routine:

```bash
python3 -c "import uuid; print(uuid.uuid4())"
# or
uuidgen | tr '[:upper:]' '[:lower:]'
```

Never reuse a UUID across routines.

## Output conventions

Routines should write results to the cloned repo on a `claude/*` branch (the default allowed prefix). Standard pattern:

1. Write a markdown report to a predictable path in the repo — something like `reports/{routine-name}/YYYY-MM-DD-HHmm-report.md`. Agree the folder with the user; the point is that every run lands somewhere they can find.
2. Commit to a `claude/{routine-name}-YYYY-MM-DD` branch
3. Also print the report to stdout so it shows in the session transcript at claude.ai/code/scheduled/{trigger_id}

The user can open the session URL to see output, or pull the branch if they want the file.

## Secrets and environment variables

To give a routine API access:

1. Go to https://claude.ai/code/environments
2. Edit Default (or create a new env) and add `KEY=VALUE` pairs
3. Reference them in the prompt as `$KEY` — the routine's Bash sessions will see them

**Always check for secret presence in the prompt** and exit gracefully if missing:

```
REQUIRED ENV VAR: API_KEY must be set. If missing, print
"Missing API_KEY — add at claude.ai/code/environments" and exit.
```

Never hardcode secrets in prompts — they're logged.

## Firing a routine

**Manually (right now, for testing)**:
```
RemoteTrigger({action: "run", trigger_id: "trig_01..."})
```
Returns the trigger config (not the session URL — fire is async; the session appears at claude.ai/code/scheduled/{trigger_id}).

**Via HTTP (for webhooks)**:
```
POST https://api.anthropic.com/v1/claude_code/routines/{trigger_id}/fire
Authorization: Bearer {per-routine-token}
anthropic-version: 2023-06-01
anthropic-beta: experimental-cc-routine-2026-04-01
Content-Type: application/json

{"text": "freeform context appended to the saved prompt"}
```

The `text` field is a single string appended as a user turn. Max 65,536 chars. If sending a JSON webhook payload, stringify it — the routine can parse the string in its prompt.

**Generating the per-routine token**: Web UI only. Open the routine at https://claude.ai/code/scheduled, click the pencil -> Add another trigger -> API -> Generate token. Shown once, can't be retrieved.

## Trigger types and how to add them

| Trigger | Created via | Notes |
|---------|-------------|-------|
| Schedule | `RemoteTrigger create` (this skill) or web UI | Cron in UTC, min 1h |
| API | Web UI only (generates bearer token) | Attach to existing routine |
| GitHub event | Web UI only | Requires Claude GitHub App installed on repo |

A single routine can have multiple triggers.

## Managing routines

```
# List all
RemoteTrigger({action: "list"})

# Get one
RemoteTrigger({action: "get", trigger_id: "trig_01..."})

# Update (partial)
RemoteTrigger({action: "update", trigger_id: "trig_01...", body: {"cron_expression": "..."}})

# Fire now
RemoteTrigger({action: "run", trigger_id: "trig_01..."})
```

**Cannot delete via API**. Go to https://claude.ai/code/scheduled to delete.

**Pausing**: set `"enabled": false` via update. Re-enable by setting back to `true`.

## Common errors and fixes

| Error | Cause | Fix |
|-------|-------|-----|
| `prompt: Extra inputs are not permitted` | Put `prompt` at top level | Move to `job_config.ccr.events[0].data.message.content` |
| `job_config must have "ccr" shape` | Used `session_request` or empty `job_config` | Use `job_config.ccr.{environment_id, session_context, events}` |
| `session_request.worker: Field required` | Used old `session_request` shape | Switch to `job_config.ccr` (v2 shape) |
| `invalid cron expression` | Interval < 1h, or 6-field cron | Use 5-field, >= 1h |
| `proto: unknown field "type"` | Added unknown top-level field | Remove non-schema fields |
| Session fires but does nothing visible | Expected — fire is async, output is in session URL | Check claude.ai/code/scheduled/{trigger_id} |

## Workflow checklist

When the user asks for a new routine:

1. **Clarify the task** — what runs, when, what output, what secrets needed
2. **Check constraints** — does it need a logged-in browser, local files, or local env? If yes, redirect to a local scheduler
3. **Pick schedule** — UTC, off-:00 minute, staggered against existing routines (check `RemoteTrigger list`)
4. **Pick tools** — minimum viable set (avoid adding WebFetch if not needed)
5. **Draft prompt** — self-contained, specific steps, explicit output format + save path, graceful handling of missing secrets
6. **Generate fresh UUID**
7. **Create** — `RemoteTrigger create`
8. **Test** — `RemoteTrigger run` immediately
9. **Report back** — trigger ID, schedule in the user's local time, session URL, any secrets still needed
10. **Say plainly what is still outstanding** if secrets or repo access are pending — a routine that fires without its key fails quietly on a schedule

## Reference: what already exists

Run `RemoteTrigger({action: "list"})` for the current set before creating anything, so new routines don't collide with existing ones. Past run history is at https://claude.ai/code/scheduled.
