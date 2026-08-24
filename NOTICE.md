# Credits and licenses

## grill-me

The `grill-me` skill in this repo is adapted from **Matt Pocock's** work, not written by Augment Growth.

- Source: https://github.com/mattpocock/skills
- Commit: `5b15a47f2d7150f545fbcacbfe381787fc0230dc`
- Retrieved: 2026-08-21
- License: MIT

Upstream publishes two separate skills: `grill-me` (a one-line shim) and `grilling` (the interview engine that does the actual work). This repo merges them into a single skill — `grilling`'s body, unmodified, published under the `grill-me` name — so that one phrase means one install. Nothing about the interview behavior was changed.

Upstream MIT license text, reproduced in full:

```
MIT License

Copyright (c) 2026 Matt Pocock

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## humanizer

The `humanizer` skill in this repo is adapted from **Siqi Chen's** work, not written by Augment Growth.

- Source: https://github.com/blader/humanizer
- Commit: `e2e92e7b4b8229253ed5c8e81dc65463fdeddda5`
- License: MIT
- Retrieved: 2026-08-21

The skill body shipped here is upstream's at commit `e2e92e7b4b8229253ed5c8e81dc65463fdeddda5` (version 2.11.2), unchanged apart from an added provenance block in the frontmatter. The underlying pattern catalogue derives from [Wikipedia's "Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by WikiProject AI Cleanup and licensed CC BY-SA.

Upstream MIT license text, reproduced in full:

```
MIT License

Copyright (c) 2025 Siqi Chen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## ce-brainstorm, ce-plan, ce-work, ce-handoff

These four skills are adapted from **Every's** compound-engineering plugin, not written by Augment Growth.

- Source: https://github.com/EveryInc/compound-engineering-plugin
- Version: `3.20.0`
- Retrieved: 2026-08-21
- License: MIT

Upstream ships them as part of a ~30-skill plugin whose members call each other freely. This repo extracts four of them to stand alone. Changed from the original:

- **Frontmatter** carries an added `origin` provenance block; skill bodies are otherwise upstream's.
- **Cross-references to plugin siblings that do not ship here** (`ce-pov`, `ce-doc-review`, `ce-proof`, `ce-code-review`, `ce-simplify-code`, `ce-commit-push-pr`, `ce-worktree`, `ce-debug`, `ce-compound`, `lfg`) were softened to graceful absence rather than deleted: each SKILL.md opens with an availability contract, and the three handoff/shipping references carry a gate that drops menu options routing to absent skills and substitutes an inline fallback. No load-bearing behavior was removed — the *intent* of each step survives, performed inline.
- **`ce-brainstorm`'s verdict routing** to `ce-pov` is handled inline, and its `references/verdict-routing.md` is not shipped.
- **Model-elevation dispatch** (`references/reasoning-elevation.md` plus its `elevation-dispatch.sh` / `peer-job-runner.py` scripts) is not shipped in `ce-brainstorm` or `ce-plan`; those steps run on the session model.
- **`ce-work`'s cross-model execution engine** — `references/execution-engines.md`, `references/cross-model-execution.md`, `references/cross-model-work-eval.md`, and the bundled Python/shell controller under `scripts/` — is not shipped. Execution is always native, and the skill's fail-closed reference-loading rule carries an explicit carve-out so those three absences do not stop a run.
- **`ce-brainstorm`'s visual-probe display helper** (`scripts/visual-probe-server.js`) is not shipped; the reference's own text fallback is the documented path.
- **Shell-dependent steps** (scratch directories, `git` probes, clipboard copies, `/tmp` managed storage) were annotated as skippable so the skills degrade rather than stall where no terminal exists.

Upstream MIT license text, reproduced in full:

```
MIT License

Copyright (c) 2025 Every

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## skill-creator

The `skill-creator` skill in this repo is **Anthropic's**, not written by Augment Growth.

- Source: https://github.com/anthropics/claude-plugins-official/tree/main/plugins/skill-creator
- Marketplace: `claude-plugins-official`, plugin `skill-creator`, snapshot `340e33aef211d95769d252324854497af871dafe`
- Retrieved: 2026-08-23
- License: Apache License 2.0

Unlike the extractions above, nothing here was adapted. Every file is upstream's
byte-for-byte — `SKILL.md`, `agents/`, `references/`, `scripts/`, `assets/`,
`eval-viewer/` — with no frontmatter provenance block added and no cross-references
softened, because the skill ships self-contained upstream and calls no plugin
siblings. This repo redistributes it so workshop attendees can install it without
adding a plugin marketplace.

Apache 2.0 requires that the license text accompany the work: it ships as
`skills/skill-creator/LICENSE.txt`, alongside `skills/skill-creator/NOTICE.md`.
The full text is not duplicated here — see that file, or
https://www.apache.org/licenses/LICENSE-2.0.

Anthropic's name and marks are used only to identify the origin of this skill, as
Apache 2.0 section 6 permits. Nothing here implies Anthropic endorses this repo or
the workshop.

## routines

Written by Malachi Rose / Augment Growth. Covered by the repository `LICENSE`.

Changed from the original: the internal version was wired to one specific Claude
account and one machine. Sanitized for publication —

- **Account-specific identifiers removed.** The hardcoded `environment_id`, the
  default GitHub repository, and the Gmail / Google Calendar / Slack
  `connector_uuid` values were replaced with placeholders plus a discovery step
  (read them off an existing routine via `RemoteTrigger list`, or from the
  environment and connector settings pages). No credentials, tokens, or API keys
  were present in the original.
- **Personal context generalized.** References to the author by name, to his
  timezone, to his laptop, and to his Obsidian vault became "the user", "their
  local timezone" (with a step to determine and confirm it), and generic local-file
  language. The cron examples keep US Pacific as a worked example, labelled as such,
  and gained a daylight-saving caveat.
- **Vault-specific output paths generalized.** The report path and the
  "add to `active/todo.md`" step were replaced with a repo-relative report folder
  agreed with the user, and a plain instruction to report outstanding blockers.
- **Availability contract added**, in the same spirit as the `ce-` extractions
  above: the skill depends on the `RemoteTrigger` tool rather than on any bundled
  file, so it now opens by naming that dependency and pointing at the web UI as
  the fallback path when the tool is unavailable.
- **Build-system frontmatter removed** (`static`, `tier`, and an `upstream` key
  holding a local filesystem path), replaced with an `origin` provenance block
  matching the rest of this repo.

## voice-skill-builder

Written by Malachi Rose / Augment Growth. Covered by the repository `LICENSE`.

Changed from the original: the earlier internal version wrote its output to hosted-sandbox paths (`/home/claude/`, `/mnt/user-data/outputs/`), which do not exist on a personal Mac or Windows machine. This copy writes relative to the user's working directory and detects the sandbox case instead of assuming it, and derives a Windows-safe slug for the generated skill folder.

## call-summary and daily-briefing

The `call-summary` and `daily-briefing` skills are **Anthropic's**, redistributed unchanged from the official knowledge-work-plugins repository (sales plugin).

- Source: https://github.com/anthropics/knowledge-work-plugins
- Paths: `sales/skills/call-summary/`, `sales/skills/daily-briefing/`
- Commit: `16d1ab5`
- Retrieved: 2026-08-23
- License: Apache 2.0 — full text ships as `LICENSE.txt` inside each skill folder (`skills/sales/call-summary/`, `skills/sales/daily-briefing/`), per the license's redistribution terms.
