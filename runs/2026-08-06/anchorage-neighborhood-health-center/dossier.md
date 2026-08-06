# Anchorage Neighborhood Health Center, internal dossier, 2026-08-06

PRIVATE. Prospect data. Never leaves this repo.

Live study: https://alaskaaihq.com/awesomeproposal/anchorage-neighborhood-health-center/

## The company

Anchorage Neighborhood Health Center, founded 1974, a Federally Qualified Health
Center in Anchorage. Roughly 31.2 million dollars of FY2025 revenue against a
fiscal year that ends June 30th, not September 30th. Medicaid is about 34 percent
of clinic revenue. A patient-majority governing board that meets monthly, which is
the FQHC governance requirement and is the reason decision latency here runs in
months and urgency pressure reads badly.

## How it was picked

Four scouts, one per ICP segment, returned 24 page-verified candidates. All 24
cleared `ledger.py check`. ANHC topped the board at fit 24.

Two Anchorage candidates were SUPPRESSED on the values screen before any contact
was made or any research spent, per the reputation clause in DEFINITION OF DONE.
thtbc.com on Guantánamo and KIRA work, kikiktagruk.com on an FCA fraud settlement.
Suppressions went 11 to 13. Neither was ever reached.

## The contact

executiveassistant@anhc.org. Verified twice, once by people-finder and again by
the fact-checker on a live re-fetch, on two separately fetched ANHC pages. It is
the only staff email rendered on either.

She is a ROUTER, not the buyer. The published role is Executive Assistant and
Board Liaison, whose job is relaying to leadership and to the board. No ANHC
executive publishes a verifiable address anywhere, so the email names nobody,
assumes no prior thread, and is written to read correctly landing in a CEO's or
COO's inbox with the subject stripped.

The people-finder invented nothing. Where it could not verify, it said so.

## What the rooms found, and the fact it turned on

The research room returned 110 candidate claims. The fact-checker verified 89 and
killed 21.

THE FINDING THAT REFRAMED THE WHOLE STUDY: **ANHC already runs an ambient AI
documentation tool in clinical production**, drafting clinicians' visit notes,
confirmed on their own blog and by the Alaska Primary Care Association. No Alaska
community health center peer checked publishes anything comparable. They are ahead
of their peers, they are not AI novices, and every "you are behind" framing died
on that fact. It is written into pick.md as a tone rule that outranks the rest of
the file.

Set against it, their own new patient page publishes two waits of "Within 1-2
business days", the second ending in a scheduling phone call. One phone number,
907-743-7200, carries general questions, refills, lab results, registration,
sliding fee applications and mammography referrals. That contrast is the thesis:
**you already put AI into clinical production, your front door still ends in a
callback.**

Killed by the fact-checker and never used: an Epic Community Connect inference,
a headcount, a "220 clinicians" figure, a named scribe vendor, a "9,000 Alaskans"
figure, and an employee-count band. 22 forbidden strings were carried in
claims.json so `claim_sweep.py` could catch any of them re-entering downstream.

DRIFT PATTERN reported by the fact-checker: the rejections leaned in TWO
consistent directions, toward making the prospect look more committed to AI than
the record supports, and toward making them look further behind on the front door
than it supports. Both were re-checked in the direction pass.

## The pick, and why the strategist was overruled

The product-strategist mapped 17 areas of the business before any build was
chosen, produced 10 opportunities and 5 candidates. **Its own RICE table scored
the no-AI control at 5.95 against the AI candidate at 3.27.** That result was not
explained away. The control became the walking skeleton.

The ai-feasibility-engineer then cut two of the three AI justifications:
- The sliding fee trigger classifier, CUT from AI scope. Plain code with unit
  tests computes it from records ANHC already keeps.
- Runtime translation of anything a patient reads and acts on, CUT. The published
  forms are fixed documents, so more languages is a one-time human reviewed
  translation that becomes a static file lookup.

LOCKED: **the new patient intake workflow, deterministic auto send and the sliding
fee clock first, two supervised model steps on top.** Phase one contains no AI at
all. The two model steps that survive are comprehending what a patient writes into
candidate field values, and an allowlisted answerer over questions ANHC already
publishes, both behind a human gate their own policy already imposes.

I renamed the pick mid-run, acting on the feasibility engineer's own naming
honesty flag. The earlier name let a phase that might never be funded carry the
headline.

KILLED permanently, both on evidence:
- **Front Door Voice Agent** (0.90). Booking needs write access to an Epic MyChart
  instance operated for Providence Health and Services Alaska, and the Community
  Connect inference was killed, so the path is unknown. Six steps at 90 percent is
  about 53 percent end to end. Its only analogue is an unaudited vendor press
  release. It is also the product this shop over-indexes on, which the ANCHORING
  LAW says is a reason to discount it further, not less.
- **Message Triage Teammate** (0.40). Its decisive metric is recall on the urgent
  class and no data exists to estimate it. A false negative on suicidal ideation
  is unbounded. Not scoped, therefore not sold.

## The economics

Ask: **9,500 dollars, one fixed organization fee, phase one only, never per seat.**
Pricing shape was a constraint, not a guess, because the verified record says a
community clinic may lack data scientists on staff and per-clinician pricing is
the wrong instrument here.

The ROI section is a BREAK-EVEN THRESHOLD table, not a savings projection. No
registration volume exists in the verified record and no headcount survived the
fact-check, so any saving is unmodellable. The only verified labour anchor is a
published Patient Financial Services Representative II range of 23.98 to 35.97
dollars an hour, so the table is priced PER HOUR OF ADMIN TIME and never per FTE.

| | Conservative | Most likely | Aggressive |
|---|---|---|---|
| Registrations a month needed to break even | 288.6 | 134.8 | 72.2 |
| Registrations a month assumed | 101 | 190 | 317 |
| Annual value of time freed | $1,613 | $6,294 | $19,213 |
| Five year total cost | $20,124 | $20,124 | $20,124 |
| Share of five year cost recovered | 35% | 141% | 439% |

**THE CONSERVATIVE CASE DOES NOT PAY BACK AT ALL**, and that is the section
heading rather than a footnote: "On staff time alone the conservative case does
not pay, so what 9,500 dollars buys is the decision." What the money buys is three
baselines that do not exist anywhere today, plus a permanent process fix that
removes the first published 1 to 2 business day window outright, plus a go or
no-go on the model phase decided on ANHC's own measured numbers.

Costs are identical in all three columns because the fee is fixed, so the cost
side never gets a cheaper assumption, and every difference between columns is an
assumption about them. Each row carries a provenance mark, and exactly one row in
the table is marked `verified`, which is the honest signal that almost nothing in
it is yet a fact about their business.

## Gates

- **study_qa.py**: 19/19 budgets met, exit 0. Prose 2,998 words against a
  2,000-3,000 budget, reached after roughly ten trimming passes that had to
  preserve every caveat. Zero "cannot", zero sentences opening And/But.
- **study_lint.py --strict**: 0 failures, 0 warnings. ROI reconciled across 3
  scenarios, 12 printed cells recomputed from roi_drivers.json.
- **room_reconcile.py**: 0 failures, 1 benign warning (many distinct money
  figures). Round one FAILED on "ROADMAP DELIVERS A STATED NON-GOAL", a roadmap
  metric about translation that lacked its own refusal token when read alone.
  Fixed at source rather than patched.
- **study-critic**: 16, 16, 7, 5 blocking items across four rounds, SHIP on round
  five. Four findings were real and structural, not cosmetic:
  1. The conservative case cleared 108 percent only because an unsourced estimate
     of our own future invoice sat inside the labour benefit line. Rebuilt
     labour-only. It became 35 percent and never pays back.
  2. An undisclosed 40/50/60 percent haircut on the benefit meant the table could
     not be reproduced from its own rows, a factor of 2.5 gap. The haircut is now
     a printed driver row and the hand check reproduces to the dollar.
  3. "Every trigger in your sliding fee rules is arithmetic" was an overclaim.
     Their policy has three triggers and only expiry is arithmetic, and our own
     demo disproved the sentence. Narrowed in both places it lived.
  4. A drift pattern with TEN homes, asserting that the published 1-2 business day
     window is staff queue time. Corrected in 6 study locations and 4 demo
     locations. `claim_sweep.py` found the homes I would have missed.
- **lead-critic**: SHIP on round one. 53 words, 0 commas, no tells. The rounds
  went into the BRIEF before the writer ever ran, which is where the contract says
  the defect usually lives.

## The direction pass

Required by Phase 6.1a and written at out/2026-08-06/direction_pass.md, 1,121
words plus an ADDENDUM. The addendum corrects my own first conclusion. I wrote
that nothing needed changing, the fact-checker then found a lean I had missed, and
the addendum records both the miss and the correction rather than quietly
rewriting the original.

## The demo

53KB, self-contained, zero external calls, no model and no chat interface. It is
honest about being a demonstration. Its reachable-share assumption is set to 80
percent to match the study's conservative column, so the two tell the same story
rather than quietly disagreeing.

## What the roadmap carries that the pick left behind

The Later lane carries the rest of the 17-area map so nothing found is wasted: the
one overloaded phone number, the sliding fee clock beyond expiry, the 56-language
translation question kept as a one-time human reviewed job rather than a runtime
model, and the shelter outreach population that the text-and-web path structurally
excludes. That exclusion is a stated constraint on the metric, reported split by
channel, or the build flatters itself.

## Honest limits carried into the study

Nine honest flags from the feasibility engineer survive into the shipped study,
including that the independent evidence says the ambient-scribe financial case is
RETENTION rather than throughput, and that AI translation holds for Spanish and
degrades sharply outside it, which is the reason translation was cut from runtime.
