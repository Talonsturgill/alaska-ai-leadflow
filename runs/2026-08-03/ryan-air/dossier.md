# Internal dossier, Ryan Air, Inc., 2026-08-03

PRIVATE. This file holds prospect research and the full internal package. It never leaves this repo.

## The company

Ryan Air, Inc. (ryanalaska.com), Anchorage HQ, Alaska bush freight carrier. Seven bush stations, Aniak, Bethel, Emmonak, Kotzebue, Nome, St. Mary's, Unalakleet, plus Anchorage corporate. Founded 1953 in Unalakleet.

**Ownership, the load-bearing correction of this run.** Ryan Air joined the Saltchuk Family of Companies, per its parent Saltchuk Aviation, and is one of six Saltchuk Aviation companies. Its own about page still reads 'a family and native company managed by the third generation of Ryan family', which is true of MANAGEMENT and silent on ownership. NO artifact this run describes them as family owned or Alaska Native owned, and no acquisition year is asserted because the parent's article carries none. Lee Ryan was named company president in 2019.

**Size is a spread, not a number.** The company publishes three different aircraft counts and two village counts across its own pages and its parent's. Fleet 20 to 25, hubs 7 or 8, villages 70 to 80, headcount 150 to 180 plus. The spread is the verified claim.

## Why it was picked

# Selection, 2026-08-03

Four lead-scouts ran, one per ICP segment. 24 candidates returned, every one
page-verified, none on the EXCLUDE set (checked in code with ledger.py check,
not by eye).

## TODAY'S LEAD

**Ryan Air, Inc.** (ryanalaska.com), Anchorage HQ with hubs in Aniak, Bethel,
Emmonak, Kotzebue, Nome, St. Mary's and Unalakleet. fit_total **24**, the
highest of the day and the only candidate above 23, so no tiebreak was needed.

Scores: ai_solvable_pain 5, ability_to_pay 4, reachability 5, offer_fit 5,
alaska_signal 5.

Why it won. Third-generation family and Alaska Native owned bush carrier moving
freight, mail and charters to about 80 Western Alaska villages from eight hubs.
Reachability is the highest score any candidate earned today, eight named
station managers plus a corporate address and two public department mailboxes,
all on a page the scout fetched. Segment shape is one we have never worked, and
the timing is real, Western Alaska freight and fuel season runs through October
and the federal fiscal year closes September 30.

## REPLACEMENT QUEUE (ranked, use in this order if the lead disqualifies)

Ties at 23 are broken by reachability first, then offer_fit, per the contract.

| # | Company | Domain | Segment | Total | Reach |
|---|---|---|---|---|---|
| 1 | Orthopedic and SportsMedicine Clinic of Fairbanks | sportsmedicineak.com | healthcare | 23 | 5 |
| 2 | Seward Hospitality Group | sewardhospitalitygroup.com | tourism | 23 | 4 |
| 3 | Cape Fox Corporation | capefoxcorp.com | ANC | 23 | 4 |
| 4 | The Aleut Corporation | aleutcorp.com | ANC | 23 | 4 |
| 5 | Advanced Physical Therapy | aptak.com | healthcare | 23 | 3 |
| 6 | Cook Inlet Region, Inc. (CIRI) | ciri.com | ANC | 23 | 3 |
| 7 | TEMSCO Helicopters | temscoair.com | tourism | 22 | 4 |
| 8 | Alaska Tour and Travel | alaskatravel.com | tourism | 22 | 4 |
| 9 | Chugach Alaska Corporation | chugach.com | ANC | 22 | 2 |
| 10 | Everts Air (Tatonduk Outfitters) | evertsair.com | other | 21 | 3 |
| 11 | The Superior Group | superioralaska.com | other | 21 | 4 |
| 12 | Major Marine Tours | majormarine.com | tourism | 21 | 4 |

Below the queue, scored but weaker: Petro Marine Services 20, Sourdough Express
20, Fountainhead Hotels 20, TLC Care Services 19, The Eye Guys Alaska 19,
Sealaska 19, Rust's Flying Service 19, Alaska Premier Dental 18, Alyeska Title
18, Koniag 18, Alaska Behavioral Health 17.

## REPUTATION SCREEN, three permanent segment exclusions surfaced

The ANC scout screened out NANA Regional Corporation, Ahtna Incorporated and
Doyon Limited on the same rule that suppressed Bering Straits, documented ICE
detention contracting through Akima, Ahtna Federal and Doyon Government Group.
Suppressing them so no future scout spends a cycle rediscovering it. This is a
never-contact write, which is the safe direction to err in.

## Dropped by scouts before scoring, recorded so a later run does not re-chase

Alaska Village Electric Cooperative (avec.org, HTTP 503 on three fetches),
Bering Air (bot wall, plus a July 2026 NTSB finding on the fatal Nome-area
crash), Construction Machinery Industrial (403 to us, would starve the research
room), Olgoonik (403 on every fetch, and needs the detention screen first),
Bowhead Transport (a UIC subsidiary, already excluded), JAG Alaska (parent is
Michigan based), CAM Alaska (under the ability-to-pay bar).


## The pick, and the four risks

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


## Discovery, the whole-business map

The strategist mapped 20 areas of the operation and scored 15 jobs before any build was chosen. The full map is in discovery.json. Target opportunity:

> When my freight lands in the village, tell me in writing that it is here, so I can collect it before storage fees start.

Three jobs tied at the top of the Ulwick board and two were ruled out on their merits. Village weather and runway conditions scored 14 and was refused because the cost of error is a human life and the human relay is the safety control. The five missing policy pages scored 14 and need no AI at all, so that is handed over free. The arrival notice job was the survivor.

**The free recommendation outranks the paid one.** Publishing the five missing policies scores 16.2 on RICE against 2.08 for the build we would sell. It leads the roadmap.


## Feasibility, what was killed and why

**Arrival Notice Desk** - DOWNSCOPE

Kept, renamed honestly, model made CONDITIONAL. On today's record the lowest rung that clears is deterministic software: a diff, a date calculation under a published rule, a fixed template and a release button. Week one is a FORMAT FINDING at one hub, and if the reconciliation is a Takeflite report or export the extraction model is deleted from scope, making the build cheaper AND more reliable. Consignee matching uses deterministic fuzzy matching with a human queue below threshold, never an LLM. Pilot at BETHEL, not Aniak or Nome.

**Takeflite Event Notification Engine** - DOWNSCOPE

Reduced from a twelve week build to a TWO WEEK ACCESS SPIKE whose only deliverable is a written yes or no on API access, event schema and contract terms, with a go or no-go attached. Nobody prices or promises the engine before that answer exists. Also stop calling it an AI candidate, it contains no model of any kind, and selling it under an AI heading is the agent washing Gartner names.

**Self-Serve Tracking Upgrade** - DOWNSCOPE

Downscoped from a four person-week build to ONE SUPPORT TICKET first. Tell them to ask Takeflite whether the Bypass Mail Order field can be enabled, because Everts exposes it on the same platform, so configuration is the likely answer. If it is a setting, nobody should be paid for it, including us. We say that out loud even though it removes billable work, because being the shop that tells them the cheap answer is the entire reason the rest of the study gets read. Zero AI either way.

**Station Voice and Chat Agent** - KILL

Killed on the record, on our own reasoning rather than deference to its 0.13 score. The ladder settles it before liability even enters: every intent decomposes to a lookup or to arithmetic, both of which deterministic software does at effectively 100 percent, testable, explainable and cheaper, so Rule 1 of Rules of ML applies at full strength and there is no unique thing AI does here. As specified it is not an agent, it is a chatbot with a database lookup and an escalation path, and calling it agentic is agent washing. Cost of delay is genuinely NEGATIVE, waiting improves it.

**Tariff Quote Engine** - KEEP

Keep in the Next lane, labelled in the study as containing ZERO AI, since that label is the point rather than a caveat. Best data readiness on the board and it is not close, the entire rule set is published verbatim with no model, no third-party dependency, no labeling and no corpus. Guardrails: the NAC-style disclaimer their sibling already publishes, and rate-table drift, the calculator must read from one maintained table and print the effective date on every quote. One dependency on the free work, an estimate can't say when freight moves because no cutoff is published.

**Internal Station Agent Copilot** - DOWNSCOPE

Downscoped to the Later lane and dropped a rung. It is squeezed from both sides, which is the finding: the high-frequency agent questions are either arithmetic, which belongs to the quote engine, or policy that is not written down anywhere, which belongs to the free publishing work. What is left is thin enough that the first honest version is a maintained internal reference page with search, NOT retrieval. Promotion trigger is explicit, log agent questions for a month after the policies are published, and if the logs show real natural-language variety keyword search misses, retrieval has earned its rung and we build it with an eval set drawn from those logs.

**Publish the missing policy pages** - KEEP

Keep, LEAD WITH IT, charge nothing. RICE arithmetic confirmed, 9 reach times 1.0 impact times 0.90 confidence over 0.5 person-weeks is 16.2 against 2.08 for the pick. It goes IN FRONT of the paid work rather than behind it.

### Where not to use AI
Nothing a shipper reads in the Arrival Notice Desk is written by a model. Finding what newly arrived is a diff, the storage date is arithmetic on a rule Ryan Air already publishes, matching a consignee is deterministic fuzzy matching with a human queue below the threshold, and the notice itself is a fixed template, all of which can be tested line by line in a way no model can. The only place a model is even considered is reading a paper reconciliation sheet, and that node drops out of scope entirely if the sheet turns out to be a Takeflite export, which is the outcome we are hoping for. We also decline the whole dispatch and weather lane, where VEIA-style tooling is real and relevant, because the cost of error is a human life and the human relay is the safety control.

### Honest flags
- The format of the daily on-hand reconciliation is unknown, and it decides whether this build contains any AI at all. If it is a Takeflite export, we delete the model and say so.
- Consignee contact details are the gap that can block the whole build. If the contact data is not there, phase one is contact capture, a data project rather than an AI project, and that goes in the scope in plain words.
- Takeflite API access is unverified and the vendor grants it, not Ryan Air. That is why the pick avoids needing it.
- No volume, call-count, cycle-time or error-rate baseline exists for this company. Every figure is a modeled illustration, not a measurement, and the shipment poundage figure is on the DO_NOT_USE list so no volume claim may appear anywhere.
- The once-daily trigger CAPS call deflection, and we say it before a reader spots it. A reconciliation that closes at end of day protects the RECORD better than it protects the PHONE, so a customer whose freight lands at ten in the morning may still call at noon.
- Human review degrades into rubber stamping. Override rate is tracked as a live metric, and a rate falling to zero is evidence the review became theatre, never evidence the system became perfect.
- The 16.2 RICE on the free policy work is publishing effort, not decision effort.
- The Everts relationship changes the pilot site rather than the scope. The on-hand list at Aniak and Nome plausibly mixes carriers, so if the reconciliation does not distinguish carrier at all, those two stations are blocked until it does.
- Saltchuk Aviation Shared Services may own this work, and sibling Northern Air Cargo already runs the estimator we would otherwise pitch. MIT NANDA found buying from specialized vendors succeeded about twice as often as internal builds, so before selling anything we should ask whether Takeflite or a notification vendor already sells it. Saying that costs us work and it is true.
- The bypass mail order lookup may be a vendor configuration rather than a build. Tell them to open a ticket first, and if it is a setting nobody should be paid for it, including us.
- Hold the tone at gaps a busy carrier has while its rates team ships every month, never at neglect, because nine customer-facing pages changed in the last six weeks and the prospect owns the sitemap that proves it.


## The engineering room

### The ask was resized mid-run
{
  "what_happened": "The roi-analyst built the case for the six-week desk as briefed and reported honestly that its CONSERVATIVE case does not clear. Computed in code: 57 percent of five-year TCO recovered, no payback inside the horizon. Under the ROI_METHOD decision rule the ask shrinks until its conservative case stands on its own, so the showrunner resized it.",
  "new_ask": "A two-week format-and-contact-data finding at Bethel. The deliverable IS the decision.",
  "why_it_clears": "Conservative recovers 217 percent of TCO with payback at month 28, and it clears on a CASH line alone with zero capacity dollars in the formula. All three scenarios pay back inside the horizon.",
  "the_desk_is_what_the_finding_gates": "The six-week desk is not dropped. It is what the finding decides, and it gets approved with MEASURED drivers replacing assumed ones, not before."
}

### ROI computed in code, six week desk (the ask as briefed)
```
[
  {
    "scenario": "conservative",
    "annual_run_rate_benefit": 6558,
    "cumulative_benefit_5yr": 28199,
    "tco_5yr": 49680,
    "percent_of_tco_recovered": 57,
    "payback_month": null,
    "pays_back_within_horizon": false
  },
  {
    "scenario": "most_likely",
    "annual_run_rate_benefit": 16257,
    "cumulative_benefit_5yr": 70716,
    "tco_5yr": 37229,
    "percent_of_tco_recovered": 190,
    "payback_month": 30,
    "pays_back_within_horizon": true
  },
  {
    "scenario": "aggressive",
    "annual_run_rate_benefit": 33075,
    "cumulative_benefit_5yr": 147184,
    "tco_5yr": 26335,
    "percent_of_tco_recovered": 559,
    "payback_month": 14,
    "pays_back_within_horizon": true
  }
]
```

### ROI computed in code, two week finding (the ask that shipped)
```
[
  {
    "scenario": "conservative",
    "annual_run_rate_benefit": 3600,
    "cumulative_benefit_5yr": 18000,
    "tco_5yr": 8280,
    "percent_of_tco_recovered": 217,
    "payback_month": 28,
    "pays_back_within_horizon": true
  },
  {
    "scenario": "most_likely",
    "annual_run_rate_benefit": 7700,
    "cumulative_benefit_5yr": 38500,
    "tco_5yr": 8083,
    "percent_of_tco_recovered": 476,
    "payback_month": 13,
    "pays_back_within_horizon": true
  },
  {
    "scenario": "aggressive",
    "annual_run_rate_benefit": 13300,
    "cumulative_benefit_5yr": 66500,
    "tco_5yr": 7245,
    "percent_of_tco_recovered": 918,
    "payback_month": 7,
    "pays_back_within_horizon": true
  }
]
```

### Riskiest assumption
That the consignee side of a Bethel airbill carries a written channel Ryan Air can actually reach, an email address or a mobile that takes text, for enough shipments that a written-notice desk changes anything. Everything else in this design has a fallback. This one has none. If most village consignees are reachable only by a call to a village agent or a sheet posted at the counter, the send leg is aimed at a channel that does not exist and phase one is contact capture, a data project wearing none of this architecture. All eight stations publishing a fax number is a hint that today's written notification may be paper, and a hint is not a finding.

### The spike that retires it
Two weeks, fixed fee, at Bethel, no production code. Days 1-2, take ten consecutive days of the daily on-hand reconciliation exactly as the station produces it and answer four things: export or sheet, does it carry a carrier column, is the shipment reference stable day to day, does anyone keep yesterday's copy. Days 3-6, pull 200 consecutive airbills for freight that landed at Bethel and count what contact channel each one actually carries, which produces the one number this whole design rests on. Count how many arrival notices go out today and by what means. Days 7-8, sit at the counter for two shifts and count and time arrival-status calls. Days 9-10, write it up as a go or no-go with THREE DOORS. Door A, export exists and contacts are there, build the desk with no model in it and say so loudly. Door B, export exists and contacts are not, phase one is contact capture and the desk ships behind it. Door C, paper only, price the reader against real sheets scored on a human-transcribed set, or walk away. No extraction accuracy figure may be spoken aloud before those sheets are in hand.


## Verification

The fact-checker ran twice. Round 1 on the research package returned FIX with 29 rejections and, more importantly, a DRIFT PATTERN: every directional error leaned the same way, making Ryan Air look further behind and the AI precedent look more solid than the pages supported. claims.json carries a DO_NOT_USE list of 18 items so none of it could reinfect downstream.

Round 2 on the finished study returned FIX with 12 rejections, all applied. The one-way drift was gone and had been replaced by a three-way split including an OVERSHOOT into unearned generosity about how well maintained their site is. RAND's 80 percent figure was cut outright rather than softened, because rand.org returned 403 on every attempt and nobody on this run had seen the page.

The study-critic ran four rounds and shipped it. Round 1 fix (12 items). Round 2 fix (fee cells not reconstructable from published drivers, rework exposure sized above the build price it was derived from, borrowed demo counts stated as fact about Bethel). Round 3 fix (three one-line items). Round 4 SHIP.


## Notes for the next run

- Twice this run a string substitution was reported applied without opening the surface it renders on, once because the string wrapped a line in the source and once because the change went into the data and not the markup. The guard is to grep for the OLD string after every substitution and require zero hits before calling it done.

- The word budget was exceeded deliberately, 3,700 against 2,000 to 3,000, on the study-critic's explicit ruling, because the overage is a failed ROI case plus the ask that replaced it, a four gate ladder with real off ramps, a section arguing against our own engagement, and the before/after figure.
