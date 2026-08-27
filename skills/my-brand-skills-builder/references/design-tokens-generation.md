# design-tokens-generation.md — generating design.md

Inlined from the standalone generate-design-md skill so this orchestrator
is self-contained. Produces a spec-conformant `design.md` following the
Google Labs DESIGN.md open specification
(github.com/google-labs-code/design.md, alpha) — the single source of
visual truth that the design skill, the renders, and every downstream
agent consume. See `examples/DESIGN.md` for a complete, populated
reference output; when in doubt about a section's shape or tone, look
there first.

Act as a Design Systems Lead. Lead with system *intent* — what each token
is FOR — not just its value, so downstream agents can extrapolate to
components nobody has tokenized yet.

The output must be:

- **Machine-parseable**: YAML frontmatter follows the DESIGN.md alpha
  schema exactly. Token references resolve. Hex colors are sRGB with `#`
  prefix. Dimensions carry units.
- **Human-explainable**: prose pairs descriptive design language with
  technical values ("Boston Clay" — Tertiary #B8422E, sole driver for
  interaction states).
- **Auditable**: source conflicts land in `## Deviations`; nothing is
  silently merged. Missing required tokens get accessible fallbacks
  tagged inline with an HTML comment.
- **Accessibility-aware**: every component `backgroundColor`/`textColor`
  pair is contrast-checked against WCAG AA; failures surface in
  `## Do's and Don'ts`.

## Source classification

Every input belongs to one of four lanes — classifying up front
determines how conflicts resolve.

| Lane | What it is | What it tells you |
|---|---|---|
| `intent` | Brand guideline PDFs, internal style docs | What the brand *should* look like |
| `reality` | Live production website, an on-brand doc/deck, app screenshots | What the brand *actually* looks like today |
| `vibe` | Social posts, ad creative, marketing pages | Emotional register, photography style, illustration mood |
| `baseline` | Competitor refs | Category conventions to lean into or break from |

Default weighting per token: `intent` > `reality` > `vibe` > `baseline` —
except when the user chose the reality lean at bootstrap Step 0, where
`reality` overrides `intent` for token values.

## Extraction

Use what the current environment provides, best tool first:

- **Live URL**: if a Firecrawl skill/tool is installed — or the user
  approved the keyless CLI setup at source inventory (`npx -y
  firecrawl-cli@latest`, no API key needed on the free tier) — scrape
  with the `branding` format (auto-extracts colors, fonts, typography,
  spacing, components), plus a markdown scrape of the homepage. If the
  user declined (the source-inventory step already offered once — don't
  re-ask), fetch the page natively and measure what the HTML/CSS
  declares: hex values in stylesheets, font-family stacks, spacing
  patterns, plus a vision pass on a screenshot when available.
- **PDF/PPT brand guide**: vision-enabled Read in 20-page chunks. Look
  for explicit hex codes, font names, spacing scales, component examples.
  Watch for inconsistency *within* the guide (logo-page palette vs
  UI-page palette) — that's its own deviation source.
- **On-brand Word doc / deck**: measure it directly. Office files are zip
  archives — read the theme XML for the real color palette and font
  scheme rather than eyeballing a render. Measured values beat asserted
  ones.
- **Social refs**: if a scraper skill is installed, pull the grid;
  otherwise ask the user for a few screenshots. Dominant colors,
  photographic style, recurring motifs — these inform prose more than
  primitives.
- **Competitor baselines**: 2-3 competitor sites for category norms,
  gap-filling only.

**Conflict capture:** every disagreement between sources gets logged and
becomes the `## Deviations` section at emit time. Don't merge silently.

## Normalization rules (every primitive, before emitting)

- **Colors**: hex sRGB, `#` prefix, uppercase, 6 digits. Convert
  HSL/OKLCH/RGB inputs on the way in.
- **Typography dimensions**: `rem` for `fontSize`/`lineHeight` (unitless
  multipliers allowed for `lineHeight`).
- **Spacing & rounded**: `px`, consistent within the file.
- **Font weights**: numeric (`400`, `700`), never named.
- **Letter spacing**: `em` preferred.

Recommended token names (Google's non-normative defaults): colors
`primary`, `secondary`, `tertiary`, `neutral`, `surface`, `on-surface`,
`error`; typography `headline-lg/md/sm`, `body-lg/md/sm`,
`label-lg/md/sm`; rounded `none/sm/md/lg/xl/full`; spacing on a
consistent 4px or 8px base scale. Avoid appearance-anchored names
(`red`, `blue`).

Token references use curly-brace dotted paths: `{colors.primary}`,
`{rounded.sm}`. Every brace path must resolve to a defined primitive
(composites allowed only inside `components`).

**Render-script compatibility:** `derive_css_from_design.py` and the PDF
pipeline read *flat* frontmatter keys — `colors.primary/secondary/
accent/text/surface/surface_variant` (underscore, not hyphen) and
`typography.display` / `typography.body` / `typography.mono` as plain
font-name strings. Emit those flat keys in the frontmatter alongside the
spec's nested typography scales, so one file serves the linter, the
render scripts, and downstream agents.

**Component variants — emit them, don't just describe them.** For every
interactive component, emit separate entries for the states the brand
actually uses (`button-primary` + `button-primary-hover`, `input-default`
+ `-focus`/`-error`). Each variant must carry a meaningfully different
value; omit identical-value placeholders. For states the spec can't
express (focus rings, transitions), emit what you know and document the
rest in an inline comment.

## Accessibility pass (before emitting)

1. Compute WCAG contrast for every `components.*` bg/text pair
   (resolving references). Threshold 4.5:1 body, 3:1 large text.
2. Failures are NOT silently patched — they become `## Do's and Don'ts`
   bullets with a suggested compliant pairing.
3. Missing required tokens get accessible fallbacks, visibly tagged:
   `error: "#B3261E"  # <!-- inferred: no error color in sources; AA-compliant baseline -->`
4. Flag any case where two semantic colors differ only by hue
   (success/error red↔green) — suggest pairing with icons or labels.

## Markdown body

Write it like a senior design lead briefing a new engineer. Pair
descriptive language with technical values; every named token earns its
name with a one-sentence reason.

Canonical section order (contiguous, no unknown sections interleaved):
**Overview** (2-4 sentences of design philosophy with evocative
pairings) → **Colors** (one bullet per token: what it's FOR, where it
never appears) → **Typography** (feeling terms + technical breakdown +
pairing rules) → **Layout** (grid, spacing base, max widths) →
**Elevation & Depth** (shadows vs tonal layers vs borders) → **Shapes**
(radius philosophy) → **Components** (brief; point to YAML; note
interaction nuance tokens can't carry) → **Do's and Don'ts** (concrete
imperatives incl. accessibility findings). `## Deviations` (only if
conflicts exist) goes after — one bullet per conflict, with the chosen
value and reason.

What NOT to include: voice/tone or copywriting guidance (that's the
voice guide's job — cross-link it at the top: `*Voice and copy guidance:
see the brand voice guide.*`); code snippets or Tailwind config.

Close the file with a provenance comment:
`<!-- generated by my-brand-skills-builder from sources: <list>; <ISO date> -->`

## Verification before declaring done

1. **Reference resolution**: every `{...}` in `components` points to a
   real primitive.
2. **Schema invariants**: frontmatter delimited by `---`; `name` present;
   hex colors 7-character; no duplicate `##` headings; canonical section
   order contiguous. (If `npx -y @google/design.md lint` is available,
   run it; otherwise hand-validate.)
3. **Five-line summary to the user**: Brand / Palette N colors / Type N
   families, N scales / Components N defined, N with variants /
   Deviations N, Inferred fallbacks N. If deviations or fallbacks exist,
   surface the specific items — they're the highest-judgment calls and
   the user should sanity-check them.

## Pitfalls

- Technical values in prose without a descriptive companion (and vice
  versa) — always pair them.
- Tokens with no functional role ("what is this FOR?").
- "Modern and clean" atmosphere descriptions — reach for evocative
  pairings an agent can use as a rubric.
- Ignoring subtle details: shadow strategy, label letter-spacing, 1.5 vs
  1.7 line-height — these separate *feels like the brand* from *looks
  like it*.
- Silently merging conflicting sources.
- Skipping the accessibility pass.
