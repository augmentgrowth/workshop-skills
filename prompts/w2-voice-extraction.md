# W2 · Step 3 — MyVoice: Extract Your Writing Samples

**Where:** Claude Code, in your **second-brain folder**.
**What you'll have when done:** a cleaned corpus of your real emails (`email-context.md`) plus a short review queue of Claude's judgment calls — the raw material for your voice skill.

**Data line, up front:** work account, work content, saved to your own machine. The prompt itself skips payments, legal, HR, and health.

## Steps

1. Confirm you're in your second-brain folder, then run `/ce-plan`.
2. Paste the whole prompt box below into it, and **approve the plan** it writes — like a manager.
3. While it runs, watch for two files: `email-context.md` (your samples) and `review-uncertain.md` (its judgment calls).
4. Open `review-uncertain.md`, tick KEEP or DROP on each item, then tell Claude: **"apply my review answers."**
5. Continue to [Step 4 — Build MyVoice](w2-build-myvoice.md) **in this same session**.

## The prompt — copy everything in the box

```text
Using my email connector (Microsoft 365 — or Gmail if that's what I have connected), build a writing-voice corpus from my sent email.

1. First, create a project folder for this build: `01_Projects/My Voice Skill/`. Everything below saves there. If you think it belongs somewhere else in my vault, propose the destination and confirm with me before writing anything.
2. Search my Sent folder for roughly my last 100 sent emails. Work token-light: triage on metadata first (sender, subject, size, date) and only open the bodies of likely keepers — never open all 100.
3. Only keep text I wrote myself — never quoted replies, forwarded text, or anything written by someone else.
4. Skip automated mail entirely: calendar invites and updates, invoices, receipts, notifications, mass mail — and anything I sent to an AI assistant, bot, or test address.
5. Strip signatures, legal footers, and quoted chains from every keeper.
6. Privacy filter: skip emails about payments, contracts under negotiation, legal, HR, or health matters. Exception: if an email is voice-rich but touches money or terms, keep the prose and replace the specific numbers or terms with [redacted] instead of dropping the whole email.
7. Authenticity filter: if an email looks AI-written or heavily AI-polished, do not put it in the main corpus.
8. Aim for at least 15 keepers with real diversity: casual AND professional, long AND short, quick replies AND thought-out ones. If the corpus is thin, search further back until it isn't; if you find more than 25 good ones, keep them — stop when you have real range, not at a number.
9. Save two files in the project folder:
   - email-context.md — the cleaned samples, numbered, each with a one-line label
   - review-uncertain.md — anything you weren't sure about (possibly AI-written or sensitive), each with a one-line reason and a KEEP / DROP checkbox for me
10. Finish by reporting: kept vs skipped counts, why you skipped what you skipped, and whether this corpus is strong enough to build my voice skill from.
```

## Done when

`email-context.md` exists in your `01_Projects/My Voice Skill/` folder and you've given verdicts on the review queue.

## If it goes sideways

- **Corpus comes back full of robot mail:** say *"drop anything auto-generated; keep only emails I actually wrote."*
- **No working scan after ~8 minutes:** switch lanes — paste 5–10 emails you're proud of directly into the chat and say "use these as my corpus instead."

## Level it up

Slack as a second source — ask Claude to add your best Slack writing to the corpus the same way.
