#!/usr/bin/env python3
"""Catch the study defects a script can catch, before a critic spends a round on them.

Written 2026-08-05. The study-critic returned TWELVE blocking items that day and
at least five of them were mechanical, which means five expensive adversarial
rounds were spent on things a regex and some arithmetic could have caught in
milliseconds. Worse, mechanical noise buries the judgement calls that actually
need a critic, so the critic gets slower AND less useful at the same time.

This runs BEFORE any critic sees the study. It is a gate, not a report, because
every check here is a fact rather than a taste. claim_sweep.py stays a report,
because finding the same claim in two places needs judgement and this does not.

WHAT IT CHECKS, and every one of these is a defect that actually shipped:

  1. FORBIDDEN CLAIMS. claims.json carries a rejected_do_not_use list written by
     the fact-checker. On 2026-08-05 a rejected claim came back in different
     words two sections away, which is the documented failure mode this whole
     pipeline keeps paying for. A rejection is worthless if nothing enforces it.

  2. UNSOURCED URLS AND UNCITED SOURCES. The MIT and RAND figures shipped in a
     draft with no entry in sources[], so they were the only two numbers a
     reader could not trace to a link we gave them.

  3. PROVENANCE HONESTY. A row marked `verified` must correspond to something the
     fact-checker actually verified. A draft marked an ABSENCE as verified, which
     reads to a skeptic as "verified figures" when it means the opposite.

  4. ROI RECONCILIATION. Recompute every derived cell from the stated drivers and
     fail on mismatch. A draft shipped a recovery row and a break-even row sitting
     on DIFFERENT BASES, so 2 divided by 4.2 printed as 43 percent when it is 48.
     An owner with a calculator finds that in a minute. Arithmetic belongs in code.

  5. UNVERIFIABLE NEGATIVES. The drift pattern, mechanised. Every run of this
     routine has leaned the same way, toward making the prospect look more
     strained than their own pages support, and the specific tell is an asserted
     negative about their internal operation that nobody outside could know.
     "Nothing dated carries the new answer to three separate desks" is not a
     finding, it is a guess wearing a finding's clothes.

Usage:
  python scripts/study_lint.py --study out/<date>/study.json \\
      [--claims out/<date>/claims.json] [--drivers out/<date>/roi_drivers.json]
"""
import argparse
import json
import os
import re
import sys

# The ROI check delegates every figure to roi_math rather than recomputing it.
# One implementation of the arithmetic, in the module the showrunner already
# runs, so the gate and the study can never be reconciling different formulas.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import roi_math  # noqa: E402

# Negative assertions about the prospect's own operation. Each of these was
# either shipped or nearly shipped, and none of them is knowable from outside.
NEGATIVE_PATTERNS = [
    r"\bnothing\s+(?:dated\s+)?(?:carries|exists|tracks|records|tells|shows|connects)\b",
    r"\bno\s+(?:one|body|process|system|record|owner|dated)\b[^.]{0,60}\b(?:carries|exists|tracks|owns|checks)\b",
    r"\bnowhere\s+a\s+\w+\s+can\b",
    r"(?:^|[.;,]\s*)they\s+have\s+no\b",
    r"(?:^|[.;,]\s*)you\s+have\s+no\b",
    r"\bnobody\s+(?:at|in|on)\s+(?:your|the)\b",
    r"\bis\s+not\s+written\s+down\s+anywhere\b",
]

# Phrasings that make the same statement HONEST, because they scope it to what we
# could actually see rather than to what is true inside their building.
HEDGES = [
    "we could find no", "we could not find", "we have no way to know",
    "nothing we verified", "we found no", "not published", "we could not verify",
    "no verified", "nothing verifiable", "we saw no",
]


NOTES = []


def walk(obj, path=""):
    """Yield (path, string) for every string in the study object."""
    if isinstance(obj, str):
        yield path, obj
    elif isinstance(obj, dict):
        for k, v in obj.items():
            yield from walk(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from walk(v, f"{path}[{i}]")


def norm(s):
    return re.sub(r"[^a-z0-9 ]+", " ", (s or "").lower())


def check_forbidden(study, claims, fail, warn):
    body = " ".join(t for _, t in walk(study))
    nbody = norm(body)

    # EXACT strings the fact-checker says must never appear. This is the precise
    # channel and it is the one that fails the build.
    for span in (claims.get("forbidden_strings") or []):
        if norm(span).strip() and norm(span).strip() in nbody:
            fail(f"FORBIDDEN STRING back in the study: {span[:80]!r}")

    # The prose rejection list is advisory only. Pulling a quoted fragment out of
    # a sentence loses the thing that made it a rejection. On 2026-08-05
    # 'mid-May to mid-September' was rejected AS BEAR LODGE'S ROOM SEASON and is
    # perfectly correct for the restaurant, and a fragment match cannot tell those
    # apart. So it warns, a human reads it, and precision lives in
    # forbidden_strings instead.
    for r in (claims.get("rejected_do_not_use") or []):
        spans = [a or b for a, b in re.findall(r"'([^']{25,})'|\"([^\"]{25,})\"", r)]
        for span in spans:
            if norm(span).strip() and norm(span).strip() in nbody:
                warn(f"a rejected claim's wording appears in the study: {span[:70]!r}\n"
                     f"        check the context, the rejection was: {r[:110]}")


def check_sources(study, fail, warn):
    sources = study.get("sources") or []
    listed = {(s.get("url") or "").rstrip("/") for s in sources}
    body_urls = set()
    for path, text in walk(study):
        if path.startswith(".sources"):
            continue
        for u in re.findall(r"https?://[^\s)\"'<>]+", text):
            body_urls.add(u.rstrip(".,").rstrip("/"))
    for u in body_urls:
        if u not in listed:
            fail(f"URL in the body with no entry in sources[]: {u}")
    if not sources:
        fail("the study lists no sources at all")


def check_provenance(study, claims, fail, warn):
    roi = study.get("roi") or {}
    rows = roi.get("table") or []
    verified_claims = claims.get("verified_claims") or []
    have_verified = bool(verified_claims)
    for r in rows:
        if r.get("mark") != "verified":
            continue
        label = (r.get("label") or "")
        cells = " ".join(str(c) for c in (r.get("cells") or []))
        # A bare \bno\b matched any cell containing the word, so a legitimate
        # verified row reading "no more than 12" or "no charge" hard-failed as
        # an asserted absence. Match the phrasings that actually MEAN nothing is
        # there, not every use of the word.
        absence_cell = (r"\bnone\b|\bzero\b|\bn/?a\b|\bno (?:figures?|data|"
                        r"records?|evidence|numbers?|basis|source)\b|"
                        r"^\s*[-–—]\s*$|^\s*$")
        if re.search(absence_cell, cells, re.I) or \
           re.search(r"\bnone\b|\bno figures?\b", label, re.I):
            fail("a row marked `verified` states an ABSENCE, which reads as "
                 f"'verified figures' and means the opposite: {label!r}\n"
                 "        drop the row, the provenance key already tells the "
                 "reader nothing is verified when no verified mark appears")
        elif not have_verified:
            fail(f"row marked `verified` but claims.json has no verified claims: {label!r}")
    marks = {r.get("mark") for r in rows if r.get("mark")}
    if rows and not marks:
        warn("no provenance marks on the ROI table at all, the honesty rail is missing")


def check_roi(study, drivers, fail, warn, drivers_path=None):
    """Recompute every derived cell from the stated drivers, on ONE basis.

    Every early return here is LOUD. This is the most valuable check in the file
    and a silent skip would let a study pass the gate with its arithmetic never
    examined, which is precisely the failure this script exists to prevent.
    """
    roi = study.get("roi") or {}
    rows = {(r.get("label") or "").lower(): r for r in (roi.get("table") or [])}
    has_table = bool(rows)

    if not drivers:
        if has_table:
            fail("ROI CHECK DID NOT RUN. The study prints an ROI table and no "
                 f"drivers file was found at {drivers_path or 'the default path'}. "
                 "Every number in that table is unverified by this gate. Pass "
                 "--drivers, or say in the run log why the table has no drivers "
                 "behind it.")
        return
    if not has_table:
        return
    order = ["conservative", "most_likely", "aggressive"]
    scen = drivers.get("scenarios") or {}
    missing = [k for k in order if k not in scen]
    if missing:
        fail("ROI CHECK DID NOT RUN. The drivers file is missing scenario(s) "
             f"{missing}, so the printed table was not reconciled against anything.")
        return

    # LABEL FRAGMENTS, several per figure. A table may legitimately word a row
    # differently, and the point of tracking them is that a NO-MATCH is loud
    # rather than silent, which is what went wrong here before.
    WANT = {
        "annual":    ("annual value", "annual benefit", "annual "),
        "tco":       ("total cost", "five-year total", "5-year total", " tco"),
        "recovered": ("recovered", "recovery", "share of"),
        "breakeven": ("break-even", "break even", "breakeven"),
    }

    def cell(frags, i):
        """The cell for a figure, plus the label it matched. None when nothing did."""
        for lab, r in rows.items():
            if any(f in lab for f in frags):
                cells = r.get("cells") or []
                if i < len(cells):
                    return str(cells[i]), lab
        return None, None

    def num(s):
        if s is None:
            return None
        m = re.findall(r"-?[\d,]+\.?\d*", s.replace(",", ""))
        return float(m[0]) if m else None

    # The break-even row is expressed in units of ONE driver, and which driver
    # that is cannot be guessed from the table. Naming it in the drivers file is
    # what lets the cross-basis check survive a build that is not this hotel.
    be_cfg = drivers.get("break_even") or {}
    be_key = be_cfg.get("unit_key")

    checked = 0
    compared = 0

    for i, name in enumerate(order):
        s = scen[name]

        # ONE implementation of the arithmetic, in roi_math, which is what the
        # showrunner runs and what the study's numbers come from. This used to
        # be a second hand-written copy keyed on a vocabulary invented for one
        # hotel study (shifts_per_day, minutes_per_interruption), so any other
        # build hard-failed the gate, and today's drivers file only passed
        # because it redundantly carried BOTH schemas with nothing checking they
        # agreed. A checker that reimplements the thing it checks is checking
        # itself.
        try:
            got = roi_math.compute(name, s)
        except (KeyError, TypeError, ZeroDivisionError) as e:
            fail(f"ROI {name}: the drivers do not fit the schema roi_math.py "
                 f"documents and consumes ({e}). Expected pursuits_per_year, "
                 "benefit_lines[hours_per_pursuit, rate, cut], implementation, "
                 "training, run_cost_per_year, run_cost_years, contingency, "
                 "year1_ramp, years. This column's printed numbers were not "
                 "reconciled against anything.")
            continue
        checked += 1

        annual = got["annual_run_rate_benefit"]
        tco = next(v for k, v in got.items() if k.startswith("tco_"))
        recovered = got["percent_of_tco_recovered"]

        hits = 0

        printed_annual, lab = cell(WANT["annual"], i)
        printed_annual = num(printed_annual)
        if printed_annual is not None:
            hits += 1
            if abs(printed_annual - annual) > max(2.0, annual * 0.01):
                fail(f"ROI {name}: annual benefit prints {printed_annual:,.0f}, "
                     f"drivers give {annual:,.0f}  (row {lab!r})")

        printed_tco, lab = cell(WANT["tco"], i)
        printed_tco = num(printed_tco)
        if printed_tco is not None:
            hits += 1
            if abs(printed_tco - tco) > max(2.0, tco * 0.01):
                fail(f"ROI {name}: five-year cost prints {printed_tco:,.0f}, "
                     f"drivers give {tco:,.0f}  (row {lab!r})")

        printed_rec, lab = cell(WANT["recovered"], i)
        printed_rec = num(printed_rec)
        if printed_rec is not None:
            hits += 1
            if abs(printed_rec - recovered) > 2.0:
                fail(f"ROI {name}: recovery prints {printed_rec:.0f}%, "
                     f"drivers give {recovered:.0f}%  (row {lab!r})")

        printed_be, be_lab = cell(WANT["breakeven"], i)
        printed_be = num(printed_be)
        if printed_be is not None:
            hits += 1
            if not be_key:
                warn(f"ROI {name}: the table prints a break-even row ({be_lab!r}) "
                     "and the drivers file does not say which driver it is "
                     "counted in. Add break_even.unit_key so the row can be "
                     "reconciled instead of trusted.")
            elif be_key not in s:
                fail(f"ROI {name}: break_even.unit_key is {be_key!r}, which is "
                     "not a driver in this scenario, so the break-even row was "
                     "not reconciled.")
            elif recovered > 0:
                # THE ONE THAT ACTUALLY SHIPPED WRONG. Recovery and break-even
                # must sit on the same basis: break-even units over modelled
                # units equals 100 over the recovered percentage, whatever the
                # unit happens to be. On 2026-08-05 the two rows were computed
                # on different bases and only a careful fact-checker caught it.
                expect_be = s[be_key] * 100.0 / recovered
                half = 0.05
                hi = s[be_key] * 100.0 / max(recovered - half, 1e-9)
                lo = s[be_key] * 100.0 / (recovered + half)
                tol = max(abs(hi - lo) / 2.0, 0.15)
                if abs(printed_be - expect_be) > tol:
                    fail(f"ROI {name}: the recovery row and the break-even row sit "
                         f"on DIFFERENT BASES. At {recovered:.0f}% recovered, "
                         f"break-even is {expect_be:.2f} {be_key}, the table "
                         f"prints {printed_be:.2f}. A reader with a calculator "
                         "finds this.")

        compared += hits
        if hits == 0:
            # THE SILENT SKIP. `checked` used to be incremented here regardless,
            # so relabelling a row made this print "ok ROI reconciled across 3
            # scenario(s)" while comparing zero numbers. A gate that passes
            # everything is worse than no gate, because it looks like coverage.
            fail(f"ROI {name}: NOT ONE PRINTED CELL WAS RECONCILED. No row label "
                 "matched anything this check knows how to verify.\n"
                 f"        table rows: {sorted(rows)}\n"
                 "        looked for labels containing: "
                 + "; ".join("/".join(v) for v in WANT.values()))

    if checked and compared:
        NOTES.append(f"ROI reconciled across {checked} scenario(s), {compared} "
                     f"printed cell(s) recomputed from "
                     f"{os.path.basename(drivers_path or 'roi_drivers.json')}")
    elif checked:
        fail("ROI CHECK COMPARED NOTHING. Every scenario parsed and no printed "
             "cell matched a label this check understands, so the table is "
             "unverified despite the drivers file being present and valid.")


def check_negatives(study, fail, warn):
    for path, text in walk(study):
        if path.startswith(".sources"):
            continue
        for sentence in re.split(r"(?<=[.!?])\s+", text):
            low = sentence.lower()
            if any(h in low for h in HEDGES):
                continue
            for pat in NEGATIVE_PATTERNS:
                if re.search(pat, low):
                    warn("UNVERIFIABLE NEGATIVE about the prospect at "
                         f"{path}\n        {sentence.strip()[:150]}\n"
                         "        say what we could SEE, not what is true inside "
                         "their building. 'We could find no...' is honest, "
                         "'nothing carries...' is a guess.")
                    break


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--study", required=True)
    ap.add_argument("--claims")
    ap.add_argument("--drivers")
    ap.add_argument("--strict", action="store_true",
                    help="treat warnings as failures too")
    a = ap.parse_args()

    study = json.load(open(a.study))
    d = os.path.dirname(a.study)
    claims_p = a.claims or os.path.join(d, "claims.json")
    drivers_p = a.drivers or os.path.join(d, "roi_drivers.json")
    claims = json.load(open(claims_p)) if os.path.exists(claims_p) else {}
    drivers = json.load(open(drivers_p)) if os.path.exists(drivers_p) else None

    fails, warns = [], []
    fail = fails.append
    warn = warns.append

    check_forbidden(study, claims, fail, warn)
    check_sources(study, fail, warn)
    check_provenance(study, claims, fail, warn)
    check_roi(study, drivers, fail, warn, drivers_p)
    check_negatives(study, fail, warn)

    print("\n  STUDY LINT  —  {}\n".format(a.study))
    for n in NOTES:
        print("  ok    " + n)
    for f in fails:
        print("  FAIL  " + f)
    for w in warns:
        print("  WARN  " + w)
    if not fails and not warns:
        print("  clean, nothing mechanical left for a critic to spend a round on")
    print("\n  {} failure(s), {} warning(s)\n".format(len(fails), len(warns)))
    return 1 if (fails or (a.strict and warns)) else 0


if __name__ == "__main__":
    sys.exit(main())
