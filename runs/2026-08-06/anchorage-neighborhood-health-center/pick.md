# THE LOCKED PICK, 2026-08-06

## The build

**The new patient intake workflow for Anchorage Neighborhood Health Center.
Deterministic auto send and the sliding fee clock first, with two supervised
model steps on top of a measured baseline.**

This is the ai-feasibility-engineer's `recommended_pick`, rescoped from the
strategist's provisional pick. Phase one contains NO AI at all.

## Why this and not the others

The RICE arithmetic ranked a no-AI control (5.95) ABOVE the AI candidate (3.27),
and that result was not explained away. It became the walking skeleton. The
feasibility engineer then cut two of the strategist's three AI justifications:

- The sliding fee trigger classifier is **cut from AI scope**. All three triggers
  in C18 are computable from records ANHC already keeps. Plain code with unit tests.
- Runtime translation of anything a patient reads and acts on is **cut**. The four
  published forms are fixed documents, so more languages is a one-time human
  reviewed translation that becomes a static file lookup, not a model at runtime.

What is left for a model is two steps: comprehending what a patient writes in
their own words into candidate field values, and an allowlisted answerer over the
administrative questions ANHC already publishes. Both behind one human gate that
ANHC's own policy already imposes (C16 requires submitted documentation).

KILLED, and both on evidence:
- **Front Door Voice Agent** (0.90). Booking needs write access to an Epic MyChart
  instance operated for Providence Health and Services Alaska (C81), and the
  Community Connect inference was killed, so the path is unknown. Six steps at 90
  percent is about 53 percent end to end. Its only analogue is an unaudited vendor
  press release. It is also the product this shop over-indexes on, which is a
  reason to discount it further, not less.
- **Message Triage Teammate** (0.40). Its decisive metric is recall on the urgent
  class and there is no data to estimate it. A false negative on suicidal ideation
  is unbounded. Not scoped, therefore not sold.

## Cagan's four risks, checked before locking

- **FEASIBILITY.** Passed by the feasibility engineer. Two model steps, no write
  access required anywhere, degrades to today's process on failure.
- **VALUE.** The target opportunity scored highest on Ulwick (14) and it is the
  only one where the pain, the current process and a same-city alternative are all
  verified primary sources (C10, C11, C80).
- **USABILITY.** The patient path is text and web, which ANHC already runs (C14).
  The staff path is reviewing a filled form instead of gathering one on a call.
  CONSTRAINT: this structurally excludes the shelter outreach population (C30), so
  the metric must be reported split by channel or it will flatter the build.
- **BUSINESS VIABILITY.** Two consecutive surplus years (C39, C40, C41), so the
  money exists. The binding constraints are SHAPE not size: pricing may not be per
  clinician per seat (C54, C64), and delivery must carry the integration work
  because a community clinic may lack the data scientists on staff (C65). A
  patient-majority board sees any material system (C35, C36), so decision latency
  runs in monthly meetings and urgency pressure reads badly.

Viability is not weak. It is shaped, and the build was shaped to fit it.

## ECONOMICS PRE-CHECK, and it sets the ask the study will make

THE ASK IS PHASE ONE ONLY, PRICED AS A FIXED ORGANIZATION FEE, NOT PER SEAT.

What Phase One buys:
1. Instrumentation on ANHC's own registration path, producing three numbers that
   do not exist anywhere today: median hours from registration to intake forms
   returned complete, median hours to a confirmed appointment, and the share of
   registrations that never reach a booked appointment.
2. The deterministic auto send, which removes the first published 1 to 2 business
   day window (C10) outright, gated on the week-one answer to why that window
   exists.
3. A go or no-go on the model phase, decided on ANHC's own measured numbers.

WHY THE CONSERVATIVE CASE CAN CLEAR. It clears as DECISION DATA plus a permanent
process fix, which is the honest shape when no baseline exists. Phase two is
roughly three person months of model work, so spending a small fixed fee to learn
whether that spend is worth making, AND keeping the auto send whatever the answer,
is defensible on its own terms. It does NOT depend on a modeled labour saving.

WHAT THE ROI SECTION MUST THEREFORE BE. A BREAK-EVEN THRESHOLD TABLE, not a
savings projection. No registration volume exists in the verified record and NO
HEADCOUNT EXISTS AT ALL (killed outright by the fact-checker), so any saving is
unmodellable and printing one would be invention. The only verified labour anchor
is a Patient Financial Services Representative II at 23.98 to 35.97 dollars an
hour (C89), so the table is priced PER HOUR OF ADMIN TIME and never per FTE. The
table answers one question: how many registrations a month, at how many admin
minutes each, does this have to touch before Phase One pays for itself. ANHC can
check that against their own numbers in an afternoon.

The ask is sized here, and the roi-analyst builds the case for THIS ask.

## The tone rule that outranks everything above

ANHC ALREADY RUNS AN AMBIENT AI DOCUMENTATION TOOL IN CLINICAL PRODUCTION (C34),
ahead of every Alaska FQHC peer checked. They are not behind and they are not AI
novices. Any sentence that treats them as either is factually wrong and will read
as an insult.
