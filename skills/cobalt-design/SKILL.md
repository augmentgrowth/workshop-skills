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

## Procedure by output type

**Markdown document with a styled export.** Write the content as clean markdown first — content decisions before styling. Then produce a standalone HTML file that carries the brand: a `<style>` block defining the palette as CSS custom properties, the heading and body font stacks from the tokens file, and the logo at the top-left of the first page. Reference logos by relative path into `assets/logos/`, or base64-embed them if the file must travel alone. Print-friendly: white ground, navy body text, blue headings.

**HTML page.** Same palette and type as above. Use full-bleed navy or cobalt sections as contrast blocks between white ones. Rounded corners and card treatments per the tokens file. Keep it responsive and give the page an explicit background color rather than inheriting one.

**Presentation or deck outline.** Title slide on cobalt blue or navy with the white lockup; content slides on white with the blue-on-light lockup small in a corner. One idea per slide, headline in blue, supporting text in navy. Use the presentation font row in the tokens file, not the web row.

## Logo selection

Blue lockup on light backgrounds. White lockup on dark, navy, cobalt, or photographic backgrounds. Standalone hexagon mark when the space is small or square — favicon, avatar, slide corner. Honor the clear-space and minimum-size rules in the tokens file; when in doubt, give it more room.

## Do not

- **Do not approximate colors.** Use the exact hex values. No "close enough" blue, no CSS named colors, no palette generated from a screenshot.
- **Do not distort logos.** No stretching, skewing, rotating, recoloring, drop shadows, or rebuilding the lockup from parts. Scale proportionally.
- **Do not invent missing values.** If you need something the tokens file doesn't define — a chart palette, an email signature spec, a specific icon — ask rather than guessing. A plausible invention becomes an unapproved brand asset the moment it ships.
- **Do not include client-confidential source material** (Word templates, internal decks) in anything you produce or hand off.

## Fonts degrade on purpose

Neue Haas Grotesk Display is licensed through Adobe Fonts and will not be installed on most machines — workshop attendees and recipients included. Always write the complete fallback stack from the tokens file rather than the family name alone. The stack is chosen so the output still reads as Cobalt when the brand font is absent; that is expected behavior, not a defect to work around.
