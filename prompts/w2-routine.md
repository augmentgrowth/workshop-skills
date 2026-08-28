# W2 · Step 7 — Your Meeting Routine

**Where:** the Claude Desktop app → **Code tab → Routines → New routine → Local.**
**What you'll have when done:** a routine that pulls today's meeting transcripts into your second brain every evening, extracts your action items into a running list, and sends you a digest of what you owe.

> **Local, not cloud — this matters.** A cloud routine runs on a server that cannot see your second-brain folder, so it will find nothing. Create it from the **New local routine** dialog. Don't paste the description into the main chat box — that path defaults to a cloud routine.

## Steps

1. Open **Routines → New routine** and choose **Local**.
2. Name it (e.g., "Evening action items digest") and set the folder to your **second-brain folder**.
3. Paste the instructions below into the Instructions box.
4. Schedule: **Weekdays** at a time you'll actually read it (4:30 PM works well).
5. Click **Create**, then hit **Run now** once to watch it work before trusting the schedule.

## The routine instructions — copy everything in the box

```text
Two phases, in order.

PHASE 1 — Pull today's transcripts.
Check my Microsoft 365 connector for any Teams meeting transcripts from meetings that happened today (for meetings I organized, they land in my OneDrive "Recordings" folder). Save each new one as a markdown file in the Meetings folder of my second brain, named "<date> - <meeting title>.md". If the connector is unavailable or finds nothing new, skip this phase and continue — don't stop.

PHASE 2 — Sweep the folder.
Look through my Meetings folder for any meetings that happened today — including any new meeting notes or transcripts that were added today. For each meeting: pull out the action items — what was agreed, who owns each item, and by when. Append my items to a running file called Action Items.md in the Meetings folder, prefixed with today's date. Append, never overwrite. Then give me a short digest: each meeting in one line, and every open action item I owe, oldest first. Don't send anything yourself, and if you find no meetings from today, tell me that in one line and stop — don't make anything up. End with one line suggesting a next step, like: "Want the full deep recap on any of these? Run /call-summary on it."
```

## Done when

- **Run now** produced a digest (or an honest "no meetings found today"), and
- the schedule chip shows your recurring time.

## If it goes sideways

- **No transcripts found:** save the [sample meeting transcript](sample-meeting-transcript-summit-mechanical.md) into your Meetings folder and Run now again — same exercise, borrowed meeting.
- **Nothing to sweep at all:** describe a different chore instead — any recurring job off any connector you have, in plain English. The pattern is the point: *a described job + a schedule = an agent.* (Simplest fallback: an 8-line morning brief from your calendar and inbox.)
- **Granola users:** if your meeting notes live in Granola, Phase 1 can read Granola instead — say so in the instructions.

## Level it up (later, not today)

Add a step that files your action items into your project management tool — with a confirmation step first, so the routine proposes and *you* approve what gets pushed. Ask Claude to draft this using the routine-builder skill.
