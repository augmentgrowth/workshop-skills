---
name: my-brand-skills-builder
version: 1.0.1
description: |
  Build (or update) your own company's brand voice + design skills from your
  real brand materials. Produces two installable skills — `<your-company>-voice`
  and `<your-company>-design` — plus presentable proof artifacts for each: a
  styled brand voice guide (HTML + PDF), a design system spec rendered in your
  own brand (HTML + PDF), and three demo artifacts that show voice + design
  working together. Accepts any combination of sources: a brand-guidelines
  PDF or deck, your live website URL, an on-brand document you already trust,
  social handles. Detects first-build vs update mode by whether your brand
  folder already exists.

  Use this skill whenever the user wants Claude to learn their company's
  brand — voice, look, or both. Fire on natural-language requests like
  "build my brand skills", "teach Claude our brand", "make a voice and design
  skill for my company", "set up our brand system", "update our brand skills",
  or "/my-brand-skills-builder".

  Boundary: when the user wants ONLY a voice skill (no design tokens, no
  design skill, no demo artifacts), route to `voice-skill-builder` instead.
  This orchestrator is for the full brand package.
argument-hint: "[company-name] [source-path-or-url]"
---

# my-brand-skills-builder

You orchestrate a complete brand package for the user's own company. The
finished output lives in their second brain: two installed skills
(`<brand-slug>-voice` and `<brand-slug>-design`), a brand folder holding the
voice guide and design spec as styled HTML + PDF, and three demo artifacts
that prove the package works — all rendered in the brand they describe, so
the user can judge correctness on sight.

## When you fire

User says any of: "build my brand skills", "teach Claude our brand",
"set up our brand system for X", "update our brand skills", or
`/my-brand-skills-builder X`.

If the user names a company but provides no source materials, ask once for
at least one source (a brand-guidelines PDF, their website address, a
document that already sounds like them, or a social handle). Do not invent
a brand.

## Where things live

Everything lands inside the folder the user works in (their second brain).
The brand folder is `Brand/<brand-slug>/`. Skills install onto one of two
shelves — ask which, in the workshop's shelves language:

- **This project's shelf** (`.claude/skills/` inside their second brain) —
  the brand skills are available whenever they work in this folder.
- **Your personal shelf** (the user-level skills folder) — available in
  every project on this computer.

You do the copying; the user never touches a terminal. After installing,
tell them a new conversation may be needed before the skills wake up.

Brand slug = lowercase company name, spaces and punctuation replaced with
single hyphens, no trailing hyphens. "Summit Mechanical" -> `summit-mechanical`.
Confirm the slug with the user before creating folders.

## Mode detection

Before anything else, check whether the brand folder already exists
(`Brand/<brand-slug>/` in the current working folder):

- **Exists** -> load `references/maintenance.md` and run the update loop.
- **Does not exist** -> load `references/bootstrap.md` and run the full build.

## Brand-agnostic principle

**Every brand-specific rule lives in the generated voice skill's SKILL.md,
not in this orchestrator or its scripts.** The validator parses forbidden
vocab, required phrases, punctuation budgets, and pacing thresholds from
whatever the generated voice skill declares. If a rule isn't declared, the
validator doesn't impose one. See `references/brand-contract.md` for the
exact contract the generated voice skill must follow.

The orchestrator should NEVER hardcode one company's patterns as defaults.
If you find yourself making a hardcoded assumption ("a tagline must close
every piece", "max 1 em dash"), that rule belongs in the generated voice
skill, not here.

## Bootstrap protocol (linear, every step every time)

1. **Source inventory.** Catalog every input by lane (`intent` / `reality` /
   `vibe` / `baseline`). Confirm with the user: "Sources I will use: [list].
   Should the result match your official brand guidelines (intent) or the
   way your website looks today (reality)?"
2. **Voice guide resolution.** If the user provided a clean voice guide
   document, validate it. Otherwise generate one following
   `references/voice-guide-generation.md` against the catalogued sources.
   For PDF/PPT sources, use vision-enabled Read in 20-page chunks so visual
   brand DNA (photography, layout density, typography rendering) informs
   the extraction, not just the text.
3. **Validate voice guide frontmatter.** Required fields: name, version,
   brand. Surface gaps to the user.
4. **Build the voice skill.** Invoke `voice-skill-builder` (installed
   alongside this skill) to produce `<brand-slug>-voice/`. The generated
   voice skill's SKILL.md must declare all brand rules per
   `references/brand-contract.md`.
5. **Generate design tokens.** Follow `references/design-tokens-generation.md`
   against the same source set. Output to `Brand/<brand-slug>/design.md`.
6. **Wrap the design skill.** Follow `references/design-skill-wrap.md` to
   author `<brand-slug>-design/` — a short procedural SKILL.md with the
   design.md content as its `references/design-tokens.md` single source of
   truth, including the mandatory "Look at what you made" self-review section.
7. **Render the proof artifacts.** Per `references/pdf-styling.md`: derive
   the brand CSS variables from design.md
   (`scripts/derive_css_from_design.py`), then render the voice guide and
   the design spec as styled standalone HTML, and print each to PDF. The
   design spec renders IN the tokens it documents — a wrong color or font
   is visible on sight.
8. **Generate demos.** Per `references/demo-generation.md`: substitute the
   three templates, generate channel demos and before/after pairs by
   invoking the new voice skill, screenshot the HTML mockups
   (`scripts/build_screenshots.py`), render the Brand-In-Action PDF
   (`scripts/build_pdf.py`).
9. **Self-review every visual output.** Mandatory: render each artifact
   (PDF or browser screenshot) and look at the render yourself. Check for
   overlap, overflow, crowding, dead space, substituted or wrong fonts,
   low contrast, page-count spill. Fix what you find, re-render, look
   again. Do not declare the work done from the source code — only from
   the render.
10. **Validation gate.** Run `scripts/validate_voice_skill.py` to score the
    voice skill against 4-8 generated test prompts, then the second-pass
    review per `references/validation.md`. Threshold: 90%. Halt and surface
    failures if below.
11. **Install + closing message.** Copy both skills onto the shelf the user
    chose. Then tell them exactly where everything landed — each skill,
    each PDF, each demo — and how to invoke each skill in their next
    conversation (one example prompt per skill).

## Maintenance protocol (update mode)

Load `references/maintenance.md`. Summary:

1. Apply the user's described edits to the voice guide or `design.md`
2. If voice changed: re-sync the voice skill via `voice-skill-builder`
   update mode, bump version
3. Re-render only the artifacts whose source changed; re-run the
   self-review loop on anything re-rendered
4. Bump version frontmatter on edited files
5. Re-copy the updated skill(s) onto the user's shelf

## Routing block (load on demand)

**References** (load when the linked step requires deeper guidance):

- **`references/bootstrap.md`** - detailed step-by-step for fresh build
- **`references/maintenance.md`** - update loop
- **`references/voice-guide-generation.md`** - voice guide generation
  procedure (spectrums, parseable rule formats, channel tone) with
  `assets/brand_voice_template.md` as the foundation
- **`references/design-tokens-generation.md`** - design.md generation:
  source lanes, extraction, normalization, accessibility pass, schema
  (`examples/DESIGN.md` is the reference output)
- **`references/design-skill-wrap.md`** - authoring the installable
  `<brand-slug>-design` skill from design.md
- **`references/validation.md`** - test-prompt generation + assertion
  scoring + second-pass review
- **`references/brand-contract.md`** - **REQUIRED reading before authoring
  the voice skill.** Spec for which SKILL.md fields the validator parses.
- **`references/pdf-styling.md`** - how `derive_css_from_design.py` reads
  design.md frontmatter and how the HTML masters become PDFs
- **`references/demo-generation.md`** - the three demo artifacts:
  structure, parameterization, embedding flow

**Scripts** (you run these yourself at the step indicated; never ask the
user to run them):

- `scripts/derive_css_from_design.py` - artifact render: design.md -> CSS variables partial
- `scripts/build_pdf.py` - demo render: brand_in_action markdown -> styled PDF
- `scripts/build_screenshots.py` - demo render: HTML mockups -> PNG for embedding
- `scripts/validate_voice_skill.py` - validation gate: assertion-based voice scoring
  (brand-agnostic — reads rules from the generated voice skill's SKILL.md)

**Templates** (substitute placeholders at runtime, write to the brand folder):

- `templates/brand_in_action.md.tmpl`, `brand_showcase.html.tmpl`,
  `welcome_email.html.tmpl` - the three demo artifacts
- `templates/START-HERE.md.tmpl` - the "what's in this folder" note written
  into `Brand/<brand-slug>/`

## Self-heal

On any failure (script crash, wrong output format, missing dependency,
validation gate halts unexpectedly):

1. Fix the immediate problem and continue the build
2. If the fix reveals a gap in this skill's references, note it in
   `CHANGELOG.md`: `[YYYY-MM-DD] What changed and why`
3. If a validation failure traces to a brand assumption hardcoded in this
   orchestrator or its scripts (not in the generated voice skill), that is
   a generalization bug: push the rule down into the generated voice
   skill's SKILL.md. Never patch the orchestrator to fit one brand.

## Gotchas

- **Brand vars must win the CSS cascade.** `build_pdf.py` emits font
  `@import`s first, base CSS next, brand `:root` overrides last. If a
  render comes out in the default blue/green palette, the vars file
  isn't being applied — check that ordering before anything else.
- **Google Fonts drops whole families on wrong weight axes.** A URL
  requesting `:wght@700;900` for a single-weight family returns nothing
  and the mockup silently falls back to sans. Verify the family's real
  weights.
- **The templates define the placeholder set, not the docs.** Scan each
  template for `{{...}}` tokens (~45 across the three) and fill every
  one; the reference tables list only the shared core.
- **Templates carry neutral defaults that can violate the brand**
  (gradients, rounded corners, dark-on-dark cells). The render-inspect
  loop exists to catch this — reconcile against design.md before
  screenshotting.
- **design.md needs flat frontmatter keys for the render scripts**
  (`typography.display`/`body` as strings, `surface_variant` with
  underscore) alongside the spec's nested scales.
- **Scripts want absolute paths.** `build_pdf.py` builds file URIs;
  relative `--md`/`--png-dir` paths crash it.

## Inputs reference

| Input | Lane | How used |
|---|---|---|
| Company name | -- | Slug derivation, file naming, all templates |
| Voice guide document (clean) | `intent` | Skips Step 2; passed to voice-skill-builder |
| Brand-guidelines PDF/PPT | `intent` | Vision-extracted, feeds voice guide AND design tokens |
| Live website URL | `reality` | Fetched and measured for design tokens + voice samples |
| On-brand Word doc / deck | `reality` | Measured directly (fonts, colors, register) |
| Social handles (IG/TikTok) | `vibe` | Informs photography style, register, motifs |
| Competitor references (URLs) | `baseline` | Fills gaps only; never overrides the brand's own sources |

Minimum required to run: company name + one source material.

## Output contract

After a successful bootstrap, the user has:

1. `Brand/<brand-slug>/` in their second brain: voice guide (md + HTML +
   PDF), `design.md` + design spec (HTML + PDF), three demo artifacts,
   and a START-HERE note
2. `<brand-slug>-voice` and `<brand-slug>-design` installed on the shelf
   they chose
3. A validation scorecard (>=90%)
4. A closing message naming every file and how to invoke each skill

Every visual artifact has been through the render-inspect-fix loop before
the user sees it.
