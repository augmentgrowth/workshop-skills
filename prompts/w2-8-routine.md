# W2 · Step 8 — Your Meeting Routine

**Where:** the Claude Desktop app → **Code tab → Routines → New routine → Local.**
**What you'll have when done:** a routine that turns your meetings into a running action-item list and a digest of what you owe — on a schedule, without you.

> **Local, not cloud — this matters.** A cloud routine runs on a server that cannot see your second-brain folder, so it will find nothing. Create it from the **New local routine** dialog. Don't paste the description into the main chat box — that path defaults to a cloud routine.

Two versions below. **Start with Option A** — it runs in ~3 minutes and shows you the whole pattern. Upgrade to Option B when you want the transcript pull automated too.

---

## Option A — demo it now: the sweep (~3 min)

Works on whatever is already in your Meetings folder. No transcripts yet? Save the [sample meeting transcript](sample-meeting-transcript-summit-mechanical.md) into `02_Areas/Meetings/` first — same exercise, borrowed meeting.

### Steps

1. **Routines → New routine → Local.** Name it (e.g., "Action items digest") and set the folder to your **second-brain folder**.
2. Paste the Option A instructions below, schedule **Weekdays** at any time you'll read it, click **Create**.
3. Hit **Run now** and watch it work.

### Option A instructions — copy everything in the box

```text
Look through 02_Areas/Meetings/ in this vault (create the folder if it doesn't exist) for meeting notes or transcripts added or modified in the last 24 hours. Work only from files in that folder — do not search my calendar, email, or anything else.

For each meeting found: pull out the action items — what was agreed, who owns each item, and by when. Append my items to 02_Areas/Meetings/Action Items.md (create it if missing), prefixed with today's date. Append, never overwrite.

Then give me a short digest: each meeting in one line, and every open action item I owe, oldest first. Don't send anything yourself, and if you find no meetings from the last 24 hours, tell me that in one line and stop — don't make anything up. End with one line suggesting a next step, like: "Want the full deep recap on any of these? Run /call-summary on it."
```

---

## Option B — the full workflow: pull + sweep

Same sweep, plus a first phase that fetches new Teams transcripts into the folder automatically. Set this up as the keeper once Option A has run clean; replace the routine's instructions with the box below (or make it a second routine).

### Option B instructions — copy everything in the box

```text
Two phases, in order. All files live in 02_Areas/Meetings/ in this vault — create that folder if it doesn't exist. Total run should stay under ~5 minutes: keep tool calls lean, and when in doubt, move on rather than dig.

PHASE 1 — Pull new transcripts (budget: a few minutes, roughly 10 tool calls — never more).
Using my Microsoft 365 connector, search my OneDrive for meeting recordings or transcripts added or modified in the last 24 hours — start with my "Recordings" folder (that's where Teams puts transcripts for meetings I organize). One or two file searches only. Do NOT enumerate my calendar, do NOT look meetings up one by one, and do NOT search mail. Save each new transcript found as a markdown file in 02_Areas/Meetings/, named "<date> - <meeting title>.md"; skip anything already saved. You'll only see meetings you attended — that's expected. If nothing turns up quickly or the connector is unavailable, say so in one line and move to Phase 2 — finding nothing is a normal outcome, not an error.

PHASE 2 — Sweep the folder.
Look through 02_Areas/Meetings/ for meeting notes or transcripts added or modified in the last 24 hours. For each meeting: pull out the action items — what was agreed, who owns each item, and by when. Append my items to 02_Areas/Meetings/Action Items.md (create it if missing), prefixed with today's date. Append, never overwrite. Then give me a short digest: each meeting in one line, and every open action item I owe, oldest first. Don't send anything yourself, and if you find no meetings from the last 24 hours, tell me that in one line and stop — don't make anything up. End with one line suggesting a next step, like: "Want the full deep recap on any of these? Run /call-summary on it."
```

---

## Done when

- **Run now** produced a digest (or an honest "no meetings found"), and
- the schedule chip shows your recurring time. ("Last 24 hours" means the routine works whatever time you schedule it — morning or evening.)

## If it goes sideways

- **A run hangs past ~5 minutes:** stop it. You're almost certainly on Option B and the pull phase is digging — switch to Option A now (it always finishes), and keep Option B's phase-1 budget lines intact when you retry.
- **Nothing to sweep at all:** describe a different chore instead — any recurring job off any connector you have, in plain English. The pattern is the point: *a described job + a schedule = an agent.* (Simplest fallback: an 8-line morning brief from your calendar and inbox.)
- **Granola users:** if your meeting notes live in Granola, Option B's Phase 1 can read Granola instead — say so in the instructions.

## Level it up (later, not today)

Add a step that files your action items into your project management tool — with a confirmation step first, so the routine proposes and *you* approve what gets pushed. Ask Claude to draft this using the routine-builder skill.
