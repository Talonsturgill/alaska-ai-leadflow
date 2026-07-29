# Dossier - Allen Marine Tours - 2026-07-29

## Snapshot
Family and Alaska Native owned, founded in Sitka in 1970 by Bob and Betty Allen, now owned and operated by their grandson Jamey Cagle. Thirty day tour vessels across Juneau, Sitka and Ketchikan, with 305 seasonal and 100 year-round workers on a season that runs 1 April to 1 October. The fleet is custom built in your own Sitka shipyard. Four stacked lines, cruise line contracted shore excursions, a direct to consumer channel under True Alaskan Tours, charters and lodge catering, and the shipyard itself.

Domain allenmarinetours.com. Segment tourism. Fit 24/25, highest across all four
scout segments. Contact Sitkainfo@allenmarine.com, verified live on the company's
own contact page across three separate fact-check passes. Decision maker Jamey
Cagle, owner and CEO, grandson of the 1970 founders. No personal address is
published anywhere fetchable, and a data-broker pattern address was found and
deliberately NOT used.

## RUN CONDITIONS (unusual, read this)
Supabase was unreachable all run (project hibernated, stuck mid-wake, every query
failing 28P01). The owner authorised proceeding without it and excluded Bristol Bay
Native Corporation by name. Dedupe was served from a NEW git ledger built this run
(scripts/ledger.py), seeded with seven companies reconstructed from the runs/
archive and the public publish history. INBOUND FIRST could not be checked, so if a
scanner opt-in was waiting it was not served. Supabase writes are owed, see
ledger/pending_supabase.json.

## THE PICK
The Operating Day Ledger. One read only screen for a single Juneau operating day, showing every sailing, its current head count, its assigned vessel and its committed vendors. A typed form captures every change to that day as a structured event. An identical templated notice goes to every party the change touches, with a one tap acknowledgement so you can see who has read it without chasing anyone. Underneath sits an append only log that can replay any past day exactly as it happened, including the corrections. Its first job is not to optimize anything. Its first job is to count the churn, which nothing public shows anyone has counted, so the decision about whether to build anything larger gets made on your numbers instead of on anyone's opinion.

Locked after the ai-feasibility-engineer DOWNSCOPED it to roughly a third of the
proposed effort and stripped BOTH AI nodes. Every one of six candidates bottomed out
at plain rules on the ladder. v1 contains no AI at all.

## WHY THIS AND NOT THE OTHERS
Sailing Day Control was the strategist's provisional pick at RICE 3.2. The
feasibility gate then killed three candidates outright and downscoped two.
- Sailing Day Control: DOWNSCOPE to ~1/3 effort, strip both AI nodes from v1
- Settlement and Commission Reconciler: DOWNSCOPE, strip AI entirely, per-template parsers beat an LLM on same-input-same-output and exhaustive testability
- Deckhand Desk: KILL, problem inferred not evidenced, no corpus evidence, solution shopping for a problem
- Season Staffing Funnel: KILL, adverse-impact exposure, buy an off-the-shelf ATS instead
- Capacity and Yield Board: KILL as a build, keep as an OUTPUT of v1's event log after one season
- Guest Answer Layer: KILL, five independent discounts, the ambiguity is in the policy not the answering

The guest-facing voice agent, the build a vendor would pitch here, scored LAST at
0.53 and was killed on five independent grounds. We are declining to sell it and the
study says so in writing.

## WHERE WE WOULD NOT USE AI
We would not use AI to write the change notices, and we would not let software assign crew. The notices are a template with your numbers merged in, so every caterer and coach company reads the same five lines in the same order every time and we can test it exhaustively, which is a thing you cannot say about a model. Crew assignment stays with a person, and the software's only job there is to refuse a combination that breaks a hard rule. Two of the four duties in that Operations Specialist posting are regulated work, and Moffatt v Air Canada says the operator owns whatever its automated channel produces, so a model that drafts a commitment is a model that can commit you to the wrong number. The reconciliation work is the same story, roughly all of it is deterministic matching that ordinary software does cheaper and safer than AI. Across all six things we looked at, the lowest tier that cleared the bar was plain rules every single time.

## THE ASK
Two to three week instrumentation slice on one port, honest return is decision data.
Conservative case recovers 105 percent of cost at month 12, which is break even, and
the study calls it break even. Payback range four to twelve months.
CONDITION STATED IN THE STUDY: both cash lines are money Allen Marine does not spend
with us later, computed against our own assumed 56,000 dollar winter price. If a
winter build was never on their table the cash return is zero and what they buy is
the measurement and the event log.

## HONEST FLAGS CARRIED INTO THE STUDY
- The data layer IS the project. All four required datasets (live passenger counts, per-hull capacity, crew roster and credentials, vendor commitments) are inferred from job-posting duties. Zero evidence any exists machine-readable. First paid engagement is discovery and instrumentation, NOT a build.
- We do not know what system carries the cruise-line contracted manifests, the PRIMARY business line. FareHarbor and Viator are verified only for the direct-to-consumer sister brand. If manifests arrive by phone, radio and email, integration is larger than estimated.
- Per-vessel capacity does not exist in evidence. Only 30 vessels is citable. The 24-140 range is a marketing disclaimer on one shuttle page, not a fleet table.
- Frequency and dollar magnitude of head-count churn is COMPLETELY UNMEASURED. The whole ROI rests on a number nobody has counted, and v1's real job is to count it.
- Human-in-the-loop is a WEAK control here. The single named reviewer works 10-14 hour days under high stress. Approval theater is the realistic failure mode.
- Crew work sits under USCG manning, credentialing and rest rules we could not source from public pages. Outside what this study can establish.
- Roughly ten operating weeks remain in 2026. Missing that window means an eight-month blind gap until late April 2027.
- The highest-certainty return in the set contains NO AI at all. Say that rather than hide it.
- c8 is a live board, re-count before the draft or drop it.
- Our read that contracted B2B pricing limits the yield lever is an INFERENCE. It goes on the call as a question, never in the study as a fact.

## QUALITY LOOP (what it cost to get here)
Seven critic rounds. Round 1 claims fact-check returned FIX on 6 of 28 claims, five
leaning the same direction. Rounds 2 to 4 study fact-checks found the same
directional drift three more times, including a spliced quote labelled as the
prospect's own words when it was our inference. Rounds 5 to 7 study-critic found 26
then 6 then 2 items, one of which was a contradiction created by an earlier fix.
Final verdict SHIP, with both ROI columns independently rebuilt from the published
page.

LESSONS FOR THE MACHINE: fix a claim everywhere it appears, not the sentence a
critic quoted. Re-read every section that references a contract change, not just the
one edited.

## SOURCES (25)
1. Alaskan Dream Cruises shut down February 2026, spokesman naming particularly high overhead and complex logistics - https://www.juneauempire.com/2026/02/16/alaskan-dream-cruises-announces-shutdown-after-15-years/
2. The stated plan to refocus 100 percent of resources on day tour excursions and the shipyard - https://www.kcaw.org/2026/02/05/alaskan-dream-cruises-shuts-down-after-15-years-of-overnight-cruises-in-southeast/
3. The Operations Specialist posting, the four duties quoted verbatim - https://jobs.rwfm.tamu.edu/view-job/?id=112698
4. The same posting, high levels of stress and 10 to 14 hour days, 5 to 7 days a week - https://jobs.rwfm.tamu.edu/view-job/?id=112698
5. Juneau's first year of daily cruise passenger caps, 16,000 most days and 12,000 Saturdays against prior peaks up to 21,000 - https://www.ktoo.org/2026/04/27/juneaus-first-cruise-ship-of-2026-kicks-off-first-year-of-daily-passenger-limits/
6. Family and Alaska Native owned, founded 1970 in Sitka, now owned and operated by Jamey Cagle - https://allenmarinetours.com/about-us/
7. Thirty day tour vessels, 305 seasonal and 100 year-round workers - https://www.juneauempire.com/2026/02/16/alaskan-dream-cruises-announces-shutdown-after-15-years/
8. The 2026 season running 1 April to 1 October, with a travel and housing stipend offered - https://www.coolworks.com/allen-marine-tours/profile
9. The fleet custom built in the Sitka shipyard - https://allenmarinetours.com/about-us/
10. The Office Manager posting, managing FareHarbor and Viator and reconciling partner fees and commissions - https://www.alaskatia.org/member-tools/job-opportunities/20471
11. The Dock Representative posting, settlement transactions with cruise line representatives - https://jobs.rwfm.tamu.edu/view-job/?id=112694
12. Huna Totem's fifteen year Disney berthing agreement at Icy Strait Point through 2041 - https://www.akbizmag.com/industry/alaska-native/disney-cruise-line-commits-to-fifteen-more-years-at-icy-strait-point/
13. Yonder's vendor published case study on Black Cat Cruises - https://www.yonderhq.com/case-study/black-cat-cruises-chatbot-answers-immediately-24-7
14. Gartner, 321 customer service leaders, October 2025, on AI and headcount - https://www.techrepublic.com/article/gartner-ai-customer-service-rehire-2027/
15. Moffatt v. Air Canada, 2024 BCCRT 149 - https://www.mccarthy.ca/en/insights/blogs/techlex/moffatt-v-air-canada-misrepresentation-ai-chatbot
16. Arival Global Operator Landscape 4th Edition, 5,664 qualified responses - https://travelprofessionalnews.com/ota-bookings-hit-surge-direct-sales-slide-across-global-experiences-industry/
17. The prior Arival study, more than 7,000 operators, on reservation systems - https://www.travolution.com/news/travel-sectors/tours-and-activities/arival-unveils-largest-ever-study-on-the-state-of-the-global-experiences-industry/
18. FareHarbor Agent announcement, 27 April 2026, no published pilot results - https://fareharbor.com/blog/meet-fareharbor-agent-ai-powered-guest-communication-for-tour-operators/
19. The True Alaskan Tours cancellation policy chain - https://truealaskantours.com/frequently-asked-questions/
20. Allen Marine recommending guests book through the cruise line - https://allenmarinetours.com/tour/waterfront-shuttle-ward-cove-to-downtown-ketchikan/
21. Vessel size varying by departure, 24 to 140 passengers - https://allenmarinetours.com/tour/waterfront-shuttle-ward-cove-to-downtown-ketchikan/
22. Three port offices with separate phones and inboxes - https://allenmarinetours.com/contact-us/
23. Captains coming through the ranks, and several with 15 to 20 years - https://allenmarinetours.com/about-us-2/
24. Adventure Green Alaska, Whale SENSE, Tourism Best Management Practices and AIANTA participation - https://allenmarinetours.com/sustainability/
25. ECMWF's AI Forecasting System in operations - https://www.ecmwf.int/en/about/media-centre/news/2025/ecmwfs-ai-forecasts-become-operational