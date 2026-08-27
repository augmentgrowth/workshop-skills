#!/usr/bin/env python3
"""Screenshot HTML demo mockups via Playwright for PDF embedding.

Reads brand_showcase.html and welcome_email.html from a 03_Demos directory
and writes full-page PNG screenshots next to them (or to --out-dir if given).
Lifted from the KidStrong vault snapshot and parameterized.

Usage:
  python build_screenshots.py \
    --html-dir /path/to/03_Demos \
    --out-dir /path/to/output

If --out-dir is omitted, PNGs land alongside the HTML.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.stderr.write(
        "Playwright required. Install with: pip install playwright && playwright install chromium\n"
    )
    sys.exit(2)


TARGETS = [
    {
        "html": "brand_showcase.html",
        "png": "brand_showcase.png",
        "viewport": {"width": 1280, "height": 800},
        "device_scale_factor": 2,
        "full_page": True,
    },
    {
        "html": "welcome_email.html",
        "png": "welcome_email.png",
        "viewport": {"width": 880, "height": 800},
        "device_scale_factor": 2,
        "full_page": True,
    },
]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--html-dir", required=True, type=Path, help="Directory containing the HTML mockups")
    ap.add_argument("--out-dir", type=Path, help="Output PNG directory (default: same as --html-dir)")
    args = ap.parse_args()

    out_dir = args.out_dir or args.html_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    if not args.html_dir.is_dir():
        sys.stderr.write(f"HTML directory not found: {args.html_dir}\n")
        return 1

    with sync_playwright() as p:
        browser = p.chromium.launch()
        for t in TARGETS:
            html_path = args.html_dir / t["html"]
            if not html_path.is_file():
                sys.stderr.write(f"WARN: skipping missing file {html_path}\n")
                continue
            ctx = browser.new_context(
                viewport=t["viewport"],
                device_scale_factor=t["device_scale_factor"],
            )
            page = ctx.new_page()
            print(f"Loading {t['html']}")
            page.goto(html_path.as_uri(), wait_until="networkidle")
            page.wait_for_timeout(1500)  # let webfonts settle
            out = out_dir / t["png"]
            page.screenshot(path=str(out), full_page=t["full_page"])
            print(f"Wrote {out} ({out.stat().st_size // 1024} KB)")
            ctx.close()
        browser.close()

    print("Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
