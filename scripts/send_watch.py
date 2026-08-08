#!/usr/bin/env python3
"""Reconcile the ledger against what actually left the outbox.

WHY THIS EXISTS, and it is the same defect twice.

On 2026-08-08 the run opened Phase 0 step 7, searched Gmail for the previous
run's subject line, and PROVED that the R&M Consultants email had been sent on
2026-08-07. It read the sent body back, diffed it, and recorded a voice delta
from it. Then it threw the fact of the send away, because no step in the
contract writes it down. `ledger.py stats` said `sent 1` while
`voice_diff.py` said nine sends had been compared to date, and the R&M lead
still read `status: drafted`.

The same run found `ledger.py scoreboard` reporting `outcome recorded 0`
against 18 leads drafted or sent. The outcome-tracking upgrade shipped on
2026-08-05 had never received a single data point in three months, so every
cut it computes, reply rate by segment, by named human versus general inbox,
by fit score, by whether we recommended AGAINST a build, was blank. That last
cut is the one that tests the honest-restraint thesis this whole routine is
built on, and it has never had a number in it.

Both are the same shape: the run holds the evidence in its hand and no code
writes it down, so the memory of record quietly disagrees with reality.

WHAT THIS DOES NOT DO. It does not touch Gmail. Only the showrunner has the
connector, so the showrunner does the reading and hands the observations here
as a file. This script does the MATCHING, which is the part that must be
computed rather than eyeballed, the same way dedupe is computed in ledger.py
and ROI arithmetic is computed in roi_math.py.

THE MATCHING RULE, deliberately conservative. A lead flips to `sent` only when
an observed message's recipient domain normalizes to that lead's domain. A
subject that also matches the archived outreach is recorded as corroboration
and a subject that differs is reported LOUDLY rather than silently accepted,
because Talon rewrites subjects by hand and a rewritten subject is still that
lead's send. Absence of an observation NEVER changes a lead. Nothing here can
invent a send.

Usage
  send_watch.py --observed out/<date>/gmail_observed.json          # report only
  send_watch.py --observed out/<date>/gmail_observed.json --apply  # write it
  send_watch.py --self-test                                        # hermetic

The observations file is a list of objects, each carrying at minimum `to`.
Optional: `subject`, `sent_at` (ISO), `thread_id`, `replied` (bool),
`reply_at`. Example:

  [ { "to": "lstory@rmconsult.com",
      "subject": "Checking R&M pay estimates before they go out",
      "sent_at": "2026-08-07T11:40:50Z",
      "replied": false } ]
"""
import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
LEADS = os.path.join(REPO, "ledger", "leads.json")

# Reuse the ledger's own normalizer so this can never disagree with dedupe.
sys.path.insert(0, HERE)
from ledger import normalize  # noqa: E402


def domain_of(address):
    """The registrable host of an email address, normalized like a domain.

    Returns None for anything that is not plausibly an address, because a
    missing recipient must never match a lead by accident.
    """
    if not address or "@" not in address:
        return None
    local, _, host = address.rpartition("@")
    # An empty local part is malformed. Without this the string "@alpha.com"
    # matched a real lead and flipped it to sent, which the self test caught
    # on the first run of this script.
    if not local.strip().strip("<").strip():
        return None
    host = host.strip().strip(">").strip()
    if not host or "." not in host:
        return None
    return normalize(host)


def load_leads(path):
    with open(path) as fh:
        data = json.load(fh)
    return data, data["leads"]


def reconcile(leads, observations):
    """Compute what the ledger should say. Pure function, no writes.

    Returns (updates, unmatched, already_current, subject_mismatches).
    `updates` is a list of dicts naming the lead index and the fields to set.
    """
    # TWO KEYS, and the exact one is tried first.
    #
    # Domain alone is not enough, which the first real run of this script
    # proved: five of twelve observed sends went to an address whose host is
    # NOT the company's primary domain. Fountainhead Hotels is
    # fountainheadhotels.com in the ledger and was written to beckyk@
    # fdialaska.com. Allen Marine Tours is allenmarinetours.com and was
    # written to Sitkainfo@allenmarine.com. Bristol Bay is bbnc.net and was
    # written to a subsidiary at bbch-llc.com. North Country Charters uses a
    # gmail address outright. A contact address living on a different host
    # from the company's website is normal, not an anomaly.
    #
    # So match the recorded contact_email EXACTLY first. That is not a guess,
    # it is the address the ledger already says we wrote to. Domain is the
    # fallback and stays conservative.
    by_address = {}
    by_domain = {}
    for i, row in enumerate(leads):
        addr = (row.get("contact_email") or "").strip().lower()
        if addr and "@" in addr:
            by_address.setdefault(addr, i)
        n = normalize(row.get("domain"))
        if n:
            by_domain.setdefault(n, i)

    updates = {}
    unmatched = []
    already_current = []
    subject_mismatches = []

    for obs in observations:
        recipients = obs.get("to")
        if isinstance(recipients, str):
            recipients = [recipients]
        recipients = recipients or []

        hit = None
        for addr in recipients:
            exact = (addr or "").strip().lower()
            if exact in by_address:
                idx = by_address[exact]
                hit = (normalize(leads[idx].get("domain")) or exact, idx)
                break
        if hit is None:
            for addr in recipients:
                d = domain_of(addr)
                if d is not None and d in by_domain:
                    hit = (d, by_domain[d])
                    break

        if hit is None:
            unmatched.append(obs)
            continue

        dom, idx = hit
        row = leads[idx]

        # Corroborate on subject where we have one to compare against, but
        # never REQUIRE it. Talon rewrites subjects by hand on the way out.
        obs_subject = (obs.get("subject") or "").strip()
        lead_subject = (row.get("subject") or "").strip()
        if obs_subject and lead_subject and obs_subject != lead_subject:
            subject_mismatches.append(
                {"domain": dom, "drafted": lead_subject, "observed": obs_subject})

        fields = {}
        if row.get("status") != "sent":
            fields["status"] = "sent"
        if obs.get("sent_at") and not row.get("sent_at"):
            fields["sent_at"] = obs["sent_at"]

        # A reply is an OUTCOME, and it is only ever written when observed
        # true. `replied: false` means "no reply seen yet", which is not the
        # same as no_reply and must not be recorded as one, because a reply
        # can still arrive tomorrow.
        if obs.get("replied") is True and row.get("result") != "replied":
            fields["result"] = "replied"
            if obs.get("reply_at"):
                fields["result_on"] = obs["reply_at"][:10]

        if not fields:
            already_current.append(dom)
            continue

        prev = updates.get(idx, {"domain": dom, "index": idx, "fields": {}})
        # A lead can appear twice in the outbox, because a draft gets resent.
        # Keep the EARLIEST timestamp rather than whichever the loop saw last,
        # so sent_at means "when this first went out" and does not depend on
        # the order Gmail happened to return the search in.
        if "sent_at" in fields and "sent_at" in prev["fields"]:
            fields["sent_at"] = min(fields["sent_at"], prev["fields"]["sent_at"])
        prev["fields"].update(fields)
        updates[idx] = prev

    return list(updates.values()), unmatched, already_current, subject_mismatches


def apply_updates(data, leads, updates, path):
    for u in updates:
        leads[u["index"]].update(u["fields"])
    with open(path, "w") as fh:
        json.dump(data, fh, indent=1)
        fh.write("\n")


def report(updates, unmatched, already_current, subject_mismatches, applied):
    print()
    print("  SEND WATCH, the ledger against the outbox")
    print()
    if updates:
        verb = "wrote" if applied else "would write"
        print("  {} {} change(s)".format(verb, len(updates)))
        for u in updates:
            bits = ", ".join("{}={}".format(k, v) for k, v in sorted(u["fields"].items()))
            print("    {:<28} {}".format(u["domain"], bits))
    else:
        print("  no changes, the ledger already matches the outbox")
    if already_current:
        print()
        print("  already current            {}".format(len(already_current)))
    if subject_mismatches:
        print()
        print("  SUBJECT REWRITTEN BY HAND on {} send(s). That is voice signal,".format(
            len(subject_mismatches)))
        print("  run voice_diff.py against these rather than ignoring them.")
        for m in subject_mismatches:
            print("    {}".format(m["domain"]))
            print("      drafted  {}".format(m["drafted"]))
            print("      sent     {}".format(m["observed"]))
    if unmatched:
        print()
        print("  UNMATCHED, {} observed message(s) match no lead. NOTHING WAS".format(
            len(unmatched)))
        print("  WRITTEN for these. A send to a domain with no ledger row is")
        print("  either a lead that was never recorded or mail that is not ours.")
        for obs in unmatched:
            print("    to={} subject={!r}".format(obs.get("to"), (obs.get("subject") or "")[:60]))
    print()
    if not applied and updates:
        print("  report only. re-run with --apply to write it.")
        print()


def self_test():
    """Hermetic. Every negative case that would make this dangerous.

    A checker that only proves it catches the thing it was written for is not
    a checker, it is a demo. Each case below is a way this script could
    corrupt the memory of record.
    """
    leads = [
        {"company": "Alpha", "domain": "alpha.com", "status": "drafted",
         "subject": "The alpha subject"},
        {"company": "Beta", "domain": "beta.org", "status": "sent",
         "sent_at": "2026-01-01T00:00:00Z"},
        {"company": "Gamma", "domain": "gamma.net", "status": "drafted",
         "subject": "The gamma subject"},
        {"company": "Delta", "domain": "delta.io", "status": "drafted",
         "result": "replied"},
        # The real shape that broke domain-only matching: the company's
        # website and the contact address are on different hosts.
        {"company": "Epsilon", "domain": "epsilon-hotels.com", "status": "drafted",
         "contact_email": "becky@epsilon-group.com"},
    ]
    fails = []

    def check(name, cond, detail=""):
        print("  {:<4} {}{}".format("ok" if cond else "FAIL", name,
                                    "" if cond else "  <- " + detail))
        if not cond:
            fails.append(name)

    # POSITIVE: the case this was written for.
    up, un, cur, sm = reconcile(leads, [
        {"to": ["someone@alpha.com"], "subject": "The alpha subject",
         "sent_at": "2026-08-07T11:40:50Z"}])
    check("a drafted lead observed in SENT flips to sent",
          len(up) == 1 and up[0]["fields"].get("status") == "sent"
          and up[0]["fields"].get("sent_at") == "2026-08-07T11:40:50Z", repr(up))

    # NEGATIVE: absence must never flip anything. This is the one that would
    # let the script invent a send.
    up, un, cur, sm = reconcile(leads, [])
    check("no observations writes nothing", up == [] and un == [], repr(up))

    # NEGATIVE: a send to a domain with no lead must not be attached to some
    # other lead just because it is the only one left.
    up, un, cur, sm = reconcile(leads, [{"to": ["x@nowhere-at-all.com"]}])
    check("an unmatched recipient matches no lead", up == [] and len(un) == 1, repr(up))

    # NEGATIVE: re-running must be idempotent, not double counted.
    up, un, cur, sm = reconcile(leads, [{"to": ["hi@beta.org"]}])
    check("an already-sent lead is a no-op", up == [] and cur == ["beta.org"], repr(up))

    # NEGATIVE: a rewritten subject is still that lead's send, and it must be
    # REPORTED rather than silently swallowed or used to reject the match.
    up, un, cur, sm = reconcile(leads, [
        {"to": ["hi@gamma.net"], "subject": "Something Talon retyped"}])
    check("a hand-rewritten subject still matches and is reported",
          len(up) == 1 and len(sm) == 1 and sm[0]["observed"] == "Something Talon retyped",
          repr((up, sm)))

    # NEGATIVE: replied:false is NOT no_reply. Recording it would freeze a
    # lead as a miss the day before it answers.
    up, un, cur, sm = reconcile(leads, [{"to": ["hi@alpha.com"], "replied": False}])
    check("replied:false records no outcome",
          len(up) == 1 and "result" not in up[0]["fields"], repr(up))

    # POSITIVE: replied:true does record one.
    up, un, cur, sm = reconcile(leads, [
        {"to": ["hi@alpha.com"], "replied": True, "reply_at": "2026-08-09T10:00:00Z"}])
    check("replied:true records the outcome",
          up[0]["fields"].get("result") == "replied"
          and up[0]["fields"].get("result_on") == "2026-08-09", repr(up))

    # NEGATIVE: an outcome already on the row is not rewritten.
    up, un, cur, sm = reconcile(leads, [{"to": ["hi@delta.io"], "replied": True}])
    check("an existing outcome is not overwritten",
          len(up) == 1 and "result" not in up[0]["fields"], repr(up))

    # NEGATIVE: malformed recipients must not crash or match.
    up, un, cur, sm = reconcile(leads, [
        {"to": ["not-an-address"]}, {"to": []}, {"to": None}, {"to": ["@alpha.com"]},
        {"to": ["a@localhost"]}])
    check("malformed recipients match nothing and do not crash",
          up == [] and len(un) == 5, repr(up))

    # NEGATIVE: www. and case must normalize the same way dedupe does, or this
    # script and the exclude set could disagree about the same company.
    up, un, cur, sm = reconcile(leads, [{"to": ["Person@WWW.Alpha.COM"]}])
    check("recipient host normalizes like the exclude set", len(up) == 1, repr(up))

    # NEGATIVE: one observation must not update two leads.
    up, un, cur, sm = reconcile(leads, [{"to": ["a@alpha.com", "b@gamma.net"]}])
    check("one message updates at most one lead", len(up) == 1, repr(up))

    # POSITIVE: the contact address on a different host still matches its lead.
    up, un, cur, sm = reconcile(leads, [{"to": ["becky@epsilon-group.com"]}])
    check("contact_email on a different host matches its lead",
          len(up) == 1 and leads[up[0]["index"]]["company"] == "Epsilon", repr(up))

    # NEGATIVE: matching the address must not drag in every other lead that
    # happens to share that unrelated host.
    up, un, cur, sm = reconcile(leads, [{"to": ["someone-else@epsilon-group.com"]}])
    check("an unrecorded address at the contact's host matches nothing",
          up == [] and len(un) == 1, repr(up))

    # NEGATIVE: the exact address wins over a domain that would match a
    # DIFFERENT lead, so a match can never be attributed to the wrong company.
    leads_conflict = [
        {"company": "One", "domain": "shared.com", "status": "drafted"},
        {"company": "Two", "domain": "two.com", "status": "drafted",
         "contact_email": "person@shared.com"},
    ]
    up, un, cur, sm = reconcile(leads_conflict, [{"to": ["person@shared.com"]}])
    check("the exact address beats a competing domain match",
          len(up) == 1 and leads_conflict[up[0]["index"]]["company"] == "Two", repr(up))

    print()
    if fails:
        print("  {} FAILED: {}".format(len(fails), ", ".join(fails)))
        return 1
    print("  all 14 checks passed")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--observed", help="JSON list of messages read out of Gmail SENT")
    ap.add_argument("--leads", default=LEADS)
    ap.add_argument("--apply", action="store_true", help="write the changes")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        print()
        print("  SEND WATCH SELF TEST")
        print()
        return self_test()

    if not args.observed:
        ap.error("--observed is required unless --self-test")

    with open(args.observed) as fh:
        observations = json.load(fh)
    if isinstance(observations, dict):
        observations = observations.get("messages", [])

    data, leads = load_leads(args.leads)
    updates, unmatched, already_current, subject_mismatches = reconcile(leads, observations)

    if args.apply and updates:
        apply_updates(data, leads, updates, args.leads)

    report(updates, unmatched, already_current, subject_mismatches, args.apply)
    return 0


if __name__ == "__main__":
    sys.exit(main())
