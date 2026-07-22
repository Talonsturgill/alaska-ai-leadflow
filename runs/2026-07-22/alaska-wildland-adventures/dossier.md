# Internal Dossier — Alaska Wildland Adventures — 2026-07-22

PRIVATE. Not for external distribution. This is the full internal record of the
research and engineering process behind the Field Study shipped to this company.

## Selection

Segment: Tourism and visitor industry. Fit score: 22/25 (highest of 22 candidates
across four segments scouted). Domain: alaskawildland.com. Full ranked shortlist
and replacement queue in out/2026-07-22/selection.md.

## Research room (Phase 2)

Four researchers (company-analyst, people-finder, competitor-analyst,
industry-analyst) ran in parallel. Findings collected in out/2026-07-22/research.json.
The fact-checker re-fetched every cited source, verified the contact, and rejected
several unsupported specifics (an inflated "100+ languages" claim, uncited award
claims, uncited numeric specifics). Verified claims survive in
out/2026-07-22/claims.json, the only file downstream work was allowed to cite.

Verified contact: Kelsey Clifford, Marketing and Social Media Manager,
kelsey@alaska-wildland.com. No verified personal email exists for owner Kirk Hoessle.

## Discovery room (Phase 3)

product-strategist mapped the whole opportunity space from claims.json alone (no
showrunner summary, no preferred angle, per the anchoring law). Nine areas mapped,
four scored as Jobs To Be Done opportunities, one target opportunity selected
(guest inquiry response speed and staff overload), four candidate builds ranked by
RICE and Cost of Delay. Full output in out/2026-07-22/discovery.json.

ai-feasibility-engineer walked the feasibility ladder on all four candidates.
Downscoped the provisional pick (a guest-facing chat+voice assistant) to a
staff-facing Reservations-Staff Copilot first, killed two candidates outright
(an AI staffing-schedule tool, ruled a deterministic-rule problem not an AI
problem, and an AI waitlist-nurture tool, built on an inference-tier claim with
no verified data). Full verdicts in out/2026-07-22/feasibility.json. Locked pick
and Cagan viability check in out/2026-07-22/pick.md.

## Engineering room (Phase 4)

staff-engineer, product-manager, roi-analyst, and delivery-lead ran in parallel
on the locked pick. Full outputs collected in out/2026-07-22/engineering.json.

ROI arithmetic computed deterministically with scripts/roi_math.py from
out/2026-07-22/roi_drivers.json:
- Conservative: 104% of 3-year TCO recovered, payback month 32 of 36 (thin, late).
- Most likely: 200% recovered, payback month 17.
- Aggressive: 470% recovered, payback month 7.
Conservative case clears, honestly and thinly, on its own.

## Assembly and render (Phase 5)

study.json assembled from claims.json, discovery.json, feasibility.json, pick.md,
and engineering.json to the FIELD_STUDY_SPEC.md contract. Rendered with
scripts/build_study_page.py to field-study.html and field-study.pdf.
demo-builder produced demo.html, a scripted interactive demonstration of the
Reservations-Staff Copilot honest about being a demo.

## Verify and honesty audit (Phase 6)

fact-checker re-audited the finished study.json against live pages. Found and the
showrunner fixed four mechanical citation defects (an unreachable competitor
source dropped, an overreaching claim about SoFLA Vacations narrowed to what its
source actually supports, an orphaned unused source removed, a misattributed
hype-flag citation corrected).

study-critic ran three rounds:
- Round 1: FIX. Found the demo presenting three specific facts (a generic "9 to 12
  day" itinerary claim, two lodge names) with no matching source in study.json.
  Also found an "overtime" word inserted beyond what the cited source said, curly
  quotes in the demo, and an under-cited pain paragraph.
- Round 2: FIX. After the showrunner independently re-fetched and verified two lodge
  pages live and added them as sources 15-16, corrected the demo's itinerary claim
  to the verified "Alaska 11-Day Grand Adventure," fixed the quote characters, and
  added inline source numbers to the pain paragraph, the critic found two more
  issues, an unsourced partnership claim (Lindblad/AdventureSmith) and an
  unstated dependency of the ROI cash benefit on an unverified overtime-pay
  assumption.
- Round 3: SHIP. Partnership claim removed since it could not be re-verified, an
  open question about overtime pay added with AWA as owner, and roi.payback_range
  now states plainly that the cash benefit collapses to capacity-only if the
  overtime assumption does not hold.

## Write room (Phase 7)

outreach-writer wrote the carrier email per OUTREACH_CRAFT.md. lead-critic shipped
it on the first full review (round 1 clean pass on punctuation/kill-list/gate,
with one polish note applied by the showrunner, naming the company directly in the
opening line instead of "the standout Kenai Peninsula outfitter"). Zero kill-list
hits, personalization gate passed (48-hour promise vs. Seward job posting is the
verified this-company-only fact), ROI presented as a range.

## Outcome

Status: drafted. Draft addressed to the verified contact, Kelsey Clifford, from
docket@alaskaaihq.com. See out/2026-07-22/outreach.json for the final subject and
body.
