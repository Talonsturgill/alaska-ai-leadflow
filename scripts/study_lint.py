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
        if re.search(r"\bnone\b|\bzero\b|\bno\b|^\s*-\s*$", cells, re.I) or \
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


def check_roi(study, drivers, fail, warn):
    """Recompute every derived cell from the stated drivers, on ONE basis."""
    if not drivers:
        return
    roi = study.get("roi") or {}
    rows = {(r.get("label") or "").lower(): r for r in (roi.get("table") or [])}
    if not rows:
        return
    order = ["conservative", "most_likely", "aggressive"]
    scen = drivers.get("scenarios") or {}
    if not all(k in scen for k in order):
        return

    def cell(label_frag, i):
        for lab, r in rows.items():
            if label_frag in lab:
                cells = r.get("cells") or []
                if i < len(cells):
                    return str(cells[i])
        return None

    def num(s):
        if s is None:
            return None
        m = re.findall(r"-?[\d,]+\.?\d*", s.replace(",", ""))
        return float(m[0]) if m else None

    for i, name in enumerate(order):
        s = scen[name]
        try:
            annual = (s["shifts_per_day"] * 365
                      * (s["minutes_per_interruption"] / 60.0)
                      * s["loaded_hourly_rate"] * s["interruptions_prevented_per_shift"])
            basis = s["year1_ramp"] + (s["years"] - 1)
            tco = (s["implementation"] + s["training"]
                   + s["run_cost_per_year"] * s["run_cost_years"]) * (1 + s["contingency"])
            per_unit = annual / s["interruptions_prevented_per_shift"]
            be = tco / (per_unit * basis)
            recovered = 100.0 * (annual * basis) / tco
        except (KeyError, ZeroDivisionError):
            continue

        printed_annual = num(cell("annual value", i))
        if printed_annual is not None and abs(printed_annual - annual) > max(2.0, annual * 0.01):
            fail(f"ROI {name}: annual benefit prints {printed_annual:,.0f}, "
                 f"drivers give {annual:,.0f}")

        printed_tco = num(cell("five-year total", i))
        if printed_tco is not None and abs(printed_tco - tco) > max(2.0, tco * 0.01):
            fail(f"ROI {name}: five-year cost prints {printed_tco:,.0f}, "
                 f"drivers give {tco:,.0f}")

        printed_rec = num(cell("recovered", i))
        printed_be = num(cell("break-even", i))
        if printed_rec is not None and abs(printed_rec - recovered) > 2.0:
            fail(f"ROI {name}: recovery prints {printed_rec:.0f}%, "
                 f"drivers give {recovered:.0f}%")
        if printed_be is not None and abs(printed_be - be) > 0.15:
            fail(f"ROI {name}: break-even prints {printed_be:.2f}, "
                 f"drivers give {be:.2f}")
        # The one that actually shipped wrong: two rows on different bases.
        if printed_rec is not None and printed_be is not None and printed_be > 0:
            implied = 100.0 * s["interruptions_prevented_per_shift"] / printed_be
            # Slack from the printed rounding of break-even itself, plus a point.
            half = 0.05
            hi = 100.0 * s["interruptions_prevented_per_shift"] / max(printed_be - half, 1e-9)
            lo = 100.0 * s["interruptions_prevented_per_shift"] / (printed_be + half)
            tol = max(abs(hi - lo) / 2.0, 1.0) + 1.0
            if abs(implied - printed_rec) > tol:
                fail(f"ROI {name}: the recovery row and the break-even row sit on "
                     f"DIFFERENT BASES. {s['interruptions_prevented_per_shift']} "
                     f"divided by {printed_be} implies {implied:.0f}%, the table "
                     f"prints {printed_rec:.0f}%. A reader with a calculator finds this.")


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
    check_roi(study, drivers, fail, warn)
    check_negatives(study, fail, warn)

    print("\n  STUDY LINT  —  {}\n".format(a.study))
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
