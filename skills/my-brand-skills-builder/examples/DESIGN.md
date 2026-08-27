---
version: alpha
name: Furniture Collections
description: Sophisticated minimalist sanctuary — Scandinavian simplicity meets luxury editorial. Gallery-like, photography-first, generous whitespace.
colors:
  primary: "#294056"
  surface: "#FCFAFA"
  surface-variant: "#F5F5F5"
  on-surface: "#2C2C2C"
  on-surface-variant: "#6B6B6B"
  outline: "#E0E0E0"
  success: "#10B981"
  warning: "#F59E0B"  # <!-- inferred: no warning state in sources; Tailwind amber-500, AA-compliant on surface -->
  error: "#EF4444"
  info: "#64748B"
typography:
  headline-display:
    fontFamily: "Manrope"
    fontSize: 3rem
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: 0.02em
  headline-lg:
    fontFamily: "Manrope"
    fontSize: 2rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.01em
  headline-md:
    fontFamily: "Manrope"
    fontSize: 1.5rem
    fontWeight: 500
    lineHeight: 1.3
  body-lg:
    fontFamily: "Manrope"
    fontSize: 1.125rem
    fontWeight: 400
    lineHeight: 1.7
  body-md:
    fontFamily: "Manrope"
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.7
  body-sm:
    fontFamily: "Manrope"
    fontSize: 0.875rem
    fontWeight: 400
    lineHeight: 1.5
  label-md:
    fontFamily: "Manrope"
    fontSize: 1rem
    fontWeight: 500
    letterSpacing: 0.01em
  label-sm:
    fontFamily: "Manrope"
    fontSize: 0.75rem
    fontWeight: 500
    letterSpacing: 0.06em
rounded:
  none: 0px
  sm: 4px
  md: 8px
  lg: 12px
  full: 9999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  2xl: 48px
  3xl: 80px
  4xl: 128px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.surface}"
    typography: "{typography.label-md}"
    rounded: "{rounded.md}"
    padding: 14px 32px
  button-primary-hover:
    backgroundColor: "#1F3142"   # ≈10% L* darken of primary
    textColor: "{colors.surface}"
    typography: "{typography.label-md}"
    rounded: "{rounded.md}"
    padding: 14px 32px
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    typography: "{typography.label-md}"
    rounded: "{rounded.md}"
    padding: 14px 32px
  card-product:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
  card-product-hover:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
    # translateY(-4px) + 0 2px 8px rgba(0,0,0,0.06) — motion not first-class in spec
  input-default:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.md}"
    padding: 14px 20px
  input-default-focus:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.md}"
    padding: 14px 20px
    # border shifts from outline to colors.primary; ring not first-class in spec
  nav-link:
    textColor: "{colors.on-surface}"
    typography: "{typography.label-sm}"
---

*Voice and copy guidance: see [./brand/voice-profile.md](./voice-profile.md).*

## Overview

Furniture Collections embodies a **sophisticated minimalist sanctuary** — Scandinavian restraint marries luxury editorial gravitas. The interface feels **spacious and tranquil**, gallery-like and photography-first, letting each furniture piece command attention as an art object. The mood is **airy yet grounded**, aspirational but approachable. Every element earns its place; nothing competes for attention. The aesthetic evokes a high-end showroom where browsing is contemplative rather than transactional.

## Colors

- **Primary (#294056):** "Deep Muted Teal-Navy" — sole vibrant anchor. Used exclusively for primary CTAs, active navigation, selected states, and focused inputs. Never decorative; always functional. Restrict to one primary CTA per screen.
- **Surface (#FCFAFA):** "Warm Barely-There Cream" — the canvas. Imperceptibly warmer than pure white, making the experience inviting rather than clinical.
- **Surface-variant (#F5F5F5):** "Crisp Very Light Gray" — secondary surface for card backgrounds and stacked content. Provides separation without visual weight.
- **On-surface (#2C2C2C):** "Charcoal Near-Black" — primary text for headlines and product names. Softer and more refined than pure black; reads as confident, not severe.
- **On-surface-variant (#6B6B6B):** "Soft Warm Gray" — body copy, descriptions, supporting metadata. Clear hierarchy without harsh contrast.
- **Outline (#E0E0E0):** "Ultra-Soft Silver Gray" — borders, dividers, structural lines. Separation so gentle it nearly dissolves.
- **Success (#10B981) / Warning (#F59E0B) / Error (#EF4444) / Info (#64748B):** functional states reserved for system feedback — confirmations, low-stock warnings, errors, neutral notices. Warning is inferred (no source value provided); Tailwind amber-500 chosen for AA contrast on surface.

## Typography

**Manrope** is the sole family — a modern geometric sans-serif with gentle humanist warmth. Slightly rounded letterforms feel contemporary yet approachable. The system speaks in one voice across the entire experience.

- **Display & headlines:** 600 weight at 2–3rem with expanded letter-spacing (0.01–0.02em). Used sparingly for hero sections and primary page titles — sparingly is the operative word. Generosity of whitespace is the headline, not size.
- **Body:** 400 weight at 1rem, **line-height 1.7** for effortless long-form reading. Generous leading is non-negotiable here — it carries the brand's "tranquil sanctuary" register more than any single color choice.
- **Labels & UI affordances:** 500 weight. CTA buttons use `label-md` (1rem, subtle 0.01em letter-spacing). Navigation uses `label-sm` with **0.06em letter-spacing and subtle uppercase** — refined sophistication, not shouting.
- **Pairing:** there is no second family. A single typeface across the entire system is part of the brand statement.

## Layout

A **responsive 12-column grid** with fluid gutters (24px mobile, 32px desktop). Max content width is **1440px** for visual balance on large displays. The product grid scales 4 → 3 → 2 → 1 columns from large desktop down to mobile.

- **Spacing base unit:** 8px. Micro-spacing uses 4px (xs). Component-internal spacing uses 16px (md). Section breathing room is **generous to dramatic** — 80–128px (3xl–4xl) between major sections is intentional, not excess.
- **Edge padding:** 24px mobile, 48px tablet/desktop — the page never hugs the device edge.
- **Hero sections:** extra-generous vertical padding (128px+) sets the contemplative pace immediately.
- **Image-to-text ratio:** weighted ~70/30 toward imagery — photography-first is system-level, not optional per page.

## Elevation & Depth

**Flat by default. Whisper-soft on interaction.**

Depth comes from tonal layering and gentle hover-state shadows, not stacked elevation. Cards rest flat on the surface. On hover, a barely-there diffused shadow appears — `0 2px 8px rgba(0,0,0,0.06)` — and the card lifts 4px. That's the only shadow vocabulary in the system. There are no "elevated" or "modal" shadow tiers; modals use a full-screen scrim instead.

When shadows aren't present, a single 1px outline-color hairline carries the same definitional weight.

## Shapes

**Subtly rounded, never playful.**

- **Buttons & inputs:** 8px radius (`rounded.md`) — approachable, modern, adult.
- **Cards & containers:** 12px radius (`rounded.lg`) — softer for content blocks that hold imagery.
- **Avatars & badges:** full-pill (`rounded.full`) — the only fully-rounded shapes in the system.

Sharp 0px corners are reserved for full-bleed imagery (which is borderless anyway). Mixing sharpness and softness in the same view breaks the system.

## Components

YAML defines token values for `button-primary`, `button-secondary`, `card-product`, `input-default`, and `nav-link`. Notes on interaction states not expressible in tokens:

- **Button hover:** primary darkens to roughly #1F3142 (≈10% L*); transitions 250ms ease-in-out.
- **Button focus:** soft outer glow in `colors.primary` at 30% opacity — keyboard-navigation accessibility, never optional.
- **Card hover:** translateY(-4px) combined with the whisper-soft shadow described in Elevation.
- **Input focus:** border shifts from `outline` to `primary`; subtle outer glow matches button focus.
- **Nav active:** 2px underline in `primary`; 200ms color transition on hover.

## Do's and Don'ts

- **Do** restrict the primary color to a single CTA per screen. The whole palette is built around it earning attention.
- **Do** maintain 1.7 line-height in body copy — it's load-bearing for the "tranquil sanctuary" register.
- **Do** use descriptive token names in handoff conversations ("Boston Clay," "Warm Barely-There Cream") so designers and engineers share vocabulary.
- **Don't** mix shapes — pairing 0px corners with 12px corners in the same view fights the system.
- **Don't** layer multiple shadow elevations. This system uses tonal layering plus one hover-shadow; that's the whole vocabulary.
- **Don't** introduce a second font family. Manrope is the brand statement.
- **Don't** rely on color alone to differentiate `success` (green) and `error` (red) — pair with iconography or text labels for color-blind users.
- **Don't** pair `on-surface-variant` (#6B6B6B) with `surface-variant` (#F5F5F5) for body text. Contrast is 4.4:1 — just under WCAG AA. Use `on-surface` (#2C2C2C) on `surface-variant` instead (12.6:1).

## Deviations

- **`colors.primary`**: brand guide PDF specifies #2B4258, production site renders #294056 (≈4 unit ΔE). Used **#294056** (production reality) — the 2026 refresh tightened the original navy spec and brand guide hasn't been updated yet. Flag for next brand-doc revision.
- **`spacing.4xl` (hero padding)**: brand guide silent on hero-specific spacing; production site uses 128px consistently across 12 crawled pages. Used **128px** (`reality` lane, no `intent` to override).

<!-- generated by generate-design-md from sources: https://furniturecollections.example.com (firecrawl branding), brand-guide-2024-v3.pdf, instagram.com/furniturecollections; 2026-05-16 -->
