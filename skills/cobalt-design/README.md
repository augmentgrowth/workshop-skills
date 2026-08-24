# Cobalt Design Skill

Official Cobalt Service Partners brand system for Claude Code — colors, typography, and logo usage — so anything you ask for comes out on-brand.

> Cobalt Service Partners brand assets, published here for Cobalt and its partner companies. The marks and brand system belong to Cobalt — use them for Cobalt work, not for anything else.

## Install (one prompt)

This skill ships in the workshop-skills repository. Open a Claude Code session in your **second brain** folder and say:

> From github.com/augmentgrowth/workshop-skills, install cobalt-design into this folder's skills so it's available whenever I work in my second brain.

Claude will place it at `.claude/skills/cobalt-design/` inside your second brain. That's the recommended home: the skill travels with your work, and every session you start there can use it.

## Use (no memorizing required)

You don't invoke this skill by name. Just ask for what you want and mention the brand or the polish level — the skill fires on its own. Examples:

- "Turn this summary into a **client-ready** one-pager **in Cobalt's look**."
- "Style this report **on-brand** and export it as a polished HTML page."
- "Draft a **Cobalt-branded** slide outline for the leadership update."

If Claude ever doesn't pick it up, say the skill name once: "use the cobalt-design skill."

## What's inside

| File | What it is |
|---|---|
| `SKILL.md` | The instructions Claude follows — when to apply the brand and how |
| `references/design-tokens.md` | The source of truth: exact colors (hex), fonts with fallbacks, logo rules |
| `assets/logos/` | Five approved logo files (light/dark lockups + standalone marks) |

---

## For agents scanning this package

**What this is:** a Claude Code skill (`SKILL.md` + resources) that applies Cobalt Service Partners' brand system to designed outputs.

**When to invoke:** any request for Cobalt-branded, styled, on-brand, polished, or client-ready documents, presentations, or HTML pages. The trigger description in `SKILL.md` frontmatter governs.

**How to use it:** read `SKILL.md` first; it routes all color/typography/logo values to `references/design-tokens.md` — never restate or approximate those values from memory, and never invent a value that isn't in the tokens file (ask instead). Logo selection: the tokens file states rules in *background* terms (blue-wordmark lockup on light backgrounds, white lockup on dark) — follow those, not the filenames. Fonts fall back gracefully per the documented stacks; end users won't have brand fonts installed.

**Install target:** `<second-brain>/.claude/skills/cobalt-design/` (project-level, so it loads for sessions in that folder). Preserve the folder structure — `SKILL.md` references its resource files by relative path.
