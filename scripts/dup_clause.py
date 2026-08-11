#!/usr/bin/env python3
"""Mechanical duplicate-clause sweep.

Bought on 2026-08-10. Three separate visible strings in one demo shipped a
duplicated clause with the same signature: a replacement was inserted and the
original left standing. The study-critic caught all three by reading, which is
exactly the wrong tool for the job, so this is the mechanical answer.

A fix applied by insertion rather than substitution leaves the old wording
adjacent to the new one inside the SAME string. That is the signature this
looks for: a word n-gram repeating within a single line or a single JSON
string value. Cross-line repetition is normal in a document (headings echo
body copy on purpose) and is NOT flagged.

THE BLIND SPOT, NAMED BY THE STUDY-CRITIC ON 2026-08-10, THE DAY THIS WAS
WRITTEN. A CLEAN EXIT HERE IS NOT A CLEAN DOCUMENT. This compares STRINGS
inside ONE edit unit. It can't see the same CLAIM restated across two adjacent
units, and that is exactly where the duplication relocated once the
within-string cases were fixed: demo.html line 644 said "a guest who parked
their own car gets nothing from it at all" and line 647, rendered inches below
it in the same card, said "a guest who drove and parked has nothing covering
them at all". Two string literals, one claim, twice on screen. This tool
reported CLEAN on that and always will.

So run scripts/claim_sweep.py as well and read the artifact. A green exit here
means one specific failure mode is absent, the one where a fix is applied by
insertion and the original is left standing. It means nothing else.

THE SAME BLIND SPOT HAS A SECOND, MORE DANGEROUS FACE, AND IT IS A REASON TO
LEAVE SOMETHING ALONE RATHER THAN TO FIX IT. Text that only reaches the DOM at
runtime is invisible to study_qa too, so the house typography rules are not
enforced on it. demo.html carries an en dash inside SRC.c15, which is a
character-for-character quotation of the prospect's own check-in page. DO NOT
"FIX" IT. A verbatim quotation outranks a typography rule, the dash rule exists
to kill AI tells and quote fidelity exists to kill fabrication, and silently
repunctuating a prospect's sentence is the sharpening reflex the fact-checker
named on this run. Ruled by the study-critic on 2026-08-10 and closed.

SCOPE. Run this on the artifacts a human or an agent EDITS by hand, which today
means demo.html and study.json. Do not run it on a generated render such as
field-study.html: build_study_page.py emits the whole body on one line with
inlined base64 fonts, so there is no edit unit to reason about and every
deliberate echo between a heading and its body reports as a hit. The render is
covered by sweeping the study.json it was built from.

Usage:
    dup_clause.py FILE [FILE ...] [--n 4]

Exits 1 if any duplicate is found, 0 if clean.
"""
import argparse
import html
import json
import re
import sys

NUMBER_WORDS = set("""zero one two three four five six seven eight nine ten
eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen
twenty thirty forty fifty sixty seventy eighty ninety hundred thousand million
and a""".split())

# Boilerplate that legitimately repeats inside one line of markup.
IGNORE = re.compile(
    r"^(class|style|href|src|id|div|span|p|li|ul|td|tr|th|var|let|const|"
    r"function|return|if|else|px|em|rem|rgba?)$", re.I)


def visible_spans(path, text):
    """Yield (label, string) for each span a reader could actually see."""
    if path.endswith(".json"):
        try:
            data = json.loads(text)
        except json.JSONDecodeError:
            data = None
        if data is not None:
            stack = [("$", data)]
            while stack:
                where, node = stack.pop()
                if isinstance(node, dict):
                    for k, v in node.items():
                        stack.append((where + "." + str(k), v))
                elif isinstance(node, list):
                    for i, v in enumerate(node):
                        stack.append((where + "[%d]" % i, v))
                elif isinstance(node, str):
                    yield where, node
            return
    if path.endswith((".html", ".htm")):
        for span in html_spans(text):
            yield span
        return
    for i, line in enumerate(text.splitlines(), 1):
        yield "line %d" % i, line


SCRIPT = re.compile(r"<script\b[^>]*>(.*?)</script>", re.S | re.I)
LITERAL = re.compile(r'"((?:[^"\\\n]|\\.)*)"'
                     r"|'((?:[^'\\\n]|\\.)*)'"
                     r"|`((?:[^`\\]|\\.)*)`", re.S)


def html_spans(text):
    """Split HTML into the units a single edit touches.

    Markup outside <script> goes line by line. Inside <script>, each string
    LITERAL is its own span, because that is the unit a botched fix duplicates
    inside. Sweeping script blocks by line instead flags ordinary code
    repetition (`fired.push(...)` four times) and flags two branches of a
    ternary that legitimately share wording, neither of which is the defect.
    """
    def line_of(offset):
        return text.count("\n", 0, offset) + 1

    cut = []
    for m in SCRIPT.finditer(text):
        cut.append((m.start(1), m.end(1)))
        body = m.group(1)
        for lit in LITERAL.finditer(body):
            raw = next(g for g in lit.groups() if g is not None)
            if len(raw.split()) < 8:
                continue
            yield ("line %d string" % line_of(m.start(1) + lit.start()),
                   raw.replace("\\n", " ").replace('\\"', '"'))

    # Everything outside the script blocks, line by line, offsets preserved.
    masked = list(text)
    for start, end in cut:
        for i in range(start, end):
            if masked[i] != "\n":
                masked[i] = " "
    for i, line in enumerate("".join(masked).splitlines(), 1):
        if line.strip():
            yield "line %d" % i, line


def words(span):
    """Strip tags and entities, then return lowercase word tokens."""
    span = re.sub(r"<[^>]+>", " ", span)
    span = html.unescape(span)
    # Numerals are kept as tokens. Dropping them made "up to 72 hours before
    # departure" and "up to 24 hours before departure" collide into a false
    # duplicate, which is the opposite of what this gate is for.
    return [w for w in re.findall(r"[A-Za-z0-9][A-Za-z0-9'’-]*", span)
            if not IGNORE.match(w)]


def duplicates(span, n):
    """Maximal word runs of length >= n occurring twice inside this one span.

    Reports the longest contiguous repeat rather than every sliding window
    inside it, so one duplicated clause is one finding.
    """
    toks = [w.lower() for w in words(span)]
    size = len(toks)
    if size < n * 2:
        return []
    pos = {}
    for i, w in enumerate(toks):
        pos.setdefault(w, []).append(i)

    consumed = set()   # (i, j) pairs already inside a longer run
    hits = []
    for i in range(size):
        for j in pos[toks[i]]:
            if j <= i or (i, j) in consumed:
                continue
            k = 0
            # Stop at j so the two occurrences never overlap.
            while i + k < j and j + k < size and toks[i + k] == toks[j + k]:
                consumed.add((i + k, j + k))
                k += 1
            if k >= n:
                run = toks[i:i + k]
                # A spelled-out figure repeats on purpose. "four thousand five
                # hundred" naming the ask twice in one paragraph is the study
                # being clear, not a botched edit.
                if all(t in NUMBER_WORDS for t in run):
                    continue
                hits.append(" ".join(run))
    return sorted(set(hits))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--n", type=int, default=4,
                    help="clause length in words (default 4, the length that "
                         "caught all three 2026-08-10 defects)")
    args = ap.parse_args()

    bad = 0
    for path in args.files:
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        for where, span in visible_spans(path, text):
            for gram in duplicates(span, args.n):
                bad += 1
                print("DUP  %s  %s\n     repeated clause: %r"
                      % (path, where, gram))
    if bad:
        print("\n%d duplicated clause(s). A fix applied by insertion leaves "
              "the original standing, substitute instead." % bad)
        return 1
    print("dup_clause: clean (%d file(s), n=%d)" % (len(args.files), args.n))
    return 0


if __name__ == "__main__":
    sys.exit(main())
