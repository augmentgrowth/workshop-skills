#!/usr/bin/env python3
"""Render a Brand-In-Action markdown source into a styled PDF.

Pandoc -> HTML body -> wrap in brand-aware CSS (variables from
derive_css_from_design.py output, plus the print-safe base layer
lifted from KidStrong's demo pipeline) -> Playwright PDF.

Usage:
  python build_pdf.py \
    --brand "Restore Hyper Wellness" \
    --md /path/to/brand_in_action.md \
    --vars-css /path/to/_brand_vars.css \
    --png-dir /path/to/03_Demos \
    --out /path/to/Restore_Brand_In_Action.pdf \
    --prepared-by "Augment Growth" \
    --prepared-for "Restore Marketing" \
    --date 2026-05-20 \
    --tagline "Body, mind, performance — restored."

Date defaults to today. Tagline is optional (cover lower-right text).
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import subprocess
import sys
from pathlib import Path

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.stderr.write(
        "Playwright required. Install with: pip install playwright && playwright install chromium\n"
    )
    sys.exit(2)


BASE_CSS = """
:root {
  --brand-primary: #4152EB;
  --brand-secondary: #59F97F;
  --brand-text: #000000;
  --brand-surface: #FFFFFF;
  --brand-surface-variant: #F5F8FB;
  --brand-font-display: 'Alumni Sans', system-ui, sans-serif;
  --brand-font-body: 'Inter', -apple-system, system-ui, sans-serif;
  --brand-font-mono: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
}

* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; background: var(--brand-surface); }
body {
  font-family: var(--brand-font-body);
  font-size: 11pt;
  line-height: 1.6;
  color: var(--brand-text);
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}

@page {
  size: Letter;
  margin: 0.6in 0.65in 0.55in;
}

/* COVER */
.cover {
  page-break-after: always;
  break-after: page;
  height: 9.6in;
  /* Flat-design brands: set --brand-cover-bg in the vars CSS (e.g. a solid
     var(--brand-primary)) to replace the default gradient — the sanctioned
     per-brand override; never edit this script for one brand. */
  background: var(--brand-cover-bg, linear-gradient(135deg, var(--brand-primary) 0%, var(--brand-secondary, var(--brand-primary)) 130%));
  color: #fff;
  padding: 0.9in 0.7in 0.7in;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  position: relative;
  margin: -0.6in -0.65in 0;
  width: calc(100% + 1.3in);
}
.cover-eyebrow {
  font-family: var(--brand-font-display);
  font-weight: 600;
  font-size: 9pt;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  opacity: 0.85;
}
.cover-headline {
  font-family: var(--brand-font-display);
  font-weight: 900;
  font-size: 70pt;
  line-height: 0.92;
  letter-spacing: -0.03em;
  text-transform: uppercase;
  margin: 30pt 0 24pt;
}
.cover-subhead {
  font-family: var(--brand-font-body);
  font-size: 14pt;
  line-height: 1.5;
  font-weight: 400;
  max-width: 5.2in;
  opacity: 0.95;
}
.cover-divider { width: 56pt; height: 4pt; background: #fff; margin: 36pt 0 24pt; }
.cover-meta {
  font-family: var(--brand-font-body);
  font-size: 9.5pt;
  opacity: 0.85;
  line-height: 1.6;
}
.cover-meta strong {
  font-family: var(--brand-font-display);
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-size: 8.5pt;
  display: block;
  opacity: 0.7;
  margin-bottom: 2pt;
}
.cover-footer {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  font-family: var(--brand-font-display);
  font-weight: 900;
  font-size: 13pt;
  letter-spacing: -0.02em;
  text-transform: uppercase;
}

/* H1 starts a new page — used as demo dividers */
h1 {
  font-family: var(--brand-font-display);
  font-weight: 900;
  font-size: 34pt;
  line-height: 1.0;
  letter-spacing: -0.025em;
  text-transform: uppercase;
  color: var(--brand-primary);
  margin: 0 0 8pt;
  page-break-before: always;
  break-before: page;
  page-break-after: avoid;
  break-after: avoid;
  padding-top: 4pt;
}
.cover + h1 { page-break-before: auto; break-before: auto; }

h2 {
  font-family: var(--brand-font-display);
  font-weight: 900;
  font-size: 18pt;
  line-height: 1.1;
  letter-spacing: -0.02em;
  text-transform: uppercase;
  color: var(--brand-text);
  margin: 22pt 0 8pt;
  page-break-after: avoid;
  break-after: avoid;
}

h3 {
  font-family: var(--brand-font-display);
  font-weight: 700;
  font-size: 12pt;
  letter-spacing: -0.005em;
  margin: 18pt 0 6pt;
  page-break-after: avoid;
  break-after: avoid;
}

p { margin: 0 0 10pt; }
strong { font-weight: 600; }
a { color: var(--brand-primary); text-decoration: underline; text-underline-offset: 2px; }

ul, ol { margin: 4pt 0 12pt 16pt; padding: 0 0 0 8pt; }
li { margin: 3pt 0; }

/* CALLOUT BLOCKQUOTES — voice "outputs" */
blockquote.callout {
  background: var(--brand-surface-variant);
  border-left: 4px solid var(--brand-primary);
  margin: 12pt 0;
  padding: 14pt 18pt 6pt;
  font-family: var(--brand-font-body);
  font-size: 10.5pt;
  line-height: 1.6;
  border-radius: 0 4pt 4pt 0;
  page-break-inside: avoid;
  break-inside: avoid;
}
blockquote.callout p { margin: 0 0 8pt; }
blockquote.callout p:last-child { margin-bottom: 0; }
blockquote.callout strong { font-family: var(--brand-font-display); }

/* CODE BLOCKS — "prompts" */
pre {
  /* themed from the brand: dark ground = brand text color, type = brand surface */
  background: var(--brand-text, #0F172A);
  color: var(--brand-surface, #E2E8F0);
  border-radius: 6pt;
  padding: 14pt 16pt;
  margin: 10pt 0 14pt;
  font-family: var(--brand-font-mono);
  font-size: 9pt;
  line-height: 1.55;
  white-space: pre-wrap;
  word-wrap: break-word;
  overflow-x: hidden;
  page-break-inside: auto;
  break-inside: auto;
}
pre code { background: none; color: inherit; padding: 0; font-size: inherit; }
code {
  font-family: var(--brand-font-mono);
  font-size: 9.5pt;
  background: var(--brand-surface-variant);
  padding: 1pt 4pt;
  border-radius: 3pt;
}

h2 + p, h3 + p { margin-top: 4pt; }

img {
  max-width: 100%;
  max-height: 8.2in;   /* keep full-page mockup screenshots on one page */
  height: auto;
  object-fit: contain;
  display: block;
  margin: 16pt auto;
  border-radius: 6pt;
  border: 1px solid #E0E0E0;
  page-break-inside: avoid;
  break-inside: avoid;
}

hr { border: 0; height: 1pt; background: #E5E7EB; margin: 22pt 0; }

@media print {
  body { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  pre, table { page-break-inside: auto; break-inside: auto; }
  blockquote.callout, img { page-break-inside: avoid; break-inside: avoid; }
  h1, h2, h3 { page-break-after: avoid; break-after: avoid; }
  h2 + *, h3 + * { page-break-before: avoid; break-before: avoid; }
}
"""


def pandoc_to_body(md_path: Path) -> str:
    """Run pandoc and extract the body content from the resulting HTML."""
    out_path = Path("/tmp/_brand_demo_body.html")
    subprocess.run(
        ["pandoc", str(md_path), "-f", "markdown", "-t", "html5", "--standalone", "-o", str(out_path)],
        check=True,
    )
    body = out_path.read_text(encoding="utf-8")
    body = re.sub(r'<header id="title-block-header">.*?</header>', "", body, flags=re.DOTALL)
    m = re.search(r"<body[^>]*>(.*)</body>", body, flags=re.DOTALL)
    if m:
        body = m.group(1)
    return body


def fix_html_for_pdf(body: str, png_dir: Path) -> str:
    """Apply the standard markdown-to-pdf compatibility fixes."""
    body = body.replace(
        'src="brand_showcase.png"',
        f'src="{(png_dir / "brand_showcase.png").as_uri()}"',
    )
    body = body.replace(
        'src="welcome_email.png"',
        f'src="{(png_dir / "welcome_email.png").as_uri()}"',
    )
    body = re.sub(r'<input\s+type="checkbox"\s*/?\s*>', "&#9744; ", body)
    body = re.sub(r"<hr\s*/?\s*>\s*(?=<h1)", "", body)
    body = body.replace("<blockquote>", '<blockquote class="callout">')
    body = re.sub(r"<h1[^>]*>\s*Brand in Action\s*</h1>", "", body)
    return body


def build_cover(brand: str, prepared_by: str, prepared_for: str, date: str, tagline: str) -> str:
    headline = brand.replace(" ", "<br/>")
    return f"""
<div class="cover">
  <div>
    <div class="cover-eyebrow">{brand.upper()} · BRAND PACKAGE · {date[:4]}</div>
    <div class="cover-headline">Brand<br/>in Action.</div>
    <div class="cover-subhead">Four demos. What the voice guide and design system you just received can actually produce — generated by Claude in a single prompt, no human rewriting.</div>
  </div>
  <div>
    <div class="cover-divider"></div>
    <div class="cover-meta">
      <strong>Prepared by</strong>{prepared_by}<br/>
      <strong style="margin-top:10pt;">For</strong>{prepared_for}<br/>
      <strong style="margin-top:10pt;">Date</strong>{date}
    </div>
    <div class="cover-footer" style="margin-top: 32pt;">
      <div>{brand.upper()}</div>
      <div style="font-family:var(--brand-font-body);font-weight:400;font-size:9pt;letter-spacing:0;text-transform:none;opacity:0.7;">{tagline}</div>
    </div>
  </div>
</div>
"""


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--brand", required=True)
    ap.add_argument("--md", required=True, type=Path, help="brand_in_action.md source")
    ap.add_argument("--vars-css", type=Path, help="brand-aware CSS variables partial from derive_css_from_design.py")
    ap.add_argument("--png-dir", required=True, type=Path, help="Directory containing brand_showcase.png + welcome_email.png")
    ap.add_argument("--out", required=True, type=Path, help="Output PDF path")
    ap.add_argument("--prepared-by", default="Augment Growth")
    ap.add_argument("--prepared-for", required=True)
    ap.add_argument("--date", default=dt.date.today().isoformat())
    ap.add_argument("--tagline", default="")
    args = ap.parse_args()

    if not args.md.is_file():
        sys.stderr.write(f"Markdown not found: {args.md}\n")
        return 1

    print("Stage 1: pandoc -> HTML body")
    body = pandoc_to_body(args.md)

    print("Stage 2: image rewrites + compatibility fixes")
    body = fix_html_for_pdf(body, args.png_dir)

    print("Stage 3: assemble styled HTML")
    cover = build_cover(args.brand, args.prepared_by, args.prepared_for, args.date, args.tagline)
    vars_css = args.vars_css.read_text(encoding="utf-8") if args.vars_css and args.vars_css.is_file() else ""
    # @import must precede all other rules; the :root overrides must FOLLOW the
    # base CSS so brand vars win the cascade. Split the partial accordingly.
    vars_imports = "\n".join(l for l in vars_css.splitlines() if l.lstrip().startswith("@import"))
    vars_rules = "\n".join(l for l in vars_css.splitlines() if not l.lstrip().startswith("@import"))

    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>{args.brand} — Brand in Action</title>
<style>{vars_imports}{BASE_CSS}{vars_rules}</style>  <!-- brand vars last so they override the base :root -->
</head>
<body>
{cover}
{body}
</body>
</html>
"""

    args.out.parent.mkdir(parents=True, exist_ok=True)
    html_intermediate = args.out.parent / f"_{args.out.stem}_styled.html"
    html_intermediate.write_text(html, encoding="utf-8")
    print(f"  styled HTML -> {html_intermediate}")

    print("Stage 4: Playwright render")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        ctx = browser.new_context(viewport={"width": 850, "height": 1100}, device_scale_factor=2)
        page = ctx.new_page()
        page.goto(html_intermediate.as_uri(), wait_until="networkidle")
        page.wait_for_timeout(2500)
        page.pdf(
            path=str(args.out),
            format="Letter",
            margin={"top": "0.6in", "bottom": "0.55in", "left": "0.65in", "right": "0.65in"},
            print_background=True,
            display_header_footer=True,
            header_template="<div></div>",
            footer_template=(
                '<div style="font-size:7pt;color:#94a3b8;width:100%;text-align:center;'
                "font-family:'Inter',sans-serif;padding:0 0.65in;display:flex;"
                'justify-content:space-between;">'
                f"<span>{args.brand} Brand in Action · {args.prepared_by}</span>"
                '<span class="pageNumber"></span></div>'
            ),
        )
        browser.close()

    print(f"PDF -> {args.out} ({args.out.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
