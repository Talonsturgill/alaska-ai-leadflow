# Fountainhead Hotels, internal dossier, 2026-08-05

PRIVATE. Prospect data. Never leaves this repo.

Live study: https://alaskaaihq.com/awesomeproposal/fountainhead-hotels/

## The company

Fountainhead Hotels, the hotel group of Fountainhead Development, Inc., Fairbanks.
Privately held, established 1985, no corporate parent. Three properties marketed,
Wedgewood Resort, Sophie Station Suites and Bear Lodge. Tim Cerny is president and
owner, Bobby Hanson is operations manager. Neither publishes a verifiable email.

## How it was picked

Four scouts, one per ICP segment, returned 23 page-verified candidates. All 23
cleared `ledger.py check`. Three tied at 24, Riverboat Discovery, Fountainhead and
Huna Totem. The contract breaks a tie on reachability first, and Fountainhead was
the only one of the three with a named human and a published business email
rendered as a live mailto on a page the scout actually fetched. The other two head
the replacement queue and were never reached.

## The contact

beckyk@fdialaska.com, Becky Kunkle, Reservations Manager. Verified twice, once by
people-finder and again by the fact-checker on a live re-fetch. It is the ONLY
email rendered anywhere on their homepage, attached to "Interested? Work with our
Reservations Manager Becky Kunkle for availability and very best rates."

She is a ROUTER, not the buyer. The email names nobody, assumes nothing about whose
desk it is, and offers the forward as an equal option to a reply. The people-finder
refused two pattern-invented addresses that aggregators asserted and one that a
search engine claimed was on their accessibility page, which it was not.

Fallback if this bounces: askus@fountainheadhotels.com, on their contact page under
all three properties.

## What the rooms found

The research room returned 56 claims. The fact-checker verified 46, rejected 11,
and reported a DRIFT PATTERN, that every substantive rejection leaned the same way,
toward making the company look more strained and further behind than its own pages
support. That warning shaped the rest of the run and was re-checked twice.

The strongest fact in the package is their own sentence: "We more than double our
current hotel staffing for summer to make sure guests have caring, personal
experiences at our properties," with Seasonal Front Desk Clerks heading the roster
they hire.

The hook is a defect anyone can check in a minute. Their Wedgewood aurora page
dates the season 21 August through 21 April. Their Bear Lodge rooms page dates the
same season mid-August to late April. The study says plainly that mid-August is a
phrase rather than a date, so the size of the gap is our reading of their words.

## The pick, and why it changed

The product-strategist provisionally picked "Desk Copilot, delivered on the Answer
Book as a funded phase one." Its OWN RICE table scored the zero-AI candidate at 4.05
against the AI candidate at 2.1.

The ai-feasibility-engineer overruled it. Three grounds:

1. The compounding math. Seven model-touched steps lands near 70 percent end to end
   at illustrative per-step figures, roughly one answer in three wrong somewhere.
2. The human in the loop was partly a comfortable story. The reviewer is by design
   a first-week seasonal hire, the person least able to detect a wrong answer,
   because not knowing the answer is why they asked.
3. The NAME was doing dishonest work. A phase two that might never be funded was
   becoming the headline, and a pick named Copilot produces a demo that is a chat
   box, which would contradict the study's own conclusion.

LOCKED: The Desk Answer Book, ai_role none. Desk Search is a conditional Next,
retrieval only, returning their own card verbatim, NOT priced.

Killed permanently: any voice agent (their desks are staffed 24/7 by design, which
removes the only justification), any guest-facing rate or cancellation assistant,
dictation, and building housekeeping route software (buy it, do not build it).

## The economics

Ask: 18,000 to 26,000 fixed, Phase 1 only. Four to seven weeks of one person, most
of it not software.

No labour saving was projected because every input is missing. The ROI is a
BREAK-EVEN THRESHOLD, computed in code by roi_math.py, reconciled on one basis
after the first fact-check caught the recovery row and the break-even row sitting
on different bases.

| | Conservative | Most likely | Aggressive |
|---|---|---|---|
| Five-year cost | 43,094 | 38,374 | 33,654 |
| Annual value if hours defer a hire | 4,087 | 23,358 | 59,130 |
| Share of cost recovered | 43% | 289% | 862% |
| Break-even interruptions per shift | 4.7 | 1.4 | 0.6 |

THE CONSERVATIVE CASE DOES NOT PAY FOR ITSELF on prevented interruptions, and that
is the section heading rather than a footnote. What it clears is the bar the
economics pre-check set, a durable artifact plus four gating baselines at a small
fixed fee. The table carries NO verified row, which is the honest signal that
nothing in it is yet a fact about their business.

## The fatal unknown, moved ahead of pricing

Whether the summer front-of-house roster is mostly RETURNING staff or first-time
hires. If mostly returning, the time-to-competence framing collapses. It resizes
the prize sharply and does not zero it. One email retires it, and the study makes
that single number the entire ask.

## Gates

- study_qa.py: 17/17 budgets met, exit 0. Word count 3,858 against a 3,000 target,
  which the critic examined and withdrew as a condition, judging roughly 1,400 of
  it to be table and source structure a prose budget was never written for.
- claim_sweep: two residual items, both judged benign (one date range with two
  endpoints, and the brief stating flatly what the ROI section then conditions).
- fact-checker on the finished study: FAIL on round one with five fixes, including
  a real arithmetic inconsistency between the recovery and break-even rows. All
  five applied.
- study-critic: FIX on round one with twelve blocking items. All twelve applied.
  SHIP on round two, verified each landed and none moved, and confirmed the ROI
  table reconciles to the last dollar.
- lead-critic: FIX, FIX, SHIP across three rounds. Round one killed an ambiguous
  antecedent, round two caught that the fix had moved rather than died AND that the
  number decayed, since "sixteen days out" would be false whenever Talon actually
  sent it. Round three carries no clock-relative number at all.

## The demo

Self-contained, zero network calls, no chat interface, no model. Its most
interactive moment tells the reader to type "checkout", watch it find nothing, then
type "check-out", and names that gap as the honest limit of Phase 1. It holds a
deliberately blank card for Bear Lodge's room season rather than borrow the
restaurant's dates, which was the top item on the fact-checker's rejected list.

## What the roadmap carries that the pick left behind

Housekeeping route optimisation as an explicit BUY, the corporate and extended-stay
path gated on one measurement only they can make, structured arrival intake as a
form and dispatch board with no voice agent, inbox routing, and a named owner with a
review cadence tied to the season boundaries they already publish.
