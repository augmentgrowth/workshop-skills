# pdf-styling.md — brand-aware HTML + PDF rendering

How `derive_css_from_design.py` turns `design.md` into a brand-aware CSS
partial, and how the styled HTML masters become PDFs. HTML is the master
artifact; every PDF is a print of its HTML.

## The pipeline

```
design.md
  -> derive_css_from_design.py
  -> _brand_vars.css  (CSS variables + @import for fonts)
  -> merged with base CSS in build_pdf.py
     (font @imports go first; the brand :root overrides go AFTER the
      base CSS so they win the cascade)
  -> styled HTML
  -> Playwright PDF render
```

The base CSS uses `var(--brand-primary)`, `var(--brand-font-display)`,
etc. throughout. Overriding those four-to-six variables themes the
entire output without touching layout.

## What gets read from design.md

The script reads the YAML frontmatter and looks for:

```yaml
---
colors:
  primary: "#0066CC"      # required — drives headings, accents, cover gradient
  secondary: "#00A86B"    # optional — cover gradient secondary stop
  accent: "#FF6B35"       # optional — pull quotes, link hovers
  text: "#1A1A1A"         # optional — body copy (falls back to #000)
  surface: "#FFFFFF"      # optional — page background
  surface_variant: "#F5F5F5"  # optional — callout backgrounds
typography:
  display: "Alumni Sans"  # required — headings, cover headline
  body: "Inter"           # required — body copy
  mono: "JetBrains Mono"  # optional — code blocks
---
```

Field names support a few aliases (e.g., `text` or `on_surface`, `body`
or `text`) per the `generate-design-md` Google Labs spec. Missing
optional fields fall back to the base CSS defaults.

## Font loading

The script emits an `@import url('https://fonts.googleapis.com/...')`
line for each named font family. Playwright waits for `networkidle`
before rendering, so fonts have time to load.

If a brand uses a non-Google font (Helvetica, Proxima Nova, custom
license), the @import won't resolve. Two paths:

1. **Best:** load the font as a self-hosted `@font-face` data: URL
   inline in the CSS partial. The script doesn't do this automatically
   — you'd add it manually in maintenance mode.
2. **Good:** pick a Google Fonts stand-in that matches the brand font's
   genre — a woodblock display gets a heavy display stand-in, a
   typewriter face gets a mono/slab, never a generic `sans-serif` drop.
   Swap the family name in the CSS partial, verify the requested weights
   actually exist for that family (a weight axis the family doesn't ship
   makes Google Fonts drop it silently), and tell the user which
   stand-in was used.
3. **Acceptable:** let the system fallback take over. Surface to the
   user that the render uses a system fallback for that face.

## Page breaks and thin pages

`build_pdf.py` forces a page break at every h1, and the shipped
`brand_in_action.md.tmpl` opens with a short intro before its first h1 —
which strands that intro on a near-empty page for every brand unless you
act. Two sanctioned moves, both content-side (never edit the script):
give the intro page genuine substance (a "what's inside" summary), or
fold the intro into the first section. The same failure mode applies to
the self-authored HTML masters (voice guide, design spec): plan section
lengths so no forced break leaves a page mostly empty — the self-review
loop treats a mostly empty page as a defect.

## Cover gradient logic

The base CSS uses:
```
background: linear-gradient(135deg, var(--brand-primary) 0%, var(--brand-secondary, var(--brand-primary)) 130%);
```

If `--brand-secondary` is missing, the gradient degenerates to a flat
fill of primary. Usually fine; surface to operator if cover looks bland.

**Flat-design brands** (design.md forbids gradients): append
`--brand-cover-bg: var(--brand-primary);` (or any solid/treatment the
brand allows) to the `_brand_vars.css` partial — `build_pdf.py`'s cover
reads `--brand-cover-bg` before falling back to the gradient. This is
the sanctioned override; never edit the script per brand.

## Validating output

After rendering, eyeball the PDF for:
- Cover gradient using brand colors (not the base-CSS default blue->green)
- Headlines in the brand display font (not Alumni Sans by default)
- Body copy in the brand body font (not Inter by default)
- Callout blockquotes with brand-primary left border
- Inline links in brand primary color

If any of these are wrong, the `_brand_vars.css` file likely has gaps.
Cat the file:

```bash
cat /tmp/_<brand-slug>_brand_vars.css
```

Confirm the expected `--brand-*` variables are present. If a variable
is missing, check `02_Design_System/design.md` frontmatter — the field
either doesn't exist or has an unrecognized alias.

## Print-safe rules

The base CSS in `scripts/build_pdf.py` already includes these print-safe
rules:

- `-webkit-print-color-adjust: exact` everywhere (colors render)
- `page-break-inside: avoid` on callouts and images
- `page-break-after: avoid` on headings (no orphaned titles)
- `overflow-x: hidden; white-space: pre-wrap` on pre blocks (no scrollbars)
- Checkboxes replaced with Unicode box character

If a future client's design system needs different print rules (e.g.,
all pages landscape), edit `build_pdf.py` directly — these aren't
parameterized.

## When to skip the script

For the voice guide and design spec, author the styled standalone HTML
master directly: one self-contained file with a `<style>` block that
inlines the `_brand_vars.css` variables plus clean document CSS (and the
print-safe rules above). Then print it to PDF with headless Chrome:

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --disable-gpu \
  --print-to-pdf="<output>.pdf" --no-pdf-header-footer "<master>.html"
```

(Resolve the Chrome/Chromium binary for the current OS; if none exists,
fall back to the Playwright path inside `build_pdf.py`.) The HTML master
ships alongside the PDF — it is the browsable, zoomable original.

Full-bleed cover geometry gotcha: a negative-margin cover must be sized
to the full printable height or it leaves a white strip at the bottom
edge (with the default margins that's 9.85in, not 9.7in). The
render-inspect loop catches it; size the cover to the printable area up
front.

`build_pdf.py` is specifically for the `brand_in_action.pdf`, which
needs:
- Custom branded cover page
- Embedded PNG screenshots of the HTML mockups
- Demo dividers (h1 starts new page)
