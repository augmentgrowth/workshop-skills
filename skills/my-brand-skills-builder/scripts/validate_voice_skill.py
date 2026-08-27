#!/usr/bin/env python3
"""Brand-agnostic voice-skill validator.

Reads rules from the wrapped voice skill's SKILL.md `## Non-negotiables`
section per the brand contract (references/brand-contract.md). Imposes
no defaults the brand didn't declare. Returns a per-prompt scorecard.

Second-pass review is invoked separately from the orchestrator (not
from this script). This script is pure-Python deterministic assertion
scoring.

Usage:
  python validate_voice_skill.py \\
    --voice-skill /path/to/wrapped/<brand>-voice/ \\
    --voice-guide /path/to/<Brand>_Brand_Voice_Guide.md \\
    --outputs-dir /path/to/rendered-test-outputs/ \\
    --brand "Brand Name" \\
    --out /tmp/<brand>-validation/scorecard.md \\
    --threshold 0.90

Exit code 0 on overall pass (every per-prompt rate >= threshold), 1 on halt.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml  # noqa: F401  (kept for future frontmatter parsing)
except ImportError:
    sys.stderr.write("PyYAML required. Install with: pip install pyyaml\n")
    sys.exit(2)


# ----------------- SKILL.md parsing -----------------

def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_non_negotiables(skill_text: str) -> str:
    """Extract the ## Non-negotiables section from a wrapped voice SKILL.md.

    Case-insensitive header match. Returns empty string if section missing.
    """
    m = re.search(
        r"##\s+Non-?negotiables.*?\n(.*?)(?=\n##\s|\Z)",
        skill_text,
        re.DOTALL | re.IGNORECASE,
    )
    return m.group(1) if m else ""


def parse_forbidden_vocab(non_neg: str) -> list[str]:
    """Find every '**Never:**' line and split on commas. Strips quote/paren noise."""
    out: list[str] = []
    for m in re.finditer(r"\*\*Never:\*\*\s*([^\n]+)", non_neg):
        out.extend(t.strip(" .,;:'\"()[]") for t in m.group(1).split(",") if t.strip())
    return [t for t in out if t]


def parse_required_phrases(non_neg: str) -> list[str]:
    """Find every 'Affirmation/Tagline, exact format:' line and pull the quoted phrase."""
    out: list[str] = []
    for m in re.finditer(r"(?:Affirmation|Tagline)[^\"]*\"([^\"]+)\"", non_neg):
        out.append(m.group(1).strip())
    return out


def detect_pattern_a(non_neg: str) -> bool:
    """Return True when the affirmation must close every piece (KidStrong-style).

    Pattern A (every piece): SKILL.md says "Affirmation, exact format: ..."
    AND mentions "every piece" or "closer when natural" or "close with".

    Pattern B (per-piece optional): SKILL.md uses "Tagline" instead, or has
    no closure-signal language. Absence in a test output is NOT a fail.
    """
    has_affirmation_rule = bool(re.search(r"affirmation[^\n]+exact format", non_neg, re.IGNORECASE))
    closure_signal = bool(
        re.search(r"every piece|closer when natural|close[s]? with", non_neg, re.IGNORECASE)
    )
    return has_affirmation_rule and closure_signal


def parse_oxford_policy(non_neg: str) -> bool:
    """True if 'No Oxford commas' is declared. Validator should enforce."""
    return bool(re.search(r"No Oxford commas?", non_neg, re.IGNORECASE))


def parse_punctuation_budget(non_neg: str) -> dict:
    """Parse em-dash / exclamation / semicolon caps from the section text.

    Defaults are permissive (no enforcement) — brands must declare caps explicitly.
    Sentinel float('inf') means 'no enforcement, informational count only'.
    """
    out: dict[str, float] = {"em": float("inf"), "excl": float("inf"), "semi": float("inf")}

    # Em-dash cap — multiple shapes:
    #   "Max N em dashes" / "max 2 em dashes" / "<=1 em dash" / "≤2 em dashes"
    #   "Em dashes — ... Maximum N per piece" (Restore style, max AFTER noun)
    #   "Em dashes — ... Maximum N-M per piece" or "N–M per piece" (range form)
    #   "1 em dash max" / "1 em dash, max"
    em_patterns = [
        r"(?:≤|<=|max(?:imum)?\s*)\s*(\d+)\s*em[\s-]+dash",
        r"(\d+)\s*em[\s-]+dash[^\n]*\bmax\b",
        # Range form: "Maximum 1-2 per piece" — capture upper bound
        r"em[\s-]+dashes?[^\n]*?max(?:imum)?\s*(\d+)\s*[-–]\s*(\d+)\s*per piece",
        # Single form: "Maximum N per piece" after noun
        r"em[\s-]+dashes?[^\n]*?max(?:imum)?\s*(\d+)\s*per piece",
    ]
    for pat in em_patterns:
        m = re.search(pat, non_neg, re.IGNORECASE)
        if m:
            # If two groups captured (range), use the upper bound
            if m.lastindex and m.lastindex >= 2 and m.group(2):
                out["em"] = int(m.group(2))
            else:
                out["em"] = int(m.group(1))
            break

    # Exclamation cap — multiple shapes:
    #   "Max N exclamation points"   (max-N-noun, KidStrong style)
    #   "Exclamation points: N max"  (noun-N-max, Restore style)
    #   "N exclamation points max"   (N-noun-max)
    #   "<= N exclamation"           (operator form)
    excl_patterns = [
        r"(?:max(?:imum)?\s*|≤|<=)\s*(\d+)[^\n]{0,40}exclamation",
        r"exclamation[^\n]{0,40}?(?:max(?:imum)?|≤|<=)\s*(\d+)",
        r"exclamation[^\n]*?(\d+)[^\n]*?\bmax\b",
        r"(\d+)\s*exclamation[^\n]*\bmax\b",
    ]
    for pat in excl_patterns:
        m = re.search(pat, non_neg, re.IGNORECASE)
        if m:
            out["excl"] = int(m.group(1))
            break

    # Semicolons: literal "No semicolons" -> cap 0
    if re.search(r"No semicolons?", non_neg, re.IGNORECASE):
        out["semi"] = 0

    return out


def parse_pacing(non_neg: str) -> dict | None:
    """Parse pacing thresholds (short_max, long_min). None if rule not declared.

    The rule fires when the non-negotiables section contains the literal
    heading word 'Pacing' + at least one short threshold + at least one
    long threshold in the same rule's text.

    If a brand doesn't declare pacing, the validator does NOT enforce it.
    This is the fix for the bug where v1.0.x silently imposed KidStrong's
    8/20 thresholds on every brand.
    """
    m = re.search(r"\*?\*?Pacing\b[^\n]*\n?([^\n]*)", non_neg, re.IGNORECASE)
    if not m:
        return None
    chunk = m.group(0) + " " + (m.group(1) or "")
    short_m = re.search(r"(?:under|<|<=|less than)\s*(\d+)\s*words?", chunk, re.IGNORECASE)
    long_m = re.search(r"(\d+)\+\s*words?|>=\s*(\d+)\s*words?", chunk, re.IGNORECASE)
    if not (short_m and long_m):
        return None
    long_val = int(long_m.group(1) or long_m.group(2))
    return {"short_max": int(short_m.group(1)), "long_min": long_val}


# ----------------- Scoring -----------------

def score_forbidden(text: str, terms: list[str]) -> tuple[bool, list[str]]:
    found: list[str] = []
    for term in terms:
        if re.search(rf"\b{re.escape(term)}\b", text, re.IGNORECASE):
            found.append(term)
    return (len(found) == 0, found)


def score_required(
    text: str, phrases: list[str], required_every_piece: bool
) -> tuple[bool, list[str]]:
    """Pattern A (required_every_piece): must appear. Pattern B: informational only."""
    if not phrases:
        return (True, [])
    found = [p for p in phrases if p.lower() in text.lower()]
    if required_every_piece:
        return (len(found) > 0, found)
    return (True, found)


def score_oxford(text: str, enforced: bool) -> tuple[bool, list[str]]:
    """Multi-word-aware Oxford comma detector. Skipped when brand doesn't enforce."""
    if not enforced:
        return (True, [])
    pattern = r"[A-Za-z][A-Za-z\s-]+?,\s+[A-Za-z][A-Za-z\s-]+?,\s+(?:and|or)\b"
    matches = re.findall(pattern, text)
    return (len(matches) == 0, matches[:3])


def score_punctuation_budget(text: str, budget: dict) -> dict:
    """Score each cap. inf cap means informational only (always passes)."""
    em = text.count("—") + text.count(" - ")
    excl = text.count("!")
    semi = text.count(";")
    return {
        "em_dashes": (em <= budget["em"], em, budget["em"]),
        "exclamations": (excl <= budget["excl"], excl, budget["excl"]),
        "semicolons": (semi <= budget["semi"], semi, budget["semi"]),
    }


def score_pacing(text: str, pacing: dict | None) -> tuple[bool, str]:
    """If pacing rule isn't declared, skip enforcement (always pass)."""
    if not pacing:
        return (True, "not enforced")
    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s.strip()]
    if not sentences:
        return (False, "no sentences")
    counts = [len(s.split()) for s in sentences]
    has_short = any(c < pacing["short_max"] for c in counts)
    has_long = any(c >= pacing["long_min"] for c in counts)
    longest, shortest = (max(counts), min(counts)) if counts else (0, 0)
    info = f"short<{pacing['short_max']}={has_short} long>={pacing['long_min']}={has_long} longest={longest}w shortest={shortest}w n={len(sentences)}"
    return (has_short and has_long, info)


def score_output(text: str, rules: dict) -> dict:
    result: dict = {}
    ok, found = score_forbidden(text, rules["forbidden"])
    result["forbidden_vocab"] = {"pass": ok, "violations": found}
    ok, found = score_required(text, rules["required"], rules["required_every_piece"])
    result["required_phrase"] = {"pass": ok, "found": found}
    ok, examples = score_oxford(text, rules["oxford_enforced"])
    result["no_oxford_comma"] = {"pass": ok, "examples": examples}
    result["punctuation_budget"] = score_punctuation_budget(text, rules["budget"])
    ok, info = score_pacing(text, rules["pacing"])
    result["pacing"] = {"pass": ok, "info": info}
    return result


# ----------------- Reporting -----------------

def fmt_threshold(val: float) -> str:
    return "∞" if val == float("inf") else str(int(val))


def format_scorecard(brand: str, results: dict, threshold: float, rules: dict) -> str:
    lines = [
        f"# {brand} Voice Skill Validation Scorecard",
        "",
        f"Threshold: {threshold:.0%}. Generated by `validate_voice_skill.py` (brand-agnostic).",
        "",
        "## Parsed rules (from wrapped voice skill SKILL.md)",
        "",
        f"- Forbidden vocab: {len(rules['forbidden'])} terms",
        f"- Required phrases: {len(rules['required'])} (every piece? {rules['required_every_piece']})",
        f"- Oxford comma enforced: {rules['oxford_enforced']}",
        f"- Em dash cap: {fmt_threshold(rules['budget']['em'])}",
        f"- Exclamation cap: {fmt_threshold(rules['budget']['excl'])}",
        f"- Semicolon cap: {fmt_threshold(rules['budget']['semi'])}",
        f"- Pacing rule: {rules['pacing'] if rules['pacing'] else 'not declared'}",
        "",
        "## Per-prompt results",
        "",
    ]

    overall_pass = True
    for prompt_id, res in results.items():
        pass_count = 0
        total = 0
        for key, val in res.items():
            if key == "punctuation_budget":
                for sub_key, (ok, count, cap) in val.items():
                    total += 1
                    pass_count += 1 if ok else 0
            else:
                total += 1
                pass_count += 1 if val.get("pass") else 0
        rate = pass_count / total if total else 0
        if rate < threshold:
            overall_pass = False
        lines.append(f"### {prompt_id} — {pass_count}/{total} ({rate:.0%})")
        lines.append("")
        for key, val in res.items():
            if key == "punctuation_budget":
                for sub_key, (ok, count, cap) in val.items():
                    mark = "PASS" if ok else "FAIL"
                    cap_disp = fmt_threshold(cap)
                    lines.append(f"- **{sub_key}**: {mark} — count {count} (budget {cap_disp})")
            else:
                ok = val.get("pass")
                mark = "PASS" if ok else "FAIL"
                detail = ""
                if "violations" in val and val["violations"]:
                    detail = f" — found {val['violations']}"
                elif "examples" in val and val["examples"]:
                    detail = f" — examples {val['examples']}"
                elif "found" in val:
                    detail = f" — found {val['found']}"
                elif "info" in val:
                    detail = f" — {val['info']}"
                lines.append(f"- **{key}**: {mark}{detail}")
        lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"Overall: {'PASS' if overall_pass else 'HALT (one or more prompts below threshold)'}")
    return "\n".join(lines)


# ----------------- Main -----------------

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--voice-skill", required=True, type=Path)
    ap.add_argument("--voice-guide", required=True, type=Path)
    ap.add_argument(
        "--outputs-dir", required=True, type=Path,
        help="Directory containing rendered prompt outputs (one .md per prompt)",
    )
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--brand", required=True)
    ap.add_argument("--threshold", type=float, default=0.90)
    args = ap.parse_args()

    skill_md = args.voice_skill / "SKILL.md"
    if not skill_md.is_file():
        sys.stderr.write(f"SKILL.md not found at {skill_md}\n")
        return 1

    skill_text = read_text(skill_md)
    non_neg = extract_non_negotiables(skill_text)

    rules = {
        "forbidden": parse_forbidden_vocab(non_neg),
        "required": parse_required_phrases(non_neg),
        "required_every_piece": detect_pattern_a(non_neg),
        "oxford_enforced": parse_oxford_policy(non_neg),
        "budget": parse_punctuation_budget(non_neg),
        "pacing": parse_pacing(non_neg),
    }

    print(
        f"Parsed rules: {len(rules['forbidden'])} forbidden, "
        f"{len(rules['required'])} required (every_piece={rules['required_every_piece']}), "
        f"oxford={rules['oxford_enforced']}, "
        f"em={fmt_threshold(rules['budget']['em'])}, "
        f"excl={fmt_threshold(rules['budget']['excl'])}, "
        f"semi={fmt_threshold(rules['budget']['semi'])}, "
        f"pacing={rules['pacing']}"
    )

    if not args.outputs_dir.is_dir():
        sys.stderr.write(f"Outputs directory not found: {args.outputs_dir}\n")
        return 1

    results: dict[str, dict] = {}
    for output_file in sorted(args.outputs_dir.glob("*.md")):
        text = read_text(output_file)
        results[output_file.stem] = score_output(text, rules)

    if not results:
        sys.stderr.write(f"No outputs found in {args.outputs_dir}/*.md\n")
        return 1

    scorecard = format_scorecard(args.brand, results, args.threshold, rules)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(scorecard, encoding="utf-8")
    print(f"Scorecard -> {args.out}")

    for prompt_id, res in results.items():
        total = 0
        pc = 0
        for key, val in res.items():
            if key == "punctuation_budget":
                for sk, (ok, _, _) in val.items():
                    total += 1
                    pc += 1 if ok else 0
            else:
                total += 1
                pc += 1 if val.get("pass") else 0
        if total and pc / total < args.threshold:
            print(f"HALT: {prompt_id} scored {pc}/{total} ({pc/total:.0%}) below threshold {args.threshold:.0%}")
            return 1

    print("All prompts pass threshold.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
