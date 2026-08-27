# maintenance.md — update-loop workflow

Load when `Brand/<brand-slug>/` already exists in the current working folder.

Goal: apply the user's described edits, re-sync derived artifacts, re-install
the updated skill(s). Same orchestrator skill, different code path.

## Step 1 — Apply the user's described edits

The user describes changes. Common patterns:

- "Add `franchisees` to the words we never use"
- "Change our primary blue from #4152EB to #3A48D9"
- "Add a TikTok section to the channel rules"
- "Update the locations stat from 185+ to 200+"

Edit the relevant source file directly:

| Change scope | Source file |
|---|---|
| Voice — non-negotiable, channel cheat-sheet, attributes | `voice/<Brand>_Brand_Voice_Guide.md` |
| Voice — per-channel detail | also `voice/<brand-slug>-voice/references/channels.md` |
| Voice — vocabulary / stats | also `voice/<brand-slug>-voice/references/vocabulary.md` |
| Design — colors, typography, spacing | `design/design.md` (and the design skill's `references/design-tokens.md`) |
| Demo content | `demos/_brand_in_action.md` (if regenerating) |

## Step 2 — Re-sync the voice skill (if voice changed)

If you edited `<Brand>_Brand_Voice_Guide.md`:

1. Determine which derived files need to change. Most edits land in the
   guide AND one of the `<brand-slug>-voice/references/*.md` files. Edit
   both to match.
2. If non-negotiables changed: edit `<brand-slug>-voice/SKILL.md`
   non-negotiables section too — that's the always-loaded layer.
3. Bump SKILL.md frontmatter `version` (semver: x.y.PATCH for edits,
   x.MINOR.0 for new rules, MAJOR.0.0 for breaking voice changes).

## Step 2a — Re-sync the design skill (if design changed)

If you edited `design/design.md`, mirror the change into the design
skill's `references/design-tokens.md` and bump its SKILL.md version.
The two must never disagree — the installed skill is what Claude reads.

## Step 3 — Re-render affected artifacts

Re-derive CSS if `design/design.md` changed:
```bash
python scripts/derive_css_from_design.py \
  --design Brand/<brand-slug>/design/design.md \
  --out /tmp/_<brand-slug>_brand_vars.css
```

Re-render only the artifacts whose source changed:

| Edited source | Re-render |
|---|---|
| Voice guide | voice guide HTML + PDF |
| design.md | design spec HTML + PDF, plus Brand-In-Action PDF (uses primary color) |
| brand_in_action.md | `demos/<Brand>_Brand_In_Action.pdf` |
| brand_showcase.html / welcome_email.html | re-run `build_screenshots.py` then re-render Brand-In-Action PDF |

Run the self-review loop (render, inspect, fix, re-render) on everything
re-rendered before showing it.

## Step 4 — Bump version frontmatter

Touch every edited file's `version:` field. Cascade conservatively:

- Patch edit (typo, single rule tightening) -> file version x.y.z+1
- New rule, new vocab term, new channel -> file version x.y+1.0
- Breaking voice change (e.g., reverse "no Oxford comma" -> "Oxford comma") -> file version x+1.0.0

## Step 5 — Re-run validation (recommended, not strict)

For non-trivial voice edits, re-run the validation suite per
`references/validation.md`. For pure design edits (colors, typography),
skip — only voice changes affect voice-skill output.

## Step 6 — Re-install

Copy the updated skill folder(s) back onto the shelf the user chose at
bootstrap (overwrite the old copy). Tell the user a fresh conversation
picks up the new version, and summarize what changed in plain language.

## Self-heal

If maintenance breaks (validation regression after a voice edit, render
script fails): fix it, note the gotcha in `CHANGELOG.md`. Future runs
should not hit the same failure.
