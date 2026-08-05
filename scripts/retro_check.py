#!/usr/bin/env python3
"""Verify the Phase 10 retro actually SHIPPED something, rather than describing it.

Written 2026-08-05, at the maintainer's instruction: "when I said retro mandatory
I meant it should actually make fixes, not just list them."

That distinction is the whole reason this file exists. Phase 10 already said
IMPLEMENT and VERIFY, and it still had a way out, because writing a careful
backlog entry feels like doing the work and reads like it too. The completion
gate accepted an entry in ledger/upgrades.json as proof, and an entry is prose.
Prose is exactly what a language model produces when it has not done anything.

So this checks the one thing prose cannot fake: whether the files an upgrade
CLAIMS to have changed were actually changed by this run's commits. An upgrade
that names scripts/foo.py and did not touch scripts/foo.py is a description, and
this exits 1 on it.

WHAT IT CHECKS

  1. AT LEAST ONE UPGRADE DATED TODAY. The floor from Phase 10 step 3. Three is
     the ceiling so a run does not wander off rebuilding the machine, one is the
     floor so it cannot do nothing and call that judgement.

  2. EVERY NAMED FILE EXISTS AND WAS TOUCHED TODAY. The load-bearing check. Read
     from git log rather than from the working tree, because an uncommitted edit
     does not survive the run and THE MERGE LAW means a run that did not merge
     did not ship.

  3. EVIDENCE AND VERIFICATION ARE REAL. An upgrade with no evidence line is a
     preference, not an upgrade. Short, generic verification text is the tell for
     a change nobody actually ran.

  4. A NEGATIVE CASE WAS TESTED. A warning rather than a failure, because it is
     judged from wording and this file refuses to fail a run on a keyword match.
     A gate that passes everything is worse than no gate, and every gate written
     on 2026-08-05 had false positives on its first attempt, so this one assumes
     it is wrong before it assumes the run is.

Usage:
  python scripts/retro_check.py                  # today, against ledger/upgrades.json
  python scripts/retro_check.py --date 2026-08-05
  python scripts/retro_check.py --upgrades <path> --repo <dir>
"""
import argparse
import datetime
import json
import os
import subprocess
import sys

# The SAME clock the ledger stamps its dates with. This defaulted to the system
# date, which is UTC on the runner, while every date this gate compares against
# is written by ledger.py's fixed Anchorage offset. The two agree for most of
# the day and disagree between 00:00 and 08:00 UTC, where a run would hard-fail
# "NO UPGRADE DATED ..." against a retro that really had shipped. A gate that
# fails a correct run on a clock difference gets switched off, and then it is
# not a gate.
ANCHORAGE = datetime.timezone(datetime.timedelta(hours=-8))


def run_date():
    return datetime.datetime.now(ANCHORAGE).strftime("%Y-%m-%d")

# Wording that indicates someone tested the case where the check SHOULD fire.
# Deliberately broad. This drives a warning, never a failure.
NEGATIVE_SIGNALS = (
    "negative case", "negative test", "false positive", "false negative",
    "injected", "reconstruct", "caught all", "confirmed it caught",
    "fails when", "failed when", "exits 1", "does fire", "did fire",
    "regression", "before and after", "without the fix",
)


def git(repo, *args):
    out = subprocess.run(["git", "-C", repo, *args],
                         capture_output=True, text=True)
    if out.returncode != 0:
        return None
    return out.stdout


def files_touched_on(repo, date):
    """Every path touched by a commit authored on `date`.

    git log rather than git status, on purpose. An edit sitting uncommitted in
    the working tree is not a shipped change, and this gate exists precisely to
    tell the difference between doing something and appearing to.
    """
    # Explicit 00:00:00 on both ends, and it matters. git's approxidate parser
    # attaches the CURRENT time of day to a bare date, so `--since 2026-08-05`
    # run at 12:11 means "since 12:11 today" and silently hides every commit
    # made this morning. The first version of this gate did exactly that and
    # reported nine described-but-not-made failures against nine changes that
    # had all really shipped.
    # The window carries the Anchorage offset explicitly. Bare timestamps are
    # read in the runner's local zone, which is UTC, so an Anchorage run date
    # and a UTC window are eight hours out of step: commits made between 00:00
    # and 08:00 UTC belong to the PREVIOUS Anchorage day and fell outside the
    # window entirely. Same class of bug as the approxidate one below, one layer
    # further out.
    nxt = (datetime.date.fromisoformat(date) + datetime.timedelta(days=1)).isoformat()
    out = git(repo, "log", "--since", date + "T00:00:00-08:00",
              "--until", nxt + "T00:00:00-08:00",
              "--name-only", "--pretty=format:")
    if out is None:
        return None
    return {ln.strip() for ln in out.splitlines() if ln.strip()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=None,
                    help="run date, default the Anchorage date ledger.py stamps")
    ap.add_argument("--repo", default=".")
    ap.add_argument("--upgrades", default=None)
    a = ap.parse_args()
    a.date = a.date or run_date()

    path = a.upgrades or os.path.join(a.repo, "ledger", "upgrades.json")
    fails, warns, oks = [], [], []

    if not os.path.exists(path):
        print("\n  RETRO CHECK  —  {}\n".format(a.date))
        print("  FAIL  no {}, so the retro left no trace at all".format(path))
        print("\n  1 failure(s), 0 warning(s)\n")
        return 1

    data = json.load(open(path))
    entries = [u for u in data.get("upgrades", []) if u.get("date") == a.date]

    # 1. The floor.
    if not entries:
        fails.append(
            "NO UPGRADE DATED {}\n"
            "        Phase 10 has a floor of one shipped change per run, and it is\n"
            "        not satisfied by a backlog entry. Every run spends a round it\n"
            "        should not have or works around something. Fix the smallest\n"
            "        real one.".format(a.date))
    elif len(entries) > 3:
        warns.append("{} upgrades dated {}, the ceiling is three, check the run did "
                     "not wander off rebuilding the machine".format(len(entries), a.date))

    touched = files_touched_on(a.repo, a.date)
    if touched is None:
        fails.append("git log failed in {}, cannot tell a shipped change from a "
                     "described one, which is the only thing this gate does"
                     .format(a.repo))
        touched = set()

    for i, u in enumerate(entries):
        tag = (u.get("change") or "untitled")[:58]

        named = u.get("files") or []
        if not named:
            fails.append("UPGRADE NAMES NO FILES\n        {}\n"
                         "        An upgrade that changed no file changed nothing."
                         .format(tag))
        for f in named:
            on_disk = os.path.exists(os.path.join(a.repo, f))
            in_commits = f in touched
            if not on_disk:
                fails.append("UPGRADE NAMES A FILE THAT DOES NOT EXIST\n"
                             "        {}\n        missing: {}".format(tag, f))
            elif not in_commits:
                fails.append(
                    "UPGRADE NAMES A FILE NO COMMIT TOUCHED TODAY\n"
                    "        {}\n        claims: {}\n"
                    "        This is the described-but-not-made failure. Either the\n"
                    "        change was never made, or it is uncommitted and will not\n"
                    "        survive the run.".format(tag, f))
            else:
                oks.append("{} really changed {}".format(tag[:40], f))

        ev = (u.get("evidence") or "").strip()
        vh = (u.get("verified_how") or "").strip()
        if len(ev) < 40:
            fails.append("UPGRADE HAS NO REAL EVIDENCE\n        {}\n"
                         "        An upgrade with no evidence line is a preference."
                         .format(tag))
        if len(vh) < 40:
            fails.append("UPGRADE HAS NO REAL VERIFICATION\n        {}\n"
                         "        A change that is not tested does not ship.".format(tag))
        elif (any(f.endswith(".py") for f in named)
              and not any(s in vh.lower() for s in NEGATIVE_SIGNALS)):
            # Only asked of upgrades that touch executable code. A change to the
            # run contract or a knowledge file has no negative case to test, and
            # demanding one there trains the reader to ignore this warning, which
            # is worse than not printing it.
            warns.append("no negative case evident in the verification of: {}\n"
                         "        A gate that passes everything looks like coverage.\n"
                         "        Say how you confirmed it FIRES when it should."
                         .format(tag))

    print("\n  RETRO CHECK  —  {}\n".format(a.date))
    for o in oks:
        print("  ok    " + o)
    for w in warns:
        print("  WARN  " + w)
    for f in fails:
        print("  FAIL  " + f)
    if not fails and not warns:
        print("  the retro shipped {} verified change(s) and the files it names "
              "were really touched".format(len(entries)))
    print("\n  {} failure(s), {} warning(s)\n".format(len(fails), len(warns)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
