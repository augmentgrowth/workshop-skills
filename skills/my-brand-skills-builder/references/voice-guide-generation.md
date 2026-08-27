# voice-guide-generation.md — generating the brand voice guide

Inlined from the standalone brand-voice-guide-generator skill so this
orchestrator is self-contained. Produces the comprehensive voice guide
that Step 2 of bootstrap hands to `voice-skill-builder`.

## Step 1: Gather required information

Collect these inputs from the catalogued sources (ask the user only for
what the sources cannot answer):

1. **Company/brand description** - what the business does, mission, purpose
2. **Target audience** - who the brand speaks to (demographics, psychographics, role)
3. **Brand personality traits** - 3-5 adjectives (bold, approachable, authoritative, playful, ...)
4. **Competitive positioning** - how the brand differs from competitors
5. **Existing content samples** - pages or copy the user likes (optional)
6. **Content to avoid** - voice/tone that doesn't fit (optional)
7. **Core values or mission**

Clarifying questions that earn their place:
- "Is your audience B2B or B2C?"
- "Should the voice feel more like a trusted advisor or an innovative disruptor?"
- "Should technical expertise come through, or should complexity be simplified?"
- "What should people feel when reading your content?"

## Step 2: Generate the guide

Use `assets/brand_voice_template.md` as the foundation, customizing each
section with brand-specific content.

### Required sections

**1. Brand Voice Overview** — one-sentence voice summary; definitions of
each personality trait; voice vs. tone explanation (voice = consistent,
tone = adaptive to context).

**2. Voice Spectrum Analysis** — position the brand, with reasons, on:
Formal↔Casual, Serious↔Playful, Authoritative↔Collaborative,
Technical↔Simple, Traditional↔Innovative. See
`references/voice_spectrum_framework.md` for positioning guidance.

**3. Language Guidelines (parseable rules — load-bearing downstream)**

Use the exact formats below so `voice-skill-builder` and the validator
can lift them directly into the generated skill's `## Non-negotiables`
section. The formats are defined by `references/brand-contract.md`.

- **Forbidden vocab** — `**Never:** word1, word2, word3` (comma-separated,
  no Oxford comma). Include reasons inline only when non-obvious.
- **Preferred vocab** — `**Use:** word1, word2, word3`.
- **Signature phrases** — Pattern A (required every piece) or Pattern B
  (per-piece optional). Pattern A example: `Affirmation, exact format:
  "I am Strong. I am Brave. I can DO THIS." Closes every piece.` Pattern B
  example: `Tagline, exact format: "Fuel Your Body. Feel the Results."`
  Use the literal words "Affirmation" (Pattern A) or "Tagline" (Pattern B)
  so the parser detects intent.
- **Punctuation budget** — concrete caps in literal phrasing the parser
  recognizes: `Em dashes: max N per piece`; `Exclamation points: max N per
  paragraph` (or `per piece`); `No semicolons.` (literal line if forbidden;
  omit to allow).
- **Pacing thresholds** — if pacing matters, specify both ends AND the
  structural pattern: `Mix short-punch sentences (under X words) with at
  least one expansion sentence (Y+ words). 3-act rhythm: short punch →
  long expansion → short close. Write the expansion first, then frame it.`
  The pattern matters more than the numbers because models can't reliably
  self-count.
- **Oxford comma policy** — `No Oxford commas.` (literal line if forbidden;
  omit if tolerated).
- **Capitalization rules** — proper-noun and trademark requirements.
- **Active voice** — declare as `Active voice always.` if required.
- **Industry jargon rules** — when to use technical terms vs. simplify.
- **Sentence structure preferences** — short vs. long mix.

Each rule goes on its own bullet under `## Non-negotiables` in the final
guide so the downstream parser can scan them.

**4. Messaging Framework** — core value proposition (1-2 sentences), 3-5
key message pillars with proof points, tagline or positioning statement,
key differentiators. See `references/messaging_frameworks.md` for
framework options.

**5. Tone Variations by Channel** — website, social (per platform),
email, customer support, sales materials, technical docs if applicable.

**6. Writing Examples** — per major channel: a good example annotated, a
bad example with why it fails. At least 3-4 examples per major content
type. `references/brand_voice_examples.md` holds real-brand calibration
material.

**7. Common Scenarios** — announcing good news, addressing mistakes,
explaining complex concepts, asking for action, celebrating customer
success, responding to criticism.

**8. Quick Reference Guide** — one-page summary per
`assets/quick_reference_template.md`: voice elevator pitch, top 5 do's
and don'ts, most common tone mistakes.

## Step 3: Format

Clean markdown, hierarchical headers, table of contents, and the
frontmatter bootstrap Step 1 validates (`name`, `version`, `brand`).

## Best practices

- **Actionable over abstract.** Every guideline carries a specific,
  usable example. Show, don't just tell.
- **Authentic.** The voice should be sustainable, not aspirational
  costume. Test examples against real brand scenarios.
- **Self-service.** Someone unfamiliar with the brand should be able to
  write confidently from the guide alone.
- **Scannable.** Comprehensive but readable; nobody uses a guide they
  can't skim.

## Pitfalls

- Abstract descriptions ("be authentic") without concrete examples
- A voice that's aspirational but unsustainable
- Only do's, no don'ts
- So long nobody reads it
- Missing tone variations for different contexts
