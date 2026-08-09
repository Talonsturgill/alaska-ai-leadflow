#!/usr/bin/env python3
"""Assemble engineering.json from what the room's four agents WROTE.

Written 2026-08-09, closing the backlog item first raised on 2026-08-08 on its
second appearance, per the retro rule that a twice-seen defect is the work.

THE DEFECT. The run contract says the four Phase 4 outputs go into
engineering.json VERBATIM, and room_reconcile.py fails the run when they do not,
because on 2026-08-05 a showrunner summary dropped six of nine keys from a design
and eight of nine from an ROI, and the keys it dropped were the caveats. Yet
staff-engineer, product-manager, roi-analyst and delivery-lead all carried
`tools: Read`. The four agents whose output MUST be persisted verbatim were the
only ones that could not persist it, so the showrunner retyped roughly 40KB of
JSON by hand every run. That transcription IS the mechanism the 2026-08-05 defect
came through. room_reconcile catches the failure after the fact, which is better
than nothing. Removing the step that produces it is cheaper.

THE FIX, in two halves. The four agents now carry Write and a PERSIST section
telling them to write their JSON to a briefed path AND return the same object.
This script collects those files.

WHY BOTH HALVES. The agents still return their JSON, so a write that did not land
is recoverable. This script's job is to make a missing or summarised file LOUD
rather than silent, because the whole point of the change is that nothing gets
quietly reshaped between the agent and the file.

WHAT IT CHECKS, per section:
  * the file exists and is valid JSON (a fence-wrapped file is unwrapped first,
    since an agent writing raw JSON sometimes wraps it anyway)
  * it is an object, not a list or a bare string
  * it keeps the keys the agent's own `# OUTPUT` block contracts, read through
    room_reconcile.contracted_keys so the agent spec stays the single schema and
    no second copy can drift

A section that fails any of those is NOT written. The script names it and exits
non-zero so the showrunner falls back to transcribing that one agent's returned
JSON by hand, which is exactly today's behaviour for that section and no worse.

Usage:
  python scripts/room_collect.py --dir out/<date>
  python scripts/room_collect.py --dir out/<date> --only roi
"""
import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from room_reconcile import SECTION_AGENT, contracted_keys  # noqa: E402

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FENCE = re.compile(r"^\s*```(?:json)?\s*(.*?)\s*```\s*$", re.S)


def read_section(path):
    """Load one agent-written file. Returns (obj, error_string)."""
    if not os.path.exists(path):
        return None, "no file at " + path
    raw = open(path).read().strip()
    if not raw:
        return None, "the file is empty"
    m = FENCE.match(raw)
    if m:
        raw = m.group(1)
    try:
        obj = json.loads(raw)
    except json.JSONDecodeError as e:
        return None, "not valid JSON ({})".format(e)
    if not isinstance(obj, dict):
        return None, "is a {}, not a JSON object".format(type(obj).__name__)
    return obj, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True, help="out/<date>")
    ap.add_argument("--room", default=None,
                    help="where the agents wrote, default <dir>/room")
    ap.add_argument("--only", action="append", default=None,
                    help="collect only these sections, repeatable")
    ap.add_argument("--repo", default=REPO_ROOT)
    a = ap.parse_args()

    room = a.room or os.path.join(a.dir, "room")
    want = a.only or list(SECTION_AGENT)
    unknown = [s for s in want if s not in SECTION_AGENT]
    if unknown:
        print("  unknown section(s): {}. known: {}".format(
            ", ".join(unknown), ", ".join(SECTION_AGENT)))
        return 2

    eng_path = os.path.join(a.dir, "engineering.json")
    eng = {}
    if os.path.exists(eng_path):
        try:
            eng = json.load(open(eng_path))
        except json.JSONDecodeError:
            eng = {}
    if not isinstance(eng, dict):
        eng = {}

    print("\n  ROOM COLLECT  —  {}\n".format(room))
    ok, bad = [], []

    for sec in want:
        agent = SECTION_AGENT[sec]
        path = os.path.join(room, sec + ".json")
        obj, err = read_section(path)
        if err:
            bad.append((sec, agent, err))
            continue

        contracted = contracted_keys(agent, a.repo)
        if not contracted:
            bad.append((sec, agent,
                        "cannot read {}'s # OUTPUT block, so the shape could not "
                        "be checked and this section was not collected".format(agent)))
            continue

        missing = [k for k in contracted if k not in obj]
        kept = len(contracted) - len(missing)
        if kept * 2 < len(contracted):
            bad.append((sec, agent,
                        "kept only {} of {} contracted keys, so it is a summary "
                        "rather than the agent's output. dropped: {}".format(
                            kept, len(contracted), ", ".join(missing))))
            continue

        eng[sec] = obj
        ok.append((sec, agent, kept, len(contracted), missing))

    for sec, agent, kept, total, missing in ok:
        note = "" if not missing else "  (missing {}, check they were not dropped)".format(
            ", ".join(missing))
        print("  ok    {:<8} {:<16} {}/{} contracted keys{}".format(
            sec, agent, kept, total, note))
    for sec, agent, err in bad:
        print("  FAIL  {:<8} {:<16} {}".format(sec, agent, err))

    if ok:
        os.makedirs(a.dir, exist_ok=True)
        with open(eng_path, "w") as f:
            json.dump(eng, f, indent=1, ensure_ascii=False)
            f.write("\n")
        print("\n  wrote {} section(s) verbatim into {}".format(len(ok), eng_path))

    if bad:
        print("\n  {} section(s) were NOT collected. For each one, take that "
              "agent's\n  returned JSON and write it to the path above, then "
              "re-run this. Do NOT\n  summarise it on the way in, which is the "
              "defect this script exists to remove.\n".format(len(bad)))
        return 1

    print("  every section came from the agent that contracts it, verbatim\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
