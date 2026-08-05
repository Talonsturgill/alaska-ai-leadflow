#!/usr/bin/env python3
"""Git-backed memory of record for the lead-flow routine.

THIS IS THE DATABASE. Supabase was retired on 2026-08-05. The ledger files under
ledger/ are committed to this private repo every run, so the routine can always
answer the questions that gate a run: have we contacted this company, did a run
already ship today, and who is still owed a study they asked for.

Structured fields live here. Large documents live as files under runs/<date>/<slug>/
and are referenced by study_path, because git stores documents better than a jsonb
column does, and re-emitting 25KB of JSON inside a tool call is how the old store
silently lost three consecutive writes.

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
  ledger.py inbound-next [--json]              oldest unserved consented opt-in
  ledger.py stats [--json]                     the analytics the database answered
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
PENDING = os.path.join(LEDGER_DIR, "retired_pending_supabase.json")  # history only

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


# ------------------------------------------------------------------- outcomes
# Added 2026-08-05. Seventeen leads, sixteen drafts, one confirmed send and not
# one recorded reply. Every quality gate in this routine is tuned against a
# target nobody has measured, which makes the whole anti-hype thesis an article
# of faith. It might be exactly right. It might be why nobody answers. This is
# the cheapest possible way to find out, and until it has data every other
# improvement to this machine is a guess wearing a lab coat.
OUTCOMES = ("no_reply", "replied", "meeting", "won", "lost", "bounced", "unsubscribed")


def cmd_record_outcome(args):
    n = normalize(args.domain)
    if args.outcome not in OUTCOMES:
        print("outcome must be one of {}".format(", ".join(OUTCOMES)), file=sys.stderr)
        return 2
    data = _load(LEADS, "leads")
    for row in data["leads"]:
        if normalize(row.get("domain")) == n:
            row["result"] = args.outcome
            row["result_on"] = today(args.date)
            if args.note:
                row["result_note"] = args.note
            _save(LEADS, data)
            print("recorded {} for {}".format(args.outcome, n))
            return 0
    print("no lead for {}".format(n), file=sys.stderr)
    return 1


def cmd_scoreboard(args):
    """What actually happened, cut the ways that would change how we work.

    Every cut here answers a question the routine currently decides by taste.
    """
    leads = _load(LEADS, "leads")["leads"]
    sent = [l for l in leads if l.get("gmail_draft_id") or l.get("status") in ("drafted", "sent")]
    known = [l for l in sent if l.get("result")]
    good = {"replied", "meeting", "won"}

    def rate(rows):
        k = [r for r in rows if r.get("result")]
        if not k:
            return None, 0
        return round(100.0 * len([r for r in k if r["result"] in good]) / len(k)), len(k)

    def cut(label, keyfn):
        buckets = {}
        for l in sent:
            buckets.setdefault(keyfn(l), []).append(l)
        out = []
        for k, rows in sorted(buckets.items()):
            r, n = rate(rows)
            out.append((k, r, n, len(rows)))
        return label, out

    cuts = [
        cut("by segment", lambda l: (l.get("segment") or "unknown").split(",")[0][:30]),
        # The thesis this shop is betting on. If restraint does not out-reply a
        # normal pitch, we are paying for honesty in replies and should know it.
        cut("recommended against a build",
            lambda l: "yes" if "no ai" in (l.get("recommended_build") or "").lower()
            or "no ai" in (l.get("outcome") or "").lower()
            or "not recommended" in (l.get("outcome") or "").lower() else "no"),
        cut("contact was a named human",
            lambda l: "yes" if l.get("contact_name") else "general inbox"),
        cut("fit score", lambda l: str(l.get("fit_score") or "?")),
    ]
    overall, n_known = rate(sent)
    if args.json:
        print(json.dumps({"drafted": len(sent), "outcome_known": n_known,
                          "reply_rate_pct": overall,
                          "cuts": {lbl: {str(k): {"rate": r, "known": kn, "total": t}
                                         for k, r, kn, t in rows} for lbl, rows in cuts}},
                         indent=1))
        return 0
    print("\n  SCOREBOARD, what actually happened\n")
    print("  drafted or sent        {}".format(len(sent)))
    print("  outcome recorded       {}".format(n_known))
    if not n_known:
        print("\n  NOTHING IS RECORDED YET, so every number below is blank and every")
        print("  quality decision this routine makes is currently unmeasured.")
        print("  After a send lands, run:")
        print("    ledger.py record-outcome --domain <d> --outcome replied|no_reply|meeting|won")
        print()
        return 0
    print("  reply rate             {}%  (of {} known)".format(overall, n_known))
    for lbl, rows in cuts:
        print("\n  {}".format(lbl))
        for k, r, kn, t in rows:
            shown = "{}%".format(r) if r is not None else "  -"
            print("    {:32} {:>4}   known {}/{}".format(k, shown, kn, t))
    print()
    return 0


# ---------------------------------------------------------------- inbound queue
# Supabase was retired on 2026-08-05. The scanner opt-in queue now arrives as
# GitHub ISSUES on this repo labelled "scan-opt-in", which is a real queue with
# an API, timestamps, state and an audit trail, and it ships with the repo the
# way everything else here does. The showrunner lists and closes those issues
# with the GitHub tools. THIS FILE owns the state, which of them we have served,
# so the answer to "who is still owed a study" is computed rather than eyeballed.
INBOUND_Q = os.path.join(LEDGER_DIR, "inbound.json")


def _inbound_q():
    if not os.path.exists(INBOUND_Q):
        return {"version": 1,
                "note": "The consented Bottleneck Scanner opt-in queue. Intake is a GitHub issue labelled scan-opt-in on this repo. A row lands here when the run picks it up, and served flips when a study ships. INBOUND OUTRANKS OUTBOUND, so anything unserved here is served before any cold scouting.",
                "queue": []}
    return json.load(open(INBOUND_Q))


def cmd_inbound_add(args):
    """Record a consented opt-in pulled off the GitHub issue queue."""
    n = normalize(args.domain)
    if not n:
        print("refusing to queue an opt-in with no domain", file=sys.stderr)
        return 2
    if not args.email or "@" not in args.email:
        print("refusing to queue an opt-in with no consented email", file=sys.stderr)
        return 2
    d = _inbound_q()
    for row in d["queue"]:
        if normalize(row.get("domain")) == n:
            print("already queued {}".format(n))
            return 0
    d["queue"].append({"domain": n, "company": args.company, "email": args.email,
                       "issue": args.issue, "queued_on": today(),
                       "served": False, "served_on": None})
    _save(INBOUND_Q, d)
    print("queued inbound {}".format(n))
    return 0


def cmd_inbound_next(args):
    """Print the OLDEST unserved opt-in that is not suppressed, or nothing.

    Exits 0 when there is one to serve, 1 when the queue is clear. That is the
    signal Phase 0 branches on, so it is computed here rather than judged.
    """
    d = _inbound_q()
    sup = {normalize(r.get("domain")) for r in _load(SUPPRESSIONS, "suppressions")["suppressions"]}
    leads = {normalize(r.get("domain")) for r in _load(LEADS, "leads")["leads"]}
    live = [r for r in d["queue"] if not r.get("served")
            and normalize(r.get("domain")) not in sup
            and normalize(r.get("domain")) not in leads]
    live.sort(key=lambda r: r.get("queued_on") or "")
    if not live:
        print("inbound queue clear, no unserved consented opt-in")
        return 1
    r = live[0]
    if args.json:
        print(json.dumps(r, indent=1))
    else:
        print("SERVE THIS FIRST  {}  {}  (queued {}, issue {})".format(
            r["domain"], r.get("email"), r.get("queued_on"), r.get("issue")))
        if len(live) > 1:
            print("{} more waiting, oldest first".format(len(live) - 1))
    return 0


def cmd_inbound_serve(args):
    """Mark an opt-in served. Close its GitHub issue in the same run."""
    n = normalize(args.domain)
    d = _inbound_q()
    for row in d["queue"]:
        if normalize(row.get("domain")) == n:
            row["served"] = True
            row["served_on"] = today()
            _save(INBOUND_Q, d)
            print("served inbound {} (close issue {})".format(n, row.get("issue")))
            return 0
    print("no queued opt-in for {}".format(n), file=sys.stderr)
    return 1


def cmd_stats(args):
    """The analytics Supabase used to answer, computed from the git ledger."""
    leads = _load(LEADS, "leads")["leads"]
    runs = _load(RUNS, "runs")["runs"]
    sup = _load(SUPPRESSIONS, "suppressions")["suppressions"]
    q = _inbound_q()["queue"]
    by_status, by_segment = {}, {}
    for l in leads:
        by_status[l.get("status") or "unknown"] = by_status.get(l.get("status") or "unknown", 0) + 1
        seg = (l.get("segment") or "unknown").split(",")[0][:34]
        by_segment[seg] = by_segment.get(seg, 0) + 1
    scored = [l["fit_score"] for l in leads if isinstance(l.get("fit_score"), int)]
    out = {
        "leads": len(leads),
        "runs": len(runs),
        "suppressions": len(sup),
        "inbound_queued": len(q),
        "inbound_unserved": len([r for r in q if not r.get("served")]),
        "by_status": by_status,
        "by_segment": by_segment,
        "mean_fit_score": round(sum(scored) / len(scored), 1) if scored else None,
        "with_contact_email": len([l for l in leads if l.get("contact_email")]),
        "with_draft": len([l for l in leads if l.get("gmail_draft_id")]),
        "sent": len([l for l in leads if l.get("status") == "sent"]),
    }
    if args.json:
        print(json.dumps(out, indent=1))
        return 0
    print("\n  LEAD FLOW, from the git ledger\n")
    for k in ("leads", "runs", "suppressions", "inbound_queued", "inbound_unserved",
              "with_contact_email", "with_draft", "sent", "mean_fit_score"):
        print("  {:22} {}".format(k, out[k]))
    print("\n  by status")
    for k, v in sorted(by_status.items(), key=lambda x: -x[1]):
        print("    {:20} {}".format(k, v))
    print("\n  by segment")
    for k, v in sorted(by_segment.items(), key=lambda x: -x[1]):
        print("    {:36} {}".format(k, v))
    print()
    return 0


INBOUND = os.path.join(LEDGER_DIR, "inbound_watch.json")


def _inbound():
    if not os.path.exists(INBOUND):
        return {"version": 1,
                "note": "Consecutive runs that could not check INBOUND FIRST. The opt-in queue is GitHub issues labelled scan-opt-in on this repo. If it cannot be read, consented inbound leads go invisible and a cold lead ships in their place, so this counter makes that cost visible instead of silent.",
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
            print("Nothing owed anywhere. Git is the only store.")
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

    s = sub.add_parser("inbound-add", help="queue a consented opt-in off the GitHub issue queue")
    s.add_argument("--domain", required=True); s.add_argument("--company")
    s.add_argument("--email", required=True); s.add_argument("--issue")
    s.set_defaults(fn=cmd_inbound_add)

    s = sub.add_parser("inbound-next", help="oldest unserved opt-in, exit 1 when the queue is clear")
    s.add_argument("--json", action="store_true"); s.set_defaults(fn=cmd_inbound_next)

    s = sub.add_parser("inbound-serve", help="mark an opt-in served")
    s.add_argument("--domain", required=True); s.set_defaults(fn=cmd_inbound_serve)

    s = sub.add_parser("record-outcome", help="what actually happened after a send")
    s.add_argument("--domain", required=True)
    s.add_argument("--outcome", required=True, help="|".join(OUTCOMES))
    s.add_argument("--note"); s.add_argument("--date")
    s.set_defaults(fn=cmd_record_outcome)

    s = sub.add_parser("scoreboard", help="reply rate, cut the ways that change how we work")
    s.add_argument("--json", action="store_true"); s.set_defaults(fn=cmd_scoreboard)

    s = sub.add_parser("stats", help="the analytics the database used to answer")
    s.add_argument("--json", action="store_true"); s.set_defaults(fn=cmd_stats)

    s = sub.add_parser("inbound-skipped", help="INBOUND FIRST could not run this run")
    s.add_argument("--reason", default="inbound issue queue unreadable")
    s.set_defaults(fn=cmd_inbound_skipped)

    s = sub.add_parser("inbound-ok", help="INBOUND FIRST ran, clear the counter")
    s.set_defaults(fn=cmd_inbound_ok)

    s = sub.add_parser("inbound-status", help="exit 1 when the skip streak has hit escalation")
    s.set_defaults(fn=cmd_inbound_status)

    args = p.parse_args()
    sys.exit(args.fn(args))


if __name__ == "__main__":
    main()
