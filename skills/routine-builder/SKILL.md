---
name: routine-builder
description: Create, fire, and manage Claude Code cloud routines (scheduled/API/GitHub-triggered remote agents). Use when asked to set up a recurring remote agent, a webhook-triggered workflow, automate a daily/weekly task in the cloud, schedule a cron job for Claude Code, or anything involving claude.ai/code/routines. Triggers on "routine", "schedule a remote agent", "webhook to Claude", "daily/weekly Claude job", "cron routine", or /routine-builder.
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

Routines are **saved Claude Code configurations that run on Anthropic-managed cloud infrastructure** — or your organization's self-hosted environment when routed there — a prompt + repo(s) + connectors, fired on a schedule, HTTP POST, or GitHub event. They keep working when your laptop is closed.

Docs: https://code.claude.com/docs/en/routines
Fire API: https://platform.claude.com/docs/en/api/claude-code/routines-fire
Web UI: https://claude.ai/code/routines

**What this skill needs.** Cloud routines can be created three ways: conversationally with the built-in `/schedule` command (also aliased `/routines`), from the web at claude.ai/code/routines, or programmatically with the `RemoteTrigger` tool — which is what this skill uses, because it gives exact control over the body shape. If `RemoteTrigger` isn't available (load it with `ToolSearch` first — it is often deferred), fall back to `/schedule` or the web UI; everything below about schedules, prompts, tools, and output conventions applies just the same.

`/schedule` requires a claude.ai subscription login; an `ANTHROPIC_API_KEY`/`ANTHROPIC_AUTH_TOKEN`/`apiKeyHelper` setup hides the command entirely.

## When to use routines vs other scheduling

| Need | Use |
|------|-----|
| Runs unattended in cloud, survives laptop off | **Cloud routine** (this skill) |
| Needs local files, local MCP servers, or local env | **Desktop scheduled task** — Desktop Code tab → Routines → New routine → Local. Runs on your machine, 1-minute minimum, full local access. Only fires while the Desktop app is open and the machine is awake. |
| Runs inside the current REPL session only | `/loop` (in-session; jobs expire with the session) |
| One-shot reminder later | One-off schedule on either a cloud routine or a Desktop task — fires once, then auto-disables |

**Cloud vs local — decide this first.** A *cloud* routine runs on Anthropic-managed infrastructure (or your organization's self-hosted environment when routed there), so it has **no access to**:
- A logged-in browser (Chrome DevTools MCP)
- Local files outside the cloned repo
- Local `.env` variables
- Local MCP servers, unless they're declared in a committed `.mcp.json` in the cloned repo or re-added as a connector at claude.ai/customize/connectors
- Anything else on the machine

If the task needs any of that, don't contort the cloud routine — create a **Desktop scheduled task** instead (Desktop Code tab → Routines → New routine → Local, or just describe it in a Desktop session). Local tasks live at `~/.claude/scheduled-tasks/<name>/SKILL.md`, run with full local file and MCP access, allow intervals down to 1 minute, and are managed with the `mcp__scheduled-tasks__*` tools. The trade: they only fire while the Desktop app is open and the computer is awake, and a missed run gets at most one catch-up.

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

- **Timezone.** The web form and `/schedule` take local wall-clock time and convert automatically. A raw `cron_expression` sent through `RemoteTrigger` is **UTC** — convert it yourself and confirm the local time back to the user before creating anything.
- **Minimum interval: 1 hour**. `*/30 * * * *` is rejected.
- **Stagger is automatic.** The platform offsets each routine by a few minutes, consistently per routine, so runs don't pile up. Picking an off-minute (`:07`, `:43`) is still tidy but no longer necessary.

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
3. Also print the report to stdout so it shows in the session transcript at claude.ai/code/routines/{trigger_id}

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
Returns the trigger config (not the session URL — fire is async; the session appears at claude.ai/code/routines/{trigger_id}).

**Via HTTP (for webhooks)**:
```
POST https://api.anthropic.com/v1/claude_code/routines/{trigger_id}/fire
Authorization: Bearer {per-routine-token}
anthropic-version: 2023-06-01
anthropic-beta: experimental-cc-routine-2026-04-01
Content-Type: application/json

{"text": "freeform context appended to the saved prompt"}
```

The `text` field is freeform and is not parsed — send JSON and the routine receives a literal string. It does **not** arrive as a bare user message: it's wrapped in a `<routine-fire-payload>` block labeled as untrusted data, and Claude is told not to follow instructions inside it unless the routine's own prompt says to. **The saved prompt must opt in explicitly** — e.g. "Investigate the alert described in the routine-fire-payload block" — or the text is inert context. The same wrapping applies to text supplied with **Run now**. Max 65,536 chars.

**Generating the per-routine token**: Web UI only. Open the routine at https://claude.ai/code/routines, click the pencil -> Add another trigger -> API -> Generate token. Shown once, can't be retrieved.

## Trigger types and how to add them

| Trigger | Created via | Notes |
|---------|-------------|-------|
| Schedule | `RemoteTrigger create` (this skill) or web UI | Cron in UTC, min 1h |
| API | Web UI only (generates bearer token) | Attach to existing routine |
| GitHub event | Web UI, or CLI via `/schedule` (v2.1.225+) — requires the Claude GitHub App installed on the repo | — |

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

# Inspect runs
RemoteTrigger({action: "list_runs", trigger_id: "trig_01..."})
RemoteTrigger({action: "get_run_log", session_id: "session_01..."})
```

**Cannot delete via API**. Go to https://claude.ai/code/routines to delete.

**Pausing**: set `"enabled": false` via update. Re-enable by setting back to `true`.

## Common errors and fixes

| Error | Cause | Fix |
|-------|-------|-----|
| `prompt: Extra inputs are not permitted` | Put `prompt` at top level | Move to `job_config.ccr.events[0].data.message.content` |
| `job_config must have "ccr" shape` | Used `session_request` or empty `job_config` | Use `job_config.ccr.{environment_id, session_context, events}` |
| `session_request.worker: Field required` | Used old `session_request` shape | Switch to `job_config.ccr` (v2 shape) |
| `invalid cron expression` | Interval < 1h, or 6-field cron | Use 5-field, >= 1h |
| `proto: unknown field "type"` | Added unknown top-level field | Remove non-schema fields |
| Session fires but does nothing visible | Expected — fire is async, output is in session URL | Check claude.ai/code/routines/{trigger_id} |

## Workflow checklist

When the user asks for a new routine:

1. **Clarify the task** — what runs, when, what output, what secrets needed
2. **Cloud or local?** If the task touches local files, a localhost MCP, a logged-in browser, or local env vars, stop and build a Desktop scheduled task instead. Only continue here if the work is genuinely repo- and connector-shaped.
3. **Pick schedule** — UTC, off-:00 minute, staggered against existing routines (check `RemoteTrigger list`)
4. **Pick tools** — minimum viable set (avoid adding WebFetch if not needed)
5. **Draft prompt** — self-contained, specific steps, explicit output format + save path, graceful handling of missing secrets
6. **Generate fresh UUID**
7. **Create** — `RemoteTrigger create`
8. **Test** — `RemoteTrigger run` immediately
9. **Report back** — trigger ID, schedule in the user's local time, session URL, any secrets still needed
10. **Say plainly what is still outstanding** if secrets or repo access are pending — a routine that fires without its key fails quietly on a schedule

## Limits

Routines draw down subscription usage like any session, plus a per-account **daily cap on runs**. One-off runs are exempt from the cap. Current consumption is at claude.ai/code/routines. A green run status means the session started and exited cleanly — not that the task succeeded. Open the run and read it.

## Reference: what already exists

Run `RemoteTrigger({action: "list"})` for the current set before creating anything, so new routines don't collide with existing ones. Past run history is at https://claude.ai/code/routines.
