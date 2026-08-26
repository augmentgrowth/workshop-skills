# Cobalt Design Tokens

The approved values for styling anything in Cobalt Service Partners' look. These are the single source of truth — use the exact values below, never an approximation.

*Source: Cobalt brand assets (Word/PowerPoint theme files, logo art) and cobaltsp.com production CSS, compiled 2026-08-21.*

---

## Color palette

| Role | Hex | Use it for |
|---|---|---|
| Primary — Cobalt Blue | `#0C64F7` | Headings and accents, links, buttons, active states, the hexagon mark |
| Deep blue — subheads | `#0649BB` | Word H3–H5 (accent1 at a 75% shade) |
| Dark — Navy ink | `#081E33` | Dark section backgrounds on web and decks, wordmark ink. **Web/deck only** — not Word body text |
| Secondary — Light Blue tint | `#C2D8FD` | Soft fills behind blue content, highlight bands |
| Accent — Bright Blue | `#3198FE` | Hover and secondary interactive states |
| Neutral — Slate gray | `#65727D` | Muted text, captions, footer links, rules (lighter step: `#A2ACB4`) |
| Neutral — Light gray | `#E8EAEC` | Panel fills, callout grounds, borders, dividers, wordmark on white |
| Ground — Cool gray | `#EEF2F5` | Light contrast bands on web, button text on cobalt fills |
| Background — White | `#FFFFFF` | Primary ground |

**Working rule.** White or navy `#081E33` grounds a web page or slide. `#0C64F7` carries emphasis — headings, links, buttons, active states. Grays support. Light-blue `#C2D8FD` fills sit behind blue content. Emphasis comes from the blue and from weight together.

**Word documents run on black.** Body text and top-level headings in a `.docx` are pure `#000000`. Navy is a web and deck ground color; Word's own theme dark is `#0E2841`. See `word-document-spec.md`.

**Cobalt's template names exactly four brand colors** — `#0C64F7`, `#C2D8FD`, `#E8EAEC`, `#A2ACB4`. Everything else here is a derived or web-only value.

**On navy/blue sections:** text is white or `#E8EAEC`; the site's card treatment is a glass fill of `rgba(255,255,255,0.05)` at 12px radius.

---

## Typography

| Use | Family | CSS fallback stack | Weights |
|---|---|---|---|
| Headings (h1–h4) | Neue Haas Grotesk Display | `"Neue Haas Grotesk Display", "Inter Tight", "Helvetica Neue", Arial, sans-serif` | 700 |
| Body | Inter / Inter Tight | `Inter, "Inter Tight", "Helvetica Neue", Arial, sans-serif` | 400 body, 700 bold |
| Monospace | Inconsolata | `Inconsolata, ui-monospace, monospace` | 400 |
| Word documents | Aptos ExtraBold (Title/H1/H2) / Aptos Display (H3–) / Aptos (body 11pt) | `Aptos, Calibri, sans-serif` | — |
| Presentations | Arial | `Arial, Helvetica, sans-serif` | — |

Neue Haas Grotesk is an Adobe Fonts license and will not be installed on most machines. The fallback stack above degrades correctly on its own — Inter Tight at 600–700 with `letter-spacing: -0.01em` on large headings is the closest free match. Always ship the full stack; never substitute a single unlicensed family name.

**Headings are large and bold (700). Weight is where Cobalt gets its presence.** Keep 400 only for oversized display lockups where the size alone carries it.

**Web heading scale.** h1 ≈ `clamp(3rem, 7vw, 7rem)` (about 112px on desktop), h2 ≈ 83px, h3 ≈ 40px, body 16–17px. The site's headlines are much larger than default editorial instinct suggests.

---

## Spacing, shape, and tone

- Confident, industrial-modern B2B. Generous whitespace on white; full-bleed cobalt-blue or navy sections for contrast blocks.
- Rounded corners are standard: **8px** on buttons and tabs, 12px on cards and panels.
- Iconography is simple line/flat, in white or cobalt blue.
- Body copy sits at a comfortable measure (roughly 65–75 characters); don't run text edge to edge.

**Buttons.** Primary is a `#0C64F7` fill with `#EEF2F5` text. Secondary is transparent with a 1px `#EEF2F5` border and `#EEF2F5` text. Both at 8px radius.

**Band rhythm.** Light pages alternate navy → cool gray `#EEF2F5` → navy → white, not navy → white over and over. The cool-gray step is what keeps a long page from reading as stripes.

**Two-tone headline device.** Cobalt's signature move: a hero headline splits mid-phrase, with the opening clause in white (or navy on a light band) and the payoff clause in `#0C64F7`. Use it on hero headlines. Title Case, no terminal period, on marketing-register pages; internal memos may keep sentence case.

**Lead paragraph.** A lead paragraph set beside a headline on a light band runs `#0C64F7`, not navy.

---

## Presentations

16:9. Keep the modern, airy layout — title slide on navy or cobalt with the white lockup, content slides on white. Do not import the dense house style of older internal decks.

- Cobalt's PowerPoint theme carries `#0B64F7` where the web carries `#0C64F7`. Either is acceptable in a deck; prefer `#0C64F7` for consistency across a mixed deliverable.
- Slide headings are bold navy on white. Blue is reserved for the takeaway or accent line.
- Shapes are square or lightly rounded, 8px maximum. Drop the 12px web radius in decks.
- Optional light chrome: a small lockup bottom-right on content slides, plus a page number. There is no dense-bullet mandate — one idea per slide still governs.

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

Cobalt brand assets — for use by Cobalt and its partner companies on Cobalt work. The marks belong to Cobalt; don't apply them to anything else.
