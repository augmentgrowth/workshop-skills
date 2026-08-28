# W2 · Step 4 — Build Your MyVoice Skill

**Where:** the **same Claude Code session** as [Step 3 — extraction](w2-3-voice-extraction.md) — the build needs your corpus and review answers on the table. (If the session feels heavy, run `/compact` first, then continue.)
**What you'll have when done:** an installed skill that writes like you.

## Steps

1. Paste the prompt box below into the same session.
2. Approve the plan, then answer the builder's few interview questions — or say "skip"; it works either way.
3. When it asks **where to install**, pick your **second brain**.
4. Continue to [Step 5 — Invoke it](w2-5-invoke-myvoice.md).

## The prompt — copy everything in the box

```text
Plan first: use the ce-plan skill to plan this build, then proceed. Use the voice-skill-builder skill to build my personal voice skill from the samples in email-context.md in my My Voice Skill project folder — apply my review answers from review-uncertain.md first. Name the skill exactly "my-voice", titled My Voice. When it asks where to install, pick my second brain.
```

## Done when

The builder reports the skill installed in your second brain's skills folder.

## If it goes sideways

- **It can't find email-context.md:** you're in a different session or folder — tell it the path: `01_Projects/My Voice Skill/email-context.md`.
- **Build runs long:** that's normal; it reads every sample. Let it finish — the next step waits for you, not the clock.
