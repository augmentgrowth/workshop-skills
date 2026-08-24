---
name: cobalt-voice
description: "This skill should be used when writing or rewriting content in Cobalt's voice, or for Cobalt audiences (business owners considering a sale, partner-company employees, customers, or the Cobalt team). Also use when a draft for Cobalt sounds AI-generated, corporate, or like private-equity marketing. Triggers on: 'write this for Cobalt', 'in Cobalt's voice', 'Cobalt tone', 'rewrite for Cobalt', 'owner-facing copy', 'partner company communication', 'Cobalt announcement', 'Cobalt email', 'Cobalt one-pager', 'sounds too corporate'."
# v1 (2026-08-21) — built from public cobaltsp.com copy + brand materials.
# The internal-document register is inferred, not evidenced. When a user with
# inside knowledge corrects a rule, treat their correction as authoritative and
# suggest they add it to references/voice-profile.md.
---

# Cobalt Voice

## Who this is

Cobalt Service Partners buys commercial access and security businesses and keeps them intact. It talks to owners who are afraid of what a sale will do to their people, and it answers that fear with specifics instead of reassurance. The posture is steward, not buyer. For a company backed by a private-equity firm, it is strikingly free of private-equity language.

Full profile, attribute by attribute, with the evidence behind each rule: **`references/voice-profile.md`**. Read it before drafting anything longer than a paragraph.
Calibration pairs showing the gap between generic copy and Cobalt's: **`references/examples.md`**.

## The five rules that carry most of the voice

1. **Open on the reader's problem.** Not on Cobalt's offer, model, or credentials.
2. **Define by negation.** The strongest Cobalt lines say what Cobalt will not do. "Amplifies, not dismantles." "Not numbers on a spreadsheet."
3. **Trade adjectives for operations.** Replace "comprehensive support" with the actual thing: dedicated technician recruiters in each market, a 45–60 day close, training hubs.
4. **Keep the craft in the sentence.** Technicians, doors, gates, customers, local teams. Never "human capital."
5. **Suppress finance vocabulary** in anything an owner, technician, or customer will read. "Partner company," always.

## Generation protocol

1. Gather the specifics first. Who is reading this, what do they already fear or doubt, and what concrete facts do you have? Vague input produces the generic version of this voice.
2. Name the reader's concern in the opening. If you cannot state it, you do not have the brief yet.
3. Answer it with a fact, a timeline, a named function, or a commitment stated in the negative.
4. Draft the long explanatory sentence first, then frame it with short ones. Cobalt's rhythm is a short claim, a longer sentence that does the work, then a short close.
5. Check channel fit. A press release, an owner letter, and a technician announcement carry the same reasoning in three different registers. See the format section in the profile.
6. Run the costume check: strip every Cobalt vocabulary marker. Does the thinking still sound like Cobalt — reader's fear first, specifics second, ownership framed as custody? If not, rethink the argument rather than restyling the words.

## Voice compass

- **Register.** Plainspoken and adult. Second person by default in owner, employee, and customer copy. Third person and no contractions in press releases.
- **Authority.** Established by specificity and by what Cobalt declines to do, never by superlatives about itself.
- **Emotion.** Warm but understated. Feeling is carried by other people's quotes, not by Cobalt's own adjectives.
- **Transitions.** Proximity and plain connectors. "That's because." "In short." "And."
- **Endings.** Land on a concrete commitment or hand the reader an open door to a conversation. Not a summary.
- **Structure.** Problem first, then the answer, then what it means for the reader specifically.

## Non-negotiables

- **Never:** portfolio company, target, acquiree, roll-up, platform play, synergies, EBITDA or multiples language in owner-, employee-, or customer-facing writing. Never "human capital," "leverage" as a verb, "world-class," "cutting-edge," "we're excited to announce."
- **Use:** partner company, long-term home, legacy, stewardship, local, behind the scenes, craft, do right by.
- **Required framing:** ownership is custody. Any sentence implying Cobalt extracts value from a business is wrong, whatever its wording.
- **Oxford comma:** yes.
- **Exclamation points:** zero in Cobalt's own voice. Permitted only inside a quoted person's words.
- **Punctuation budget:** draft zero em dashes. Add one only where the contrast genuinely earns it, as in "amplifies — not dismantles —". Never two in a paragraph. Semicolons: none in external copy.
- **Contractions:** on, except in press releases.

## Dead patterns

- Leading with Cobalt's own model, scale, or backing.
- Feature-list dumps of support services with no reader consequence attached.
- "We're excited to announce."
- Superlative stacking. ("Best-in-class" appears in Cobalt's real copy, so it is allowed once, never twice.)
- Naming or knocking competitors. Cobalt criticizes a practice, "financial engineering," never a firm.
- Summary paragraphs that restate the piece.
- Perfectly parallel three-item structures in every paragraph.

## AI tells to avoid

Em dash overuse. Colon-driven constructions ("Here's the thing:"). Semicolons in external copy. "Let's dive in," "It's worth noting," "At the end of the day." Every paragraph the same length. Consecutive paragraphs opening with the same structure. Hedging stacks.

Cobalt's real copy does use dashes, which makes over-dashing the easiest way to make Cobalt sound machine-written. Guard that one hardest.

## Pre-flight check (run before every response)

**Vocabulary.** No forbidden finance terms. "Partner company" used where relevant. No more than two or three Cobalt vocabulary markers in the whole piece.
**Claims.** Every support claim names a real function, timeline, or resource. No unbacked superlatives.
**Punctuation.** Em dashes: zero or one. Exclamation points: zero in Cobalt's voice. Semicolons: zero. Oxford commas present.
**Voice and structure.** Opens on the reader's concern. At least one commitment stated in the negative. Rhythm varies. Ending lands on something concrete.

**Hard fails** — forbidden vocabulary, Cobalt framed as an extractor, a semicolon or exclamation in external copy, two or more em dashes, or two categories failing: regenerate from scratch.
**Soft fails** — one marginal miss: ship it and flag in the reply, not in the output. "Heads up, the close is softer than Cobalt's usual. Reply if you want a rewrite."

## Self-validation via subagent (when the runtime supports it)

Dispatch a same-family validator subagent. Give it the full non-negotiables list verbatim, since it has no memory of this conversation, paste the draft, and ask for `{"pass": bool, "fails": [{"rule": str, "evidence": str}]}`. Where subagents are unavailable, the pre-flight check is the only gate.
