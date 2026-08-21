# Voice Skill Framework

Blueprint for generating voice skills for individuals or brands. Each section maps to a section in the output. Populate from analysis, interview, and calibration data.

Throughout this document, **"subject"** means the person or brand the voice skill is being built for. **"[Name]"** is a placeholder for the subject's name (a person's name or a brand name).

## Output Structure

Three files. All sections below describe what to generate and how to derive it from input.

### File 1: SKILL.md (Core Voice Identity)

#### Frontmatter

```yaml
---
name: [name]-voice
description: "This skill should be used when writing ANY content for [Name] or when output sounds AI-generated, too formal, or doesn't sound like [Name]. Triggers on: 'write a post', 'draft a newsletter', 'LinkedIn post', 'X post', 'write copy', 'email draft', 'write like [name]', 'write content', 'rewrite in [name]'s voice', 'brand copy', 'website copy', 'ad copy', 'support reply'."
---
```

#### Who This Is

2-3 sentences capturing the subject's energy, not their resume or mission statement. Third person. Focus on what makes them distinctive as a communicator.

Derive from voice identity analysis + user corrections from the interview.

**For individuals:**
Good: "A builder who thinks out loud. Processes decisions in real time and isn't afraid to show the seams."
Bad: "An experienced marketing professional with a passion for innovation."

**For brands:**
Good: "A company that talks to developers the way developers talk to each other. Specific, opinionated, occasionally irreverent. Treats its audience as peers, not prospects."
Bad: "An innovative technology company committed to empowering users with cutting-edge solutions."

#### Core Attributes

3-5 attributes. Each one needs three parts:

- **What it is.** Concrete description with quotes from the samples.
- **This is not.** The over-applied/costume version. This definition is critical for Opus. Without it, Opus latches onto the attribute and over-applies it. "Thinks out loud" without "This is not performing uncertainty" leads to hedges on every sentence. For brands, "challenger tone" without "This is not being contrarian for the sake of it" leads to every sentence picking a fight.
- **Generic vs [Name].** One pair showing the gap.

Derive from distinctive attributes analysis. Only include attributes that are genuinely unusual. "Clear communicator" is not an attribute. "Discovers conclusions while writing instead of declaring them upfront" is. For brands, "customer-centric" is not an attribute. "Explains complex features through the customer's workflow, not the product's architecture" is.

#### Thinking Architecture

How the subject processes and presents ideas. This section separates voice from costume.

**For individuals**, answer these from analysis:
- Do they start with conclusions or discover them?
- Do they resolve every thread or leave some open?
- Do they connect across domains?
- How do they handle uncertainty?

If discovery-mode thinker, include:
- "Start with what happened"
- "Find the thread (tension, not the obvious takeaway)"
- "Follow it (let writing discover where it's going)"
- "Leave threads unresolved when they are"

If thesis-first thinker, match their actual pattern. Not everyone thinks out loud. Some people are declarative and that's their voice.

**For brands**, the equivalent is editorial logic. How the brand reasons about its subject matter and audience:
- Does the brand lead with the customer's problem or its own solution?
- Does it educate first, then sell? Or is the value proposition upfront?
- Does it acknowledge tradeoffs and complexity, or simplify aggressively?
- Does it position against competitors explicitly, or just build its own case?

Capture the brand's reasoning pattern, not just its tonal wrapper. A brand that "thinks" by starting with the customer's pain point and walking them to the solution will produce fundamentally different content than one that leads with its own innovation, even if both sound "friendly and approachable."

#### Generation Protocol

Step-by-step for creating content. Always include these steps:

1. Gather raw material (specifics, context, brief if brand)
2. Find the genuine thread
3. Choose format-specific entry point
4. Draft in the subject's natural mode (discovery or thesis)
5. Run editing protocol

Always include the costume check: "Strip all voice markers. Does the thinking still sound like [Name]? If not, rethink, don't restyle."

For brands, also include: "Check channel fit. The same idea should sound different in a tweet vs. a landing page vs. a support reply, but the reasoning and values should be recognizable across all of them."

#### Voice Compass

Calibrate across these dimensions. Derive from sample analysis.

- **Register:** How they sound. One-sentence description.
- **Authority:** How they establish credibility. For individuals: work speaks, credentials, data, relationships. For brands: expertise, social proof, transparency, track record.
- **Emotion:** Default emotional register (understated, expressive, matter-of-fact). For brands, note whether emotion shifts by context (e.g., warmer in community, more restrained in product copy).
- **Transitions:** How they connect ideas (proximity, explicit connectors, key-word repetition).
- **Endings:** How they close (specific detail, open door, echo opening, call to action).
- **Structure:** How they organize (chronological, argument-first, discovery, problem-solution).

#### Dead Patterns

Structural patterns the subject naturally avoids. Common ones for individuals:
- Thesis-first (if they're a discovery writer)
- Setup-payoff symmetry
- Uniform paragraph weight
- Balanced rhetoric
- Summary endings

Common ones for brands:
- Feature-list dumps
- "We're excited to announce" openings
- Competitor bashing
- Vague superlatives ("best-in-class," "world-class")
- Hype without specifics

Only include patterns they actually avoid (visible in analysis by absence). Don't include all of these by default.

#### AI Tells

Always include this section in the generated skill. It defines the punctuation, structural, and phrasing habits that make output smell like AI rather than a human (or a brand with a human feel). The model should actively avoid these unless the subject's actual writing uses them.

**Punctuation tells.** These appear constantly in AI-generated text and rarely in natural human writing at the same frequency.
- Em dash overuse. AI writing leans on em dashes as a universal connector. Do not use em dashes unless the subject's samples contain them consistently. Use periods, commas, or parentheses instead.
- Colon-driven sentences. "Here's the thing: [explanation]" and "The answer is simple: [point]" are AI-native constructions. Replace with natural sentence flow.
- Semicolons in casual or mid-register writing. Real people rarely use semicolons outside of academic or legal contexts.
- Ellipsis for dramatic effect in professional writing.

**Structural tells.**
- Opening with a declaration followed by a colon-separated list.
- Perfectly balanced parallel structure in every paragraph.
- Three-item lists everywhere (the "rule of three" applied mechanically).
- Every section the same length. Human writing is asymmetric.
- Summary paragraphs that restate everything just said.

**Phrasing tells.**
- "Let's dive in," "Let's explore," "Let's break this down."
- "Here's the thing," "Here's why that matters."
- "It's worth noting that..."
- "At the end of the day..."
- Hedging stacks like "It's important to note that while..."
- Starting consecutive paragraphs with the same structure.

**How to use this section in the generated skill.** Include the AI tells that are most relevant given the subject's voice. If the subject writes formally, semicolons might not be a tell. The point is to define a "not this" list calibrated to the gap between AI defaults and the subject's natural patterns. Em dashes and colon-driven constructions stay on the list unless the subject's samples show genuine, consistent use of them.

The editing protocol (Pass 4) should reference this section when checking for AI tells in the output.

#### Grammar and Style

Mechanical rules derived from their writing:

- Punctuation habits (what they use, what they avoid)
- Contraction policy
- Fragment usage
- Sentence structure tendencies (short punches, long flowing, mixed)
- POV default
- Oxford comma preference
- Emoji policy

Be specific. "No em dashes" is better than "casual punctuation."

#### Natural Vocabulary

Words and phrases recurring in the samples. Categorize as:
- **Action** (verbs they gravitate toward)
- **Assessment** (how they evaluate things)
- **Thinking** (how they signal processing)
- **Transition** (how they connect thoughts)

For brands, also consider:
- **Identity** (words the brand uses to describe itself and its domain)
- **Audience** (how they refer to and address their users/customers)

Always include the anti-costume warning: "These are textures, not a checklist. If more than 2-3 vocabulary markers appear in a single piece, most are probably performing. This cap applies to word choice only, not punctuation."

#### Adapting to Format

How voice shifts by channel. Derive from samples across formats or interview.

For individuals: at minimum cover short-form, medium-form, long-form, professional. Describe the volume knob for each.

For brands: cover each channel the brand uses. Common dimensions to calibrate per channel:
- **Social (short-form):** How compressed can the voice get? Does personality increase or decrease at short lengths?
- **Website / landing pages:** Where does the voice sit between editorial and conversion copy?
- **Email:** Transactional vs. narrative. How much personality in operational communications?
- **Support / docs:** Does the brand voice soften here? How much personality in help content?
- **Ads / campaigns:** How far can the voice stretch for attention while staying recognizable?

The key question for brands: what stays constant across all channels (the non-negotiables), and what flexes?

#### Writing Craft

Core craft principles matching their style. Include only what's relevant:

- **Show Over Explain.** Use if their writing lets scenes carry points.
- **Density.** Use if their writing is tight and load-bearing.
- **Rhythm and Feel.** Always include (word choice by sound, sentence variation).
- **Sentence Craft.** Always include (end on strength, strong verbs, positive form).
- **Trust the Reader.** Use if their writing states what happened and lets the reader interpret.

#### Rule-Breaking Protocol

2-3 sanctioned breaks from their default patterns. These earn their place by contrast. Derive from moments in their writing where they break their own rules for effect.

Examples: a long rolling sentence in otherwise punchy prose, a moment of raw emotion in understated writing, an unexpected analogy that reframes the whole point.

#### Brand Non-Negotiables (required when subject is a brand)

Brand voice skills face higher operational stakes than individual ones — they get handed off to clients who run them across teams and channels without an Augment-side oversight loop. To stay consistent in that context, brand SKILL.md must include four additions beyond the individual blueprint. (These are also the spec enforced by `brand-design-system-builder`'s `brand-contract.md` validator when the brand ships through that orchestrator.)

1. **`## Non-negotiables` section** — explicit, parseable rules on their own bullets: forbidden vocab (`**Never:** ...`), preferred vocab (`**Use:** ...`), required phrases (signature affirmation/tagline with exact format), Oxford comma policy, punctuation budget (em-dash cap, exclamation cap, semicolons), pacing thresholds if relevant. Spec: `brand-design-system-builder/references/brand-contract.md` documents the exact parser syntax.

2. **Write to a pattern, not a count** (in Generation Protocol). Models can't reliably self-count after drafting — testing showed a model claim its longest sentence was 37 words when the actual was 19. Give the wrapped skill's generator a structural pattern, not a number to check after.
   - **For pacing rules** (e.g., "20+ words for the long sentence"): bake in a **3-act rhythm** — short punch → long expansion → short close. Instruct: "Write the expansion sentence FIRST, then frame it with short punches." Include one worked example in the SKILL.md showing what the expansion looks like for this brand's voice. The model needs a pattern to copy, not a number to hit.
   - **For punctuation caps** (e.g., "em-dash cap 1"): instruct "Draft 0 by default; add only if it earns its place." Don't say "draft 0–1" — say "draft 0." Asking for headroom on a 1-cap is asking for the cap.

   Edge-aiming and count-checking are the #1 causes of off-by-one fails. Pattern-writing beats count-checking.

3. **`## Pre-flight check (run before EVERY response)`** — an agent-readable checklist organized by category (Vocabulary / Claims / Punctuation / Voice + structure). The agent verifies each item before responding. Close with a **split fail-handling rule**:
   - **Hard fails** (forbidden vocab, missing required phrase, semicolons, punctuation 2+ over cap, 2+ categories failing) → regenerate from scratch.
   - **Soft fails** (off-by-1 on pacing, 1 over an em-dash cap, single marginal miss) → ship + flag in chat reply (not in the output): "Heads up — [specific miss]. Shipping as-is — reply if you want a rewrite."

4. **`## Self-validation via subagent (when your runtime supports it)`** — same-family validator pattern. Claude validates Claude, GPT validates GPT, Gemini validates Gemini. The validator subagent prompt must be self-contained (it has no memory), list every non-negotiable explicitly, paste the draft, and request JSON output `{"pass": bool, "fails": [{"rule": str, "evidence": str}]}`. Fallback when runtime doesn't support subagents (Claude.ai chat, ChatGPT free tier): pre-flight is the only gate.

These four exist because brand voice skills get used at scale by people who can't watch every output. The pre-flight + validator subagent are the client-side safety net that replaces the Augment-side Codex review.

### File 2: references/editing.md (Editing Protocol)

Generate a customized editing protocol. Start with these standard passes and adjust:

- **Pass 0: Costume Check.** Always include. Customize with the subject's specific voice markers to check. Include the acid test.
- **Pass 1: First-Line Test.** Delete opening sentence, check if piece improves.
- **Pass 2: Verb Pass.** Scan for weak verbs. Customize threshold to match their style (some writers use "was" naturally).
- **Pass 3: Punctuation Pass.** Customize to their specific rules. If they use em dashes, don't cut them.
- **Pass 4: Dead Pattern Pass.** Customize with their specific dead patterns. Include only the AI tells relevant to their voice.
- **Pass 5: "So What?" Pass.** Standard. Every paragraph earns its spot.
- **Pass 6: Header Pass.** Skip if they don't use headers. Otherwise, headers should be specific claims.
- **Pass 7: Conversational Shape Pass.** Asymmetry, list length, arrival order, posture checks. Adjust posture check to match their register.
- **Pass 8: Connection Pass.** Test transitions. Use their natural connective tissue, not generic ones.
- **Pass 9: Ending Test.** Three endings that work: land on specific, open a door, echo opening. For brands, CTA-based endings are also valid if that's their pattern.
- **Pass 10: Read-Aloud Test.** Trust the ear over the eye.

For brands, add:
- **Pass 11: Channel Fit Check.** Is this calibrated for the specific channel? A landing page shouldn't read like a tweet, and vice versa.
- **Pass 12: Brand Consistency Check.** Would someone who reads the brand's existing content recognize this as the same voice?

Key customizations:
- Pass 0 must reference THEIR specific vocabulary markers
- Pass 3 must match THEIR punctuation rules (not a universal standard)
- Pass 4 must flag THEIR specific dead patterns
- Pass 8 must use THEIR natural transition words

### File 3: references/examples.md (Calibration Examples)

Generate from the subject's actual writing. Four sections:

**Section 1: Voice Calibration (Generic AI vs [Name])**

5-8 pairs. For each, take a real thought from the samples and write the generic AI version of the same thought. The gap should be immediately obvious.

Derive from the best/most distinctive writing samples. Pick moments where the voice is strongest. For brands, include pairs across different content types (marketing copy, support, social) to show the voice holds across contexts.

**Section 2: Thinking (AI Declaration vs [Name]'s Approach)**

2-3 pairs showing how the subject arrives at insights vs how AI declares them. Focus on the reasoning process, not the style. Show the AI version announcing the insight ("The key takeaway is...") and the subject's version following its natural reasoning pattern to get there.

For brands, this might look like: AI version leads with "Our product is the best solution for X" while the brand version starts with the customer's problem and walks through why this approach matters.

**Section 3: Costume vs Natural**

2-3 pairs showing over-applied voice markers vs the same voice occurring naturally. The costume version hits every vocabulary marker. The natural version sounds like the subject because the THINKING is right, not because it uses the right words.

For brands, this is especially important. A costume version will cram the brand's buzzwords into every sentence, while the natural version uses brand vocabulary sparingly and lets the reasoning carry the identity.

**Section 4: Craft Examples**

3-5 before/after pairs from the samples showing specific craft principles. Openings, density, rhythm, endings. The "before" is a slightly genericized version. The "after" is the actual writing with annotation of what makes it work.

## Quality Criteria

The generated voice skill passes these tests:

1. **Calibration pair test.** Read a pair from examples.md. The gap between generic and [Name] should be immediately obvious.
2. **"This is not" test.** Each definition prevents a specific, realistic over-application that Opus would actually do.
3. **Thinking test.** The Thinking Architecture describes how they THINK or REASON, not just how they WRITE.
4. **Costume test.** Imagine stripping all voice markers from output. Would the thinking still be recognizable?
5. **Coffee-shop test.** Read any calibration output aloud. Sounds like a person talking (or a brand that sounds human)? Right. Sounds generated? The skill needs work.
6. **Cross-channel test (brands only).** Read outputs across two different channels. Do they sound like the same brand? If not, the Voice Compass or Adapting to Format section needs work.
