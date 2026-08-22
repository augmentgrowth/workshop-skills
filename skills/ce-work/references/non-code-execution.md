# Non-Code Execution (Knowledge-Work Carve-Out)

Loaded from Phase 0 Input Triage when the plan carries `execution: knowledge-work`. The plan is a **production plan** for a non-code deliverable (a synthesized document, a study artifact, a research write-up) — typically produced by `ce-plan`'s approach-altitude flow. Execute it to produce the deliverable. This is a minority-case branch; the normal code lifecycle does not apply and is not invoked here.

## What this skips

Do **not** run any of the code-shipping machinery — it does not fit knowledge work:

- No branch/worktree setup (Phase 1 Step 2).
- No task-list-from-implementation-units, no execution-strategy/subagent dispatch keyed on `Files:`.
- No Test Discovery, no test-scenario completeness, no system-wide test check.
- No incremental code commits, and none of `references/shipping-workflow.md` (no PR, no CI).

## Execute the production plan

1. **Read the plan fully.** It is a decision artifact describing *how* the deliverable gets made: which sources to read, how to mine each, how they combine, the shape of the deliverable, and any forks the user already confirmed. Honor those decisions.
2. **Read the sources the plan names** — the actual inputs (PDFs, transcripts, docs, links). Treat user-named resources as authoritative; read them rather than working from memory. If a named source is missing, say so plainly rather than substituting.
3. **Synthesize and produce the deliverable** following the plan's intended shape and the confirmed forks. This is the work the approach-plan deliberately deferred.
4. **Save and report.** Write the deliverable somewhere the user will actually find it again, and report its absolute path. Choose the destination in this order: the path the user named at the checkpoint; otherwise **the folder the plan itself lives in**, beside the source material the deliverable was built from; otherwise a `docs/` subpath, but **only in a project that already has one** — do not create a `docs/` folder in a workspace that has none. Give the file a descriptive, dated name (`YYYY-MM-DD-<topic>.md`) rather than a generic one. Offer a git commit only where a repository actually exists; where it does not, say the file is written and leave it there.

## Stay scoped to non-code deliverables

The carve-out is for knowledge-work output. If producing the deliverable legitimately requires emitting code (a script, a config file, a data-transform), route that specific sub-step back through the normal code path so its safeguards (Test Discovery, review, commit hygiene) still apply — do not silently produce code under the carve-out. The deliverable itself stays non-code.
