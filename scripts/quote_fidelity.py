#!/usr/bin/env python3
"""Every quoted span in the demo must still be its source's words.

HONESTY names one unforgivable failure, a fabricated fact, and the fact-checker
named the way it actually happens on this desk: a SHARPENING REFLEX, where a
quote rebuilt from memory comes back rebuilt in the direction of the point it
was supporting. The study-critic has ruled twice that a verbatim quotation
outranks our own house typography, so a prospect's punctuation is left exactly
as they wrote it.

Bought on 2026-08-10. A round-8 fix asked for house ordinals on the demo's date
strings, and the honest way to apply that to 30-odd strings is a bulk regex over
the file. That file also holds every verbatim quotation the demo shows. The
sweep happened to be safe, because the pattern required a digit followed by
whitespace or punctuation and the quoted dates already carried ordinals, but
that was luck rather than design, and it was only checked afterwards by hand.
A bulk edit over a file containing quotations needs a gate, not a spot check.

WHAT IT DOES. Pulls every string in the demo's SRC table and asserts each is a
substring of the matching quote in claims.json, comparing on collapsed
whitespace only. Punctuation, capitalisation, dashes and spelling must match
character for character, because those are exactly what a sharpening reflex
edits. A span whose id has no quote in claims.json is reported, not skipped.

Usage:
    quote_fidelity.py --demo out/<date>/demo.html --claims out/<date>/claims.json

Exits 1 on any drift.
"""
import argparse
import json
import re
import sys

SRC_BLOCK = re.compile(r"var SRC\s*=\s*\{.*?\n\};", re.S)
ENTRY = re.compile(r"(c\d+)\s*:\s*\{\s*parts\s*:\s*\[(.*?)\]\s*,", re.S)
STRING = re.compile(r'"((?:[^"\\]|\\.)*)"')


def collapse(text):
    """Whitespace is layout. Everything else is the source's own writing."""
    return re.sub(r"\s+", " ", text.replace('\\"', '"')).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--demo", required=True)
    ap.add_argument("--claims", required=True)
    args = ap.parse_args()

    claims = json.load(open(args.claims, encoding="utf-8"))
    quotes = {}
    for key in ("verified_company_facts", "verified_industry_claims",
                "verified_claims"):
        for entry in claims.get(key, []):
            if isinstance(entry, dict) and entry.get("quote"):
                quotes.setdefault(entry["id"], entry["quote"])

    demo = open(args.demo, encoding="utf-8").read()
    block = SRC_BLOCK.search(demo)
    if not block:
        print("FAIL  no SRC table found in", args.demo)
        return 1

    checked = drifted = unsourced = 0
    for match in ENTRY.finditer(block.group(0)):
        cid, raw = match.group(1), match.group(2)
        spans = STRING.findall(raw)
        if cid not in quotes:
            unsourced += 1
            print("NOTE  %s has %d quoted span(s) and no quote in claims.json"
                  % (cid, len(spans)))
            continue
        for span in spans:
            checked += 1
            if collapse(span) not in collapse(quotes[cid]):
                drifted += 1
                print("DRIFT %s\n  demo  : %s\n  claims: %s"
                      % (cid, collapse(span), collapse(quotes[cid])))

    if drifted:
        print("\n%d quoted span(s) no longer match the source. A quote is not "
              "ours to tidy, restore it character for character." % drifted)
        return 1
    print("quote_fidelity: %d span(s) match their source exactly%s"
          % (checked, ", %d id(s) unsourced" % unsourced if unsourced else ""))
    return 1 if unsourced else 0


if __name__ == "__main__":
    sys.exit(main())
