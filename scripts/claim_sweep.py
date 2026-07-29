#!/usr/bin/env python3
"""Find every place a claim lives, and every place two of them disagree.

Written after the 2026-07-29 run, which took seven critic rounds to ship. Six of
those rounds were spent on ONE defect wearing different clothes, and the two
lessons that came out of it are the two things this script mechanises.

LESSON 1, fix a claim everywhere it appears, not the sentence a critic quoted.
Round four applied nine fixes at the exact strings the critic named and left the
same argument standing three sections later in different words. Round five caught
it again. A critic quotes a SPAN, but the defect is a CLAIM, and a claim has more
than one home. `echoes` finds the other homes.

LESSON 2, re-read every section that references a change, not just the one edited.
Adding plan.phase1_later made vendor fan-out conditional in the plan while the
roadmap still promised it outright, and a funding gate ended up resting on a
measurement that might never be collected. A section does not know who cites it.
`conflicts` finds values that disagree across sections.

This never judges whether a claim is TRUE. The fact-checker does that against live
pages. This only answers "where else does this live" and "do those places agree",
which is the part a model reliably gets wrong and a script reliably gets right.

Usage
  claim_sweep.py --study out/<date>/study.json
  claim_sweep.py --study <f> --strict        exit 1 if any conflict is found
  claim_sweep.py --self-test                 run against the 2026-07-29 defects
"""

import argparse
import json
import re
import sys
from itertools import combinations

STOP = set("""a an and are as at be been but by can could do does for from had has have
he her his how i if in into is it its me my no not of on or our out over she should so
some such than that the their them then there these they this those to too under until
up us was we were what when where which who why will with would you your yours it's
one two three four five six seven eight nine ten""".split())

# Each pattern yields a comparable value. Kinds are deliberately coarse, because the
# question is "do these two mentions of the same KIND of fact agree", not "parse it".
PATTERNS = [
    ("date", re.compile(r"\b(\d{1,2}\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)(?:\s+\d{4})?)\b", re.I)),
    ("date", re.compile(r"\b((?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(?:,?\s+\d{4})?)\b", re.I)),
    ("date", re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")),
    ("percent", re.compile(r"\b(\d+(?:\.\d+)?)\s*(?:percent|%)", re.I)),
    ("money", re.compile(r"\$\s?([\d,]+(?:\.\d{2})?)|\b([\d,]{4,})\s+dollars\b", re.I)),
    ("duration", re.compile(r"\b(\d+\s+to\s+\d+|\d+)\s+(hours?|days?|weeks?|months?|years?|person-months?|person-weeks?)\b", re.I)),
    ("count", re.compile(r"\b(\d[\d,]*)\s+(vessels?|ports?|sailings?|candidates?|workers?|employees?|passengers?|items?|bullets?|seats?)\b", re.I)),
]

QUOTED = re.compile(r'"([^"]{25,})"')
CONDITIONAL = re.compile(r"\b(conditional|only if|if you|may never|might never|would need|unless|optional|your call|opt into|gated on)\b", re.I)


def walk(obj, path=""):
    """Yield (json_path, string) for every string leaf."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from walk(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from walk(v, f"{path}[{i}]")
    elif isinstance(obj, str) and obj.strip():
        yield path, obj


def sentences(text):
    for s in re.split(r"(?<=[.!?])\s+", text):
        s = s.strip()
        if len(s) > 20:
            yield s


def section_of(path):
    """Top-level study section, so we only compare across real boundaries."""
    parts = [p for p in path.split(".") if p]
    return parts[0].split("[")[0] if parts else "?"


def words(text):
    return {w for w in re.findall(r"[a-z][a-z'-]{3,}", text.lower()) if w not in STOP}


def jaccard(a, b):
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def extract_values(study):
    """Every measurable value, with the sentence and section it lives in."""
    out = []
    for path, text in walk(study):
        for sent in sentences(text):
            for kind, rx in PATTERNS:
                for m in rx.finditer(sent):
                    val = next((g for g in m.groups() if g), None)
                    if val is None:
                        continue
                    val = val.strip().lower().replace(",", "")
                    if kind == "duration":
                        val = f"{val} {m.group(2).lower().rstrip('s')}"
                        kind = "duration:" + m.group(2).lower().rstrip("s")
                    if kind == "count":
                        kind = "count:" + m.group(2).lower().rstrip("s")
                    out.append({"kind": kind, "value": val, "sentence": sent,
                                "path": path, "section": section_of(path),
                                "words": words(sent)})
    return out


MONTHS = set("""january february march april may june july august september october
november december""".split())
UNITS = set("""hours hour days day weeks week months month years year percent dollars
vessels vessel ports port sailings sailing candidates workers employees passengers
items bullets seats about roughly around least most more than over under""".split())


def subject_words(word_set):
    """What a sentence is ABOUT, with the measured thing itself stripped out.

    Two mentions of the same fact rarely share phrasing, but they nearly always
    share the subject noun. 'your season ends 6 October' and 'the 2026 season runs
    1 April to 1 October' agree on almost nothing except the word that matters.
    """
    return {w for w in word_set if w not in MONTHS and w not in UNITS and not w.isdigit()}


def find_conflicts(values, threshold=0.15):
    """Same kind of fact, same subject, different value.

    This is the 'your season ends 6 October' versus 'the season ends 1 October'
    detector. Two guards keep it honest. Mentions inside ONE sentence are never a
    conflict, because '1 April to 1 October' is a range and not a disagreement. And
    a cluster only counts when it spans more than one sentence.
    """
    conflicts = []
    by_kind = {}
    for v in values:
        by_kind.setdefault(v["kind"], []).append(v)

    for kind, items in by_kind.items():
        used = set()
        for i, a in enumerate(items):
            if i in used:
                continue
            cluster, used_now = [a], {i}
            for j, b in enumerate(items):
                if j in used or j in used_now or b["sentence"] == a["sentence"]:
                    continue
                shared = subject_words(a["words"]) & subject_words(b["words"])
                if shared and jaccard(a["words"], b["words"]) >= threshold:
                    cluster.append(b)
                    used_now.add(j)
            # Three guards against the obvious false positives, learned by running
            # this against a study that was already correct.
            #
            # SIBLINGS. roi.scenarios.conservative and .most_likely are SUPPOSED to
            # carry different numbers. Values under a shared parent are a designed
            # comparison, not a contradiction.
            parents = {c["path"].rsplit(".", 1)[0].rsplit("[", 1)[0] for c in cluster}
            if len(parents) < 2:
                used.add(i)
                continue
            # SAME VALUE SET. Gartner's "20 percent cut, 50 percent rehire" appears
            # in two sections and carries BOTH numbers in both. Two sentences that
            # list the same values agree, however many values that is.
            per_sentence = {}
            for c in cluster:
                per_sentence.setdefault(c["sentence"], set()).add(c["value"])
            if len(set(map(frozenset, per_sentence.values()))) < 2:
                used.add(i)
                continue
            # RANGES. "1 April to 1 October" is one span, not a disagreement.
            if len(per_sentence) < 2:
                used.add(i)
                continue
            used |= used_now
            conflicts.append({"kind": kind, "values": sorted({c["value"] for c in cluster}),
                              "mentions": cluster})
    return conflicts


def find_echoes(study, threshold=0.5):
    """The same claim restated in another section, in different words.

    Answers the question a critic's report cannot: where ELSE does this live. Only
    compares across top-level sections, because repetition inside one paragraph is
    usually deliberate.
    """
    sents = []
    for path, text in walk(study):
        for s in sentences(text):
            sents.append({"path": path, "section": section_of(path),
                          "sent": s, "words": words(s)})
    echoes = []
    for a, b in combinations(sents, 2):
        if a["section"] == b["section"]:
            continue
        sim = jaccard(a["words"], b["words"])
        if sim >= threshold:
            ca, cb = bool(CONDITIONAL.search(a["sent"])), bool(CONDITIONAL.search(b["sent"]))
            echoes.append({"similarity": round(sim, 2), "a": a, "b": b,
                           "conditional_mismatch": ca != cb})
    return sorted(echoes, key=lambda e: -e["similarity"])


def find_quote_drift(study):
    """A quoted span must read identically everywhere it is quoted.

    Matched fuzzily on purpose. Drift is usually one inserted or dropped word, and
    a prefix key would file the two variants apart precisely when they differ. On
    2026-07-29 a posting quote gained the word 'tour' between two sections, which
    is exactly the size of error a prospect catches by opening his own page.
    """
    quotes = []
    for path, text in walk(study):
        for m in QUOTED.finditer(text):
            q = m.group(1).strip()
            quotes.append({"quote": q, "path": path,
                           "toks": set(re.findall(r"[a-z]+", q.lower()))})
    drift, used = [], set()
    for i, a in enumerate(quotes):
        if i in used:
            continue
        group = [a]
        used.add(i)
        for j, b in enumerate(quotes):
            if j in used:
                continue
            if jaccard(a["toks"], b["toks"]) >= 0.75:
                group.append(b)
                used.add(j)
        variants = {g["quote"] for g in group}
        if len(variants) > 1:
            drift.append({"variants": sorted(variants),
                          "paths": [g["path"] for g in group]})
    return drift


def find_conditional_mismatch(study, max_spread=3):
    """A claim hedged in one section and asserted flat in another.

    Whole-sentence similarity cannot find this, because the hedged version and the
    unconditional version often share almost no vocabulary. What they share is the
    distinctive phrase naming the thing. On 2026-07-29 'templated fan out' was
    conditional in plan.phase1_later and unconditional in roadmap.now, and a
    funding gate ended up resting on a measurement that might never be collected.
    """
    idx = {}
    for path, text in walk(study):
        sec = section_of(path)
        for s in sentences(text):
            # Keep short words and stopwords IN the sequence. The phrase that names
            # the thing is often built from them ("fan out", "day one"), and
            # filtering them first destroys the adjacency the match depends on.
            toks = re.findall(r"[a-z][a-z'-]{2,}", s.lower())
            cond = bool(CONDITIONAL.search(s))
            for k in range(len(toks) - 1):
                bg = (toks[k], toks[k + 1])
                # Distinctive means at least one real content word carries it.
                # Both words must be content words, and at least one substantial.
                # "including the" dies on the stopword. "templated fan" survives,
                # because the phrase that names a thing often ends in a short word.
                # Requiring BOTH to be long killed the real case, so it does not.
                if not all(t not in STOP for t in bg):
                    continue
                if not any(len(t) >= 5 for t in bg):
                    continue
                idx.setdefault(bg, []).append(
                    {"path": path, "section": sec, "sent": s, "cond": cond})
    out, seen_pairs = [], set()
    for phrase, items in idx.items():
        if len(items) > max_spread:
            continue  # too common to be distinctive
        if len({i["section"] for i in items}) < 2:
            continue
        if len({i["cond"] for i in items}) < 2:
            continue
        key = tuple(sorted({i["path"] for i in items}))
        if key in seen_pairs:
            continue
        seen_pairs.add(key)
        out.append({"phrase": " ".join(phrase), "mentions": items})
    return out


def report(study, strict=False, echo_threshold=0.5):
    values = extract_values(study)
    conflicts = find_conflicts(values)
    echoes = find_echoes(study, echo_threshold)
    drift = find_quote_drift(study)
    cond = find_conditional_mismatch(study)

    print("=" * 72)
    print("CLAIM SWEEP")
    print("=" * 72)
    print(f"  {len(values)} measurable values, {len(echoes)} cross-section echoes\n")

    print(f"-- CONFLICTS ({len(conflicts)}) --  same kind of fact, different value")
    if not conflicts:
        print("   none\n")
    for c in conflicts:
        print(f"   [{c['kind']}] {' vs '.join(c['values'])}")
        for m in c["mentions"]:
            print(f"      {m['path']}  ->  {m['sentence'][:88]}")
        print()

    print(f"-- CONDITIONAL MISMATCH ({len(cond)}) --  same claim, hedged in one place only")
    if not cond:
        print("   none\n")
    for e in cond:
        print(f"   \"{e['phrase']}\"")
        for m in e["mentions"]:
            mark = "HEDGED    " if m["cond"] else "FLAT      "
            print(f"      {mark} {m['path']}  ->  {m['sent'][:76]}")
        print()

    print(f"-- QUOTE DRIFT ({len(drift)}) --  a quotation that differs between uses")
    if not drift:
        print("   none\n")
    for d in drift:
        print(f"   {d['paths']}")
        for v in d["variants"]:
            print(f"      {v[:88]}")
        print()

    print(f"-- ECHOES ({len(echoes)}) --  fix the claim in ALL of these, not just one")
    for e in echoes[:15]:
        print(f"   sim {e['similarity']}  {e['a']['section']} <-> {e['b']['section']}")
        print(f"      {e['a']['path']}  ->  {e['a']['sent'][:84]}")
        print(f"      {e['b']['path']}  ->  {e['b']['sent'][:84]}")
    if len(echoes) > 15:
        print(f"   ... and {len(echoes)-15} more")
    print()

    hard = len(conflicts) + len(drift) + len(cond)
    if hard:
        print(f"RESULT: {hard} item(s) need a decision before this ships.")
    else:
        print("RESULT: no conflicts, no quote drift, no conditional mismatch.")
    return 1 if (strict and hard) else 0


SELF_TEST = {
    "thesis": "Your season ends 6 October and about nine operating weeks remain.",
    "homework": {"business": "The 2026 season runs 1 April to 1 October."},
    "plan": {
        "metrics": [{"target": "The winter build proceeds only if the slice shows changes on a majority of operating days."}],
        "phase1_later": ["Templated fan out to outside parties, only if you decide they should hear from a system."],
        "problem": 'The posting says "Monitor updates to passenger counts and modify vessel schedules as needed."',
    },
    "roadmap": {
        "now": [{"item": "Templated fan out and acknowledgement tracking to motorcoach companies and caterers."}],
        "gates": "GATE 1 is funded only if the slice shows changes on a majority of operating days and exposure clearing three times the build cost.",
    },
    "build": {"feasibility": 'The posting says "Monitor updates to passenger counts and modify vessel tour schedules as needed."'},
}


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--study")
    p.add_argument("--strict", action="store_true", help="exit 1 when anything needs a decision")
    p.add_argument("--echo-threshold", type=float, default=0.5)
    p.add_argument("--self-test", action="store_true",
                   help="run against the real 2026-07-29 defects this script exists to catch")
    a = p.parse_args()

    if a.self_test:
        print("SELF-TEST, fixtures are the actual 2026-07-29 defects.\n")
        rc = report(SELF_TEST, strict=True, echo_threshold=0.45)
        print("\nExpected to catch: the 6 October / 1 October season conflict, the")
        print("quote that gained 'tour' between two sections, and the fan out that is")
        print("conditional in the plan and unconditional in the roadmap.")
        sys.exit(0 if rc == 1 else 1)  # self-test PASSES by finding problems

    if not a.study:
        p.error("--study is required unless --self-test")
    sys.exit(report(json.load(open(a.study)), a.strict, a.echo_threshold))


if __name__ == "__main__":
    main()
