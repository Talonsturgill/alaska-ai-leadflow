# The locked pick, 2026-08-09

**Out of hours guest request capture and triage desk, timestamp first, model second.**

`ai_role: none` in phase one. That is the recommendation, not a caveat attached to one.

## What it is, in one sentence

A structured, multilingual request form plus an out-of-hours greeting on the 1-800
line plus a timestamped ingest on their own published inbox, all writing into one
queue, so a guest's cancellation or change request gets a server-written arrival
time against the 24 hour refund clock even when the reservation office is shut.

## Why this and not the others

The feasibility engineer killed the voice agent outright and downscoped three of
the remaining four. What survived is the deterministic core of the strategist's
provisional pick, with generation, booking validation and runtime translation all
stripped out.

The argument in one line: the guest's money sits on a 24 hour clock (c12) while
the only published route to act runs 40 hours a week (c10, c11). The gap between
a 24 hour clock and a 40 hour service week is the whole opportunity, and closing
it is a form, a clock and a queue.

## Cagan's four risks, checked before locking

**FEASIBILITY.** Cleared, and it is the least risky thing in the candidate set.
Phase one is a form, a server-side timestamp, an inbox ingest, a telephony
greeting and a governed content file. There is no model, no autonomy and no
dependency on the third-party ticketing system, because booking validation was
deliberately killed and the reference is captured as an unvalidated string. The
one integration nobody could assess from outside the company was moved out of
phase one rather than assumed away.

**VALUE.** Strong, and it is the only high-scoring opportunity in the file where
every component is the company's own published policy rather than an inference.
The residual risk is that they believe the phone is already fine. Phase one
answers that with their own numbers rather than our argument, which is the right
way to lose that disagreement if we are wrong.

**USABILITY.** High. A form with dropdowns and a booking reference field is the
most ordinary interaction on the internet, and the internal side is a queue of
items the reservation agent already handles today, just with an arrival time
attached. Nothing asks a guest to learn a new behaviour, and the new path is
offered at the exact moment the old one fails.

**BUSINESS VIABILITY.** Holds, and this is the risk that would have killed a
bigger build. They can afford it, 180 employees and almost 2,000 train starts a
season (c3, c7). They can adopt it, the change is additive and lands on a small
office rather than on the represented onboard workforce. It cuts legal exposure
rather than adding it, because a single governed source of policy text is the
direct answer to the Moffatt problem (c44), where the current site carries the
office hours on product pages and not on the cancellation page. Brand risk is
low, nothing guest-facing speaks in the company's voice that a human did not
write.

One viability item is flagged rather than assumed. About 40 workers voted to join
SMART-TD in April (c33). Reservation Agents are not among the roles that article
names, which is why this build appears clear of it, and absence from a list is
not proof of non-representation, so it is confirmed with the company before
anything ships.

## ECONOMICS PRE-CHECK, before the engineering room burns

Sizing the SMALLEST honest ask this build supports, so the roi-analyst builds the
case for that ask and not for the biggest build we can imagine.

**The ask is a Phase 1 pilot in the region of 25 to 30 thousand dollars**, which
buys the form, the greeting, the ingest, the governed policy file, professionally
translated fixed strings, and the four counters. Run cost is small because there
is no inference to pay for.

**The honest return is DECISION DATA FIRST, cash second, and that ordering is the
finding rather than a hedge.** The contract permits a pilot whose honest return is
measured baselines that gate a bigger spend, and that is exactly what this is.
Nothing in this business can be sized today. No channel split, no passenger count,
no trains per day, no call or email volume is published anywhere. Phase one
produces those numbers as a by-product of work the agent already does.

**THE HONEST COMPLICATION, and the engineering room must carry it rather than bury
it.** Making cancellation easier can COST them money in the short run. Today a
guest who cannot reach anyone inside 24 hours forfeits all rights to a refund
(c12), and the railway keeps that fare. A build that lets the same guest cancel at
9pm Saturday converts a forfeiture into a refund minus a $10.00 penalty. The gain
is reselling that seat on a ride that usually sells out in advance (c14), plus
fewer disputes and less goodwill damage. Which effect is larger depends on their
sell-out rate by departure, and they do not publish it.

So the conservative case may NOT lean on resold seats. It has to clear on the
things that do not depend on an unpublished number: out-of-hours contacts captured
that today bounce against a closed office, agent time not spent on repeat
questions while a train is loading, and the decision data itself. The roi-analyst
is briefed accordingly, and the study says this out loud, because a proposal that
only shows the upside of easier cancellation is exactly the kind of thing a
skeptical owner catches.

**Verdict: the ask clears at this size, and it is locked at Phase 1 only.** The
self-service cancellation desk and the phase-two classifier are both gated on
measured results, and neither is priced here.

## What rides to the Later lane

The delivery-lead carries these so nothing the discovery room found is wasted:
the deterministic self-service change and cancellation desk (gated on a written
feasibility assessment of the ticketing vendor's API, run in the off season), the
phase-two single-node classifier on inbound email, seasonal hiring (best measured
outside evidence in the file, weakest local evidence, and a union constraint), and
first-party post-ride feedback capture.

## What we recommend they buy from someone else

An off-the-shelf tourism chat widget at published list pricing of $95 to $295 a
month (c48), which we are not paid for, configured to answer only published
non-money content and to hand off on anything touching cancellation, refund or
price. With the plain warning that under Moffatt the liability for what it says
stays with them, whoever built it (c44). No vendor is going to open with that.
