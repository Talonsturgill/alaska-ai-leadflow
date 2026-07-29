#!/usr/bin/env python3
"""Git-backed memory of record for the lead-flow routine.

Supabase remains the inbound-scanner queue and the analytics store, but dedupe
no longer depends on it. The ledger files under ledger/ are committed to this
private repo every run, so the routine can always answer the only two questions
that gate a run: have we contacted this company, and did a run already ship
today.

Dedupe is computed here rather than narrated by the model, the same way ROI
arithmetic is computed in roi_math.py. A domain either matches the ledger or it
does not, and that answer is not a judgement call.

Usage
  ledger.py normalize <domain>
  ledger.py exclude-set [--json]
  ledger.py check <domain> [<domain> ...]      exit 1 if ANY is excluded
  ledger.py ran-today [--date YYYY-MM-DD]      exit 0 if a run already shipped
  ledger.py add-lead --json <file|->
  ledger.py add-suppression --domain D --company C --reason R
  ledger.py add-run --status success|no_lead|failed [--shortlist N] [--notes T]
  ledger.py pending [--json]                   Supabase writes still owed
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone, timedelta

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER_DIR = os.path.join(REPO, "ledger")
LEADS = os.path.join(LEDGER_DIR, "leads.json")
SUPPRESSIONS = os.path.join(LEDGER_DIR, "suppressions.json")
RUNS = os.path.join(LEDGER_DIR, "runs.json")
PENDING = os.path.join(LEDGER_DIR, "pending_supabase.json")

# America/Anchorage is UTC-8 (AKDT) in summer, UTC-9 (AKST) in winter. The
# routine only needs the date, and it fires mid-morning Alaska time, so a fixed
# -8 offset never lands on the wrong calendar day for our purposes.
ANCHORAGE = timezone(timedelta(hours=-8))


def today(date_str=None):
    if date_str:
        return date_str
    return datetime.now(ANCHORAGE).strftime("%Y-%m-%d")


def normalize(domain):
    """Lowercase, drop scheme, drop leading www., drop path and trailing slash.

    Matches the DOMAIN NORMALIZATION rule in prompts/routine_instructions.md, so
    https://www.Denali-Lodge.com/about becomes denali-lodge.com.
    """
    if not domain:
        return ""
    d = domain.strip().lower()
    d = re.sub(r"^[a-z][a-z0-9+.-]*://", "", d)   # scheme
    d = d.split("/")[0]                            # path
    d = d.split("?")[0].split("#")[0]
    d = d.split("@")[-1]                           # tolerate an email
    d = d.split(":")[0]                            # port
    d = re.sub(r"^www\.", "", d)
    return d.strip(".")


def _load(path, key):
    if not os.path.exists(path):
        return {"version": 1, key: []}
    with open(path) as fh:
        data = json.load(fh)
    data.setdefault(key, [])
    return data


def _save(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    data["updated"] = today()
    with open(path, "w") as fh:
        json.dump(data, fh, indent=2, sort_keys=False)
        fh.write("\n")


def exclude_set():
    """Every normalized domain the routine must never contact."""
    out = {}
    for row in _load(LEADS, "leads")["leads"]:
        n = normalize(row.get("domain"))
        if n:
            out[n] = {"company": row.get("company"), "why": "already in leads",
                      "run_date": row.get("run_date")}
    for row in _load(SUPPRESSIONS, "suppressions")["suppressions"]:
        n = normalize(row.get("domain"))
        if n:
            out[n] = {"company": row.get("company"), "why": "suppressed",
                      "reason": row.get("reason")}
    return out


def cmd_normalize(args):
    print(normalize(args.domain))
    return 0


def cmd_exclude_set(args):
    ex = exclude_set()
    if args.json:
        print(json.dumps(ex, indent=2))
    else:
        for d in sorted(ex):
            print(d)
    return 0


def cmd_check(args):
    ex = exclude_set()
    hit = False
    for raw in args.domains:
        n = normalize(raw)
        if n in ex:
            meta = ex[n]
            print("EXCLUDED  {}  ({}, {})".format(
                n, meta.get("company") or "?", meta.get("why")))
            hit = True
        else:
            print("clear     {}".format(n))
    return 1 if hit else 0


def cmd_ran_today(args):
    day = today(args.date)
    for row in _load(RUNS, "runs")["runs"]:
        if row.get("run_date") == day and row.get("status") == "success":
            print("A successful run already shipped for {}.".format(day))
            return 0
    print("No successful run recorded for {}.".format(day))
    return 1


def cmd_add_lead(args):
    raw = sys.stdin.read() if args.json == "-" else open(args.json).read()
    lead = json.loads(raw)
    n = normalize(lead.get("domain"))
    if not n:
        print("refusing to add a lead with no domain", file=sys.stderr)
        return 2
    lead["domain"] = n
    lead.setdefault("run_date", today())
    data = _load(LEADS, "leads")
    for i, row in enumerate(data["leads"]):
        if normalize(row.get("domain")) == n:
            data["leads"][i] = {**row, **lead}   # idempotent upsert
            _save(LEADS, data)
            print("updated existing lead {}".format(n))
            return 0
    data["leads"].append(lead)
    _save(LEADS, data)
    print("added lead {}".format(n))
    return 0


def cmd_add_suppression(args):
    n = normalize(args.domain)
    data = _load(SUPPRESSIONS, "suppressions")
    for row in data["suppressions"]:
        if normalize(row.get("domain")) == n:
            print("already suppressed {}".format(n))
            return 0
    data["suppressions"].append({"company": args.company, "domain": n,
                                 "reason": args.reason, "date": today()})
    _save(SUPPRESSIONS, data)
    print("suppressed {}".format(n))
    return 0


def cmd_add_run(args):
    data = _load(RUNS, "runs")
    data["runs"].append({"run_date": today(args.date), "status": args.status,
                         "shortlist_count": args.shortlist, "notes": args.notes})
    _save(RUNS, data)
    print("recorded run {} {}".format(today(args.date), args.status))
    return 0


INBOUND = os.path.join(LEDGER_DIR, "inbound_watch.json")


def _inbound():
    if not os.path.exists(INBOUND):
        return {"version": 1,
                "note": "Consecutive runs that could not check INBOUND FIRST. The scanner opt-in queue lives only in Supabase, so an outage makes consented inbound leads invisible and a cold lead ships in their place. This counter makes that cost visible instead of silent.",
                "consecutive_skips": 0, "first_skipped": None, "last_checked": None}
    return json.load(open(INBOUND))


def cmd_inbound_skipped(args):
    """Record that INBOUND FIRST could not run. Escalates as it repeats."""
    d = _inbound()
    d["consecutive_skips"] += 1
    d["first_skipped"] = d["first_skipped"] or today()
    d["last_skipped"] = today()
    d["reason"] = args.reason
    _save(INBOUND, d)
    n = d["consecutive_skips"]
    print("INBOUND FIRST skipped {} run(s) in a row, since {}.".format(n, d["first_skipped"]))
    if n >= 3:
        print("ESCALATE. Consented opt-ins have now been outranked by cold leads {} runs "
              "running. Someone asked for a study and has not been served. Say this "
              "LOUDLY at the top of the delivery summary, not in a footnote.".format(n))
    return 0


def cmd_inbound_ok(args):
    """INBOUND FIRST ran. Clear the counter and report what the outage cost."""
    d = _inbound()
    was, since = d["consecutive_skips"], d.get("first_skipped")
    d.update({"consecutive_skips": 0, "first_skipped": None, "last_checked": today(),
              "reason": None})
    _save(INBOUND, d)
    if was:
        print("INBOUND FIRST is readable again after {} skipped run(s) since {}.".format(was, since))
        print("DRAIN THE BACKLOG. Serve inbound every run until the queue is empty, "
              "before ANY cold scouting resumes. Cold leads shipped during the outage "
              "took their place, and that debt is paid oldest first.")
    else:
        print("INBOUND FIRST checked cleanly.")
    return 0


def cmd_inbound_status(args):
    d = _inbound()
    n = d["consecutive_skips"]
    print(json.dumps(d, indent=2))
    return 1 if n >= 3 else 0


def cmd_pending(args):
    data = _load(PENDING, "pending")
    if args.json:
        print(json.dumps(data, indent=2))
    else:
        rows = data["pending"]
        if not rows:
            print("No Supabase writes owed.")
        for row in rows:
            print("{}  {}  {}".format(row.get("queued_on"), row.get("kind"),
                                      row.get("summary")))
    return 0


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("normalize"); s.add_argument("domain"); s.set_defaults(fn=cmd_normalize)

    s = sub.add_parser("exclude-set")
    s.add_argument("--json", action="store_true"); s.set_defaults(fn=cmd_exclude_set)

    s = sub.add_parser("check"); s.add_argument("domains", nargs="+")
    s.set_defaults(fn=cmd_check)

    s = sub.add_parser("ran-today"); s.add_argument("--date")
    s.set_defaults(fn=cmd_ran_today)

    s = sub.add_parser("add-lead"); s.add_argument("--json", required=True)
    s.set_defaults(fn=cmd_add_lead)

    s = sub.add_parser("add-suppression")
    s.add_argument("--domain", required=True); s.add_argument("--company", default=None)
    s.add_argument("--reason", required=True); s.set_defaults(fn=cmd_add_suppression)

    s = sub.add_parser("add-run")
    s.add_argument("--status", required=True, choices=["success", "no_lead", "failed"])
    s.add_argument("--shortlist", type=int, default=None)
    s.add_argument("--notes", default=None); s.add_argument("--date")
    s.set_defaults(fn=cmd_add_run)

    s = sub.add_parser("pending"); s.add_argument("--json", action="store_true")
    s.set_defaults(fn=cmd_pending)

    s = sub.add_parser("inbound-skipped", help="INBOUND FIRST could not run this run")
    s.add_argument("--reason", default="Supabase unreachable")
    s.set_defaults(fn=cmd_inbound_skipped)

    s = sub.add_parser("inbound-ok", help="INBOUND FIRST ran, clear the counter")
    s.set_defaults(fn=cmd_inbound_ok)

    s = sub.add_parser("inbound-status", help="exit 1 when the skip streak has hit escalation")
    s.set_defaults(fn=cmd_inbound_status)

    args = p.parse_args()
    sys.exit(args.fn(args))


if __name__ == "__main__":
    main()
