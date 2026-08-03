# THE LOCKED PICK, 2026-08-03

**Arrival Notice Desk, deterministic workflow with one conditional extraction node,
piloted at Bethel.**

The locked build is the ai-feasibility-engineer's recommended pick, downscoped from
what discovery proposed. Discovery called it "workflow automation with a narrow
document-extraction model". The engineer ruled that overstates what the evidence
earns, and the model is now CONDITIONAL on a week-one format finding. If the daily
on-hand reconciliation turns out to be a Takeflite export, the model is deleted from
scope and the build gets cheaper and more reliable. That is the outcome we say we
are hoping for, out loud, in the study.

## What it is

Rides a process the station is already required to run. The Bethel Lead Cargo Agent
posting says an on-hand reconciliation is completed daily, so each station already
produces a daily list of what is physically sitting at a destination. The desk takes
that list, diffs it against yesterday to find what newly arrived, drafts a written
arrival notice per consignee carrying the shipment reference, the arrival timestamp
and the date storage fees would begin under the published rule, and a station agent
releases the batch or holds any line. Sent notices are stored with their timestamp
as the record the tariff's storage clause depends on. A day-two reminder goes out on
anything still uncollected.

Nothing a shipper reads is written by a model.

## Cagan's four risks, checked before locking

**Feasibility.** Strong, and the engineer owns this one. Every customer-visible step
is deterministic and exhaustively testable. Seven of ten steps run at roughly 99.9
percent each, and their residual failures are bounced deliveries and stale contacts,
which are detectable and retryable rather than silent. No autonomy anywhere, so the
compounding-error math never gets the chance to run.

**Value.** Real, and unusually so, because it does not depend on customer behaviour
changing. This is the only job on the whole opportunity map where the company's own
published tariff creates the obligation rather than a customer creating a request.
Storage fees start three days after written notification of arrival, so the notice is
simultaneously the service, the cost reduction, and the evidentiary basis for a fee
they already publish.

**Usability.** Good. One screen, a capped batch, and only the diff and low-confidence
lines demand an explicit action. The reviewer is the person who physically handled
that freight that day, so the human in the loop holds genuine ground truth rather
than rubber-stamping a black box. The real risk is that review DEGRADES into rubber
stamping over weeks, which is why override rate ships as a live metric and a rate
falling to zero is read as theatre, never as perfection.

**Business viability. THIS IS THE WEAK ONE, and it sizes the ask.** Ryan Air is one
of six Saltchuk Aviation companies. Saltchuk Aviation Shared Services exists as a
named entity that could claim this work, and sibling Northern Air Cargo already runs
the self-serve estimator we would otherwise have pitched. A buying decision may not
sit entirely in Anchorage. Viability holds ONLY if the first ask is small enough to
sit inside a single operating decision at one hub rather than a group IT programme.
That is a constraint on the ASK, not a reason to drop the build, and it is why the
study asks for a one-hub pilot and not a network rollout.

The pick holds on all four. It is not dropped to the next candidate.

## ECONOMICS PRE-CHECK, the smallest honest ask

The ask the study will make is a **Phase 1 pilot at Bethel, one hub, roughly six
weeks**, and the ROI case is built for THAT ask and nothing larger.

Why that shape is the smallest honest one. Two facts about this build make anything
bigger dishonest today. The format of the daily reconciliation is unknown, and
whether Ryan Air holds current consignee contact details is unknown. Either answer
can change the build materially, and the contact answer can block it outright, in
which case phase one is contact capture, a data project rather than an AI project.
Pricing a network rollout across seven or eight stations before those two answers
exist would be reverse-engineering a number to clear an approval, which is exactly
the failure Flyvbjerg names and exactly what ROI_METHOD tells us the conservative
case has to be defensible against.

**The honest return is decision data plus a working desk at one station.** That is a
legitimate ask shape under the contract, and it has to be stated in those terms
rather than dressed up as a hard-dollar case. The pilot delivers four things a
larger commitment currently rests on and cannot get any other way: the format
finding, a consignee contact-data audit, a measured baseline for agent minutes and
written-notice rate at one hub, and a live desk producing timestamped notices.

**Does the conservative case clear its own bar?** Yes, on two independent grounds,
and it must clear on the first alone.

1. Recovered station-agent minutes at Bethel, the hub carrying four of the ten open
   positions. Every driver here is ASSUMED and must be labelled so, because no call
   count, cycle time or shipment volume for this company is verified anywhere and the
   poundage figure is on the DO_NOT_USE list. The case is a range over stated
   drivers, never a number.
2. The avoided cost of committing to a multi-station rollout under two unverified
   assumptions. A pilot that costs a fraction of the rollout and can retire both
   assumptions is cheap insurance against scoping the larger build wrong.

The roi-analyst builds for the Phase 1 pilot ask only. If the conservative case does
not clear at that size, the honest move is to shrink the ask further to a two-week
format-and-contact-data finding, which still clears because its entire deliverable is
the decision itself.

## What rides alongside, and what we refuse

**We lead with the free thing.** Publishing the missing freight cutoff, claims
procedure, embargo policy, perishables handling and station hours scores 16.2 on
RICE against 2.08 for the paid pick. It needs no AI, no integration and no vendor,
and it goes in FRONT of the paid work in the study, not behind it. The caveat travels
with the number: half a week is the publishing effort, not the decision effort.

**We tell them to open a support ticket before paying anyone.** Everts exposes a
Bypass Mail Order lookup on the same Takeflite platform Ryan Air already pays for. If
that is a tenant setting, nobody should be paid to build it, including us.

**We decline the obvious build, on the record.** A station voice and chat agent is
what a lazy vendor would lead with, and it is killed. Every intent decomposes to a
lookup or to arithmetic that deterministic software does at effectively 100 percent,
testable and cheaper. Moffatt v. Air Canada holds a carrier responsible for what its
systems tell a customer, and here the bot would be stating the fact that starts a
billable storage clock. Its cost of delay is genuinely negative, so waiting improves
it, which is the definition of something that should not be phase one.

**We decline the dispatch and weather lane entirely.** VEIA-style tooling is real and
relevant and we will not build there. The cost of error is a human life and the human
relay is the safety control.
