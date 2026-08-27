#!/usr/bin/env python3
"""Derive a CSS variables partial from a design.md tokens file.

Reads the YAML frontmatter from a generate-design-md output and emits a
:root { --brand-primary: ... } block plus Google Fonts @import line for
the display + body typefaces. The partial is prepended to the base
markdown-to-pdf CSS so rendered PDFs are brand-themed automatically.

Usage:
  python derive_css_from_design.py --design path/to/design.md --out path/to/_brand_vars.css

Output: a single CSS file. Always-prefer-existing semantics: only emits
variables that exist in the frontmatter; downstream CSS uses fallbacks.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.stderr.write("PyYAML required. Install with: pip install pyyaml\n")
    sys.exit(2)


GOOGLE_FONT_URL = "https://fonts.googleapis.com/css2?family={family}:wght@400;500;600;700;900&display=swap"


def parse_frontmatter(md_path: Path) -> dict:
    """Extract YAML frontmatter from a markdown file. Returns {} if none."""
    text = md_path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return {}
    return yaml.safe_load(m.group(1)) or {}


def normalize_color(value: str) -> str:
    """Ensure a hex value has a leading #. Pass non-hex tokens through unchanged."""
    if not value:
        return value
    v = value.strip()
    if re.match(r"^[0-9A-Fa-f]{3,8}$", v):
        return f"#{v}"
    return v


def font_family_for_css(name: str) -> str:
    """Quote multi-word font names for CSS font-family declarations."""
    if not name:
        return name
    return f"'{name}'" if " " in name else name


def font_url_family(name: str) -> str:
    """Convert a font name to its Google Fonts URL family token (spaces -> +)."""
    return name.replace(" ", "+") if name else ""


def emit_css(tokens: dict) -> str:
    """Build the CSS partial from a flat dict of token keys."""
    colors = (tokens.get("colors") or {})
    typography = (tokens.get("typography") or {})

    primary = normalize_color(colors.get("primary") or "")
    secondary = normalize_color(colors.get("secondary") or "")
    accent = normalize_color(colors.get("accent") or "")
    text = normalize_color(colors.get("text") or colors.get("on_surface") or "")
    surface = normalize_color(colors.get("surface") or colors.get("background") or "")
    surface_variant = normalize_color(colors.get("surface_variant") or "")

    display = typography.get("display") or typography.get("heading") or ""
    body = typography.get("body") or typography.get("text") or ""
    mono = typography.get("mono") or typography.get("code") or "JetBrains Mono"

    families = [f for f in {display, body, mono} if f]
    font_imports = "\n".join(
        f"@import url('{GOOGLE_FONT_URL.format(family=font_url_family(f))}');"
        for f in families
    )

    vars_block = [":root {"]
    if primary:
        vars_block.append(f"  --brand-primary: {primary};")
    if secondary:
        vars_block.append(f"  --brand-secondary: {secondary};")
    if accent:
        vars_block.append(f"  --brand-accent: {accent};")
    if text:
        vars_block.append(f"  --brand-text: {text};")
    if surface:
        vars_block.append(f"  --brand-surface: {surface};")
    if surface_variant:
        vars_block.append(f"  --brand-surface-variant: {surface_variant};")
    if display:
        vars_block.append(f"  --brand-font-display: {font_family_for_css(display)}, system-ui, sans-serif;")
    if body:
        vars_block.append(f"  --brand-font-body: {font_family_for_css(body)}, -apple-system, system-ui, sans-serif;")
    if mono:
        vars_block.append(f"  --brand-font-mono: {font_family_for_css(mono)}, 'SF Mono', Menlo, monospace;")
    vars_block.append("}")

    return font_imports + "\n\n" + "\n".join(vars_block) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--design", required=True, type=Path, help="Path to design.md")
    ap.add_argument("--out", required=True, type=Path, help="Path to output _brand_vars.css")
    args = ap.parse_args()

    if not args.design.is_file():
        sys.stderr.write(f"design.md not found: {args.design}\n")
        return 1

    tokens = parse_frontmatter(args.design)
    if not tokens:
        sys.stderr.write(
            f"WARN: no YAML frontmatter found in {args.design}. "
            "Output CSS will be empty.\n"
        )

    css = emit_css(tokens)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(css, encoding="utf-8")
    print(f"Wrote {args.out} ({len(css)} bytes, {len(tokens.get('colors') or {})} colors)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
