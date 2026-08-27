# brand-contract.md — what the wrapped voice skill must declare

This is the contract between the orchestrator's validator and every wrapped
voice skill it scores. Every brand authors their own SKILL.md following this
spec. The validator never imposes rules the brand didn't declare.

This is the load-bearing principle: **brand-specific rules live in the
brand's wrapped voice skill, never in the orchestrator.** A new client never
inherits another client's quirks.

## Required frontmatter

```yaml
---
name: <brand-slug>-voice
version: x.y.z
description: |
  Write in <Brand>'s brand voice for any content type. Use when writing ad copy,
  social posts, website copy, email, landing pages, video scripts, or any marketing
  content for <Brand>.
  Triggers on: '<Brand>', '<brand-slug> copy', '<brand-slug> ad', ...
---
```

## Required body section: `## Non-negotiables`

The validator parses this section by header text — it must literally be
named "Non-negotiables" or "Non-Negotiables" (case-insensitive). Every rule
the validator can check is parsed out of this section. Other body sections
(channel cheat-sheet, generation protocol, etc.) are not parsed.

### Rule formats the validator recognizes

#### Forbidden vocabulary

Lines matching `**Never:** term1, term2, term3, ...`:

```markdown
- **Never:** modalities, customers, stores, ingredients, patients, participants
```

The validator scans every test output for these terms with word-boundary
matching. Case-insensitive.

#### Preferred vocabulary (informational, not validated)

```markdown
- **Use:** therapies, clients, studios, nutrients, Members
```

Informational. The validator doesn't check that you used these. Surface them
in your scoring rubric or rely on second-pass review for that.

#### Required phrases — TWO patterns

**Pattern A: Required every piece** (KidStrong-style — the affirmation closes
every output).

```markdown
- **Affirmation, exact format:** "I am Strong. I am Brave. I can DO THIS."
```

The validator looks for the literal "Affirmation" word + the phrase "exact
format" + "every piece" (or "closer when natural" or "close with") in the
non-negotiables section. If present, the affirmation must appear verbatim in
every test output. If absent in any output -> FAIL.

**Pattern B: Per-piece optional** (Restore-style — the tagline is available
but not mandatory).

```markdown
- **Tagline, exact format:** "Fuel Your Body. Feel the Results."
```

Use "Tagline" instead of "Affirmation", and do NOT include "every piece" or
"closer" in the surrounding context. The validator will detect this is
optional. The scorecard shows which outputs included it, but absence is not
a FAIL.

**Distinction reminder:** The validator chooses Pattern A vs Pattern B by
looking for the conjunction of (the word "Affirmation") AND (any of "every
piece", "closer when natural", "close with"). If both are present, it's
Pattern A. Otherwise it's Pattern B. This is intentional — KidStrong's voice
ritualizes the affirmation; Restore's tagline is a tool, not a closer.

#### Oxford comma policy

```markdown
- **No Oxford commas.** Every list of three+ items: drop the comma before the final "and"/"or".
```

If "No Oxford commas" appears in the non-negotiables, the validator checks
every test output for "X, Y, and Z" patterns (multi-word aware).

To opt out: omit the rule. Some brands tolerate Oxford commas.

#### Punctuation budget

The validator parses these patterns out of the section text:

| Pattern | What's parsed |
|---|---|
| `Max N exclamation points per [piece\|paragraph]` | exclamation cap |
| `<= N em dashes per piece` or `N em dash max` or `≤N em dashes` | em-dash cap |
| `No semicolons.` (literal line) | semicolon cap = 0 |

Defaults if not declared (permissive — does not impose KidStrong's tight caps):

| Rule | Default |
|---|---|
| em dashes | unlimited (informational count only) |
| exclamations | unlimited (informational count only) |
| semicolons | unlimited (informational count only) |

To enforce a cap, the brand explicitly declares it. To skip enforcement, the
brand omits the rule.

#### Pacing thresholds

Two numbers control pacing:
- `short_max` (words) — sentences below this count as "short punches"
- `long_min` (words) — sentences at-or-above this count as "long expansions"

The rule fires when the non-negotiables section contains all three of:
- `Pacing.` (literal heading word, period optional)
- `<X words` or `under X words` or `<= X words` — picks up `short_max`
- `Y+ words` or `>= Y words` — picks up `long_min`

Example (KidStrong, explicit thresholds):
```markdown
- **Pacing.** Mix short-punch sentences (under 8 words) with at least one longer expansion sentence (20+ words) per piece. Never flat, uniform lengths.
```

If the rule is not declared, the validator does NOT enforce pacing. (Earlier
v1.0.x of the orchestrator wrongly imposed KidStrong's 8/20 thresholds on
all brands — that's the bug this contract fixes.)

To declare pacing but with different thresholds:
```markdown
- **Pacing.** Mix short-punch sentences (under 12 words) with at least one longer expansion sentence (18+ words) per piece.
```

To opt out of pacing entirely: omit the rule. The validator skips the check.

#### Active voice, trademarks, capitalization

These are informational. The validator does not currently check active voice
or trademark inclusion programmatically. Second-pass review handles
those. Surface them in the non-negotiables for the wrapped skill to follow,
but don't expect regex scoring on them.

## Minimal viable wrapped voice skill

The shortest SKILL.md that the validator can score:

```yaml
---
name: <brand-slug>-voice
version: 1.0.0
description: Write in <Brand>'s brand voice. Triggers on: '<Brand>'.
---

# <Brand> Voice

## Non-negotiables

- **Never:** [list of forbidden terms]
```

This validates: no forbidden vocab in test outputs. Nothing else is checked
(no required phrase, no Oxford rule, no punctuation cap, no pacing
threshold). Add rules as the brand's voice tightens.

## Authoring a wrapped voice skill — checklist

When you build a new client's `<brand-slug>-voice/SKILL.md`:

- [ ] Frontmatter: `name`, `version`, `description` (with trigger keywords)
- [ ] `## Non-negotiables` section header (exact name, case-insensitive)
- [ ] `**Never:**` line with forbidden vocab
- [ ] `**Use:**` line with preferred vocab (informational)
- [ ] **EXACTLY ONE** signature-phrase rule (pick Pattern A *or* B, not both)
- [ ] If Oxford commas are forbidden: include the literal "No Oxford commas." rule
- [ ] If em dashes / exclamations / semicolons should be capped: declare explicit caps
- [ ] If pacing matters: declare both `short_max` and `long_min` in the rule text
- [ ] **`## Pre-flight check`** section — mandatory checklist the agent runs before every response (see "Required: Pre-flight + validator subagent" below)
- [ ] **`## Self-validation via subagent`** section — same-family validator pattern for runtimes that support subagents
- [ ] **Pattern-based drafting** in `## Generation protocol` — for pacing rules, bake in a 3-act rhythm (short punch → long expansion → short close) and instruct "Write the expansion sentence FIRST, then frame it." Include one worked example. For punctuation caps, instruct "draft 0 by default" not "draft 0–1." Models can't self-count reliably; patterns beat counts.
- [ ] **Split fail-handling** at the end of `## Pre-flight check` — hard fails (forbidden vocab, missing required phrase, semicolons, punctuation 2+ over cap, 2+ categories failing) → regenerate from scratch; soft fails (off-by-1 on pacing, 1 over an em-dash cap, single marginal miss) → ship + flag in chat reply (not in the output itself).
- [ ] Other channel-specific rules go in `references/channels.md` (the validator doesn't read them, but the wrapped skill's agent does)

## Required: Pre-flight + validator subagent

Every wrapped voice skill SKILL.md must include two sections so the skill is self-sufficient when handed off to clients (who won't have access to the orchestrator's validator).

### Section 1: `## Pre-flight check (run before EVERY response)`

A specific, agent-readable checklist organized by category (Vocabulary / Claims / Punctuation / Voice + structure). The agent reads this before responding and verifies each item.

**Why mandatory:** Pre-flight catches drift before output reaches the user. Works in every runtime — no subagent capability required. Costs nearly nothing in tokens.

**Format guidance:** Use `- [ ]` checkboxes. Group related rules. Make each item self-contained (the agent shouldn't need to look elsewhere to interpret the rule). Include count instructions for quantitative rules ("Em dashes: max 2 per piece. Count them.").

Close the section with a **split fail-handling rule** (this is mandatory — single-track regen-on-fail causes churn on marginal misses):

- **Hard fails — regenerate from scratch.** Any forbidden vocab, missing required phrase (Pattern A brands only), any semicolon, em-dashes 2+ over cap, exclamation points 1+ over their per-piece-or-paragraph cap, or 2+ different rule categories failing. Patches cascade — start over.
- **Soft fails — ship the draft + flag in chat reply (not in the output itself).** Off-by-1 on pacing (e.g., longest sentence is 19 words against a 20+ rule), em-dashes exactly 1 over cap, a single marginal miss on one quantitative rule, or a borderline judgment call on Title Case / capitalization. Tell the user in your chat reply: "Heads up — [specific miss]. Shipping as-is — reply if you want a rewrite."

Why split it: regen churn on a 19-word sentence is worse than a transparent flag. The model also drafts cleaner when it knows the edge isn't a cliff — pair this with the "Drafting headroom" generation-protocol step so the model targets 22–25 words on a 20+ rule rather than hitting 19 and failing.

### Section 2: `## Self-validation via subagent (when your runtime supports it)`

A pattern the agent follows when its runtime can spawn subagents. The validator subagent runs on the same LLM family as the primary generator.

**Why same-family:** Cross-family validation is noisier because each LLM family has slightly different conventions (emphasis markers, sentence rhythm, hedging patterns). Claude validates Claude. GPT validates GPT. Gemini validates Gemini.

**Required structure:**
1. **Step 1:** "Draft your response. Run the pre-flight check above."
2. **Step 2:** "Spawn a validator subagent" with a self-contained prompt that:
   - Names the brand
   - Lists every non-negotiable explicitly (the validator subagent has no memory)
   - Pastes the draft
   - Requests JSON output: `{"pass": bool, "fails": [{"rule": str, "evidence": str}]}`
3. **Step 3:** "If pass: ship. If fail: regenerate, re-validate. After 2 cycles, ship best draft + note remaining fails."
4. **Fallback:** "If runtime doesn't support subagents (Claude.ai chat, ChatGPT free tier, etc.), pre-flight is the only gate."

This pattern works in any subagent-capable runtime (Claude Code, Cowork, Anthropic Workbench with agents SDK, OpenAI Assistants with parallel runs, Gemini's agent toolkit). The skill describes the pattern; the runtime decides the specific mechanism.

## What this contract prevents

- **Cross-client rule bleed.** A pacing rule from KidStrong shouldn't accidentally fail Restore validation. The validator can't enforce rules the brand didn't author.
- **Orchestrator drift.** Future maintainers can't sneak a new "universal" rule into the orchestrator. New rules go into individual brand voice skills.
- **Brittle defaults.** Permissive defaults (no enforcement when unspecified) mean adding new brand types doesn't require validator changes.

## What this contract assumes

- Brand voice skills are produced by `voice-skill-builder` (or by hand following the same convention). The contract docs are the spec for both paths.
- The validator script is `scripts/validate_voice_skill.py` in this orchestrator. Updates to that script must preserve the parse semantics documented here, or this file is updated in lockstep.
- Second-pass review catches qualitative gaps that regex scoring can't. The contract is a floor, not a ceiling.

## Migration: existing wrapped voice skills

If you ship a brand and later find the wrapped skill doesn't declare a rule
that's failing validation, the fix is **always** to update the wrapped
skill's SKILL.md to declare the rule explicitly (or omit it intentionally).
**Never** patch the validator script with a brand-specific default.

Example self-anneal from the 2026-05-20 Restore run:
- Symptom: 5/6 prompts failed "missing affirmation"
- Wrong fix: lower the validator's affirmation threshold
- Right fix: detect Pattern A vs Pattern B in the parser; Restore's
  non-negotiable was Pattern B (tagline available, not mandatory)
- The Restore voice skill SKILL.md kept its "Tagline, exact format:" line.
  No change there. The validator changed to honor the brand's intent.

That's the principle in action.
