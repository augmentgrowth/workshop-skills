# Cobalt Word Document Spec

Measured from Cobalt's own Word template, `TEMPLATE - Cobalt Basic Word Document.dotx`. For any `.docx` output, this file outranks instinct and outranks the web conventions in `design-tokens.md` — the template is what Cobalt documents actually look like.

*Source: Cobalt Basic Word Document template, measured 2026-08-26.*

---

## Page

US Letter, portrait. Margins **0.65"** on all four sides. Header distance 0.35", footer distance 0.5".

---

## Type ramp

| Element | Spec |
|---|---|
| Title | Aptos ExtraBold 28pt, `#0C64F7`, letter-spacing −0.5pt, space after 0 |
| Subtitle | Aptos bold 10pt, black, ALL CAPS, space after 30pt |
| H1 | Aptos ExtraBold 18pt, **black**, dotted 0.5pt rule above, space before 30pt / after 4pt, line 1.5 |
| H2 | Aptos ExtraBold 14pt, **black**, space before 24pt |
| H3 | Aptos 14pt, `#0649BB` |
| H4 | Aptos italic 12pt, `#0649BB` |
| Body | Aptos 11pt, **black**, line 1.15, space after 12pt |

The subtitle follows a fixed pattern: **SUBTITLE – VERSION – DATE (MONTH YYYY)**.

The 30pt/24pt heading lead-ins are report-scale values. A one-page memo may compress them to roughly 14–18pt to hold the page — keep the ramp's proportions when you do.

**The family member is the fidelity lever.** Aptos ExtraBold carries Title, H1, and H2; Aptos Display sits at H3 and below; plain Aptos is the body. Substituting Aptos Display where ExtraBold belongs reads noticeably light and wrong, even though the family name matches.

Aptos ships with Microsoft 365, so no `altName` gymnastics are required on Cobalt machines. If the tooling emits `altName="Calibri"` fallbacks, leave them — they are harmless.

---

## Lists

**Bullets.** Square `▪` marker, indent 0.25" with 0.25" hanging. The lead-in phrase runs **bold `#0C64F7`**; the rest of the line is black.

**Numbered.** Decimal, bold numeral, same indents, space after 12pt.

---

## Callout

A single-cell table filled `#E8EAEC`, no borders, text indented 0.2" inside the cell. Heading is Aptos bold 12pt `#0C64F7`; body is 12pt black. No left rule — the fill alone carries it.

---

## Table

Header row fills `#0C64F7` with white bold 11pt text. Body rows fill `#E8EAED`. **All** borders are white — 0.5pt on the sides, 3pt on the bottom — so the cells read as separated tiles rather than a ruled grid.

---

## Logo

Full lockup, **top-right of the first content page, placed in the body** — 2.3" wide. Not a running header, and not repeated on later pages.

---

## Footer

Every page. Dotted 0.5pt rule above, right-aligned, two lines:

1. `COBALT SERVICE PARTNERS` in bold 8pt `#0C64F7` caps, followed by ` – <Doc Title> – <Version Date>` in bold 8pt black.
2. `Proprietary – Do not distribute without consent from Cobalt Service Partners, LLC` in italic 6pt `#A2ACB4`.

Page number sits at the far right, bold 10pt, centered in an `#E8EAEC` hexagon. A plain right-aligned page number is an acceptable simplification when the hexagon device is impractical in the tooling.

---

## Cover page (multi-page reports only)

Memos and one-pagers do not get a cover. Reports do:

- Full-bleed navy hexagon-network ground.
- White lockup, 2.75" wide, top-left.
- TITLE 33pt white caps. HEADLINE 16pt white bold. DATE 24pt `#A2ACB4` caps.
- Bottom-left, white: "Business Proprietary" and "Not for distribution without consent from Cobalt Service Partners, LLC".
- The cover is unnumbered.

---

## Brand colors named by the template

Cobalt's own theme names exactly four: `#0C64F7`, `#C2D8FD`, `#E8EAEC`, `#A2ACB4`. Deep blue `#0649BB` (accent1 at a 75% shade) carries H3–H5. Word's theme dark is `#0E2841`, not the web navy.
