# W2 · Step 8 — Your Meeting Routine

**Where:** the Claude **Desktop app**, Code tab, in your **second-brain folder**.
**What you'll have when done:** a routine that turns your meetings into a running action-item list and a digest of what you owe — on a schedule, without you.

**The move: describe the routine to Claude, and Claude builds it.** You don't fill out a form — you paste one prompt and approve what it creates. (Prefer clicking it together yourself? The manual path is at the bottom.)

## Steps

1. Open Claude Code (Desktop app) in your second-brain folder.
2. No meeting notes yet? Save the [sample meeting transcript](sample-meeting-transcript-summit-mechanical.md) into `02_Areas/Meetings/` first — same exercise, borrowed meeting.
3. Paste the prompt box below. Claude creates the routine as a **local scheduled task** on your machine.
4. When it's created, click **Run now** on it once — you'll watch it work AND pre-approve its tools so scheduled runs never stall on permission prompts.

## The prompt — copy everything in the box

```text
Create a local scheduled routine on this machine (a Desktop scheduled task — local, NOT a cloud routine) named "Action items digest", running weekdays at 4:30 PM, with exactly these instructions:

---
Look through 02_Areas/Meetings/ in this vault (create the folder if it doesn't exist) for meeting notes or transcripts added or modified in the last 24 hours. Work only from files in that folder — do not search my calendar, email, or anything else.

For each meeting found: pull out the action items — what was agreed, who owns each item, and by when. Append my items to 02_Areas/Meetings/Action Items.md (create it if missing), prefixed with today's date. Append, never overwrite.

Then give me a short digest: each meeting in one line, and every open action item I owe, oldest first. Don't send anything yourself, and if you find no meetings from the last 24 hours, tell me that in one line and stop — don't make anything up. End with one line suggesting a next step, like: "Want the full deep recap on any of these? Run /call-summary on it."
---

After creating it, tell me where it lives and remind me to hit Run now once to approve its tools.
```

*(Change "weekdays at 4:30 PM" to any time you'll actually read it — "last 24 hours" means the routine works whatever time it runs.)*

## Done when

- **Run now** produced a digest (or an honest "no meetings found"), and
- the routine shows in your Scheduled/Routines list with its recurring time.

## If it goes sideways

- **Claude builds a cloud routine instead:** stop it and say "make it a LOCAL scheduled task on this machine" — a cloud routine runs on a server that can't see your second brain.
- **A run hangs past ~5 minutes:** stop it and check the instructions — the sweep above touches only your Meetings folder and always finishes; hangs come from added steps that search calendars or mail.
- **Nothing to sweep at all:** describe a different chore instead — any recurring job off any connector you have, in plain English. The pattern is the point: *a described job + a schedule = an agent.* (Simplest fallback: an 8-line morning brief from your calendar and inbox.)

## Level it up (later, not today)

Ask Claude to **add a Phase 1** to the routine: before the sweep, search OneDrive (via your Microsoft 365 connector) for meeting transcripts added in the last 24 hours — one or two file searches only, never calendar enumeration — and save new ones into `02_Areas/Meetings/`. Granola users: same idea, reading Granola. Or go further: have the routine file your action items into your project management tool with a confirm-first step — the routine proposes, you approve.

## Manual path (if you'd rather click it yourself)

**Routines → New routine → Local** (local matters — cloud can't see your files). Name it, point the folder at your second brain, paste the instructions between the `---` marks above into the Instructions box, schedule weekdays at your time, Create, then **Run now** once.
