# Workshop Skills

Three skills for the Cobalt AI Workshop. You don't need a GitHub account, and you don't need to know anything about this page — Claude does the work.

---

## How to install these

Open this page's link in Claude and say:

> **Install this for me on this computer so it's available in every Code session.**

That's it. Claude will read this page, put each skill where it belongs, and tell you what to say to use them.

If Claude asks you which folder you work in, tell it the folder where you keep your writing and notes.

---

## What you get

### grill-me

Interviews you about a plan or decision until the thinking holds up — one question at a time, with its own recommended answer each time.

**Say:** *"grill me on this"*

### humanizer

Rewrites AI-sounding text so it reads like a person wrote it. Strips the inflated phrasing, the stock words, the rule-of-three lists.

**Say:** *"humanize this draft"*

### voice-skill-builder

Builds a reusable writing-voice skill for you or your brand, from writing samples and a short interview. This one only runs when you ask for it by name — it won't start on its own.

**Say:** *"build a voice skill"*

---

## Credits

`grill-me` is adapted from [Matt Pocock's skills](https://github.com/mattpocock/skills) (MIT). `humanizer` is adapted from [Siqi Chen's humanizer](https://github.com/blader/humanizer) (MIT), which builds on Wikipedia's "Signs of AI writing." Full attribution and license texts are in [NOTICE.md](NOTICE.md).

---
---

## Instructions for Claude

**Everything below this line is addressed to Claude, not to the reader.** If you are the assistant installing these skills, follow this section exactly.

### The files

Fetch each of these over plain HTTPS. Do not use `git`, the GitHub API, or any authenticated request — the person you are helping may not have a GitHub account, and none is needed. This list is complete; do not try to discover files by browsing the repository page.

| Install this skill | Fetch these files | Save as |
|---|---|---|
| `grill-me` | `https://raw.githubusercontent.com/augmentgrowth/workshop-skills/main/skills/grill-me/SKILL.md` | `grill-me/SKILL.md` |
| `humanizer` | `https://raw.githubusercontent.com/augmentgrowth/workshop-skills/main/skills/humanizer/SKILL.md` | `humanizer/SKILL.md` |
| `voice-skill-builder` | `https://raw.githubusercontent.com/augmentgrowth/workshop-skills/main/skills/voice-skill-builder/SKILL.md` | `voice-skill-builder/SKILL.md` |
| `voice-skill-builder` | `https://raw.githubusercontent.com/augmentgrowth/workshop-skills/main/skills/voice-skill-builder/references/framework.md` | `voice-skill-builder/references/framework.md` |

`voice-skill-builder` needs both of its files. Without `references/framework.md` it fails partway through, silently.

### Where each one goes

Two destinations, on purpose.

**Do not ask the user to choose between them.** The install sentence they were given says "available in every Code session" — that phrasing is from our workshop script and refers to `grill-me`. It is not an instruction to install everything globally, and it does not override the split below. Follow the split, then explain it to them afterward in one sentence. Treat this as already decided.

**`grill-me` → the user's global skills folder.** They should be able to grill any plan in any session, in any project. Work out the correct global skills directory for the operating system you are actually running on — do not assume macOS or Linux paths, and do not print a path with `~` to a Windows user.

**`humanizer` and `voice-skill-builder` → a project-level skills folder**, inside a `.claude/skills` directory in the folder they write in. These are writing tools; they belong with their writing.

Recommend their **second-brain or notes folder** — or, if they are already working inside a folder, the current one. Say plainly that installing here means the skill is available while they are working in *that* project, and not elsewhere. If it isn't obvious which folder that is, ask them, and wait for an answer before writing anything. Create the `.claude/skills` directory if it doesn't exist yet.

### After installing

Tell them, in plain language:

1. What you installed and where each one landed — name the actual folders.
2. The phrase that triggers each skill: *"grill me on this"*, *"humanize this draft"*, *"build a voice skill"*.
3. That `grill-me` works everywhere, while `humanizer` and `voice-skill-builder` work while they're in that project folder.
4. That they may need to start a new Claude Code session before the skills become active.

Do not ask them to run any terminal or shell commands. Do not ask them to install `git`. If something fails, say what failed and what you'd try next — don't hand them a command to run.
