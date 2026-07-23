# Internal Dossier, Bristol Bay Native Corporation, 2026-07-23

PRIVATE. This is the full internal paper trail for the run. Prospect data lives here,
never in the public repo. The public package is only the study page and demo.

## Pick and why
- Company: Bristol Bay Native Corporation (bbnc.net), Alaska Native regional corporation, Anchorage.
- Segment: anc. Fit total 24 (highest of the day's shortlist).
- Path: the day's inbound opt-in (Paychex, Inc.) was disqualified and suppressed
  (national payroll/HR-automation vendor, not an Alaska SMB, personal-email opt-in
  against a Fortune-1000 company). Resumed cold scouting; BBNC was the top of a clean
  shortlist of 8+ candidates across four segments.
- Replacement queue (if BBNC had disqualified): Calista (23), Doyon Government Group (22),
  Chugach (22), Alaska Property Managers (22, reach 5), Major Marine Tours (21),
  Alyeska Therapy Center (21), PND Engineers (21), UNIT Company (21).

## Research (verified, claims.json is the source of truth)
- BBNC: ANCSA regional corp incorporated June 13 1972, ~9,900 shareholders (2015, now
  opening to descendants). Strongest year in history: $3.2B revenue, $202M earnings,
  $84M net income, ~$31M distributions.
- Government Services Group: 22 subsidiaries, over 2,500 personnel worldwide, more than
  $300M/yr in contracts, many 8(a) SDBs. Agencies: DHA, USAF, US Army, NRC.
- Also: BBCH construction (5 brands), industrial/petroleum, seafood, tourism, new
  financial-services line (Alaska Growth Capital / Alaska Investment Management).
- Pain (structural): proposal/capture/8(a) compliance across 22 separate entities;
  perpetual graduate-and-replace churn on the nine-year 8(a) clock leaks past-performance
  memory. Also live payroll/compliance hiring and board-season shareholder call surges.
- Competitors and AI: peer ANC Koniag has CASPER + Koniag AI Solutions (vendor metrics:
  75% requirements-analysis cut, 50% language determination, $29.3M savings); ASRC Federal
  mission-delivery AI; Doyon internal HR/payroll automation; Alutiiq Salesforce capture
  (automation not AI). BBNC shows NO public AI. Leap: cross-subsidiary past-performance RAG
  is a gap no verified peer has claimed.
- Industry: Deltek Clarity 2026 (917 GovCons): adoption 45->90%, 84 hrs/proposal,
  83% missed opps, margins 20->17%, ~5% "fully developed". Hard CUI/CMMC/FedRAMP/ITAR
  limits; human-in-the-loop mandatory. GovDash/SPATHE and Sweetspot vendor claims.

## Contact (verified)
- Celeste Hunt, Chief Business Development Officer, Bristol Bay Construction Holdings,
  chunt@bbch-llc.com (verbatim on https://www.bbch-llc.com/contact/).
- CAVEAT: she leads the construction sibling, not the primary gov-services target. No
  verifiable email exists for the gov-services group (parent offers only a form + phone
  907.278.3602). She is a genuine, senior, relevant BD decision-maker whose own bid-and-
  capture function is directly served by the build, so the draft goes to her honestly.
- Leadership (verified, bbnc.net): Jason Metrokin (CEO), Scott Torrison (EVP & COO),
  Ryan York (CFO), Renee Wardlaw (SVP & CAO), Regina Monroe (President Bristol Bay Services).

## Discovery and pick
- Full opportunity map (12 areas) scored for underserved. Target opportunity: proposal
  reuse across the 22-subsidiary 8(a) family (underserved 16).
- LOCKED build: Capture Memory, a governed retrieval layer over BBNC's own past-performance
  library (generation-light, deterministic access control outside the model, nothing auto-
  submitted), with Opportunity Radar (deterministic SAM.gov eligibility lookup) as companion.
  Shred-to-Draft (human-checkpointed) is the funded Phase-2. Shared-Services Agentic OS
  killed as a first build.
- Feasibility: retrieval tier + one generation-light LLM step. Where NOT to use AI: the
  CUI/ITAR/8(a) access boundary and NAICS/eligibility matching (deterministic). Data-
  readiness (corpus assembly + classification) IS the project; retired by a 2-4 week spike.

## Engineering
- Staff-engineer: 11-component C4 design, GovCloud/GCC High boundary, deterministic ACL
  pre-filter, citation + separate screening instance, walking skeleton on one sub
  (8-14 wks), Radar (3-5 wks), group rollout unestimated until spike returns per-doc cost.
- PM: proposal-grade PRD, PR/FAQ opening, falsifiable metrics (precision@k, citation
  faithfulness / zero leakage, proposal-hours, reuse rate), reason-bearing non-goals.
- ROI (computed in code, roi_math.py, rate $88/hr assumed): conservative ~$11.8k/yr,
  $133k TCO, 39% recovered, NO cash payback in 5yr (clears as decision data); most-likely
  ~$26.6k/yr, $100k TCO, 119%, payback ~45 mo; aggressive ~$59.9k/yr, $80.5k TCO, 342%,
  payback ~14 mo. Capacity not cash (defer-hire test), win-rate quarantined out of cash math.
- Delivery-lead: WSJF Now/Next/Later roadmap, staged funding gates each earned by measured
  results, full opportunity map carried in Later.

## Gates
- Fact-checker (research): verdict fix, 3 trims applied. Company confirmed real Alaska
  business; contact verified.
- Fact-checker (study): verdict fix, 3 precision softenings applied; all numbers verbatim.
- Study-critic: fix (3 mechanical fixes: MIT/RAND source rows, $88/hr stated, payback
  reconciled), then SHIP on re-audit.
- Demo: genericized unverified subsidiary names to A/B/C, glyphs swapped to text.
- Lead-critic: (see outreach.json).

## Deliverable
- Study: runs/2026-07-23/bristol-bay-native-corporation/field-study.html (+ .pdf, demo.html).
- Published (public, unlisted, noindex): alaskaaihq.com/awesomeproposal/bristol-bay-native-corporation/
- Draft to: Celeste Hunt, chunt@bbch-llc.com, from docket@ (Talon sets sender and sends).
