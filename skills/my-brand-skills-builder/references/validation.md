# validation.md — assertion-based scoring + second-pass review

Goal: catch voice drift before the skill ships. Pattern proven across
several real brand packages (KidStrong and Restore appear below as worked
examples).

## Why two passes

Regex assertions catch the deterministic stuff (forbidden vocab,
required phrases, punctuation budget). They miss:

- Multi-word Oxford commas ("character, body, and brain" — KidStrong's
  original single-word regex missed this)
- Vague hype without proof ("most kids forget the iPad exists" — passes
  forbidden-vocab but violates "every claim earns proof")
- Off-tone register (formal voice on a TikTok hook)
- Pacing flatness (all sentences within 4 words of each other)

The second-pass reviewer catches those by reading the output as an LLM
with the non-negotiables in context — it judges qualitatively where the
assertion suite is mechanical.

Both passes always run.

## Test prompt generation

Read the voice guide. Pull from two sections:

1. **Channel cheat-sheet** — one prompt per channel that has a row in
   the table. Generate a realistic operator request for that channel.
2. **Non-negotiables** — one or two "free-form" prompts that don't
   name a channel, just a topic. These test core voice without channel
   scaffolding.

Target: 4-8 prompts total. Example set:

| ID | Channel | Topic |
|---|---|---|
| `01_instagram` | Instagram | New center opening, single hero shot |
| `02_email` | Email | Reply to a parent's specific concern |
| `03_facebook` | Facebook | Transformation story (real customer arc) |
| `04_website` | Website | Hero copy + 3 supporting subheads |
| `05_freeform_a` | (none) | Brand mission in 3 sentences |
| `06_freeform_b` | (none) | Why we exist, no template |

The "freeform" prompts replicate KidStrong's Test C (FB post probing
Thinking Architecture) and Test D (website hero probing Rule-Breaking
sentence rhythm). They surface drops in load-bearing patterns the
channel-specific prompts mask.

## Running the wrapped skill against each prompt

The orchestrator (not this script) handles this. For each prompt:

```
1. Open a fresh sub-context with the wrapped voice skill installed
2. Send the prompt
3. Capture the output
4. Write to /tmp/<brand-slug>-validation/outputs/<prompt-id>.md
```

In practice this happens via a subagent call (`context: fork`) per
prompt — keeps validation outputs from polluting the main orchestrator
context.

## Assertion scoring

`scripts/validate_voice_skill.py` reads the voice skill's SKILL.md,
extracts the non-negotiables section, and parses out:

- **Forbidden vocab**: lines matching `**Never:** term1, term2, ...`
- **Required phrases**: quoted strings on `Affirmation, exact format: "..."`
  or `Tagline, exact format: "..."` lines

Then scores each output against the rules **the voice skill declared**
(per `references/brand-contract.md` — undeclared rules are not
enforced). Example assertion set for a brand that declared everything:

| Assertion | Rule (as declared by the brand) |
|---|---|
| `forbidden_vocab` | No term from the Never list appears (case-insensitive, word-boundary) |
| `required_phrase` | Required phrase appears verbatim (Pattern A) or is tracked (Pattern B) |
| `no_oxford_comma` | No "X, Y, and Z" pattern with multi-word items |
| `punctuation_budget.*` | Em-dash / exclamation / semicolon caps at the brand's declared values |
| `pacing` | Short + long sentence mix at the brand's declared thresholds |

Pass rate per prompt = passed assertions / total assertions. Threshold:
90% per prompt. Any prompt below = HALT.

The script writes a markdown scorecard to `--out`. Exit code 0 = pass,
1 = halt.

## Second-pass review (validator subagent)

After assertion scoring, hand the same outputs + non-negotiables to a
validator subagent on the same LLM family as the generator (same-family
validation is less noisy — each family has its own conventions). If the
runtime cannot spawn subagents, run the review yourself in a fresh,
careful pass with only the non-negotiables and outputs in view. Prompt
template:

```
Review these voice outputs against the brand's non-negotiables. Flag
specific violations the regex scoring missed. Be especially alert to:

1. Multi-word Oxford commas — KidStrong's recurring regex blind spot
2. Vague hype claims without proof points
3. Off-tone register (formal where conversational is required, or vice versa)
4. Pacing flatness — sentences uniform in length even if min/max exist
5. Forbidden vocab in conjugated/compound forms (e.g., "instructional"
   when "instructor" is forbidden)
6. Required phrases that appear but in wrong context (e.g., affirmation
   in the middle of a sales pitch instead of as a closer)

Non-negotiables:
<paste from voice guide>

Outputs to review:
<paste each output, labeled by prompt ID>

Format your response as a table:
| Prompt | Finding | Severity (block/warn) |
```

Append the reviewer's findings to the scorecard. Halt if any `block`
severity.

## What to do when validation halts

Don't install or hand over the skill. Fix it, re-run.

Common patterns and fixes (lifted from KidStrong's iteration log):

| Symptom | Likely cause | Fix |
|---|---|---|
| Pacing fails on website prompt | Long-rolling-sentence rule lives in references/, not always-loaded | Add Pacing line to non-negotiables section |
| Oxford comma in multi-word list | Original rule was single-word focused | Tighten the rule: "Every list of three+ items: drop the comma before the final and/or. Scan multi-word lists too." |
| Vague claims pass forbidden-vocab but the reviewer flags | "Every claim earns proof" rule lives in references/editing.md, not always-loaded | Add to non-negotiables |
| Required phrase missing on some prompts | Phrase is only enforced on certain channels in voice guide | Either tighten voice guide rule or accept channel-specific scoring |

After fixing: re-run the validation suite. KidStrong
went through three iterations (initial run -> Pacing fix -> Oxford+proof
fix) before all assertions and second-pass review aligned at 100%.

## Output

Scorecard at `/tmp/<brand-slug>-validation/scorecard.md` includes:

- Per-prompt pass table (assertion-level granularity)
- Second-pass findings appended
- Overall summary (PASS / HALT)
- Suggested fixes for any halts

This file is operator-facing. Make it readable.
