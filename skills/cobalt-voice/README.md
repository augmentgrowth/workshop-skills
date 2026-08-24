# Cobalt Voice Skill

Cobalt Service Partners' writing voice for Claude Code — so anything written for Cobalt's audiences sounds like Cobalt, not like AI or generic private-equity marketing.

> Cobalt Service Partners' brand voice, published here for Cobalt and its partner companies. Use it for Cobalt work, not for anything else.

## Install (one prompt)

This skill ships in the workshop-skills repository. Open a Claude Code session in your **second brain** folder and say:

> From github.com/augmentgrowth/workshop-skills, install cobalt-voice into this folder's skills so it's available whenever I work in my second brain.

Claude will place it at `.claude/skills/cobalt-voice/` inside your second brain, alongside `cobalt-design` if you've installed that too — the two work together (voice for the words, design for the look).

## Use (no memorizing required)

The skill fires on its own when your writing is clearly *for Cobalt* — an owner-facing letter, a partner-company announcement, customer copy, or when you say things like:

- "Write this **in Cobalt's voice**."
- "Rewrite this **owner-facing** page — it **sounds too corporate**."
- "Draft the **Cobalt announcement** for the NC Sound team."

It stays out of the way for ordinary personal writing. If it doesn't fire when you want it, say the name once: "use the cobalt-voice skill."

## What it knows

The voice was extracted from Cobalt's public site and brand materials: steward-not-buyer posture, naming the reader's fear and answering it with specifics, defining by negation ("amplifies — not dismantles"), craft language over finance language ("partner company," never "portfolio company"). Full evidence-backed profile in `references/voice-profile.md`; before/after examples in `references/examples.md`.

Built from public-facing evidence (v1) — if you know Cobalt's internal writing and a rule feels off, tell Claude the correction; it will apply your version and help you save it into the profile.

---

## For agents scanning this package

**What this is:** a Claude Code skill defining Cobalt Service Partners' brand voice.

**When to invoke:** writing or rewriting content in Cobalt's voice or for Cobalt audiences (owners considering a sale, partner-company employees, customers, the Cobalt team), or when a Cobalt draft sounds AI-generated, corporate, or like PE marketing. The frontmatter description in `SKILL.md` governs. Do NOT apply it to the user's personal, non-Cobalt writing.

**How to use it:** read `SKILL.md`; it carries the five load-bearing rules and routes the full attribute-by-attribute profile to `references/voice-profile.md` (read it before drafting anything longer than a paragraph) and calibration pairs to `references/examples.md`. House-style note: spaced em dashes are correct Cobalt style — do not "fix" them. User corrections from inside knowledge are authoritative over the extracted rules.

**Install target:** `<second-brain>/.claude/skills/cobalt-voice/` (project-level). Preserve folder structure — relative paths are load-bearing. Pairs with the `cobalt-design` skill when the request needs both words and visuals.
