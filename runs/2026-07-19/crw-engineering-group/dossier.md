# Dossier — CRW Engineering Group, Inc. — 2026-07-19

STATUS: Study held at the ship gate. NOT sent, NOT drafted to the prospect.
A note was left for Talon instead. Recorded in leadflow.leads as "researched."

## Pick
CRW Engineering Group, Inc. (crweng.com), Anchorage & Palmer, AK. Segment: other
(labor-scarce / paperwork-heavy professional services). Picked from a 20-candidate
shortlist across all four ICP segments, fit_total 23/25, the highest of the field.
Full shortlist and scoring: selection.md (out/2026-07-19/selection.md in the repo,
not archived here since it names other candidates, private pipeline data).

## Research (Phase 2)
Four researchers ran in parallel (company-analyst, people-finder, competitor-analyst,
industry-analyst). The fact-checker's first pass returned "fix," five claims were
trimmed or dropped (two competitor profiles that would not re-fetch, two competitor
claims trimmed to only their confirmed sub-facts, one industry statistic pairing that
didn't hold together, and unverified PE/FNSPE credential letters dropped from
leadership). What survived became claims.json, the only source cited downstream.

Verified contact: info@crweng.com, present on https://www.crweng.com/about/leadership/
next to President Brian Looney's listing. No individually named personal email was
found on any fetched page. Leadership confirmed: Brian Looney (President), Shane
Blanchard, Pete Bellezza.

## Discovery and feasibility (Phase 3)
product-strategist mapped the whole business, scored five opportunities, and picked
"assemble a compliant RFP/SOQ response fast" as the target opportunity (Ulwick score
15, highest of the set). ai-feasibility-engineer downscoped the pick to keep the
compliance checklist deterministic (never AI-judged) and killed two other candidates
outright, a recruiting-automation idea (real pain, but a conventional ATS problem,
not a genuine AI fit, and risky in a labor-scarce market) and a rural client
project-status portal (no sourced client complaint, cuts against Alaska's buy-local
culture). Locked pick: Proposal & SOQ Engine (downscoped). Full reasoning in
pick.md, feasibility.json (out/2026-07-19/, not duplicated here).

## Engineering (Phase 4)
staff-engineer, product-manager, roi-analyst, and delivery-lead ran in parallel on
the locked pick. Architecture, PRD, and roadmap all held up under the study-critic's
review, no changes were requested there across two passes.

## The honest ROI finding
roi-analyst modeled a five-year TCO of $176k (aggressive) to $300k (conservative)
against three benefit scenarios. The CONSERVATIVE and MOST-LIKELY cases do not pay
back within five years, only the AGGRESSIVE case clears (18-24 month payback). This
is a real, honestly-modeled finding, not an error, stated plainly per ROI_METHOD's
core rule that a program only working under aggressive assumptions carries more risk
and we say so.

## Why the study did not ship
study-critic ran twice, per the routine's one-fix-and-rerender rule.

Pass 1 (verdict: fix) found: a math mismatch between the stated annual benefit
figures and the stated percent-of-TCO-recovered figures (missing an explicit
statement of the year-one benefit ramp), a citation that pointed the wrong source at
one of two blended statistics, an underspecified assumption behind the smallest ROI
benefit line, a generic "a principal" value-owner where a named person was available,
and a structural critique that the study priced and headlined the full 5-year build
as the ask rather than resizing the ask to a smaller pilot the honest numbers could
actually support.

Fixes applied: split the blended citation into two correctly-sourced entries, stated
the compliance-disqualification benefit's assumed frequency and dollar value, named
Brian Looney as value owner, and restructured the ROI section to lead with a
$20,000-$30,000 Phase-1 pilot ask with the full build carried only as gated,
illustrative context.

Pass 2 (verdict: fix, again) found the reconciliation still off by roughly 7-10
percent in all three scenarios (a residual ramp-math imprecision), and a structural
point that the pilot still leans on the full build's failing scenario narrative
rather than having its own standalone ROI case (e.g., "the value of the information
itself"). The critic was explicit that these are narrow, ROI-section-specific issues,
not fundamental hype, fabrication, or a hit against the AI_SCOPING or ROI_METHOD hype
tables, and that everything else, the feasibility ladder, the where-not-to-use-AI
line, non-goals, falsifiable metrics, the demo's honesty, and specificity to CRW,
passed clean on both reads.

Per the routine's rule (one fix-and-rerender cycle, then stop rather than loop), the
study is held. This is a true, honest field study that needs about fifteen minutes
of a human tightening the ROI arithmetic and giving the pilot its own small
standalone case, not a rebuild. See out/2026-07-19/study.json for the current state,
and the two study-critic reports below for exactly what to fix.

## What ships to Talon
field-study.html, field-study.pdf, and demo.html in this folder, exactly as they
stand today, plus this dossier. A note was left in Talon's Gmail drafts explaining
the above and pointing at these files. Nothing was sent or drafted to CRW.

## Study-critic findings, verbatim

### Pass 1 (fix)
- roi.scenarios/payback_range: stated TCO-recovery percentages didn't reconcile with
  the stated annual benefit figures (missing explicit ramp statement).
- roi.conservative_clears/scenarios: full build priced and headlined as the ask
  despite not clearing conservative, recommended resizing to a pilot ask.
- homework.industry_ai[1]: 63%/27% statistics blended under one citation that only
  supported one of the two numbers.
- roi.benefits[2]: compliance-disqualification benefit had no stated assumption
  basis.
- roi.value_owner: generic "a principal" where a named leader (Brian Looney) was
  available and the study was already addressed to him.

### Pass 2 (fix)
- roi.scenarios: cumulative benefit figures still off by roughly 7-10% versus the
  stated run-rate and ramp.
- roi.conservative_clears/scenarios/payback_range: the pilot still rides the full
  build's failing scenario narrative instead of having its own standalone,
  clearing ROI case.
- Minor, non-blocking: architecture diagram uses fully generic system labels with no
  named CRW-specific existing system (acceptable since CRW's real stack was never
  confirmed, but worth a human's attention if the diagram is refined).

Everything else (hype tables, agent-washing, hero-number pattern, feasibility ladder,
non-goals, metrics, base-rate honesty, demo honesty and scope, specificity) passed
clean on both reads.
