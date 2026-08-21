---
name: voice-skill-builder
description: "This skill should be used when building a voice skill for a person or brand. Triggers on: 'build a voice skill', 'create a voice profile', 'capture my voice', 'make a writing skill', 'voice skill for [name]', 'teach Claude my voice', 'clone my writing style', 'build my voice', 'personal voice skill', 'brand voice', 'brand voice guide', 'company tone of voice', 'voice for our brand', 'brand writing style', 'capture our brand voice'."
disable-model-invocation: true
---

# Voice Skill Builder

Build a voice skill for a person or brand from writing samples and a short interview. The output is a complete, Opus-optimized `.skill` file the user can install with one click.

## Process Overview

Six phases in order: Intake, Analysis, Interview, Generate (draft), Calibration, Package.

### Subject Type

The skill supports two subject types: **individual** (a person's writing voice) and **brand** (a company, product, or organization's voice).

Auto-detect the subject type from context. Look at the user's request, the samples provided, and conversational cues. Signals:

- **Individual:** User says "my voice," "my writing style," provides personal blog posts, social media, newsletters authored by one person. Samples have a consistent first-person perspective.
- **Brand:** User says "our brand," "company voice," "brand tone," provides marketing copy, website content, ad campaigns, brand guidelines, support templates. Samples come from multiple authors or have a corporate perspective.

If it's ambiguous, ask. Otherwise, proceed with the detected type and adapt each phase accordingly. The rest of this document uses **"subject"** to mean whoever or whatever the voice belongs to, whether a person or a brand.

### Phase 1: Intake

Ask for writing samples. 5-10 pieces across different formats provide the strongest foundation. Even 2-3 are useful.

**How to gather samples (offer all that apply):**

- **Reference past chats.** Use `conversation_search` and `recent_chats` to pull the subject's words from previous conversations. Search for writing-related topics (posts they drafted, content they discussed, explanations they gave). This is often the fastest and most natural source of voice data since the user doesn't have to prepare anything.
- **Paste in chat.** The user can paste writing samples directly into the conversation.
- **Upload files.** The user can attach documents, screenshots, or text files.
- **Fetch URLs.** If the user provides a URL (blog, website, LinkedIn profile, newsletter archive, X profile), fetch that page and use it as a starting sample. Then look for related content to broaden the sample set:
  - Follow links to other posts, articles, or pages by the same author or on the same site.
  - For blogs and newsletters, look for an archive or index page and pull 3-5 additional pieces.
  - For company websites, navigate to key pages (about, product, blog) to capture voice across contexts.
  - For social profiles, scroll or paginate to collect a range of posts.
  - Aim to gather 5-10 samples total from the URL and its related pages. Tell the user what you found: "I pulled 7 pieces from your blog (3 posts, the about page, and 3 newsletter issues). Want me to look at anything else?"
  - If the site is behind a login wall or fetch fails, let the user know and ask them to paste samples instead.

**Brand-specific intake guidance:**
When the subject is a brand, also look for these if available:
- Existing brand or style guidelines
- Marketing copy across channels (website, ads, social, email)
- Customer-facing communications (support emails, onboarding flows)
- Internal tone documentation or brand decks

Diversity of formats matters more for brands since voice consistency across channels is part of what the skill will enforce.

If no samples are available through any method, skip to Phase 3. The output will be less grounded but still functional.

### Phase 2: Analysis

Read all samples. Extract patterns across these dimensions:

**Voice identity.** What kind of subject is this? Not their resume or mission statement. Their energy, their relationship to their audience, their default posture.

**Distinctive attributes.** 3-5 traits that make the voice recognizable. Look for what's UNUSUAL. Every brand can be "innovative and customer-centric." Every person can be "clear and professional." What makes THIS subject different? For each attribute, note:
- What it looks like (with quotes from the samples)
- What the over-applied version looks like (the costume)

**Thinking patterns.** How do they process and present ideas?
- Start with conclusions or discover them?
- Resolve every thread or leave some open?
- Make cross-domain connections?
- Project confidence or show uncertainty?
- For brands: Do they lead with the customer's problem or their own solution? Educate or persuade? Challenge conventions or reassure?

**Grammar and style fingerprint.** Punctuation habits, contraction usage, sentence length distribution, paragraph weight, POV default.

**Natural vocabulary.** Recurring words and phrases. Note them as texture, not as a checklist to enforce.

**Dead patterns.** What the subject naturally avoids. Identify by absence.

### Phase 3: Interview

The model should do the work. The user's job is to react, not to fill out a survey.

After analysis, present a concise summary of what you found. Cover the voice identity, 3-5 distinctive attributes, the anti-patterns you inferred (what the subject avoids), the audience relationship, and the formats you observed. Frame it as a confident read, not a tentative guess.

Example: "Here's what I'm seeing from the samples: [Name] writes like [identity]. The voice is distinctive because [attributes]. It avoids [anti-patterns]. The audience relationship is [description]. I saw content across [formats]. Anything off here, or anything important I'm missing?"

**The user corrects, confirms, or adds.** This is the interview. Most of the time, the analysis will be close enough that the user only needs to nudge a few things. That's the goal. A quick "yeah, but we're more X than Y" is more useful than the user picking from a list of options they all agree with.

**Only ask structured questions when you're genuinely stuck.** Use `ask_user_input` sparingly. Reserve it for moments where the samples are ambiguous or contradictory and you need the user to break a tie. Examples of when a question earns its place:

- Samples show both formal and casual registers with no clear pattern → ask which is the default vs. the exception
- Humor appears in some samples but not others → ask whether that's intentional range or inconsistency
- Brand samples come from clearly different eras or campaigns → ask which represents the current voice

**Questions to avoid:**
- Anything where every option is obviously applicable ("What formats do you write in?" when you can see the formats in the samples)
- Anything where the answers are self-evidently good ("What does bad writing sound like?" Nobody picks "good jargon.")
- Anything the model can infer from the samples (audience, tone, register, anti-patterns)

**If no samples were provided**, the interview carries more weight. In this case, ask open-ended questions conversationally rather than structured multi-selects. Let the user describe what they're going for in their own words. That description itself becomes voice data. Good questions for the no-samples case:

- "Describe the voice you're going for as if you were briefing a new writer on day one."
- "Send me a link to someone (or a brand) whose voice is in the neighborhood of what you want. What would you keep and what would you change?"
- "What's the one thing you never want this voice to sound like?"

**Flow:** Lead with the analysis summary. Let the user react. Ask structured questions only if the reaction leaves genuine ambiguity. One round of follow-up at most.

### Phase 4: Generate (Draft)

Generate the complete 3-file voice skill using `references/framework.md` as the structural blueprint. Every section populated from analysis + interview data.

The skill directory structure:
```
[name]-voice/
├── SKILL.md
├── references/editing.md
└── references/examples.md
```

Use the subject's name (person or brand) for `[name]`. Create the directory and all three files as `[name]-voice/` inside the folder the user is currently working in. Do not write to an absolute path outside that folder.

Present a brief summary of what was generated: the core attributes, the dead patterns, and the grammar rules. Don't present the files yet. The user needs to see the skill in action before it ships.

### Phase 5: Calibration

Now test the draft skill. Write 2-3 short outputs as if the skill were already active. Different formats if possible.

For individuals: one short-form (tweet/post), one medium-form (newsletter intro, article section).
For brands: test across the channels they actually use. Try a social post, a product page snippet, a support reply, or an ad headline. Cross-channel consistency is the real test for brand voices.

Follow the Generation Protocol, Voice Compass, and Grammar and Style rules from the draft skill you just wrote.

Present the outputs and ask: "These were written using the voice skill. Point at anything that doesn't sound right."

The user's corrections go directly into the skill files:
- "We wouldn't phrase it that way" → update Dead Patterns or Grammar and Style
- "Too casual / too formal" → adjust Voice Compass register
- "Close but missing something" → add or revise a Core Attribute
- "That line feels like a setup" → add to Dead Patterns with a specific example
- "Sounds right" → skill is calibrated, proceed to packaging

Revise the skill files based on feedback. If corrections were significant, produce one more test output to confirm the fix. Repeat until the user confirms.

### Phase 6: Package

The generated `[name]-voice/` folder is already a working skill. How you finish depends on where you are running.

**Running on the user's own computer (Claude Code):** the folder is the deliverable. Offer to install it for them by copying it into their skills directory — global if they want the voice available everywhere, or the project's `.claude/skills/` if it belongs to one body of work. Resolve the correct path for their operating system; do not assume macOS. Tell them they may need to start a new session before it becomes active.

**Running in a hosted sandbox** (a `/home/claude` working directory exists): package the folder as a `.skill` zip archive and present the file for one-click install.

```python
import zipfile
from pathlib import Path

skill_dir = Path("[name]-voice")            # relative to the working directory
output_path = Path("[name]-voice.skill")

with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for file_path in skill_dir.rglob('*'):
        if file_path.is_file():
            zipf.write(file_path, file_path.relative_to(skill_dir.parent))
```

Either way, give a brief summary of what the skill contains and suggest the user test it on a real writing task.

## Opus Optimization

The generated voice skill will be used with Claude Opus. Apply these guidelines to everything generated:

**Language precision over volume.** Opus responds to clear, precise instructions. Avoid CAPS emphasis, "MUST", "CRITICAL", "ALWAYS", "NEVER" in the generated skill. State rules plainly.

**Model clean punctuation in the skill itself.** The model absorbs the style of its own instructions. If the voice skill is full of em dashes and colons, the output will be too. Write the skill files using periods, commas, and natural sentence flow. Avoid the same AI tells you're asking the model to suppress.

**Anti-costume protocol is essential.** Opus over-applies explicit patterns. Every voice attribute needs a "This is not" definition. The Natural Vocabulary section must include the anti-costume warning (no more than 2-3 vocabulary markers per piece). This cap applies to vocabulary only, not to punctuation. Punctuation tells like em dashes and colon-driven sentences are off by default. This applies equally to brand voices. Opus will latch onto brand buzzwords and overuse them just as readily as personal quirks.

**Thinking Architecture is the differentiator.** Without it, Opus produces stylistically correct but intellectually generic output. For individuals, the section on how the person THINKS (not just writes) is what separates costume from voice. For brands, the equivalent is how the brand REASONS about its audience and domain, its editorial logic rather than its surface tone.

**Discovery structure.** Opus defaults to thesis-first (declare the point, then support it). The generated skill should instruct discovery-mode drafting unless the subject's actual voice IS thesis-first. Many brands are genuinely thesis-first. That's fine. Capture it accurately rather than forcing discovery mode.

## Reference Files

- **`references/framework.md`** Section-by-section blueprint for the generated voice skill. Describes what each section should contain, how to derive it from input, and quality criteria.
