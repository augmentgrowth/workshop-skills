# Cobalt Design Tokens

The approved values for styling anything in Cobalt Service Partners' look. These are the single source of truth — use the exact values below, never an approximation.

*Source: Cobalt brand assets (Word/PowerPoint theme files, logo art) and cobaltsp.com production CSS, compiled 2026-08-21.*

---

## Color palette

| Role | Hex | Use it for |
|---|---|---|
| Primary — Cobalt Blue | `#0C64F7` | Headings and accents, links, buttons, active states, the hexagon mark |
| Dark — Navy ink | `#081E33` | Body text on light, dark section backgrounds, wordmark ink |
| Secondary — Light Blue tint | `#C2D8FD` | Soft fills behind blue content, highlight bands, table header rows |
| Accent — Bright Blue | `#3198FE` | Hover and secondary interactive states |
| Neutral — Slate gray | `#65727D` | Muted text, captions, footer links, rules (lighter step: `#A2ACB4`) |
| Neutral — Light gray | `#E8EAEC` | Panel fills, borders, dividers, wordmark on white |
| Background — White | `#FFFFFF` | Primary ground |

**Working rule.** White or navy `#081E33` grounds the page. `#0C64F7` carries emphasis — headings, links, buttons, active states. Grays support. Light-blue `#C2D8FD` fills sit behind blue content. Emphasis comes from the blue, not from heavy weights.

**On navy/blue sections:** text is white or `#E8EAEC`; the site's card treatment is a glass fill of `rgba(255,255,255,0.05)` at 12px radius.

---

## Typography

| Use | Family | CSS fallback stack | Weights |
|---|---|---|---|
| Headings (h1–h4) | Neue Haas Grotesk Display | `"Neue Haas Grotesk Display", "Inter Tight", "Helvetica Neue", Arial, sans-serif` | 300–400 |
| Body | Inter / Inter Tight | `Inter, "Inter Tight", "Helvetica Neue", Arial, sans-serif` | 400 body, 700 bold |
| Monospace | Inconsolata | `Inconsolata, ui-monospace, monospace` | 400 |
| Word documents | Aptos Display (headings) / Aptos (body) | `Aptos, Calibri, sans-serif` | — |
| Presentations | Arial | `Arial, Helvetica, sans-serif` | — |

Neue Haas Grotesk is an Adobe Fonts license and will not be installed on most machines. The fallback stack above degrades correctly on its own — Inter Tight at 400–500 with `letter-spacing: -0.01em` on large headings is the closest free match. Always ship the full stack; never substitute a single unlicensed family name.

Headings are large and plain-weight (400), not bold.

---

## Spacing, shape, and tone

- Confident, industrial-modern B2B. Generous whitespace on white; full-bleed cobalt-blue or navy sections for contrast blocks.
- Rounded corners are standard: 6px on buttons and tabs, 12px on cards and panels.
- Iconography is simple line/flat, in white or cobalt blue.
- Body copy sits at a comfortable measure (roughly 65–75 characters); don't run text edge to edge.

---

## Logo usage

Files ship in `assets/logos/`.

| File | What it is | Put it on |
|---|---|---|
| `LOGO_Cobalt_blue_full_dark.png` | Full lockup — blue hexagon, navy `COBALT` wordmark, blue `SERVICE PARTNERS` | Light backgrounds (white, light gray) |
| `LOGO_Cobalt_blue_full_lite.png` | Full lockup — blue hexagon, light-gray wordmark | Dark/navy backgrounds where the blue mark still reads |
| `LOGO_Cobalt_white_full.png` | Full lockup, all-white knockout | Cobalt blue, navy, or photography |
| `LOGO_Cobalt_blue_image_only.png` | Standalone hexagon mark, blue | Light backgrounds — favicons, avatars, small marks |
| `LOGO_Cobalt_white_image_only.png` | Standalone hexagon mark, white | Dark or cobalt-blue backgrounds |

**Rules.**

- Clear space: keep a margin equal to the height of the hexagon mark on all four sides. Nothing — text, rules, image edges — enters that zone.
- Minimum size: full lockup no smaller than 120px wide on screen (1.25in in print); standalone mark no smaller than 24px.
- Never recolor the hexagon outside cobalt blue `#0C64F7` or white.
- Never stretch, skew, rotate, add effects to, or reconstruct the lockup from parts. Scale proportionally only.
- Never place the blue lockup on a cobalt-blue field — use the white knockout there.

---

Cobalt brand assets — internal use by Cobalt and its portfolio companies; do not republish.
