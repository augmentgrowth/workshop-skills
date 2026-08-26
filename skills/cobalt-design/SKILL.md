---
name: cobalt-design
description: Applies Cobalt Service Partners' approved brand system — colors, typography, logo usage — to documents, presentations, HTML pages, and other designed outputs. Use whenever the user asks for Cobalt-branded, styled, on-brand, polished, or client-ready work.
---

# Cobalt Design

Cobalt brand assets — for use by Cobalt and its partner companies on Cobalt work. The marks belong to Cobalt; don't apply them to anything else.

## When to apply

Any output someone outside your own notes will look at: a memo or one-pager, a deck or deck outline, an HTML page or export, a report, a template. If the user says "make this look right," "client-ready," "on-brand," or names Cobalt, this applies.

Not for internal scratch notes, code, or plain-text chat answers.

## First step, always

**Read `references/design-tokens.md`.** It holds every color, font stack, logo file, and usage rule. This file deliberately does not repeat those values — the tokens file is the single source of truth, so read it before you style anything.

If the output is a Word document, read **`references/word-document-spec.md`** as well. It is measured from Cobalt's own template and outranks both this file and the web conventions in the tokens file.

## Procedure by output type

**Word document (.docx).** Follow `references/word-document-spec.md` exactly — page setup, type ramp, callout, table, footer, cover. Two rules there override instinct, and both get broken constantly:

- **Top-level headings are black Aptos ExtraBold, not blue.** Blue belongs to the title, H3 and below, bullet lead-in phrases, and table header rows. A document with blue H1s is not a Cobalt document.
- **The logo goes top-right of the first content page, in the body.** Not a repeating running header, not on later pages.

Every page carries the proprietary footer line. Before building, settle three things — the document title, the version/date string for the subtitle and footer, and whether this is a memo (no cover) or a multi-page report (cover). If the user did not give them, invent plausible ones and say so at the end.

**Markdown document with a styled export.** Write the content as clean markdown first — content decisions before styling. Then produce a standalone HTML file that carries the brand: a `<style>` block defining the palette as CSS custom properties, the heading and body font stacks from the tokens file, and the logo at the top-left of the first page. Reference logos by relative path into `assets/logos/`, or base64-embed them if the file must travel alone. Print-friendly: white ground, navy body text, blue headings.

**HTML page.** Same palette and type as above. Use full-bleed navy or cobalt sections as contrast blocks, following the band rhythm in the tokens file. Rounded corners and card treatments per the tokens file. Keep it responsive and give the page an explicit background color rather than inheriting one.

Give the hero an anchor. A bare full-width navy band of type reads under-designed next to cobaltsp.com. When no illustration is available, ground the hero with a radial cobalt glow — `radial-gradient` from `#0C64F7` at low alpha — or a simple hexagon line-art motif.

**Presentation or deck outline.** Title slide on cobalt blue or navy with the white lockup; content slides on white with the blue-on-light lockup small in a corner. One idea per slide. Headings bold navy on white, blue reserved for the takeaway line. Use the presentation font row and the presentation section in the tokens file, not the web row.

## Look at what you made

**Mandatory for every visual output.** After generating, render the artifact — PDF, image, or a browser screenshot — and look at the render yourself. Check for overlap, overflow, crowding, dead space, substituted or wrong fonts, low contrast, and page-count spill. Fix what you find, re-render, and look again.

Do not declare the work done from the source code. Only from the render.

## Logo selection

Blue lockup on light backgrounds. White lockup on dark, navy, cobalt, or photographic backgrounds. Standalone hexagon mark when the space is small or square — favicon, avatar, slide corner. Honor the clear-space and minimum-size rules in the tokens file; when in doubt, give it more room.

## Do not

- **Do not approximate colors.** Use the exact hex values. No "close enough" blue, no CSS named colors, no palette generated from a screenshot.
- **Do not distort logos.** No stretching, skewing, rotating, recoloring, drop shadows, or rebuilding the lockup from parts. Scale proportionally.
- **Do not invent missing brand values.** If you need something the tokens file doesn't define — a chart palette, an email signature spec, a specific icon — ask rather than guessing. A plausible invention becomes an unapproved brand asset the moment it ships.
- **Do not leave placeholders in content.** No `[Name]`, no `[DATE]`, no blank lines waiting to be filled. Invent plausible specifics — dates, names, numbers, email addresses — so the draft reads as a finished document, then list what you invented when you hand it over. A bracket in a client-ready file is worse than a wrong guess the user can correct.
- **Do not use navy for Word body text or Word headings.** Word runs on black. Navy is web and deck.
- **Do not use `#C2D8FD` as a panel ground.** Callouts and panels are `#E8EAEC`. Light blue sits behind blue content, not under body copy.
- **Do not omit the proprietary footer line** from a Cobalt document. Every page carries it.
- **Do not include client-confidential source material** (Word templates, internal decks) in anything you produce or hand off.

## Fonts degrade on purpose

Neue Haas Grotesk Display is licensed through Adobe Fonts and will not be installed on most machines — workshop attendees and recipients included. Always write the complete fallback stack from the tokens file rather than the family name alone. The stack is chosen so the output still reads as Cobalt when the brand font is absent; that is expected behavior, not a defect to work around.
