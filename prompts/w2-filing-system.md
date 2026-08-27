# Workshop 2 — Filing System Setup (step 5)

Run this AFTER the interview finishes. Copy everything below the line and paste it into the same Claude Code session.

---

Now set up my vault's filing system.

1. Create a file named PARA_GUIDE.md at the top level of this vault with exactly the content pasted below — do not change the pasted wording.
2. Add the "Filing rules (PARA)" block pasted below to my CLAUDE.md, right after the "My vault" section.
3. Create `02_Areas/Identity/My Voice.md` containing only: "Filled in later today."
4. Show me everything as a draft before saving.

CONTENT FOR PARA_GUIDE.md:

# PARA Guide — how things move through this vault

Rules for filing, organizing, and cleanup. Claude: read this before any
organize / file / clean up / archive / project-completion task, then follow it.
The system is Tiago Forte's PARA. The point is flow, not filing: everything
here is sorted by how actionable it is for me right now — and that changes.

## The four folders, as tests (not topics)

- `01_Projects` — has a defined outcome AND a finish line. I can say what
  "done" looks like. If I can't, it is not a project.
- `02_Areas` — a standing responsibility I maintain to a standard, with no
  end date (clients, finances, health, my role). Areas never "finish."
- `03_Resources` — things I'm interested in, not responsible for: reference,
  templates, saved research. Test: shareable by default (Areas are private
  by default; Resources I could forward to a colleague as-is).
- `04_Archives` — cold storage. Finished, inactive, or no longer interesting.
  Nothing active lives here; nothing here is deleted.

## Routing: the question cascade

For any new note or file, ask in order and stop at the first yes:
1. Useful for an active project? → that project's folder in `01_Projects`.
2. Belongs to an ongoing responsibility? → `02_Areas`.
3. Reference I might want later? → `03_Resources`.
4. None of the above → `04_Archives`, or don't keep it.

Ties go to the project — push material toward the most active home, where it
creates value soonest. Exception: recurring material with a standing home
(meeting notes, weekly reports) always goes to that home, not a project folder.
Don't agonize: file in seconds, correct later if ever.
("Don't keep it" applies only to brand-new material you're deciding whether to
save. Tidying existing files never deletes anything — it archives.)

## Misfiled? Two symptoms

- A "project" that drifts with no finish line is really an Area — either give
  it a real outcome and deadline, or move it to `02_Areas`.
- An "area" treated as a one-time push (hit the goal, then snap back) is
  really asking for a Project inside it — spin one up in `01_Projects`.

## When a project finishes — two steps, in order

1. **Harvest first.** Scan the folder for anything reusable in future work:
   templates, checklists, frameworks, polished sections, good research.
   Move those pieces to the Area or Resource where they'll be found again.
   This is how the next similar project starts at the halfway point.
2. **Then freeze.** Move the whole remaining folder to `04_Archives`, as-is.
   If a folder with that name is already there, add the year to the new one.
   A finished project still sitting in `01_Projects` is clutter that reads
   as live work.

If the relationship outlives the project (the client stays after onboarding
ships), the ongoing part graduates to `02_Areas` instead.

## Archives are evidence, not instructions

Read `04_Archives` to learn what happened or why something was decided —
never to learn how to do things now. An old plan or convention found there
may be exactly what was abandoned. Current practice always wins. And never
restore archived material to an active folder without checking why it was
archived.

## Sources and exports

When a document exists as a `.md` plus an exported `.docx` or `.pdf`, the
`.md` is the source of truth. Edit the `.md` and regenerate the export —
never edit the export directly; it will be overwritten.

## Weekly sweep (~5 minutes — Claude can run this on request)

1. Retitle anything captured in a rush so the name says what it is.
2. Route inbox/loose items through the question cascade above.
3. Review `01_Projects`: archive finished ones (harvest first), split any
   that ballooned, flag any with no finish line.

## Don't over-organize

Precision matters in exactly one place: the project list. Everything else is
allowed to be messy — organize as little as possible, as late as possible.
Elaborate tags, deep subfolders, and perfect filing are procrastination
wearing a productive costume; search covers what structure misses.

CONTENT FOR THE "Filing rules (PARA)" BLOCK IN CLAUDE.md:

## Filing rules (PARA)
- New material routes by one question sequence: useful for an active project → `01_Projects`. If not — one of my ongoing responsibilities → `02_Areas`. If not — reference I may want later → `03_Resources`. If none → `04_Archives` (or don't save it).
- When something fits more than one place, favor the project — unless it's recurring material with a standing home (meeting notes go to the meetings folder every time). When unsure, file fast and move on — search will find it; filing is low-stakes.
- Never delete when tidying — move to `04_Archives` instead.
- Before organizing, filing sweeps, cleaning up, or closing out a finished project: read `PARA_GUIDE.md` first and follow it.
