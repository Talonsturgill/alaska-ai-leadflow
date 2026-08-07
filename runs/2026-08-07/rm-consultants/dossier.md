# Internal dossier, R&M Consultants, Inc., 2026-08-07

PRIVATE. Real prospect data. This file never leaves this repo.

- Live study: https://alaskaaihq.com/awesomeproposal/rm-consultants/
- Contact drafted to: Len Story, Chief Executive Officer, lstory@rmconsult.com
- Study-critic: SHIP on round 6. Lead-critic: SHIP on round 3.


---

## The locked pick and the economics pre-check

# THE LOCKED PICK, 2026-08-07, R&M Consultants, Inc.

## The build

**The Documentation Gap Sentinel**, Phase 1 of what would become the Field Record
Copilot. Phase 1 has NO AI IN IT AT ALL.

The ai-feasibility-engineer is the authority here and it downscoped the strategist
twice. It kept the model off the Sentinel entirely (the strategist had put a small
language model on the narrative node from day one and the engineer ruled it unearned),
and it confined the model in the later Copilot phase to exactly two nodes where the
input is genuinely messy. Every enumerable documentation requirement stays in rules,
because a rule can be listed, argued over with their own construction administration
lead, and tested exhaustively, while a model can only be sampled.

It also corrected the strategist's own label. The Sentinel is NOT the walking
skeleton of the Copilot. It touches storage, rules and reporting while leaving the
three riskiest components untouched, field capture, offline sync, and the export
into the owner's record. It is a standalone Phase 1 that earns on its own and
retires the data-access risk. The capture and export risks stay live until the
spike answers them.

## What was killed

The Firmwide Knowledge Assistant, and the reason is worth carrying into the study.
It was competitor envy driving scope, a direct answer to Michael Baker's Titan, and
a 100-person firm copying a 6,000-person firm's platform economics is the transfer
that does not survive contact. Reach alone was holding its RICE score up and the
strategist admitted it.

## What we are declining OUT LOUD, and this is the study's spine

The loudest cited pain in the whole claims file is proposal work sitting on senior
billable staff. The bullet "Conduct research and write technical portions of
proposals to assist in bringing in new work." is verbatim on TWO departments'
senior postings, and a third senior seat carries "Developing proposals."

We are not selling them that, and we say so.

Three evidential reasons, none of them modesty.
1. R&M announced a Proposal Manager into the Marketing Group on July 14th 2026,
   twenty-four days before this study. A live human fix is mid-installation.
2. The function is run by a 29-year FSMPS CPSM whose own bio names proposal
   development as a specialty.
3. The industry-analyst worked vendor case studies, comparison sites, SMPS and ACEC
   channels and the trade press and found NO named firm at any size attached to a
   measured proposal-productivity number with a stated method. It is the loudest
   marketed pocket in this industry and the thinnest measured one.

Meanwhile the one independent measurement anywhere in this industry sits on the
task their own posting names as a duty.

## Cagan's four risks, checked before locking

- FEASIBILITY. The engineer did this and it clears, conditionally. Two model nodes
  and one structural human gate, not a chain. The condition is a two-week spike.
- VALUE. Cited verbatim from their own posting, "Administer project documentation
  and audit trails to ensure funding participation", against a firm where nearly
  95 percent of work is for public clients. That makes a documentation gap a
  reimbursement problem, not a filing problem. Anchored by an independent
  FHWA co-sponsored measurement on the same task.
- USABILITY. Phase 1 requires NO change to how anyone works. No field app, no new
  habit, no training a seasonal crew. That is the strongest usability position
  available and it is why Phase 1 is the Sentinel rather than the Copilot.
- BUSINESS VIABILITY FOR THIS OWNER. Employee-owned, 100-plus staff, four offices,
  a fourth opened this February, moved up a Zweig headcount bracket between 2023
  and 2026, CMMC Level 2 certified in December 2025. They can afford an
  eighteen-thousand-dollar fixed fee, they have an IT group and a named compliance
  partner, and nothing has to be sold to a customer for it to pay. Adoption is the
  usual failure mode and Phase 1 sidesteps it by not requiring adoption.

VIABILITY CLEARS. No drop to the next candidate.

## ECONOMICS PRE-CHECK, and I GOT IT WRONG, and the room caught me

Back-of-envelope on the SMALLEST honest ask, conservative case only.

Drivers, all conservative, all assumptions we do not have from them:
  60 pay-estimate / progress-submittal documentation reconciliations a year
  2.0 hours each locating and reconciling against contract requirements
  0.75 hours each for the separate senior review pass
  95 dollars an hour loaded, 40 and 35 percent of that time removed
  8 project closeouts a year, roughly 12 hours each, 30 percent removed
  ZERO owner-agency review events in this column, by construction

THE ERROR. I narrated a conservative run rate of roughly 11,900 dollars a year
and sized an 18,000 dollar ask against it. The roi-analyst refused the number and
showed the arithmetic does not produce it. Computed in scripts/roi_math.py, these
drivers produce **8,792 dollars a year**. I had doubled a line. At 18,000 the
conservative case recovered 97 percent of five year cost and NEVER PAID BACK.
It did not clear.

This is precisely the failure the rule about computing every number in code
rather than narrating it exists to prevent, and the showrunner is the one who
broke the rule. It goes in the retro.

THE FIX, and no driver was touched. ROI_METHOD says shrink the ask rather than
pretty the number, so the ask shrank. Solved in code by holding the conservative
drivers fixed and sweeping implementation:

    ask      %TCO recovered   conservative payback
  18,000           97          never
  16,000          104          month 57
  14,000          111          month 52
  12,000          119          month 47
  10,000          128          month 42

**THE ASK IS NOW 12,000 DOLLARS, FIXED FEE, PHASE 1 ONLY**, split into two gates,
and the first is a real stop point so the only irreversible commitment is 4,000.
- Gate A, 4,000 dollars, weeks 1 and 2. The spike. Does the owner agency dictate
  the field record system, is today's documentation reachable and machine
  readable, and which projects actually carry CUI markings. Plus the four-week
  baseline starts. THEY CAN STOP HERE AND KEEP EVERY ANSWER.
- Gate B, 8,000 dollars, weeks 3 to 8. The rules-only Sentinel on live projects.

COMPUTED, all three columns, at the 12,000 ask:
  Conservative   8,792/yr   119 percent of five year cost   payback month 47
  Most likely   27,825/yr   384 percent                     payback month 15
  Aggressive    48,480/yr   684 percent                     payback month 7

The conservative case clears, late but inside the horizon, and the study prints
month 47 rather than hiding behind month 15.

## The condition the engineer would not sign without

If the spike finds that Alaska DOT&PF or another owner agency mandates a field
record system R&M has no authority to feed, the Copilot's export path collapses
and the Sentinel becomes the entire build rather than its first phase. The study
must SAY THAT, not quietly reshape the pitch afterwards.

## What the study may never say

- That R&M is behind on AI. The narrowed negative covers one services page and one
  page of a paginated news index. A firm can run AI internally and publish nothing.
- That R&M has ever had a disallowance, an audit finding or a record dispute.
- That any federal rule requires AI-use disclosure in an A/E proposal. None was found.
- That Michael Baker aimed Titan at proposal or capture work. That page never loaded
  and the release that did load does not mention proposals.
- Any revenue, headcount, hours, volume or win-rate figure for R&M. None is published.



---

## The direction pass

# THE DIRECTION PASS, 2026-08-07, R&M Consultants

One question, asked of the whole study and nothing else. Does this make them look
worse than the evidence actually does?

Three tests on every unflattering sentence. Could we KNOW this from outside their
building? Is the unflattering reading load-bearing or decoration? Would they
recognise themselves, or get defensive at something they know is unfair?

---

## FINDING 1, and I caused it. CUT, then RESTORED.

**The sentence.** "That seat is open now, one of eleven across your four offices."

**What licensed it.** Their open-positions page, verbatim, eleven roles. Solid.

**The problem.** The original draft followed it with "Eleven open roles at a firm
that just moved up a Zweig headcount bracket and opened a fourth office reads as
growth, not trouble." THE PROSE TRIM DELETED THAT SENTENCE and kept the eleven.

That is the drift pattern operating through a length gate rather than through an
agent. Every trimming pass cuts qualifiers before it cuts claims, because
qualifiers read as slack. What was left was a bare count of vacancies at a firm
whose own evidence says it is growing, which is exactly the shading this pass
exists to catch. Nothing an agent wrote was wrong. The showrunner's own editing
made the study less fair, twice, in two consecutive trims.

**Verdict: RESTORE, and find the words elsewhere.** Done.

## FINDING 2. The Today column asserts a workflow we have never seen. SOFTEN.

**The sentences.** All four changed rows of the before/after figure. "someone
opens the project folder and works out what this contract requires", "They search
daily reports, materials certifications, test results and quantity records", "A
senior reviewer builds a second completeness check from scratch", "Whatever is
missing gets chased, sometimes after the crew has already left that site."

**What licensed it.** Nothing about R&M specifically. The claims file says it
outright: "Whether R&M uses a commercial field system today is not published and
we do not claim to know."

**Could we know this from outside?** No. This is the generic shape of construction
administration work, drawn as though we had watched theirs.

**Is it load-bearing?** The figure is, the certainty is not. A reader who already
has a system will hit row two, think "we do not do that", and stop trusting the
rest of the page. The unearned certainty costs us more than it buys.

**Verdict: SOFTEN, and say plainly that the left column is our assumption.** Done,
in the text that leads into the figure. Naming it as ours to be corrected is
better than asserting it, and it doubles as the ask.

## FINDING 3. The eleven-openings fact, second look. KEEP.

Already carries "Your postings carry no dates, so we have no idea how long any has
been up and we are not going to pretend otherwise." That is the honest ceiling,
stated in our own voice about our own analysis. Keep as is.

## FINDING 4. The competitor paragraph. KEEP.

"Among the Alaska owned firms we could read... we found no published AI position
and no named tool" is about DOWL, CRW and PDC, not about R&M, and it is narrowed
in the next sentence to the pages we actually fetched, plus an admission that HDL
could not be read at all. The study NEVER says R&M publishes nothing on AI, which
was checked directly. The Michael Baker paragraph ends by cutting against us
rather than against them.

## FINDING 5. The disallowance question. KEEP, it is the strongest sentence here.

"Nothing published anywhere says R&M has ever had a funding disallowance, an audit
finding or a record dispute. We looked, we found no evidence of one, and we are not
hinting there is." Unprompted, unflattering to our own pitch, and true. This is
what the pass is supposed to produce more of.

---

## THE PATTERN, stated plainly

The agents did not shade this study. Every unflattering claim they wrote came
with its own limit attached, and the fact-checker's earlier drift finding had
already been corrected in claims.json before the rooms ran.

THE SHADING CAME FROM THE LENGTH GATE. Three trimming passes ran to get prose
from 3,723 words under 3,000, and the thing a trimmer removes first is the
qualifying clause. That is a mechanism, not an accident, and it will happen on
every run that overshoots its budget. It goes to the retro.

---

## ADDENDUM, after the Phase 6 fact-check

The pass above was written before the second fact-check ran, and that check found
the drift had MOVED rather than stopped. Recorded here because this artifact is
the home for this class of defect.

Its finding, in its own words: "Every rejection overstates motion and proximity."
Five spans, all leaning the same way.
- "just moved up a Zweig headcount bracket" and "opened a fourth office", both
  true in our research and NEITHER traceable to a source in the study. Rewritten
  against the Zweig facts that are cited, not patched with a new citation.
- "Michael Baker, with a principal office on C Street", which pulled the
  competitive threat into the prospect's own neighbourhood. Cut.
- "two aggregators we looked at were still listing a CEO who retired in 2019",
  uncheckable and sitting inside the section about restraint. Cut.
- "three weeks before we started", when the interval is 24 days. Made exact.
- "a certification you paid for in December", when what is published is an
  announcement. Corrected to announced.

THE PATTERN ACROSS BOTH CHECKS IS THE POINT. The morning check found the
tightening INSIDE the quotation marks. This one found the quotes clean and the
tightening migrated into the connective prose around them. Fixing the quotes did
not fix the habit, it relocated it, which is the same lesson the contract already
carries about fixing a claim rather than a sentence, one level up.

Note also that finding 1 above, the fairness sentence this pass RESTORED, is
where two of the five rejections landed. Restoring fairness introduced unsourced
facts. Both corrections were right and they pulled against each other, which is
worth knowing.



---

## Selection and the replacement queue

# Selection, 2026-08-07

Cold scouting. Inbound queue read clean (zero open scan-opt-in issues), so all four
lead-scouts ran, one per ICP segment.

23 page-verified candidates merged, zero hit the 29-domain EXCLUDE set, shortlist
gate cleared many times over.

## THE PICK

**R&M Consultants, Inc.** — rmconsult.com — Anchorage, Fairbanks, Juneau, Wasilla
Segment: other labor-scarce / paperwork-heavy. **fit_total 24**, the single highest
and unshared, so no tie-break was needed.

Scores: ai_solvable_pain 4, ability_to_pay 5, reachability 5, offer_fit 5,
alaska_signal 5.

Why it won. Employee-owned Alaska engineering and surveying firm, 100+ staff across
four offices, with nearly 95 percent of work for public clients, so permitting
narratives, agency submittals and SOQ/proposal production repeat constantly. It was
the only candidate scoring 5 on reachability, a named leader with a direct business
email printed on a page the scout fetched, which is the criterion that most often
sinks a strong lead at Phase 2. Confidence high across four fetched pages.

Noted for the room, not as a conclusion: CRW Engineering Group (crweng.com) was
contacted 2026-07-19 and is an Anchorage civil engineering peer. Different company,
no dedupe hit. The bar is that this study could not have been produced for CRW.

## REPLACEMENT QUEUE, in order

 2. Choggiung, Limited (choggiung.com) 23, ANC, Dillingham
 3. Gana-A'Yoo, Limited (ganaayoo.com) 23, ANC, Anchorage
 4. Capstone Clinic (capstoneclinic.com) 23, healthcare, Wasilla
 5. Chena Hot Springs Resort (chenahotsprings.com) 23, tourism, Fairbanks
 6. Huna Totem Corporation (hunatotem.com) 22, ANC, Juneau
 7. Shee Atika, Incorporated (sheeatika.com) 22, ANC, Sitka
 8. Orthopedic Physicians Alaska (opalaska.com) 22, healthcare (reachability flagged low)
 9. Solstice Alaska Consulting (solsticeak.com) 22, other, Anchorage
10. Alaska Seaplanes (flyalaskaseaplanes.com) 22, tourism, Juneau
11. Alaska Behavioral Health (alaskabehavioralhealth.org) 21
12. Advanced Physical Therapy of Alaska (aptak.com) 21
13. Major Marine Tours (majormarine.com) 21
14 through 23 in out/2026-08-07/shortlist.json.

## Reputation screening at this phase

The ANC scout ran the subsidiary screens this desk has been burned into using,
immigration-enforcement and detention contracting, and documented federal-contracting
fraud. All six ANC candidates it returned were screened and came back clean, with
what it checked recorded in why_fit. Sitnasuak carries a note that it is legally
independent of the already-suppressed Bering Straits Native Corporation.

Nothing was dropped for reputation in the other three segments.



---

## Shortlist, all 23 scored candidates

```json
[
 {
  "company": "R&M Consultants, Inc.",
  "domain": "rmconsult.com",
  "location": "Anchorage, Fairbanks, Juneau, Wasilla, Alaska",
  "why_fit": "Employee-owned Alaska engineering and surveying firm, 100+ staff, nearly 95% public-client work, so permitting narratives, agency submittals and SOQ/proposal production repeat constantly while 11 technical seats sit open across all four offices.",
  "scores": {
   "ai_solvable_pain": 4,
   "ability_to_pay": 5,
   "reachability": 5,
   "offer_fit": 5,
   "alaska_signal": 5
  },
  "fit_total": 24,
  "source_url": "https://www.rmconsult.com/join-us/open-positions/",
  "confidence": "high, four fetched pages, named leader Andrea Story CMAO with a direct business email on the open-positions page",
  "segment": "Other labor-scarce or paperwork-heavy Alaska SMBs"
 },
 {
  "company": "Choggiung, Limited",
  "domain": "choggiung.com",
  "location": "Dillingham, Alaska",
  "why_fit": "Largest Bristol Bay village corp, 2,700 shareholders, ~15 corporate staff carrying two SBA 8(a) firms under Wood River Federal plus the Bristol Inn, Bayside Diner, leasing and gravel. Screened Choggiung, Wood River Federal, Umyuaq and Intelligent Technology against ICE/ERO/CBP-detention and FCA/kickback/sham-8(a) and found none.",
  "scores": {
   "ai_solvable_pain": 5,
   "ability_to_pay": 4,
   "reachability": 4,
   "offer_fit": 5,
   "alaska_signal": 5
  },
  "fit_total": 23,
  "source_url": "https://www.choggiung.com/",
  "confidence": "high",
  "segment": "Alaska Native corporations and tribal enterprises"
 },
 {
  "company": "Gana-A'Yoo, Limited",
  "domain": "ganaayoo.com",
  "location": "Anchorage, Alaska (Galena, Koyukuk, Nulato, Kaltag)",
  "why_fit": "Nine subsidiaries across construction, facility services, remote camp and logistics, manufacturing and IT, all running ANC 8(a) and HUBZone certifications. Screened Khotol Services, Gana-A'Yoo Services Corp and Kaiyuh Information Technologies on both screens, nothing found.",
  "scores": {
   "ai_solvable_pain": 5,
   "ability_to_pay": 4,
   "reachability": 4,
   "offer_fit": 5,
   "alaska_signal": 5
  },
  "fit_total": 23,
  "source_url": "https://www.ganaayoo.com/contact/",
  "confidence": "high",
  "segment": "Alaska Native corporations and tribal enterprises"
 },
 {
  "company": "Capstone Clinic (Capstone Family Medicine)",
  "domain": "capstoneclinic.com",
  "location": "Wasilla, Palmer and Eagle River, Alaska, employer and occupational medicine reaching the North Slope",
  "why_fit": "Alaskan physician-owned multi-clinic primary care, urgent care, surgery, radiology and lab group whose occupational medicine line runs on employer paperwork, general business email published on its own contact and providers pages.",
  "scores": {
   "ai_solvable_pain": 5,
   "ability_to_pay": 4,
   "reachability": 4,
   "offer_fit": 5,
   "alaska_signal": 5
  },
  "fit_total": 23,
  "source_url": "https://capstoneclinic.com/providers/",
  "confidence": "high on existence, size and contact. info@capstoneclinic.com on two separately fetched pages. Co-founder Wade Erickson MD named. Three active clinics, not the pandemic-era seven.",
  "segment": "Independent healthcare and elder care"
 },
 {
  "company": "Chena Hot Springs Resort",
  "domain": "chenahotsprings.com",
  "location": "Chena Hot Springs Road, 60 miles east of Fairbanks, AK",
  "why_fit": "Year-round resort running front desk, reservations, an activity/tour desk and a heavy international aurora season, with public reviews documenting front-desk overload, understaffed dining and a phone line unreliable enough that they publish a backup number.",
  "scores": {
   "ai_solvable_pain": 5,
   "ability_to_pay": 4,
   "reachability": 4,
   "offer_fit": 5,
   "alaska_signal": 5
  },
  "fit_total": 23,
  "source_url": "https://www.chenahotsprings.com/contact-us/",
  "confidence": "high",
  "segment": "Tourism and visitor industry"
 },
 {
  "company": "Huna Totem Corporation",
  "domain": "hunatotem.com",
  "location": "Juneau and Hoonah, Alaska",
  "why_fit": "Village corp running four cruise destinations under a new 15-year Disney Cruise Line agreement signed July 22nd 2026, while HunaTek carries the 8(a) federal side. Screened HunaTek subsidiary lines on both screens, nothing found.",
  "scores": {
   "ai_solvable_pain": 4,
   "ability_to_pay": 5,
   "reachability": 4,
   "offer_fit": 4,
   "alaska_signal": 5
  },
  "fit_total": 22,
  "source_url": "https://hunatotem.com/",
  "confidence": "high",
  "segment": "Alaska Native corporations and tribal enterprises"
 },
 {
  "company": "Shee Atika, Incorporated",
  "domain": "sheeatika.com",
  "location": "Sitka, Alaska",
  "why_fit": "Urban ANC, ~3,400 shareholders, nine wholly owned government-contracting companies, eight separately 8(a) certified. Screened Shee Atika Government Services, Federal, Systems and American Marine and Technical Services on both screens, nothing found.",
  "scores": {
   "ai_solvable_pain": 5,
   "ability_to_pay": 4,
   "reachability": 3,
   "offer_fit": 5,
   "alaska_signal": 5
  },
  "fit_total": 22,
  "source_url": "https://sheeatika.com/who-we-are/staff/",
  "confidence": "high",
  "segment": "Alaska Native corporations and tribal enterprises"
 },
 {
  "company": "Orthopedic Physicians Alaska",
  "domain": "opalaska.com",
  "location": "Anchorage, Eagle River, Wasilla, Soldotna, Kodiak",
  "why_fit": "Independent 1966-founded orthopedic group, 11 facilities, 20+ physicians, an ASC, seven-day walk-in injury clinics, therapy, rheumatology and imaging. Referral, prior-auth and cross-site scheduling load at scale.",
  "scores": {
   "ai_solvable_pain": 5,
   "ability_to_pay": 5,
   "reachability": 2,
   "offer_fit": 5,
   "alaska_signal": 5
  },
  "fit_total": 22,
  "source_url": "https://opalaska.com/about-us/",
  "confidence": "high on scale and independence. LOW on reachability, CEO Rick Watson named but no email published anywhere.",
  "segment": "Independent healthcare and elder care"
 },
 {
  "company": "Solstice Alaska Consulting, Inc.",
  "domain": "solsticeak.com",
  "location": "Anchorage, Alaska",
  "why_fit": "~10-person Anchorage environmental planning shop whose entire product is documents, NEPA and permitting packages, public involvement records and grant writing.",
  "scores": {
   "ai_solvable_pain": 5,
   "ability_to_pay": 3,
   "reachability": 4,
   "offer_fit": 5,
   "alaska_signal": 5
  },
  "fit_total": 22,
  "source_url": "https://www.solsticeak.com/our-team",
  "confidence": "high on identity and contact; ability to pay is the honest weak spot",
  "segment": "Other labor-scarce or paperwork-heavy Alaska SMBs"
 },
 {
  "company": "Alaska Seaplanes",
  "domain": "flyalaskaseaplanes.com",
  "location": "Juneau, AK, serving Southeast Alaska communities",
  "why_fit": "Phone-first commuter, charter and tour operator whose own contact page runs reservations 6:00am to 6:30pm in summer and tells customers to call rather than use the form for time-sensitive matters, a stated message-handling gap on top of constant weather rebooking across three separate inboxes.",
  "scores": {
   "ai_solvable_pain": 5,
   "ability_to_pay": 4,
   "reachability": 3,
   "offer_fit": 5,
   "alaska_signal": 5
  },
  "fit_total": 22,
  "source_url": "https://www.flyalaskaseaplanes.com/contact-us/",
  "confidence": "high",
  "segment": "Tourism and visitor industry"
 },
 {
  "company": "Alaska Behavioral Health",
  "domain": "alaskabehavioralhealth.org",
  "location": "Anchorage, Fairbanks, Wasilla",
  "why_fit": "Self-described largest community behavioral health center in the state, four Fairbanks clinics plus a Cohen Military Family Clinic and a mobile crisis team.",
  "scores": {
   "ai_solvable_pain": 5,
   "ability_to_pay": 4,
   "reachability": 3,
   "offer_fit": 4,
   "alaska_signal": 5
  },
  "fit_total": 21,
  "source_url": "https://alaskabehavioralhealth.org/employment/work-with-us/",
  "confidence": "medium. /about/ returned 403. Only published address is an HR inbox on a second domain. Offer fit marked down, behavioral health notes are the most privacy-loaded documents in the segment.",
  "segment": "Independent healthcare and elder care"
 },
 {
  "company": "Advanced Physical Therapy of Alaska",
  "domain": "aptak.com",
  "location": "Anchorage, Wasilla, Fairbanks, Soldotna, Seward",
  "why_fit": "Employee-owned five-clinic PT practice that publishes paid documentation time as a recruiting benefit and has carried three pelvic health vacancies with sign-on bonuses since April 2026.",
  "scores": {
   "ai_solvable_pain": 5,
   "ability_to_pay": 4,
   "reachability": 3,
   "offer_fit": 4,
   "alaska_signal": 5
  },
  "fit_total": 21,
  "source_url": "https://aptak.com/career/",
  "confidence": "high on the hiring pain. MEDIUM-LOW on contact, the widely repeated info@aptak.com was NOT on the fetched contact page and must not be used without verification.",
  "segment": "Independent healthcare and elder care"
 },
 {
  "company": "Major Marine Tours",
  "domain": "majormarine.com",
  "location": "Seward, AK (Kenai Fjords)",
  "why_fit": "Locally owned day-cruise operator of 30-plus years with multiple vessels, a named owner-president on its own company page and a published business email, running a four-month booking crush and a September staff cliff.",
  "scores": {
   "ai_solvable_pain": 4,
   "ability_to_pay": 4,
   "reachability": 4,
   "offer_fit": 4,
   "alaska_signal": 5
  },
  "fit_total": 21,
  "source_url": "https://majormarine.com/our-company/",
  "confidence": "high",
  "segment": "Tourism and visitor industry"
 },
 {
  "company": "Sitnasuak Native Corporation",
  "domain": "snc.org",
  "location": "Nome and Anchorage, Alaska",
  "why_fit": "Largest village corp in the Bering Straits region, 15 active subsidiaries across fuel, retail, tactical apparel, title and escrow, properties. Legally independent of Bering Straits Native Corporation and carries none of that corporation's ICE work. Screens clean.",
  "scores": {
   "ai_solvable_pain": 4,
   "ability_to_pay": 4,
   "reachability": 3,
   "offer_fit": 4,
   "alaska_signal": 5
  },
  "fit_total": 20,
  "source_url": "https://www.snc.org/contact/",
  "confidence": "medium",
  "segment": "Alaska Native corporations and tribal enterprises"
 },
 {
  "company": "Alaska Sleep Clinic (Alyeska International, Inc.)",
  "domain": "alaskasleep.com",
  "location": "Anchorage, Fairbanks, Soldotna, Wasilla",
  "why_fit": "Independent veteran-owned diagnostic sleep testing group, four AASM-accredited labs plus its own DME arm, economics run on prior authorization and CPAP compliance reporting.",
  "scores": {
   "ai_solvable_pain": 5,
   "ability_to_pay": 4,
   "reachability": 2,
   "offer_fit": 5,
   "alaska_signal": 4
  },
  "fit_total": 20,
  "source_url": "https://www.alaskasleep.com/about/",
  "confidence": "LOW on reachability, no email published, /contact-us/ 404s. Sub-sector caveat, sleep/CPAP DME is a repeat FCA category nationally, nothing adverse found on this company.",
  "segment": "Independent healthcare and elder care"
 },
 {
  "company": "Imaging Associates of Alaska",
  "domain": "imagingak.com",
  "location": "Anchorage, Eagle River, Palmer",
  "why_fit": "Three outpatient imaging centers managed by the largest independent radiology group in the state, their own patient pages say they obtain preauthorization on the patient's behalf.",
  "scores": {
   "ai_solvable_pain": 5,
   "ability_to_pay": 4,
   "reachability": 2,
   "offer_fit": 5,
   "alaska_signal": 4
  },
  "fit_total": 20,
  "source_url": "https://www.imagingak.com/contact-us/",
  "confidence": "LOW on reachability, five phone and fax lines, zero emails, zero names. The preauthorization line is UNVERIFIED, its page 404d on fetch.",
  "segment": "Independent healthcare and elder care"
 },
 {
  "company": "UNIT Company",
  "domain": "unitcompany.com",
  "location": "Anchorage, Alaska, projects statewide",
  "why_fit": "100% Alaskan-owned general contractor, 45 years, 450+ projects, hiring QC Systems Manager and Project Engineer now, submittal and closeout load peaking before freeze-up.",
  "scores": {
   "ai_solvable_pain": 4,
   "ability_to_pay": 4,
   "reachability": 3,
   "offer_fit": 4,
   "alaska_signal": 5
  },
  "fit_total": 20,
  "source_url": "https://unitcompany.com/careers",
  "confidence": "medium-high, no named decision-maker verified, team page 404s",
  "segment": "Other labor-scarce or paperwork-heavy Alaska SMBs"
 },
 {
  "company": "Alcan Electrical & Engineering",
  "domain": "alcanelectric.com",
  "location": "Anchorage HQ plus Fairbanks, Juneau, Wasilla",
  "why_fit": "Alaskan-owned since 1971, 200+ employees across four offices, bid takeoffs, submittals, RFIs and multi-site closeout paperwork scale with a union labor pool they can't grow.",
  "scores": {
   "ai_solvable_pain": 4,
   "ability_to_pay": 5,
   "reachability": 2,
   "offer_fit": 4,
   "alaska_signal": 5
  },
  "fit_total": 20,
  "source_url": "https://www.alcanelectric.com/about/",
  "confidence": "medium, LOW on reachability, no email and no named leader found",
  "segment": "Other labor-scarce or paperwork-heavy Alaska SMBs"
 },
 {
  "company": "Northern Alaska Tour Company",
  "domain": "northernalaska.com",
  "location": "Fairbanks, AK, to the Arctic Circle, Prudhoe Bay and Utqiagvik",
  "why_fit": "Alaskan-owned since 1987, multi-day Dalton Highway and aurora logistics with summer phone hours 7am to 10pm daily, a published business email, and a separate recruiting site signalling a hard seasonal hiring load.",
  "scores": {
   "ai_solvable_pain": 4,
   "ability_to_pay": 3,
   "reachability": 4,
   "offer_fit": 4,
   "alaska_signal": 5
  },
  "fit_total": 20,
  "source_url": "https://www.northernalaska.com/about-us/",
  "confidence": "high",
  "segment": "Tourism and visitor industry"
 },
 {
  "company": "The Kuskokwim Corporation",
  "domain": "kuskokwim.com",
  "location": "Anchorage, Alaska",
  "why_fit": "ANCSA corp merging 10 village corporations, ~17 subsidiaries, ~400 employees in aviation, construction, environmental restoration and facility outfitting with 8(a) sole-source pursuit as the growth engine. Screens clean.",
  "scores": {
   "ai_solvable_pain": 4,
   "ability_to_pay": 4,
   "reachability": 2,
   "offer_fit": 4,
   "alaska_signal": 5
  },
  "fit_total": 19,
  "source_url": "https://business.anchoragechamber.org/list/member/the-kuskokwim-corporation-7008",
  "confidence": "medium, their own site renders client-side and returned no content",
  "segment": "Alaska Native corporations and tribal enterprises"
 },
 {
  "company": "TEMSCO Helicopters, Inc.",
  "domain": "temscoair.com",
  "location": "Ketchikan HQ, bases in Juneau, Skagway, Denali",
  "why_fit": "Four bases each publishing its own reservations or dispatch email, cruise-day tour volume plus utility flying, and weather-driven rescheduling. Reputation screen clean.",
  "scores": {
   "ai_solvable_pain": 4,
   "ability_to_pay": 4,
   "reachability": 3,
   "offer_fit": 4,
   "alaska_signal": 4
  },
  "fit_total": 19,
  "source_url": "https://temscoair.com/about/",
  "confidence": "medium, no named decision-maker, ownership above the operating company unclear",
  "segment": "Tourism and visitor industry"
 },
 {
  "company": "Alaska Logistics Services",
  "domain": "alaskalogistics.net",
  "location": "Anchorage, Seward, Juneau, Tacoma",
  "why_fit": "Barge and marine freight to Bethel, Nome, Dillingham, Naknek and village runs, quoting and cargo-status traffic spikes as sailing windows close.",
  "scores": {
   "ai_solvable_pain": 4,
   "ability_to_pay": 4,
   "reachability": 2,
   "offer_fit": 4,
   "alaska_signal": 4
  },
  "fit_total": 18,
  "source_url": "https://www.alaskalogistics.net/contact",
  "confidence": "medium, LOW on reachability and ownership, Tacoma office sits Outside",
  "segment": "Other labor-scarce or paperwork-heavy Alaska SMBs"
 },
 {
  "company": "Everts Air",
  "domain": "evertsair.com",
  "location": "Alaska, 13 hubs statewide",
  "why_fit": "Alaska freight and passenger carrier, continuous maintenance and ops hiring, dispatch, charter quoting and maintenance recordkeeping are document-heavy.",
  "scores": {
   "ai_solvable_pain": 4,
   "ability_to_pay": 4,
   "reachability": 2,
   "offer_fit": 3,
   "alaska_signal": 5
  },
  "fit_total": 18,
  "source_url": "https://evertsair.com/careers",
  "confidence": "medium-low, only a recruitment address, scale unverified",
  "segment": "Other labor-scarce or paperwork-heavy Alaska SMBs"
 }
]
```


---

## Verified claims, the only citable facts

```json
{
 "company": "R&M Consultants, Inc.",
 "domain": "rmconsult.com",
 "as_of": "2026-08-07",
 "fact_checker_verdict": "fix, applied. Every rejected quotation below has been corrected to what the page actually says, every over-scoped negative narrowed to what was fetched, and every unverified claim removed rather than softened.",
 "drift_pattern_to_watch": "The fact-checker found two directional patterns and BOTH flatter the pitch. FIRST, EVERY MISQUOTE TIGHTENED THE SOURCE into better prose while leaving the quotation marks on. SECOND, EVIDENCE WAS UPGRADED A HALF-STEP AT EVERY JOINT: a preprint became peer-reviewed, a ranking-share statistic became a severity level, a scoped productivity figure lost its scope, a negative confirmed on two pages became a negative about a whole site. Nothing downstream may re-tighten a quote or re-upgrade a source. Quote long and exact or do not quote.",
 "contact": {
  "name": "Len Story, PLS",
  "role": "Chief Executive Officer",
  "role_warning": "ADDRESS HIM AS CHIEF EXECUTIVE OFFICER AND NOTHING MORE. The 'Board President' string is NOT on the cited page and was rejected. Do not use it anywhere.",
  "email": "lstory@rmconsult.com",
  "contact_source": "https://www.rmconsult.com/our-people/len-story/",
  "contact_ok": true,
  "verification": "Re-fetched by the fact-checker. lstory@rmconsult.com renders as a live mailto on R&M's own domain, and the page reads 'to his current position as Chief Executive Officer' in the present tense. Corroborated by the Zweig 2026 article, which separately titles him 'PLS, R&M's Chief Executive Officer'. Third-party aggregators still list a CEO who retired in 2019; none were used.",
  "buyer_or_router": "BUYER"
 },
 "about_them": [
  {
   "claim": "Nearly 95% of our work is for public clients",
   "verbatim": true,
   "url": "https://www.rmconsult.com/who-we-are/"
  },
  {
   "claim": "Founded in 1969, R&M is an Alaska-based, employee-owned professional services consulting firm",
   "verbatim": true,
   "url": "https://www.rmconsult.com/who-we-are/"
  },
  {
   "claim": "The Who We Are page carries a '100+ Employees' figure and 'Founded 1969'. NO precise headcount is published anywhere. Zweig placed the firm in the 100-199 bracket for 2026 and in the 50-99 bracket for 2023.",
   "verbatim": false,
   "url": "https://www.rmconsult.com/who-we-are/"
  },
  {
   "claim": "Eleven positions are open at once across four offices: Land Surveyor; Project Civil Engineer - Construction Administration; Project Civil Engineer - Surface Transportation; Project Civil Engineer - Utilities; Project Geotechnical Engineer; Senior Environmental Geologist or Engineer; Senior Land Surveyor; Senior Project Civil Engineer - Surface Transportation; Senior Project Civil Engineer - Utilities; Staff Civil Engineer - Water Resources; Staff Surveyor. NO POSTING DATES ARE SHOWN, so how long any role has been open is genuinely unknowable from outside.",
   "verbatim": false,
   "url": "https://www.rmconsult.com/join-us/open-positions/"
  },
  {
   "claim": "Conduct research and write technical portions of proposals to assist in bringing in new work.",
   "verbatim": true,
   "url": "https://www.rmconsult.com/job-posting/senior-land-surveyor/",
   "note": "THE LOAD-BEARING QUOTE OF THE STUDY. This exact bullet appears on the Senior Land Surveyor posting (Geomatics) AND the Senior Project Civil Engineer posting (Engineering). Two departments, same duty. Quote it in full. The shortened form 'technical proposal portions' was REJECTED as a misquote."
  },
  {
   "claim": "Conduct research and write technical portions of proposals to assist in bringing in new work.",
   "verbatim": true,
   "url": "https://www.rmconsult.com/job-posting/senior-project-engineer/",
   "note": "Second department. Actual posting title is 'Senior Project Civil Engineer - Surface Transportation'."
  },
  {
   "claim": "Developing proposals.",
   "verbatim": true,
   "url": "https://www.rmconsult.com/job-posting/senior-environmental-geologist-or-engineer/",
   "note": "A third senior seat, alongside 'Producing cost estimates.' and 'Writing technical reports and analyzing data.'"
  },
  {
   "claim": "Review designs, plan drawings, engineering reports and other contract deliverables for feasibility, technical accuracy and quality.",
   "verbatim": true,
   "url": "https://www.rmconsult.com/job-posting/senior-project-engineer/"
  },
  {
   "claim": "15 or more years of experience in civil design work, with emphasis in highway and street design",
   "verbatim": true,
   "url": "https://www.rmconsult.com/job-posting/senior-project-engineer/",
   "note": "CORRECTED. The tighter resume-style paraphrase was rejected."
  },
  {
   "claim": "Administer project documentation and audit trails to ensure funding participation",
   "verbatim": true,
   "url": "https://www.rmconsult.com/job-posting/project-engineer-construction-administration/"
  },
  {
   "claim": "Travel within Alaska will be required, and the ideal candidate must be willing to work in project locations throughout the state for extended periods of time during construction season.",
   "verbatim": true,
   "url": "https://www.rmconsult.com/job-posting/project-engineer-construction-administration/",
   "note": "This posting is classified 'Seasonal, Full-Time, Hourly'."
  },
  {
   "claim": "R&M achieved CMMC Level 2 certification, announced December 22nd 2025, with Stratus Services. 'CMMC Level 2 includes 110 controls based on NIST Special Publication 800-171 Revision 2'",
   "verbatim": true,
   "url": "https://www.rmconsult.com/news-and-views/rm-achieves-cmmc-level-2-certification-with-guidance-from-stratus-services/"
  },
  {
   "claim": "The certification positions R&M to continue delivering high-quality infrastructure solutions for clients such as the U.S. Army Corps of Engineers and other federal agencies under the purview of the Department of Defense, while ensuring their systems, data and client information remain secure.",
   "verbatim": true,
   "url": "https://www.rmconsult.com/news-and-views/rm-achieves-cmmc-level-2-certification-with-guidance-from-stratus-services/",
   "note": "CORRECTED. Three separate rewrites of this sentence were rejected. Use it whole or not at all."
  },
  {
   "claim": "Cybersecurity is essential to the work we do, especially when supporting federal clients. With Stratus' expertise, we were able to implement the required controls and confirm that we're doing the right things to keep our data secure.",
   "verbatim": true,
   "url": "https://www.rmconsult.com/news-and-views/rm-achieves-cmmc-level-2-certification-with-guidance-from-stratus-services/",
   "note": "Jere Fisher, Group Manager of IT. Contiguous."
  },
  {
   "claim": "The biggest challenge is time. If your in-house team lacks the required expertise, bring in outside support to get you started.",
   "verbatim": true,
   "url": "https://www.rmconsult.com/news-and-views/rm-prepares-for-federal-cybersecurity-standards-with-cmmc-compliance/",
   "note": "Jere Fisher, Group Manager of IT. Contiguous."
  },
  {
   "claim": "The process can feel overwhelming, but it ultimately strengthens a firm's security posture and ensures we can continue supporting DoD projects while safeguarding critical information.",
   "verbatim": true,
   "url": "https://www.rmconsult.com/news-and-views/rm-prepares-for-federal-cybersecurity-standards-with-cmmc-compliance/",
   "note": "Jere Fisher, Group Manager of IT. Contiguous."
  },
  {
   "claim": "On July 14th 2026 R&M announced Siobhan Johansen hired as Proposal Manager into the Marketing Group and Carly Guthrie as Human Resources Generalist into Business Services.",
   "verbatim": false,
   "url": "https://www.rmconsult.com/news-and-views/new-marketing-and-human-resources-professionals-join-rms-business-services-department/"
  },
  {
   "claim": "She specializes in marketing and strategic planning, market research, communications and proposal development.",
   "verbatim": true,
   "url": "https://www.rmconsult.com/our-people/andrea-story/",
   "note": "Andrea Story, FSMPS, CPSM, Chief Marketing & Administrative Officer. CORRECTED, the compressed 'marketing strategy' version was rejected. She became Alaska's first Certified Professional Services Marketer in 2001, Fellow in 2021, 29 years of industry experience."
  },
  {
   "claim": "Zweig Group 2026 Best Firms To Work For: #10 in the 100-199 Employees category, #11 in the Civil Engineering category, marking R&M's 15th consecutive year on the list.",
   "verbatim": false,
   "url": "https://www.rmconsult.com/news-and-views/rm-named-one-of-zweig-groups-2026-best-firms-to-work-for/",
   "note": "The article separately titles Len Story 'PLS, R&M's Chief Executive Officer', which is the currency corroboration for the contact."
  },
  {
   "claim": "The What We Do page lists 24 service lines: Airports, Construction Administration, Contaminated Sites, Geology, Geotechnical, GIS, Grant Writing, Hydrographic, Hydrology, Land Development, Land Surveying, Materials Testing, NEPA, Parks & Trails, Permitting, Planning, Public Involvement, Remote Sensing, Right of Way, Site Development, Special Inspections, Surface Transportation, Utilities, Waterfront.",
   "verbatim": false,
   "url": "https://www.rmconsult.com/what-we-do/"
  },
  {
   "claim": "NARROWED NEGATIVE, and it must be stated at exactly this scope. The words artificial intelligence, AI, machine learning, automation and automated appear nowhere on R&M's What We Do page, nor on the twelve items shown on page one of their news index. The news index is PAGINATED, so this is NOT a claim about the whole site and must never be written as one.",
   "verbatim": false,
   "url": "https://www.rmconsult.com/what-we-do/",
   "note": "Second page checked: https://www.rmconsult.com/news-and-views/category/news/ . The fact-checker rejected the whole-site version specifically because a single older post would make the study wrong in a way the recipient discovers first."
  },
  {
   "claim": "email@rmconsult.com is rendered on the Who We Are page. astory@rmconsult.com, jobs@rmconsult.com and email@rmconsult.com are all rendered on the open-positions page.",
   "verbatim": false,
   "url": "https://www.rmconsult.com/who-we-are/"
  }
 ],
 "competitors": [
  {
   "claim": "Titan brings together the world's leading frontier models in a single secure interface, strengthening AI-enhanced service delivery through unprecedented access to knowledge for more than 6,000 engineers, architects and scientists.",
   "verbatim": true,
   "url": "https://www.prnewswire.com/news-releases/michael-baker-international-unveils-titan-an-enterprise-ai-platform-powering-a-new-way-of-working-302745052.html",
   "note": "Michael Baker International, announced April 16th 2026. Michael Baker has a principal office at 3900 C St in Anchorage and bids the same agency work."
  },
  {
   "claim": "a no-code/low-code agent builder that allows any Michael Baker expert to create purpose-built AI agents tailored to their discipline and then publish those agents to an internal library accessible across the enterprise",
   "verbatim": true,
   "url": "https://www.prnewswire.com/news-releases/michael-baker-international-unveils-titan-an-enterprise-ai-platform-powering-a-new-way-of-working-302745052.html"
  },
  {
   "claim": "an enterprise operating layer, providing unified, secure access to the world's most advanced large language models",
   "verbatim": true,
   "url": "https://www.prnewswire.com/news-releases/michael-baker-international-unveils-titan-an-enterprise-ai-platform-powering-a-new-way-of-working-302745052.html",
   "note": "Reach also stated as 'more than 120 office locations'."
  },
  {
   "claim": "DROPPED AND MAY NOT BE USED. The claim that Michael Baker's Titan carries 'a program manager's proposal analysis tool accessible to every capture team in the firm' came from a blog page that returned HTTP 503 on four separate attempts across two agents. The press release, which DID load, does not mention proposals, pursuits or capture teams at all. The showrunner confirmed this absence directly. NOTHING downstream may claim Michael Baker has aimed AI at proposal or pursuit work.",
   "verbatim": false,
   "url": null
  },
  {
   "claim": "Prohibit the use of generative AI for use in any final work product",
   "verbatim": true,
   "url": "https://www.hdrinc.com/artificial-intelligence-informational-statement",
   "note": "HDR, which has an Anchorage office. HDR states it uses AI 'in support of our internal operations and in the service of our clients and communities', names six principles (Accountability, Transparency, Privacy, Fairness, Responsibility, Sustainability), states 'Clients always retain ownership of their data', and names a 'Generative Artificial Intelligence Usage Policy'. NO named tool, NO named project, NO measured result on that page."
  },
  {
   "claim": "Big data, machine learning, and AI all have nearly limitless untapped potential to change the way we live and work",
   "verbatim": true,
   "url": "https://www.dowl.com/news/our-geobusiness-future-big-data-machine-learning-and-ai/",
   "note": "DOWL, July 16th 2020, by Brad Melocik and Teresa Patterson, from a Geoprofessional Business Association workshop. The source sentence continues ', and the emergence of these concepts is being hailed as the Fourth Industrial Revolution.' The article makes NO claim that DOWL deploys any of it."
  },
  {
   "claim": "NARROWED NEGATIVE. The ten news items on page one of DOWL's news index, spanning April 15th 2024 to February 4th 2026, contain no mention of AI, machine learning or automation. The index is paginated 1 through 5, so this is page one, NOT the site. DOWL's homepage was not fetched and no claim is made about it.",
   "verbatim": false,
   "url": "https://www.dowl.com/company/news/"
  },
  {
   "claim": "NARROWED NEGATIVE. CRW Engineering Group's homepage contains no occurrence of artificial intelligence, AI, machine learning, automation or automated. The single technology string is a PROJECT TITLE on that homepage, 'Whittier City Park Master Plan, Unmanned Aerial Vehicle (UAV) 3D Modeling'. Nothing on the page says it was used for surveying, so do not say so.",
   "verbatim": false,
   "url": "https://www.crweng.com/"
  },
  {
   "claim": "UNASSESSED, NOT CLEAN. HDL Engineering Consultants of Anchorage, Palmer and Kenai is a genuine head-to-head Alaska competitor whose site returned an empty body on three fetch attempts. Any sentence about 'no Alaska firm' must account for this or be scoped to the firms actually checked: DOWL, CRW and PDC/RESPEC.",
   "verbatim": false,
   "url": null
  },
  {
   "claim": "PDC Engineers was acquired by RESPEC on May 8th 2020. RESPEC's Data & Technology expertise page names Software Services, Strategy & Advisory, Staffing, and Data Insight & Innovation, covering data engineering, analytics, modeling, geospatial systems, SCADA and IoT, with no mention of artificial intelligence or machine learning on that page.",
   "verbatim": false,
   "url": "https://www.respec.com/expertise/data-technology/"
  }
 ],
 "industry": [
  {
   "claim": "Inspectors using HeadLight experienced a 28 percent increase in productivity when creating and submitting daily work reports (DWRs).",
   "verbatim": true,
   "url": "https://rosap.ntl.bts.gov/view/dot/56247",
   "tier": "INDEPENDENT",
   "note": "THE FULL SENTENCE IS MANDATORY. Louisiana DOTD / LTRC, FHWA co-sponsored, Rupnow Coco White Yamaura 2020, 50+ construction projects. Quoting the prefix alone was REJECTED because it drops the clause that bounds the number. Also verbatim: 'Inspectors collected and shared 1.9 times more observations while increasing the number of photo and other media observations'; 'The increase in productivity for Department-wide adoption is estimated to exceed 117,000 hours per year'; 'submission rate improvements up to 66 percent completed within 24 hours and up to 82 percent completed within 72 hours.' NOTE: the winning system is workflow and capture automation with light ML, NOT a large language model."
  },
  {
   "claim": "coding agents could save 1-5 hours per subsection, up to roughly a 15% reduction in drafting time",
   "verbatim": true,
   "url": "https://www.gend.co/blog/draftnepabench-ai-federal-permitting",
   "tier": "BENCHMARK WITH EXPERT EVALUATION",
   "note": "DraftNEPABench, a national-lab benchmark assessed by '19 subject matter experts familiar with NEPA review' across tasks from 18 federal agencies. A MODEL VENDOR IS A CO-AUTHOR, so 15% is a CEILING under favourable conditions. The authors' own caveat is verbatim: 'if references are incomplete or out of date, models may not reliably identify those discrepancies unless explicitly instructed'."
  },
  {
   "claim": "RAG-based approaches substantially outperform PDF document contexts",
   "verbatim": true,
   "url": "http://arxiv.org/abs/2407.07321v3",
   "tier": "PREPRINT, NOT PEER-REVIEWED",
   "note": "CORRECTED. Calling this peer-reviewed was REJECTED, arXiv is a preprint server. NEPAQuAD/MAPLE, PNNL with Iowa State, submitted July 10th 2024, revised June 12th 2025, five frontier LLMs. Models 'consistently achieve their highest performance when provided with the gold passage as context'. No absolute accuracy percentage in the abstract. THE VISIBLE PAGE MAY NOT SAY 'RAG', that word is banned by FIELD_STUDY_SPEC. Say what it means in plain words."
  },
  {
   "claim": "INDOT with Purdue, Sensors, April 22nd 2023, 3,549 images (2,350 cracked, 1,199 non-cracked). Crack detection 'average classification accuracy was approximately 0.94'. Sealed-crack detection approximately 0.93. Crack-type classification approximately 0.84. But 'the average IoU was approximately 0.61' and 'average crack pixel detection recall and precision were 0.68 and 0.35, respectively'.",
   "verbatim": true,
   "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10181228/",
   "tier": "INDEPENDENT PEER-REVIEWED",
   "note": "CORRECTED. Two sub-figures (0.93 precision, 0.94 recall at the detection step) were NOT confirmed and have been dropped. The argument does not need them. The authors recommend manual-AI collaboration rather than full automation. This is the cleanest published proof in the industry that coarse detection works and fine measurement does not."
  },
  {
   "claim": "The civil engineer must maintain responsibility for project planning, designing, building, operations, maintenance, and the protection of the public health, safety, and welfare",
   "verbatim": true,
   "url": "https://www.asce.org/advocacy/policy-statements/ps573---artificial-intelligence-and-engineering-responsibility",
   "tier": "AUTHORITATIVE",
   "note": "ASCE Policy Statement 573, adopted July 18th 2024. Also verbatim: 'AI cannot serve as a replacement for the professional judgement of a licensed Professional Engineer' and 'AI cannot be held accountable, nor can it replace the training, experience, and judgement of a professional engineer.' WARNING: these quotes contain the word 'cannot'. They are QUOTED SOURCE TEXT. Do not paraphrase them into our own voice, and do not let our own prose use that word."
  },
  {
   "claim": "With 80% of insurers viewing AI adoption by design firms as a potential disruptor, Maxwell noted that its use must be supported by disciplined controls, transparency and accountability.",
   "verbatim": true,
   "url": "https://www.insurancebusinessmag.com/us/news/construction/most-aande-liability-insurers-plan-rate-hikes-in-2026--ames-and-gough-566403.aspx",
   "tier": "AUTHORITATIVE",
   "note": "Ames & Gough 2026 survey of 15 leading A&E professional liability insurers. Also verified: '73% are planning modest rate increases, largely in the single-digit range' and '60% reported higher claim severity in 2025, up from 53% the prior year and 41% in 2023'."
  },
  {
   "claim": "CORRECTED AND HANDLE WITH CARE. The Ames & Gough discipline figures are SHARES OF INSURERS NAMING a discipline as highest-severity, NOT severity levels and NOT claim rates. The source says '80% of respondents ranking structural engineering as the highest-severity discipline, followed by civil engineering at 73% and architecture at 60%.' Writing '73% claim severity in civil engineering' was REJECTED as a metric error that drifts toward alarm, and civil engineering is R&M's own discipline, so it is the number most likely to be quoted back at us.",
   "verbatim": false,
   "url": "https://www.insurancebusinessmag.com/us/news/construction/most-aande-liability-insurers-plan-rate-hikes-in-2026--ames-and-gough-566403.aspx",
   "tier": "AUTHORITATIVE"
  },
  {
   "claim": "ISO/Verisk released three OPTIONAL generative-AI exclusion endorsements effective January 2026 for commercial general liability: CG 40 47 (Coverage A and B), CG 40 48 (Coverage B only) and CG 35 08 (products/completed operations). Each carrier chooses whether to attach them. Definition verbatim: 'a machine-based learning system or model that is trained on data with the ability to create content or responses, including but not limited to text, images, audio, video or code.'",
   "verbatim": false,
   "url": "https://www.independentagent.com/vu_resource/verisk-to-roll-out-new-general-liability-exclusions-for-generative-ai-exposures/",
   "tier": "AUTHORITATIVE",
   "note": "CORRECTED. The quoted form TITLE for CG 40 47 was not confirmed, so do not put quotation marks around a form title. The word OPTIONAL is load-bearing and must survive into the study."
  },
  {
   "claim": "UNVERIFIED BY THIS DESK, DO NOT CITE AS CHECKED. The fact-checker could not reach, within its priority list: the GovTech Honolulu CivCheck piece, the GovTech Massachusetts GrantWell piece, both PNNL releases, the Microsoft Kimley-Horn and WSP case studies, Carahsoft/Bentley, Bluebeam, BST Global, ACEC, AASHTO, natlawreview, permitting.innovation.gov, the Nature citation-integrity piece and rfpm.ai. Their content sits in research.json for the room's understanding, but NONE of it may appear as a cited fact in the study.",
   "verbatim": false,
   "url": null
  },
  {
   "claim": "THE INDUSTRY'S OWN EVIDENCE GAP, and it is the most important calibration in this package. The industry-analyst worked vendor case-study pages, comparison sites, SMPS and ACEC channels and the trade press, and found NO named firm of any size attached to a measured proposal-productivity number with a stated method. Proposal and SF330 automation is the LOUDEST MARKETED pocket in this industry and the THINNEST MEASURED one. Every circulating figure (20% faster, 60% less duplicate content, 75% time savings, 44% win rates) is vendor-published and mostly anonymised. Where the measured evidence actually is: field documentation, and cited human-approved drafting.",
   "verbatim": false,
   "url": null,
   "tier": "ANALYST FINDING, stated as such, not as a cited number"
  }
 ],
 "what_we_could_not_verify": [
  "Any revenue figure for R&M. No page carried one, rocketreach returned 403, and R&M did not appear in the fetched Alaska Business Top 49ers list. NO revenue number may appear anywhere.",
  "A precise headcount. The firm says 100+ and Zweig places it in the 100-199 bracket. No exact number exists publicly.",
  "How long any of the eleven roles has been open. No posting dates are published. The stale-posting argument is NOT available.",
  "Any proposal volume, win rate, pursuit count, or hours spent on proposals at R&M. Nothing of the kind is published. Every driver of that shape is an ASSUMPTION and must be labelled one.",
  "Whether R&M uses AI internally today. The narrowed negative covers two published pages only. A firm can run AI internally and publish nothing, which is common in this sector.",
  "Michael Baker's Titan blog, HTTP 503 on four attempts across two agents. The proposal and capture-team claim is dropped entirely.",
  "HDL Engineering Consultants, empty body on three attempts. Unassessed, not clean.",
  "Employee sentiment. Glassdoor returned 403 and Indeed carries only 7 reviews at 4.4 out of 5, so the two negative review quotes are a weak minority signal and MUST NOT be characterised as a pattern or used at all.",
  "Any State of Alaska policy on consultant AI use in submittals. None was located. Alaska HB 306's final status could not be verified because legiscan returned 403, so no claim about its passage may be made.",
  "That any federal solicitation requires AI-use disclosure in an A/E proposal. NO blanket rule was found. Do not imply one exists."
 ]
}
```


---

## Research room

```json
{
 "company": {
  "agent": "company-analyst",
  "what_they_do": "R&M Consultants, Inc. is a multi-discipline Alaska engineering and professional services consulting firm specializing in cold region design. Its own site states: \"Founded in 1969, R&M is an Alaska-based, employee-owned professional services consulting firm\" and that it \"specializes in cold region design and has devoted our practice to becoming experts in the environmental and logistical challenges that influence designs in Alaska\" (https://www.rmconsult.com/who-we-are/). The What We Do page lists 24 service lines verbatim: Airports, Construction Administration, Contaminated Sites, Geology, Geotechnical, GIS, Grant Writing, Hydrographic, Hydrology, Land Development, Land Surveying, Materials Testing, NEPA, Parks & Trails, Permitting, Planning, Public Involvement, Remote Sensing, Right of Way, Site Development, Special Inspections, Surface Transportation, Utilities, Waterfront (https://www.rmconsult.com/what-we-do/). Internally the work is organized into departments named in job postings and the staff directory: Engineering, Earth Sciences, Geomatics, Construction Services, Planning, and Business Services. Concrete work includes design of Stage 1B of the Alaska DOT&PF Sterling Highway MP 45-60 project, described as \"reconstruction of approximately two miles of the Sterling Highway\"; an AASHTO-accredited and USACE-certified materials laboratory operating \"since 1970\"; remote sensing using \"terrestrial equipment, Unmanned Aerial Systems (UAS), airplanes, helicopters and boats\" to collect imagery, LiDAR and sonar; grant writing broken into \"Grant Research,\" \"Strategy Development,\" \"Narrative Drafting,\" \"Technical Review,\" \"Graphic Design,\" and \"Project Management,\" including an application that produced a $20 million RAISE award for Haines; and public involvement work whose deliverables include \"Community survey design, administration and analysis\" and \"Printed and digital communication collateral that brand projects through identifiable logos, postcards, newsletters, e-newsletters, project website development\".",
  "size": "FACT: The company describes itself as a \"100+ person multi-discipline firm\" and its Who We Are page carries a \"100+ Employees\" figure alongside \"Founded 1969\". The AEDC member listing repeats \"a 100+ person, entirely Alaska-based, employee-owned professional services consulting firm\". FACT: Zweig Group placed R&M in the \"100-199 Employees\" category for its 2026 Best Firms To Work For award, at #10, and #11 in Civil Engineering, its \"15th consecutive year\" on the list. FACT: For the 2023 award the firm was ranked in the 50-99 employee bracket, \"#11 for firms with 50-99 employees and #18 in the civil engineering category\". INFERENCE: the move from the 50-99 bracket to the 100-199 bracket between the 2023 and 2026 Zweig lists indicates real headcount growth over roughly three years. FACT: \"30 Employee Owners\" is stated on the benefits page. FACT: LinkedIn shows the company size band as 51-200 employees. THIN SPOT: the staff directory lists individual staff with photos but states no total; page-reading estimates were inconsistent (roughly 135 to 140+) and no specific roster count is treated as fact. THIN SPOT: no revenue figure could be verified on any page successfully fetched. rocketreach.co returned HTTP 403 and R&M did not appear in the fetched Alaska Business Top 49ers list page, so no revenue number is asserted.",
  "locations": [
   "Anchorage, Alaska (headquarters), 9101 Vanguard Drive, Anchorage, AK 99507, phone 1-907-522-1707. The history page states R&M \"relocated to its current Anchorage headquarters at 9101 Vanguard Drive in 1991\".",
   "Fairbanks, Alaska, office reopened in 2009 per the history page; listed as an office location across the site.",
   "Juneau, Alaska, listed as an office location.",
   "Wasilla, Alaska, 2002 East Bogard Road, Suite B. Opened and reported by Alaska Business Magazine on February 3, 2026, described as \"fully operational and staffed to serve the Mat-Su region,\" with Jason Johnston PE as primary contact.",
   "Project geography is statewide. The projects page filters by Aleutians, Interior, North Slope, Northwest, Southcentral, Southeast, Southwest and Statewide."
  ],
  "revenue_model": "FACT: Fee-for-service professional consulting, overwhelmingly to government. The Who We Are page states verbatim: \"Nearly 95% of our work is for public clients\" and lists the markets as \"Airports, Harbors, Roads, Public Facilities, Utilities, Recreational Facilities\". FACT: Named clients visible in the projects page client filter include Alaska Airlines, Municipality of Anchorage, Port of Alaska, University of Alaska Anchorage, the Federal Aviation Administration and various state agencies. FACT: Alaska DOT&PF is a client, named as owner on the Sterling Highway MP 45-60 project where \"R&M is the designer for Stage 1B\". FACT: Federal defense-adjacent work is explicit. The CMMC certification article says the certification \"strengthens R&M's capacity to continue delivering infrastructure solutions for clients including the U.S. Army Corps of Engineers and other Department of Defense-affiliated federal agencies\". FACT: Construction administration is a second, delivery-side revenue stream where R&M acts as owner's representative, including \"Contractor Progress Payments,\" \"Construction Observation and Reporting,\" \"Contractor QC Plan Review and Monitoring\" and \"Project As-Built and Closeout\". FACT: Grant writing is sold \"either as a standalone engagement or as an added-value component to existing work\". INFERENCE: with ~95% public clients, revenue depends on winning competitively procured public agency selections (RFP/SOQ responses) and on term/on-call agreements, so proposal throughput and win rate are the top of the funnel. The site does not describe its procurement mechanics in those words.",
  "pains": [
   {
    "pain": "Eleven positions are open simultaneously, spread across all four offices, and a large share are senior roles requiring 15+ years of experience and an Alaska professional license.",
    "evidence_quote": "Land Surveyor, Project Civil Engineer - Construction Administration, Project Civil Engineer - Surface Transportation, Project Civil Engineer - Utilities, Project Geotechnical Engineer, Senior Environmental Geologist or Engineer, Senior Land Surveyor, Senior Project Civil Engineer - Surface Transportation, Senior Project Civil Engineer - Utilities, Staff Civil Engineer - Water Resources, Staff Surveyor",
    "source_url": "https://www.rmconsult.com/join-us/open-positions/",
    "kind": "fact"
   },
   {
    "pain": "The senior hires they are chasing sit in the scarcest part of the Alaska labor pool. NOTE: the open positions page carries no posting dates, so how long any role has been open CANNOT be verified. The standard stale-posting signal is genuinely unavailable here.",
    "evidence_quote": "B.S. in Civil Engineering with 15+ years civil design experience emphasizing highway/street design",
    "source_url": "https://www.rmconsult.com/job-posting/senior-project-engineer/",
    "kind": "fact"
   },
   {
    "pain": "A stated summer crunch, in their own newsroom.",
    "evidence_quote": "They've provided much needed support during the busy summer months, while also bringing the team fresh perspectives and energy.",
    "source_url": "https://www.rmconsult.com/news-and-views/growing-the-next-generation-of-professionals-meet-rms-2026-intern-class/",
    "kind": "fact"
   },
   {
    "pain": "Construction administration is structurally seasonal and requires people away from the office for long stretches. The posting is classified Seasonal, Full-Time, Hourly.",
    "evidence_quote": "Travel within Alaska will be required, and the ideal candidate must be willing to work in project locations throughout the state for extended periods of time during construction season.",
    "source_url": "https://www.rmconsult.com/job-posting/project-engineer-construction-administration/",
    "kind": "fact"
   },
   {
    "pain": "Construction administration carries a heavy compliance-documentation burden tied directly to whether the project keeps its funding.",
    "evidence_quote": "Administer project documentation and audit trails to ensure funding participation",
    "source_url": "https://www.rmconsult.com/job-posting/project-engineer-construction-administration/",
    "kind": "fact"
   },
   {
    "pain": "Proposal writing is distributed onto senior billable technical staff rather than being fully carried by a marketing function. The same duty appears in multiple senior technical postings across two different departments.",
    "evidence_quote": "Conduct research and write technical proposal portions",
    "source_url": "https://www.rmconsult.com/job-posting/senior-land-surveyor/",
    "kind": "fact"
   },
   {
    "pain": "Same duty, different department. The Senior Project Civil Engineer in Engineering also researches and drafts proposal content on top of design supervision and deliverable review.",
    "evidence_quote": "Review designs, plan drawings, engineering reports and other contract deliverables for feasibility, technical accuracy and quality",
    "source_url": "https://www.rmconsult.com/job-posting/senior-project-engineer/",
    "kind": "fact"
   },
   {
    "pain": "The senior environmental role bundles proposal development, cost estimating, technical report writing and data analysis into one licensed, expensive seat.",
    "evidence_quote": "Developing proposals",
    "source_url": "https://www.rmconsult.com/job-posting/senior-environmental-geologist-or-engineer/",
    "kind": "fact"
   },
   {
    "pain": "They added dedicated proposal capacity in July 2026. Siobhan Johansen was hired as Proposal Manager into the Marketing Group.",
    "evidence_quote": "R&M's deep roots and strong connections throughout the state really resonated with me.",
    "source_url": "https://www.rmconsult.com/news-and-views/new-marketing-and-human-resources-professionals-join-rms-business-services-department/",
    "kind": "fact"
   },
   {
    "pain": "Compliance and IT work outruns in-house capacity. The firm's own IT Group Manager named time and expertise as the binding constraint on their CMMC Level 2 effort.",
    "evidence_quote": "The biggest challenge is time. If your in-house team lacks the required expertise, bring in outside support to get you started.",
    "source_url": "https://www.rmconsult.com/news-and-views/rm-prepares-for-federal-cybersecurity-standards-with-cmmc-compliance/",
    "kind": "fact"
   },
   {
    "pain": "The same IT manager described the compliance process as overwhelming in feel, while defending its value.",
    "evidence_quote": "The process can feel overwhelming, but it ultimately strengthens a firm's security posture and ensures we can continue supporting DoD projects while safeguarding critical information.",
    "source_url": "https://www.rmconsult.com/news-and-views/rm-prepares-for-federal-cybersecurity-standards-with-cmmc-compliance/",
    "kind": "fact"
   },
   {
    "pain": "Isolated employee-review signal of cross-department friction. TREAT AS WEAK, the sample is 7 reviews and the overall rating is 4.4 out of 5, so this is a minority voice and NOT a pattern.",
    "evidence_quote": "I practically begged for help with no response given. Management fight between departments.",
    "source_url": "https://www.indeed.com/cmp/R&m-Consultants,-Inc./reviews",
    "kind": "fact"
   },
   {
    "pain": "Growth is outpacing the back office. In the first eight months of 2026 they opened a fourth office, moved up a Zweig headcount bracket, ran an intern class across four departments, and hired both a Proposal Manager and an HR Generalist into Business Services.",
    "evidence_quote": "R&M's employee-owned culture, outstanding reputation and investment in its people made it an easy choice for me.",
    "source_url": "https://www.rmconsult.com/news-and-views/new-marketing-and-human-resources-professionals-join-rms-business-services-department/",
    "kind": "inference"
   },
   {
    "pain": "With nearly 95% of work from public clients, revenue is gated by competitively procured agency selections, which makes proposal volume and quality a throughput constraint on growth. The site never says this; it follows from the client mix plus proposal duties in senior technical job descriptions.",
    "evidence_quote": "Nearly 95% of our work is for public clients",
    "source_url": "https://www.rmconsult.com/who-we-are/",
    "kind": "inference"
   },
   {
    "pain": "Any system touching federal project data is inside a certified compliance boundary. R&M holds CMMC Level 2, built on 110 NIST SP 800-171 Rev. 2 controls covering access control, data storage security, incident response and system monitoring. This is a CONSTRAINT on where their data can be processed, not a complaint.",
    "evidence_quote": "Cybersecurity is essential to the work we do, especially when supporting federal clients. With Stratus' expertise, we were able to implement the required controls and confirm that we're doing the right things to keep our data secure.",
    "source_url": "https://www.rmconsult.com/news-and-views/rm-achieves-cmmc-level-2-certification-with-guidance-from-stratus-services/",
    "kind": "fact"
   }
  ],
  "notable_context": "OWNERSHIP AND HISTORY (fact, https://www.rmconsult.com/who-we-are/history/). Founded 1968-69 by Ralph Migliaccio, a research geologist at the University of Alaska Fairbanks, as R&M Geological Consultants, work driven by the Trans-Alaska Pipeline System. Jim Rooney joined as a cold-regions geotechnical civil engineer; renamed R&M Engineering and Geological Consultants in 1969 and R&M Consultants, Inc. in 1974. Rooney became President in 1982 after Migliaccio's death. In 1984 the firm split into three entities anticipating an economic contraction. In 2002 employees purchased the company from Jim Rooney, ownership transferring to principals Frank Rast (PE), Len Story (PLS), Rick Bennett (PLS), Bob Grier (PE) and Charlie Riddle (CPG). Ownership today is a principal/shareholder model, NOT a universal ESOP, evidenced by the 30 Employee Owners figure against a 100+ person headcount.\n\nDECISION MAKERS AND VERIFIED CONTACTS (all addresses read off fetched pages, none guessed). Len Story, PLS, Chief Executive Officer, at R&M since 1979, field surveyor to VP of Surveying and Mapping to COO to CEO, one of the 2002 buyers, lstory@rmconsult.com (https://www.rmconsult.com/our-people/len-story/). Andrea Story, FSMPS, CPSM, Chief Marketing & Administrative Officer, 29 years of industry experience, became \"Alaska's first Certified Professional Services Marketer (CPSM)\" in 2001, specializes in \"marketing strategy, market research, communications, and proposal development,\" astory@rmconsult.com (https://www.rmconsult.com/our-people/andrea-story/). Jeremiah Jere Fisher, Group Manager of IT, the named voice on the cybersecurity and compliance program. Chris Black, PE, CESCL, Group Manager of Site Development & Water Resources, cblack@rmconsult.com. Carly Guthrie, Human Resources Generalist. Van Le, AICP, manages the grant writing group. Greg Shearer, PE, CESCL, WAQTC, manages Construction Administration. General inboxes on a fetched page: jobs@rmconsult.com and email@rmconsult.com.\n\nCULTURE AND EMPLOYER BRAND (fact). Fifteen consecutive years on Zweig Group's Best Firms To Work For, 2026 rank #10 in the 100-199 Employees category and #11 in Civil Engineering, with CEO Len Story quoted: \"This recognition is especially meaningful because it comes directly from our employees. I'm proud to be a part of the R&M team and work alongside such talented and dedicated people who care deeply about each other, our clients and the communities we serve throughout Alaska.\" Benefits include medical, vision, dental, long-term disability and life insurance, a 401(k), \"Annual Bonuses and Profit Sharing,\" \"16-41 Days of Personal Leave (dependent on years of experience and tenure with R&M),\" \"9 Paid Holidays Per Year,\" plus a golf simulator. Culture page states \"We know that work and family are intertwined, and we make space to be great at both.\" Indeed shows 4.4 out of 5 across 7 reviews. Glassdoor returned HTTP 403 and could not be read.\n\nMISSION AND POSITIONING (fact). \"Providing innovative professional solutions - for Alaskans, by Alaskans - through uncompromised quality and world class expertise.\" and \"Improving Alaska's communities through innovative cold region design solutions.\" Six stated values: Clients, Employees, Community, Teamwork, Excellence, Integrity. The by-Alaskans, buy-local identity is central and explicit.\n\nTECH AND TOOLING SIGNALS (fact, from job postings). AutoCAD Civil 3D, Microsoft Project, Word and Excel, Trimble Business Center, and for water resources \"Autodesk Storm and Sanitary Analysis, HEC-HMS, HEC-RAS, TR-55, SWMM, and FishXing\". Remote sensing runs UAS, airborne, mobile, terrestrial and bathymetric LiDAR plus sonar and imagery, with the team \"creating accurate and usable datasets\". One staff member, Cody Gibson, earned a Certified Mapping Scientist - Remote Sensing certification in January 2026. NO PAGE FETCHED MENTIONS AI, MACHINE LEARNING, OR AUTOMATION ANYWHERE IN THEIR SERVICES OR NEWS.\n\nRECENT NEWS TIMELINE (fact). Sept 2025 new staff in graphic design, surveying and water resources. Oct 22 2025 CMMC preparation article. Dec 22 2025 CMMC Level 2 certification achieved with Stratus Services, called \"one of the first ~500 companies to achieve Level 2 compliance out of the 119,000 the DoD estimates will need it\" by Stratus CEO Joshua Rabe. Jan 2026 Wasilla office opens, staff promotions, Cody Gibson certification. Apr and May 2026 new hires. Jul 3 2026 Sterling Highway MP 45-60 milestone. Jul 14 2026 Proposal Manager and HR Generalist hired. Jul 30 2026 intern class across Engineering, Planning, Geomatics and Construction Services, recruited from UAA and UAF. Apr 15 2025 (Alaska Business Magazine) launched a new Land Development Group hiring Dave Whitfield, formerly Planning and Zoning Manager and Platting Officer for the Municipality of Anchorage, handling \"entitlement applications, zoning analyses, code drafting, and subdivision/site design support\". INFERENCE: the Land Development Group is a deliberate push toward private-sector and municipal entitlement work, which would diversify away from the ~95% public mix, though no page states that intent.\n\nDATA GAPS AND CORRECTIONS. Their LinkedIn About text is stale, still reading \"From offices in Anchorage, Fairbanks and Juneau\" months after the Wasilla office opened. https://www.rmconsult.com/people/ and https://www.rmconsult.com/contact/ both return HTTP 404; the live paths are /our-people/ and the office details in the site footer.",
  "confidence": "HIGH on what they do, service lines, ownership history, employee-ownership structure, offices, leadership names and titles, client mix, seasonality, hiring load, compliance posture, and every verified contact email, all read off pages fetched directly. MEDIUM on exact current headcount: the firm says 100+ and Zweig places it in the 100-199 bracket, but no page states a precise number. LOW / NOT ASSERTED on revenue: no figure on any fetchable page, rocketreach 403, not in the fetched Top 49ers list. LOW on employee sentiment: Glassdoor 403 and Indeed carries only 7 reviews, so the negative quotes are a weak minority signal and must not be characterized as a pattern. NOT AVAILABLE: job posting dates, so the classic role-open-for-months proof could not be established for any of the 11 openings."
 },
 "people": {
  "agent": "people-finder",
  "leaders": [
   {
    "name": "Len Story, PLS",
    "role": "Chief Executive Officer, voted President of R&M's Board of Directors. Employee-owner since 1979 (field surveyor to VP to COO to CEO, effective January 1st 2016). One of five principal owners named in the 2002 employee buyout.",
    "source_url": "https://www.rmconsult.com/our-people/len-story/"
   },
   {
    "name": "Len Story",
    "role": "CEO appointment and Board presidency, corroborating announcement",
    "source_url": "https://www.rmconsult.com/news-and-views/rms-len-story-named-ceo/"
   },
   {
    "name": "Andrea Story, FSMPS, CPSM",
    "role": "Chief Marketing & Administrative Officer",
    "source_url": "https://www.rmconsult.com/our-people/andrea-story/"
   },
   {
    "name": "Paul Hetzel",
    "role": "Vice President, Construction Services",
    "source_url": "https://www.rmconsult.com/our-people/paul-hetzel/"
   },
   {
    "name": "Frank Rast PE, Len Story PLS, Rick Bennett PLS, Bob Grier PE, Charlie Riddle CPG",
    "role": "The five principal owners employees transferred to in 2002 when they purchased R&M from Jim Rooney. Historical, not a current roster.",
    "source_url": "https://www.rmconsult.com/who-we-are/history/"
   },
   {
    "name": "Bret Coburn",
    "role": "Former CEO 2002-2014 then CFO. RETIRED, announced January 27th 2019. DO NOT CONTACT. Third-party data brokers still list him as CEO and they are stale.",
    "source_url": "https://www.rmconsult.com/news-and-views/bret-coburn-and-jim-robar-pls-retire-from-rm-consultants-inc/"
   }
  ],
  "best_contact": {
   "type": "email",
   "value": "lstory@rmconsult.com",
   "name": "Len Story",
   "role": "Chief Executive Officer and Board President",
   "source_url": "https://www.rmconsult.com/our-people/len-story/",
   "buyer_or_router": "BUYER"
  },
  "alternate_contacts": [
   {
    "value": "astory@rmconsult.com",
    "name": "Andrea Story",
    "role": "Chief Marketing & Administrative Officer",
    "source_url": "https://www.rmconsult.com/our-people/andrea-story/",
    "also_rendered_at": "https://www.rmconsult.com/join-us/open-positions/",
    "buyer_or_router": "BUYER-ROUTER hybrid"
   },
   {
    "value": "email@rmconsult.com",
    "role": "general business inbox",
    "source_url": "https://www.rmconsult.com/who-we-are/"
   },
   {
    "value": "phetzel@rmconsult.com",
    "name": "Paul Hetzel",
    "role": "VP Construction Services",
    "source_url": "https://www.rmconsult.com/our-people/paul-hetzel/"
   }
  ],
  "ownership": "Alaska-based employee-owned professional services consulting firm, founded 1969. In 2002 employees purchased the company from Jim Rooney and ownership passed to five principal owners including Len Story. No outside parent, no PE sponsor found. Offices Anchorage (HQ, 907.522.1707), Fairbanks (907.452.5270), Juneau, Wasilla.",
  "scout_claim_verdict": "CONFIRMED with a framing correction. astory@rmconsult.com IS rendered on the open-positions page as a mailto labelled 'Email Andrea', corroborated on her own bio page. The open-positions page does not state WHY she is listed there, so calling it a recruiting contact would be an inference.",
  "currency_warning": "Rocketreach, ZoomInfo, Seamless and Manta all surfaced in search and Manta still lists Bret Coburn as CEO, which R&M's own site contradicts. NONE were used. Every address came from rmconsult.com pages fetched directly. The CEO announcement is dated 2016 and no 2024-2026 press release naming a president was found; what makes Len Story current is that his bio page is live today rendering 'Chief Executive Officer'.",
  "site_structure_note": "No /about-us/, /about-us/leadership/ or /contact/ path exists, all 404. Live structure is /who-we-are/, /our-people/, /what-we-do/, /projects/, /news-and-views/, /join-us/. No dedicated leadership roster page.",
  "confidence": "high"
 },
 "competitors": {
  "agent": "competitor-analyst",
  "competitors": [
   {
    "name": "Michael Baker International (Anchorage office, 3900 C St., Ste. 900, Anchorage, AK 99503)",
    "note": "National engineering and consulting firm with a long-standing Anchorage principal office and an AGC of Alaska membership, competing for the same DOT&PF, federal and municipal agency work R&M bids. Alaska work spans cold regions engineering, transportation, geotechnical, hydrology, environmental permitting, public involvement, GIS and LiDAR mapping.",
    "ai_usage": "THE ONLY FIRM IN THIS FIELD WITH EVIDENCE OF CHANGED WORK, NOT A MARKETING PAGE. Unveiled 'Titan', a proprietary enterprise AI platform, on April 16th 2026. Verbatim from Michael Baker's own blog: 'Titan allows our teams to instantly tap firmwide knowledge, rapidly make sense of complex data and collaborate across disciplines in real time.' No-code agent builder whose output is shared firmwide, verbatim: 'A transportation engineer's workflow agent becomes available to the entire transportation practice, or a program manager's proposal analysis tool is accessible to every capture team in the firm.' Rollout marks, verbatim: 'The platform was piloted with real users across multiple disciplines before broad rollout, with adoption supported by Michael Baker's AI Champions Network.' Data posture, verbatim: 'No data is retained by external AI providers. No client-sensitive content leaves Michael Baker's secure perimeter.' PR Newswire release of April 16th 2026 puts access at 'more than 6,000 engineers, architects and scientists' across 120+ offices. Separately a VENDOR CASE STUDY documents Mach9 Digital Surveyor extracting sign faces from mobile LiDAR for a statewide DOT sign inventory, 2,500+ miles mapped, 65,000+ signs extracted, 99%+ accuracy inside 90 days. LIMIT ON THIS CLAIM: that DOT is a South-Central U.S. state DOT, NOT Alaska. No adoption or usage numbers for Titan are published.",
    "source_url": "https://mbakerintl.com/news-insights/making-a-difference-blog/technology/rewiring-the-way-michael-baker-works-with-titan-our-proprietary-enterprise-ai-platform/ ; https://www.prnewswire.com/news-releases/michael-baker-international-unveils-titan-an-enterprise-ai-platform-powering-a-new-way-of-working-302745052.html ; https://mach9.ai/customers/case-studies/michael-baker ; https://members.agcak.org/memberdirectory/Details/michael-baker-international-2181486"
   },
   {
    "name": "HDR Alaska, Inc. (582 East 36th Avenue, Suite 500, Anchorage, AK 99503-4169)",
    "note": "National design and engineering firm with a real Anchorage office and a visible Alaska public-works portfolio: Homer Harbor Expansion, Airport Way/Steese Expressway Intersection, Seward Highway Road and Bridge Rehabilitation, William Jack Hernandez Sport Fish Hatchery. Direct competition for DOT&PF and municipal transportation and waterfront pursuits.",
    "ai_usage": "A PUBLISHED POSITION, NOT A DEMONSTRATED DEPLOYMENT. HDR maintains a public 'Artificial Intelligence Informational Statement' saying it uses AI 'in support of our internal operations and in the service of our clients and communities', built on six stated principles: Accountability, Transparency, Privacy, Fairness, Responsibility, Sustainability. Notable for what it forbids: it commits to 'Prohibit the use of generative AI for use in any final work product', states 'Clients always retain ownership of their data', requires written client consent for any client data use with generative AI, and bars client data from model training. Names a 'Generative Artificial Intelligence Usage Policy' internally. No named tool, no named platform, no named project, no measured result. Procurement armor and governance language, not evidence that the work changed.",
    "source_url": "https://www.hdrinc.com/artificial-intelligence-informational-statement ; https://www.hdrinc.com/locations/US/Alaska/Anchorage"
   },
   {
    "name": "DOWL (Anchorage and Juneau, Alaska; founded 1962)",
    "note": "The closest structural analogue to R&M in the Alaska-owned tier. Multi-disciplined consulting firm since 1962, four practice areas: Water and Environmental Services, Transportation and Structures, Civil and Land Development, Construction-Related Services. Offices in Anchorage and Juneau plus Oregon, Washington, Nevada. Head-to-head on the same agency shortlists.",
    "ai_usage": "NONE FOUND, and the one AI artifact that exists is six years old and forward-looking. Homepage carries no reference to artificial intelligence, machine learning, automation or digital delivery. Ten news items fetched from the news index spanning April 2024 to February 4th 2026 contain zero AI or automation mentions. The only AI item anywhere on the site is a July 16th 2020 piece by Brad Melocik PE PH M.ASCE and Teresa Patterson PE Env SP M.ASCE from the Geoprofessional Business Association's Crystal Ball Workshop, stating verbatim that 'Big data, machine learning, and AI all have nearly limitless untapped potential to change the way we live and work.' Speculative commentary about the future of the profession. No claim that DOWL deploys any of it.",
    "source_url": "https://www.dowl.com/ ; https://www.dowl.com/company/news/ ; https://www.dowl.com/news/our-geobusiness-future-big-data-machine-learning-and-ai/"
   },
   {
    "name": "PDC Engineers, a RESPEC Company (Fairbanks, Anchorage and Juneau, Alaska)",
    "note": "Alaska multi-discipline firm serving facilities, transportation, land development and utilities, acquired May 8th 2020 by RESPEC, a 100 percent ESOP geoscience and engineering firm. At acquisition PDC employed more than 100 professionals with stated expertise in 'design services in extreme environments such as in the Artic, Antarctic, and military applications.' The most interesting comparison case, because it is the one Alaska firm whose parent actually sells technology.",
    "ai_usage": "NONE FOUND IN AI TERMS, which is the surprise. RESPEC lists 'Digital Transformation' as an impact area and runs a full 'Data & Technology' expertise domain, and the acquisition release says the combination lets them expand 'delivery of technology solutions to the infrastructure market.' Yet the fetched Data & Technology page names only Software Services, Strategy & Advisory, Staffing, and Data Insight & Innovation, covering data engineering, analytics, modeling, geospatial systems, SCADA and IoT, with no mention of artificial intelligence, machine learning, automation or digital twins anywhere on it. Homepage the same. Insights index surfaced one asset, a 'Data Quality Management' whitepaper, and no AI articles.",
    "source_url": "https://www.respec.com/expertise/data-technology/ ; https://www.respec.com/ ; https://www.respec.com/news/respec-acquires-pdc-engineers/ ; https://www.respec.com/insights/"
   },
   {
    "name": "CRW Engineering Group, Inc. (3940 Arctic Boulevard, Suite 300, Anchorage; Palmer, AK; Olympia, WA)",
    "note": "Founded 1981, one of the largest solely-Alaskan engineering firms, full-service across civil, mechanical, electrical, structural, geotechnical and environmental, plus land and aerial surveying, mapping and planning. Service list including Airport Engineering, Rural Infrastructure, Survey & Mapping, Hydraulics & Hydrology and Federal Services sits directly on top of R&M's public-client work.",
    "ai_usage": "NONE FOUND. No mention of artificial intelligence, machine learning, automation or digital tools anywhere on the fetched homepage. The single technology reference is 'Unmanned Aerial Vehicle (UAV) 3D Modeling' used for surveying, which is field data capture and photogrammetry, not AI. Worth naming precisely, because drone capture is the thing most often mistaken for an AI move in this sector and it is not one.",
    "source_url": "https://www.crweng.com/"
   }
  ],
  "where_target_is_behind": "R&M is behind on exactly one axis and it is narrow, but it is the axis that decides shortlists. Michael Baker International, at 3900 C St in Anchorage, bidding the same agency work, spent April 2026 putting an AI operating layer in front of every one of its 6,000-plus staff, and the single most exposed line for R&M is the one about proposals, verbatim: 'a program manager's proposal analysis tool is accessible to every capture team in the firm.' R&M's whole revenue model is winning public solicitations, and a national competitor now has firmwide shared purpose-built agents pointed at pursuit work while R&M's own site carries no AI or automation posture of any kind. Michael Baker also has one documented production ML result, 65,000-plus signs from mobile LiDAR at 99-plus percent accuracy in 90 days for a statewide DOT sign inventory, a capability story R&M has no counter to in a survey and mapping interview. HONEST CAVEAT: that project was a South-Central U.S. DOT and not Alaska, so the capability is proven and the Alaska application is not. The second exposure is governance, not tooling. HDR Alaska has a public principled AI statement with a hard commitment that no generative AI ends up in a final work product. R&M has no published position at all. The moment an agency adds an AI-disclosure question to a solicitation, HDR and Michael Baker each have an answer already written and R&M is drafting one under deadline. Nothing else in this field is ahead of R&M and it would be dishonest to say otherwise.",
  "where_target_could_lead": "The Alaska-owned tier is empty, and that is the finding. Across DOWL, CRW and PDC/RESPEC, three firms that bid against R&M constantly, the total published evidence of AI is one speculative 2020 workshop article on DOWL's site that makes no claim of use, one UAV 3D modeling line on CRW's survey page that is photogrammetry rather than AI, and a RESPEC Data & Technology practice that sells data engineering, analytics, geospatial, SCADA and IoT and still does not use the words artificial intelligence or machine learning anywhere on its own expertise page. PND Engineers, checked as an additional Anchorage-headquartered peer, mentions nothing either. No Alaska-headquartered engineering firm in this set has published an AI policy, named an AI tool, or shown a client-facing automation. The whole national field, excepting Michael Baker, is in the same place at a shallower depth. Two distinct open positions: first the plain capability position, where the first Alaska-owned firm to show a real measured change in how work gets done rather than a page about it owns ground nobody has contested; second the governance position, cheaper and untaken by anyone in the Alaska-owned tier, being the first in-state firm able to hand an agency a written defensible answer about how AI is and is not used on its deliverables. The second is available at almost no cost and is the harder one for a competitor to take back.",
  "confidence": "High on the competitor set and on who has moved. Every claim traces to a page fetched in session; the Michael Baker Titan detail comes from Michael Baker's own blog plus the PR Newswire release rather than a search snippet. TWO CAVEATS. First, HDL Engineering Consultants of Anchorage, Palmer and Kenai is a genuine head-to-head Alaska competitor with an overlapping service list, and it is DELIBERATELY EXCLUDED because hdlalaska.com returned an empty body on three fetch attempts. Treat HDL as UNASSESSED, not as clean. Second, absence of evidence here is absence of a PUBLIC claim. A firm can be running AI internally and saying nothing, which is common in this sector, so 'none found' means nothing published on a page fetched and never means nothing happening. The Michael Baker Mach9 result is verified from the VENDOR's case study, not Michael Baker's own site, and its DOT is explicitly outside Alaska."
 },
 "industry": {
  "agent": "industry-analyst",
  "industry": "AEC consulting - civil engineering, land surveying, environmental permitting and transportation design firms (50-300 staff) working primarily for public agency owners (state DOT, municipal, federal, tribal, utility)",
  "in_production": [
   {
    "who": "Louisiana DOTD (LTRC evaluation, 50+ construction projects across four districts) using HeadLight photo-based e-Construction inspection",
    "what_ai": "Mobile, photo/media-first field inspection replacing paper daily work reports. Auto-generation of DWRs from tagged field observations. Workflow automation with ML-assisted capture, NOT generative AI.",
    "outcome": "INDEPENDENT MEASUREMENT (state DOT research center, FHWA co-sponsored, Rupnow/Coco/White/Yamaura, 2020). Verbatim: 'Inspectors using HeadLight experienced a 28 percent increase in productivity'; department-wide adoption estimated to save over 117,000 hours annually; inspectors collected '1.9 times more observations'; DWRs completed within 24 hours up to 66%, within 72 hours up to 82%; zero lost claims during the pilot. Related multi-state consortium work (CA, WA, TX, MN) reported each field inspector repurposing roughly 38 hours of admin work per month, about 1.6 hours per day.",
    "source_url": "https://rosap.ntl.bts.gov/view/dot/56247",
    "reliability": "proven"
   },
   {
    "who": "City and County of Honolulu Department of Planning and Permitting, using CivCheck AI-guided plan review (agency-side, screens submittals from design consultants)",
    "what_ai": "AI pre-screen that guides the APPLICANT before formal review, flagging missing documents and likely code non-compliance so fewer correction cycles reach staff reviewers.",
    "outcome": "AGENCY-MEASURED, reported by GovTech (July 2nd 2026). Verbatim: average review times decreased 'from 73 days to 32.5 days' (about 40.5 days faster per permit) and 'plan review cycles dropped from 3.4 to 1.4 cycles.' Sample: '19 CivCheck-processed residential permits' vs '17 similar non-CivCheck projects.' DPP spokesperson Davis Pitner acknowledged '19 completed applications is a relatively small sample.' Scope limited to residential. Launched December 2025.",
    "source_url": "https://www.govtech.com/artificial-intelligence/honolulu-launches-ai-assisted-fast-track-permit-review",
    "reliability": "proven"
   },
   {
    "who": "US DOE / Pacific Northwest National Laboratory PermitAI",
    "what_ai": "NEPATEC 2.0 open machine-readable corpus of environmental review documents plus SearchNEPA (beta, ~30 DOE evaluators), ChatNEPA, CommentNEPA, WriteNEPA, EngageNEPA.",
    "outcome": "GOVERNMENT-REPORTED DEPLOYMENT (PNNL release, August 21st 2025). Corpus: 'approximately 120,000 documents from 60,000 projects authored by more than 60 different agencies,' over 50 years. Earlier release (Dec 3rd 2024) reported 28,212 documents across 2,917 NEPA reviews, 4.8 million pages, on HuggingFace. Baseline: an EIS typically takes 'around two to four years and costs from $100,000 to $1 million.' No end-to-end cycle-time improvement published. PNNL states explicitly that AI will not automate the NEPA process and human evaluators remain the decision-makers.",
    "source_url": "https://www.pnnl.gov/news-media/permitai-ushers-new-era-faster-better-federal-permitting",
    "reliability": "proven"
   },
   {
    "who": "PNNL PermitAI team with OpenAI, DraftNEPABench (benchmark, not a shipped product)",
    "what_ai": "Generalized coding agents drafting NEPA document subsections, scored on structure, clarity, accuracy and use of references.",
    "outcome": "BENCHMARK WITH EXPERT EVALUATION (national lab preprint, February 2026). Drafting tasks spanning 18 federal agencies, assessed by '19 subject matter experts familiar with NEPA review.' Verbatim: 'Experts found coding agents could save 1-5 hours per subsection - up to roughly a 15% reduction in drafting time.' CRITICAL CAVEAT quoted: 'if references are incomplete or out of date, models may not reliably identify those discrepancies unless explicitly instructed,' and the benchmark evaluates 'well-specified tasks where relevant context is available,' not real work involving 'more ambiguity, discretion, and iterative expert feedback.' Co-author is a model vendor, so treat 15% as a CEILING under favorable conditions.",
    "source_url": "https://www.gend.co/blog/draftnepabench-ai-federal-permitting",
    "reliability": "proven"
   },
   {
    "who": "PNNL / Iowa State University, NEPAQuAD benchmark and MAPLE evaluation pipeline",
    "what_ai": "Five frontier LLMs answering questions drawn from real Environmental Impact Statements.",
    "outcome": "INDEPENDENT PEER-REVIEWED MEASUREMENT (arXiv 2407.07321, submitted July 10th 2024, revised June 12th 2025). Two findings that shape any document-assistant build. First, 'RAG-based approaches substantially outperform PDF document contexts,' meaning dumping whole PDFs into a long context window is measurably worse than proper retrieval. Second, models perform best only when handed the gold passage, and NEPA regulatory reasoning remains hard for all five. No absolute accuracy percentage published in the abstract.",
    "source_url": "http://arxiv.org/abs/2407.07321v3",
    "reliability": "proven"
   },
   {
    "who": "Indiana DOT with Purdue University (JTRP), machine-aided bridge deck crack condition assessment",
    "what_ai": "Deep learning (image classification plus semantic segmentation) over real INDOT Bridge Inspection Application System photos, assigning FHWA condition states for reinforced concrete deck cracking.",
    "outcome": "INDEPENDENT PEER-REVIEWED MEASUREMENT (Sensors, April 22nd 2023; NSF OAC-1835473 plus INDOT/Purdue JTRP). Dataset 3,549 images (2,350 cracked, 1,199 non-cracked). Crack detection about 0.94 accuracy, 0.93 precision, 0.94 recall. Sealed-crack detection about 0.93 accuracy. Crack-type classification about 0.84. BUT semantic segmentation, the step that actually quantifies the defect, landed at 'average IoU was approximately 0.61' with 0.68 recall and 0.35 precision. Authors' own conclusion: manual-AI collaboration is recommended for risk management rather than full automation, and real inspection imagery underperformed purpose-built datasets. The cleanest published illustration in the industry that coarse triage works and fine measurement does not.",
    "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10181228/",
    "reliability": "proven"
   },
   {
    "who": "Commonwealth of Massachusetts Federal Funds and Infrastructure Office with Northeastern University's Burnes Center, GrantWell",
    "what_ai": "AI tool that finds matching grants for a community, summarizes grant documents, answers requirement questions, and drafts a first-pass project narrative.",
    "outcome": "GOVERNMENT DEPLOYMENT, NO OUTCOME DATA YET (launched March 26th 2026; GovTech coverage). Free to all Massachusetts communities. Director Quentin Palfrey, verbatim: 'The tool is not intended to replace human review of the grant-writing process, rather it is designed to help save users time and capacity.' Pennsylvania launched a comparable grant-search tool in 2024. Directly adjacent to the funding-application work civil firms do for small municipal and rural clients.",
    "source_url": "https://www.govtech.com/artificial-intelligence/massachusetts-uses-ai-to-help-cities-access-grant-funding",
    "reliability": "proven"
   },
   {
    "who": "Kimley-Horn (civil/transportation consulting, 10,000+ employees), Microsoft 365 Copilot",
    "what_ai": "Meeting transcription and summaries, rapid document comparison to surface prior decisions, plus a design-side application on utility-scale solar grading.",
    "outcome": "VENDOR CASE STUDY, NAMED CUSTOMER (published by Microsoft, April 22nd 2026). Reported: automated transcription and summaries 'reduced need for dedicated note-takers'; '50% reduction in grading while maintaining power production' on utility-scale solar sites. Named quotes include CTO Nick Otto, 'The black box problem with AI is a huge one for us,' and SVP Melissa Hewitt, 'Our approach has always been about augmentation, not necessarily automation.' No hours-saved figure, no baseline, no independent audit.",
    "source_url": "https://www.microsoft.com/en/customers/story/26418-kimley-horn-microsoft-365",
    "reliability": "vendor_claim"
   },
   {
    "who": "WSP (global engineering consultancy), Microsoft 365 Copilot",
    "what_ai": "General knowledge-work assistance: repetitive task automation, drafting and editing, information lookup, translation, code/formula help.",
    "outcome": "VENDOR CASE STUDY, NAMED CUSTOMER (Microsoft). Reported: 'More than four fifths (84%) of WSP Copilot users who respond to a regular survey about the tool confirm they are saving time every day.' SELF-REPORTED perceived time saving among respondents to a voluntary internal survey, NOT a measured productivity delta.",
    "source_url": "https://www.microsoft.com/en/customers/story/26012-wsp-microsoft-365-copilot/",
    "reliability": "vendor_claim"
   },
   {
    "who": "Hawaii DOT, City of Plano TX, Alabama DOT, Utah DOT, Bentley Systems Blyncsy",
    "what_ai": "Computer vision on crowdsourced dashcam imagery detecting pavement distress, signs, guardrail, striping, replacing windshield survey crews.",
    "outcome": "VENDOR CASE STUDY, NAMED AGENCIES. Verbatim from Bentley/Carahsoft: Hawaii DOT 'cut manual surveys by 95%, identified 930+ issues per week, and achieved nearly $1M in annual savings'; Plano TX 'cut road maintenance costs by 90%'. Bentley's own editorial blog, when fetched, named NO specific DOT clients. Treat every number as vendor-published. No independent evaluation of Blyncsy accuracy found.",
    "source_url": "https://www.carahsoft.com/bentley/solutions/blyncsy",
    "reliability": "vendor_claim"
   },
   {
    "who": "AEC proposal/SF330 automation vendors (Flowcase, OpenAsset with Shred, Unanet, Deltek Vantagepoint with Dela, Workorb, Bidara)",
    "what_ai": "Auto-population of SF330 Sections E/F from personnel and project databases, resume and project-sheet generation, RFP shredding into compliance matrices, image/asset selection.",
    "outcome": "VENDOR MARKETING, mostly UNNAMED CUSTOMERS. The circulating figures (20% faster proposals, 60% less duplicate content, '75% time savings with 44%+ win rates', an '85-person engineering firm' slashing image-handling time) all trace to vendor blogs or vendor-published comparison pages, and the ones with numbers generally do not name the firm. Deltek publishes a 25% operational efficiency claim without a named A/E source. HONEST FINDING: this is the LOUDEST MARKETED pocket in the industry and the THINNEST MEASURED one. Standalone tool pricing roughly $30-80 per user per month, though most vendors quote per deployment.",
    "source_url": "https://rfpm.ai/alternatives",
    "reliability": "vendor_claim"
   }
  ],
  "the_gap": "THE MARKETING POINTS AT PROPOSALS AND AT DESIGN. THE MEASURED WINS ARE IN FIELD DOCUMENTATION AND IN CITED, HUMAN-APPROVED DRAFTING. Every AEC AI vendor pitch aimed at a firm this size leads with SF330 and pursuit automation, and that is precisely the pocket where this search could not find a single named firm attached to a measured number. The circulating proposal statistics are vendor-published, mostly with the customer anonymized, and none carry a method. Meanwhile the two hardest numbers in the entire industry are unglamorous: a state DOT research center measuring 28% inspector productivity on field documentation, and 19 federal subject matter experts measuring 1 to 5 hours per subsection on NEPA drafting with references verified and humans approving. SECOND GAP, DESIGN SIDE. AI is marketed hardest for design generation, and the peer-reviewed evidence says visual AI is good at DETECTION and bad at MEASUREMENT. INDOT/Purdue got about 0.94 accuracy answering 'is there a crack' and 0.61 IoU with 0.35 precision answering 'how big is it'. A firm that buys AI to produce quantities, dimensions or a stamped number is buying at the wrong end of that curve. THIRD GAP, MOST LIKELY TO COST MONEY. The single most-marketed architecture, point a model at your PDF library and ask it questions, is the one the peer-reviewed benchmark in this exact domain measured as inferior. NEPAQuAD/MAPLE found retrieval substantially outperforms feeding PDF documents as context. Buying the long-context demo is buying the version that was measured and found worse. FOURTH GAP, PECULIAR TO PUBLIC-AGENCY WORK. The rule that actually binds is NOT a procurement AI-disclosure rule, because this search found no such blanket rule. It is the PE seal, the standard of care, and the insurance file. ASCE PS 573 puts responsibility on the licensed engineer, 80% of A&E professional liability insurers now treat AI adoption as a disruptor, ISO published generative-AI exclusions effective January 2026, and renewal questionnaires are asking who reviews AI output and whether that review is documented. That reframes the whole buying decision for a firm this size: the deliverable that makes AI safe here is a REVIEW AND CITATION-VERIFICATION RECORD, not a faster first draft. A firm with a documented human-review trail can answer its insurer, its client and a licensing board. A firm with a faster draft and no trail has bought risk. FIFTH GAP, CLIENT SIDE. The agencies these firms serve are deploying AI on the RECEIVING end of the firm's work, Honolulu on plan review, Massachusetts on grant narratives, PNNL on NEPA search and comment processing, several DOTs on asset condition. That changes what a good submittal looks like before it changes what a good design looks like, and it is the shift least likely to be on an owner's radar.",
  "grounding_facts": [
   {
    "fact": "Bluebeam 2026 Building the Future AEC Technology Outlook, over 1,000 technology decision-makers at manager level or above across five countries, surveyed online July 2025: only 27% of AEC firms currently use AI; 68% of AI adopters 'have saved at least $50,000'; 46% 'have saved 500-1,000 hours using AI tools'; top barriers data sharing security 42% and cost/complexity 33%; 56% report AI helps offset skilled labor shortages. Published October 28th 2025. VENDOR-SPONSORED survey with a stated method.",
    "source_url": "https://press.bluebeam.com/2025/10/new-bluebeam-report-shows-early-ai-adopters-in-aec-seeing-significant-roi-despite-uneven-adoption/",
    "reliability": "vendor"
   },
   {
    "fact": "BST Global AI + Data Insights 2025 Global AEC Industry Report, run with the ACEC Technology Committee, published June 16th 2025. 54% of respondents from firms of 500 employees or fewer; 59% ACEC member firms. Findings: 'only about 20% claimed readiness at a mature or advanced level'; at least one third say their AI strategy is not integrated with business strategy; more than half are currently using open or public GenAI models; only 1% have achieved widespread adoption of AI-enabled processes. No total sample size or confidence interval published.",
    "source_url": "https://bstglobal.com/blog/ai-data-insights-2025-global-aec-industry-report/",
    "reliability": "vendor"
   },
   {
    "fact": "ACEC Research Institute Engineering Business Sentiment Survey, Q1 2026: 628 executive-level leaders at engineering firms, surveyed January 13th to 25th 2026, administered by the Institute for Association and Nonprofit Research. More than half of firms report investing in dedicated AI-focused talent. Earlier ACEC Q1 2025 reporting: 63% of member firms have an AI strategy in place or are actively developing one.",
    "source_url": "https://engineeringinc.acec.org/blog/engineering-firms-report-rebounding-economic-confidence-accelerating-ai-investment/",
    "reliability": "authoritative"
   },
   {
    "fact": "AASHTO Committee on Transportation System Operations AI survey, March 6th to May 28th 2025, 76 respondents from 51 State DOTs. Most critical AI roles: traffic management and optimization 77.3%, data analysis 74.7%, safety/incident detection 73.7%. Biggest challenges: data quality and availability 76%, security 69.3%, reliability 61.3%, lack of skilled workforce 56%, implementation costs 47%.",
    "source_url": "https://aashtojournal.transportation.org/aashto-survey-reviews-impact-of-ai-on-operations/",
    "reliability": "authoritative"
   },
   {
    "fact": "ASCE Policy Statement 573, Artificial Intelligence and Engineering Responsibility, adopted July 18th 2024. Verbatim: 'The civil engineer must maintain responsibility for project planning, designing, building, operations, maintenance, and the protection of the public health, safety, and welfare'; 'AI cannot serve as a replacement for the professional judgement of a licensed Professional Engineer'; 'AI cannot be held accountable, nor can it replace the training, experience, and judgement of a professional engineer.'",
    "source_url": "https://www.asce.org/advocacy/policy-statements/ps573---artificial-intelligence-and-engineering-responsibility",
    "reliability": "authoritative"
   },
   {
    "fact": "Ames & Gough 2026 survey of 15 leading architects and engineers professional liability insurers: 73% planning rate increases; 60% reported higher claim severity in 2025, up from 53% the prior year and 41% in 2023, with NO insurer reporting a decrease; claim severity by discipline runs structural engineering 80%, civil engineering 73%, architecture 60%; and 80% of insurers view AI adoption by design firms as a potential disruptor whose use 'must be supported by disciplined controls, transparency and accountability.'",
    "source_url": "https://www.insurancebusinessmag.com/us/news/construction/most-aande-liability-insurers-plan-rate-hikes-in-2026--ames-and-gough-566403.aspx",
    "reliability": "authoritative"
   },
   {
    "fact": "ISO/Verisk released three optional generative-AI exclusion endorsements effective January 2026 for commercial general liability: CG 40 47 'Exclusion - Generative Artificial Intelligence', CG 40 48 (Coverage B only), and CG 35 08 (products/completed operations). All three define generative AI as 'a machine-based learning system or model that is trained on data with the ability to create content or responses.' The endorsements are OPTIONAL and each carrier chooses whether to attach them.",
    "source_url": "https://www.independentagent.com/vu_resource/verisk-to-roll-out-new-general-liability-exclusions-for-generative-ai-exposures/",
    "reliability": "authoritative"
   },
   {
    "fact": "Federal procurement: NO blanket requirement to disclose AI use in a proposal was found. The National Law Review analysis cites no agency mandating AI disclosure and no named clause with an effective date. It identifies the actual exposure as misrepresentation, verbatim: 'inaccurate or misleading representations - whether made manually or by an AI system - can lead to lost opportunities, bid protests, False Claims Act liability, and poor past performance ratings,' plus source selection information breaches under FAR 3.104, and notes that 'Some federal government solicitations require original writing, specific formats, or certifications that may conflict with generative AI use.'",
    "source_url": "https://natlawreview.com/article/navigating-federal-solicitations-artificial-intelligence",
    "reliability": "authoritative"
   },
   {
    "fact": "CEQ Permitting Technology Action Plan, following the Presidential Memorandum 'Updating Permitting Technology for the 21st Century' signed April 15th 2025. Permitting Innovation Center established April 30th 2025; Action Plan issued May 30th 2025. Verbatim: 'As agencies consider the use of artificial intelligence (AI) in their NEPA and permitting software systems, they should reference the Office of Management and Budget memorandum M-25-21.' Four service delivery standards, a 90-day implementation clock for listed agencies, and NO quantified performance targets.",
    "source_url": "https://permitting.innovation.gov/resources/action-plan/",
    "reliability": "authoritative"
   },
   {
    "fact": "PNNL PermitAI baseline for federal environmental review, from the lab's own December 3rd 2024 release: an environmental impact statement typically requires 'around two to four years and costs from $100,000 to $1 million.' The team states plainly that AI will not automate the entire NEPA review process and that human NEPA evaluators remain the drivers of decision-making.",
    "source_url": "https://www.pnnl.gov/news-media/faster-more-informed-environmental-permitting-ai-guided-support",
    "reliability": "authoritative"
   },
   {
    "fact": "Citation integrity is a measured, worsening problem in professional and technical documents. A Nature analysis found fabricated references rose from 1 in 2,828 papers in 2023 to 1 in 458 in 2025, roughly a sixfold increase. Named consultancies have had reports withdrawn or corrected over hallucinated citations. For a firm whose deliverables cite codes, standards, permits and prior agency decisions, verification of every reference is the control that makes an AI drafting tool usable rather than a liability.",
    "source_url": "https://www.nature.com/articles/d41586-026-00969-z",
    "reliability": "authoritative"
   },
   {
    "fact": "Buying signal for firms this size: standalone AEC proposal/DAM tools are reported to run roughly $30-80 per user per month, but 'almost nobody in this category publishes full pricing' and the major vendors 'quote per deployment, scoped to firm size and modules.' Deltek Vantagepoint (the dominant A/E ERP) ships its Dela AI assistant inside the existing product, which means for firms already on Vantagepoint the first AI capability is a RELEASE, not a purchase.",
    "source_url": "https://rfpm.ai/alternatives",
    "reliability": "vendor"
   },
   {
    "fact": "Alaska-specific: NO formal statewide State of Alaska AI policy governing agency or consultant use was located in this search. Alaska HB 306 (33rd Legislature) would have set AI policy for state agencies including human oversight, a public inventory of AI in use, and regular impact assessments, but its final status COULD NOT BE VERIFIED because legiscan.com returned HTTP 403, so no claim about its passage is made.",
    "source_url": "https://www.aft.org/sites/default/files/media/documents/2025/ai_in_state_gov_report_2025.pdf",
    "reliability": "vendor"
   }
  ],
  "confidence": "HIGH on the governing layer and on the industry-adoption picture. ASCE PS 573, the Ames & Gough insurer survey, the ISO/Verisk exclusions, the AASHTO CTSO survey, the ACEC and BST/ACEC surveys, and the federal permitting memorandum chain were all fetched directly and quoted. HIGH on the five measured wins: Louisiana DOTD/HeadLight, Honolulu DPP/CivCheck, DraftNEPABench, NEPAQuAD/MAPLE and the INDOT/Purdue bridge study are all fetched, dated, and carry a stated method, sample and limitation. MEDIUM on roadway asset AI, where deployment is real and named but every performance number is Bentley-published. LOW on proposal and SF330 automation, and THIS IS THE MOST IMPORTANT CALIBRATION IN THE REPORT: the category is unquestionably shipping and widely bought, but after working vendor case-study pages, comparison sites, SMPS and ACEC channels, ENR and the trade press, this search found NO named firm of any size attached to a measured proposal-productivity number with a stated method. That is a genuine evidence gap, not a search shortfall, though it is possible the numbers exist inside paywalled Zweig Group and SMPS research and inside ACEC PDFs that returned HTTP 403. KNOWN COVERAGE HOLES: nspe.org, acec.org PDF hosting, enr.com, sciencedirect.com, legiscan.com, ltrc.la.gov and several state DOT PDF endpoints all blocked automated fetching, and the environment could not extract text from PDFs, so PDF-only primary sources are represented here only through fetched HTML secondaries or are absent. Nothing in this report is sourced to a search snippet alone."
 }
}
```


---

## Discovery room

```json
{
 "opportunity_map": [
  {
   "area": "Business development and proposal production (Marketing Group)",
   "what_ai_could_change": "Senior technical staff carry a proposal duty on top of billable work. The Senior Land Surveyor and Senior Project Civil Engineer - Surface Transportation postings both carry the identical bullet 'Conduct research and write technical portions of proposals to assist in bringing in new work.' and the Senior Environmental Geologist or Engineer posting carries 'Developing proposals.' Retrieval over R&M's own prior technical narratives and project records could turn a blank page into a cited first draft. Weighed honestly, this is the loudest area and the thinnest-measured one: the industry-analyst found no named firm at any size attached to a measured proposal-productivity number with a stated method, and R&M hired a dedicated Proposal Manager into Marketing on July 14th 2026, so a human intervention is already live here."
  },
  {
   "area": "Construction administration, field inspection and the funding audit trail",
   "what_ai_could_change": "The Project Civil Engineer - Construction Administration posting carries 'Administer project documentation and audit trails to ensure funding participation' and 'Travel within Alaska will be required, and the ideal candidate must be willing to work in project locations throughout the state for extended periods of time during construction season.', classified Seasonal, Full-Time, Hourly. Structured field capture plus drafted daily reports plus a completeness check against contract documentation requirements. This is where the only independent measured number in the whole file sits: Louisiana DOTD/LTRC with FHWA, 'Inspectors using HeadLight experienced a 28 percent increase in productivity when creating and submitting daily work reports (DWRs).' The note that matters is that the winning system there was workflow and capture automation with light ML, not a large language model."
  },
  {
   "area": "NEPA and environmental permitting documentation",
   "what_ai_could_change": "NEPA and Permitting are two of the 24 listed service lines. DraftNEPABench, assessed by 19 subject matter experts across tasks from 18 federal agencies, puts 'coding agents could save 1-5 hours per subsection, up to roughly a 15% reduction in drafting time'. A model vendor co-authored it, so 15% is a ceiling under favourable conditions, and the authors' own caveat is that where references are incomplete or out of date the models may not reliably flag the discrepancy unless told to. Modest, real, capped."
  },
  {
   "area": "Public involvement and comment response",
   "what_ai_could_change": "Public Involvement is a named service line and NEPA work generates comment-response obligations. Classification, clustering and drafted responses over a bounded comment set with every response approved by a person is a textbook language job. Volume at a 100-plus person firm is bursty rather than steady, which caps the size."
  },
  {
   "area": "Grant writing as a billable service line",
   "what_ai_could_change": "Grant Writing sits in the 24 service lines, which means R&M writes grants for public clients rather than only for itself. Same machinery as proposals, except the output is revenue-generating delivery instead of overhead. Nothing about grant volume or win rate is published, so this is an interesting shape with no evidence behind it yet."
  },
  {
   "area": "Design QA/QC and the licensed review chokepoint",
   "what_ai_could_change": "'Review designs, plan drawings, engineering reports and other contract deliverables for feasibility, technical accuracy and quality' is a verbatim duty on the Senior Project Civil Engineer posting. Deterministic completeness checking is genuinely available here, sheet index against sheets present, callouts that resolve, quantities that reconcile. Generative review of a stamped deliverable is the single worst place in this firm to put a model. ASCE Policy Statement 573, adopted July 18th 2024, holds the responsibility with the licensed engineer, and the Ames & Gough 2026 survey of 15 A&E liability insurers found 80% of insurers viewing AI adoption by design firms as a potential disruptor, with ISO/Verisk issuing three optional generative-AI exclusion endorsements effective January 2026."
  },
  {
   "area": "Land surveying and geomatics",
   "what_ai_could_change": "Two of the eleven open roles are surveying seats and the CEO is a PLS. Field-to-finish note reduction, right-of-way and title research, and survey record retrieval are real. Most of the actual win here is deterministic data plumbing rather than a model."
  },
  {
   "area": "Remote sensing, GIS and hydrographic",
   "what_ai_could_change": "Automated feature and defect detection over imagery and point clouds. The cleanest published calibration in the file is INDOT with Purdue, 3,549 images, where crack classification accuracy was approximately 0.94 while 'the average IoU was approximately 0.61' and 'average crack pixel detection recall and precision were 0.68 and 0.35, respectively'. Coarse detection works, fine measurement does not, and those authors recommend manual-AI collaboration rather than full automation."
  },
  {
   "area": "Geotechnical, geology and contaminated sites",
   "what_ai_could_change": "Boring logs, lab results and site characterization reporting are semi-structured and repetitive. Extraction and report assembly are plausible. Interpretation stays with the licensed professional."
  },
  {
   "area": "Materials testing and special inspections",
   "what_ai_could_change": "Honestly, very little AI. Breaks, gradations and densities are structured, stable and high-volume, which is exactly the profile where deterministic automation is cheaper, testable and safer. Saying so out loud is worth more here than a model."
  },
  {
   "area": "Institutional knowledge across four offices and 24 service lines since 1969",
   "what_ai_could_change": "Retrieval over the firm's own corpus. The strongest technical support in the file is NEPAQuAD/MAPLE, a PNNL and Iowa State preprint (not peer reviewed), finding 'RAG-based approaches substantially outperform PDF document contexts' with models performing best when handed the exact right passage. This is also precisely what a direct competitor built: Michael Baker International's Titan, announced April 16th 2026, an 'enterprise operating layer' giving 'unprecedented access to knowledge for more than 6,000 engineers, architects and scientists', and Michael Baker has a principal office at 3900 C St in Anchorage bidding the same agency work."
  },
  {
   "area": "Recruiting, onboarding and seasonal ramp",
   "what_ai_could_change": "Eleven positions open at once across four offices. No posting dates are published, so how long any has been open is unknowable from outside and no staleness argument is available. The defensible read is capacity, not desperation: a seasonal hourly field workforce that re-onboards every spring is the population that benefits most from a system carrying the documentation rules for them."
  },
  {
   "area": "IT, CMMC Level 2 and the compliance boundary",
   "what_ai_could_change": "R&M achieved CMMC Level 2 on December 22nd 2025 with Stratus Services, '110 controls based on NIST Special Publication 800-171 Revision 2'. Jere Fisher, Group Manager of IT, said 'The biggest challenge is time. If your in-house team lacks the required expertise, bring in outside support to get you started.' Continuous control evidence is an obvious automation target, though whether it currently burdens them is an assumption and they already have a named partner. The far more important use of this fact is architectural: any system touching federal project data has to sit inside that certified boundary, which constrains every candidate below and is an asset almost no firm this size holds."
  },
  {
   "area": "Business services, project accounting and contract administration",
   "what_ai_could_change": "Nearly 95% of the work is for public clients, so invoicing, certified payroll, subconsultant administration and progress billing run against agency rules. Rules-based automation territory. Low glamour, real hours, and no model required for most of it."
  },
  {
   "area": "Marketing and firm reputation",
   "what_ai_could_change": "Andrea Story is Chief Marketing & Administrative Officer, Alaska's first Certified Professional Services Marketer, and 'She specializes in marketing and strategic planning, market research, communications and proposal development.' Fifteen consecutive years on Zweig Group's Best Firms To Work For, #10 in the 100-199 employees category for 2026. This is a function that is already strong and well led. It needs leverage far less than it needs to be left alone."
  }
 ],
 "outcome": "Recover senior and field staff hours currently spent producing, chasing and reconciling project records that are not the engineering itself, and hold or improve the completeness of those records while doing it. Measured as: hours per person per week on one named document class, baselined by R&M for four weeks before anything is built, with a target reduction at 90 days of live use, the count of records produced holding or rising, and zero increase in review or audit findings against those records. A build that produces fewer hours but a thinner record has failed this outcome, and a build whose only claim is that it exists has failed it before it starts. No R&M revenue, headcount, proposal volume or hours figure is published anywhere, so every baseline in this outcome is one they measure, never one we assert.",
 "opportunities": [
  {
   "job": "When I am a construction inspector or CA engineer working a project site somewhere in Alaska during the season, I need what happened today to become a complete, dated, auditable record, so that funding participation on the project is never put at risk by a gap in documentation.",
   "pain_source": "Verbatim duty 'Administer project documentation and audit trails to ensure funding participation' on https://www.rmconsult.com/job-posting/project-engineer-construction-administration/ , plus verbatim on the same posting 'Travel within Alaska will be required, and the ideal candidate must be willing to work in project locations throughout the state for extended periods of time during construction season.' and its Seasonal, Full-Time, Hourly classification. Construction Administration and Special Inspections are two of the 24 service lines. Nearly 95% of the work is for public clients per https://www.rmconsult.com/who-we-are/ , which is what makes funding participation money rather than paperwork.",
   "current_workaround": "Unknown in specifics and that matters. The generic shape in this sector is field notes plus a phone camera plus a form, typed into the owner's or the firm's record system in the evening or after the trip. Whether R&M uses a commercial field system today is not published and we do not claim to know.",
   "importance": 9,
   "satisfaction": 4,
   "opportunity_score": 14,
   "notes": "Highest Ulwick score and the only job in this set backed by an independent measurement rather than a vendor claim: Louisiana DOTD/LTRC with FHWA over 50-plus projects, 'Inspectors using HeadLight experienced a 28 percent increase in productivity when creating and submitting daily work reports (DWRs).', with 'Inspectors collected and shared 1.9 times more observations while increasing the number of photo and other media observations' and 'submission rate improvements up to 66 percent completed within 24 hours and up to 82 percent completed within 72 hours.' The satisfaction score of 4 is the weakest number on this page and it is an estimate, since nothing about R&M's current field tooling is published. Torres cross-check: sizing is good but seasonal, market position is open (no Alaska competitor we checked publishes anything here), strategy fit is direct because 95% public clients means federal-aid reimbursement is the business."
  },
  {
   "job": "When I need something the firm already knows, a prior report, a spec approach, the boring log from the last job in that community, the person who ran it, I need to find it without knowing who to ask.",
   "pain_source": "Inferred from cited structure rather than stated by R&M, and labelled as such. The hook is the word research in the verbatim bullet 'Conduct research and write technical portions of proposals to assist in bringing in new work.' appearing on two different departments' postings, against a firm with 24 service lines, four offices, '100+ Employees' and 'Founded 1969'.",
   "current_workaround": "Asking a colleague, and searching a network drive by memory of the project name.",
   "importance": 8,
   "satisfaction": 3,
   "opportunity_score": 13,
   "notes": "Scores second, and the score flatters it. R&M has never said this hurts, so the push force is my inference. The pull force is loud because a direct competitor built exactly this: Michael Baker's Titan. A job where pull is strong and push is inferred is the precise shape of the pilot that MIT NANDA measured producing no P&L impact. CMMC Level 2 cuts both ways here, it is a genuine moat and a genuine constraint on where the corpus may be processed."
  },
  {
   "job": "When a deliverable is about to carry a licensed professional's stamp, I need it reviewed for feasibility, technical accuracy and quality before it leaves the building.",
   "pain_source": "Verbatim 'Review designs, plan drawings, engineering reports and other contract deliverables for feasibility, technical accuracy and quality.' on https://www.rmconsult.com/job-posting/senior-project-engineer/ , a seat requiring '15 or more years of experience in civil design work, with emphasis in highway and street design'.",
   "current_workaround": "A senior engineer's redline, by hand, on the most expensive hours in the firm.",
   "importance": 9,
   "satisfaction": 6,
   "opportunity_score": 12,
   "notes": "Scores high and is deliberately not the target, which is the clearest demonstration on this page that the numbers rank the debate rather than decide it. Cost of error lands on a professional stamp. ASCE Policy Statement 573 places that responsibility with the licensed engineer, the Ames & Gough 2026 survey found 80% viewing AI adoption by design firms as a potential disruptor with 60% reporting higher claim severity in 2025 up from 53%, and ISO/Verisk released three optional generative-AI exclusion endorsements effective January 2026. A narrow deterministic completeness checker is defensible here. A generative reviewer is not, and telling them so is worth more than selling it."
  },
  {
   "job": "When a senior seat sits open, I need the work that seat would have done to still get done, without burning out the people covering it.",
   "pain_source": "Eleven positions open at once across four offices per https://www.rmconsult.com/join-us/open-positions/ , including four senior seats and two surveying seats.",
   "current_workaround": "Existing staff absorb it, which is why the proposal-writing duty is stapled to senior technical seats in the first place.",
   "importance": 8,
   "satisfaction": 4,
   "opportunity_score": 12,
   "notes": "This is a cross-cutting condition rather than a standalone build target, and it is the demand-side reason the other jobs matter. Handle with care: no posting dates are published, so how long any role has been open is genuinely unknowable and any argument built on stale postings is unavailable to us. R&M is also #10 on Zweig Group's 2026 Best Firms To Work For in its size bracket for the 15th consecutive year, so this is a growth and scarcity story, never a distress story."
  },
  {
   "job": "When I am a senior engineer or surveyor with fifteen-plus years of design experience, I need to research and write the technical portions of a proposal so the firm brings in new work, without giving up the billable hours I was hired for.",
   "pain_source": "Verbatim and repeated across departments: 'Conduct research and write technical portions of proposals to assist in bringing in new work.' on both https://www.rmconsult.com/job-posting/senior-land-surveyor/ (Geomatics) and https://www.rmconsult.com/job-posting/senior-project-engineer/ (Engineering), plus 'Developing proposals.' alongside 'Producing cost estimates.' on https://www.rmconsult.com/job-posting/senior-environmental-geologist-or-engineer/ .",
   "current_workaround": "The senior person writes it, drawing on past proposals and project files, with the Marketing Group producing and assembling.",
   "importance": 8,
   "satisfaction": 5,
   "opportunity_score": 11,
   "notes": "The loudest cited signal in the file and deliberately not the target. Three reasons, all evidential. One, R&M announced Siobhan Johansen as Proposal Manager into the Marketing Group on July 14th 2026, twenty-four days before this study, so a live human fix is mid-installation and habit is at its freshest. Two, the function is already led by a 29-year FSMPS CPSM who specializes in proposal development. Three, the industry-analyst finding: proposal and SF330 automation is the loudest marketed pocket in this industry and the thinnest measured one, with every circulating figure vendor-published and mostly anonymised. Also note what we may not say: the claim that Michael Baker aimed Titan at proposal or capture work was dropped entirely after a 503 on four attempts, and the press release that did load does not mention proposals at all."
  },
  {
   "job": "When I write a NEPA document or a permit application, I need a defensible, correctly cited document that survives agency review.",
   "pain_source": "NEPA and Permitting are named service lines on https://www.rmconsult.com/what-we-do/ , and 'Writing technical reports and analyzing data.' is a verbatim duty on https://www.rmconsult.com/job-posting/senior-environmental-geologist-or-engineer/ .",
   "current_workaround": "Drafting from templates and prior documents by hand.",
   "importance": 7,
   "satisfaction": 5,
   "opportunity_score": 9,
   "notes": "Real and honestly capped. DraftNEPABench, 19 subject matter experts across 18 federal agencies, gives 'coding agents could save 1-5 hours per subsection, up to roughly a 15% reduction in drafting time', and a model vendor co-authored it so that is a ceiling under favourable conditions. The authors' own caveat about incomplete or out-of-date references matters more than the headline for a firm whose documents get litigated."
  },
  {
   "job": "When a public process generates hundreds of comments, I need a defensible comment and response record.",
   "pain_source": "Public Involvement and NEPA are both named service lines on https://www.rmconsult.com/what-we-do/ .",
   "current_workaround": "A spreadsheet, sorted and answered by hand.",
   "importance": 6,
   "satisfaction": 3,
   "opportunity_score": 9,
   "notes": "Genuinely well matched to what language models do well, classification and clustering with a person approving every response. Sizing is the limit, the work is bursty at a firm this size rather than continuous, so it belongs in a later lane rather than first."
  },
  {
   "job": "When I hold CMMC Level 2, I need continuous evidence that 110 controls are still in place, without it eating my IT group.",
   "pain_source": "Verbatim, 'CMMC Level 2 includes 110 controls based on NIST Special Publication 800-171 Revision 2', achieved December 22nd 2025 with Stratus Services, and Jere Fisher, Group Manager of IT, verbatim: 'The biggest challenge is time. If your in-house team lacks the required expertise, bring in outside support to get you started.'",
   "current_workaround": "An external partner, Stratus Services, plus the internal IT group.",
   "importance": 8,
   "satisfaction": 7,
   "opportunity_score": 9,
   "notes": "Low opportunity score because they solved it well and recently, with a named partner. Ongoing evidence burden is an assumption on my part, not a cited fact. The value of this item is not as a build, it is as the constraint every other build must satisfy: federal project data has to stay inside that certified boundary, which rules out the casual architecture and is why a shop that respects it wins here."
  },
  {
   "job": "When a public client needs money for a project, I need to turn their need into a fundable application against a specific notice of funding.",
   "pain_source": "Grant Writing is one of the 24 service lines on https://www.rmconsult.com/what-we-do/ .",
   "current_workaround": "A person, writing.",
   "importance": 6,
   "satisfaction": 5,
   "opportunity_score": 7,
   "notes": "The most interesting unpicked item on this page and the one with the least evidence. Unlike proposals this is billable delivery rather than overhead, so leverage here raises capacity in a revenue line. Nothing about grant volume, staffing or win rate is published, so it is a hypothesis, and it rides to the roadmap's later lane rather than into a candidate."
  },
  {
   "job": "When a specimen is broken or a gradation is run, I need the result into the report and the client's hands correctly.",
   "pain_source": "Materials Testing and Special Inspections are named service lines on https://www.rmconsult.com/what-we-do/ .",
   "current_workaround": "Lab forms and spreadsheets into a report template.",
   "importance": 6,
   "satisfaction": 5,
   "opportunity_score": 7,
   "notes": "Included so the map is honest rather than because it sells. Inputs are structured, stable and high-volume, which is the exact profile where deterministic automation is cheaper, exhaustively testable and safer than a model. The right answer here is that they do not need AI for it."
  }
 ],
 "target_opportunity": {
  "job": "Turning a day of field construction administration into a complete, dated, auditable project record that protects funding participation, done inside the Alaska construction season by a partly seasonal crew working across the state.",
  "why": "It tops the Ulwick ranking at 14 and it is the only job here standing on two independent legs. The pain leg is cited directly from R&M's own posting, 'Administer project documentation and audit trails to ensure funding participation', against a firm where nearly 95% of work is for public clients, which makes a documentation gap a reimbursement problem rather than a filing problem. The evidence leg is the single independent measurement in the entire file, Louisiana DOTD/LTRC with FHWA over 50-plus projects, where 'Inspectors using HeadLight experienced a 28 percent increase in productivity when creating and submitting daily work reports (DWRs).', with 1.9 times more observations collected and shared and submission rates up to 66 percent within 24 hours. Every other pocket in this industry is measured by vendors or not at all. I am explicitly declining the louder signal. The proposal-writing duty is the most quoted thing in this claims file and it appears in three senior postings, yet R&M installed a dedicated Proposal Manager into Marketing on July 14th 2026, the function is run by a 29-year FSMPS CPSM whose stated specialty is proposal development, and the industry-analyst found no named firm anywhere attached to a measured proposal-productivity number with a stated method. Arriving with a proposal tool four weeks into a new Proposal Manager's tenure, on vendor evidence, into a function that is already good, is how a build gets politely piloted and quietly dropped. Three honesty flags on the target itself. R&M's current field documentation tooling is not published, so the satisfaction score of 4 is an estimate. Their construction administration volume and field headcount are not published, so every reach figure below is a labelled assumption. Whether the owner agency dictates the system of record on federal-aid work is unknown and is the riskiest assumption in the whole analysis, which is why the candidates are shaped to feed a record system rather than replace one.",
  "forces": "Push is strong and specific: funding participation is named as a duty to administer, the season compresses the work into a few months, the crew includes seasonal hourly staff who re-onboard every spring, and a Construction Administration engineer seat is currently open so the load is being carried by someone else. Pull is the strongest available in this file, an independent FHWA co-sponsored 28 percent measured on this exact task, not a vendor slide. Anxiety is real and concentrated into one question, who owns the system of record on an agency project, plus connectivity on remote Alaska sites and whether a new record form survives an audit. Habit is moderate rather than fierce, since whatever they do today works well enough that the firm is thriving. The decisive factor is that this job has a natural annual switching moment, spring mobilization, when new seasonal staff are being onboarded anyway and a changed process costs the least it will ever cost. Push plus pull beats anxiety plus habit here, on the condition that the system-of-record question is answered before anyone builds, so it goes to a time-boxed spike rather than into a proposal. Compare that against the proposal opportunity, where habit was reinforced by a hire twenty-four days ago and anxiety includes two accomplished marketing professionals who will reasonably ask what evidence exists, and there is no honest answer that is not vendor-published."
 },
 "candidates": [
  {
   "name": "Field Record Copilot",
   "our_build": "Workflow automation, with a narrow language model on exactly two nodes",
   "what_it_does": "Mobile-first, offline-capable capture for construction administration staff on site. The inspector talks, photographs and taps rather than types, the system holds the project's pay items, contract documentation requirements and yesterday's context, and a fixed-step workflow turns the raw capture into a structured daily work report draft. The inspector reviews and approves before anything is a record, then the record exports in the format the owner's system of record ingests, so we feed the agency's record rather than fight it. The language model appears only where the input is genuinely messy, converting spoken and photographed observation into structured draft text, and flagging what today's contract requirements say should be documented and is not. Everything else is deterministic and exhaustively testable, which is the honest reading of the Louisiana evidence, where the winning system was workflow and capture automation with light ML rather than a large language model. It runs inside R&M's CMMC Level 2 boundary because federal project data has to.",
   "rice": {
    "reach": "About 25 field and construction administration staff across a roughly five-month season. ASSUMPTION, not a fact. R&M publishes '100+ Employees' and no breakdown, so this is estimated from Construction Administration, Materials Testing and Special Inspections being three of the 24 service lines plus one open seasonal CA engineer seat. R&M would correct this number in week one.",
    "impact": "2 (high). Anchored to a measured 28 percent productivity increase on this exact task, plus 1.9 times more observations collected and shared, from an independent FHWA co-sponsored study across 50-plus projects.",
    "confidence": "65%. High confidence that the mechanism works, since the evidence is independent and task-specific rather than vendor-published. Discounted hard for transfer risk, we do not know R&M's current tooling, their CA volume, or whether the owner agency dictates the record format on federal-aid projects.",
    "effort": "4 person-months",
    "score": "8.1"
   },
   "cost_of_delay": "HIGH and calendar-dated, the strongest in this set. The work only exists during the Alaska construction season and the posting confirms extended field periods during it. Building now cannot help the current season, which is nearly spent. A decision made through the winter deploys at spring mobilization, when new seasonal staff are onboarding anyway and the switching cost is at its annual minimum. A decision that slips past roughly March forfeits the entire 2027 season and the next opportunity is spring 2028, so delay here costs a full year of benefit rather than a few weeks."
  },
  {
   "name": "Documentation Gap Sentinel",
   "our_build": "Workflow automation, deterministic first, with one small language model node",
   "what_it_does": "No field app and no change to how anyone works. It reads the documentation already being produced on each active project and, before the pay estimate or progress submittal goes out, reports what the contract and funding requirements say must be documented and is not yet present. Rules do almost all of it, since documentation requirements are enumerable. A small language model node reads the unstructured narrative in existing reports to decide whether a required item was actually covered. Output is a per-project gap list with a person deciding what to do about it.",
   "rice": {
    "reach": "About 12 project managers and CA leads. ASSUMPTION on the same basis as above.",
    "impact": "2 (high). It attacks the funding-participation risk directly, which is the cited duty, and a single avoided disallowance is material.",
    "confidence": "60%. The duty is cited verbatim. We have zero evidence of any actual finding or disallowance at R&M and are not going to imply one, so the frequency of the thing it prevents is unknown.",
    "effort": "1.5 person-months",
    "score": "9.6"
   },
   "cost_of_delay": "MODERATE. It shares the seasonal clock, though closeout and pay estimates run past the field season, so it earns for more of the year than the field app does. No cliff."
  },
  {
   "name": "Project Record Assistant",
   "our_build": "Retrieval over their own files, scoped to one project's construction record",
   "what_it_does": "When a change order, a claim or a dispute arrives months later, this answers what the record actually shows, with a citation to the specific report, photo or entry, over a deliberately bounded corpus of one project rather than the whole firm. Bounded corpus is the honest way to do retrieval, since precision degrades as a corpus grows and the cure is better retrieval rather than more documents.",
   "rice": {
    "reach": "About 12 project managers and CA leads. ASSUMPTION.",
    "impact": "1 (medium). Large value when a claim happens, near zero otherwise.",
    "confidence": "50%. NEPAQuAD/MAPLE supports the retrieval mechanism, though it is a preprint rather than peer reviewed. Nothing published tells us how often R&M faces claims or record disputes.",
    "effort": "3 person-months",
    "score": "2.0"
   },
   "cost_of_delay": "LOW. Event-driven and unscheduled. It also gets strictly better the longer the Field Record Copilot has been feeding it structured records, which is an argument for sequencing it after, never instead."
  },
  {
   "name": "Pursuit Research Assistant",
   "our_build": "Retrieval over their own files plus the paperwork and proposal engine",
   "what_it_does": "For the senior engineer or surveyor whose posting says to conduct research and write technical portions of proposals, this returns R&M's own prior technical narrative, project descriptions and resumes with a citation to the source project, so the starting point is the firm's real prior text rather than a blank page. A person writes the actual narrative and the new Proposal Manager owns production.",
   "rice": {
    "reach": "About 20 senior technical staff across Geomatics, Engineering and Environmental, plus the Marketing Group, year-round rather than seasonal. ASSUMPTION on headcount split.",
    "impact": "1 (medium). Honest ceiling. No comparable measured figure exists to justify more.",
    "confidence": "35%, and this is the Confidence lever doing its intended job rather than a strawman. The industry-analyst worked vendor case studies, comparison sites, SMPS and ACEC channels and the trade press and found no named firm of any size attached to a measured proposal-productivity number with a stated method. Every circulating figure is vendor-published and mostly anonymised. Timing compounds it, since a Proposal Manager started July 14th 2026 and is establishing her own process now.",
    "effort": "3.5 person-months",
    "score": "2.0"
   },
   "cost_of_delay": "NEGATIVE, which is unusual enough to say plainly. Waiting improves this one. A new Proposal Manager needs a few months to set her own baseline, and arriving before that baseline exists means colliding with a live human fix and having no measurement to improve against afterwards. The right time to revisit this is after her process has run a full pursuit cycle."
  },
  {
   "name": "Firmwide Knowledge Assistant inside the CMMC boundary",
   "our_build": "Retrieval over their own files at firm scale, edging toward an agentic operating system",
   "what_it_does": "The direct answer to Michael Baker's Titan. One secure interface over R&M's 57 years of project records across four offices and 24 service lines, sitting inside the CMMC Level 2 boundary so federal project data never leaves it, which is a thing very few 100-person firms could even attempt.",
   "rice": {
    "reach": "100-plus, effectively everyone.",
    "impact": "1 (medium). Broad and shallow per person, and unmeasurable without a named task.",
    "confidence": "25%. R&M has never said finding its own knowledge is a problem, so the push force is inferred. Corpus readiness is unknown, CUI segregation inside the corpus is unknown, and no acceptance metric is nameable yet. This is the exact shape of the enterprise pilot that MIT NANDA measured producing no P&L impact.",
    "effort": "12 person-months",
    "score": "2.1"
   },
   "cost_of_delay": "LOW to MODERATE. Michael Baker announced Titan on April 16th 2026 and has a principal office at 3900 C St in Anchorage bidding the same agency work, which is genuine competitive pressure. There is no cliff, and note that reach alone is carrying this score, which is RICE's known weakness. Strip the 100-person reach and nothing here is ready to build."
  }
 ],
 "provisional_pick": {
  "name": "Field Record Copilot, whose first shippable slice is the Documentation Gap Sentinel",
  "why_over_others": "The Sentinel actually scores higher on RICE, 9.6 against 8.1, and the honest resolution is that it is not a rival, it is the walking skeleton of the same build. It touches the real data, proves the documentation requirements can be encoded and checked, and earns its keep on its own before anyone asks a field crew to change how they work. What it will not do alone is redesign the workflow, and workflow redesign is the one differentiator McKinsey found separating the firms that see EBIT impact from the roughly 80 percent that do not, so shipping only the Sentinel would buy a report nobody has time to act on. Pick the Copilot, sequence the Sentinel first, fund the second phase only when the first phase's actuals clear. Against Pursuit Research Assistant, 2.0, this is the comparison that matters most because the proposal pain is the loudest cited signal in the file. It loses on evidence and on timing, not on volume. The one independently measured productivity number available anywhere in this industry sits in field documentation, and the pocket the pain points at is the one the industry-analyst found loudest marketed and thinnest measured, with no named firm attached to a method. Timing seals it, R&M hired a Proposal Manager twenty-four days ago and the professional move is to let her process settle and measure it, not to sell over the top of it. Against Firmwide Knowledge Assistant, 2.1, reach is the only thing holding that score up. Twelve person-months, an unknown corpus, CUI mixed into it, and no acceptance metric we could state today. Against Project Record Assistant, 2.0, it is genuinely good and genuinely later, and it gets materially better once the Copilot has been producing structured records to retrieve over, so building it first would be building it on the worst possible corpus. What would change this pick. If the time-boxed spike finds that Alaska DOT and the other owner agencies mandate a field record system that R&M has no authority to feed or replace, the Copilot's export path collapses and the Sentinel becomes the whole build rather than its first phase. That question gets answered in a two-week spike before a line of production code, not after."
 },
 "pays_off": true
}
```


---

## Feasibility gate

```json
{
 "verdicts": [
  {
   "candidate": "Field Record Copilot",
   "lowest_tier": "workflow",
   "cost_of_error": "Low per event, high in aggregate, which is the profile a model can live with. A wrong word in a drafted daily report costs an edit, because the inspector approves before anything becomes a record, so the human gate is structural rather than advisory. The expensive error is the silent one, a required item never documented at all, and on work that is nearly 95 percent public-client that lands on funding participation. That error class belongs to the rule layer and never to the model. The coverage flag has to be tuned for recall, since a false 'you are missing a density test' costs ten seconds and a false 'all good' costs a reimbursement argument.",
   "data_readiness": "Half ready, half the project, and we should say which half. Pay items, contract documentation requirements and spec sections exist as documents today and are enumerable, so encoding them is work rather than research. Three things are unknown and load-bearing. Whether R&M has authority to feed or replace the field record on a federal-aid job, whether today's reports are exportable at all, and which projects actually carry CUI markings. 'Federal project data' is not a synonym for CUI, and R&M's own contracts settle that in an afternoon. Offline capture is the hardest control question in the build, since cached project data on a field device pulls in device management, encryption and media handling inside a boundary certified on December 22nd 2025 against 110 controls based on NIST SP 800-171 Rev 2. Any new in-scope system changes the asset inventory and the system security plan, so the assessor conversation happens before the build, not after it.",
   "step_math": "The model touches exactly two nodes, spoken and photographed observation into structured draft text, and a narrative coverage flag. Everything else is deterministic. At 0.90 per model step roughly 0.81 of drafts arrive needing no edit, at 0.95 roughly 0.90, and neither number is the safety number, since the inspector approves before a record exists. The number that matters is the residual, a required item that the rules miss and the reviewer also misses, which is bounded by rule coverage rather than by model recall. That is the whole argument for keeping enumerable requirements in rules. The design that fails the math is the one nobody should propose here, capture then transcribe then structure then classify then check then file then submit with no human, seven steps at 0.90 is roughly 0.48.",
   "verdict": "downscope",
   "change_or_reason": "Three specific changes. One, confine the model to the two genuinely messy nodes named above, keep every enumerable requirement in rules where it is exhaustively testable, and keep the export mapping into the owner's format deterministic, since a format is a contract. Two, stop attributing the 28 percent to AI. The Louisiana DOTD and LTRC result came from workflow and capture automation with light ML, so the deterministic layer carries the business case on its own and the model nodes get measured as a separate increment against it. Three, scope the pilot to projects R&M can name as non-CUI unless the contracts read says otherwise, and run the system-of-record question as a two-week spike before a line of production code."
  },
  {
   "candidate": "Documentation Gap Sentinel",
   "lowest_tier": "rules",
   "cost_of_error": "Asymmetric, and the design has to respect the asymmetry. A false flag costs a project manager a minute. A false clear manufactures confidence right before a pay estimate goes out and is worse than shipping nothing, because it replaces a person's own check with a machine's silence. So this tool never asserts completeness. It reports only the specific items it did not find, it names what it did not look at, and no screen in it ever says all clear.",
   "data_readiness": "This is where the 1.5 person-month estimate lives or dies, and the strategist attached the access risk only to the Copilot. Reading the documentation already being produced assumes it is reachable and machine readable. If today's daily reports and materials records sit as scanned PDFs, or inside an owner agency portal R&M has no export from, then extraction becomes the project and that estimate is wrong. It is the same unknown as the system-of-record question wearing different clothes, so it goes into the same spike.",
   "step_math": "Version one has ZERO model steps. Rules over structured fields are deterministic and exhaustively testable, so end-to-end reliability equals rule coverage, and rule coverage is something you can enumerate on a page and argue over with their own construction administration lead. Adding the narrative coverage node later puts one model step at roughly 0.85 to 0.90 on that single requirement class, tuned for recall. One step means no compounding, which is exactly why this is the right place to start.",
   "verdict": "downscope",
   "change_or_reason": "Ship version one with NO AI IN IT. The strategist put a small language model on the narrative node from day one and it is not earned yet, since the enumerable requirements are the bulk of the value and a rule does them cheaper, faster and testably. Add the narrative node only after the rule layer has run a real closeout cycle and somebody can point at the requirement types the rules keep missing. Also correct the label. Calling this the walking skeleton of the Copilot OVERSTATES what it retires, because it touches storage, rules and reporting while leaving the three riskiest components untouched, field capture, offline sync, and the export into the owner's record. It is a standalone Phase 1 that earns on its own and retires the data access risk, and the capture and export risks stay live until the spike answers them."
  },
  {
   "candidate": "Project Record Assistant",
   "lowest_tier": "retrieval",
   "cost_of_error": "Higher than it was scored. This gets used when a change order, a claim or a dispute is live, which is a contractual and sometimes legal setting, so a confident wrong answer can move a position R&M takes for money. The index itself is discoverable and has to respect legal hold. It returns documents and citations, never conclusions, and it never writes the summary that somebody later quotes into a claim position.",
   "data_readiness": "Worst corpus first if it is built now. Today's project record is unstructured and inconsistent by definition, which is the condition the recommended build fixes upstream. Nothing published tells us how often R&M faces a claim or a record dispute, so the frequency of the event this serves is unknown and is theirs to state, not ours to assume.",
   "step_math": "Two steps, retrieve then cite, so there is no compounding problem. On a deliberately bounded single-project corpus, hybrid search with reranking is the honest shape, and precision degrades as the corpus grows, which is the real argument for holding it to one project rather than the firm. Reliability is not the risk here. Value frequency is.",
   "verdict": "downscope",
   "change_or_reason": "Keep it, move it to the later lane, and rename what it is. It is an EVIDENCE LOCATOR, not a question answerer. Sequence it after the Copilot has been producing structured records to search over, since building it first means building it on the worst possible version of its own corpus. Two constraints ride with it, no generated conclusions in a claims context, and legal-hold-aware indexing."
  },
  {
   "candidate": "Pursuit Research Assistant",
   "lowest_tier": "rules",
   "cost_of_error": "Low, which is exactly why it is tempting. A person writes the narrative and a Proposal Manager owns production, so a bad suggestion costs a delete. The real cost here is not an error at all. It is arriving on top of a live human fix. R&M announced a Proposal Manager into the Marketing Group on July 14th 2026, twenty-four days before this study, into a function led by a 29-year FSMPS CPSM whose stated specialty is proposal development. Selling over the top of that is a political error rather than a technical one, and it is the more expensive kind.",
   "data_readiness": "Unknown in the way that decides the whole candidate. Whether R&M already keeps project descriptions and resumes in an A/E CRM is not published, and most firms in this bracket do. If it does, the blank page problem is content hygiene and search, not a model. If it does not, that library is the project, and it is a records job long before it is an AI job. Nothing about R&M's proposal volume, pursuit count, hours or win rate is published anywhere, so there is no baseline to improve against either.",
   "step_math": "Two steps, retrieve then draft, mechanically fine. It fails on evidence rather than on reliability. The industry read in this file found no named firm at any size attached to a measured proposal-productivity number with a stated method, and every circulating figure in this pocket is vendor-published and mostly anonymised, so there is no honest number to promise against.",
   "verdict": "downscope",
   "change_or_reason": "Downscope to NO AI and NO BUILD this year. The first move is the Proposal Manager's own baseline, four weeks of where the hours actually go, plus tagging and searching the prior narratives they already hold, which costs almost nothing and is useful whatever happens next. Revisit only after her process has run a full pursuit cycle and there is a measurement a build would have to beat. This is the loudest cited pain in the file, carried verbatim on three senior postings, so we SAY THE DECLINE OUT LOUD to R&M rather than quietly, otherwise it reads as though we missed it."
  },
  {
   "candidate": "Firmwide Knowledge Assistant inside the CMMC boundary",
   "lowest_tier": "retrieval",
   "cost_of_error": "Undefined, because the use is undefined. A system with no named task has no error definition and therefore no acceptance bar, which is the failure this whole discipline exists to prevent. The specific asymmetric risk is the certified boundary. One index spanning 57 years of records across four offices, with CUI and non-CUI mixed and no working classification, is an information flow problem inside a certification R&M paid for in December 2025. The downside is not a pilot that fizzles quietly. It is an incident in the one place this firm holds a moat.",
   "data_readiness": "Not ready and not close. Corpus condition unknown, CUI segregation unknown, access control model absent, freshness unaddressed, and no acceptance metric nameable today. Pointing retrieval at a document pile is on the industry kill list precisely because precision degrades as the corpus grows and enterprise use needs permissioning that nobody has built here yet.",
   "step_math": "As pitched, an operating layer with agent behaviour runs something like 8 to 15 steps of planning, tool choice, retrieval and synthesis. At 0.85 to 0.90 per step that is roughly 12 to 40 percent end to end, which no engineer should lean on anywhere near stamped work. Strip it back to one or two retrieval steps and the math is fine, though at that point it is search, and the benefit is still unnamed.",
   "verdict": "kill",
   "change_or_reason": "KILL as scoped. It is competitor envy driving scope, a direct answer to a platform announced by a firm with more than 6,000 engineers, architects and scientists across more than 120 office locations, and a 100-plus person firm copying a 6,000-person firm's platform economics is the transfer that does not survive contact. Reach alone is holding its RICE score up and the strategist admits it, so strip the reach and nothing here is ready to build. The agentic framing also needs naming honestly, since an internal library of purpose-built agents is language from a press release rather than a measured capability we may repeat. What survives the kill is not the platform. It is the observation that R&M's certified boundary is a real differentiator, which the recommended build uses quietly instead of announcing."
  }
 ],
 "recommended_pick": {
  "name": "Field Record Copilot, shipped as the Documentation Gap Sentinel first, with the model confined to two nodes and every enumerable requirement kept in rules",
  "why_it_survives": "It survives because it is the only candidate here whose value is measured by somebody with no product to sell. Louisiana DOTD and LTRC with FHWA, across 50-plus construction projects, measured a 28 percent productivity increase for inspectors creating and submitting daily work reports, and that finding sits on the same task R&M's own posting names, administer project documentation and audit trails to ensure funding participation. It survives the ladder because the bulk of it is deterministic and I am recommending it be built that way, with the model earning only the two nodes where the input is genuinely messy, a spoken observation and a narrative requirement. It survives cost of error because the inspector approves before anything becomes a record, so no model output reaches a funding file unreviewed. It survives the compounding math because there are two model steps and one human gate, not a chain. It survives on timing, since the work is seasonal and a decision made through the winter deploys at spring mobilization when new seasonal staff are onboarding anyway and switching cost is at its annual floor, while a decision that slips past roughly March forfeits a full year. It survives with one condition attached and I would not sign it without the condition. The two-week spike answers whether the owner agency dictates the field record system, and if the answer is that R&M has no authority to feed it, the export path collapses and the Sentinel becomes the entire build instead of its first phase. Saying that before the money moves is the difference between this and the 80 percent that fail."
 },
 "where_not_to_use_ai": "Four parts of this build stay deterministic on purpose. The enumerable documentation requirements, because a rule can be listed, argued over with your construction administration lead and tested exhaustively, while a model can only be sampled. The export mapping into the owner agency's record format, because a format is a contract and the same input has to produce the same output every time. Materials testing results, breaks, gradations and densities, which are structured, stable and high volume, the exact profile where deterministic automation is cheaper, safer and easier to defend than a model. Certified payroll, progress billing and subconsultant administration also stay in rules, since they run against published agency rules that change on a schedule rather than by judgment. One place gets NO generative AI at all. A deliverable about to carry a licensed professional's stamp does not get reviewed by a model. ASCE Policy Statement 573, adopted July 18th 2024, leaves that responsibility with the licensed engineer, the 2026 Ames and Gough survey of 15 A&E liability insurers found 80 percent viewing AI adoption by design firms as a potential disruptor with 60 percent reporting higher claim severity in 2025 up from 53 percent, and ISO and Verisk released three optional generative-AI exclusion endorsements effective January 2026, optional meaning each carrier chooses whether to attach them. A narrow deterministic completeness checker on a stamped deliverable is defensible. A generative reviewer is not, and telling R&M so is worth more to them than selling it.",
 "honest_flags": [
  "Every reach number in this candidate set is an assumption and none of them are ours to assert. About 25 field and construction administration staff, about 12 project managers and CA leads, about 20 senior technical staff. R&M publishes 100-plus employees and no breakdown, and no volume, hours, proposal count or win rate is published anywhere, so R&M supplies those numbers in week one and every ROI driver moves when they do.",
  "The 28 percent belongs to structured capture and workflow, NOT to a language model. The Louisiana system was workflow and capture automation with light ML, so anyone citing that number to justify a model node is misattributing it. The deterministic layer has to carry the business case alone and the model nodes get measured separately against it.",
  "The riskiest assumption in the whole analysis is still unanswered. Whether Alaska DOT and PF or another owner agency dictates the field record system on federal-aid work decides whether an export path exists at all. Two weeks, before code. If the agency owns the system and will not take a feed, the Copilot collapses to the Sentinel and the study has to say so rather than quietly reshape the pitch.",
  "CMMC is being used loosely across the candidate set and it needs tightening. A federal project is not automatically CUI, and which projects carry CUI markings is answered by R&M's own contracts, not by us. Any new in-scope system is a change to the asset inventory and the system security plan, so the assessor conversation belongs before the build. Offline mobile capture is the hardest control problem in the recommended build, and if the cached data is CUI then device management, encryption and media handling are real line items in the estimate rather than footnotes.",
  "The insurance question is live for any build with a generative node, not only for design review. ISO and Verisk issued three optional generative-AI exclusion endorsements effective January 2026, and optional means each carrier decides. R&M should ask its own carrier what is attached to its own policy before a generative node ships. We have no visibility into their policy and we should not pretend otherwise.",
  "Nothing published tells us R&M has ever had a funding disallowance, an audit finding or a record dispute, and we are NOT implying one. The Sentinel is insurance against a risk whose frequency at this firm is unknown, and that belongs in the ROI as a stated assumption with a range, never as a hero number.",
  "The Sentinel's 1.5 person-month estimate is contingent, not quoted. It assumes today's field documentation is reachable and machine readable. If it lives as scanned PDFs or inside an owner portal R&M has no export from, extraction becomes the project and that figure is wrong by a lot.",
  "We can't verify whether R&M already runs AI internally. The narrowed negative in the claims file covers one services page and one page of a paginated news index, nothing more. A firm can run AI internally and publish nothing, which is common in this sector, so no sentence anywhere may imply they are behind.",
  "No blanket federal rule requiring AI-use disclosure in an A and E proposal was found, so the study may not imply one exists. Disclosure obligations are solicitation-specific and R&M's own contracts people own that read.",
  "Whether R&M already owns an A and E CRM holding project descriptions and resumes is unverified, and that single unknown decides whether the pursuit candidate is an AI question or a content hygiene question. The claims file also forbids any suggestion that Michael Baker aimed Titan at proposal or capture work, since the only page that would have supported it never loaded."
 ]
}
```


---

## Engineering room, four agents verbatim

```json
{
 "pick": "Documentation Gap Sentinel, Phase 1 of the Field Record Copilot, rules only with zero AI",
 "ask": "12,000 dollars fixed fee, Phase 1 only, split 4,000 at Gate A and 8,000 at Gate B",
 "prd": {
  "problem": "R&M's own posting for a Project Civil Engineer in Construction Administration names the duty as \"Administer project documentation and audit trails to ensure funding participation\". At a firm where nearly 95 percent of the work is for public clients, that sentence is about money rather than filing. An item that never made it into the record is a reimbursement argument, not a paperwork chore. The people carrying that duty are doing it from project locations across the state during the construction season, on a posting the firm classifies Seasonal, Full-Time, Hourly, alongside the requirement that \"Travel within Alaska will be required, and the ideal candidate must be willing to work in project locations throughout the state for extended periods of time during construction season.\" The crew that has to know every documentation requirement is partly a crew that re-onboards every spring, and one Construction Administration engineer seat is open right now, so the load is being carried by somebody else in the meantime. We want to be exact about what we do not know, because it changes how this proposal is written. Nothing published tells us how many pay estimates or progress submittals R&M reconciles in a year, how long one takes, how many people sit in construction administration, or what field tooling R&M uses today. Nothing published says R&M has ever had a disallowance, an audit finding or a record dispute, and we are not implying one. What is published is the duty, the public-client mix that makes the duty expensive when it slips, and the seasonal shape that decides when a change is cheap. The reason to decide now is the calendar rather than the technology. The work only exists during the season, the 2026 season is nearly spent, and a decision taken through the winter lands at spring mobilization when seasonal staff are being onboarded anyway and a changed process costs the least it ever will. A decision that slips past roughly March 2027 forfeits the 2027 season, and the next natural moment is spring 2028.",
  "after_state": "Before a pay estimate or a progress submittal leaves R&M, the project manager gets a short list naming the specific documentation items that project's own contract requires and that are not in the file yet, next to a plain statement of what the check did not look at, so a gap gets closed while the crew is still on site instead of surfacing at closeout. Nobody in the field changes how they work for that to happen.",
  "goals": [
   "Answer the three questions that decide whether any of this is buildable, inside two weeks and before a line of production code: whether an owner agency dictates the field record system on R&M's federal-aid work and whether R&M has authority to feed it, whether today's construction documentation is reachable and machine readable, and which projects carry CUI markings under R&M's own contracts.",
   "Put a real baseline in R&M's hands, measured by R&M's own project managers over four weeks on named pilot projects, so that every number this proposal is later judged against belongs to R&M rather than to us. Every driver we used to size the ask is an assumption, and this goal replaces the assumptions with measurements.",
   "Run a completeness check against the contract documentation requirements on two or three live projects, ahead of the pay estimate or progress submittal, reporting only the specific items it did not find and naming what it did not look at.",
   "Require zero change to how field and seasonal staff work in Phase 1. No field app, no new habit, no training a seasonal crew. Adoption is the usual way a build like this dies, and Phase 1 sidesteps it by not asking for adoption.",
   "Leave the encoded requirement list with R&M as a plain, readable, editable artifact their construction administration lead can argue with line by line, whether or not anything further is ever built."
  ],
  "non_goals": [
   {
    "item": "The tool never asserts completeness. It reports only the specific items it did not find, it names the requirement classes and the document types it did not look at, and no screen in it ever says all clear.",
    "reason": "The error costs are asymmetric. A false flag costs a project manager a minute. A false clear manufactures confidence right before a pay estimate goes out and replaces a person's own check with a machine's silence, which is worse than shipping nothing at all."
   },
   {
    "item": "No model of any kind in Phase 1. Not a large one, not a small one, not on the narrative, not anywhere.",
    "reason": "Documentation requirements are enumerable, so a rule does them cheaper, faster and testably. A rule can be listed on a page, argued over with your construction administration lead and tested exhaustively. A model can only be sampled. The model node earns its place later or never, and only once somebody can point at the requirement types the rules keep missing."
   },
   {
    "item": "Nothing carrying a licensed professional's stamp is reviewed by this tool, and no generative review of stamped work is on this roadmap at any phase.",
    "reason": "ASCE Policy Statement 573, adopted July 18th 2024, holds that \"The civil engineer must maintain responsibility for project planning, designing, building, operations, maintenance, and the protection of the public health, safety, and welfare\". The 2026 Ames and Gough survey of 15 A&E liability insurers found 80 percent viewing AI adoption by design firms as a potential disruptor, with 60 percent reporting higher claim severity in 2025, up from 53 percent the prior year. A narrow deterministic completeness check on a deliverable is defensible. A generative reviewer is not, and telling you so is worth more than selling it to you."
   },
   {
    "item": "This is not a replacement for an owner agency's system of record, and Phase 1 writes nothing into one.",
    "reason": "On federal-aid work the agency may own the record and may not accept a feed at all. Phase 1 reads what R&M already produces and reports to R&M's own people. We would rather feed an agency's record later than fight it, and we will not know which is possible until the Gate A spike answers it."
   },
   {
    "item": "No field capture, no offline sync, no mobile app, and no export into any external record in Phase 1.",
    "reason": "Those are the three riskiest components in the eventual build and none of them is retired by Phase 1. Bundling them in would make the estimate a guess, and offline cached project data on a field device pulls in device management, encryption and media handling inside a boundary R&M had certified on December 22nd 2025."
   },
   {
    "item": "Not proposal or pursuit tooling, and we are declining that deliberately rather than missing it.",
    "reason": "It is the loudest signal in your own public material, carried verbatim on two departments' senior postings as \"Conduct research and write technical portions of proposals to assist in bringing in new work.\" and on a third as \"Developing proposals.\" We are declining it for three evidential reasons. R&M announced a Proposal Manager into the Marketing Group on July 14th 2026, so a live human fix is mid-installation. The function is led by a 29-year FSMPS CPSM whose own bio names proposal development as a specialty. Our industry read worked vendor case studies, comparison sites, SMPS and ACEC channels and the trade press and found no named firm at any size attached to a measured proposal-productivity number with a stated method, so there is no honest number we could promise against. It is the loudest marketed pocket in this industry and the thinnest measured one."
   },
   {
    "item": "No firmwide search across R&M's records, four offices or 24 service lines.",
    "reason": "Corpus condition is unknown to us, CUI segregation inside it is unknown, and no acceptance measure is nameable today. A 100-plus person firm copying a 6,000-person firm's platform economics is the transfer that does not survive contact, and the reach of an idea is not a reason to build it."
   },
   {
    "item": "No CUI-marked project inside the Phase 1 pilot unless R&M's contracts people direct otherwise, and no new system stood up inside the certified boundary before the assessor conversation happens.",
    "reason": "A federal project is not automatically CUI. R&M's own contracts settle which projects carry the markings, not us. Any new in-scope system changes the asset inventory and the system security plan, so that conversation belongs before the build rather than after it."
   }
  ],
  "metrics": [
   {
    "metric": "Hours spent per pay estimate or progress submittal locating and reconciling documentation against contract requirements, on the pilot projects.",
    "baseline": "Unknown to us and nowhere published. ASSUMED at roughly 2.0 hours per reconciliation for sizing the fee only, and that assumption has no standing once a measurement exists. What we would measure: R&M's project managers on the pilot projects log the time per submittal for four weeks, on a one-page tally we supply and they own.",
    "target": "A 25 to 40 percent reduction against R&M's own measured baseline. If the measured baseline lands below the 2.0 hours we assumed, the target moves down with it and we say so in the Gate B readout, rather than holding a percentage that flatters us against a number that turned out smaller.",
    "timeframe": "Baseline collected weeks 1 to 4. Target judged at 90 days of live use, counted from the week 8 Gate B delivery."
   },
   {
    "metric": "Count of documentation items that had to be chased, reconstructed or reissued after a submittal went out, or at project closeout, on the pilot projects.",
    "baseline": "Unknown and deliberately not assumed, because guessing this one would be guessing at how well R&M already does its job. What we would measure: R&M records one line per such item on the same four-week tally, with the project and the requirement named.",
    "target": "30 to 50 percent fewer such items, with the reduction showing up as items raised before the submittal rather than after it. A drop in the after-the-fact count with no matching rise in the before-submittal count would mean the rules are missing things, not that things stopped being missed, and we would report it that way.",
    "timeframe": "Baseline weeks 1 to 4. Target judged at 90 days of live use."
   },
   {
    "metric": "Rule coverage and misses. Coverage is the share of the documentation requirement list agreed with R&M's construction administration lead that the Sentinel actually checks. A miss is a requirement that is on that agreed list, is genuinely absent from the project file, and that the Sentinel failed to report.",
    "baseline": "Zero coverage at kickoff, and this baseline is a fact rather than an estimate, because nothing is encoded on day one and the agreed list does not exist yet.",
    "target": "Every requirement on the agreed list is either checked by the Sentinel or named in the report as not checked, with no third category. Zero misses across a back test of at least 10 already completed submittals from the pilot projects, or every completed submittal those projects have if there are fewer than 10, scored against an R&M reviewer working the same list by hand.",
    "timeframe": "Scored at Gate B exit in week 8, and re-scored at 90 days against that period's live submittals."
   },
   {
    "metric": "Change demanded of field and seasonal staff, measured as hours of training required and the count of new tools any field person has to log into.",
    "baseline": "Zero at kickoff, since no such tool exists today. The commitment is that it stays at zero, which is what makes this falsifiable rather than decorative.",
    "target": "Zero training hours and zero new logins for any field or seasonal person through week 8. If Phase 1 turns out to need either, we have broken the design promise and we report it as a failure of the design, not as a scope change.",
    "timeframe": "Checked at Gate B exit, week 8."
   }
  ],
  "phase1_must": [
   "Gate A, weeks 1 and 2, the spike, and it is a real stop point. Three questions answered in writing: does an owner agency dictate the field record system on R&M's federal-aid projects and does R&M have authority to feed it, is today's construction documentation reachable and machine readable, and which projects carry CUI markings under R&M's own contracts. R&M can stop at week 2, keeps the memo and the baseline instrument, and pays only the 4,000 dollar Gate A portion of the 12,000 dollar fixed fee.",
   "The baseline instrument, delivered in week 1. One page, roughly ten minutes per submittal, definitions written down so two project managers count the same thing the same way. It starts in week 1 and completes in week 4.",
   "Requirement encoding sessions with R&M's construction administration lead in weeks 3 and 4, producing a written, numbered list of the documentation requirements for the pilot projects, marked line by line as checked or not checked. That list is the acceptance artifact and R&M keeps it whatever happens next.",
   "Gate B, weeks 3 to 8, the Sentinel itself, rules only, no model. It reads the documentation R&M already produces on two or three named live projects and reports, ahead of the pay estimate or progress submittal, the specific required items it did not find.",
   "The report format, which is half the product. Missing items only, each tied to the numbered requirement and the project, with an explicit closing statement of what this check did not look at. No completeness assertion anywhere in it.",
   "A back test before it goes live, against already completed submittals from the pilot projects, scored against an R&M reviewer working the same list by hand.",
   "The Gate B readout in week 8, comparing what the four-week baseline measured against what the first weeks of live use show, with the 90-day measurement plan and a named R&M owner for the number.",
   "Handover of everything: the rule list, the report definitions, the spike memo and the baseline data, in a form R&M can maintain without us."
  ],
  "phase1_later": [
   "LATER, not in Phase 1: the narrative coverage check, which is the single place a small model would earn a role. It only gets proposed after the rule layer has run a real closeout cycle and somebody at R&M can point at the requirement types the rules keep missing. Until that list exists, the model is unearned.",
   "LATER: structured field capture with offline sync for construction administration staff on remote sites. This is the hardest control problem in the whole idea, since cached project data on a field device pulls in device management, encryption and media handling, and it is not attempted before the CUI question is settled.",
   "LATER, and conditional: export of the completed record into the owner agency's system in the format that system ingests. If the Gate A spike finds that the agency owns the record and will not take a feed, this never happens, the eventual Field Record Copilot loses its export path, and the Sentinel becomes the entire build rather than its first phase. We are saying that now rather than reshaping the pitch afterwards.",
   "LATER: an evidence locator over one project's construction record, for the moment a change order, a claim or a dispute arrives months later. It returns documents and citations, never conclusions, it respects legal hold, and it gets materially better once structured records exist to search over, which is why building it first would be building it on the worst possible version of its own corpus.",
   "LATER, and honestly low value: comment and response handling for public involvement work, which fits the machinery well and is bursty rather than continuous at a firm this size.",
   "NOT ON THIS ROADMAP AT ALL: proposal and pursuit tooling, firmwide search, and any generative review of stamped work."
  ],
  "need_from_you": [
   "Two or three named active projects for the pilot, chosen by you, plus a one-line confirmation from your contracts people that those projects carry no CUI markings, or an instruction to include one and treat it accordingly. This is the single item that most affects the schedule.",
   "Your construction administration lead, roughly 6 to 8 hours total across weeks 3 and 4, to enumerate and argue the documentation requirement list. This is the highest-value hours in the engagement and there is no substitute for that person.",
   "The contract documentation requirements for those projects: the relevant spec sections, the pay item list, and whatever owner documentation manual the projects run under.",
   "Read access to where today's daily reports, materials records and submittal backup actually live, in whatever form they are, plus a named IT contact to arrange it. Scans are an answer we can work with, and Gate A exists partly to find out.",
   "Your project managers on the pilot projects, roughly ten minutes per submittal for four weeks, to fill the baseline tally. Without four weeks of it, the 90-day targets can't be judged and we will say so rather than substitute our own assumption.",
   "One 45-minute conversation with your IT group about whether anything in Phase 1 is in scope for your certified boundary, and, if it is, a short conversation with whoever supports your CMMC posture before anything is stood up.",
   "One named person on your side who owns the number after handover and compares actuals to baseline at 90 days. A metric with no owner stops being measured within a month.",
   "A yes or no from Len Story at the end of week 2 on whether Gate B proceeds."
  ],
  "risks": [
   {
    "risk": "An owner agency dictates the field record system on federal-aid work and R&M has no authority to feed it. This is the riskiest assumption in the entire analysis and it is unanswered today.",
    "mitigation": "It is answered in the two-week Gate A spike, before a line of production code and before most of the money moves. If the answer is that the agency owns the record and will not accept a feed, we tell you at week 2, the export path for the eventual Copilot collapses, and the Sentinel becomes the whole build rather than its first phase. Phase 1 itself still works in that world, since it reads what you produce and reports to your own people, and you would be deciding with the answer in hand instead of paying for a discovery later."
   },
   {
    "risk": "Today's documentation is not reachable or not machine readable. If daily reports and materials records sit as scanned PDFs, or inside an owner portal R&M has no export from, extraction becomes the project and the effort estimate behind this fee is wrong by a lot.",
    "mitigation": "The 1.5 person-month estimate under this fee is contingent on machine-readable source documents, and we are saying so before you sign rather than after. Gate A checks it directly. If extraction turns out to be the project, we say so at week 2, you stop there with the spike memo and the baseline in hand, the Gate B portion is not billed, and we would come back with a differently shaped and differently priced proposal or with a recommendation not to do it."
   },
   {
    "risk": "A false clear. The tool reports nothing missing, a person trusts it, and a required item goes out undocumented, which is a worse outcome than never having built it.",
    "mitigation": "The design refuses the failure rather than managing it. The tool never asserts completeness, it reports only what it did not find, every report names what the check did not look at, and no screen says all clear. Phase 1 is rules only, so coverage is enumerable on a page and testable exhaustively, and the acceptance bar at week 8 is zero misses on a back test against your own reviewer working the same list by hand."
   },
   {
    "risk": "CMMC scope creep. A new system touching project data could change the asset inventory and the system security plan behind a Level 2 certification achieved on December 22nd 2025 against 110 controls based on NIST SP 800-171 Revision 2.",
    "mitigation": "We treat the boundary as a constraint rather than a footnote. A federal project is not automatically CUI, and which of your projects carry the markings is answered by your own contracts and not by us, which is why it is one of the three Gate A questions. The pilot is scoped to projects you name as non-CUI unless your contracts read says otherwise, and the conversation about in-scope systems happens before the build, not after it."
   },
   {
    "risk": "We anchor on a measured number from somewhere else and it does not transfer. The one independent measurement in this whole field is Louisiana DOTD and LTRC with FHWA over 50-plus projects, where \"Inspectors using HeadLight experienced a 28 percent increase in productivity when creating and submitting daily work reports (DWRs).\"",
    "mitigation": "We are not promising you that number and it is not the target in this document. It is a different firm, a different agency and a different system, and the system that produced it was workflow and capture automation with light machine learning rather than a language model, so nobody should cite it to justify a model. It sets direction. Every target above comes from a baseline your own people measure."
   },
   {
    "risk": "The thing this tool insures against may be rare at R&M. Nothing published says you have ever had a disallowance, an audit finding or a record dispute, and we are not implying one, so the frequency of the event is genuinely unknown to us.",
    "mitigation": "The business case rests on recovered hours in reconciliation and closeout, which are the drivers your four-week baseline measures. Avoided-disallowance value is carried as a stated range with the assumption named, never as the headline number, and if your own history says the event is rare, the case is the hours case and we would tell you to judge it on that alone."
   },
   {
    "risk": "The baseline never actually gets collected, which is the most common way an engagement like this quietly loses its ability to prove anything.",
    "mitigation": "The instrument is one page and roughly ten minutes per submittal, delivered in week 1 so collection starts before any build. If fewer than four weeks of records exist by week 4, we say in the Gate B readout that the 90-day targets can't be judged, rather than filling the hole with our own assumption and calling it a result."
   },
   {
    "risk": "It underperforms. At 90 days the measured reduction lands below the low end of the range.",
    "mitigation": "That is the finding and the roadmap stops there. We do not fund a later phase on a phase whose actuals did not clear, and the gates exist for exactly that. You keep the spike answers, the requirement list, the baseline data and the running check whatever the number says, and the fee is fixed, so the overrun risk on Phase 1 is ours rather than yours. The honest outside view is that most builds in this category do not produce a measurable result, which is why this one is small, gated and measured against a baseline you own."
   },
   {
    "risk": "Rules go stale. Spec sections and agency documentation manuals change, and a requirement list nobody maintains slowly turns into a machine that reports the wrong gaps.",
    "mitigation": "The rule list is plain, numbered and editable by design, and naming its maintenance owner at R&M is a Gate B exit condition rather than a nice-to-have. If no owner is named, we would say the tool has a shelf life and put that in the readout."
   },
   {
    "risk": "Liability exposure around generative tools in design firms is tightening. ISO and Verisk released three optional generative-AI exclusion endorsements effective January 2026 for commercial general liability, and optional means each carrier chooses whether to attach them.",
    "mitigation": "Phase 1 has no generative component at all, so those endorsements are not in play for what we are proposing. Before any later phase adds one, R&M should ask its own carrier what is attached to its own policy. We have no visibility into your policy and we are not going to pretend otherwise."
   }
  ],
  "open_questions": [
   {
    "q": "Does Alaska DOT and PF, or another owner agency, dictate the field record system on your federal-aid projects, and do your contracts give R&M authority to feed or replace it?",
    "owner": "R&M contracts and construction administration leads, with us, inside the Gate A spike in weeks 1 and 2. This is the question that decides whether Phase 1 is a first phase or the whole build."
   },
   {
    "q": "Is today's construction documentation reachable and machine readable, or does it live as scans and inside an owner portal with no export?",
    "owner": "R&M IT with us, Gate A. The effort estimate behind this fee depends on the answer."
   },
   {
    "q": "Which projects actually carry CUI markings?",
    "owner": "R&M's own contracts people. This is settled by reading your contracts and is not ours to determine."
   },
   {
    "q": "Does standing up anything in Phase 1 put a new system in scope for your certified boundary, and if so what does your assessment require before it runs?",
    "owner": "R&M IT, with whoever supports your CMMC posture. Answered before the build, not after."
   },
   {
    "q": "Which two or three active projects are the pilot, and which document classes are in scope, daily reports and pay estimate backup only, or materials testing and special inspection records as well?",
    "owner": "R&M's construction administration lead, at the requirement encoding sessions in weeks 3 and 4."
   },
   {
    "q": "How many pay estimate and progress submittal reconciliations does R&M actually run in a year, how long does one take, and how many closeouts happen annually? Every driver we used to size this ask is an assumption on all three.",
    "owner": "R&M project managers, through the four-week baseline. We would rather be corrected in week one than be right by accident."
   },
   {
    "q": "Who owns the number after handover, and who maintains the requirement list as spec sections and agency manuals change?",
    "owner": "R&M, named at Gate B exit in week 8."
   },
   {
    "q": "If the spike finds the owner agency owns the record and will not take a feed, does the Sentinel still justify itself for R&M on its own?",
    "owner": "Len Story, at the Gate A decision in week 2, with our written recommendation in front of him either way."
   }
  ]
 },
 "design": {
  "one_liner": "Build a rules-only Documentation Gap Sentinel that reads the project documentation R&M already produces and, before each pay estimate and at closeout, reports the specific contract-required items it did not find plus everything it was unable to look at, so a gap in the funding audit trail is caught by a person while there is still time to fix it.",
  "architecture": {
   "nodes": [
    {
     "id": "sources",
     "label": "R&M project records (daily reports, materials records, pay estimate packets on the R&M file share)",
     "kind": "system"
    },
    {
     "id": "agency",
     "label": "Owner agency record system (Alaska DOT&PF or whichever agency the contract names), read only, access confirmed at Gate A",
     "kind": "external"
    },
    {
     "id": "intake",
     "label": "Record Intake Service (read only connectors, writes nothing back, produces a per-run file manifest)",
     "kind": "build"
    },
    {
     "id": "rulebook",
     "label": "Requirement Rulebook (one YAML file per contract, versioned in git, each rule cites its spec section)",
     "kind": "data"
    },
    {
     "id": "engine",
     "label": "Gap Engine and Coverage Ledger (deterministic rules over PostgreSQL, zero model steps)",
     "kind": "build"
    },
    {
     "id": "report",
     "label": "Gap Report (missing items plus a named list of what was not examined, never an all clear)",
     "kind": "build"
    },
    {
     "id": "pm",
     "label": "R&M project manager and construction administration lead (owns the rulebook, reads the report)",
     "kind": "user"
    }
   ],
   "edges": [
    {
     "from": "sources",
     "to": "intake",
     "label": ""
    },
    {
     "from": "agency",
     "to": "intake",
     "label": ""
    },
    {
     "from": "intake",
     "to": "engine",
     "label": ""
    },
    {
     "from": "rulebook",
     "to": "engine",
     "label": ""
    },
    {
     "from": "engine",
     "to": "report",
     "label": ""
    },
    {
     "from": "report",
     "to": "pm",
     "label": ""
    },
    {
     "from": "pm",
     "to": "rulebook",
     "label": ""
    }
   ],
   "caption": "Phase 1 of the Documentation Gap Sentinel, end to end. The highlighted boxes are the work we would do. There is no model anywhere in this diagram, because Phase 1 has none by design, and every documentation requirement lives in rules your own construction administration lead can read and argue with. The later phases attach at exactly two points, field capture ahead of the Record Intake Service and a narrative coverage check beside the Gap Engine, and neither is switched on here."
  },
  "build_vs_buy": [
   {
    "component": "Record Intake Service, the read only connectors to R&M project folders",
    "decision": "build",
    "why": "No vendor sells a reader for R&M's own project numbering, folder conventions and pay estimate packet layout, and the defining property of this component is that it writes nothing back to any source. It is thin, a few hundred lines of glue sitting on bought parsing libraries, and it earns its keep by producing the per-run file manifest that the safety story depends on."
   },
   {
    "component": "Document text extraction (Apache Tika, pdfplumber, openpyxl) and on premise OCR (OCRmyPDF with Tesseract)",
    "decision": "buy",
    "why": "Parsing is a solved commodity and writing our own is pure waste. These run as libraries inside R&M's own boundary, which matters, because shipping project documents to a hosted extraction API would move data outside an assessed environment for no benefit."
   },
   {
    "component": "Requirement Rulebook format and the Gap Engine",
    "decision": "build",
    "why": "This is the differentiator and the only real intellectual property in Phase 1. The rules are R&M's own contract documentation requirements written down so they can be listed on a page, argued over with the construction administration lead, and tested exhaustively. A commercial checker encodes its own vendor idea of a requirement against a generic contract, which is precisely the thing that fails an agency review of an Alaska federal aid job."
   },
   {
    "component": "Coverage and Unexamined Manifest",
    "decision": "build",
    "why": "This is the safety component and it has no market. Every checker on the market reports what it found. The failure that would hurt R&M is what it never looked at, so the manifest names every folder, file and format the run skipped, and it prints on the report itself rather than hiding in a log."
   },
   {
    "component": "Relational store, PostgreSQL",
    "decision": "buy",
    "why": "It holds pointers, file hashes, extracted field values and run history. Ordinary relational work, open source, already familiar to any IT group, and it runs wherever R&M IT puts it."
   },
   {
    "component": "Hosting and runtime",
    "decision": "buy",
    "why": "Use infrastructure that already sits inside R&M's assessed boundary, selected by R&M IT with Stratus Services. A new cloud tenancy would be a new in scope system, which changes the asset inventory and the system security plan, so the cheapest and safest architecture is the one that adds no new boundary at all."
   },
   {
    "component": "Identity and access",
    "decision": "buy",
    "why": "Reuse R&M's existing directory and single sign on. A second user store inside a boundary certified against 110 controls is a liability rather than a feature, and the Sentinel has no external users to justify one."
   },
   {
    "component": "Report rendering, HTML plus WeasyPrint for PDF",
    "decision": "buy",
    "why": "A gap report is a document. Rendering it is commodity work and the PDF has to survive being emailed and filed, which these tools already do."
   },
   {
    "component": "Scheduling, systemd timers or R&M's existing job scheduler",
    "decision": "buy",
    "why": "The cadence is one run per project per pay estimate cycle plus one at closeout. That does not earn a workflow platform, and an unnecessary platform is another in scope component to document."
   },
   {
    "component": "Export mapping into an owner agency record format (Phase 2 or later, and only if Gate A says a feed is permitted)",
    "decision": "build",
    "why": "A format is a contract, so the same input has to produce the same output every time, with a golden file test per field and a version pinned to the agency's own spec. This stays deterministic forever. No model touches it."
   },
   {
    "component": "Field capture and offline sync (Phase 2)",
    "decision": "buy",
    "why": "Evaluate commercial construction field record products before writing a line of capture code. The independent Louisiana DOTD and LTRC study, co sponsored by FHWA across 50 plus projects, measured one such product, HeadLight, and the honest read is that capture, offline sync and photo handling are the three riskiest components in the whole Copilot. Paying someone else to own them beats owning them, if a product clears the boundary and export questions."
   },
   {
    "component": "Base language model (Phase 3 only, one narrow node)",
    "decision": "buy",
    "why": "Nobody should train a model for this, and in Phase 1 nobody should run one either. The only defensible use is a single narrative coverage check tuned for recall, added after the rule layer has run a real closeout cycle and someone can point at the requirement types the rules keep missing."
   }
  ],
  "cross_cutting": {
   "auth": "No new user store. The Sentinel authenticates people against R&M's existing directory and single sign on, and it reaches sources through a read only service account scoped to named project folders, one account per pilot project rather than one account with everything. Three roles only. A reader sees gap reports for projects they are on, a rulebook owner (the construction administration lead) approves rule changes, and an operator runs and re deploys. Rulebook edits land through a git pull request with a named approver, so every rule change carries an author, a date and a reviewer. There is no internet facing surface and no external user, which keeps the access control model small enough to describe in the system security plan in one paragraph.",
   "data_security": "The whole system sits inside the boundary R&M certified at CMMC Level 2 on December 22nd 2025, which covers 110 controls based on NIST Special Publication 800-171 Revision 2. Nothing leaves it. No hosted API call, no telemetry to us, no copy of a project document on our machines. The store holds pointers, hashes, extracted field values and run history rather than copies of documents, which keeps the data footprint small on purpose. A new in scope system changes the asset inventory and the system security plan, so the conversation with R&M IT and Stratus Services happens inside Gate A, before any build. A federal project is not automatically CUI, and which projects carry CUI markings is answered by R&M's own contracts rather than by us, so the Phase 1 pilot runs on projects R&M can name as non CUI unless their contracts read says otherwise. Logs carry file paths and rule identifiers, never document content. Our own access during the engagement is through R&M's controlled path or a screen share, and the deliverable is code and rules in their repository.",
   "observability": "Every run writes a signed run record holding the rulebook version, the source paths read, the count of files read, the count of files unreadable and why, the rules evaluated, and the gaps raised. Three numbers get tracked weekly and shown to the owner. Precision, the share of raised gaps the project manager confirms were real. The miss log, gaps a person found that the Sentinel did not raise, which is the number that actually decides whether this tool is trustworthy. Coverage, the share of the contract's enumerable requirements that have a rule at all, stated as a fraction rather than as a percentage of an unknown whole. Every rule carries a golden file regression test built from a real closed packet, so a rule change that breaks an old case fails before it ships. The four week baseline that starts in Gate A is what any later phase gets measured against.",
   "failure_modes": "The named worst case is a false clear, a run that stays quiet on a project it never properly read. Three things hold that line. The tool never asserts completeness, no screen in it says all clear, and the report leads with what was not examined before it lists what was missing. A source that is unreachable produces a loud unexamined entry rather than a clean report. A file that fails to parse becomes an unexamined item, never a passed item. Second failure mode, a stale rulebook, where a contract amendment moves a requirement and the rules keep checking the old one. Rules are pinned to a contract version, each cites its spec section, and the report prints the rulebook version it ran. Third, alert fatigue, where a long list gets ignored. Rules are scoped per project, gaps dedupe within a pay estimate cycle, and the list sorts by the deadline it threatens. Fourth, the corpus turns out to be scanned images or lives inside an agency portal with no export, in which case extraction becomes the project. Gate A finds that before money is committed, and it triggers a re price or a stop rather than a silent overrun."
  },
  "goals": [
   "Ahead of each pay estimate or progress submittal, and again at closeout, produce a per project list of the specific contract required documentation items the rules did not find, each item naming its source requirement and the exact places that were searched.",
   "Print, on the same report, a named list of everything the run was unable to examine, so the reader always knows the shape of the tool's blind spot.",
   "Keep every documentation requirement in rules that R&M's construction administration lead can read line by line, dispute, and see tested against real closed packets. Zero model steps in Phase 1.",
   "Require no change whatsoever to how field or office staff work. No app to install, no new habit, no training for a seasonal crew.",
   "Run entirely inside R&M's existing assessed boundary, adding no new external data path and no new user store.",
   "Answer the three Gate A questions in writing, whether or not Phase 2 ever happens, and hand R&M the answers, the project matrix and the draft rulebook as their property.",
   "Establish a four week baseline on one named document class so any later phase is measured against a real number rather than an asserted one."
  ],
  "non_goals": [
   {
    "item": "Asserting that a project's documentation is complete, or showing any all clear state",
    "reason": "A false flag costs a project manager a minute. A false clear manufactures confidence right before a pay estimate goes out and replaces a person's own check with a machine's silence, which is worse than shipping nothing at all."
   },
   {
    "item": "Any generative AI in Phase 1, including the narrative coverage node",
    "reason": "Enumerable requirements are the bulk of the value and a rule does them cheaper, faster and testably. A rule can be enumerated and argued with. A model can only be sampled. The narrative node gets added after the rule layer has run a real closeout cycle and somebody can point at the requirement types the rules keep missing."
   },
   {
    "item": "Any automated review of a deliverable about to carry a licensed professional's stamp",
    "reason": "ASCE Policy Statement 573, adopted July 18th 2024, leaves that responsibility with the licensed engineer. The 2026 Ames and Gough survey of 15 A and E liability insurers found 80 percent viewing AI adoption by design firms as a potential disruptor, and ISO and Verisk released three optional generative AI exclusion endorsements effective January 2026, optional meaning each carrier decides what is attached. A narrow deterministic completeness check on a stamped deliverable is defensible. A generative reviewer is not."
   },
   {
    "item": "Writing anything into an owner agency's system of record",
    "reason": "Whether R&M holds any authority to feed that record is unknown until Gate A answers it, and a write path into an agency system is a different contract with a different assurance bar. Phase 1 reads only."
   },
   {
    "item": "Mobile, offline field capture",
    "reason": "Capture, offline sync and photo handling are the three riskiest components in the whole Copilot, and cached project data on a field device pulls device management, encryption and media handling into a certified boundary. That is Phase 2, it starts with a buy evaluation, and it stays parked until the spike is done."
   },
   {
    "item": "Firmwide search over 57 years of records across four offices",
    "reason": "It was killed on purpose. Corpus condition is unknown, CUI segregation inside that corpus is unknown, and no acceptance metric is nameable today. One index spanning mixed CUI and non CUI content is an information flow problem inside the certification R&M paid for in December 2025."
   },
   {
    "item": "Anything aimed at proposals, pursuits or SF330 production",
    "reason": "R&M announced a Proposal Manager into the Marketing Group on July 14th 2026, into a function led by a 29 year FSMPS CPSM whose bio names proposal development as a specialty. The industry read found no named firm at any size attached to a measured proposal productivity number with a stated method. There is a live human fix mid installation and no honest evidence to sell against it."
   },
   {
    "item": "Auto submitting a pay estimate, or gating a submittal on the Sentinel's output",
    "reason": "The report is an input to a person's judgement about money. The moment the tool can hold up a submittal, its false flags start costing real days and its silence starts carrying authority it has not earned."
   },
   {
    "item": "Multi tenant hosting, or any hosting on our infrastructure",
    "reason": "Project data stays inside R&M's assessed boundary. Our infrastructure is not in that boundary and putting it there would be a certification problem rather than a convenience."
   },
   {
    "item": "CUI marked projects in the Phase 1 pilot, unless R&M's contracts read says otherwise",
    "reason": "A federal project is not automatically CUI. R&M's own contracts settle which projects carry markings, and until that read is done the pilot stays on projects R&M can name as non CUI."
   }
  ],
  "riskiest_assumption": "That R&M can actually feed this thing. Three legs, one assumption. First, that today's construction administration documentation is reachable from inside R&M's own boundary and machine readable rather than scanned images or a locked owner agency portal. Second, that R&M holds enough of the project record on its own side for a rules engine to check anything meaningful, rather than the owner agency owning the record R&M has no export from. Third, that R&M can name a set of active projects that carry no CUI markings for the pilot. If leg one is wrong, extraction becomes the project and the effort estimate is wrong by a lot. If leg two is wrong, the later Copilot's export path collapses and the Sentinel becomes the entire build rather than its first phase, which is a real outcome this design is shaped for rather than shaped around. If leg three is wrong, the pilot waits on contract reads before it starts.",
  "spike_to_retire_it": "Gate A, two calendar weeks, fixed fee, before a line of production code, and R&M keeps every answer whether or not they proceed. Four workstreams. ONE, the contracts read. Sit with R&M's contracts administration and take 6 to 10 active or recently closed construction administration projects. For each one record the owner agency, whether the contract or that agency's construction manual names a mandated field record system, whether R&M holds any export or feed right into it, and whether the contract carries CUI markings. Deliverable is a one page matrix, one row per project. TWO, the readability measurement. Take three real closed pay estimate packets, run a read only harvest, and measure the share of required items recoverable from a text layer or a structured field without heavy OCR, plus file naming consistency and whether dates and pay item numbers are machine recoverable. The threshold is set in advance, in writing, before the measurement is taken. If under 60 percent of required items are recoverable without an OCR heavy path, the Phase 1 build estimate is wrong, and Gate B is re priced or declined rather than absorbed. THREE, the boundary conversation. One working session with R&M IT and Stratus Services on whether a read only service inside the boundary is a change to the asset inventory and the system security plan, and what that change costs in effort and in assessor time. FOUR, start the four week baseline on one named document class, hours per person per week, recorded by R&M rather than estimated by us. Gate A ships the project matrix, the measured readability number against the pre stated threshold, a draft rulebook of 20 to 40 enumerated rules from one real contract, the system security plan impact note, and a written go, re price, or stop. All of it is theirs to keep.",
  "delivery": {
   "walking_skeleton": "Week 3, day one of Gate B. One project, one folder, three rules, run by hand from a command line, ending in a one page PDF that a named construction administration lead actually reads. The slice touches every component in the diagram. The Record Intake Service reads a copy of one real project folder read only and emits the file manifest. The Requirement Rulebook holds three rules taken verbatim from that project's contract, each citing its spec section. The Gap Engine evaluates those three rules and writes to PostgreSQL. The Gap Report renders, and it leads with the unexamined list before it lists a single missing item. Everything hard is on crutches deliberately. No scheduler, no single sign on, the operator runs it, one project only, no OCR path. The point of the skeleton is that the report reaches a human on day one, so the argument about what a useful gap looks like starts in week 3 rather than week 8.",
   "then_mvp": "Flesh out across weeks 4 to 6. Grow the rulebook to the full enumerable set for one contract type, targeting 30 to 60 rules, each landing with a golden file regression test built from a real closed packet. Harden the intake connector against the real source location rather than a copy. Build the Coverage and Unexamined Manifest properly, since that is the safety component and it deserves its own tests. Add single sign on and a simple report list page. Add the scheduled run tied to the pay estimate cycle. MVP at week 8 is the Sentinel running unattended on 3 to 5 live projects on their own cadence, the report reaching the project manager ahead of each pay estimate and at closeout, the rulebook owned by R&M's construction administration lead in their git repository, and three numbers on the table, precision on raised gaps, the miss log of gaps a person found and the rules did not, and rule coverage against the contract. Phase 2 is not in this delivery and does not start until Phase 1's actuals are on the table.",
   "estimate_range": "GATE A, weeks 1 and 2, roughly 0.4 to 0.6 person months of our time, confidence high at about 85 percent, because the work is reading, measuring and writing rather than building. The only real schedule risk is people availability during the construction season, which is why the contracts read and the boundary session get booked before week one starts. GATE B, weeks 3 to 8, roughly 1.0 to 1.6 person months, confidence moderate at about 60 to 70 percent, and that confidence is explicitly conditional on Gate A's readability measurement clearing the pre stated threshold. Phase 1 is 8 calendar weeks in total at a fixed 12,000 dollars, split 4,000 dollars at Gate A and 8,000 dollars at Gate B, and the fee does not move inside Gate B. The one scenario that changes the number is the corpus turning out to be scanned images or sitting inside an agency portal with no export, in which case Gate B is a 2.5 to 4 person month extraction project, which is a different contract, and it gets re priced or declined at the gate rather than absorbed mid build. Phase 2, field capture and offline sync, is a concept level band only, roughly 3 to 6 person months at 30 to 40 percent confidence, and it starts with a buy evaluation rather than a build. Anyone quoting Phase 2 tighter than that today is guessing.",
   "what_narrows_it": "Six things, five of which Gate A answers directly. The measured share of required items recoverable without OCR, which is the single biggest driver of Gate B effort. The count of enumerable requirements pulled from one real contract, because rulebook size maps almost linearly to build days. Whether the sources are one file share or several plus an agency portal, since each additional source is a connector. R&M's own answer on which pilot projects carry CUI markings. The assessor's answer on whether a read only in boundary service is a system security plan change and what that costs. And the sixth, which is R&M's to commit rather than ours to estimate, roughly 6 to 10 hours of the construction administration lead's time spread across the six weeks for rule review, since rules nobody senior has argued with are the fastest way to build the wrong checker."
  }
 },
 "roi": {
  "ask_resize_note": "THE ASK WAS RESIZED FROM 18,000 TO 12,000 DOLLARS AFTER THIS ANALYSIS, AND THE ANALYST IS THE REASON. It flagged that the showrunner's Phase 3 economics pre-check had narrated a conservative run rate of roughly 11,900 dollars a year from drivers that do not produce it. Computed in scripts/roi_math.py, these conservative drivers produce 8,792 dollars a year. At an 18,000 dollar fee the conservative case recovered 97 percent of five year cost and never paid back inside the horizon, so it did NOT clear. No driver was bent. The ask was cut instead, which is what ROI_METHOD says to do. At 12,000 dollars the conservative case recovers 119 percent and pays back at month 47. This is the exact failure the rule about computing arithmetic in code rather than narrating it exists to prevent, and it was the showrunner that broke the rule.",
  "the_ask": "12,000 dollars fixed fee, Phase 1 only, split across two gates. GATE A, 4,000 dollars, weeks 1 and 2, the spike plus the baseline instrument. It is a real stop point and R&M keeps every answer. GATE B, 8,000 dollars, weeks 3 to 8, the rules only Sentinel on live projects. The only irreversible commitment is the 4,000.",
  "cost_note": "Five year total cost of ownership, not sticker price. The 12,000 dollar fixed fee is the implementation and integration line in full, which is the honest shape for an eight week build where the work IS the integration. It buys Gate A, a two week spike answering whether an owner agency dictates the field record system, whether today's documentation is reachable and machine readable, and which projects carry CUI markings, plus the start of a four week measured baseline. It then buys Gate B, weeks 3 to 8, the rules only Sentinel running on live projects. Gate A is a real stop point, so if R&M stops there most of the fee is unspent and every answer stays with them. Training and change management is assumed at 30 hours of R&M staff time, roughly 16 hours of rule enumeration sessions with their construction administration lead, 8 hours of project manager orientation to the gap report, and 6 hours of contracts and IT time inside Gate A. That line is small on purpose, because Phase 1 changes nobody's workflow. Run cost is assumed at 2,800 dollars a year and the single biggest reason it is that low is that Phase 1 has NO model in it, so there is no inference cost, no evaluation harness and no model refresh at all. The line is hosting inside their existing certified environment, roughly twelve hours a year of rule maintenance as agency requirement sets change, false flag triage, and a modest support allowance. Run cost is carried for 4.5 of the 5 years because the tool goes live around week eight. Contingency is 20 percent, the top of the 15 to 20 band, applied to the whole stack including a fixed fee that can't overrun, which is deliberately conservative and should be read that way. Every one of these cost drivers is our assumption and none of them came from R&M.",
  "benefits": [
   {
    "benefit": "Pre submittal documentation reconciliation, staff time recovered",
    "kind": "capacity",
    "basis": "Assumed 60 pay estimate and progress submittal documentation reconciliation events a year across R&M's construction administration work, at an assumed 2.0 hours each of locating records and cross checking them against contract documentation requirements, at an assumed 95 dollar fully loaded internal cost, with an assumed 40 percent of that time removed. The Sentinel removes the search for what is missing, not the judgement about what to do next, which is why the cut is well under half.",
    "note": "CAPACITY, not cash. The redeploy test is NOT passed, because we do not know R&M's utilisation and they publish nothing that would tell us. The only conversion route we can see from outside is avoid backfill on the seasonal Project Civil Engineer, Construction Administration seat that is currently posted, and only R&M can say whether that seat would otherwise be filled. We do not assume it and no dollar in this model depends on it. Anchor is R&M's own verbatim posting duty, administer project documentation and audit trails to ensure funding participation, against a firm where nearly 95 percent of work is for public clients."
   },
   {
    "benefit": "Second reviewer completeness check before the submittal goes to the owner, time recovered",
    "kind": "capacity",
    "basis": "The same assumed 60 events a year, at an assumed 0.75 hours each for the senior review pass that a federal aid submittal normally gets, at the same assumed 95 dollar loaded cost, with an assumed 35 percent removed. The Sentinel changes that pass from a check built from scratch into reading a list of specific items it did not find.",
    "note": "CAPACITY. This line must NOT overlap the line above and the study should say so plainly. The line above is the person assembling. This line is the different, more senior person checking. If R&M tells us one person does both, this line collapses to zero and the case gets worse, not better, so it is the first driver to test against the measured baseline in Gate A."
   },
   {
    "benefit": "Project closeout documentation assembly effort reduced",
    "kind": "capacity",
    "basis": "An assumed 8 project closeouts a year at an assumed 1,140 dollars of internal documentation assembly cost each, which is roughly twelve hours of a project engineer's assumed loaded time, with an assumed 30 percent reduction. A checker that runs through the season means the gaps are closed as they appear rather than discovered at the end, which is the point in the cycle where a missing record is most expensive to chase.",
    "note": "CAPACITY. The 30 percent is deliberately low. A continuously running completeness check plausibly does more than that at closeout, and we are not claiming it until somebody measures it."
   },
   {
    "benefit": "Internal rework when a record gap surfaces at an owner agency record review",
    "kind": "cash",
    "basis": "SET TO ZERO EVENTS IN THE CONSERVATIVE COLUMN BY CONSTRUCTION. Assumed 2 events a year at an assumed 4,000 dollars of internal response cost in the most likely column, and 3 events at 5,000 dollars in the aggressive column, with an assumed 35 to 40 percent reduction. This is the cost of assembling a response, not lost funding.",
    "note": "HANDLE WITH CARE AND READ THE ZERO. Nothing published tells us R&M has ever had a funding disallowance, an audit finding or a record dispute, and we are not implying one exists. The frequency is our assumption with a visible range starting at zero, R&M owns the real number, and the conservative column carries none of it. This line never carries the case and if a reader deletes it entirely the conservative verdict is unchanged."
   }
  ],
  "benefit_phasing": "No day one full benefit anywhere in this model. Phase 1 goes live around week eight, then a ninety day stabilisation while the rule set is argued over with R&M's construction administration lead and tuned for recall, since a false clear is worse than shipping nothing and the tool never asserts completeness. Year one is therefore partial, assumed at 45 percent of full run rate in the conservative column, 55 percent most likely, 65 percent aggressive. The spread is wider than a normal ramp because Alaska construction work is seasonal, so year one turns substantially on whether the build lands before spring mobilisation or part way through the season. Year two is full run rate. Year three onward is held flat rather than compounded, because rule coverage grows only as fast as somebody enumerates new requirement types and we will not model growth we have no evidence for. QUARANTINED, NOT IN THE FORMULA. Three real benefits are deliberately left unquantified and carry no dollars anywhere in this table. Reduced anxiety for the person whose posting says they administer audit trails to ensure funding participation. A cleaner, more defensible project record if a claim or change order ever goes contentious. An enumerated, written down list of documentation requirements that keeps its value even if the software is thrown away. Owners respect these being named and left out of the arithmetic.",
  "scenarios": {
   "conservative": "60 reconciliation events a year, 2.0 hours each, a 95 dollar loaded rate and a 40 percent cut, plus a 0.75 hour senior review pass at 35 percent, 8 closeouts at an assumed 1,140 dollars with 30 percent removed, and ZERO agency review events. Every driver in this column sits at or below what we believe the honest floor is. Computed run rate is 8,792 dollars a year. At the resized 12,000 dollar ask it recovers 119 percent of five year cost and pays back at month 47, which is late but inside the horizon. At the original 18,000 it recovered 97 percent and never paid back, which is why the ask moved.",
   "most_likely": "90 events a year, 3.0 hours each, a 110 dollar loaded rate and a 45 percent cut, a 1.0 hour senior review pass at 40 percent, 10 closeouts at an assumed 2,200 dollars with 35 percent removed, and 2 agency record review events a year at an assumed 4,000 dollars with 35 percent removed. This column reflects what we actually expect from a 100 plus person firm running construction administration, materials testing and special inspections as three separate service lines across four offices on nearly 95 percent public client work. It clears comfortably and it is not the column the decision should rest on.",
   "aggressive": "110 events a year, 3.5 hours each, a 120 dollar loaded rate and a 50 percent cut, a 1.0 hour review pass at 45 percent, 12 closeouts at 2,800 dollars with 40 percent removed, and 3 agency review events at 5,000 dollars with 40 percent removed. Deliberately held below what an optimistic reading would support, because a five to seven times spread between the outer columns already tells a CFO the honest truth, which is that R&M publishes no volume, no hours, no headcount split and no rate, so the width of this range IS the state of our knowledge rather than a rhetorical device."
  },
  "conservative_clears": true,
  "conservative_clears_note": "TRUE ONLY BECAUSE THE ASK WAS CUT. At 18,000 dollars it was false, 97 percent recovered and no payback. At 12,000 it is 119 percent recovered with payback at month 47. Nothing about the drivers changed.",
  "computed": [
   {
    "scenario": "Conservative",
    "annual_run_rate_benefit": 8792,
    "cumulative_benefit_5yr": 39126,
    "tco_5yr": 32940,
    "percent_of_tco_recovered": 119,
    "payback_month": 47,
    "pays_back_within_horizon": true
   },
   {
    "scenario": "Most likely",
    "annual_run_rate_benefit": 27825,
    "cumulative_benefit_5yr": 126604,
    "tco_5yr": 32940,
    "percent_of_tco_recovered": 384,
    "payback_month": 15,
    "pays_back_within_horizon": true
   },
   {
    "scenario": "Aggressive",
    "annual_run_rate_benefit": 48480,
    "cumulative_benefit_5yr": 225432,
    "tco_5yr": 32940,
    "percent_of_tco_recovered": 684,
    "payback_month": 7,
    "pays_back_within_horizon": true
   }
  ],
  "payback_range": "Printed as the computed span, never as a point. Month 47 in the conservative column, month 15 most likely, month 7 aggressive. That gap between columns IS the decision, and the study shows both ends of it rather than the middle. There is no single payback figure here and the study must not narrate one.",
  "base_rate_note": "The outside view applies to THIS proposal, not to somebody else's. MIT's finding that about 95 percent of enterprise AI pilots show no measurable P&L impact, and RAND's that about 80 percent of AI projects fail, are the reference class this build belongs to and we are not claiming an exemption. Four things are designed in to put it in the small share that pays, and each is checkable. One, Phase 1 has NO AI IN IT AT ALL, so end to end reliability equals rule coverage, and rule coverage is a list you can print on a page and argue over with your own construction administration lead rather than a number you can only sample. Two, it requires no adoption, because it changes nobody's workflow and produces a report, and thin adoption is the failure mode that eats most of that 95 percent. Three, Gate A is a real stop point that buys a measured baseline BEFORE the larger commitment, which is the single most reliable way to leave the reference class. Four, the number has a named owner and a defined variance check. The same base rate is exactly why the conservative column is printed at month 47 rather than hidden behind the most likely one.",
  "value_owner": "R&M names the person in week one, we name the ROLE. The number belongs to whoever owns the duty their own posting states verbatim, administer project documentation and audit trails to ensure funding participation, which is the construction administration lead. The countersign on the hours baseline belongs to whoever controls project accounting, because the baseline is timesheet data and the value owner should not be the only person who sees it. VARIANCE CHECK, and it is defined before the money moves. The four week baseline inside Gate A records actual hours per reconciliation event and per closeout. The same measurement is re run at 90 days and at 12 months after go live and the delta is reported to the value owner against that baseline, not against anything in this table. Two reliability counts ride alongside it because rule coverage IS the reliability number here, gaps flagged versus gaps confirmed real, and gaps a human found that the rules missed. If the 12 month actual comes in below the conservative column, the honest conclusion is that the Sentinel did not pay and we should say so at the time.",
  "assumptions": [
   "EVERY DRIVER BELOW IS AN ASSUMPTION, NOT A FACT. R&M publishes no revenue, no precise headcount, no headcount split, no project volume, no hours, no rates and no win rate. The fact checker confirmed this explicitly. Nothing in this model came from R&M and all of it is ours to defend and theirs to replace in week one.",
   "60 documentation reconciliation events a year, conservative. Assumed from a 100 plus person firm running Construction Administration, Materials Testing and Special Inspections as named service lines across four Alaska offices.",
   "2.0 hours per event of locating and reconciling documentation against contract requirements, conservative. Low for federal aid documentation, which carries daily reports, materials certifications, test results, certified payroll and quantity documentation.",
   "95 dollars an hour fully loaded internal cost, conservative. Stated plainly, this is BELOW a typical fully loaded A and E project engineer cost and well below any billing rate. It is deliberately low and we did not raise it.",
   "40 percent of reconciliation time removed, conservative. This is the driver we are least sure of, because the Sentinel removes the search and not the judgement.",
   "0.75 hours per event for a second, senior review pass with 35 percent removed. If R&M tells us one person assembles and checks, this line goes to zero and the conservative case gets worse. Test it first in Gate A.",
   "8 project closeouts a year at 1,140 dollars of internal assembly cost each with 30 percent removed. The 1,140 is an assumed dollar figure standing for roughly twelve hours of the assumed loaded time.",
   "ZERO owner agency record review events in the conservative column. Nothing published tells us R&M has ever had a disallowance, an audit finding or a record dispute and we are not implying one. The most likely and aggressive columns assume 2 and 3 events a year respectively at 4,000 and 5,000 dollars of internal response cost. This line does not carry the case in any column.",
   "30 hours of R&M staff time for training and change management, valued at 2,850 dollars, and 2,800 dollars a year of run cost. Both are ours to defend. The run cost is low specifically because Phase 1 has no model and therefore no inference, evaluation or refresh cost.",
   "20 percent contingency applied to the whole stack including a fixed fee that can't overrun. Deliberately conservative.",
   "Year one ramp of 45 percent conservative, from an eight week build plus a ninety day stabilisation, widened by Alaska seasonality. Years three to five held flat, not compounded.",
   "THE 28 PERCENT FROM LOUISIANA DOTD IS NOT A DRIVER AND MUST NOT BE USED AS ONE. It belongs to structured capture and workflow automation with light ML, it was measured on inspectors creating and submitting daily work reports, and Phase 1 is not that system. It is context for direction only and no dollar in this table is anchored to it.",
   "THE ARITHMETIC CORRECTION, RECORDED RATHER THAN QUIETLY FIXED. The showrunner's Phase 3 pre-check narrated a conservative run rate of roughly 11,900 dollars from drivers that produce 8,792. The analyst caught it, roi_math.py confirmed it, and the ask was cut from 18,000 to 12,000 rather than a driver being adjusted to rescue the original number."
  ]
 },
 "roadmap": {
  "now": [
   {
    "item": "Gate A, a two week spike that answers the three questions the whole build rests on. Does an owner agency dictate the field record system on federal aid work, is today's field documentation reachable and machine readable, and which projects actually carry CUI markings under R&M's own contracts. No production code is written in these two weeks.",
    "metric": "Three written answers with the contract language and the export test behind each one, plus a named list of projects R&M's own contracts confirm as non CUI. Success is that the answers exist and are sourced, not that they are favourable. If the first answer is that the agency owns the record and won't take a feed, that finding is the deliverable and everything below changes shape in the open rather than quietly.",
    "why_first": "It is the riskiest assumption in the entire analysis and it costs two weeks instead of four person months. It is also the strongest off ramp in the engagement. R&M can stop at day fourteen and keep the system of record answer, the data access answer, the CUI scope answer and their own baseline, all of which are worth having whether or not a line of code ever gets written."
   },
   {
    "item": "R&M's own four week baseline on one named document class, started in week one and owned by their construction administration lead. Hours per pay estimate or progress submittal documentation reconciliation, hours per project closeout, the count of each inside the window, and any review findings raised against those records.",
    "metric": "Four consecutive weeks logged by R&M. Nothing about R&M's volumes, hours or headcount split is published anywhere, so every driver in the business case is theirs to supply and ours to recompute once they do. Without this baseline the later gates have no bar to test and the honest default at those gates is no.",
    "why_first": "Every funding gate below rests on it, and it can only be collected before the tool changes the thing being measured. Starting it alongside the spike is the only way it exists in time to decide anything."
   },
   {
    "item": "Gate B, the rules only Documentation Gap Sentinel running on live projects through the 2026 closeout and pay estimate season, weeks three to eight. It reads the documentation already being produced and reports the specific items it did not find before a pay estimate or progress submittal goes out. Zero AI in it. No field app, no new habit, no training for a seasonal crew.",
    "metric": "Rule coverage enumerated on a page and signed off by R&M's construction administration lead before it runs, then hours per reconciliation and per closeout against their four week baseline, the count of records produced holding or rising, and no increase in review findings. One constraint is measured as a defect rather than a feature. The tool never asserts completeness, so a screen that reads all clear is a bug. It reports only what it did not find and it names what it did not look at.",
    "why_first": "Closeout and pay estimates run past the field season, so this is the one piece that can start earning this autumn rather than waiting for spring. It is also the smallest job in the set at roughly 1.5 person months, it asks nobody to change how they work, and it retires the data access risk the spring increment depends on. Highest value over smallest job in the whole set, which is why it is Phase 1 and why the ask is 12,000 dollars rather than anything larger."
   }
  ],
  "next": [
   {
    "item": "The CMMC scope decision, taken before any capture increment is designed. The assessor and Stratus conversation, the asset inventory and system security plan change, and a written in scope or out of scope decision for every component that would cache project data on a field device.",
    "metric": "A recorded scope decision per component from R&M's compliance partner before a line of capture code, and a pilot project list limited to projects their own contracts read confirms as non CUI. Measured as zero new in scope systems introduced without a recorded change to the asset inventory behind the 110 controls certified on December 22nd 2025."
   },
   {
    "item": "Structured field capture and a drafted daily work report, deployed at spring mobilization 2027 while seasonal staff are onboarding anyway. The inspector speaks, photographs and taps, a fixed step workflow builds the draft, and the inspector approves before anything becomes a record. The model touches exactly two nodes and every enumerable requirement stays in rules.",
    "metric": "Against R&M's own recorded baseline, hours per report day, the share of reports submitted within 24 hours and within 72 hours, and observations captured per report day holding or rising. Draft edit rate is tracked as its own separate increment so the deterministic layer and the model nodes are never reported as one number. A build that produces fewer hours and a thinner record has failed this outcome."
   },
   {
    "item": "The deterministic export into the owner agency's record format, built only if Gate A found that an export path exists at all.",
    "metric": "Share of records the owner's system accepts on first submission with no rekeying, against however much rekeying R&M records today. A format is a contract, so the same input has to produce the same output every time, measured as zero variance across repeated runs of the same input."
   },
   {
    "item": "The narrative coverage flag, the first model node ever added to the Sentinel, earned only after a real closeout cycle names the requirement types the rules keep missing.",
    "metric": "A named list of requirement types the rule layer missed across one full closeout cycle, then recall on that single class, tuned so a false flag costs a project manager a minute and a false clear is treated as a defect. It ships only if that list is long enough to be worth one model step, and the honest outcome is that it doesn't ship."
   },
   {
    "item": "R&M asks its own liability carrier what is attached to its own policy before any generative node goes live. ISO and Verisk released three optional generative AI exclusion endorsements effective January 2026, and optional means each carrier chooses.",
    "metric": "A written answer from their broker on file before the first model node runs on live work. We have no visibility into their policy and we won't pretend otherwise, so this is a yes or no on record rather than an assumption anyone carries forward."
   }
  ],
  "later": [
   {
    "item": "The Evidence Locator, which is the Project Record Assistant downscoped to what it should have been. It returns documents and citations over a deliberately bounded single project corpus when a change order or a claim is live. No generated conclusions in a claims context ever, and legal hold aware indexing from day one. It gets materially better once the capture increment has been producing structured records, so building it first would build it on the worst possible version of its own corpus.",
    "metric": "R&M states the frequency first, how many change orders, claims or record disputes a year actually reach this, since nothing published tells us. Then hours to assemble an evidence pack for one of them against their own logged baseline, with every returned item traceable to a source document and zero written summaries that could later be quoted into a claim position."
   },
   {
    "item": "A NEPA and permitting drafting increment, capped honestly. DraftNEPABench, assessed by 19 subject matter experts across tasks from 18 federal agencies, puts the ceiling at 1 to 5 hours saved per subsection and up to roughly a 15 percent reduction in drafting time, and a model vendor co authored it, so that is a ceiling under favourable conditions rather than a forecast.",
    "metric": "Hours per subsection against R&M's own baseline on one document type, held to that published ceiling in any case we ever build. A second metric matters more for a firm whose documents get litigated, the rate at which incomplete or out of date references are caught, since the benchmark authors' own caveat is that models may not reliably identify those discrepancies unless explicitly instructed."
   },
   {
    "item": "Comment classification and clustering on one public involvement process, with a person approving every single response. Public Involvement and NEPA are both named service lines, so the obligation is real even though the volume is bursty at a firm this size rather than continuous.",
    "metric": "Comments moved into an approved comment and response record per person hour against their current spreadsheet baseline, with 100 percent of responses approved by a person. R&M's own comment volume on one process decides whether this is worth building at all, and that number is theirs."
   },
   {
    "item": "Grant writing support, the most interesting unpicked item on the map and the one with the least evidence behind it. Grant Writing is one of the 24 service lines, so unlike proposals this is billable delivery rather than overhead, and leverage here raises capacity in a revenue line instead of trimming an internal cost.",
    "metric": "R&M supplies grant volume, staffing and win rate first, none of which is published anywhere. Then applications delivered per available person week and win rate, both baselined by them before anything is built. This stays a hypothesis until those numbers exist."
   },
   {
    "item": "Deterministic completeness checking on design deliverables, sheet index against sheets present, callouts that resolve, quantities that reconcile. No generative review of anything about to carry a licensed professional's stamp, and that is a permanent line rather than a phase we grow out of.",
    "metric": "Completeness defects surfaced before the stamp against what the senior redline catches today, counted by them. ASCE Policy Statement 573, adopted July 18th 2024, leaves the responsibility with the licensed engineer, so the metric here is defects surfaced to the reviewer, never judgments made in place of one."
   },
   {
    "item": "Materials testing and special inspections get deterministic automation, not AI, and saying so is worth more to R&M than selling the alternative. Breaks, gradations and densities are structured, stable and high volume, which is the exact profile where a rule is cheaper, safer and exhaustively testable.",
    "metric": "Share of results reaching the client report with no retyping, and transcription corrections per hundred results, both against a count R&M takes first. If this is ever built it gets built as plumbing and priced as plumbing."
   },
   {
    "item": "Certified payroll, progress billing and subconsultant administration against published agency rules. Rules based work with no model required for most of it, and it earns year round rather than seasonally, which is unusual on this list.",
    "metric": "Hours per billing cycle and rework rate on agency submittals against R&M's own baseline. Nearly 95 percent of the work is for public clients, so these run against agency rules that change on a schedule rather than by judgment, which is what makes a rule the right tool."
   },
   {
    "item": "Coarse feature and defect detection over imagery and point clouds in Remote Sensing and GIS, scoped to what the published evidence actually supports rather than what the demos show.",
    "metric": "Detection recall on a set R&M labels themselves. The calibration to hold it to is INDOT with Purdue across 3,549 images, where average classification accuracy was approximately 0.94 while the average IoU was approximately 0.61 and average crack pixel detection recall and precision were 0.68 and 0.35. Coarse detection works, fine measurement does not, and those authors recommend manual and AI collaboration rather than full automation."
   },
   {
    "item": "Field to finish note reduction and survey record retrieval in Geomatics. Most of the real win here is deterministic data plumbing rather than a model, which is worth knowing before anyone budgets for one.",
    "metric": "Hours from field data to a finished drawing on one survey type against their own baseline, plus time to locate a prior survey record, timed by them on a handful of real lookups rather than estimated."
   },
   {
    "item": "Boring log, lab result and site characterization report assembly in Geotechnical and Contaminated Sites. Extraction and assembly only. Interpretation stays with the licensed professional.",
    "metric": "Hours per report against their own baseline, with a transcription error rate at or below whatever the manual path produces today, measured on the same set of reports both ways."
   },
   {
    "item": "Continuous control evidence for the 110 controls behind the CMMC Level 2 certification. Deliberately last on this list, since they solved it well and recently with a named partner, and the idea that the ongoing evidence burden hurts is our assumption rather than anything they said.",
    "metric": "Hours the IT group spends collecting evidence per assessment cycle, a number only they hold. If that number turns out to be small, this never gets built and that is the correct outcome."
   },
   {
    "item": "Pursuit and proposal tooling, DECLINED for this year and said out loud rather than skipped quietly, because it is the loudest cited pain in the whole file and passing over it silently would read as though we missed it. R&M announced a Proposal Manager into the Marketing Group on July 14th 2026 and the function is led by a 29 year FSMPS CPSM whose own bio names proposal development as a specialty, so a live human fix is mid installation and arriving on top of it is a political error rather than a technical one.",
    "metric": "The Proposal Manager's own baseline is both the metric and the revisit trigger. Four weeks of where the hours actually go, then a full pursuit cycle under her process, and we revisit only once there is a measurement a build would have to beat. The first move costs almost nothing and is useful whatever happens next, tagging and searching the prior technical narratives R&M already holds. No named firm at any size is attached to a measured proposal productivity number with a stated method, so there is no honest number to promise against today."
   }
  ],
  "gates": "Phase 1 is 12,000 dollars fixed fee, 4,000 at Gate A and 8,000 at Gate B, and it buys the Sentinel and nothing else. Nothing in the Next lane is being sold today. Every headcount, volume and reach figure anywhere in this package is our labelled assumption, and R&M corrects them in week one.\n\nGATE A, end of week two, and it is a real stop. R&M can end the engagement here and keep the system of record answer, the data access answer, the CUI scope answer and their own started baseline. The 8,000 dollar Gate B portion is never invoiced, so the only irreversible commitment in this proposal is 4,000 dollars. Two findings can come out of this gate and both get said plainly rather than reshaped. If an owner agency mandates a field record system R&M has no authority to feed, the export path collapses, the Sentinel becomes the entire build rather than its first phase, and the Next lane shrinks accordingly. If today's documentation lives as scanned PDFs or inside an owner portal with no export, extraction becomes the project, the 1.5 person month figure is wrong by a lot, and the work gets repriced in the open at this gate rather than absorbed quietly later.\n\nGATE B, end of week eight, and it is also a stop. R&M keeps a running rules only Sentinel, the enumerated rule set their own construction administration lead signed, and a measured before and after on their own numbers. They own it whether or not anything further happens, and Phase 1 has to pay for itself on that alone.\n\nGATE C, the winter decision, by March 1st 2027. The spring capture increment is funded only if Phase 1's actuals clear a stated bar. Hours per reconciliation and per closeout down against their own four week baseline, the count of records produced holding or rising, no increase in review findings, and rule coverage their construction administration lead is willing to put a name to. If the baseline was never collected, the bar can't be tested and the honest default at this gate is no. If the bar is missed, the spring increment doesn't get funded and Phase 1 still stands on its own.\n\nGATE D, inside the spring increment, and these are preconditions rather than parallel workstreams. No component caches project data on a field device until R&M's compliance partner has recorded the asset inventory and system security plan change. No generative node ships until R&M's own carrier has answered in writing. Each model node is measured as its own increment against the deterministic layer, because the 28 percent measured by Louisiana DOTD and LTRC with FHWA belongs to workflow and capture automation with light ML rather than to a language model, so the deterministic layer carries the case alone and any model node that can't show its own separate lift gets removed.\n\nKILLED, not parked. The Firmwide Knowledge Assistant is dead rather than sitting in the Later lane, and the reason is worth carrying. It was a direct answer to a platform announced by a firm with more than 6,000 engineers, architects and scientists across more than 120 office locations, and a 100 plus person firm copying that platform's economics is the transfer that doesn't survive contact. Reach alone was holding its score up. What survives the kill is the observation that R&M's certified boundary is a genuine differentiator, which this build uses quietly instead of announcing.\n\nDECLINED, deliberately and with reasons rather than by omission. Pursuit and proposal tooling for this year, with the revisit trigger written into the Later lane. Materials testing, which needs deterministic automation rather than AI. Generative review of any deliverable about to carry a licensed professional's stamp, which is a permanent no at any phase.",
  "need_from_you": "Two or three named active projects for the pilot with a one line confirmation from contracts that they carry no CUI markings. Roughly 6 to 8 hours of the construction administration lead across weeks three and four to enumerate and argue the requirement list. The contract documentation requirements for those projects, spec sections, pay item list and owner documentation manual. Read access to where daily reports, materials records and submittal backup actually live, plus a named IT contact. Ten minutes per submittal from the pilot project managers for four weeks to fill the baseline tally. One 45 minute conversation with IT about certified boundary scope. One named person who owns the number at 90 days. A yes or no from Len Story at the end of week two on whether Gate B proceeds.",
  "high_integrity_dates": [
   "March 1st 2027, the go or no go on the spring capture increment. This is the one real date in the roadmap and we are making it a commitment. Alaska's construction season sets it, not us. A decision after roughly the end of March can't be built, tested and deployed in time for spring mobilization, so it forfeits the entire 2027 season and the next honest start is spring 2028.",
   "Spring mobilization 2027, the deployment window for the capture increment if the March decision is a go. We commit to that window and we commit to not dropping a new field habit on a crew mid season. New seasonal staff are onboarding then anyway, so switching cost is at its annual floor, and their own posting says field staff work in project locations throughout the state for extended periods of time during construction season.",
   "October 1st 2026, the latest Phase 1 start that still puts the Sentinel on the 2026 closeout and pay estimate season. This is exactly why Phase 1 is the Sentinel rather than the field app. Closeout and pay estimates run past the field season, so the rules only version can start earning this autumn. A later start still works, the first earning window simply slides into 2027 and Gate C loses the data it was meant to decide on."
  ]
 }
}
```


---

## ROI drivers

```json
{
 "scenarios": {
  "conservative": {
   "pursuits_per_year": 60,
   "benefit_lines": [
    {
     "label": "Pre submittal documentation reconciliation, time recovered (CAPACITY)",
     "hours_per_pursuit": 2.0,
     "rate": 95,
     "cut": 0.4
    },
    {
     "label": "Second reviewer completeness check before submittal, time recovered (CAPACITY)",
     "hours_per_pursuit": 0.75,
     "rate": 95,
     "cut": 0.35
    }
   ],
   "avoided_cost_lines": [
    {
     "label": "Project closeout documentation assembly (CAPACITY)",
     "events_per_year": 8,
     "cost_per_event": 1140,
     "reduction": 0.3
    },
    {
     "label": "Internal rework at an owner agency record review (CASH, zeroed by construction)",
     "events_per_year": 0,
     "cost_per_event": 4000,
     "reduction": 0.35
    }
   ],
   "implementation": 12000,
   "training": 2850,
   "run_cost_per_year": 2800,
   "run_cost_years": 4.5,
   "contingency": 0.2,
   "year1_ramp": 0.45,
   "years": 5
  },
  "most_likely": {
   "pursuits_per_year": 90,
   "benefit_lines": [
    {
     "label": "Pre submittal documentation reconciliation, time recovered (CAPACITY)",
     "hours_per_pursuit": 3.0,
     "rate": 110,
     "cut": 0.45
    },
    {
     "label": "Second reviewer completeness check before submittal, time recovered (CAPACITY)",
     "hours_per_pursuit": 1.0,
     "rate": 110,
     "cut": 0.4
    }
   ],
   "avoided_cost_lines": [
    {
     "label": "Project closeout documentation assembly (CAPACITY)",
     "events_per_year": 10,
     "cost_per_event": 2200,
     "reduction": 0.35
    },
    {
     "label": "Internal rework at an owner agency record review (CASH, assumed frequency)",
     "events_per_year": 2,
     "cost_per_event": 4000,
     "reduction": 0.35
    }
   ],
   "implementation": 12000,
   "training": 2850,
   "run_cost_per_year": 2800,
   "run_cost_years": 4.5,
   "contingency": 0.2,
   "year1_ramp": 0.55,
   "years": 5
  },
  "aggressive": {
   "pursuits_per_year": 110,
   "benefit_lines": [
    {
     "label": "Pre submittal documentation reconciliation, time recovered (CAPACITY)",
     "hours_per_pursuit": 3.5,
     "rate": 120,
     "cut": 0.5
    },
    {
     "label": "Second reviewer completeness check before submittal, time recovered (CAPACITY)",
     "hours_per_pursuit": 1.0,
     "rate": 120,
     "cut": 0.45
    }
   ],
   "avoided_cost_lines": [
    {
     "label": "Project closeout documentation assembly (CAPACITY)",
     "events_per_year": 12,
     "cost_per_event": 2800,
     "reduction": 0.4
    },
    {
     "label": "Internal rework at an owner agency record review (CASH, assumed frequency)",
     "events_per_year": 3,
     "cost_per_event": 5000,
     "reduction": 0.4
    }
   ],
   "implementation": 12000,
   "training": 2850,
   "run_cost_per_year": 2800,
   "run_cost_years": 4.5,
   "contingency": 0.2,
   "year1_ramp": 0.65,
   "years": 5
  }
 }
}
```


---

## ROI computed in roi_math.py

```json
[
  {
    "scenario": "conservative",
    "annual_run_rate_benefit": 8792,
    "cumulative_benefit_5yr": 39126,
    "tco_5yr": 32940,
    "percent_of_tco_recovered": 119,
    "payback_month": 47,
    "pays_back_within_horizon": true
  },
  {
    "scenario": "most_likely",
    "annual_run_rate_benefit": 27825,
    "cumulative_benefit_5yr": 126604,
    "tco_5yr": 32940,
    "percent_of_tco_recovered": 384,
    "payback_month": 15,
    "pays_back_within_horizon": true
  },
  {
    "scenario": "aggressive",
    "annual_run_rate_benefit": 48480,
    "cumulative_benefit_5yr": 225432,
    "tco_5yr": 32940,
    "percent_of_tco_recovered": 684,
    "payback_month": 7,
    "pays_back_within_horizon": true
  }
]

```


---

## The study

```json
{
 "meta": {
  "company": "R&M Consultants, Inc.",
  "domain": "rmconsult.com",
  "segment": "Alaska engineering and surveying consultancy",
  "place": "Anchorage, Alaska",
  "date": "August 7th 2026",
  "prepared_for_first": true
 },
 "thesis": "Your construction administration posting names a documentation duty that protects your public funding.",
 "brief": "We read your public pages, your job postings, your news archive and your competitors, then spent the day on one question. Where could a small, honest build change how R&M works.\n\nThe answer we expected was proposals. Two senior seats in two different departments carry the identical duty, \"Conduct research and write technical portions of proposals to assist in bringing in new work.\", and a third carries \"Developing proposals.\" That is the loudest signal in your public material and we are not selling you anything for it. You hired a Proposal Manager twenty four days before we started, and we could not find one named firm at any size attached to a measured proposal productivity number with a stated method.\n\nWhat we found instead sits in a sentence from your Construction Administration posting: \"Administer project documentation and audit trails to ensure funding participation\". At a firm where nearly 95 percent of work is for public clients, that is a sentence about money. We have never seen an R&M project record, so we have no evidence you are missing anything. What we can see is that the duty exists and that a miss is not clerical.\n\nSo we would build the smallest useful thing. Before each pay estimate goes out, a check reads the documentation you already produce and reports the contract required items it did not find. It has no AI in it. Every requirement lives in a rule your own construction administration lead can read and argue with. It never says all clear, because a false clear is worse than shipping nothing.\n\nTwelve thousand dollars, eight weeks, two gates, and the first is four thousand and a real stop point.\n\nYour volumes, hours and rates are published nowhere, so every driver is our assumption and yours to correct. On the cautious version this recovers 119 percent of five year cost and pays back in month 47, just under four years, which is poor by any normal standard. The middle version is month 15. If one person both prepares and reviews, the cautious column drops to 99 percent and never pays back. That benefit is about 93 hours a year, roughly two and a half work weeks, and it is capacity rather than cash. Two numbers turn most of this into your own figures, roughly how many reconciliations you run a year and roughly how long one takes.",
 "found": {
  "title": "One sentence in your own job posting describes work that protects money, not paperwork",
  "lede": "Your Construction Administration posting names the duty. The client mix is what makes it expensive.",
  "body": "Your posting for a Project Civil Engineer in Construction Administration lists, among the duties, \"Administer project documentation and audit trails to ensure funding participation\". Read that against your Who We Are page, \"Nearly 95% of our work is for public clients\", and it becomes a sentence about money. An item that never reached the record is a reimbursement conversation rather than a filing problem.\n\nWe have never seen an R&M project record, so we have no evidence you are missing anything at all. What we can see is that the duty exists, that a person is named as responsible for it, and that the consequence of a miss is money.\n\nThe same posting asks for work \"in project locations throughout the state for extended periods of time during construction season\", and is classified Seasonal, Full-Time, Hourly. That is ordinary staffing for an Alaska season and reads to us as seasonality rather than a gap.\n\nOne of eleven roles open across your four offices sits in that group. Your postings carry no dates, and eleven openings at a firm ranked tenth in its size bracket on Zweig Group's 2026 list reads as scale rather than trouble.",
  "callout_big": "Nearly 95%",
  "callout_note": "of your work is for public clients, in your own words on your own page. That is the number that turns a documentation gap into a funding question.",
  "body_2": "We checked the field in both directions. DOWL published a 2020 piece on machine learning that claims no deployment of its own, and beyond that we found no current AI position and no named tool at DOWL, CRW or RESPEC. That absence covers only the pages we fetched, and a firm can run AI internally and say nothing about it. A fourth competitor's site would not load across three attempts, so we assessed three of four.\n\nThe more useful half is where this is measurably working, and it is not where the marketing points. The strongest independent result in your industry is a Louisiana state transportation department evaluation of photo based field inspection across more than fifty construction projects, which measured a 28 percent productivity increase for inspectors creating and submitting daily work reports. Two caveats belong in the same breath. That system was photographs filed on a fixed form and routed through set steps rather than a model, which is part of why what we would build has no model in it. It also measures field inspectors writing daily reports, the spring 2027 item rather than phase one, so none of that 28 percent is in our table.\n\nHDR publishes an AI statement that is mostly restraint, including \"Prohibit the use of generative AI for use in any final work product\". Michael Baker announced a platform in April reaching \"more than 6,000 engineers, architects and scientists\". Those are the economics of a rollout to a firm many times the size of the 100 plus people your own page names, and they do not transfer down."
 },
 "costing": {
  "title": "We can't tell you what this costs you, and neither can anyone else from outside",
  "lede": "Four numbers decide this and you are the only source for any of them.",
  "body": "We went looking for what this costs R&M and came back with nothing. Not the reconciliations you run in a year, not how long one takes, not what an hour costs you loaded. Your closeout count and what an assembly costs are not published either.\n\nNothing published says R&M has ever had a funding disallowance, an audit finding or a record dispute. We looked, and we are not hinting there is one. The cautious column assumes zero.",
  "callout_big": "17 assumptions",
  "callout_note": "Four move the answer most, how many reconciliations you run, how long one takes, what an hour costs you loaded, and how much of that time a check actually removes. The rest sit in the table below, every one marked. Your own four week baseline, started in week one, replaces the first two with measurements you take, and your own accounting supplies the third. How much a check removes is only known once it runs, at week eight.",
  "body_2": null
 },
 "opportunity": {
  "title": "What changes is that the list of what is missing exists before anyone goes looking",
  "lede": "One monthly pay estimate submittal, walked step by step.",
  "outcome_body": "One caution before the figure. We have never seen your records or your process.",
  "before_after": {
   "headline": "Preparing one monthly pay estimate submittal, today and after phase one",
   "before_title": "Today",
   "after_title": "After",
   "note": "The left column is our assumption, not your process. Row five is identical on purpose, and it is the most important row here. Deciding whether a gap actually matters is a judgement about a contract and about money, and it stays with the person whose name is on the project. We are not automating that and we would not know how to.",
   "rows": [
    {
     "today": "A progress payment comes due, so someone opens the project folder and works out what this contract requires for this pay period.",
     "after": "The check has already run against that project's rulebook. The required list exists before anyone opens the folder.",
     "gone": true
    },
    {
     "today": "They search daily reports, materials certifications, test results and quantity records to see what is actually there.",
     "after": "The report names the specific items the rules did not find, each one pointing back at the requirement it came from.",
     "gone": true
    },
    {
     "today": "A senior reviewer builds a second completeness check from scratch before it goes to the owner.",
     "after": "The senior reviewer reads a short list instead of rebuilding the check.",
     "gone": false
    },
    {
     "today": "Whatever is missing gets chased, sometimes after the crew has already left that site.",
     "after": "Whatever is missing was flagged before the submittal, while people are still out there.",
     "gone": false
    },
    {
     "today": "A person decides whether the gap actually matters and what to do about it.",
     "after": "A person decides whether the gap actually matters and what to do about it.",
     "gone": false
    }
   ]
  },
  "after_body": "The figure leaves out the part that makes this safe. The report never tells you a project is complete. It lists what it did not find, then names what it could not look at, so a folder it failed to reach shows up as unexamined rather than passing.\n\nThere is a third thing it can't show you. A requirement nobody wrote into the rulebook produces no line at all, which is why gate B runs the rules against submittals your own reviewer already checked by hand, and why the rulebook has a named owner rather than an author."
 },
 "build": {
  "title": "What we would build, and there is no AI anywhere in it",
  "lede": "A rulebook, a reader, a checker, and a report that admits what it missed.",
  "plain_parts": "A rulebook, one plain file per contract, holding what that contract requires, each rule naming its spec section. A reader that opens your project folders and writes nothing back. A checker that runs the rulebook against what it found. A report listing what it did not find, then naming everything it could not examine. Your construction administration lead owns the rulebook.",
  "what_it_does": "Ahead of each pay estimate or progress submittal, and again at closeout, it runs against what you already produce and reports the missing items with the requirement each came from.\n\nNothing changes for your field crews and there is nothing for them to install. The change lands on two desks, whoever prepares the estimate and whoever reviews it. If those two do not change how they work the hours in the table do not move.",
  "feasibility": "An early draft put a small language model on one part of this. It is out. Documentation requirements are enumerable, so a rule does them cheaper and testably. A rule can be printed on a page and disputed by your construction administration lead. A model can only be sampled. Until somebody can name the requirement types the rules keep missing, a model here is unearned.\n\nA firmwide assistant over 57 years of your records scored well on paper and is also out. Putting marked and unmarked federal material into one searchable pile runs against your CMMC Level 2 certification, announced in December 2025, which sets rules about where federal information sits.\n\nOne line holds at every phase. Nothing carrying a licensed professional's stamp gets reviewed by a model. ASCE Policy Statement 573 states that \"The civil engineer must maintain responsibility for project planning, designing, building, operations, maintenance, and the protection of the public health, safety, and welfare\". Insurers watch the same ground, with 80 percent of fifteen surveyed this year viewing AI adoption by design firms as a potential disruptor. Liability forms picked up generative AI exclusion endorsements in January 2026, optional rather than automatic, so that is a question for your broker rather than a settled fact.",
  "build_vs_buy": "We would buy every commodity part, the document parsing, the database, your own sign on, the report rendering, and hosting inside the environment your CMMC Level 2 certification already governs rather than standing anything new up beside it. That line is for whoever owns that boundary to draw rather than us. We would build only what is yours, starting with the reader, which has to understand folder conventions that will not be identical across Anchorage, Fairbanks, Juneau and Wasilla, then the rulebook format, the checker, and the piece that tracks what was not examined.",
  "architecture": {
   "nodes": [
    {
     "id": "sources",
     "label": "Your project records",
     "kind": "system"
    },
    {
     "id": "intake",
     "label": "Record reader",
     "kind": "build"
    },
    {
     "id": "rulebook",
     "label": "Requirement rulebook",
     "kind": "data"
    },
    {
     "id": "engine",
     "label": "Gap checker",
     "kind": "build"
    },
    {
     "id": "report",
     "label": "Gap report",
     "kind": "build"
    },
    {
     "id": "pm",
     "label": "Your project manager",
     "kind": "user"
    }
   ],
   "edges": [
    {
     "from": "sources",
     "to": "intake"
    },
    {
     "from": "intake",
     "to": "engine"
    },
    {
     "from": "rulebook",
     "to": "engine"
    },
    {
     "from": "engine",
     "to": "report"
    },
    {
     "from": "report",
     "to": "pm"
    },
    {
     "from": "pm",
     "to": "rulebook"
    }
   ],
   "caption": "Phase one, end to end. The highlighted boxes are the work we would do. The owner agency's record system is deliberately not here, because phase one does not read it and gate A decides whether it ever could. There is no model box either. The arrow running back from your project manager to the rulebook matters most, since the rules are only as good as the person who argues with them."
  }
 },
 "roi": {
  "title": "On the most cautious assumptions this pays back in month 47, just under four years",
  "lede": "Nothing here is a fact about your business yet. That is what your own four week baseline is for.",
  "lede_body": "Read the marks down the left before the numbers. Not one row is marked verified, because nothing about your volumes, hours or rates is published anywhere we could reach.\n\nThis ask started at eighteen thousand. At that price the cautious column never paid back, so the price came down rather than the assumptions going up.\n\nA payback in month 47 is a poor result by any normal standard. Gate A costs four thousand and your own four week baseline starts in week one rather than after it, so your volumes and your hours get measured while the three questions are being answered. How much a check actually removes stays our assumption until it runs at week eight.",
  "table_caption": "Five year view. Every input is a row, so the outputs at the bottom can be rebuilt from the page. Running cost starts at month seven, so it is charged for 4.5 of the five years, which is why the subtotal is 27,450 rather than 28,850. Your staff time is costed at the cautious hourly rate in all three columns, so it does not get cheaper as the case improves. Hours a year converts the closeout saving back to hours at the same loaded rate and leaves out the owner agency response, which we costed in dollars only, so the middle column is 121.5 plus 36 plus 70. Years three to five are held flat rather than compounded. Cost rows are ours and identical in all three columns.",
  "table_head": [
   "",
   "Conservative",
   "Most likely",
   "Aggressive"
  ],
  "table": [
   {
    "label": "Our fee, phase one, fixed",
    "cells": [
     "$12,000",
     "$12,000",
     "$12,000"
    ],
    "mark": "assumed"
   },
   {
    "label": "Your staff time, about 30 hours at the cautious rate, held flat across columns",
    "cells": [
     "$2,850",
     "$2,850",
     "$2,850"
    ],
    "mark": "assumed"
   },
   {
    "label": "Running and maintaining it, $2,800 a year from month seven, so 4.5 years",
    "cells": [
     "$12,600",
     "$12,600",
     "$12,600"
    ],
    "mark": "assumed"
   },
   {
    "label": "Subtotal before contingency",
    "cells": [
     "$27,450",
     "$27,450",
     "$27,450"
    ],
    "mark": "modelled"
   },
   {
    "label": "Contingency on the whole stack",
    "cells": [
     "20%",
     "20%",
     "20%"
    ],
    "mark": "assumed"
   },
   {
    "label": "Five year cost, all in",
    "cells": [
     "$32,940",
     "$32,940",
     "$32,940"
    ],
    "mark": "modelled"
   },
   {
    "label": "Reconciliation events a year",
    "cells": [
     "60",
     "90",
     "110"
    ],
    "mark": "assumed"
   },
   {
    "label": "Hours per event, locating and cross checking",
    "cells": [
     "2.0",
     "3.0",
     "3.5"
    ],
    "mark": "assumed"
   },
   {
    "label": "Loaded internal cost an hour",
    "cells": [
     "$95",
     "$110",
     "$120"
    ],
    "mark": "assumed"
   },
   {
    "label": "Portion of that time removed",
    "cells": [
     "40%",
     "45%",
     "50%"
    ],
    "mark": "assumed"
   },
   {
    "label": "Senior review pass, hours per event",
    "cells": [
     "0.75",
     "1.0",
     "1.0"
    ],
    "mark": "assumed"
   },
   {
    "label": "Portion of the review pass removed",
    "cells": [
     "35%",
     "40%",
     "45%"
    ],
    "mark": "assumed"
   },
   {
    "label": "Project closeouts a year",
    "cells": [
     "8",
     "10",
     "12"
    ],
    "mark": "assumed"
   },
   {
    "label": "Documentation assembly cost per closeout",
    "cells": [
     "$1,140",
     "$2,200",
     "$2,800"
    ],
    "mark": "assumed"
   },
   {
    "label": "Portion of closeout assembly removed",
    "cells": [
     "30%",
     "35%",
     "40%"
    ],
    "mark": "assumed"
   },
   {
    "label": "Owner agency record reviews a year",
    "cells": [
     "0",
     "2",
     "3"
    ],
    "mark": "assumed"
   },
   {
    "label": "Internal response cost per review",
    "cells": [
     "$4,000",
     "$4,000",
     "$5,000"
    ],
    "mark": "assumed"
   },
   {
    "label": "Portion of that response removed",
    "cells": [
     "35%",
     "35%",
     "40%"
    ],
    "mark": "assumed"
   },
   {
    "label": "Year one adoption ramp",
    "cells": [
     "45%",
     "55%",
     "65%"
    ],
    "mark": "assumed"
   },
   {
    "label": "Hours a year this gives back",
    "cells": [
     "about 93",
     "about 228",
     "about 354"
    ],
    "mark": "modelled"
   },
   {
    "label": "Annual value once running",
    "cells": [
     "$8,792",
     "$27,825",
     "$48,480"
    ],
    "mark": "modelled"
   },
   {
    "label": "Share of five year cost recovered",
    "cells": [
     "119%",
     "384%",
     "684%"
    ],
    "emphasis": true,
    "mark": "modelled"
   },
   {
    "label": "Payback",
    "cells": [
     "month 47",
     "month 15",
     "month 7"
    ],
    "emphasis": true,
    "mark": "modelled"
   }
  ],
  "table_note": "Every driver is a row above and none came from you. The cautious column assumes zero owner agency record reviews, so nothing in it depends on you having had a problem. About a third of that column sits in the closeout rows, and a four week baseline may not contain a closeout, so those rows can still be our assumptions when gate C is decided.\n\nRecovered hours are capacity rather than cash. About 93 hours a year on the cautious column is roughly two and a half work weeks of one person's time, and only money if you redeploy it.\n\nTwo things break the cautious column and we computed both. The two time recovery rows assume two different people. If one person does both, the column recovers 99 percent and never pays back inside five years. Separately, if running it overruns by a fifth, the column falls to 109 percent and payback slips to month 53.",
  "payback_big": "119%",
  "payback_range": "of five year cost recovered on the most cautious assumptions, paying back in month 47, just under four years. That is about 93 hours a year, roughly two and a half work weeks, and it is capacity rather than cash until you redeploy it. The middle version is month 15.",
  "base_rate_note": "The outside view here is bad and it applies to us. MIT's NANDA initiative reported in August 2025 that only about 5 percent of AI pilot programs reach rapid revenue acceleration, with the rest stalling at little or no measurable impact on profit and loss. That counts pilots without a bottom line result rather than AI not working, and we claim no exemption.\n\nFour things here are attempts to be in the minority that pays. Phase one contains no AI, so its reliability is rule coverage, checkable against your own contract documents. It asks no adoption of your field crews. Your baseline is measured before the larger commitment, and the number gets a named owner and a check at 90 days.",
  "value_owner": "Your construction administration lead should own the number, since it is their posting the whole finding came from, with whoever runs project accounting countersigning the hours baseline so the owner is not the only person who sees it."
 },
 "roadmap": {
  "title": "You can stop after two weeks and keep everything it produced",
  "lede": "Two gates inside the ask, and the first one is a genuine off ramp.",
  "body": "Phase one is twelve thousand dollars fixed, eight weeks, four thousand at gate A and eight thousand at gate B. The only irreversible commitment is the four thousand.\n\nGate A is two weeks and writes no code. It answers three questions we do not know. Whether an owner agency dictates the field record system on your federal aid work and whether you may feed it. Whether today's documentation is machine readable or sitting in scans. Which projects carry controlled markings. Two of those can go against us.",
  "now": [
   {
    "item": "Gate A, two weeks of questions and no code. Three answers in writing, sourced to your own contracts, plus a draft rulebook from one real contract",
    "metric": "The three answers exist and are sourced. Success is that they are answered, not that they are favourable"
   },
   {
    "item": "Your own four week baseline, started week one and owned by your construction administration lead. Hours per reconciliation and the count, plus the hours on the next closeout whenever it lands, since at eight to twelve a year one may not fall inside the four weeks",
    "metric": "Four consecutive weeks logged by your people, roughly ten minutes per submittal. Without it, nothing later can be judged and we would say so"
   },
   {
    "item": "Gate B, the rules only check running on two or three live projects through your 2026 closeout season",
    "metric": "Zero misses on a run against submittals your own reviewer already checked by hand. Then the funding bar, which is that the four week baseline shows at least 2.0 hours per reconciliation event and the measured reduction reaches 40 percent, which is the cautious column"
   }
  ],
  "next": [
   {
    "item": "The controlled marking and boundary decision, recorded before any component would cache project data on a field device",
    "metric": "A written scope decision per component, and no new in scope system without a recorded change"
   },
   {
    "item": "Field reports filled in on a form instead of typed free hand, at spring mobilisation 2027, while seasonal staff are onboarding anyway",
    "metric": "Hours per report day, and the share of reports submitted within 24 and 72 hours"
   },
   {
    "item": "An export into the owner agency format that produces the same file from the same records every time, built only if gate A found an export path exists",
    "metric": "Share of records accepted on first submission with no rekeying"
   },
   {
    "item": "One narrow model step, a coverage flag on requirement types the rules keep missing",
    "metric": "A named list of missed requirement types from a real closeout cycle. A short list means it does not ship"
   }
  ],
  "later": [
   {
    "item": "An evidence locator over one project's record for when a change order or claim arrives months later. It returns documents and citations, never conclusions",
    "metric": "You state the frequency first, since we could find no published figure for how often that reaches you"
   },
   {
    "item": "NEPA and permitting drafting, two of your own 24 service lines, capped at 1 to 5 hours per subsection, which is the vendor's own published benchmark rather than an independent measurement",
    "metric": "Hours per subsection against your baseline, plus the rate at which stale references get caught"
   },
   {
    "item": "Grant writing, a service line you sell rather than an overhead, which is the most interesting thing we did not pick",
    "metric": "You supply grant volume and win rate first. Until then it stays a hypothesis"
   },
   {
    "item": "Materials testing and special inspections need plain automation and not AI. Breaks, gradations and densities are structured and high volume",
    "metric": "Share of results reaching the client report with no retyping"
   }
  ],
  "gates": "Gate A, end of week two, is a real stop. You keep the answers and the started baseline, and the eight thousand is never invoiced. Gate B, end of week eight, is also a stop, and you keep a running check, the rule set your lead signed, and a before and after on your own numbers.\n\nGate C is the winter decision, by March 1st 2027, and Alaska sets that date rather than us. The spring phase gets funded only if the four week baseline shows at least 2.0 hours per reconciliation event and the measured reduction reaches 40 percent, which is the cautious column. Below either, phase one is the finding and the roadmap stops there. That comes off two or three projects, a handful of events rather than a season, so a borderline result reads as directional rather than as the bar cleared.",
  "need_from_you": "Two or three named active projects, and a line from contracts on whether they carry controlled markings. Six to eight hours of your construction administration lead in weeks three and four. Read access to where the records live, scans included. Ten minutes per submittal from your project managers for four weeks. One named person who owns the number at 90 days."
 },
 "honest": {
  "title": "Five ways this is a bad buy, and the first one could end it at week two",
  "lede": "Every one of these is answered here rather than left hanging.",
  "body": "An owner agency may own the record and refuse a feed. That is the riskiest assumption here and it is unanswered today, which is why gate A costs four thousand rather than twelve. If it goes against us we tell you at week two and this becomes the whole build rather than its first phase. Phase one still works there, since it reads what you produce.\n\nYour documentation may not be machine readable. If daily reports and materials records are scans, getting the text off them becomes the project and our estimate is wrong by a lot. Gate A measures it against a threshold we write down before we look. If it fails you stop at week two with the memo and a baseline two weeks in rather than four.\n\nOur numbers may be wrong in either direction. The four week baseline replaces our volume and hours guesses with your measurements, the reduction rows stay assumptions until gate B, and the bar is stated in advance: the four week baseline shows at least 2.0 hours per reconciliation event and the measured reduction reaches 40 percent, which is the cautious column.\n\nIt may underperform even then. If the measured reduction misses 40 percent, gate C does not fund the spring phase. You stop there and you keep the running check and the rule set your own lead signed. The running cost stays yours from that point and you can switch it off.\n\nThe rules can go stale. Standard specifications and agency manuals get revised, and a list nobody maintains reports the wrong gaps against the new ones. Naming who maintains it is a condition of finishing."
 },
 "next_step_title": "Two numbers from you turn most of this table into your own figures",
 "next_step": "Tell us roughly how many pay estimate and progress submittal reconciliations you run in a year, and roughly how long one takes. Those two move about seven tenths of the cautious column.",
 "sources": [
  {
   "claim": "Your Construction Administration posting, on administering documentation and audit trails to ensure funding participation, on statewide travel during construction season, and on the Seasonal Full-Time Hourly classification",
   "url": "https://www.rmconsult.com/job-posting/project-engineer-construction-administration/"
  },
  {
   "claim": "Your Who We Are page, on nearly 95 percent public clients, 100+ employees and founded 1969",
   "url": "https://www.rmconsult.com/who-we-are/"
  },
  {
   "claim": "Your open positions page, the eleven listed roles, and the absence of any posting dates; also your four offices, Anchorage, Fairbanks, Juneau and Wasilla",
   "url": "https://www.rmconsult.com/join-us/open-positions/"
  },
  {
   "claim": "The Senior Land Surveyor posting, on researching and writing technical portions of proposals",
   "url": "https://www.rmconsult.com/job-posting/senior-land-surveyor/"
  },
  {
   "claim": "The Senior Project Civil Engineer posting, carrying the same proposal duty in a second department",
   "url": "https://www.rmconsult.com/job-posting/senior-project-engineer/"
  },
  {
   "claim": "The Senior Environmental Geologist or Engineer posting, on developing proposals",
   "url": "https://www.rmconsult.com/job-posting/senior-environmental-geologist-or-engineer/"
  },
  {
   "claim": "Your July 14th 2026 announcement of a Proposal Manager into the Marketing Group",
   "url": "https://www.rmconsult.com/news-and-views/new-marketing-and-human-resources-professionals-join-rms-business-services-department/"
  },
  {
   "claim": "Andrea Story's bio, on specialising in proposal development",
   "url": "https://www.rmconsult.com/our-people/andrea-story/"
  },
  {
   "claim": "Your CMMC Level 2 certification announcement of December 22nd 2025",
   "url": "https://www.rmconsult.com/news-and-views/rm-achieves-cmmc-level-2-certification-with-guidance-from-stratus-services/"
  },
  {
   "claim": "Your Zweig Group 2026 placement, tenth in the 100 to 199 employee category and a fifteenth consecutive year",
   "url": "https://www.rmconsult.com/news-and-views/rm-named-one-of-zweig-groups-2026-best-firms-to-work-for/"
  },
  {
   "claim": "Your What We Do page, the 24 service lines, checked for any mention of AI or automation",
   "url": "https://www.rmconsult.com/what-we-do/"
  },
  {
   "claim": "Len Story's page, where we read the address this reached you at",
   "url": "https://www.rmconsult.com/our-people/len-story/"
  },
  {
   "claim": "DOWL's 2020 article on big data and machine learning, which claims no deployment",
   "url": "https://www.dowl.com/news/our-geobusiness-future-big-data-machine-learning-and-ai/"
  },
  {
   "claim": "DOWL's news index, page one, checked for AI and automation",
   "url": "https://www.dowl.com/company/news/"
  },
  {
   "claim": "CRW Engineering's homepage, checked for AI and automation",
   "url": "https://www.crweng.com/"
  },
  {
   "claim": "RESPEC's data and technology page, checked for AI and machine learning",
   "url": "https://www.respec.com/expertise/data-technology/"
  },
  {
   "claim": "HDR's AI statement, on prohibiting generative AI in any final work product",
   "url": "https://www.hdrinc.com/artificial-intelligence-informational-statement"
  },
  {
   "claim": "Michael Baker's April 16th 2026 announcement of its platform, its reach and its agent library",
   "url": "https://www.prnewswire.com/news-releases/michael-baker-international-unveils-titan-an-enterprise-ai-platform-powering-a-new-way-of-working-302745052.html"
  },
  {
   "claim": "ASCE Policy Statement 573, adopted July 18th 2024, on where engineering responsibility sits",
   "url": "https://www.asce.org/advocacy/policy-statements/ps573---artificial-intelligence-and-engineering-responsibility"
  },
  {
   "claim": "The 2026 Ames and Gough survey of fifteen A and E liability insurers, on AI adoption as a disruptor",
   "url": "https://www.insurancebusinessmag.com/us/news/construction/most-aande-liability-insurers-plan-rate-hikes-in-2026--ames-and-gough-566403.aspx"
  },
  {
   "claim": "The ISO generative AI exclusion endorsements effective January 2026, and that they are optional",
   "url": "https://www.independentagent.com/vu_resource/verisk-to-roll-out-new-general-liability-exclusions-for-generative-ai-exposures/"
  },
  {
   "claim": "The Louisiana DOTD evaluation of photo based field inspection, the one independent measurement in this field",
   "url": "https://rosap.ntl.bts.gov/view/dot/56247"
  },
  {
   "claim": "The federal permitting drafting benchmark, published by the vendor and assessed by nineteen subject matter experts",
   "url": "https://www.gend.co/blog/draftnepabench-ai-federal-permitting"
  },
  {
   "claim": "The outside view we hold ourselves to, on how often enterprise AI pilots show no measurable result",
   "url": "https://finance.yahoo.com/news/mit-report-95-generative-ai-105412686.html"
  }
 ]
}
```


---

## The outreach

```json
{
 "subject": "Checking R&M pay estimates before they go out",
 "body": "Nearly 95% of your work is for public clients so every pay estimate goes to an agency reviewer. A required document that never made the file is a reimbursement question.\n\nWe already did the study on flagging what's missing before the package goes out and there's no AI in it.\n\nhttps://alaskaaihq.com/awesomeproposal/rm-consultants/\n\nNo strings, we're here if you want a hand.",
 "to": "lstory@rmconsult.com",
 "to_name": "Len Story",
 "title_note": "Chief Executive Officer, R&M Consultants, Inc. Address is a live mailto on his own bio page at https://www.rmconsult.com/our-people/len-story/, re-fetched and confirmed by the fact-checker twice today, with the title reading 'to his current position as Chief Executive Officer' in the present tense. He is the BUYER, not a router. NOTE: he must never be called Board President, that string was rejected as not on the cited page. Third-party aggregators still list a CEO who retired in 2019 and none were used.",
 "link": "https://alaskaaihq.com/awesomeproposal/rm-consultants/",
 "opens_on": "Their own Who We Are page states verbatim 'Nearly 95% of our work is for public clients', so every pay estimate they send goes to a public agency reviewer before it is paid. That figure is theirs and no other firm shares it, and it sets up the recommended build instead of arriving from somewhere else.",
 "lead_critic": "ship on round 3. Rounds 1 and 2 were both rejected and BOTH REJECTIONS WERE BRIEF FAILURES RATHER THAN WRITING FAILURES, which is the Phase 7 ladder firing early rather than at round four. Round 1 opened on a verbatim quote from two of their job postings; the critic said that read as a machine diffing two pages and failed the meeting test, since OUTREACH_CRAFT holds that a duplicated posting line is evidence and evidence stays in the study. Round 2 opened on 'your senior engineers write proposal sections on top of billable work'; it passed the meeting test and failed specificity outright, because it is true of every mid-size Anchorage engineering firm. That second rejection condemned the FACT rather than the sentences, so the opening fact was changed rather than the wording patched. Round 3 shipped with zero problems and zero tells.",
 "word_count_prose": 59,
 "comma_count": 1,
 "subject_chars": 45,
 "industry_proof": "Deliberately NOT carried, and this is a judgement rather than an omission. The strongest independent number in their industry is the Louisiana state transportation department's 28 percent on daily work report creation and submission. It belongs to the spring 2027 roadmap item rather than to phase one, and the study says so in terms. Putting it in a sixty word email would have read as a promise about what we would deliver, which OUTREACH_CRAFT forbids. The honest finding that proposal automation is the loudest marketed and thinnest measured corner of the industry was carried in rounds 1 and 2 and was cut when the opening fact changed, because the critic ruled that restraint belongs in the study where the Allen Marine send taught us it belongs.",
 "roi_in_email": "None, by design. The conservative case pays back in month 47 and recovers 119 percent, and under one plausible sensitivity it never pays back at all. A number that shape needs the study's framing around it, and the friendlier alternative is exactly the hero number the gate exists to prevent. The email carries no money at all so nothing in it can be read as a projection.",
 "personalization_gate": {
  "this_company_only_fact": "Nearly 95% of their work is for public clients, verbatim from their own page, carried straight into the operational consequence that every pay estimate goes to an agency reviewer.",
  "hero_number": false,
  "kill_list_hits": [],
  "em_or_en_dashes": 0,
  "colons_semicolons_in_prose": 0,
  "cannot_used": false,
  "sentence_openers": ["Nearly", "A", "We", "No"],
  "links": 1,
  "self_reference": "none, the email never says who or what produced the study",
  "implies_a_problem_they_have_had": false,
  "passes": true
 },
 "voice_delta_note": "The close was written in the register VOICE_DELTAS flags as READY TO PROMOTE. `lengthened` now stands at SIX separate sends, where a clipped ask keeps being replaced by hand with something warmer offering help without strings. 'No strings, we're here if you want a hand.' is that register written in rather than left for Talon to add. The delivery summary carries the drafted OUTREACH_CRAFT diff for a human to approve."
}

```
