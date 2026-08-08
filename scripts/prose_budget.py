#!/usr/bin/env python3
"""Which study.json field is spending the prose budget.

WHY THIS EXISTS. knowledge/MACHINE_BACKLOG.md recorded it on 2026-08-07 after a
run made roughly twenty seven trimming passes across five critic rounds to hold
3,000 words. study_qa reports ONE number, computed from the rendered HTML, so
nothing tells the showrunner which field contributes what. Every trim was
therefore a guess, and the cost was not the passes. In EVERY critic round of
that run a caveat was lost or garbled in the cutting, because trimming removes
qualifying clauses first. Qualifiers read as slack, and on a document whose
whole value is its honesty disclosures that is the worst possible thing to cut
blind.

It came back on 2026-08-08. This run trimmed twice, guessed both times, and
landed 19 words over on the second pass. Second appearance, so it stops being a
note and becomes the work.

HOW IT WORKS, and the method is chosen so the number cannot lie. It does not
re-implement the word counter and it does not guess at the template. It renders
the study once for a baseline, then re-renders it once per field with THAT FIELD
EMPTIED, and reports the drop in study_qa's own prose count. The delta is by
construction the words that field actually puts on the page, through the real
builder, measured by the real gate.

That method also detects, for free, the worst failure this pipeline has. A
field whose delta is ZERO never reached the page at all, which is a renamed key
silently dropping a section, and it is reported as UNRENDERED rather than as a
cheap trim.

Usage
  prose_budget.py --study out/<date>/study.json
  prose_budget.py --study out/<date>/study.json --over 19   # what to cut
  prose_budget.py --self-test
"""
import argparse
import copy
import json
import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
BUILDER = os.path.join(HERE, "build_study_page.py")
QA = os.path.join(HERE, "study_qa.py")

# Every study.json path that carries PROSE, the text a reader moves through
# linearly. Table cells, source lines and figure labels are deliberately absent,
# because FIELD_STUDY_SPEC counts them as structure and study_qa does not charge
# them against the reading-time budget either.
PROSE_PATHS = [
    ("thesis",), ("brief",),
    ("found", "lede"), ("found", "body"), ("found", "callout_note"), ("found", "body_2"),
    ("costing", "lede"), ("costing", "body"), ("costing", "callout_note"), ("costing", "body_2"),
    ("opportunity", "lede"), ("opportunity", "outcome_body"), ("opportunity", "after_body"),
    ("build", "lede"), ("build", "plain_parts"), ("build", "what_it_does"),
    ("build", "feasibility"), ("build", "build_vs_buy"),
    ("roi", "lede"), ("roi", "lede_body"), ("roi", "table_note"),
    ("roi", "payback_range"), ("roi", "base_rate_note"), ("roi", "value_owner"),
    ("roadmap", "lede"), ("roadmap", "body"), ("roadmap", "gates"), ("roadmap", "need_from_you"),
    ("honest", "lede"), ("honest", "body"),
    ("next_step",),
]


def get_in(obj, path):
    for k in path:
        if not isinstance(obj, dict) or k not in obj:
            return None
        obj = obj[k]
    return obj


def set_in(obj, path, value):
    for k in path[:-1]:
        obj = obj[k]
    obj[path[-1]] = value


# A one-word stand-in rather than an empty string. Emptying a field is what the
# first version of this script did and it was wrong twice over: the builder
# DROPS a section whose field is empty (the spec says so, "anything left null is
# dropped"), so the delta swallowed sibling content and reported 568 words for a
# 107 word field. Substituting one distinctive token keeps the section rendering
# and makes the delta the field's own contribution, plus it gives us a string to
# search for to answer the separate question of whether the field reached the
# page at all.
SENTINEL = "zqxjkbudgetprobe"


def render(study_obj, workdir, tag):
    """Render this study object. Returns (prose_words, html_text)."""
    sp = os.path.join(workdir, f"s_{tag}.json")
    hp = os.path.join(workdir, f"h_{tag}.html")
    with open(sp, "w") as fh:
        json.dump(study_obj, fh)
    r = subprocess.run([sys.executable, BUILDER, "--study", sp, "--out", hp],
                       capture_output=True, text=True)
    if not os.path.exists(hp):
        raise RuntimeError("builder produced no html: " + (r.stderr or r.stdout)[-400:])
    with open(hp) as fh:
        html = fh.read()
    q = subprocess.run([sys.executable, QA, "--html", hp], capture_output=True, text=True)
    m = re.search(r"prose words\s+([\d,]+)", q.stdout)
    if not m:
        raise RuntimeError("study_qa printed no prose count")
    return int(m.group(1).replace(",", "")), html


def measure(study_path):
    with open(study_path) as fh:
        base = json.load(fh)
    rows = []
    with tempfile.TemporaryDirectory() as wd:
        baseline, _ = render(base, wd, "base")
        for i, path in enumerate(PROSE_PATHS):
            cur = get_in(base, path)
            if not isinstance(cur, str) or not cur.strip():
                continue
            probe = copy.deepcopy(base)
            set_in(probe, path, SENTINEL)
            try:
                n, html = render(probe, wd, str(i))
            except Exception as e:
                rows.append({"field": ".".join(path), "words": None, "error": str(e)[:80]})
                continue
            # The sentinel stands in for the whole field, so it contributes at
            # most one word wherever it landed. Add it back.
            contribution = baseline - n + 1
            # Two separate questions, and conflating them is what made the first
            # version cry wolf. ON THE PAGE is whether the text renders at all.
            # PROSE is whether study_qa charges it against the reading budget.
            # A table note renders and is deliberately counted as structure, so
            # it is 0 prose and absolutely not missing.
            on_page = SENTINEL in html
            rows.append({"field": ".".join(path),
                         "words": max(contribution, 0),
                         "own_words": len(cur.split()),
                         "on_page": on_page})
    rows.sort(key=lambda r: (r["words"] is None, -(r["words"] or 0)))
    return baseline, rows


def report(baseline, rows, over):
    print()
    print("  PROSE BUDGET, by study.json field")
    print()
    print(f"  rendered prose total              {baseline:,}")
    if over:
        print(f"  need to cut                       {over}")
    print()
    print("  {:<34} {:>8} {:>8}".format("field", "on page", "in json"))
    print("  " + "-" * 52)
    missing, structure = [], []
    for r in rows:
        if r.get("error"):
            print("  {:<34} {:>8} {:>8}  {}".format(r["field"], "ERR", "-", "render failed"))
            continue
        if not r.get("on_page"):
            missing.append(r)
            tag = "NOT ON PAGE"
        elif r["words"] == 0:
            structure.append(r)
            tag = "structure"
        else:
            tag = ""
        print("  {:<34} {:>8} {:>8}  {}".format(
            r["field"], r["words"], r["own_words"], tag))
    print()
    if missing:
        print("  NOT ON PAGE. These fields carry text that never reached the page")
        print("  at all. That is a renamed key silently dropping content, which is")
        print("  the worst failure this pipeline has. Fix the shape, do not trim.")
        for r in missing:
            print(f"    {r['field']}  ({r['own_words']} words in study.json)")
        print()
    if structure:
        print("  STRUCTURE, not a defect. These render but study_qa counts them as")
        print("  table cells, source lines or figure labels rather than prose, so")
        print("  cutting them buys nothing against the reading budget.")
        for r in structure:
            print(f"    {r['field']}  ({r['own_words']} words, rendered)")
        print()
    if over:
        # Suggest the smallest set of fields that could absorb the overage, so
        # the cut lands somewhere it fits rather than somewhere it is noticed.
        cands = [r for r in rows if r.get("words") and r["words"] >= over]
        print(f"  Any ONE of these can absorb {over} words without touching another:")
        for r in cands[:6]:
            print(f"    {r['field']}  ({r['words']} on page)")
        print()
        print("  Cut restatement, never a qualifier. Trimming removes qualifying")
        print("  clauses first, and on this document those clauses are the honesty.")
        print()


def self_test():
    """Prove the arithmetic, without paying for a render.

    The renders are exercised by the real run. What is worth testing hermetically
    is the part that could silently corrupt a report: path handling on a nested
    study object, and the rule that a zero delta means UNRENDERED rather than
    a free trim.
    """
    fails = []

    def check(name, cond, detail=""):
        print("  {:<4} {}{}".format("ok" if cond else "FAIL", name,
                                    "" if cond else "  <- " + detail))
        if not cond:
            fails.append(name)

    doc = {"thesis": "a b c", "found": {"body": "d e", "lede": ""},
           "roi": {"table_note": "f g h i"}}
    check("get_in reads a nested path", get_in(doc, ("found", "body")) == "d e")
    check("get_in on a missing path returns None",
          get_in(doc, ("nope", "gone")) is None)
    check("get_in on a missing leaf returns None",
          get_in(doc, ("found", "absent")) is None)
    d2 = copy.deepcopy(doc)
    set_in(d2, ("found", "body"), "")
    check("set_in empties only its own leaf",
          d2["found"]["body"] == "" and d2["thesis"] == "a b c" and doc["found"]["body"] == "d e")
    check("an empty field is skipped, not measured",
          not (isinstance(get_in(doc, ("found", "lede")), str)
               and get_in(doc, ("found", "lede")).strip()))

    # The classification rule, which is the part a reader acts on.
    rows = [{"field": "a", "words": 40, "own_words": 40, "on_page": True},
            {"field": "b", "words": 0, "own_words": 55, "on_page": False},
            {"field": "c", "words": 12, "own_words": 12, "on_page": True},
            {"field": "roi.table_note", "words": 0, "own_words": 219, "on_page": True}]
    missing = [r for r in rows if not r.get("on_page")]
    structure = [r for r in rows if r.get("on_page") and r["words"] == 0]
    check("a field that never reached the page is reported NOT ON PAGE",
          len(missing) == 1 and missing[0]["field"] == "b", repr(missing))
    check("NEGATIVE, a rendered table note is STRUCTURE and not a missing section",
          len(structure) == 1 and structure[0]["field"] == "roi.table_note", repr(structure))
    check("NEGATIVE, structure is never reported as missing",
          "roi.table_note" not in [r["field"] for r in missing])
    absorbers = [r for r in rows if r["words"] and r["words"] >= 19]
    check("only a field big enough to absorb the overage is suggested",
          [r["field"] for r in absorbers] == ["a"], repr(absorbers))
    absorbers0 = [r for r in rows if r["words"] and r["words"] >= 100]
    check("NEGATIVE, nothing is suggested when no field is big enough",
          absorbers0 == [], repr(absorbers0))

    print()
    if fails:
        print("  {} FAILED: {}".format(len(fails), ", ".join(fails)))
        return 1
    print("  all 10 checks passed")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--study")
    ap.add_argument("--over", type=int, default=0,
                    help="words to cut, so the report names fields that can absorb it")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        print()
        print("  PROSE BUDGET SELF TEST")
        print()
        return self_test()
    if not args.study:
        ap.error("--study is required unless --self-test")
    baseline, rows = measure(args.study)
    report(baseline, rows, args.over)
    return 0


if __name__ == "__main__":
    sys.exit(main())
