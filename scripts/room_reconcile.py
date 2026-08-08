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

  6. THE SHOWRUNNER FILED A SUMMARY INSTEAD OF THE ROOM'S OUTPUT. Each section of
     engineering.json is checked against the `# OUTPUT` block of the agent that
     contracts it, so the agent spec is the schema and no second copy can drift.
     This is why check 2 above had never examined anything: the PRD in
     engineering.json kept ZERO of the product-manager's ten contracted keys.
     The fields a summary drops are the caveats, non_goals, open_questions,
     assumptions, conservative_clears, base_rate_note, and a dropped key is read
     by nobody, where dropped prose would at least face a critic.

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


# Which agent contracts each engineering.json section. The agent spec IS the
# schema, so this stays in sync by construction rather than by anyone
# remembering to update a second copy.
SECTION_AGENT = {
    "prd": "product-manager",
    "design": "staff-engineer",
    "roadmap": "delivery-lead",
    "roi": "roi-analyst",
}

# Fields whose absence silently DISABLES a check rather than merely losing
# detail. Missing one of these is always a failure, never a warning, because a
# check with no input passes and looks like coverage.
LOAD_BEARING = {"non_goals"}


def contracted_keys(agent, repo_root):
    """The top-level keys an agent's `# OUTPUT` block promises to return."""
    path = os.path.join(repo_root, ".claude", "agents", agent + ".md")
    if not os.path.exists(path):
        return None
    src = open(path).read()
    i = src.find("# OUTPUT")
    if i < 0:
        return None
    j = src.find("{", i)
    if j < 0:
        return None
    depth, blob = 0, None
    for k in range(j, len(src)):
        if src[k] == "{":
            depth += 1
        elif src[k] == "}":
            depth -= 1
            if depth == 0:
                blob = src[j:k + 1]
                break
    if blob is None:
        return None
    keys, depth = [], 0
    for tok in re.finditer(r'[{}]|"([\w_]+)"\s*:', blob):
        t = tok.group(0)
        if t == "{":
            depth += 1
        elif t == "}":
            depth -= 1
        elif depth == 1:
            keys.append(tok.group(1))
    return keys


def check_shapes(eng, repo_root, fails, warns, notes):
    """Did the showrunner persist what the agents returned, or its own summary?

    Check 6, added 2026-08-05 after the non-goal check was found to have never
    examined anything. The cause was not the check. engineering.json held a
    showrunner rewrite: four ad-hoc keys over the product-manager's ten, six of
    nine dropped from the design, eight of nine from the ROI.

    Two failures in one. Every downstream check reading a contracted key found
    nothing and passed in silence. And the fields a summary drops are the
    caveats, non_goals, open_questions, assumptions, conservative_clears,
    base_rate_note, build_vs_buy, spike_to_retire_it. That is the drift pattern
    operating at the filing cabinet instead of in the prose, and it is worse
    there, because prose gets read by a critic and a dropped key gets read by
    nobody.
    """
    for sec, agent in SECTION_AGENT.items():
        want = contracted_keys(agent, repo_root)
        if not want:
            warns.append(f"cannot read the contracted output shape for {agent}, "
                         f"so the {sec} section was not shape-checked")
            continue
        got = set((eng.get(sec) or {}).keys())
        if not got:
            fails.append(f"engineering.json has no {sec} section at all, and "
                         f"{agent} is contracted to produce one")
            continue
        missing = [k for k in want if k not in got]
        kept = len(want) - len(missing)

        if kept * 2 < len(want):
            fails.append(
                f"THE {sec.upper()} IS A REWRITE, NOT {agent.upper()}'S OUTPUT\n"
                f"        it kept {kept} of {len(want)} contracted keys\n"
                f"        dropped: {', '.join(missing)}\n"
                f"        persisted instead: {', '.join(sorted(got - set(want))) or '(nothing extra)'}\n"
                "        Persist the agent's JSON VERBATIM. A summary drops the\n"
                "        caveats and silently disables every check downstream.")
            continue

        lost = [k for k in missing if k in LOAD_BEARING]
        if lost:
            fails.append(
                f"the {sec} is missing {', '.join(lost)}, which is not a detail. "
                f"A check that reads it has no input, so it passes and looks "
                f"like coverage. {agent} is contracted to produce it.")
        rest = [k for k in missing if k not in LOAD_BEARING]
        if rest:
            warns.append(f"the {sec} is missing contracted key(s) {', '.join(rest)} "
                         f"from {agent}, check they were not summarised away")
        if not missing:
            notes.append(f"the {sec} carries all {len(want)} keys {agent} contracts")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True, help="out/<date>")
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), help="repo root, for .claude/agents")
    ap.add_argument("--strict", action="store_true")
    a = ap.parse_args()

    def load(name):
        p = os.path.join(a.dir, name)
        return json.load(open(p)) if os.path.exists(p) else None

    eng = load("engineering.json")
    feas = load("feasibility.json")

    # ABSENCE OF INPUT IS A FAILURE, NEVER A PASS. Both files used to be
    # optional in practice: a missing engineering.json printed "nothing to
    # reconcile" and exited 0, and a missing feasibility.json left checks 1, 3
    # and 5 as silent no-ops while the script printed the all-clear. Four of the
    # five checks here read feasibility.json, so without it this script is an
    # expensive way to print a reassuring line.
    missing = []
    if not eng:
        missing.append("engineering.json (the room's four outputs)")
    if not feas:
        missing.append("feasibility.json (the kill list and the locked pick, "
                       "which four of the five checks reconcile against)")
    if missing:
        print("\n  ROOM RECONCILE  —  {}\n".format(a.dir))
        for m in missing:
            print("  FAIL  MISSING INPUT, nothing was reconciled: " + m)
        print("\n  This gate cannot pass on absent input. Produce the file or "
              "say in the\n  run log why this run has no room to reconcile.\n")
        return 1

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
    # STRONG MARKERS ONLY. The first list carried bare nouns, "vendor", "buy",
    # "measurement", "gated", and those refuse nothing on their own: a roadmap
    # line promising a killed capability that happened to mention a vendor was
    # excused as "refuses it in place". A refusal is a NEGATION or a DEFERRAL,
    # it is a grammatical act, not a topic. Every entry below either negates or
    # postpones, so it cannot be satisfied by a line that merely discusses the
    # same subject matter.
    REFUSAL = (
        # explicit negation
        "not ", "never", "no ", "without", "declined", "killed", "ruled out",
        "rules out", "out of scope", "non-goal", "non goal", "excluded",
        "we would not", "we will not", "do not build", "deliberately",
        "explicitly not", "refuse", "drop", "dropped", "removed",
        # contrast, which is how a buy-instead-of-build refusal gets written
        "rather than", "instead of", "as opposed to",
        # deferral, which is how a conditional refusal gets written
        "only if", "only when", "conditional", "gated on", "gate on",
        "until we", "before we", "would have to be earned", "measure first",
        "not priced", "not in phase one", "not phase one", "later lane",
    )

    # A BUILD-IT-OURSELVES kill is refused by BUYING, and no amount of adding
    # nouns to a global list expresses that. "Housekeeping route optimisation,
    # BOUGHT from an established vendor" carries no negation and no contrast
    # word, and it is a complete refusal of "Building housekeeping route
    # optimisation ourselves". So the refusal vocabulary is derived from what
    # was killed rather than pooled across every kill: buy-language only counts
    # as a refusal when the thing killed was building it in-house.
    BUY_REFUSAL = ("buy", "bought", "buying", "purchase", "purchased", "licence",
                   "license", "licensed", "off the shelf", "off-the-shelf",
                   "subscription", "vendor", "third party", "third-party",
                   "existing tool", "commercial")

    def refusal_markers(subject):
        low = norm(subject)
        if re.search(r"\b(ourselves|in house|inhouse|from scratch|our own)\b", low):
            return REFUSAL + BUY_REFUSAL
        return REFUSAL

    def kill_subjects():
        """The killed capabilities, whatever shape the conscience returned them in.

        On 2026-08-08 this crashed the whole script with an AttributeError,
        because the ai-feasibility-engineer returned kill_list entries as
        {"capability": ..., "why": ...} objects rather than bare strings, which
        is a more useful shape and one its own `# OUTPUT` block does not forbid.
        A gate that dies on a legitimate output is worse than a gate that fails,
        because the run in front of it is under pressure and will skip it.

        Accept both shapes. Take the capability text and drop the reason, since
        only the subject is matched against.
        """
        out = []
        raw = (feas or {}).get("kill_list") or []
        if isinstance(raw, dict):          # a mapping of capability -> why
            raw = list(raw.keys())
        for k in raw:
            if isinstance(k, str):
                out.append(k)
            elif isinstance(k, dict):
                # Prefer the documented key, then any obvious synonym, and fall
                # back to the longest string value rather than silently skipping
                # an entry, because a dropped kill is a kill that stops binding.
                v = (k.get("capability") or k.get("item") or k.get("kill")
                     or k.get("subject") or k.get("what"))
                if not v:
                    vals = [s for s in k.values() if isinstance(s, str)]
                    v = max(vals, key=len) if vals else None
                if v:
                    out.append(v)
        return out

    killed = kill_subjects()

    # A kill list that is missing or empty makes check 1 examine nothing while
    # still reporting success, which is the exact failure mode this script was
    # written to stop. Say so out loud rather than passing quietly.
    if not killed:
        notes.append("NO KILL LIST. feasibility.json carries no kill_list entries, so "
                     "the killed-capability check examined nothing this run. That is "
                     "either a conscience that killed nothing, which is rare, or a "
                     "shape this reader did not understand.")

    # A string's PATH can make it a refusal by construction, and ignoring that
    # made this check unusable on 2026-08-08. It raised 27 failures and every
    # single one was a false positive of the same shape: a non-goal recorded as
    # {"item": "<the killed thing>", "reason": "<why we refuse it>"}. The item
    # field NAMES the capability with no hedge in it, because the hedge is the
    # sibling reason field and because sitting in a non_goals list IS the hedge.
    #
    # That is the opposite of the defect this check exists to catch, and the
    # run contract explicitly demands non-goals be stated that way. A gate that
    # fails a document for obeying the contract teaches the next run to skip
    # the gate, so the path is now part of the reading.
    #
    # Narrow on purpose. Only these containers, and a non_goals entry still has
    # to carry a reason, or it is a bare refusal nobody justified and it warns.
    REFUSING_CONTAINERS = ("non_goals", "non_goal", "not_doing", "out_of_scope",
                           "kill_list", "killed", "excluded")
    ASKING_CONTAINERS = ("open_questions", "questions", "risks", "assumptions")

    def container_of(path):
        return re.findall(r"\.([A-Za-z_]+)", path or "")

    def scan_for_killed(label, section):
        for path, text in strings(section):
            low = norm(text)
            parts = container_of(path)
            in_refusing = any(p in REFUSING_CONTAINERS for p in parts)
            in_asking = any(p in ASKING_CONTAINERS for p in parts)
            for subject in killed:
                if not mentions(low, subject, need=3):
                    continue
                if in_refusing:
                    notes.append(f"{label} names the killed item inside a refusing "
                                 f"section ({parts[0] if parts else '?'}), which is "
                                 f"compliance: {subject[:56]}")
                    continue
                if in_asking:
                    notes.append(f"{label} raises the killed item as a question or a "
                                 f"risk rather than a promise: {subject[:56]}")
                    continue
                markers = refusal_markers(subject)
                # Outside those containers the hedge must sit in THIS string, not
                # merely somewhere in the section. One correct refusal elsewhere
                # must not immunise a promise here, which is the bug this check
                # shipped with.
                if any(h in low for h in markers):
                    notes.append(f"{label} references the killed item and refuses it "
                                 f"in place: {subject[:64]}")
                else:
                    fails.append(f"{label.upper()} PROMISES A KILLED CAPABILITY\n"
                                 f"        the feasibility gate killed: {subject[:100]}\n"
                                 f"        at {path}\n        {text.strip()[:130]}")

    # 6. Did the showrunner persist the agents' output, or its own summary?
    check_shapes(eng, a.repo, fails, warns, notes)

    scan_for_killed("roadmap", roadmap)
    scan_for_killed("PRD", prd)
    scan_for_killed("design", design)

    # 2. A stated non-goal delivered by the roadmap.
    # This check had never examined a single thing. It read ng["non_goal"], and
    # product-manager.md emits {"item", "reason"}, so every phrase came back
    # None and the loop did nothing while the script printed its all-clear.
    # Worse, the real PRD emitted non_goals: null, so there was nothing to read
    # under any key. Both failure modes are now visible.
    non_goals = prd.get("non_goals")
    if not non_goals:
        warns.append("the PRD states NO non-goals. product-manager is contracted to "
                     "emit them and a proposal with no stated scope boundary is how "
                     "a Later item becomes an expectation. Nothing to reconcile the "
                     "roadmap against here.")
        non_goals = []

    def ng_phrase(ng):
        """The non-goal text, whatever key the PRD used to carry it."""
        if isinstance(ng, str):
            return ng
        if not isinstance(ng, dict):
            return ""
        for k in ("item", "non_goal", "goal", "name", "text", "description"):
            v = ng.get(k)
            if isinstance(v, str) and v.strip():
                return v
        return ""

    for ng in non_goals:
        phrase = ng_phrase(ng)
        if not phrase:
            warns.append("a non_goals entry carries no readable text under any known "
                         f"key, so it was not reconciled: {str(ng)[:90]}")
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
        # Match on DISTINCTIVE terms only. "The Desk Answer Book" yields desk,
        # answer and book, and all three are domain wallpaper, so the old check
        # matched any text mentioning a desk and could never fire. A drift
        # warning that cannot fire is worse than none, because the clean run
        # reads as evidence the builds agree.
        kt = distinctive(keyterms(pick_name, n=6))
        if not kt:
            warns.append(f"the locked pick ({pick_name[:60]}) is named entirely in "
                         "domain-generic words, so drift cannot be detected from its "
                         "name. Read the four outputs by hand this run, and prefer a "
                         "pick name carrying at least one distinctive term.")
        else:
            for label, text in (("design", blob(design)), ("PRD", prd_text),
                                ("roadmap", roadmap_text)):
                # mentions(), not any(). A single shared word is not evidence the
                # output is costing the same build: "Aurora Concierge Telemetry
                # Platform" matched on "aurora" alone, which appears all over a
                # study about aurora season, so a total pick substitution raised
                # nothing at all.
                if not mentions(text, pick_name):
                    warns.append(f"the {label} never names the locked pick "
                                 f"({pick_name[:60]}), check it is costing the same "
                                 f"build. Looked for: {', '.join(kt)}")

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
