#!/usr/bin/env python3
"""Cross-check the engineering room's four outputs BEFORE they become a study.

Written 2026-08-05, backlog item 6. That day the product-manager wrote its PRD
before the staff-engineer's design existed, noticed the problem itself, and said
plainly the two would need reconciling. They happened to agree. Nothing checked.

The four Phase 4 agents run in parallel and none of them can see the others'
constraints. Each is individually excellent and they can still contradict each
other, and the contradiction only surfaces later, when a critic finds it and
charges a round for it, or worse when the prospect finds it.

claim_sweep.py already does this for the FINISHED study and reliably finds real
conflicts. This runs the same idea one stage earlier, where a fix is cheap and no
critic round has been spent yet.

WHAT IT CHECKS

  1. KILLED CAPABILITY PROMISED ANYWAY. feasibility.json carries a kill_list, the
     things the conscience explicitly ruled out. If the PRD, the roadmap or the
     design promises one of them as a deliverable, the room has contradicted its
     own gate. This is the highest-value check here, because the kill list is
     precisely where the pipeline's incentive gradient pushes hardest.

  2. NON-GOAL PROMISED AS A GOAL. The PRD's non_goals exist to be honest about
     scope. A roadmap item that delivers a stated non-goal is the same defect one
     document later.

  3. THE PICK DRIFTED. The locked build has a name. If the design, the PRD, the
     ROI and the roadmap are not all costing and planning the SAME build, the
     study is assembling four different proposals.

  4. NUMBERS THAT DISAGREE. The fee, the timeline and the headline figures appear
     in more than one output. Where two outputs print different values for the
     same thing, a reader with a calculator finds it.

  5. AI ROLE DRIFT. If the locked pick has ai_role none and any output describes a
     model doing work in phase one, the room has quietly re-added the thing the
     feasibility gate removed. That happened in miniature on 2026-08-05, where a
     phase two that might never be funded was becoming the headline.

Usage:
  python scripts/room_reconcile.py --dir out/<date>
"""
import argparse
import json
import os
import re
import sys

MONEY = re.compile(r"\$?\b(\d{1,3}(?:,\d{3})+|\d{4,6})\b(?:\s*(?:dollars|usd))?", re.I)
# Phrases that mean a model is doing work, as opposed to describing one.
AI_DOING = re.compile(
    r"\b(?:the model|an? (?:llm|model)|generative|generates? (?:the )?(?:answer|prose|response)"
    r"|semantic (?:search|match)|embedding|retrieval[- ]augmented)\b", re.I)
# Hedges that mean the output is DISCUSSING a model rather than shipping one.
AI_HEDGE = [
    "no ai", "no model", "not priced", "conditional", "phase two", "phase 2",
    "would have to be earned", "we would not", "never", "killed", "declined",
    "only if", "not in phase one", "not phase one", "deliberately not",
]


def strings(obj, path=""):
    if isinstance(obj, str):
        yield path, obj
    elif isinstance(obj, dict):
        for k, v in obj.items():
            yield from strings(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from strings(v, f"{path}[{i}]")


def norm(s):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]+", " ", (s or "").lower())).strip()


# Words that are everywhere in THIS domain and therefore distinguish nothing.
# Without this, "Arrival Desk as a build now" matched "Book Builder and the Desk
# Book site", because both carry desk and build. A match has to rest on a term
# that actually names the capability.
DOMAIN_GENERIC = {
    "desk", "desks", "build", "building", "builds", "built", "card", "cards",
    "season", "seasonal", "property", "properties", "page", "pages", "answer",
    "answers", "front", "guest", "guests", "hotel", "hotels", "room", "rooms",
    "book", "site", "phase", "study", "work", "week", "weeks", "team", "staff",
    "system", "systems", "scoped", "now", "later", "next", "them", "their",
}


def keyterms(s, n=4):
    """The distinctive words of a phrase, for loose matching."""
    stop = {"the", "a", "an", "of", "for", "and", "or", "to", "in", "on", "with",
            "any", "no", "not", "at", "it", "is", "we", "that", "this", "would"}
    words = [w for w in norm(s).split() if w not in stop and len(w) > 3]
    return words[:n]


def distinctive(words):
    return [w for w in words if w not in DOMAIN_GENERIC]


def mentions(haystack, phrase, need=3):
    """True when enough of a phrase's distinctive words co-occur.

    A proportion, not a fixed count. Kill-list entries carry OUR words as well as
    the capability's, so "Any voice agent, permanently" yields three key terms of
    which only two name the thing. Demanding all three missed a roadmap line that
    promised the voice agent outright, which is the single most important thing
    this check exists to catch.
    """
    import math
    kt = keyterms(phrase)
    if len(kt) == 1:
        # Single-term kills like "Dictation in v1" never matched at all under a
        # two-word minimum. Match the stem so dictation also catches dictate.
        w = kt[0]
        return w not in DOMAIN_GENERIC and len(w) >= 6 and w[:6] in haystack
    if not kt:
        return False
    hit = sum(1 for w in kt if w in haystack)
    threshold = max(2, math.ceil(len(kt) * 0.6))
    if hit < min(threshold, len(kt)):
        return False
    # At least one MATCHED word must actually name the capability rather than
    # being domain wallpaper, or every string with "desk" and "build" in it
    # trips every kill-list entry that mentions a desk or a build.
    dis = distinctive(kt)
    if dis and not any(w in haystack for w in dis):
        return False
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True, help="out/<date>")
    ap.add_argument("--strict", action="store_true")
    a = ap.parse_args()

    def load(name):
        p = os.path.join(a.dir, name)
        return json.load(open(p)) if os.path.exists(p) else None

    eng = load("engineering.json")
    feas = load("feasibility.json")
    if not eng:
        print("no engineering.json in {}, nothing to reconcile".format(a.dir))
        return 0

    fails, warns, notes = [], [], []

    design = eng.get("design") or {}
    prd = eng.get("prd") or {}
    roadmap = eng.get("roadmap") or {}

    def blob(section):
        return norm(" ".join(t for _, t in strings(section)))

    all_text = blob(eng)
    roadmap_text = blob(roadmap)
    prd_text = blob(prd)

    # 1. Killed capability promised anyway.
    # The kill list phrases things as "Building X ourselves" or "X as a scoped
    # build". A roadmap refuses those in its OWN words, and the first version of
    # this list was too narrow to recognise them: "BOUGHT from an established
    # vendor" is the refusal of "building it ourselves", and "gated on one
    # measurement" is the refusal of "as a scoped build". Both read as promises
    # until the vocabulary covers how a refusal actually gets written.
    REFUSAL = ("killed", "we would not", "we will not", "not priced", "non-goal",
               "non goal", "permanent", "declined", "do not build", "never",
               "explicitly not", "rather than", "only if", "not a build",
               "measure first", "conditional", "buy", "bought", "buying",
               "gated", "gate on", "measurement", "only they can", "vendor",
               "before anything", "held in", "not scoped")

    def scan_for_killed(label, section):
        for path, text in strings(section):
            low = norm(text)
            for k in ((feas or {}).get("kill_list") or []):
                subject = k.split(".")[0]
                if not mentions(low, subject, need=3):
                    continue
                # The hedge must sit in THIS string, not merely somewhere in the
                # section. One correct refusal elsewhere must not immunise a
                # promise here, which is exactly the bug this check shipped with.
                if any(h in low for h in REFUSAL):
                    notes.append(f"{label} references the killed item and refuses it "
                                 f"in place: {subject[:64]}")
                else:
                    fails.append(f"{label.upper()} PROMISES A KILLED CAPABILITY\n"
                                 f"        the feasibility gate killed: {subject[:100]}\n"
                                 f"        at {path}\n        {text.strip()[:130]}")

    scan_for_killed("roadmap", roadmap)
    scan_for_killed("PRD", prd)
    scan_for_killed("design", design)

    # 2. A stated non-goal delivered by the roadmap.
    for ng in (prd.get("non_goals") or []):
        phrase = ng.get("non_goal") if isinstance(ng, dict) else str(ng)
        if not phrase:
            continue
        for path, text in strings(roadmap):
            low = norm(text)
            if not mentions(low, phrase, need=3):
                continue
            if any(h in low for h in REFUSAL):
                notes.append(f"roadmap references a non-goal and holds it in place: "
                             f"{phrase[:64]}")
            else:
                fails.append(f"ROADMAP DELIVERS A STATED NON-GOAL\n"
                             f"        PRD says this is out of scope: {phrase[:100]}\n"
                             f"        at {path}\n        {text.strip()[:130]}")

    # 3. The pick drifted.
    pick = (feas or {}).get("recommended_pick") or {}
    pick_name = pick.get("name") or ""
    if pick_name:
        kt = keyterms(pick_name, n=3)
        for label, text in (("design", blob(design)), ("PRD", prd_text),
                            ("roadmap", roadmap_text)):
            if kt and not any(w in text for w in kt):
                warns.append(f"the {label} never names the locked pick "
                             f"({pick_name[:60]}), check it is costing the same build")

    # 5. AI role drift, the one the pipeline is most prone to.
    if (pick.get("ai_role") or "").lower() == "none":
        for path, text in strings(eng):
            low = text.lower()
            if AI_DOING.search(low) and not any(h in low for h in AI_HEDGE):
                warns.append("AI ROLE DRIFT, the locked pick has ai_role none and "
                             f"this reads as a model doing work in phase one\n"
                             f"        {path}\n        {text.strip()[:140]}")

    # 4. Numbers that disagree across outputs.
    seen = {}
    for path, text in strings(eng):
        for m in MONEY.finditer(text):
            v = int(m.group(1).replace(",", ""))
            if v < 1000:
                continue
            seen.setdefault(v, set()).add(path.split(".")[1] if "." in path else path)
    fee_like = sorted(v for v in seen if 5000 <= v <= 500000)
    if len(fee_like) > 6:
        warns.append("many distinct money figures across the room's outputs "
                     f"({len(fee_like)}), worth one read for a fee that drifted: "
                     f"{fee_like[:8]}")

    print("\n  ROOM RECONCILE  —  {}\n".format(a.dir))
    for n in notes:
        print("  ok    " + n)
    for w in warns:
        print("  WARN  " + w)
    for f in fails:
        print("  FAIL  " + f)
    if not fails and not warns:
        print("  the four outputs agree with each other and with the locked pick")
    print("\n  {} failure(s), {} warning(s)\n".format(len(fails), len(warns)))
    return 1 if (fails or (a.strict and warns)) else 0


if __name__ == "__main__":
    sys.exit(main())
