# bootstrap.md — fresh-build workflow

Load when `Brand/<brand-slug>/` does NOT exist in the current working folder.

Goal: produce the full brand package — two installed skills + proof
artifacts — from the catalogued source materials.

## Step 0 — Source inventory + lean confirmation

Print every catalogued source with its lane label:

```
Sources I will use:
  [intent]    your brand-guidelines PDF  (vision-extracted)
  [reality]   https://www.yourcompany.com/  (fetched and measured)
  [vibe]      @yourcompany on Instagram

Should the result match your official brand guidelines (intent), or the
way your website looks today (reality)? [intent]
```

The user confirms. Slug derivation: lowercase company name, single-hyphenated.
"Summit Mechanical" -> `summit-mechanical`. Confirm before creating folders.

Also ask now which shelf the finished skills should live on (see "Where
things live" in SKILL.md) so Step 9 needs no second question.

Brand folder: `Brand/<brand-slug>/` in the current working folder. Create
the tree now:

```
Brand/<brand-slug>/
├── voice/
├── design/
└── demos/
```

## Step 0a — Voice guide resolution

If the user provided a clean voice guide document, skip to Step 1.

Otherwise follow `references/voice-guide-generation.md`. For PDF/PPT
sources, vision-read in 20-page chunks. This captures:
- color photography style + dominant grade
- logo placement, sizing, lockup variants
- typography rendering at actual size (not just font-name metadata)
- layout density, grid systems, white-space conventions
- photographic mood (lifestyle vs studio vs documentary)

Feed all chunks plus any fetched website/social content into the voice
guide generation. Save the output to:

```
Brand/<brand-slug>/voice/<Brand>_Brand_Voice_Guide.md
```

## Step 1 — Validate voice guide frontmatter

Required fields:
- `name: <Brand> Brand Voice Guide`
- `version: 1.0`
- `brand: <Brand canonical name>`

Surface missing fields to the user. Do not proceed until present.

## Step 2 — Build the voice skill

Invoke `voice-skill-builder` (normally installed alongside this skill)
with the validated voice guide as input. If it is not installed in this
environment, author the voice skill by hand instead: follow
`references/brand-contract.md` plus the structure below — the contract
is sufficient on its own. Target structure:

```
Brand/<brand-slug>/voice/<brand-slug>-voice/
├── SKILL.md            # always-loaded, target <100 lines
├── references/
│   ├── editing.md      # editing protocol
│   ├── examples.md     # calibration pairs (15-20 examples)
│   ├── channels.md     # per-channel rules
│   └── vocabulary.md   # forbidden/preferred, signature phrases, brand stats
└── README.md           # what this skill is
```

The generated voice skill's SKILL.md must declare all brand rules per
`references/brand-contract.md` — read that contract before authoring.

## Step 3 — Generate design tokens

Follow `references/design-tokens-generation.md` with:
- the same source set as Step 0a
- the intent/reality lean from Step 0
- vision-enabled PDF reading (same chunked pattern)

Output: `Brand/<brand-slug>/design/design.md`

Inspect frontmatter — must contain at minimum: `colors.primary`,
`typography.display` (or a display-role typography token), and a body
typography token. If any is missing or tagged inferred, surface to the
user before continuing — these load-bear for every render step.

## Step 3a — Wrap the design skill

Follow `references/design-skill-wrap.md` to author:

```
Brand/<brand-slug>/design/<brand-slug>-design/
├── SKILL.md                      # short: procedure by output type + do-nots
└── references/design-tokens.md   # the design.md content — single source of truth
```

## Step 4 — Render the proof artifacts

```bash
# Derive brand-aware CSS from design.md (you run this; never the user)
python scripts/derive_css_from_design.py \
  --design Brand/<brand-slug>/design/design.md \
  --out /tmp/_<brand-slug>_brand_vars.css
```

Per `references/pdf-styling.md`, produce for each of the two documents a
styled standalone HTML master, then print it to PDF:

- `Brand/<brand-slug>/voice/<Brand>_Brand_Voice_Guide.html` + `.pdf`
- `Brand/<brand-slug>/design/<Brand>_Design_System.html` + `.pdf`

The design spec renders IN the tokens it documents. Include three
calibration pairs (generic AI copy vs. their voice) in the voice guide so
a human can judge fit instantly.

**Self-review loop (mandatory, both artifacts).** Render, look at the
render yourself, check for overlap, overflow, crowding, dead space,
substituted or wrong fonts, low contrast, page-count spill. Fix, re-render,
look again. Only the render counts as done.

## Step 5 — Generate demo artifacts

Substitute placeholders in templates into the demos folder:

| Template | Output |
|---|---|
| `templates/brand_in_action.md.tmpl` | `demos/_brand_in_action.md` (rendered after substitution) |
| `templates/brand_showcase.html.tmpl` | `demos/brand_showcase.html` |
| `templates/welcome_email.html.tmpl` | `demos/welcome_email.html` |

Placeholders: `{{BRAND}}`, `{{BRAND_SLUG}}`, `{{TAGLINE}}`, `{{PRIMARY_COLOR}}`,
`{{SECONDARY_COLOR}}`, `{{DISPLAY_FONT}}`, `{{BODY_FONT}}`,
`{{SIGNATURE_PHRASE}}`, `{{AFFIRMATION}}`. Values come from design.md
frontmatter + voice guide non-negotiables section. See
`references/demo-generation.md` for the full flow.

Optional: if a `humanizer` skill is installed, run the rendered
`_brand_in_action.md` through it before the PDF render to remove AI tells.

```bash
# Screenshot the two HTML mockups for embedding
python scripts/build_screenshots.py \
  --html-dir Brand/<brand-slug>/demos/ \
  --out-dir Brand/<brand-slug>/demos/

# Render the PDF
python scripts/build_pdf.py \
  --brand "<Brand>" \
  --md Brand/<brand-slug>/demos/_brand_in_action.md \
  --vars-css /tmp/_<brand-slug>_brand_vars.css \
  --png-dir Brand/<brand-slug>/demos/ \
  --out Brand/<brand-slug>/demos/<Brand>_Brand_In_Action.pdf \
  --prepared-for "<Brand> Team" \
  --tagline "<Brand tagline from voice guide>"
```

Run the same self-review loop on the demo PDF and both HTML mockups.
Then delete the working intermediates (`_*.md`, and PNGs used only for
embedding) so the demos folder holds only the finished files.

## Step 6 — Validation gate

Load `references/validation.md` for the full pattern. Summary:

1. Read the voice guide. Extract the "Channel cheat-sheet" and the
   "Non-negotiables" sections.
2. Generate 4-8 test prompts: one per channel mentioned in the cheat-sheet,
   plus 1-2 "free-form" prompts (no channel angle) to test core voice.
3. For each prompt: invoke the generated voice skill, write the output to
   `/tmp/<brand-slug>-validation/outputs/<prompt-id>.md`.
4. Run `scripts/validate_voice_skill.py`:
   ```
   python scripts/validate_voice_skill.py \
     --voice-skill Brand/<brand-slug>/voice/<brand-slug>-voice/ \
     --voice-guide Brand/<brand-slug>/voice/<Brand>_Brand_Voice_Guide.md \
     --outputs-dir /tmp/<brand-slug>-validation/outputs/ \
     --brand "<Brand>" \
     --out /tmp/<brand-slug>-validation/scorecard.md
   ```
5. **Second-pass review.** Spawn a validator subagent (same LLM family)
   per `references/validation.md` to catch what regex scoring misses.
   Append its findings to the scorecard.

If any prompt scores below 90% (after both passes), HALT. Surface the
scorecard to the user. Common fixes: tighten the non-negotiables section
in the voice guide, add a missing rule, regenerate the voice skill,
re-run validation.

On PASS, copy the scorecard into the brand folder so the user keeps it:
`Brand/<brand-slug>/voice/validation_scorecard.md`.

## Step 7 — Install the skills

Copy both skill folders onto the shelf the user chose in Step 0:

- This project's shelf: `.claude/skills/<brand-slug>-voice/` and
  `.claude/skills/<brand-slug>-design/` inside their second brain
- Personal shelf: the user-level skills folder (resolve the correct path
  for their operating system; do not assume macOS)

You do the copying. Tell the user a fresh conversation may be needed
before the skills wake up.

## Step 8 — START-HERE note

Render `templates/START-HERE.md.tmpl` with placeholders substituted to
`Brand/<brand-slug>/START-HERE.md`.

## Done state

Report in plain language, naming real paths:

```
Your brand package is ready:
  Skills installed:  <brand-slug>-voice, <brand-slug>-design  (on your chosen shelf)
  Voice guide:       Brand/<brand-slug>/voice/<Brand>_Brand_Voice_Guide.pdf
  Design system:     Brand/<brand-slug>/design/<Brand>_Design_System.pdf
  Demos:             Brand/<brand-slug>/demos/  (Brand-In-Action PDF + 2 live mockups)
  Validation:        scorecard PASS (>=90%)

Try each skill in a new conversation:
  "Write an Instagram post about <topic> in our voice"
  "Make this one-pager look like <Brand>"
```
