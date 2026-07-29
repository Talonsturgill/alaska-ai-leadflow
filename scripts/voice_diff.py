#!/usr/bin/env python3
"""Learn the house voice from what Talon actually sends.

The routine drafts. A human edits and sends. Everything he changes on the way out
is a correction to our voice model, and until now that signal evaporated unless he
happened to mention it. This captures it.

WHY IT WRITES TO ITS OWN FILE. Observed edits are evidence, not law. They land in
knowledge/VOICE_DELTAS.md, which OUTREACH_CRAFT.md points at, and never inside
OUTREACH_CRAFT.md itself. The craft doc stays hand-authored, so no run can quietly
rewrite the rules it is judged against, and a human decides when a pattern has
earned promotion into the law.

WHY IT COUNTS. One edit is noise. The same edit three times is a rule. Every delta
carries a recurrence count, and the script says plainly when a pattern has repeated
often enough to be worth promoting.

Usage
  voice_diff.py --drafted out/<date>/outreach.json --sent out/<date>/sent.json
  voice_diff.py ... --record        append to the ledger and re-render the notes
  voice_diff.py --summary           what has recurred, and what is ready to promote
"""

import argparse
import difflib
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER = os.path.join(REPO, "ledger", "voice_deltas.json")
NOTES = os.path.join(REPO, "knowledge", "VOICE_DELTAS.md")
PROMOTE_AT = 3

CONTRACTIONS = {
    "we are": "we're", "it is": "it's", "is not": "isn't", "we would": "we'd",
    "you would": "you'd", "do not": "don't", "does not": "doesn't", "that is": "that's",
    "there is": "there's", "i will": "i'll", "we will": "we'll", "cannot": "can't",
    "will not": "won't", "they are": "they're", "you are": "you're", "let us": "let's",
    "was not": "wasn't", "have not": "haven't", "would not": "wouldn't", "i am": "i'm",
}


def sentences(text):
    out = []
    for block in text.split("\n"):
        block = block.strip()
        if not block or block.startswith("http"):
            if block.startswith("http"):
                out.append(block)
            continue
        for s in re.split(r"(?<=[.!?])\s+", block):
            s = s.strip()
            if s:
                out.append(s)
    return out


def norm(s):
    return re.sub(r"\s+", " ", s.lower().strip())


def classify(before, after):
    """Name the KIND of edit, because the kind is what generalises."""
    b, a = norm(before), norm(after)
    kinds = []

    for long, short in CONTRACTIONS.items():
        if long in b and short in a:
            kinds.append("contraction")
            break
    for long, short in CONTRACTIONS.items():
        if short in b and long in a:
            kinds.append("expansion")
            break

    if len(a) < len(b) * 0.7:
        kinds.append("shortened")
    elif len(a) > len(b) * 1.3:
        kinds.append("lengthened")

    bw, aw = set(re.findall(r"[a-z']+", b)), set(re.findall(r"[a-z']+", a))
    dropped, added = bw - aw, aw - bw
    if {"reply", "yes"} & dropped and {"click", "link", "look", "see"} & added:
        kinds.append("cta softened")
    if {"agent", "team"} & dropped:
        kinds.append("agent-team framing cut")
    if {"expected", "probably"} & dropped:
        kinds.append("presumption cut")

    return kinds or ["reworded"], sorted(dropped)[:8], sorted(added)[:8]


def diff(drafted, sent):
    d, s = sentences(drafted), sentences(sent)
    sm = difflib.SequenceMatcher(None, [norm(x) for x in d], [norm(x) for x in s])
    deltas = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        if tag == "delete":
            for x in d[i1:i2]:
                deltas.append({"kinds": ["deleted"], "before": x, "after": None,
                               "dropped": [], "added": []})
        elif tag == "insert":
            for x in s[j1:j2]:
                deltas.append({"kinds": ["added"], "before": None, "after": x,
                               "dropped": [], "added": []})
        else:  # replace, pair them up so the classifier sees before and after
            for k in range(max(i2 - i1, j2 - j1)):
                b = d[i1 + k] if i1 + k < i2 else None
                a = s[j1 + k] if j1 + k < j2 else None
                if b and a:
                    kinds, dr, ad = classify(b, a)
                elif b:
                    kinds, dr, ad = ["deleted"], [], []
                else:
                    kinds, dr, ad = ["added"], [], []
                deltas.append({"kinds": kinds, "before": b, "after": a,
                               "dropped": dr, "added": ad})
    return deltas


def load_ledger():
    if not os.path.exists(LEDGER):
        return {"version": 1, "note": "Observed hand edits between the drafted email and what was actually sent. Evidence, not law. OUTREACH_CRAFT.md stays hand-authored.", "entries": []}
    return json.load(open(LEDGER))


def counts(led):
    """How many SENDS carried this pattern, not how many times it fired.

    Four contractions inside one email is one observation, not four. Promotion is
    about a habit repeating across different emails, so counting occurrences would
    let a single wordy draft promote itself into the law.
    """
    c = {}
    for e in led["entries"]:
        for k in {k for d in e["deltas"] for k in d["kinds"]}:
            c[k] = c.get(k, 0) + 1
    return c


def occurrences(led):
    """Raw fire count, for the log only. Never gates promotion."""
    c = {}
    for e in led["entries"]:
        for d in e["deltas"]:
            for k in d["kinds"]:
                c[k] = c.get(k, 0) + 1
    return c


def render_notes(led):
    c, occ = counts(led), occurrences(led)
    ready = sorted([k for k, n in c.items() if n >= PROMOTE_AT and k not in ("reworded", "added", "deleted")],
                   key=lambda k: -c[k])
    lines = [
        "# Voice deltas, observed",
        "",
        "Every edit Talon made between the drafted email and the one he actually sent.",
        "Written by scripts/voice_diff.py at the start of each run. This file is",
        "EVIDENCE, not law. knowledge/OUTREACH_CRAFT.md is the law and stays",
        "hand-authored, so no run can rewrite the rules it is judged against.",
        "",
        f"A pattern seen in {PROMOTE_AT} or more SEPARATE sends has earned a look at",
        "promotion into OUTREACH_CRAFT.md. Counting sends rather than occurrences is",
        "deliberate, four contractions in one email is one observation, not four.",
        "That promotion is a human decision, never automatic.",
        "",
        "## Recurring patterns",
        "",
    ]
    if not c:
        lines.append("None recorded yet.")
    for k, n in sorted(c.items(), key=lambda kv: -kv[1]):
        flag = "  <- READY TO PROMOTE" if k in ready else ""
        lines.append(f"- **{k}**, in {n} send(s), {occ.get(k, 0)} time(s) total{flag}")
    if ready:
        lines += ["", "The writer keeps making these and Talon keeps undoing them. Fix the brief,",
                  "not the individual email."]
    lines += ["", "## Log", ""]
    for e in reversed(led["entries"][-12:]):
        lines.append(f"### {e['run_date']}, {e['company']}")
        lines.append("")
        for d in e["deltas"]:
            tags = ", ".join(d["kinds"])
            if d["before"] and d["after"]:
                lines.append(f"- `{tags}`")
                lines.append(f"  - drafted: {d['before']}")
                lines.append(f"  - sent:    {d['after']}")
            elif d["before"]:
                lines.append(f"- `{tags}` drafted, cut before sending: {d['before']}")
            else:
                lines.append(f"- `{tags}` not drafted, added by hand: {d['after']}")
        lines.append("")
    return "\n".join(lines) + "\n"


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--drafted", help="out/<date>/outreach.json, what the routine wrote")
    p.add_argument("--sent", help="JSON with the sent body, from the Gmail read-back")
    p.add_argument("--company", default="unknown")
    p.add_argument("--run-date", default="unknown")
    p.add_argument("--record", action="store_true", help="append to the ledger and re-render the notes")
    p.add_argument("--summary", action="store_true", help="show recurring patterns only")
    a = p.parse_args()

    led = load_ledger()

    if a.summary:
        c = counts(led)
        print(f"{len(led['entries'])} sends compared.\n")
        if not c:
            print("Nothing recorded yet.")
            return 0
        occ = occurrences(led)
        for k, n in sorted(c.items(), key=lambda kv: -kv[1]):
            mark = "  READY TO PROMOTE" if n >= PROMOTE_AT and k not in ("reworded", "added", "deleted") else ""
            print(f"  {k:28} in {n} send(s), {occ.get(k,0)}x total{mark}")
        return 0

    if not (a.drafted and a.sent):
        p.error("--drafted and --sent are required unless --summary")

    drafted = json.load(open(a.drafted)).get("body", "")
    sj = json.load(open(a.sent))
    sent = sj.get("body") or sj.get("plaintextBody") or ""
    if not sent and "messages" in sj:
        sent = sj["messages"][0].get("plaintextBody", "")
    if not drafted or not sent:
        print("Could not read both bodies. Nothing to compare.", file=sys.stderr)
        return 2

    deltas = diff(drafted, sent)
    print(f"{len(deltas)} edit(s) between what we drafted and what went out.\n")
    for d in deltas:
        print(f"  [{', '.join(d['kinds'])}]")
        if d["before"]:
            print(f"    - {d['before'][:96]}")
        if d["after"]:
            print(f"    + {d['after'][:96]}")
        print()

    if a.record:
        led["entries"].append({"run_date": a.run_date, "company": a.company, "deltas": deltas})
        os.makedirs(os.path.dirname(LEDGER), exist_ok=True)
        json.dump(led, open(LEDGER, "w"), indent=2)
        open(NOTES, "w").write(render_notes(led))
        c = counts(led)
        ready = [k for k, n in c.items() if n >= PROMOTE_AT and k not in ("reworded", "added", "deleted")]
        print(f"Recorded. {len(led['entries'])} sends compared to date.")
        if ready:
            print(f"READY TO PROMOTE into OUTREACH_CRAFT.md: {', '.join(ready)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
