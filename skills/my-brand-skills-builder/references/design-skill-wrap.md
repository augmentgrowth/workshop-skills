# design-skill-wrap.md — authoring the installable `<brand-slug>-design` skill

After `design.md` exists, wrap it as an installable design skill so the
brand's look applies automatically whenever the user asks for on-brand
work — the same shape as a professionally packaged design skill: a short
procedural SKILL.md plus a single-source-of-truth tokens reference.

## Structure

```
<brand-slug>-design/
├── SKILL.md                      # short: when to apply, procedure by output type, do-nots
└── references/design-tokens.md   # the design.md content — every value lives here, nowhere else
```

`references/design-tokens.md` IS the generated design.md (same content;
add a one-line header noting it's the installed copy). When design.md
changes in maintenance mode, this file changes with it.

## SKILL.md template

Author it with these sections, populated from design.md — keep it under
~80 lines; values live in the tokens file, never repeated in SKILL.md:

```markdown
---
name: <brand-slug>-design
version: 1.0.0
description: Applies <Brand>'s brand system — colors, typography, logo
  usage — to documents, presentations, HTML pages, and other designed
  outputs. Use whenever the user asks for <Brand>-branded, styled,
  on-brand, polished, or client-ready work.
---

# <Brand> Design

## When to apply

Any output someone outside the user's own notes will look at: a memo or
one-pager, a deck or deck outline, an HTML page or export, a report, a
template. If the user says "make this look right," "client-ready,"
"on-brand," or names <Brand>, this applies. Not for internal scratch
notes, code, or plain-text chat answers.

## First step, always

Read `references/design-tokens.md`. It holds every color, font stack,
and usage rule. This file deliberately does not repeat those values —
the tokens file is the single source of truth.

## Procedure by output type

[One short subsection per output type the brand actually produces —
document with styled export, HTML page, deck outline — each stating
which tokens drive it and any brand-specific rules extracted from
design.md's Do's and Don'ts.]

## Look at what you made

Mandatory for every visual output. After generating, render the
artifact — PDF, image, or a browser screenshot — and look at the render
yourself. Check for overlap, overflow, crowding, dead space, substituted
or wrong fonts, low contrast, and page-count spill. A mostly empty page
is a defect — rebalance or merge until every page earns its place. Fix
what you find, re-render, and look again. Do not declare the work done
from the source code. Only from the render.

## Do not

- Do not approximate colors. Use the exact hex values from the tokens
  file. No "close enough," no CSS named colors.
- Do not invent missing brand values. If the tokens file doesn't define
  something (a chart palette, an icon style), ask rather than guessing.
- Do not distort logos — no stretching, recoloring, or rebuilding.
- [Any brand-specific do-nots surfaced by design.md's Do's and Don'ts,
  including WCAG pairings to avoid.]

## Fonts degrade on purpose

[If the brand font is licensed/uncommon: state the full fallback stack
from the tokens file and that outputs should still read as <Brand> when
the brand font is absent — expected behavior, not a defect.]
```

## Rules

- **Brand rules live in the wrapped skill, not this orchestrator** —
  same principle as the voice side (`references/brand-contract.md`).
- Populate every bracketed section from design.md; delete sections that
  don't apply rather than leaving placeholders.
- The "Look at what you made" section is not optional — it is what makes
  the installed skill self-correcting for a non-technical owner.
- After authoring, smoke-test it: generate one small on-brand artifact
  following the new SKILL.md, run its own self-review loop, and confirm
  the tokens file answered every styling question without guessing.
