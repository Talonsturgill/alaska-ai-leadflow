# Internal dossier, The Tatitlek Corporation, 2026-09-19

PRIVATE. This file is the run's paper trail and never leaves this repo.

## The one-line story of this run

The strategist and the feasibility engineer both picked a Key Personnel and
Past Performance Evidence Engine. The engineer flagged that the whole pick
rested on one unretired assumption about GovEagle's feature set, retirable by
a single page fetch nobody had made. The showrunner made the fetch. GovEagle's
own pages already do past-performance matching, so the build was a duplicate of
software the prospect already pays for. The pick moved to a measurement, and
the study's headline finding became the coverage map, handed over free.

The study-critic then took four rounds, 27 failures to 24 to 11 to ship.

---

## PHASE 1, SELECTION

# Selection, 2026-09-19

## The pick

**The Tatitlek Corporation** (tatitlek.com), Anchorage, Alaska.
Alaska Native village corporation of Tatitlek, Prince William Sound.
Fit total **24 of 25**, the single highest of 23 merged candidates.
ai_solvable_pain 5, ability_to_pay 5, reachability 4, offer_fit 5, alaska_signal 5.
Scout source: https://tatitlek.com/our-company/

Picked on score alone, no tie-break needed.

## Reputation pre-screen (run before the room, because this segment keeps failing it)

17 of the 19 rows in ledger/suppressions.json are Alaska Native corporations
disqualified on values, almost all of them for ICE detention contracting or for
federal-contracting fraud on the exact ground we would sell into. So the screen
ran before the research room was spent, not after.

- ICE and immigration detention contracting: two searches returned no link
  between Tatitlek or its subsidiaries and immigration enforcement or detention.
- False Claims Act, 8(a) fraud, self-dealing: no settlement, suit or
  investigation surfaced.

Clean so far, and NOT yet cleared. The research room carries an explicit
reputation brief and the RESEARCH GATE still applies. If either comes back
positive, suppress and take the next name below.

## Replacement queue, ranked (use in this order on any disqualification)

 1. Gana-A'Yoo, Limited            ganaayoo.com              23  ANC
 2. Huna Totem Corporation         hunatotem.com             23  ANC
 3. Orthopedic Physicians Alaska   opalaska.com              23  healthcare
 4. Alaska Travel Adventures       alaskatraveladventures.com 23 tourism
 5. Northern Alaska Tour Company   northernalaska.com        23  tourism
 6. Cook Inlet Housing Authority   cookinlethousing.org      22  ANC
 7. The Kuskokwim Corporation      kuskokwim.com             22  ANC   (site would not render, re-verify first)
 8. Alaska Premier Dental Group    smilealaska.com           22  healthcare
 9. Anchorage Veterinary Clinic    anchoragevetclinic.com    22  healthcare
10. Solstice Alaska Consulting     solsticeak.com            22  SMB
11. St. George Tanaq Corporation   tanaq.com                 21  ANC
12. Advanced Physical Therapy AK   aptak.com                 21  healthcare
13. Alaska X (Alaska Excursions)   alaskax.com               21  tourism
14. Imaging Associates             imagingak.com             20  healthcare
15. Alaskan Home Health            alaskanhomehealth.com     20  healthcare
16. Cruz Construction              cruzconstruct.com         20  SMB
17. Island Air Service             flyadq.com                20  tourism
18. Alaska Tour & Travel           alaskatravel.com          20  tourism
19. Taiga Ventures                 taigaventures.com         19  SMB
20. Amak Towing Company            amaktowing.com            18  SMB
21. Alaska Logistics Services      alaskalogistics.net       17  SMB
22. Northern Air Cargo             nac.aero                  17  SMB

If the queue empties, re-scout the under-covered segments before any no_lead
ending is even considered.

## Dedupe

Computed with `ledger.py check` on all 23 domains, not eyeballed. Zero hits
against the 39-domain EXCLUDE set. tatitlek.com is clean.

## Seasonal context handed to the scouts

Federal fiscal year ends September 30th, the heaviest solicitation and award
window of the year. Summer visitor season closing statewide. Last barge runs to
western and northern Alaska. Freeze-up ahead. 2026 PFD lands early October.
Legislature out of session.


---

## PHASE 2, RESEARCH GATE

# RESEARCH GATE, 2026-09-19, The Tatitlek Corporation

## Verdict: PASS, proceed to Phase 3.

## Real, operating Alaska business, confirmed from more than two independent pages
- tatitlek.com, their own site, seven named subsidiaries each with UEI, CAGE and NAICS.
- BLM, final ANCSA patents signed April 11th, 2024, 137,245.79 acres.
- USAspending prime-award API, live federal awards through September 1st, 2026.
- Alaska Business Magazine, July 7th, 2026, on the new president.
Not a shell, not stale, not a national chain with an Alaska pin.

## Reputation and values, the screen this segment keeps failing

17 of the 19 rows in ledger/suppressions.json are Alaska Native corporations
dropped on values. The two recurring reasons are immigration detention
contracting and federal-contracting fraud. Both were screened here, twice,
first before the room was spent and again with the room's findings in hand.

FRAUD: nothing found. No False Claims Act settlement, no DOJ, GSA OIG or SBA
OIG action, no debarment, no 8(a) size-protest or self-dealing finding, across
the parent and every subsidiary name. The one adjacent item is a 2012 wage-and-
hour class action against Tatitlek Support Services over role-player overtime
and misclassification, fourteen years old, and not contracting fraud.

IMMIGRATION: one adverse item, and it does not hold up. A single sentence in an
Anchorage Daily News piece of July 24th, 2018 lists "Tatitlek Native Corp.
subsidiary GeoNorth" among ANCs holding border-control contracts over the prior
fifteen years. It gives no contract, no agency, no amount, no date and no
detention role. It uses the wrong corporate name. Three parallel investigations
that DO name the suppressed corporations do not name this one.

So the showrunner checked it against primary data rather than leaving it at a
judgement call. Four USAspending recipient searches, award types A through D,
roughly 270 award rows: the Tatitlek parent family back to FY2015, GeoNorth back
to FY2008, Tatitlek Support Services, Tatitlek Training Services.

RESULT: zero immigration, customs, border or detention awards anywhere. Every
Department of Homeland Security dollar in the data is U.S. Coast Guard, and the
descriptions say what it is, Rescue 21 Alaska sustainment (the Coast Guard's
maritime search-and-rescue distress calling system), the Alaska VHF
communication system, Digital Selective Calling, Vessel Traffic Service, and
guard services at Coast Guard bases. GeoNorth's largest customer by row count is
the Indian Health Service, 52 of 100 rows. Its DoD work is imagery libraries and
web content management.

An initial keyword screen flagged seven rows. All seven were the matcher finding
"ICE" inside "SERVICE" and "PRICE". None is an immigration contract.

## Why this is a pass and not a quiet lowering of the bar

The bar actually applied to the seventeen suppressed corporations was CURRENT,
SUBSTANTIAL and DETENTION-SPECIFIC: shareholders publicly demanding divestment,
Krome and Guantanamo, an 800-bed processing center, a $35M guard contract at
Port Isabel, an ICE award six days before the run, detention operation services
in the company's own words. Tatitlek meets none of it, and the primary data
contradicts the only sentence that suggested otherwise. Suppressing on this
evidence would hold Tatitlek to a standard no shipped lead was held to.

## Residual uncertainty, recorded rather than dropped

What GeoNorth's 2018-era border-control work actually was is still unestablished.
It does not appear in prime-award data for the period, which leaves an expired
pre-2008 award or a subcontract as possibilities neither confirmed nor excluded.
This does not reach the suppression bar. It is written down here so a later run
that finds more can weigh it against what this run knew.

## What the study may NOT do with this

Nothing in the study or the email touches immigration, detention, the ADN piece,
or the values screen. That is internal qualification, not prospect-facing
material, and putting it on a page would be both irrelevant and insulting.


---

## PHASE 3, FEASIBILITY PASS ONE AND WHY IT WAS RE-RUN

# Feasibility pass 1, and why it was re-run

Pass 1 walked the ladder on all five candidates and returned:
- Key Personnel and Past Performance Evidence Engine: DOWNSCOPE, recommended pick
- Data Call Runner: DOWNSCOPE, renamed Data Call Tracker, agent washing called out
- LLM Disclosure and Incident Register: KEEP, and explicitly mostly-not-AI
- Bid/No-Bid Capacity Check: KILL, fails the GeoNorth question outright
- Shareholder Preference Talent Matcher: KILL, motivating argument is on the rejected list

Its first honest_flag was that the whole pick rested on an unretired assumption:
nothing verified said what GovEagle's feature set covers, and the assumption was
retirable by one public page fetch this run had not made. It named the cost of
being wrong, proposing a duplicate of a tool they already bought, to the VP of
Business Development, inside a study whose posture is that we sit beside the tool
they chose.

THE SHOWRUNNER MADE THAT FETCH. GovEagle's own pages (C48 to C51) show it
already maps task areas to past performance, matches PWS requirements to the
strongest projects, and drafts from past-performance write-ups. The condition
the engineer set has fired. The past-performance half of the recommended pick is
dead on verified evidence.

Whether GovEagle handles key-personnel RESUMES is still unverified. It is named
on no page fetched and asserted only by search summaries, which is the same
standard that rejected the ADN sentence. DATA CALLS appear nowhere on any
GovEagle page fetched.

So the engineer is re-run on corrected facts rather than the showrunner picking
the build itself. That is a retry replacing the same planned agent, not an
addition to the spawn plan.


---

## PHASE 3, THE LOCKED PICK

# THE LOCKED PICK, 2026-09-19, The Tatitlek Corporation

## The locked build

**A free GovEagle coverage map, then one measured data call, then a deterministic
Data Call Tracker they own.**

The locked build is the ai-feasibility-engineer's recommended pick from pass two.
No model sits in the shipped path. The headline deliverable is not the tracker,
it is the coverage map, and it costs them nothing.

## How the pick moved, and why that is the point

The strategist's provisional pick was a Key Personnel and Past Performance
Evidence Engine. It topped the Ulwick board at 15 and the RICE ranking at 7.0.
The feasibility engineer kept it in pass one and then flagged, as its first
honest note, that the whole thing rested on an assumption nobody had retired:
nothing verified said what GovEagle's feature set covers, and one page fetch
would settle it.

The showrunner made the fetch. GovEagle's own pages say it maps task areas to
past performance, matches PWS requirements to the strongest projects, and drafts
from past-performance write-ups (C49, C50, C51). The past-performance half of
the recommended build was already on an invoice Tatitlek is paying.

That is the run working. A study that shipped the Evidence Engine would have
offered a duplicate of a tool they already bought, to the Vice President of
Business Development whose own requisition names it.

## Cagan's four risks, checked before locking

**Feasibility.** The engineer walked the ladder. The shipped tracker is rules,
a scheduler and a completeness board, with zero required model steps, so there
is no compounding-error chain and every step can be tested exhaustively. Lowest
risk on the board.

**Value.** THE WEAK LEG, and it is not papered over. Nothing fetched says their
data calls are slow. The entire evidence base is one clause in one posting
saying the new hire participates in them (C11). No baseline exists. The pick
answers this by making the first paid deliverable a MEASUREMENT rather than a
tool, and by stating out loud that if the measurement says the process holds,
the honest recommendation is that they buy nothing.

**Usability.** A completeness board read against a compliance matrix GovEagle
already produces (C48, C51). The proposal manager approves the recipient list,
the system chases on a schedule a human set. It never authors a fact and never
writes into a submitted volume.

**Business viability FOR THIS OWNER.** Affordability is not in question.
Adoption has a natural owner, the Dahlgren seat posted at $130,000 and up (C09),
and landing alongside that hire beats landing after it invents a manual method.
The honest weakness is that GeoNorth Information Systems, their own NAICS 518210
subsidiary (C05), can build this. So we do NOT sell an exclusive build. We sell
the specification, the owner-map extraction method, the acceptance bar and the
speed, and we say in the study that the tracker should end up theirs, hosted and
owned by GeoNorth. A company that owns an information-systems subsidiary would
be insulted by any other position.

Viability holds for a spec-and-measurement engagement. It does NOT hold for an
exclusive build, so the study does not ask for one.

## ECONOMICS PRE-CHECK, before the engineering room burns

**The ask is sized here, and the roi-analyst builds the case for THIS ask, not
for the biggest build we can imagine.**

**Phase 0, free.** The GovEagle coverage map, which parts of the job their own
tool's pages already cover, handed over at no charge. Plus the two questions only
their GovEagle rep can answer, does it handle key-personnel resumes, and does
Team assignments reach contributors outside the proposal team. This is the part
of the study with the highest value to them and we charge nothing for it.

**Phase 1, the ask.** One real data call measured end to end, plus the owner-map
extraction method and the tracker specification with its acceptance bar. Small,
a few weeks, priced in the low five figures.

**Does the conservative case clear at that size?** Yes, and by construction
rather than by optimism. The honest return of Phase 1 is DECISION DATA, a
measured baseline that gates any further spend, which the ROI method explicitly
permits as a qualifying ask shape. They finish Phase 1 knowing what one data
call actually costs them and holding a specification they can hand to GeoNorth.
If the measurement shows the process is fine, they have bought the right to stop,
which is worth the price of not building the wrong thing.

**What the ROI table will honestly look like.** Mostly `assumed` marks and
possibly no `verified` row at all. No baseline exists, the pursuit count is
unknown, and the 30-pursuits-per-quarter figure in the RICE score is invented and
may not be used. The Field Study contract blesses this outcome directly: a table
with no verified row tells the reader plainly that nothing in it is yet a fact
about their business, which is exactly what a pilot is for. The roi-analyst is
briefed to build it that way rather than to manufacture certainty.

**No-pay gate: NOT fired.** An honest ask exists at a size the conservative case
clears. Proceed to Phase 4.

## What the engineering room must NOT do

- Never suggest they are starting from nothing. They run GovEagle (C08).
- Never duplicate anything C48 to C51 shows GovEagle already doing.
- Never resolve the GovEagle resume question in either direction. It is
  unverified and it stays a question put to them.
- Never assert that data calls are slow. Nothing fetched says so.
- Never assert they are in scope for the proposed GSA disclosure rule. C46
  covers LLMs used in the PERFORMANCE of a contract, and capture is pre-award.
  The strategist asserted this and the engineer struck it.
- Never write the proposed GSA rule as a current obligation. C45, C46 and C47
  are all PROPOSED.
- Never imply the MDA award is under review or at risk (C26 FORBIDDEN_USE).
- Never use the invented 30-pursuits-per-quarter figure in any number.

## The replacement queue is untouched

No company was disqualified. The BUILD changed, twice, which is the discovery
room doing its job. Tatitlek remains the lead.


---

## RETRO MATERIAL GATHERED DURING THE RUN

# Retro material, gathered as it happened, 2026-09-19

## THE PATTERN OF THE RUN: three gates reading keys their producers do not emit

All three found in one run, all the same shape, a checker and its producer
drifting apart with nothing asserting they still agree.

1. room_reconcile read feasibility.json["kill_list"]. The
   ai-feasibility-engineer contracts `verdicts`. The killed-capability check
   had been examining an empty list and reporting success. Three candidates
   were killed this run and the gate passed on nothing. FIXED AND VERIFIED.
2. study_lint read rejected_do_not_use entries as strings. The fact-checker
   contracts them as OBJECTS. The gate died with a TypeError and took the
   whole Phase 6 lint out before any critic saw the study. FIXED AND VERIFIED.
3. quote_fidelity read entry["quote"] while claims.json stores "verbatim",
   AND matched only lowercase bare `c\d+` ids while this run's ids are
   uppercase and quoted. Either alone empties the check. The demo-builder hit
   it, worked around it by carrying no quotations, and flagged it in its
   handback, which is the only reason it was found. FIXED AND VERIFIED.

Only number 1 announced itself, because it prints a NO KILL LIST note when the
list is empty. That note is the reason the pattern was visible at all, and it
is the design worth copying: a gate that examines nothing should say so.

## OBSERVED, NOT FIXED, ceiling of three already spent

dup_clause on the RENDERED study page returns 77 false positives. The renderer
emits the entire document body as one 38,573-character line, so the tool's
"one line is one edit unit" rule collapses and every legitimate cross-section
repetition is flagged. The brief is REQUIRED by FIELD_STUDY_SPEC to restate the
body so it survives being forwarded alone, so those repeats are the contract
working. Pointed at the demo, which is what it was built for, it is clean.
This is a usability trap rather than a defect in the check, and the contract
does not list dup_clause as a Phase 6 gate. The fix if it ever earns one is to
run it over study.json's strings rather than the rendered HTML.

## SPAWN-PLAN NOTE

product-strategist and ai-feasibility-engineer carry `tools: Read` and cannot
persist their own output, so the showrunner transcribes it. That is the open
MACHINE_BACKLOG item from 2026-08-08, closed on 2026-08-09 for the four Phase 4
agents (which now have Write and a PERSIST block and wrote their own files
cleanly this run) but never extended to the two Phase 3 agents. It bit twice
this run. Note the in-flight discovery already recorded in that entry: agent
definitions load at SESSION START, so adding Write now could not take effect in
this run anyway.

## THE PICK MOVED TWICE AND THAT IS THE RUN WORKING

The strategist's provisional pick and the feasibility engineer's pass-one pick
were both a Key Personnel and Past Performance Evidence Engine. The engineer
flagged, as its first honest note, that the whole pick rested on an unretired
assumption retirable by one page fetch. The showrunner made the fetch and
GovEagle's own pages killed the build. Cost: one extra feasibility pass.
Value: the study did not quote a prospect a second copy of software he already
runs. That trade is worth taking every time, and the lesson is that an agent
naming a cheap decisive check should have it run before the room burns.


---

## DISCOVERY (the full opportunity map, verbatim)

```json
{
  "opportunity_map": [
    {
      "area": "Capture and pipeline management (BD front end)",
      "what_ai_could_change": "Already changed, and this is the anchor fact. Their own live requisition 2026-2731 names GovEagle as 'our Artificial Intelligence (AI) Tool' and requires the hire to log, stage and update each pursuit in it from identification through award decision (C08, C10). AI could still change what GovEagle does not hold, the evidence a pursuit needs rather than the pursuit record itself. Anything proposed here must sit beside GovEagle or explain why it sits elsewhere."
    },
    {
      "area": "Key personnel resumes for solicitations",
      "what_ai_could_change": "The posting assigns a $130,000-and-up seat (C09) to 'the development and scrubbing of key personnel resumes, so they align with solicitation requirements' (C11). Retrieval over their own resume corpus plus structured extraction against a shredded requirements list could turn a rewrite into a review. This is document work over material they already own, not a judgement call."
    },
    {
      "area": "Data calls across the delivery organisation",
      "what_ai_could_change": "The same hire participates in 'any and all data call activities as needed' (C11) across 1,300 employees in 46 locations worldwide (C03, C04) and seven subsidiaries (C05). AI could identify who holds the answer, draft the ask, normalise what comes back and report completeness against the compliance matrix. The hard part is orchestrating people, not generating text."
    },
    {
      "area": "Proposal production, compliance and scheduling",
      "what_ai_could_change": "Least headroom of the obvious candidates. A standing Bid and Proposal team already 'owns the proposal process, scheduling, and compliance' (C12), and GovEagle is in the pipeline (C08). Industry self-reports 84 hours to develop one proposal (C29, a Deltek survey self-report, not a measurement of Tatitlek). Peers report real gains here (C39, C41), but C42 is the qualifier, SPATHE's 24 hour result is a Red Team ready draft, not a submission ready proposal. Proposing a writer to a company with a staffed writing function is proposing a replacement."
    },
    {
      "area": "Price to win and gate review materials",
      "what_ai_could_change": "The hire develops 'capture plans, price to win analysis, and gate review materials' and presents them to the Director and senior leadership (C14). AI could assemble the deck from pipeline and past-performance facts. It should not produce the price-to-win number itself, that is a judgement with a cost of error measured in award decisions."
    },
    {
      "area": "Bid/no-bid against real delivery capacity",
      "what_ai_could_change": "The posting requires coordination 'with operations, contracts, pricing, and program staff to align capture strategy with business goals and execution capacity' (C13), while about 150 requisitions sit open (C16) and 22 still carry 2025-series numbers (C15). A join between the pipeline and actual staffing state would make a gate review honest. It needs systems we have never seen, so it is the highest strategic value and the lowest data readiness on the map."
    },
    {
      "area": "Recruiting and requisition throughput",
      "what_ai_could_change": "About 150 open requisitions across three pages on September 19th (C16), 22 carrying 2025-series numbers, the lowest 2025-2195 (C15). Screening, requirement matching and letters of intent for key personnel are ordinary AI work. Note C17 honestly, no Alaska location appeared on the iCIMS board that day and Prince William Sound and Valdez work routes through a separate TCC channel, so the board is not the whole hiring surface."
    },
    {
      "area": "Shareholder services and the hiring preference",
      "what_ai_could_change": "They publish preference for 'shareholders, shareholder descendants and shareholder spouses who meet job qualifications' (C18) against more than 300 shareholders (C02). Matching a preference pool to open roles across 46 locations is a real matching problem. It is also HR-private data, and the claims file warns directly against reading the board as a contradiction of the preference (C17), so the motivating evidence is thin."
    },
    {
      "area": "Contract vehicle administration",
      "what_ai_could_change": "Five published vehicles and certifications, ISO 9001:2015, ANC 8(a) sole source, SEAPORT NXG, GSA STARS III, OASIS+ 8(a) and SB (C06). Each carries its own ordering process and reporting. Retrieval over vehicle terms so a capture manager gets the right ordering path in seconds is low-risk, high-frequency work."
    },
    {
      "area": "AI governance and disclosure under the proposed GSA rule",
      "what_ai_could_change": "Mostly not an AI problem, which is worth saying. GSA posted an AI-specific acquisition rule to the Federal Register on June 17th, 2026 defining four contractor roles (C45). It would require disclosure of all LLMs used in performance within 120 days (C46) and notification within 72 hours of an LLM-related incident (C47). Both are PROPOSED, not in force. It applies to GSA government-wide vehicles, and C06 confirms Tatitlek holds OASIS+ and STARS III. They already run an AI tool in the business (C08), so a register and a workflow is the answer, deterministic, not a model."
    },
    {
      "area": "Demonstrating self-performance on 8(a) work",
      "what_ai_could_change": "Hegseth said the Pentagon is 'doing away with these pass-through schemes' and will 'make sure that every small business getting a contract is the one actually doing the work' (C25, attributed to the Anchorage Daily News). Evidence assembly, who did which labour hours on which award, is a records problem AI could shape. No source says anything about Tatitlek's own awards, and nothing here may be written as though it does."
    },
    {
      "area": "Contract and award record keeping",
      "what_ai_could_change": "Tatitlek Management Services holds a Missile Defense Agency award made 8(a) sole source with one offer received (C22), potential value $99,981,096.40, $11,707,278.07 obligated to date, base period October 8th 2025 to October 7th 2027 (C23). Turning award records into reusable past-performance narrative is retrieval work over public and internal documents."
    },
    {
      "area": "Contracting officer facing marketing",
      "what_ai_could_change": "They already sell the path directly, 'Reduce procurement cycle time with a direct 8(a) sole-source award, ideal when schedule sensitivity is paramount' (C07). AI could generate a tailored capability package per agency. Low value, they can write this themselves, and marketing copy is the shallowest end of what we do."
    },
    {
      "area": "Delivery on DoD sites, facilities, security, installation support",
      "what_ai_could_change": "Honestly, very little that we could build from the outside. This work happens on customer sites under customer rules, and DoD is exempt from the federal AI use-case inventory GAO reported (C33), so we cannot even see the customer's own posture. Anything touching controlled or contract data needs the customer's authorisation, not ours. Name it and leave it."
    },
    {
      "area": "Geospatial and information systems (GeoNorth)",
      "what_ai_could_change": "This is a build-versus-buy constraint, not an opportunity. GeoNorth Information Systems is one of their seven listed subsidiaries (C05), and both GeoNorth and Tatitlek Technologies were verified at NAICS 518210, data processing and hosting. They can host, run and extend anything we hand over. Any proposal has to survive the question 'why would we not have GeoNorth build this'."
    },
    {
      "area": "Front desk, phones and reception",
      "what_ai_could_change": "Nothing worth proposing, and this is here so the map is not quietly edited to flatter our catalogue. A federal services contractor with 1,300 employees across 46 locations (C03, C04) does not win or lose on inbound calls. A voice or front-desk agent would be the wrong product sold to the right company."
    },
    {
      "area": "Executive continuity and institutional knowledge",
      "what_ai_could_change": "Long tenures at the top, CEO since 2006 (C19), President since 2018 (C20), COO since 2015 (C21). Where an organisation runs on people who have been there that long, the corporate memory is in heads and in files, not in systems. Retrieval over their own documents is the only honest way to make that memory queryable, and it is a Later item, not a first build."
    }
  ],
  "outcome": "Tatitlek puts more qualified bids in front of its customers each quarter without adding BD or proposal headcount beyond the one Dahlgren seat it is already funding at $130,000 and up (C09), and the hours the 1,300-person, 46-location organisation (C03, C04) burns answering data calls and rewriting resumes fall. Measured three ways, all falsifiable against a baseline they hold today. One, submitted proposals per quarter. Two, elapsed hours from RFP release to a complete key-personnel package, which is the thing C11 names. Three, the share of a bid's required resumes that are solicitation-aligned before the data call closes. Not measured by whether a tool is installed. If those three numbers do not move, the build failed, whatever else it did.",
  "opportunities": [
    {
      "job": "When a solicitation names key personnel requirements, produce resumes for named staff that provably map to those requirements, so the bid is compliant and scores well.",
      "pain_source": "C11, the posting assigns 'the development and scrubbing of key personnel resumes, so they align with solicitation requirements' to the new hire. C09, that seat is posted at $130,000.00+ DOE.",
      "current_workaround": "A senior person, by hand, in Word. The company is buying a $130,000-plus seat that carries this duty, which is the clearest statement in the whole file about what it costs them today.",
      "importance": 9,
      "satisfaction": 3,
      "opportunity_score": 15,
      "notes": "Highest score on the board. Importance is compliance-critical, a non-aligned resume is a scored weakness. Satisfaction is low by revealed behaviour, you do not put a task on a $130,000 seat if it is already handled. Torres cross-check, sizing is every pursuit with key personnel across seven subsidiaries (C05), strategy fit is strong because two Alaska Native peers report gains in exactly this lane (C39, C43), and willingness to pay is already demonstrated in cash."
    },
    {
      "job": "When a proposal needs facts from across the delivery organisation, get them from the right people in 46 locations fast enough to hold the proposal schedule.",
      "pain_source": "C11, 'participation in any and all data call activities as needed'. C04, 1,300 employees dispersed through offices throughout Alaska and 46 locations worldwide. C12, the Bid and Proposal team owns scheduling.",
      "current_workaround": "Email and spreadsheets and chasing people, inferred from the fact that a capture manager is assigned to participate in the calls rather than to receive their output.",
      "importance": 9,
      "satisfaction": 4,
      "opportunity_score": 14,
      "notes": "Converges with the job above, both are the same underlying need, the corporate memory of who we have and what they have done. Separated here because the solutions are different in kind, one is retrieval over documents, the other is orchestration of humans. Satisfaction is a notch higher because a standing Bid and Proposal team (C12) already runs a process around it."
    },
    {
      "job": "When an RFP drops, get to a compliant Red Team ready draft without burning the team.",
      "pain_source": "C29, contractors in Deltek's survey reported an average of 84 hours spent developing a single proposal. C12, the Bid and Proposal team owns proposal process, scheduling and compliance.",
      "current_workaround": "A staffed Bid and Proposal team (C12) plus GovEagle in the capture pipeline (C08).",
      "importance": 9,
      "satisfaction": 6,
      "opportunity_score": 12,
      "notes": "THE OBVIOUS IDEA, AND IT IS NOT THE WINNER, which is the point of scoring before solutioning. Importance is as high as anything here, but satisfaction is the highest on the board because they already bought a GovCon AI tool (C08) and already staff the function (C12). C29 is a survey self-report about 917 contractors (C27), not a measurement of Tatitlek, and any use of it has to say so. C42 caps the peer evidence honestly, the SPATHE 24 hour result is a Red Team ready draft, not a submission ready proposal."
    },
    {
      "job": "Before committing to a pursuit, know whether we can actually staff and deliver it.",
      "pain_source": "C13, 'Coordinate with operations, contracts, pricing, and program staff to align capture strategy with business goals and execution capacity on assigned pursuits.' C16, about 150 open requisitions. C15, 22 listings carrying 2025-series requisition numbers.",
      "current_workaround": "Cross-functional coordination between four named functions, which is a meeting.",
      "importance": 8,
      "satisfaction": 4,
      "opportunity_score": 12,
      "notes": "Strategically the biggest prize on the map and the least buildable from outside. Torres market-position check fails us here, this lives inside their staffing, pricing and contracts systems, which is GeoNorth's home ground (C05), not ours. C13 is a coordination requirement in a job posting, not evidence that the coordination is failing, so importance is inferred and satisfaction is a guess."
    },
    {
      "job": "Fill open requisitions, including long-open ones, while honoring the shareholder preference.",
      "pain_source": "C16, about 150 open requisitions across three pages on September 19th. C15, 22 still carry 2025-series numbers, the lowest 2025-2195. C18, published preference for shareholders, shareholder descendants and shareholder spouses who meet job qualifications.",
      "current_workaround": "The iCIMS board, plus a separate TCC hiring channel for Prince William Sound and Valdez work (C17).",
      "importance": 8,
      "satisfaction": 5,
      "opportunity_score": 11,
      "notes": "Delivery capacity is literally what a services contractor sells, so importance is real. C15 is explicitly hedged as an observation on one day, and the inference that iCIMS IDs are year-prefixed is NOT a fetched fact, so 'these have been open a year' may not be said. C17 forbids pairing the board with the shareholder preference as a contradiction, which removes the most persuasive version of this argument, correctly."
    },
    {
      "job": "Find and shape the right opportunities early enough to influence them.",
      "pain_source": "C30, Deltek found 83 percent of contractors missed opportunities in 2025 because they discovered them too late.",
      "current_workaround": "GovEagle, which is where pursuits are logged, staged and updated from identification through award decision (C08, C10), plus the vehicle portals behind C06.",
      "importance": 8,
      "satisfaction": 6,
      "opportunity_score": 10,
      "notes": "Discovery is the core of what a capture tool sells. Proposing it means proposing to replace a tool they chose and deployed. Satisfaction is set high deliberately. The pain source is also industry-wide survey data, not a Tatitlek statement, which caps confidence in any build built on it."
    },
    {
      "job": "Get capture plans, price to win and gate review materials in front of the Director and senior leadership on schedule.",
      "pain_source": "C14, 'Develop capture plans, price to win analysis, and gate review materials for assigned pursuits, and present these materials to the Director and senior leadership as required.'",
      "current_workaround": "The capture manager builds them, by hand, per pursuit.",
      "importance": 7,
      "satisfaction": 4,
      "opportunity_score": 10,
      "notes": "Assembly of the deck is automatable. The price-to-win number is not, and should not be, the cost of error is an award decision. A build here has to be explicit about which half it touches, which is a good discipline and a small prize."
    },
    {
      "job": "Know and be able to disclose what large language models are used in performance of our contracts.",
      "pain_source": "C45, GSA posted an AI-specific acquisition rule defining four contractor roles. C46, disclosure of all LLMs used in performance within 120 days. C47, notification within 72 hours of discovering an LLM-related incident. C06, they hold OASIS+ and GSA STARS III. C08, they already run an AI tool in the business.",
      "current_workaround": "Nothing evidenced. If it exists today it is a spreadsheet, and it may not exist because the obligation does not exist yet.",
      "importance": 6,
      "satisfaction": 2,
      "opportunity_score": 10,
      "notes": "The most underserved job in raw satisfaction terms and deliberately not the most important, because C46 and C47 are PROPOSED and not in force, and writing them as a current obligation would be a lie. Importance rises sharply if the rule lands. Real clock, conditional trigger."
    },
    {
      "job": "Be able to show, on demand, that the entity holding the contract is the one doing the work.",
      "pain_source": "C25, Hegseth said 'we're doing away with these pass-through schemes. We'll make sure that every small business getting a contract is the one actually doing the work', reported by the Anchorage Daily News.",
      "current_workaround": "Contract administration records and timekeeping.",
      "importance": 7,
      "satisfaction": 5,
      "opportunity_score": 9,
      "notes": "Industry policy context, not a stated Tatitlek pain, and the file is explicit that no source says anything about Tatitlek's awards being reviewed or at risk (C26 FORBIDDEN_USE). Confidence in this job is therefore low by construction and it must never be dramatised. Kept on the map because the underlying records problem is real for every ANC."
    },
    {
      "job": "Show a contracting officer quickly why the 8(a) sole source path fits their schedule.",
      "pain_source": "C07, their own page, 'Reduce procurement cycle time with a direct 8(a) sole-source award, ideal when schedule sensitivity is paramount.'",
      "current_workaround": "Their website and capability statements, which already say this well.",
      "importance": 5,
      "satisfaction": 6,
      "opportunity_score": 5,
      "notes": "Satisfaction exceeds importance, so the opportunity term is zero. They are already good at this. Listed so the map is complete and so nobody circles back to it later thinking it was missed."
    }
  ],
  "target_opportunity": {
    "job": "Produce the people-and-past-performance evidence a bid needs, key personnel resumes mapped to solicitation requirements plus the data-call answers behind them, from a 1,300-employee, 46-location, seven-subsidiary organisation, fast enough to hold the proposal schedule.",
    "why": "It carries the highest Ulwick score on the board, 15, and it is the only high-importance job where satisfaction is genuinely low. It is also the only job whose cost Tatitlek has stated in dollars, they are hiring a seat at $130,000 and up (C09) whose named duties include resume scrubbing against solicitation requirements and participation in any and all data calls (C11). That is revealed willingness to pay, which beats any survey number in this file. It sits in the gap GovEagle leaves, GovEagle holds the pursuit record from identification through award decision (C08, C10), which is a pipeline, not a corpus of their own people and their own past work. Torres cross-check. Sizing, every pursuit that names key personnel, across seven subsidiaries (C05) and five vehicles (C06). Market position, we are not competing with the tool they chose, we sit beside it, which is the only position worth holding here. Strategy fit, two Alaska Native peers have publicly reported results in this exact lane, K Corp at a 60 percent reduction in proposal preparation time with zero new hires (C39) and Koniag with a narrow non-generative automation cutting a one-hour task to two minutes (C44). Care versus satisfaction, high care, low satisfaction, which is the definition of underserved. ONE HONEST CAVEAT, stated up front rather than buried. Nothing in the verified file tells us what GovEagle's feature set covers. If it already carries a resume and past-performance module, this target collapses and the right answer moves to the AI disclosure register or the data-call agent. That is one question to Wamsher, and it should be asked before a line of code, not after.",
    "forces": "PUSH, they are about to spend $130,000-plus a year (C09) on a seat that includes rewriting resumes to match solicitations (C11), and the industry self-reports 84 hours per proposal (C29, a survey of 917 contractors, not of Tatitlek). PULL, the two most relevant peers in the file are both Alaska Native corporations reporting real gains, K Corp at 60 percent less proposal prep with no new hires (C39) and a threefold increase in monthly submissions (C40), and Koniag's DORA, a narrow non-generative SAM.gov automation credited in an AWS case study with cutting a one-hour task to two minutes (C44). Both are vendor-published and not audited, and that has to be said every time they are used. ANXIETY, high, and it is the force that decides this. TRAX alleges in live Court of Federal Claims litigation that the Army used AI that hallucinated multiple times during a source selection (C37), and the Army conceded one identified weakness was not supported by the record (C38). The proposed GSA rule would make every LLM used in performance a disclosable item within 120 days (C46) with 72-hour incident reporting (C47). Deltek found 45 percent of contractors unclear on the return on AI and only 5 percent fully mature (C31). HABIT, strong, GovEagle is already the system of record for pursuits (C10) and the Bid and Proposal team already owns process, scheduling and compliance (C12). VERDICT, push plus pull exceeds anxiety plus habit ONLY for a build that retrieves and assembles from their own documents with a human approving every output, that stays out of the technical volume, and that stays out of controlled and contract data. Anxiety here is lowered by the shape of the build, not by argument. A generative proposal writer flips the same verdict to no."
  },
  "candidates": [
    {
      "name": "Key Personnel and Past Performance Evidence Engine",
      "our_build": "RAG over their own files, plus the paperwork engine",
      "what_it_does": "Ingests the resume and past-performance material the seven subsidiaries (C05) already hold. When a solicitation arrives, it shreds the key-personnel and past-performance requirements into a checklist, retrieves the candidate people and prior work that match, and produces a requirement-mapped resume draft plus a gap list saying exactly what is missing and who has to answer for it. Every output is a draft a human edits and approves, it exports to their own Word templates, and it writes nothing into GovEagle, it hands the capture manager a finished artefact to attach to the pursuit GovEagle already holds (C10). CONTRACT DATA POSITION, stated plainly because it changes what is buildable. Resumes are personal data and some past-performance narrative touches contract detail, so the corpus is scoped to BD-releasable material only, nothing controlled, nothing from a DoD site, and the store lives where their own IT controls it, which GeoNorth can host (C05, NAICS 518210). If the GSA rule lands as proposed, the models in this pipeline become disclosable within 120 days (C46), so a model inventory is a day-one design output, not a later retrofit.",
      "rice": {
        "reach": "Every pursuit that carries a key-personnel or past-performance requirement, plus the named staff drawn from 1,300 employees across 46 locations (C03, C04). Modelled at 30 pursuits per quarter. STATED ASSUMPTION, the pursuit count is not a fetched fact, nothing in the verified file gives one, and it must be replaced with their real number before any ROI is built on it.",
        "impact": "2, massive. It hits the exact task their own posting puts on a $130,000-plus seat (C11, C09), and the peer evidence for this lane is the strongest in the file (C39, C44).",
        "confidence": "70 percent. Discounted from high because the pain is primary and verbatim from their own requisition, but we cannot see GovEagle's feature set, we have never seen the state of their resume corpus, and the peer results (C39, C40) are vendor-published statements about vendor customers, not audits.",
        "effort": "6 person-weeks",
        "score": "30 x 2 x 0.70 / 6 = 7.0"
      },
      "cost_of_delay": "Real and dated. The Dahlgren seat is live now at $130,000 and up (C09). Whoever fills it will build a personal manual method for doing C11 within a quarter, and that method becomes the habit any build then has to displace. Landing this alongside the hire costs a fraction of landing it after. Six months of delay converts a tool into a change-management project."
    },
    {
      "name": "Data Call Runner, a digital employee for proposal information gathering",
      "our_build": "Digital employee, plus workflow automation",
      "what_it_does": "Different in kind from the engine above, this one orchestrates people rather than documents. On RFP release it derives the information requests from the compliance matrix, works out who across the seven subsidiaries and 46 locations (C04, C05) owns each answer, sends the request, chases the non-responders on the proposal manager's schedule, normalises what comes back into the proposal format, and reports completeness against the deadline the Bid and Proposal team is holding (C12). It reduces the capture manager's data-call participation (C11) from chasing to reviewing exceptions.",
      "rice": {
        "reach": "30 pursuits per quarter (same stated assumption as above), but each one touches many more people, contributors across 46 locations (C04).",
        "impact": "2, massive where it works. It removes the coordination load rather than the typing load, which is the larger of the two.",
        "confidence": "50 percent. Heavily discounted. The evidence is one clause in one posting (C11), we have no visibility into how data calls run today, and the build needs their directory, their identity system and behaviour change across seven subsidiaries. Change management across 1,300 people is the risk, not the model.",
        "effort": "10 person-weeks",
        "score": "30 x 2 x 0.50 / 10 = 3.0"
      },
      "cost_of_delay": "Low. Nothing about this gets harder by waiting a quarter, and it gets easier once the evidence corpus exists, because the runner has somewhere to put what it collects. This is a Next-lane item by sequence, not by merit."
    },
    {
      "name": "LLM Disclosure and Incident Register for GSA vehicles",
      "our_build": "Workflow automation, and mostly not AI at all",
      "what_it_does": "A register of every LLM and LLM-backed service used in the performance of work under their GSA vehicles (C06 confirms OASIS+ and STARS III), who operates it, which contract or task order it touches, and what changed when. Plus a 72-hour incident path with the contracting officer notification pre-drafted and the clock started automatically (C47). It is deterministic, a form, a database and a workflow, and it would be dishonest to dress it as an AI build. Its honesty is the product. They already run an AI tool in the business (C08), so they are already in scope for the disclosure the rule proposes (C46) the day it lands.",
      "rice": {
        "reach": "Contract actions under two GSA government-wide vehicles (C06), modelled at 25 per quarter, plus every internal AI tool already in use starting with GovEagle (C08).",
        "impact": "1, high but defensive. It protects against a future obligation and moves no revenue.",
        "confidence": "45 percent. Discounted hard and correctly. C46 and C47 are PROPOSED, not in force, and C45 is trade-press reporting on a Federal Register posting. Building a product on a rule that has not landed is speculation, and the honest version says so.",
        "effort": "3 person-weeks",
        "score": "25 x 1 x 0.45 / 3 = 3.75"
      },
      "cost_of_delay": "The only genuinely clock-driven item on the list, and the clock is conditional. If the rule lands as proposed, the disclosure window is 120 days from the trigger (C46) and incident notification is 72 hours (C47), two different obligations on two different clocks. A company that already has the register on the day the rule lands has a non-event. A company that does not has a 120-day scramble across seven subsidiaries. Cheap enough that it should ride along with whatever else gets built rather than compete with it."
    },
    {
      "name": "Bid/No-Bid Capacity Check",
      "our_build": "Workflow automation over their pipeline and staffing systems, with retrieval",
      "what_it_does": "Joins the pursuit record GovEagle already holds (C10) to the actual staffing state, about 150 open requisitions (C16) including 22 carrying 2025-series numbers (C15), and surfaces at the gate review whether the labour to deliver this pursuit exists, is already committed elsewhere, or would have to be hired. It turns the coordination C13 requires between operations, contracts, pricing and program staff into a standing readout instead of a meeting.",
      "rice": {
        "reach": "Gate reviews only, a small number of high-value events. Modelled at 12 per quarter.",
        "impact": "2, massive per event. A wrong bid/no-bid is the most expensive routine decision in this business.",
        "confidence": "35 percent. The lowest here and it deserves to be. C13 is a coordination requirement in a job posting, not evidence that coordination is failing. It needs write access to staffing, pricing and contracts systems we have never seen, and data readiness is unknown. This is also the candidate GeoNorth (C05) is best placed to build, because it lives inside their own systems.",
        "effort": "12 person-weeks",
        "score": "12 x 2 x 0.35 / 12 = 0.70"
      },
      "cost_of_delay": "None identified. No cited fact puts a clock on it."
    },
    {
      "name": "Shareholder Preference Talent Matcher",
      "our_build": "RAG plus workflow automation over their ATS and shareholder records",
      "what_it_does": "Matches the preference-eligible pool, shareholders, shareholder descendants and shareholder spouses (C18), drawn from more than 300 shareholders (C02), against open requisitions (C16) including the long-listed ones (C15), and flags eligible candidates to recruiters before a role goes to open market. Mission-aligned in a way nothing else here is, an ANC exists for its shareholders.",
      "rice": {
        "reach": "About 150 open requisitions (C16), but only the subset where a preference-eligible candidate plausibly exists, which is unknown and probably small given that no Alaska location appeared on the board that day and Alaska work routes through a separate TCC channel (C17). Modelled honestly at 30, not 150.",
        "impact": "1, high on mission, indirect on revenue.",
        "confidence": "30 percent. The lowest confidence in the set. No cited fact says placing shareholders is difficult, and the claims file explicitly forbids the inference that would have made this case, that the board contradicts the preference (C17, and it is in rejected_do_not_use). Building a pitch on a rejected inference is exactly the failure mode the file was written to stop.",
        "effort": "8 person-weeks",
        "score": "30 x 1 x 0.30 / 8 = 1.1"
      },
      "cost_of_delay": "None identified. Note the RICE artefact honestly, scored on raw requisition count this lands near 5.6 and looks like a contender. It is not. Reach measured in headcount rather than in decisions the tool actually changes is how a weak idea gets a strong score."
    }
  ],
  "provisional_pick": {
    "name": "Key Personnel and Past Performance Evidence Engine",
    "why_over_others": "It tops the Ulwick board (15) and the RICE ranking (7.0 against 3.75, 3.0, 1.1 and 0.70), and unlike everything below it, the company has already priced the pain, a $130,000-plus seat (C09) whose named duties include scrubbing resumes to align with solicitation requirements and sitting in any and all data calls (C11). OVER THE OBVIOUS IDEA, a generative proposal or RFP-response writer, which is the first thing these facts suggest and therefore the thing to test hardest. It loses on satisfaction, not importance. GovEagle is already in the capture pipeline (C08, C10) and a standing Bid and Proposal team already owns process, scheduling and compliance (C12), so a writer is a replacement offer to a staffed function, and the TRAX allegation of AI hallucinating in a source selection (C37, C38) is precisely the anxiety a generated technical volume raises in this market. OVER THE DATA CALL RUNNER, which targets the same job and is the better long-term answer. It needs their directory, their identity system and behaviour change across seven subsidiaries and 46 locations (C04, C05) before it delivers anything, and its evidence is a single clause. The engine works on documents they already own and needs nobody's habits to change on day one. Build the corpus first and the runner has somewhere to put what it collects, which makes this a sequence, not a rejection. OVER THE DISCLOSURE REGISTER, which is honest, cheap, and mostly not an AI build, and which protects against obligations that are PROPOSED and not in force (C45, C46, C47). It moves no revenue. It is small enough to ride along rather than compete, and it is the right Next item if the rule advances. OVER THE CAPACITY CHECK, the biggest prize and the worst fit for an outside team. It lives inside staffing, pricing and contracts systems we have never seen (C13), and GeoNorth (C05) is better placed to build it. OVER THE TALENT MATCHER, whose motivating argument is on the rejected list (C17). THE BUILD-VERSUS-BUY ANSWER, said out loud because they will ask it. GeoNorth Information Systems is their own subsidiary at NAICS 518210 (C05) and they have in-house development capability, so they can absolutely build this themselves and they can certainly host and own it. The honest position is that the engine should end up theirs, running on their infrastructure, and what we sell is the scoped method and the speed of getting there, not a dependency. Exclusivity is not on the table and pretending otherwise would insult a company that owns an information-systems subsidiary. THE ONE THING THAT WOULD OVERTURN THIS, and it is one question, not a study. If GovEagle already carries a resume or past-performance module, this pick is wrong and the disclosure register moves to first. Nothing in the verified file answers that, so it gets asked before anything is built."
  },
  "pays_off": true
}
```

---

## FEASIBILITY, PASS TWO (verbatim)

```json
{
  "pass": 2,
  "note": "Pass 1 recommended a Key Personnel and Past Performance Evidence Engine, conditional on an unretired assumption about GovEagle's feature set. The showrunner fetched GovEagle's own pages (C48-C51), the condition fired, and the engineer re-decided. See feasibility_v1_note.md.",
  "verdicts": [
    {
      "candidate": "Key Personnel and Past Performance Evidence Engine",
      "lowest_tier": "retrieval",
      "verdict": "kill",
      "cost_of_error": "A wrong resume or past-performance mapping is a scored weakness caught late by a Color Team review, survivable with a human approving every draft. The cost of error that actually kills this one is OURS. Proposing it now means proposing a duplicate of a tool they already bought, to the VP of Business Development who runs it, and the study never recovers from that.",
      "data_readiness": "Untested and now moot for the past-performance half. GovEagle's drafting layer already pulls from past-performance write-ups (C50). For the resume half we have never seen the corpus, and resumes are personal data with their own permissioning problem.",
      "step_math": "Not reached. The build dies on duplication before reliability matters.",
      "change_or_reason": "PASS-ONE VERDICT DOES NOT SURVIVE. C49 says GovEagle maps task areas to past performance and shows where you are strong and where you have gaps, and matches PWS requirements to your strongest projects. C50 says its AI drafting layer pulls from past proposals, past-performance write-ups and boilerplate. C51 says requirements are extracted, organised by section and mapped to the response outline. That is the past-performance half, shipping and bought. The resume half is UNVERIFIED in both directions, so it can't be sold either. It becomes a QUESTION in the study, not a build."
    },
    {
      "candidate": "Data Call Runner",
      "lowest_tier": "rules",
      "verdict": "downscope",
      "cost_of_error": "A missed answer slips a submission the Bid and Proposal team is holding to a deadline (C12). An auto-sent chase to the wrong person across seven subsidiaries is cheap once and corrosive at volume. Guardrail, the proposal manager approves the recipient list, the system sends on a schedule a human set, and it never writes an answer into a volume. Under the self-performance climate C25 describes, the attestation behind a fact needs a name on it, so a model may normalise a returned answer's FORMAT and may never vouch for its TRUTH.",
      "data_readiness": "THIS GAP IS THE PROJECT and the study must say so. The compliance matrix exists, GovEagle produces it (C48, C51), so an export surface is required and its existence is unverified. The owner map across 1,300 employees, 46 locations and seven subsidiaries (C03, C04, C05) has never been seen, is HR-adjacent, and may not exist as a structured artefact. Building and keeping it fresh is the real work and staleness is the top failure mode. Historical data calls are almost certainly email and spreadsheets, so NO BASELINE EXISTS and the first deliverable is a measurement, not a tool.",
      "step_math": "The digital-employee version chains derive, identify owner, send, chase, normalise, map, report. Four model steps. At 90 percent per step that is about 0.66 end to end, at 95 percent about 0.81, across roughly thirty items per pursuit, which guarantees several silently wrong items every time with nobody assigned to catch them. THE DETERMINISTIC TRACKER HAS ZERO REQUIRED MODEL STEPS, so there is no chain to compound and every step can be tested exhaustively.",
      "change_or_reason": "Downscope survives and tightens. Rename to Data Call Tracker and drop the digital-employee costume, which is agent washing by Gartner's own definition, a scheduler with email templates called an employee. Spine is rules: owner map, due dates, reminders, escalation, and a completeness board read against the compliance matrix. Rules of ML Rule 1 applies cleanly. The ONE node that could later earn a single LLM call is mapping a free-text requirement to an owner when no rule matches, and it must be earned by measuring how often the rules miss."
    },
    {
      "candidate": "LLM Disclosure and Incident Register",
      "lowest_tier": "rules",
      "verdict": "keep",
      "cost_of_error": "A missed disclosure under a rule that has not landed. Asymmetric and cheap to prevent, which is the argument for a form and a table rather than a model. A model has no business near a regulatory attestation, where full transparency is required, a stated wrong-fit condition in Google PAIR.",
      "data_readiness": "The data is a list they can write down in an afternoon, starting with GovEagle (C08). No corpus, no labels, no freshness problem beyond an owner keeping it current.",
      "step_math": "Not applicable. Deterministic throughout, no model in the path.",
      "change_or_reason": "Survives untouched and is the only candidate GovEagle makes MORE relevant, since GovEagle is the first row in the register. ONE CORRECTION TO ITS JUSTIFICATION: the strategist wrote they are already in scope for the proposed disclosure because they run an AI tool. C46 covers LLMs used in the PERFORMANCE of a contract or task order, and capture and bidding are PRE-AWARD, so whether GovEagle use falls inside is UNESTABLISHED. Asserting it leans the same way as every other error this run caught. Strike the assertion, keep the register, present it as cheap insurance on a conditional clock."
    },
    {
      "candidate": "Bid/No-Bid Capacity Check",
      "lowest_tier": "rules",
      "verdict": "kill",
      "cost_of_error": "The most expensive routine decision in this business, and under C37 and C38 a model influencing a source-selection-adjacent judgement is the exact anxiety this market carries.",
      "data_readiness": "Worst on the board. Needs staffing, pricing and contracts systems inside their perimeter that we have never seen.",
      "step_math": "Irrelevant. Dead twice over.",
      "change_or_reason": "Kill survives and gains a second, stronger reason. GovEagle already ships Bid/no-bid analysis, Opportunity fit score, pWin calculator and Early go or no go guidance (C48, C49). The GeoNorth reason stands alongside it (C05)."
    },
    {
      "candidate": "Shareholder Preference Talent Matcher",
      "lowest_tier": "rules",
      "verdict": "kill",
      "cost_of_error": "An error touches a shareholder's employment prospects and the corporation's obligation to its own people, the least forgiving surface this company has.",
      "data_readiness": "Shareholder records and ATS data, both private, both consent-bound, neither seen.",
      "step_math": "Not reached.",
      "change_or_reason": "Untouched by the fetch and still dead for the original and better reason. Its motivating argument is on the rejected list (C17). A pitch built on a rejected inference is the precise failure the claims file exists to stop."
    }
  ],
  "recommended_pick": {
    "name": "Data Call Tracker, a deterministic completeness board for proposal data calls, preceded by a free GovEagle coverage map",
    "why_it_survives": "IT IS SMALL AND I AM SAYING SO. A thin true build beats a rich invented one, and after the fetch this is what is honestly left. It survives the GovEagle test because data calls appear on NO GovEagle page fetched, the only lane on the whole map where that is true, while the Evidence Engine, the capacity check and bid/no-bid all collided with C48 to C51 head on. It survives cost of error because it tracks status and never authors a fact. It survives the compounding math trivially, the shipped version has no model in the path. IT DOES NOT SURVIVE THE GEONORTH QUESTION AS AN EXCLUSIVE BUILD, and pretending otherwise to a company that owns a NAICS 518210 subsidiary (C05) would insult them. GeoNorth can build this, should host it, and should own it. What we sell is the specification, the owner-map extraction, the acceptance bar, and landing it in weeks alongside the Dahlgren hire (C09) before that seat invents a personal manual method any tool then has to displace. If they hand the spec to GeoNorth and build it themselves, the study did its job and we say so in writing. PHASE ZERO IS NOT A BUILD AND IS FREE: the coverage map handed over at no charge, the two questions only their GovEagle rep can answer, and one real data call measured end to end. If that measurement says the process is fine, the honest recommendation is that they buy nothing from us this quarter."
  },
  "where_not_to_use_ai": "Start with the part worth more than anything we could sell. DO NOT BUILD, AND DO NOT LET ANYONE SELL YOU, a second copy of what GovEagle already ships. Its own pages name RFP shredding, the compliance matrix, outline generation, Color Team reviews, the capability matrix, pWin, bid/no-bid analysis, opportunity fit score, task area matching and pipeline analytics (C48, C49), and its drafting layer already pulls from past proposals, past-performance write-ups and boilerplate (C50). Past-performance and task-area matching is a solved line item on an invoice you are already paying. Beyond that, the data-call spine is rules and not a model, owner routing where a rule matches, due dates, reminders, escalation and counting what is outstanding, all testable exhaustively and none of it degrading silently. The price-to-win number stays human (C14), the cost of error there is an award decision. The LLM disclosure register is a form, a table and a workflow, because a regulatory attestation needs full transparency and that is a stated wrong-fit condition for AI. Deciding whether a returned data-call answer is TRUE stays with the person who owns it, a model may normalise its format and may never vouch for the fact. Nothing we build generates prose into a submitted technical volume, which is where the TRAX allegation lives (C37, C38). And the front desk, the phones and any voice agent, which a 1,300-person federal services contractor across 46 locations does not win or lose on.",
  "honest_flags": [
    "MY PASS-ONE PICK IS DEAD AND THE FETCH KILLED IT. The Evidence Engine's past-performance half is a duplicate of a tool they already own, by the vendor's own words (C49, C50). That is the conscience cutting both ways, and the study should carry it as the finding it is rather than bury it.",
    "GovEagle's handling of key-personnel RESUMES is UNVERIFIED in both directions and must stay that way in the study. Say what we looked at and what we did not find, and put the question to them.",
    "The whole pick rests on data calls not appearing on FOUR fetched GovEagle pages. That is a bounded fetch and not proof of absence, the third time this run that absence of evidence has been tempting to read as evidence of absence. Write it as what we searched and did not find, never as a finding.",
    "C48's Team assignments and C51's requirement-to-outline mapping are the nearest adjacency to the tracker. The reading that those sit inside the pursuit rather than reaching contributors across 46 locations is the ENGINEER'S INFERENCE, not a fetched fact, and it is the single thing most likely to make this pick wrong too.",
    "NOTHING FETCHED SAYS THEIR DATA CALLS ARE SLOW. The evidence is one clause in one posting (C11). No baseline exists, so the first deliverable is a measurement and the build is conditional on it. If the measurement says the process holds, the right answer is that they need nothing from us.",
    "The strategist's claim that they are already in scope for the proposed GSA disclosure rule is UNESTABLISHED. C46 covers LLMs used in the PERFORMANCE of a contract, and capture is pre-award. Strike it from the study.",
    "The 30-pursuits-per-quarter reach figure is invented. No ROI may rest on it until they supply their real number.",
    "We are recommending something their own subsidiary could build, and the study says so unprompted. If both open questions come back covered by GovEagle, what honestly remains is the coverage map and a deterministic register, and the study should be willing to print that."
  ]
}
```

---

## THE ENGINEERING ROOM (verbatim, as the four agents returned it)

```json
{
  "prd": {
    "problem": "Requisition 2026-2731 asks one person at Dahlgren, posted at $130,000.00+ DOE, to handle \"participation in any and all data call activities as needed\" and to \"Support the development and scrubbing of key personnel resumes, so they align with solicitation requirements\" (C09, C11). That seat sits beside a standing Bid and Proposal team that already owns proposal process, scheduling and compliance (C12), and the answers a data call collects have to come back from people spread across 1,300 employees, 46 locations worldwide and seven subsidiaries (C03, C04, C05). The pipeline itself is already held in GovEagle, named in Tatitlek's own posting as its Artificial Intelligence tool (C08, C10). So the question is not whether Tatitlek has tooling here. It is narrower and more awkward than that. Nobody has measured what one data call actually takes to run end to end, so nobody can say whether it needs anything at all. We could not find it measured, and we can't measure it from outside. The Dahlgren seat will answer that question by inventing a personal method, one pursuit at a time, and that method becomes the thing any future tool has to displace.",
    "after_state": "A proposal manager opens one board the morning after a data call goes out, sees every requirement with a named owner, a due date and a status, and knows in under a minute what is still outstanding and who is holding it, without a single message asking who owns what.",
    "goals": [
      "Hand over, free and before any engagement, a written map of which parts of the capture and proposal job GovEagle's own pages already say it covers, so nobody sells Tatitlek a second copy of a tool it is already paying for (C48, C49, C50, C51).",
      "Establish a real measured baseline for one live data call, end to end, because no baseline exists today and every number after this one depends on it.",
      "Produce the owner-map extraction method and a specification for a deterministic Data Call Tracker, with its acceptance bar written down before anyone builds anything.",
      "Leave Tatitlek holding an artefact they can hand straight to GeoNorth, their own NAICS 518210 subsidiary (C05), and build themselves without us.",
      "Land the method alongside the Dahlgren hire rather than after it, so the new seat starts on a shared method instead of a private one (C09).",
      "Leave them able to say no. If the measurement shows the process holds, the recommendation we write is that they build nothing this quarter, and we would rather write that than sell past it."
    ],
    "non_goals": [
      {
        "item": "Building, or letting anyone sell them, anything GovEagle's own pages already name. That covers RFP shredding, the compliance matrix, outline generation, Color Team reviews, the capability matrix, pWin, bid/no-bid analysis, opportunity fit score, task area matching, pipeline analytics, and the drafting layer that pulls from past proposals and past-performance write-ups.",
        "reason": "It is on an invoice Tatitlek already pays (C48, C49, C50, C51). This restraint is the most valuable thing in the engagement and it is the part we charge nothing for. Our own first candidate build, a past-performance evidence engine, died on exactly this test once we read GovEagle's pages, and we would rather report that than ship it."
      },
      {
        "item": "No model writes, judges or vouches for any answer. Nothing we specify generates prose into a submitted volume, and nothing decides whether a returned answer is true.",
        "reason": "A contractor has alleged in the Court of Federal Claims that the Army used AI that hallucinated during a source selection, and the Army conceded one identified weakness was not supported by the record (C37, C38). Under the self-performance climate the Pentagon described in January, the attestation behind a fact needs a person's name on it (C25). A tracker tracks status. A human owns the fact."
      },
      {
        "item": "We do not ask for an exclusive build, and we do not want to host this.",
        "reason": "GeoNorth Information Systems is Tatitlek's own information systems subsidiary (C05) and can build and host this. A company that owns one would be right to be insulted by any other position. We sell the specification, the extraction method, the acceptance bar and the speed."
      },
      {
        "item": "Nothing resume-related in Phase 1, despite resume scrubbing sitting in the same requisition clause (C11).",
        "reason": "Whether GovEagle handles key-personnel resumes is unverified in both directions. It is named on no GovEagle page we fetched, and the search summaries that claim it are not evidence. Specifying a build against an unanswered question is how a prospect ends up buying a duplicate. It is open question 1 and it stays one."
      },
      {
        "item": "No touching price to win, bid/no-bid, or any gate decision.",
        "reason": "The posting keeps price to win analysis with the human presenting to the Director and senior leadership (C14), the cost of an error there is an award, and GovEagle already ships bid/no-bid analysis, an opportunity fit score and early go or no go guidance (C48, C49)."
      },
      {
        "item": "No shareholder records, no applicant tracking data, no HR systems.",
        "reason": "The hiring preference for shareholders, shareholder descendants and shareholder spouses (C18) touches the corporation's obligation to its own people. Those records are private and consent-bound, we have never seen them, and it is the least forgiving surface this company has."
      },
      {
        "item": "No voice agent, no front desk automation, no chat layer.",
        "reason": "A 1,300-person federal services contractor across 46 locations does not win or lose on any of it (C03, C04). We mention it only because it is what most shops would have proposed."
      },
      {
        "item": "No integration work in Phase 1, including any GovEagle API build.",
        "reason": "Whether the compliance matrix can be exported in a machine-readable form is unverified, and the tracker reads against it. Phase 1 answers that question rather than assuming an answer and blowing the estimate on it."
      }
    ],
    "metrics": [
      {
        "metric": "Cycle time for one complete data call, from issue to the last answer in hand, plus the spread across individual requirements.",
        "baseline": "NONE EXISTS, and we will not invent one. Nothing we fetched says how long a Tatitlek data call takes. The entire evidence base is one clause in requisition 2026-2731 (C11). Measurement method: a timestamped log kept alongside one real, live data call, recording issue time, every requirement, its named owner, every chase and every answer returned, with the proposal manager confirming the log is complete before we close it.",
        "target": "A defensible number with the per-requirement spread beside it, every requirement in the log accounted for with none dropped, signed off by the Bid and Proposal team as the baseline of record (C12). The target here is that the number exists and is trusted, not that it lands anywhere in particular, because setting a target before the baseline exists would be inventing the baseline.",
        "timeframe": "Within one pursuit cycle of Phase 1 starting, and in their hands within five working days of that data call closing."
      },
      {
        "metric": "Share of that data call's requirements whose owner is resolved by rule alone, with no human lookup.",
        "baseline": "UNKNOWN and assumed absent. No owner map across the seven subsidiaries and 46 locations has ever been seen and it may not exist as a structured artefact at all (C04, C05). Measurement method: run the owner-map extraction on the same measured data call and count resolved against total, writing down every miss verbatim.",
        "target": "At least 80 percent resolved by rule, every miss listed. That 80 is a bar we set, not a figure about their business. Below it, the honest report is that rules alone are the wrong spine, we say so at the gate, and the miss list becomes the evidence for whether one narrow model call is ever earned later.",
        "timeframe": "Same measurement window, reported in the same document as the baseline."
      },
      {
        "metric": "Count of items in the Phase 1 specification that duplicate a capability GovEagle already provides.",
        "baseline": "Our starting list is the coverage map itself, checked against GovEagle's platform, solutioning, proposals and automation pages (C48, C49, C50, C51). That is a bounded fetch and not proof of absence, so their GovEagle administrator marks each line confirmed, corrected or unknown.",
        "target": "Zero. Checked line by line at the funding gate, with their administrator's markup on the record. Any line that comes back corrected is struck from the specification before a build is quoted, not after.",
        "timeframe": "Before any build money is committed, which is the end of Phase 1."
      },
      {
        "metric": "Requirements still outstanding 48 hours before the internal submission cutoff, on the first two data calls run against the built tracker. This one is conditional and only exists if Phase 1 clears its gate.",
        "baseline": "Set by metric 1, not by us. It does not exist yet and no number belongs here until that measurement lands.",
        "target": "At or below half the measured baseline count, with every remaining item showing a named owner and a last-chased timestamp. Falsified if either of the two calls misses it, and a miss means the recommendation is to stop rather than to extend.",
        "timeframe": "Within two pursuit cycles after the tracker goes live."
      }
    ],
    "phase1_must": [
      "The GovEagle coverage map, free and first. Line by line against the capabilities GovEagle's own pages name, plus a plain statement of which pages we read and what we looked for and did not find on them.",
      "The two questions only their GovEagle account rep can answer, written so they can be forwarded to the rep as they stand.",
      "One real live data call instrumented end to end, with the timestamped log, the completed baseline number and the per-requirement spread.",
      "The owner-map extraction method, run on that same data call, producing the requirement-to-owner rules and a verbatim list of every requirement the rules missed.",
      "The Data Call Tracker specification: the data model, the rules spine of owner routing, due dates, reminders and escalation, the completeness board read against the compliance matrix GovEagle already produces (C48, C51), the human approval points, and the acceptance bar written before anyone builds.",
      "A written answer on whether the compliance matrix can be exported machine-readably, with a manual paste-in fallback specified so the tracker never depends on an integration nobody has confirmed exists.",
      "A written gate recommendation with a real no-build option, including the sentence that if the measurement says the process holds, they should buy nothing further from us."
    ],
    "phase1_later": [
      "The tracker itself, built and hosted against the specification, ideally by GeoNorth (C05).",
      "A second and third measured data call, the cheapest way to narrow a sample of one.",
      "An LLM disclosure and incident register, which is a form, a table and an owner, with GovEagle as row one (C08). Worth noting that GSA posted an AI-specific acquisition rule to the Federal Register on June 17th, 2026 (C45), and that its 120 day disclosure and 72 hour incident clauses are PROPOSED and not in force (C46, C47). Whether Tatitlek falls in scope is unestablished, since those clauses address models used in the performance of a contract and capture is pre-award. This is cheap insurance on a conditional clock, nothing more.",
      "One narrow model call at the single node that could earn it, mapping a free-text requirement to an owner when no rule matches, earned only if metric 2's miss list shows the rules need it.",
      "Rolling the tracker past the first pursuit to the other subsidiaries and locations.",
      "Anything resume-related, and only after open question 1 comes back from their GovEagle rep."
    ],
    "need_from_you": [
      "One live data call we can instrument, in flight, with the proposal manager's agreement. Without a live one there is no baseline and Phase 1 has nothing to measure. This is the single dependency that can move the whole timeline.",
      "Thirty to forty five minutes with whoever administers GovEagle at Tatitlek, to mark our coverage map confirmed, corrected or unknown line by line.",
      "An answer from your GovEagle account rep on the two open questions below. We can't get it, only the account holder can.",
      "A named proposal manager as decision owner. The tracker never picks who gets chased, a human approves the recipient list, and the system only sends on a schedule that human set.",
      "One real compliance matrix export, or a screenshot of what it looks like today, so the specification is written against your actual artefact rather than our guess at it.",
      "A named contact at GeoNorth if GeoNorth is to build it, so the specification is written to their stack and not to ours.",
      "Written sign-off from the Bid and Proposal team that the measured number is the baseline of record (C12). A baseline nobody signs is a number nobody defends at the next gate.",
      "A decision on what the log may record. Our default is requirement, owner, timestamps and status, and never the content of an answer, because data call answers can be business-sensitive. Say the word and we narrow it further."
    ],
    "risks": [
      {
        "risk": "GovEagle may already cover data calls. Team assignments is named on its platform page (C48) and requirement-to-outline mapping on its proposals page (C51). Our reading that those sit inside a pursuit rather than reaching contributors across seven subsidiaries and 46 locations is our inference, not a fetched fact, and it is the single thing most likely to make this whole recommendation wrong.",
        "mitigation": "The coverage map is the first deliverable and it costs nothing. If their administrator or rep says Team assignments already does this, we stop, write that down, and Tatitlek has spent zero dollars finding out. We would rather be wrong for free than right for a fee."
      },
      {
        "risk": "The measurement may show the process is fine. Nothing we fetched says their data calls are slow, and we are not going to pretend otherwise. One clause in one posting is the entire evidence base (C11).",
        "mitigation": "That outcome is a deliverable, not a failure. Phase 1 buys the right to stop, which is worth the price of not building the wrong thing. The gate is written with a real no-build branch and we are saying so before they pay, not after."
      },
      {
        "risk": "The owner map may not exist as a structured artefact, and staleness is the top failure mode of any version that does. People move across 46 locations and seven subsidiaries (C04, C05).",
        "mitigation": "The extraction method is Phase 1 work, not an assumption. The specification carries a named freshness owner and a re-verification cadence as an acceptance criterion, so a stale map fails the bar rather than quietly producing wrong chases. If the rules resolve under 80 percent, we report that rules are the wrong spine instead of papering over the gap with a model."
      },
      {
        "risk": "GeoNorth can build this, so we are recommending something a subsidiary could do in-house.",
        "mitigation": "Said here first, unprompted. We do not ask for an exclusive build and we do not want to host it. If Tatitlek takes the specification, the extraction method and the acceptance bar and hands the lot to GeoNorth, the engagement did its job and we will say so in writing."
      },
      {
        "risk": "One measured data call is a sample of one, and a single pursuit can be unrepresentative.",
        "mitigation": "We report it as a sample of one, with the per-requirement spread beside the headline figure, and the acceptance bar is set against the range rather than the single number. A second measured call sits in the Next lane as the cheapest way to narrow it."
      },
      {
        "risk": "The Dahlgren seat may be filled and running a private method before any of this lands (C09).",
        "mitigation": "Timing is the reason Phase 1 is weeks and not months. If the seat is already filled and a method is in place, the measurement still stands and the specification bends to their method rather than the other way round. Displacing a working habit is not something we would ask them to do."
      },
      {
        "risk": "If the tracker gets built and underperforms, Tatitlek has paid for a board nobody opens.",
        "mitigation": "Funding is staged. The build is Phase 2 and is released only if Phase 1's numbers clear the gate. If the built tracker misses the outstanding-count target across two pursuits, our written recommendation is to stop, and we will write what we got wrong. The measured baseline and the specification stay theirs either way, which is the part that holds value even in the bad case."
      },
      {
        "risk": "Deltek's 2026 study reports 45 percent of contractors unclear on the return on AI investment, with only 5 percent fully developed in AI maturity (C31), in a field where 90 percent report using AI in some capacity (C28). The base rate for proving payback here is poor.",
        "mitigation": "We are not asking them to beat that base rate on faith. Phase 1 produces a measurement rather than a tool, which is the one thing that turns an unclear return into a checkable one. It is also why the shipped tracker has no model in its path at all."
      }
    ],
    "open_questions": [
      {
        "q": "Does GovEagle handle key-personnel resumes? Resume scrubbing sits in the same requisition clause as data call participation (C11), so it matters. We read GovEagle's platform, solutioning, proposals and automation pages and found resumes named on none of them (C48, C49, C50, C51). Search-engine summaries assert that it does, which is not evidence we will stand behind. It is unverified in both directions and we are not going to resolve it for you in either.",
        "owner": "Tatitlek's GovEagle account rep, asked by Mark Wamsher. We can't settle it from outside and will not guess."
      },
      {
        "q": "Does GovEagle's Team assignments (C48) reach contributors outside the proposal team, across the seven subsidiaries and 46 locations (C04, C05)? Our reading that it sits inside a pursuit is an inference, not a fetched fact.",
        "owner": "Tatitlek's GovEagle account rep plus whoever administers the tool internally. If the answer is yes, this build should not happen and we will say so."
      },
      {
        "q": "Can the compliance matrix be exported from GovEagle in a machine-readable form? The completeness board reads against it (C48, C51), so the answer changes the specification.",
        "owner": "Tatitlek's GovEagle administrator, answered inside Phase 1."
      },
      {
        "q": "How many pursuits actually run a data call in a quarter? We have no figure, we will not invent one, and any return estimate stays a range with visible assumptions until Tatitlek supplies the real number.",
        "owner": "Mark Wamsher and the BD Director."
      },
      {
        "q": "Who owns the owner map once it exists, and who is accountable for keeping it current? A map with no owner goes stale, and a stale map chases the wrong people.",
        "owner": "Tatitlek BD leadership, with GeoNorth if GeoNorth hosts it."
      },
      {
        "q": "Does the Dahlgren seat run data calls, or does the Bid and Proposal team? The posting has the seat participating while the Bid and Proposal team owns process, scheduling and compliance (C11, C12), which reads as shared rather than assigned.",
        "owner": "Mark Wamsher."
      }
    ]
  },
  "design": {
    "one_liner": "Build Tatitlek a deterministic Data Call Tracker that takes the compliance matrix GovEagle already produces (C48, C51), routes each required answer to a named owner across the seven subsidiaries and 46 locations (C04, C05), chases on a schedule a human set, and shows the Bid and Proposal team (C12) one honest completeness readout, so the outcome moved is the hours a proposal manager spends finding out what is still outstanding, measured against a baseline we take first.",
    "architecture": {
      "nodes": [
        {
          "id": "pm",
          "label": "Proposal manager and capture lead, Bid and Proposal team (C12)",
          "kind": "user"
        },
        {
          "id": "goveagle",
          "label": "GovEagle, compliance matrix export (C08, C48, C51)",
          "kind": "external"
        },
        {
          "id": "intake",
          "label": "Requirement intake and rules-based owner routing",
          "kind": "build"
        },
        {
          "id": "ownermap",
          "label": "Owner map, seven subsidiaries and 46 locations (C04, C05)",
          "kind": "data"
        },
        {
          "id": "scheduler",
          "label": "Due dates, reminders and escalation ladder",
          "kind": "build"
        },
        {
          "id": "mail",
          "label": "Tatitlek corporate mail tenant and SSO",
          "kind": "external"
        },
        {
          "id": "contributors",
          "label": "Subsidiary contributors who own an answer",
          "kind": "user"
        },
        {
          "id": "board",
          "label": "Completeness board and append-only audit log",
          "kind": "build"
        }
      ],
      "edges": [
        {
          "from": "goveagle",
          "to": "intake",
          "label": ""
        },
        {
          "from": "pm",
          "to": "intake",
          "label": ""
        },
        {
          "from": "pm",
          "to": "ownermap",
          "label": ""
        },
        {
          "from": "ownermap",
          "to": "intake",
          "label": ""
        },
        {
          "from": "intake",
          "to": "scheduler",
          "label": ""
        },
        {
          "from": "scheduler",
          "to": "mail",
          "label": ""
        },
        {
          "from": "mail",
          "to": "contributors",
          "label": ""
        },
        {
          "from": "contributors",
          "to": "board",
          "label": ""
        },
        {
          "from": "scheduler",
          "to": "board",
          "label": ""
        },
        {
          "from": "board",
          "to": "pm",
          "label": ""
        }
      ],
      "caption": "Three build nodes, one data store, no model anywhere in the shipped path, and that is the honest answer rather than a gap. GovEagle stays the source of the requirement set, the tracker only tracks status against it. Requirements arrive as an export or a pasted CSV, rules match each one to a named owner from the owner map, the proposal manager approves the recipient list before anything sends, the scheduler chases on a cadence a human set through Tatitlek's own mail tenant so a request arrives from a tatitlek.com address, contributors mark status and attach a pointer to their own file, and the board counts what is outstanding. Every build node ships as one deployable that GeoNorth Information Systems, their own NAICS 518210 subsidiary (C05), hosts and owns."
    },
    "build_vs_buy": [
      {
        "component": "Identity and single sign-on",
        "decision": "buy",
        "why": "Their corporate tenant already authenticates 1,300 employees (C03). The tracker speaks OIDC to whatever identity provider GeoNorth names and keeps no password store and no second user directory, because a tracker that invents its own logins across 46 locations (C04) will be abandoned by month two."
      },
      {
        "component": "Notification transport",
        "decision": "buy",
        "why": "Chases go through Tatitlek's own mail tenant, not through a sending domain we stand up. A data call request from an unfamiliar domain lands in quarantine, and deliverability is a solved commodity that nobody should pay us to reinvent."
      },
      {
        "component": "Datastore, scheduler and queue",
        "decision": "buy",
        "why": "Managed Postgres plus a job table and a managed cron in whichever cloud GeoNorth already operates. There is nothing differentiated about storing thirty rows per pursuit and waking up daily."
      },
      {
        "component": "A generic work tracker, Smartsheet or SharePoint list or Jira, instead of software",
        "decision": "buy",
        "why": "This row is deliberately here and it is the cheapest honest outcome. If the measured data call shows a low item count and few chases, the right answer is a bought list plus the owner map plus a written cadence, and we say so rather than build. The specification is worth more than the code, and the code should only exist if the measurement earns it."
      },
      {
        "component": "GovEagle compliance matrix ingest adapter",
        "decision": "build",
        "why": "Nobody sells a bridge from GovEagle's compliance matrix (C48, C51) into a tracker, and whether an export or API surface exists at all is unverified, so the adapter is built with a manual CSV upload path as the first-class fallback rather than as a degraded mode. Thin, deterministic, and testable against a real past matrix file."
      },
      {
        "component": "Owner map across seven subsidiaries and 46 locations",
        "decision": "build",
        "why": "This is the differentiator and the only part of the design that could not be bought. No product knows that a given contract-data question belongs to a named person at a named subsidiary (C05) at a named location (C04). The extraction method, the review cadence and the staleness report are the actual intellectual property in this engagement, and they outlive any tool it is loaded into."
      },
      {
        "component": "Rules-based routing, escalation ladder and completeness board",
        "decision": "build",
        "why": "Small enough that buying it means buying a large product to use one screen, and the logic is Tatitlek-shaped, one pursuit, one compliance matrix, one due date per item, one escalation path into the Bid and Proposal team that owns scheduling and compliance (C12). Rules across the whole spine means zero required model steps, no compounding error chain, and exhaustive tests."
      },
      {
        "component": "Hosting, operation and long-term ownership",
        "decision": "build",
        "why": "Built and run by GeoNorth, not by us, and we are writing that down unprompted. GeoNorth Information Systems is their own NAICS 518210 subsidiary (C05), it can build this, and a company that owns an information-systems house would be right to be insulted by a dependency pitch. We sell the specification, the owner-map extraction, the acceptance bar and the speed of getting there alongside the Dahlgren capture seat (C09). Repo, runbook, tests and data model transfer at the end of the MVP phase, and there is no licence and no hosting invoice from us."
      }
    ],
    "cross_cutting": {
      "auth": "OIDC against Tatitlek's existing identity provider through GeoNorth, with three roles. Proposal manager is the only role that can create a pursuit, approve the recipient list and edit the owner map. Contributor sees only the items assigned to them on one pursuit. Leadership gets read-only counts with no requirement text. Contributors who have no seat in the tenant, which is likely somewhere across 46 locations (C04), get a single-purpose expiring link scoped to their own items on one pursuit, never a standing account. No account is ever created by the system, because the identity provider is the system of record for who works here and the tracker isn't.",
      "data_security": "The tracker holds status, not substance. An item stores a requirement identifier, a section reference, a short title, an owner, a due date and a state. Full requirement text stays in GovEagle and answer files stay in whatever system the contributor already uses, with the tracker holding only a pointer, which is what keeps controlled and export-restricted material out of it by construction rather than by policy. BD-releasable material only, nothing pulled from a DoD site, and no personal data. The owner map stores a work email, a role, a subsidiary and a location, never an employee record, never a resume, never anything shareholder related (C18). Retention is item-level rows purged a set number of days after award decision, with only de-identified cycle-time aggregates kept, so the historical value survives and the exposure does not. Hosted in GeoNorth's environment under their existing controls, which is also why the security review is theirs to run and not ours to assert.",
      "observability": "Every state change appends to an immutable audit log with who, what, when and by which route, because the question a proposal manager actually asks under deadline is when this was last chased and by whom. Beyond that, four instruments. Per-item cycle time from first request to accepted, compared against the baseline taken in the spike. Reminder delivery receipts, so a silent chase is visible as a failure rather than as a non-response. A weekly owner-map staleness report listing every entry past its review date, since staleness is the top failure mode of the whole design. A rules-miss counter recording every item no rule could route, which is the only measurement that could ever earn a single model call later, and it has to be earned rather than assumed.",
      "failure_modes": "Six, mapped onto the nodes. Owner map goes stale after a reorganisation or a departure, so entries carry review dates, the staleness report is weekly, and a bounced or out-of-office reply flags the entry rather than silently retrying. No GovEagle export surface exists, so CSV upload is a first-class path and the walking skeleton runs on it. Chases go to the wrong person, so the proposal manager approves the recipient list before the first send, re-routing is one click, and every re-route increments a counter that tells us the rules are wrong. Notification fatigue, so the cadence and the escalation ladder are set by a human per pursuit and capped, never tuned by the system. A contributor never logs in, so status can also be captured from a structured email reply and, failing that, entered by the proposal manager on their behalf with the audit log recording that it was entered on behalf. The worst one is social rather than technical, somebody reading a green board as proof an answer is correct, so the board states submitted by a named person at a time and never states correct, and nothing in the product vouches for the truth of a fact."
    },
    "goals": [
      "Give the Bid and Proposal team (C12) one readout of what is outstanding on a live data call, read against the compliance matrix GovEagle already produces (C48, C51), so nobody assembles that answer by hand from an inbox.",
      "Route each required answer to a named owner at a named subsidiary and location (C04, C05) by deterministic rule, with the proposal manager approving the recipient list before anything sends.",
      "Chase and escalate on a cadence a human set, from Tatitlek's own mail domain, with delivery receipts so silence is distinguishable from failure.",
      "Produce a measured baseline for one real data call first, so any further spend is gated on their own numbers rather than on an industry survey figure (C29 is a self-report about other firms and says nothing about Tatitlek).",
      "Keep zero required model steps in the shipped path, so every rule can be tested exhaustively and nothing degrades silently.",
      "Build the owner map as a durable asset with review dates and a staleness report, because the map is worth more than the software around it.",
      "Hand the whole thing to GeoNorth (C05) as a repo, a runbook, a test suite and a data model, with no licence and no hosting dependency on us."
    ],
    "non_goals": [
      {
        "item": "RFP shredding, compliance matrix generation, outline generation, Color Team reviews, capability matrix, pWin, bid and no-bid analysis, opportunity fit score, task area matching, pipeline analytics, and drafting from past-performance write-ups",
        "reason": "GovEagle's own pages name every one of these (C48, C49, C50, C51) and Tatitlek already runs GovEagle in capture (C08, C10). Building a second copy of a tool that is already on an invoice they pay is waste, and proposing it to the Vice President of Business Development whose own requisition names that tool would be worse than waste."
      },
      {
        "item": "Generating any prose that lands in a submitted technical volume",
        "reason": "That is exactly the surface the TRAX allegation concerns, an allegation in live litigation about the government's own use of AI in source selection (C37, C38). The tracker tracks status and never authors a fact."
      },
      {
        "item": "Judging whether a returned answer is true, complete or compliant",
        "reason": "Under the self-performance climate the Pentagon described (C25), the attestation behind a fact needs a person's name on it. A model may normalise a returned answer's format and may never vouch for its truth, and the board shows who submitted what and when, never that it is correct."
      },
      {
        "item": "Anything touching key-personnel resumes",
        "reason": "Two independent reasons. Resumes are personal data and personal data stays out of this system entirely. Separately, whether GovEagle already handles key-personnel resumes is unverified in both directions, named on no page we fetched and asserted only by search summaries, so it stays a question for their GovEagle rep rather than a build."
      },
      {
        "item": "Any price-to-win number or bid recommendation",
        "reason": "Price to win is a named responsibility of the capture role and goes to the Director and senior leadership (C14). The cost of error is an award decision, so it stays human."
      },
      {
        "item": "An LLM anywhere in the shipped path",
        "reason": "It has not been earned. The one node that could ever justify a single call is mapping a free-text requirement to an owner when no rule matches, and the rules-miss counter has to show a real miss rate first. Adding a model before that is the agent-washing this design exists to avoid."
      },
      {
        "item": "Becoming a system of record for employees, org structure or HR data",
        "reason": "The identity provider and their HR system already are. The owner map is a routing table of roles and work addresses that points at them, and it holds nothing that would make it an HR record."
      },
      {
        "item": "Any integration with the iCIMS careers board",
        "reason": "That is hiring data about individuals, not proposal data, and pulling it in would import personal data for no benefit to a data call."
      },
      {
        "item": "An exclusive build, a licence, or a hosted service we run for them",
        "reason": "GeoNorth is a NAICS 518210 subsidiary of this same corporation (C05) and can build and host this. Designing for dependency would be designing against their own interests, so the design targets handover from day one."
      },
      {
        "item": "Any claim about the proposed GSA AI acquisition rule applying to this system",
        "reason": "C45, C46 and C47 are proposed and not in force, and C46 covers models used in the performance of a contract while capture and bidding are pre-award. There is no model in this system anyway, so the question doesn't arise here."
      }
    ],
    "riskiest_assumption": "That a Tatitlek data call loses real, measurable time to status chasing that GovEagle is not already handling. Two things have to be true and neither is verified. First, that data calls cost them time at all, where the entire evidence base is one clause in one job posting saying the new hire participates in data call activities (C11). Nothing fetched says their data calls are slow, and we will not say it. Second, that GovEagle's Team assignments (C48) sit inside the pursuit team rather than reaching contributors across seven subsidiaries and 46 locations (C04, C05). That second one is an engineer's inference from a bounded fetch of four GovEagle pages, it is not a fetched fact, and it is the single thing most likely to make this design wrong. If either half fails, the correct outcome is that Tatitlek builds nothing and the free coverage map was the whole deliverable. The technology is not the risk. Rules, a scheduler and a board are the lowest-risk thing on the board, and a well-built solution to a problem that isn't there is still worthless.",
    "spike_to_retire_it": "One measured data call, run before any code is written, in three steps. STEP ONE, three questions in writing to their GovEagle account rep, which cost nothing and which only that rep can answer. Does GovEagle handle key-personnel resumes. Do Team assignments reach contributors outside the proposal team, across subsidiaries and locations. Does the compliance matrix have an export or API surface. A yes to the second question ends the engagement honestly and we will say so in the same email. STEP TWO, agree the go and no-go thresholds BEFORE the measurement starts, with Tatitlek setting the final numbers, so the result can't be argued into a purchase afterwards. Our proposed starting point is build nothing if fewer than a quarter of items need more than one chase, and if the proposal manager's own chase time comes in under four hours for the pursuit. STEP THREE, instrument exactly one live data call and change nothing about how it runs. A shared sheet we supply, one row per required item, capturing first request sent, every chase, answer received, answer accepted, the recipient's subsidiary and location, and any item that had to be re-routed because the first recipient was wrong. The readout is eight numbers. Item count, distinct owners, distinct subsidiaries and locations touched, median and 90th-percentile hours from request to accepted, chases per item, re-route rate, and proposal manager hours spent chasing. A ninth number decides the architecture rather than the go decision, the share of items a simple section-to-function rule would have routed correctly, which is the rules-miss rate the whole deterministic design rests on. Time box, two days to instrument, the length of one real pursuit's data call for the measurement itself, two days to read out. If the numbers clear the thresholds Tatitlek set, the walking skeleton starts. If they don't, we write that down and nobody buys anything.",
    "delivery": {
      "walking_skeleton": "One pursuit, twenty requirement items, one reminder, end to end on crutches, running against a real past compliance matrix rather than synthetic data. Import that matrix as a CSV upload, since the export surface is unverified and the fallback path is the one that must work first. Rules route the twenty items against a hand-seeded owner map of about ten named owners the proposal manager approved. One reminder sends through Tatitlek's mail tenant. One contributor opens a scoped expiring link, marks an item submitted and attaches a pointer to their own file. The board reads one of twenty complete and the audit log carries the row. Stubbed on purpose, no escalation ladder, no digest, no multi-pursuit, no owner-map editor, no API ingest, and it runs on a GeoNorth sandbox from the first day so the handover target is never a later migration. It touches every node in the diagram and it actually runs.",
      "then_mvp": "Flesh out in this order. Full escalation ladder with a per-pursuit cadence a human sets and a cap. Bulk import plus the GovEagle export adapter if the rep confirms a surface exists. Owner-map editor with review dates, the weekly staleness report and bounce flagging. Structured email-reply status capture for contributors who never log in, plus enter-on-behalf with audit. Read-only leadership counts. Per-item cycle-time metrics reported against the spike baseline, which is the only way anyone can tell whether this worked. MVP is one live pursuit run entirely on the tracker by the Bid and Proposal team alongside the Dahlgren capture seat (C09), followed by the handover package to GeoNorth, repo, runbook, test suite, data model, owner-map extraction method and the written acceptance bar.",
      "estimate_range": "Ranges at concept, wide on purpose, each tied to a phase and a confidence. PHASE 0, the GovEagle coverage map and the three questions for their rep, already done and free, zero cost to them, high confidence because it is finished. PHASE 1, the spike, two to four weeks calendar and twenty to forty hours of our time, about 80 percent confidence, the variance being their pursuit cadence rather than our scope. PHASE 2, the walking skeleton, two to four weeks after the spike clears, about 65 percent confidence, assuming a CSV path and a GeoNorth sandbox available in week one. PHASE 3, flesh out to MVP, a further six to twelve weeks, about 50 percent confidence, which is the Cone of Uncertainty being honest at concept stage. The upper end doubles if no export surface exists and the owner map has to be extracted by interview across seven subsidiaries, because that is people-availability work and not engineering work. PHASE 4, handover to GeoNorth, one to two weeks, about 70 percent confidence. These numbers describe effort we can estimate. Nothing here estimates their benefit, because no baseline exists yet and that is what Phase 1 is for.",
      "what_narrows_it": "Six things, in the order they would move the range most. The measured data call itself, which replaces every assumption about item count, owner count and chase volume with their own numbers. A yes or no from their GovEagle rep on whether Team assignments reach contributors outside the proposal team, which is the answer that could end the project rather than narrow it. A yes or no on a compliance matrix export or API, which is worth roughly a fortnight of the Phase 3 band. Seeing one real compliance matrix export file, because the adapter is only as predictable as the format it reads. Their actual pursuit count per quarter, which we do not have and will not guess, since the figure floated earlier in this analysis was invented and is not used in any number here. GeoNorth naming its hosting stack and identity provider, which converts three integration unknowns into configuration."
    }
  },
  "roadmap": {
    "now": [
      {
        "item": "Hand over the GovEagle coverage map, free, before anything is bought. Every duty named in your own requisition 2026-2731 gets marked covered, not covered, or unverified, against a GovEagle page we actually fetched. Bid/no-bid analysis, opportunity fit score, task area matching, capability matrix, RFP shredding, compliance matrix, pWin, outline generation and the drafting layer that already pulls from past proposals and past-performance write-ups all come back covered (C48, C49, C50, C51). Data calls appear on no GovEagle page we fetched, which is what we searched for and did not find, never a finding. Two questions ride along with it and only your GovEagle rep can answer them. Does GovEagle handle key-personnel resumes, which is unverified in both directions and which we refuse to settle for you. Does Team assignments reach contributors outside the proposal team, across the seven subsidiaries (C05) and the 46 locations (C04).",
        "metric": "Count of the duties in requisition 2026-2731 resolved to covered, not covered, or unverified, each carrying the page it came from. Success is that the map takes scope out of our own proposal rather than adding it. Second metric, both rep questions answered in writing within two weeks of you asking them.",
        "why_first": "It costs you nothing and it can end this engagement before a dollar moves. It has already proved itself once. The same fetch killed the build we were going to recommend, a Key Personnel and Past Performance Evidence Engine that topped our own scoring, because GovEagle's own pages say it maps task areas to past performance, matches PWS requirements to your strongest projects, and drafts from past-performance write-ups (C49, C50). We would have sold you a second copy of a tool you already pay for, to the Vice President of Business Development whose own requisition names it."
      },
      {
        "item": "Measure one real data call end to end, on one live pursuit, after September 30th. Request issued through to last answer received. Nothing gets built and nothing gets changed, we instrument what already happens and write the numbers down.",
        "metric": "Six numbers that do not exist anywhere today. Elapsed hours from the request going out to the last answer arriving. Count of distinct people asked across subsidiaries and locations. Count of chase rounds. Count of items where the first person asked was not the person holding the answer. Count of compliance-matrix items still outstanding at your own internal cut-off. Hours the proposal manager spent routing and chasing, counted separately from hours spent reviewing.",
        "why_first": "This is the walking skeleton, and it sits on the weakest leg of our own case, which we would rather state than hide. Nothing we fetched tells us how your data calls run today. The entire evidence base is one clause in requisition 2026-2731 saying the new hire participates in any and all data call activities (C11). No baseline exists, so a tool bought before a measurement is a guess with an invoice attached. It is the smallest job on this board and it is the only one that produces a hard result the rest of the roadmap can be funded from. The clock is the Dahlgren seat, requisition 2026-2731, live now at $130,000 and up (C09). Whoever fills it will invent a personal manual method for the data-call work inside a quarter, and that method becomes the habit any tool then has to displace. Landing the measurement alongside that hire costs a fraction of landing it afterwards, and that is the only genuine cost of delay on the board."
      },
      {
        "item": "Extract the owner map for that same pursuit and write down the method that produced it, so your team can run it again without us. Who, across the seven subsidiaries and 46 locations, owns which kind of answer, tied line by line to the compliance matrix GovEagle already produces (C48, C51).",
        "metric": "Share of that pursuit's compliance-matrix items with a named owner resolved by a written rule rather than by asking somebody. Recorded as a number, not as a judgement. Second metric, the method is written clearly enough that your own team repeats the extraction on a second pursuit with nobody from us in the room.",
        "why_first": "It falls out of the measurement at almost no extra cost, and it is the artefact you keep if you stop at the first gate. It is also the actual work behind any tracker. The honest top failure mode of a system like this is not accuracy, it is the owner map going stale, and that gets measured at Gate 4 rather than promised here."
      }
    ],
    "next": [
      {
        "item": "The Data Call Tracker specification with its acceptance bar, written for you to own and to hand to GeoNorth. Owner-routing rules, due dates, a scheduler, reminders, escalation, and a completeness board read against the compliance matrix. Zero model steps in the shipped path, so there is no chain of probabilities to compound and every step can be tested exhaustively. It tracks status and never authors a fact, never vouches for the truth of an answer, and never writes into a submitted volume.",
        "metric": "The acceptance bar is written in the six numbers the Now measurement produced, not in adjectives, so a finished tracker either clears it or does not. Second metric, GeoNorth can price and schedule the build from the specification without a single question back to us."
      },
      {
        "item": "Run the tracker alongside your current method on one real data call, in the shadow, before it becomes anyone's method. Built by GeoNorth if they want it, which is the outcome we expect and the one we are writing the specification for.",
        "metric": "Items outstanding at your internal cut-off, and re-routes to a different owner, both measured against the Now baseline on a pursuit of comparable size. Our proposed bar is that both at least halve. Below that it stays in the shadow and the spend stops."
      },
      {
        "item": "Measure how often the owner-routing rules fail to resolve an owner from a free-text requirement. This is the one node in the whole system that could ever earn a single model call, and we are not proposing one now.",
        "metric": "Rules-miss rate per pursuit. A model call gets considered only if the miss rate stays above a level you agree is worth paying to close, and it would be one call at one node with a human confirming the routing, never a chain of steps handing errors to each other."
      },
      {
        "item": "Check the owner map for decay at 90 days against a live pursuit, because staleness is what kills this class of system, not accuracy.",
        "metric": "Share of owner-map entries still correct 90 days after extraction. Below a bar you set, the honest answer is that the map needs a named owner inside Tatitlek or that it should not exist at all."
      }
    ],
    "later": [
      {
        "item": "An LLM disclosure and incident register. Deterministic, a form and a table and a workflow, and we will say out loud that it is mostly not an AI build, because a regulatory attestation needs full transparency and that is a stated wrong-fit condition for a model. GovEagle is its first row (C08). The GSA acquisition rule posted to the Federal Register on June 17th is PROPOSED and not in force (C45, C46, C47), and whether your capture use falls inside it is unestablished, since C46 covers models used in the performance of a contract or task order and capture sits before award. We are not going to tell you that you are in scope for something nobody has ruled on. It is worth having on its own merits and it should ride along cheaply with other work rather than compete for a slot.",
        "metric": "Time from a question arriving to a complete, current answer about which AI tools are in use, who operates each one, and which contract or task order it touches. Today that answer lives in people's heads, and a register turns it into a lookup."
      },
      {
        "item": "Retrieval over the ordering terms of the vehicles and certifications you publish, ISO 9001:2015, ANC 8(a) sole source contracting, SEAPORT NXG, GSA STARS III, OASIS+ 8(a) and SB (C06). Each carries its own ordering process and its own reporting. Low risk, high frequency, and deliberately left fuzzy rather than broken down before there is a reason to.",
        "metric": "Time for a capture manager to get the correct ordering path and its constraints for a named vehicle, measured against how long that takes today."
      },
      {
        "item": "Retrieval over your own documents so the institutional memory is queryable. Your CEO has held the seat since 2006, your President since 2018, your COO since 2015 (C19, C20, C21). An organisation with tenures like that keeps a great deal of its memory in people and in files rather than in systems, and retrieval over material you already own is the only honest way to make that memory answerable. A Later bet, not a first build.",
        "metric": "Share of the questions a new capture hire asks in their first 90 days that are answerable from documents rather than from somebody's recall."
      },
      {
        "item": "REFUSED, and written here so nobody circles back later thinking we overlooked it. A Bid/No-Bid Capacity Check is not on any lane and is not something we will sell you. GovEagle already ships bid/no-bid analysis, opportunity fit score, pWin and early go or no go guidance (C48, C49). The part GovEagle does not cover lives inside your staffing, pricing and contracts systems, which is GeoNorth's home ground and not ours.",
        "metric": "None. A refusal carries no metric and is not work we will do."
      },
      {
        "item": "REFUSED. A Shareholder Preference Talent Matcher is not on any lane. The argument that would have sold it, that your job board contradicts your published hiring preference for shareholders, shareholder descendants and shareholder spouses, is on our own rejected list. Your Prince William Sound and Valdez work routes through a separate TCC hiring channel, so that board was never the whole hiring surface, and a pitch built on an inference we had already refused is the exact failure our fact-checking exists to stop.",
        "metric": "None. A refusal carries no metric and is not work we will do."
      },
      {
        "item": "REFUSED. The Key Personnel and Past Performance Evidence Engine is not on any lane, and it was our own highest-scoring candidate before the fetch. Its past-performance half duplicates what GovEagle already does, in the vendor's own words (C49, C50). Its resume half is unverified in both directions, so it is a question for your GovEagle rep and never a roadmap item, and we refuse to answer it for you in either direction.",
        "metric": "None. A refusal carries no metric and is not work we will do."
      }
    ],
    "gates": "Five gates, each one a real off-ramp, and the money is released only as the results prove out. GATE 0, zero cost, before anything is bought. The coverage map plus the two answers from your GovEagle rep. If the rep confirms that Team assignments already reaches contributors outside the proposal team across your subsidiaries and locations, the tracker is a duplicate and it dies here, unbought. We wrote that possibility down before you asked the question, because it is the single inference most likely to make this whole recommendation wrong. What you keep if you stop, the map, in writing, free. GATE 1, the honest one, and it is built so it can say stop. Before the measurement runs, your proposal manager and your BD lead write down what a process that holds looks like, on the six numbers in the Now lane. Then we measure one real data call and compare it against your written bar, not ours. If it clears, the right outcome is that you buy nothing further from us. We will say so in writing, the specification half of the scope does not get written and does not get billed, and the engagement ends there having cost you a few hours and a small fee. If you would rather we propose the bar, ours is that fewer than one item in five needed a re-route to a different owner, and nothing was outstanding at your internal cut-off. What you keep if you stop, the baseline numbers, the owner map for that pursuit, and the extraction method. GATE 2, build versus buy, and you should expect us to lose it. The specification goes to GeoNorth. If GeoNorth can price and schedule the build from it without a question back to us, GeoNorth builds it, hosts it and owns it, and that is a success for this engagement rather than a loss. We are selling a specification, a measurement and a method, never an exclusive build and never a dependency, and pretending otherwise to a company that owns a NAICS 518210 subsidiary would be an insult. GATE 3, the pilot gate. The tracker shadows the current method on one real data call before it becomes anyone's method. The bar is the Gate 1 baseline, and our proposal is that outstanding-at-cutoff and re-route counts both at least halve on a pursuit of comparable size. Below that it stays in the shadow and the spend stops. GATE 4, the maintenance gate at 90 days. The owner map gets checked for decay against a live pursuit. If it has gone stale past a bar you set, the honest answer is that it needs a named owner inside Tatitlek or that it should not exist, because a tracker sitting on a stale owner map is worse than email. WHAT WE NEED FROM YOU, named here because this is where the real schedule risk lives and it is never in our engineering. One live pursuit we can instrument after September 30th, with your proposal manager's permission. The compliance matrix for that pursuit exported out of GovEagle, and whether that export surface exists is unverified, so it is the first thing we check rather than the first thing we assume. Your proposal manager for about an hour at the start and an hour at the end. The two questions put to your GovEagle rep, which only you can ask. One named decision-maker for the gates, and we assume that is you unless you tell us otherwise.",
    "high_integrity_dates": [
      "September 19th, a commitment already met. The GovEagle coverage map is in this study today, free. There is no start date to wait for and nothing to sign to get it.",
      "September 30th, a deliberate promise to stay out of your way. The federal fiscal year ends in eleven days and it is the heaviest solicitation and award window of your year. We will not instrument anything before it. The measured data call runs on the first suitable live pursuit after September 30th, because measuring your team inside that window would get in the way and would also produce a baseline you could fairly dismiss as atypical.",
      "No other date here is a commitment, including any date tied to the Dahlgren seat, which has no published start date and which we will not invent one for. Everything else is anchored to your action rather than to a calendar, for example within a set number of days of receiving the compliance matrix export, because a date we do not control is a promise we can't keep."
    ]
  },
  "roi": {
    "cost_note": "Five year total cost of ownership, not a sticker price, and the largest line is not ours. The stack is our Phase 1 fee (a fixed band of $16,000 to $22,000 for one data call measured end to end, the owner map extraction method, and the Data Call Tracker specification with its acceptance bar), plus the internal build and integration if the measurement says build, plus training and change management stated in hours, plus five years of run cost, plus contingency. The build line is assumed to be internal work by GeoNorth Information Systems, their own NAICS 518210 subsidiary (C05), because a company that owns an information systems subsidiary should own this tool, and we are not asking for an exclusive build. Two things about the run line are worth saying out loud. There is NO inference or token cost, because the shipped tracker has no model in its path, it is rules, a scheduler and a completeness board. The real recurring cost is keeping the owner map fresh across seven subsidiaries and 46 locations (C04, C05), assumed at 70, 45 and 32 hours a year across the three columns, and staleness is the failure mode most likely to kill this tool. Training and change management is 140, 110 and 90 hours, priced at each column's own hourly rate, never described as included. Contingency is 20 percent in the conservative and most likely columns and 15 percent in the aggressive one. Our Phase 1 fee is roughly a quarter to a third of the assumed build cost it gates, which is the whole argument for buying the measurement before the tool.",
    "benefits": [
      {
        "benefit": "Proposal coordinator time spent assembling and chasing outstanding data call answers",
        "kind": "capacity",
        "basis": "Assumed 8, 12 and 16 hours of coordination per data call across the three columns, at an assumed loaded rate of $62, $78 and $88 an hour, with an assumed cut of 25, 35 and 45 percent, against an assumed 10, 20 and 32 data calls a year. Not one of those numbers is measured at Tatitlek. The only verified salary anchor in the whole model is the $130,000.00+ posted floor on requisition 2026-2731 (C09), which is a floor on one Dahlgren seat and not a fully loaded cost.",
        "note": "CAPACITY, and it converts to cash only by REDEPLOY, the coordinator's recovered hours going back into capture plans, price to win work and gate review material that the same posting already assigns (C13, C14). No hire is deferred and no backfill is avoided by this line, so we do not claim either. Nothing fetched says their data calls are slow, so this line assumes a coordination load exists, never that it is failing."
      },
      {
        "benefit": "Time spent working out who across the subsidiaries owns a given answer",
        "kind": "capacity",
        "basis": "Assumed 3, 5 and 6 hours per data call at the same column rates, with an assumed cut of 35, 50 and 60 percent, against the same assumed volumes. The cut is higher here than anywhere else in the model because a written owner map is the part of the work a list genuinely removes.",
        "note": "CAPACITY, converting by REDEPLOY. This is the one benefit that lands from Phase 1 ALONE, with or without a tracker, because the owner map is a Phase 1 deliverable and it is theirs to keep. It decays without upkeep, which is why the run cost carries owner map refresh hours in every column."
      },
      {
        "benefit": "Contributor time lost to unclear, duplicated or re-sent requests across 46 locations",
        "kind": "capacity",
        "basis": "Assumed 8, 14 and 20 aggregate contributor hours per data call, spread across everyone a single data call touches, at an assumed $55, $62 and $68 an hour, with a deliberately low assumed cut of 15, 25 and 30 percent.",
        "note": "CAPACITY, and the WEAKEST line in the stack, which is why its cut is the lowest. It arrives as fragmented minutes across many people in many places, and fragmented minutes are the hardest kind of capacity to redeploy into anything a CFO can see. Treat it as the line to delete first if the case has to stand on less."
      },
      {
        "benefit": "Avoided rebuild of a tracker specified without a measured baseline",
        "kind": "cash",
        "basis": "Assumed one such rebuild every five years (0.2 events a year), at an assumed rebuild cost of $20,000, $25,000 and $30,000, with an assumed 40, 50 and 60 percent of that avoided by holding a measured baseline and a written acceptance bar before anyone writes code.",
        "note": "CASH, by AVOID-SPEND, and it is the decision data line. It is the only benefit that exists because Phase 1 is a measurement rather than a tool. It is deliberately small, since a counterfactual about a build they have never said they would commission is the softest thing in this model and should not be asked to carry the case."
      }
    ],
    "benefit_phasing": "No day one benefits in any column. Phase 1 is a few weeks and produces a number, not a saving. If the gate opens, the tracker goes live around the middle of year one, then takes about ninety days to stabilise while the owner map is corrected against what actually happens on a live data call. Year one is therefore modelled at 25, 30 and 40 percent of run rate across the three columns. Year two is the first full run rate year. Years three to five hold that run rate and do not compound, because a completeness board has no mechanism by which it gets better on its own, and a model that assumed compounding here would be inventing one. Run cost accrues over 4.5 of the five years, matching the mid year one go live.",
    "scenarios": {
      "conservative": "Low volume, low hours, thin cut, top of our fee band, highest build and run cost, slowest ramp. Ten data calls a year, 8 coordination hours each, a 25 percent cut, $62 an hour with no employer burden added on top of the verified posted floor (C09), a $48,000 internal build, $6,000 a year to run and 20 percent contingency. THIS COLUMN DOES NOT CLEAR, and it is not close. At the low end of our assumed volume the tracker recovers a small fraction of its five year cost, which is the honest answer to a question nobody has measured yet. That result is the argument, not an embarrassment. It is why the recommended ask is NOT the tracker. The ask is Phase 1 at $16,000 to $22,000, priced openly as decision data, and its worst honest outcome is that the measurement says their process holds and they buy nothing further from us this quarter. That outcome still leaves them the owner map, the specification and a documented reason not to spend the build money, which is what the fee is for.",
      "most_likely": "Twenty data calls a year, 12 coordination hours each, a 35 percent cut, $78 an hour, a $44,000 internal build, $5,000 a year to run, 20 percent contingency and a 30 percent year one ramp. THIS COLUMN DOES NOT CLEAR EITHER, and it is the most important number in the section. At our genuine central assumptions the tracker returns roughly two thirds of its five year cost, which says the build is a real decision rather than an obvious one, and that it turns on two quantities nobody in this document has measured, how many data calls a year they run and how many hours each one actually consumes. Measure those two numbers for the price of Phase 1 and the decision stops being a guess.",
      "aggressive": "Thirty two data calls a year, 16 coordination hours each, a 45 percent cut, $88 an hour, a leaner $36,000 internal build, $4,200 a year to run, 15 percent contingency and a 40 percent year one ramp. THIS IS THE ONLY COLUMN THAT CLEARS, and it pays back inside the five year horizon rather than quickly. It requires their real volume to sit near the top of our assumed range and the coordination load to be genuinely heavy. We have no evidence that it does, so we are not pricing as though it does. A build that only clears under aggressive assumptions is a build you fund after a measurement, never before one."
    },
    "conservative_clears": false,
    "payback_range": "There is no payback inside five years in the conservative or most likely columns. The aggressive column pays back somewhere in year three, and that figure moves by many months on small changes to volume and hours, so read it as a band and not a date. The Phase 1 ask is not a payback instrument at all and we will not dress it as one. It is decision data, priced at $16,000 to $22,000 against an assumed build of $36,000 to $48,000 and a five year path costing roughly $90,000 to $130,000, and what it buys is the right to spend or not spend that money on a measured number instead of an assumption.",
    "base_rate_note": "The outside view first. MIT's finding is that about 95 percent of enterprise AI pilots show no measurable P&L impact, and RAND puts the failure rate of AI projects at around 80 percent. In this company's own market Deltek reports 90 percent of government contractors now using AI in some capacity, up from 45 percent (C28), while 45 percent of the same respondents say they are unclear on the return (C31). Nearly everyone is adopting, and nearly half can't prove payback. Four things are designed into this ask to put it in the small share that pays. First, the shipped tracker has NO MODEL IN ITS PATH. It is rules, a scheduler and a completeness board, so it is not in the reference class those failure figures measure, and its nearest published peer is the kind of narrow non generative automation AWS credits Koniag with, where a one hour vendor responsibility task became two minutes (C44), rather than the generative drafting tools the surveys are counting. Second, the first paid deliverable is a MEASUREMENT and not a tool, so the most common failure, building something nobody needed, is gated out before the build money moves. Third, adoption has a named owner rather than a committee, the Dahlgren capture seat posted at $130,000 and up (C09), and landing alongside that hire beats landing after it invents a personal manual method. Fourth, we are willing to conclude that they should buy nothing, and the conservative and most likely columns above are what that willingness looks like in numbers.",
    "value_owner": "Mark Wamsher, Vice President of Business Development (C01), owns the number at the executive level, because the tool sits in the pipeline his own requisition describes (C08, C10). Day to day ownership belongs to the incoming Strategic Proposal Support and Capture Manager on requisition 2026-2731 (C09), whose posting already assigns participation in data call activities (C11), with the standing Bid and Proposal team owning the completeness data since it already owns proposal process, scheduling and compliance (C12). The variance check is concrete and cheap. Phase 1 produces the baseline, measured hours and elapsed days on one real data call, broken out by coordinator time, owner identification time and contributor time. After go live, the same three measurements are taken on the next three data calls and compared against that baseline, and the gate to any further spend is whether the measured delta is at least 60 percent of what the most likely column assumes. If it is not, the honest call is to stop, and we will say so in writing.",
    "assumptions": [
      "VOLUME IS ASSUMED, NOT MEASURED. Ten, 20 and 32 formal proposal data calls a year across the three columns. Nothing fetched states their pursuit count or their data call count, and confidence in this driver is LOW. It is the single driver that moves the answer most. Phase 1 replaces it with their own number. The 30 pursuits per quarter figure that appeared in our internal scoring earlier in this run was invented, it is forbidden here, and it is used nowhere in this model.",
      "HOURLY RATES ARE ASSUMED. $62, $78 and $88 an hour for proposal and capture time, $55, $62 and $68 for contributor time. The single verified salary anchor available is the $130,000.00+ posted floor on requisition 2026-2731 (C09), which is a posted FLOOR on one Dahlgren seat and not a fully loaded cost. The conservative column deliberately adds no employer burden on top of that floor, the other two columns add assumed burden.",
      "HOURS PER DATA CALL ARE ASSUMED. Coordination 8, 12 and 16 hours. Owner identification 3, 5 and 6 hours. Aggregate contributor time 8, 14 and 20 hours. Deltek's reported average of 84 hours to develop a single proposal (C29) is a SELF REPORT by respondents to Deltek's survey of 917 contractors (C27), not a measurement of Tatitlek, so it is used here only as an outer envelope that makes a coordination slice of this size plausible. It is not a driver in this model.",
      "CUT PERCENTAGES ARE ASSUMED. 25, 35 and 45 percent on coordination. 35, 50 and 60 percent on owner identification. 15, 25 and 30 percent on contributor friction. The published peer results (C39 to C44) are vendor published and unaudited, with no baseline method disclosed, and C42 caps the strongest of them at a Red Team ready draft rather than a submission ready proposal, so none of them sets a driver here.",
      "THE PROBLEM ITSELF IS ASSUMED. Nothing fetched says their data calls are slow, late or expensive. The entire evidence base is one clause in one live posting saying the hire participates in any and all data call activities as needed (C11). This model assumes a coordination load exists, which a proposal across seven subsidiaries and 46 locations (C04, C05) must have in some size, and it assumes nothing about whether that load is currently failing.",
      "BUILD COST IS ASSUMED at $48,000, $44,000 and $36,000 of internal effort, on the assumption that GeoNorth Information Systems (C05) builds and hosts the tracker. We are not selling an exclusive build, and if they hand the specification to GeoNorth and build it themselves, the engagement did its job.",
      "OUR PHASE 1 FEE is a fixed band of $16,000 to $22,000, and the conservative column prices the top of the band. The scope driver behind the band is how many of the seven subsidiaries (C05) the owner map has to reach.",
      "TRAINING AND CHANGE MANAGEMENT is 140, 110 and 90 hours, priced at each column's own coordinator rate. It covers participation in the measured data call, the owner map interviews, and rollout to the people a data call actually touches. It is never described as included.",
      "RUN COST is 70, 45 and 32 hours a year of owner map upkeep plus hosting and monitoring inside GeoNorth, accruing over 4.5 of the five years. There is NO inference or token line, because the shipped tracker has no model in its path. Staleness of the owner map is the top failure mode and this line is what pays to prevent it.",
      "CONTINGENCY is 20 percent in the conservative and most likely columns and 15 percent in the aggressive one, sized against organisational risk rather than software risk.",
      "RAMP is 25, 30 and 40 percent of run rate in year one, reflecting a mid year one go live and about ninety days of stabilisation. Years three to five are modelled flat, with no compounding, because a completeness board has no mechanism that makes it better on its own.",
      "CAPACITY TO CASH CONVERSION IS REDEPLOY in all three labour lines, and it is not automatic. If the recovered hours do not visibly go into capture plans, price to win analysis or gate review material (C13, C14), those lines stay capacity and never become dollars. Only the avoided rebuild line is cash.",
      "QUARANTINED, AND DELIBERATELY OUTSIDE THE FORMULA. The free Phase 0 coverage map, the answer to the open question about whether GovEagle handles key personnel resumes, reduced dependence on the one person who knows who to call, and a cleaner first ninety days for the incoming Dahlgren hire. All real, none of them quantified here, none of them propping up a column.",
      "NO ROW IN THIS TABLE IS A VERIFIED FACT ABOUT THEIR BUSINESS. The only verified figure anywhere in the model is the posted salary floor (C09), and it is an anchor for an assumed rate rather than a measured cost. Expect the provenance rail to read assumed and modelled throughout. That is what a pilot is for.",
      "THE MISSILE DEFENSE AGENCY AWARD (C22, C23) IS USED NOWHERE IN THIS MODEL. No line here rests on it, and nothing in this section implies it is under review, flagged or at risk."
    ],
    "drivers": {
      "scenarios": {
        "conservative": {
          "pursuits_per_year": 10,
          "benefit_lines": [
            {
              "label": "Coordinator time assembling and chasing data call answers",
              "hours_per_pursuit": 8,
              "rate": 62,
              "cut": 0.25
            },
            {
              "label": "Finding who owns an answer across the subsidiaries",
              "hours_per_pursuit": 3,
              "rate": 62,
              "cut": 0.35
            },
            {
              "label": "Contributor time on unclear or repeated requests",
              "hours_per_pursuit": 8,
              "rate": 55,
              "cut": 0.15
            }
          ],
          "avoided_cost_lines": [
            {
              "label": "Rebuild of a tracker specified without a measured baseline",
              "events_per_year": 0.2,
              "cost_per_event": 20000,
              "reduction": 0.4
            }
          ],
          "implementation": 70000,
          "training": 8680,
          "run_cost_per_year": 6000,
          "run_cost_years": 4.5,
          "contingency": 0.2,
          "year1_ramp": 0.25,
          "years": 5
        },
        "most_likely": {
          "pursuits_per_year": 20,
          "benefit_lines": [
            {
              "label": "Coordinator time assembling and chasing data call answers",
              "hours_per_pursuit": 12,
              "rate": 78,
              "cut": 0.35
            },
            {
              "label": "Finding who owns an answer across the subsidiaries",
              "hours_per_pursuit": 5,
              "rate": 78,
              "cut": 0.5
            },
            {
              "label": "Contributor time on unclear or repeated requests",
              "hours_per_pursuit": 14,
              "rate": 62,
              "cut": 0.25
            }
          ],
          "avoided_cost_lines": [
            {
              "label": "Rebuild of a tracker specified without a measured baseline",
              "events_per_year": 0.2,
              "cost_per_event": 25000,
              "reduction": 0.5
            }
          ],
          "implementation": 62000,
          "training": 8580,
          "run_cost_per_year": 5000,
          "run_cost_years": 4.5,
          "contingency": 0.2,
          "year1_ramp": 0.3,
          "years": 5
        },
        "aggressive": {
          "pursuits_per_year": 32,
          "benefit_lines": [
            {
              "label": "Coordinator time assembling and chasing data call answers",
              "hours_per_pursuit": 16,
              "rate": 88,
              "cut": 0.45
            },
            {
              "label": "Finding who owns an answer across the subsidiaries",
              "hours_per_pursuit": 6,
              "rate": 88,
              "cut": 0.6
            },
            {
              "label": "Contributor time on unclear or repeated requests",
              "hours_per_pursuit": 20,
              "rate": 68,
              "cut": 0.3
            }
          ],
          "avoided_cost_lines": [
            {
              "label": "Rebuild of a tracker specified without a measured baseline",
              "events_per_year": 0.2,
              "cost_per_event": 30000,
              "reduction": 0.6
            }
          ],
          "implementation": 52000,
          "training": 7920,
          "run_cost_per_year": 4200,
          "run_cost_years": 4.5,
          "contingency": 0.15,
          "year1_ramp": 0.4,
          "years": 5
        }
      }
    }
  }
}
```

---

## THE RESEARCH ROOM (verbatim, as the four researchers returned it)

```json
{
  "company": {
    "what_they_do": "The Tatitlek Corporation (TTC) is the ANCSA village corporation for the Native Village of Tatitlek, an Alutiiq community on the eastern shore of Prince William Sound. Founded 1973 under the Alaska Native Claims Settlement Act, headquartered in Anchorage. Despite Alaska ownership the operating business is almost entirely a Lower 48 federal services contractor: 'The Tatitlek Corporation delivers mission-critical solutions to government agencies, defense contractors, and high-profile private sector customers at locations throughout the United States and around the world' (https://tatitlek.com/operations/). Seven subsidiaries are named on its own site, each with its own UEI, CAGE and primary NAICS: (1) GeoNorth Information Systems LLC, satellite/geospatial, collection, processing and delivery of remotely-sensed information, operates a U.S.-owned satellite downlink for electro-optical and SAR data, NAICS 518210; (2) Tatitlek Federal Services LLC, professional/admin support, engineering, information assurance and cyber security services, NAICS 541611, GSA 8(a) STARS III 47QTCB22D0425, GM Don Muse; (3) Tatitlek Government Services LLC, facilities, security, logistics, IT, NAICS 561210, STARS III 47QTCB22D0658, OASIS+ 8(a) 47QRCA26DA026 and OASIS+ SB 47QRCA25DSB06, GM Russ Todd; (4) Tatitlek Management Services LLC, facilities operations and maintenance plus professional services, NAICS 541990, GSA MAS 47QRAA25D00AN, SeaPort-NxG N0017825D7880, GM Robert Ruggiero PMP CFM CPE; (5) Tatitlek Professional Services LLC, NAICS 541512, GM Robert Dulin; (6) Tatitlek Technologies LLC, NAICS 518210, OASIS+ Unrestricted (Technical and Engineering), GM Paul Fondren; (7) Tatitlek Universal Services Inc., construction, commercial and industrial facilities construction, jet engine test cell construction, NAICS 236220, bonding single projects up to $30 million and an aggregate bonded surety program of $100 million, GM Jared Hayes. Historic/legacy entity names in the public record: Tatitlek Support Services Inc., Tatitlek Training Services Inc. (military role players), Tatitlek Construction Services Inc., Tatitlek Contractors Inc. Separately TTC is a third owner of TCC (Tatitlek Chenega Chugach), the Alaska oil spill prevention and response joint venture serving Alyeska's Ship Escort Response Vessel System out of Valdez. It also runs the Copper Mountain Foundation (scholarships), shareholder services, land management, and Valdez real estate.",
    "size": "FACT from their own site: Shareholders 300+, Global employees 1,300, Operations over five decades, and '1,300 employees geographically dispersed through project and business offices located throughout Alaska and 46 locations worldwide' (https://tatitlek.com/ and https://tatitlek.com/our-company/). Lands: 108,166 acres in Prince William Sound (https://tatitlek.com/lands/); BLM records the full ANCSA entitlement as 137,245.79 acres through Sections 12(a) and 12(b), with final patents signed April 11, 2024, making Tatitlek the first village in the Chugach Region to obtain its full land entitlements (https://www.blm.gov/blog/2024-04-18/tatitlek-entitlement-complete). Open hiring on September 19, 2026: 150 live requisitions across three pages of their iCIMS board. HigherGov lists TTC as parent of 18 subsidiary organizations, UEI JUR8UL7JVLG7, CAGE 63FM0, founded October 25, 1973, most recent federal award dated September 1, 2026. THIN SPOT, FLAGGED: no revenue figure is published anywhere fetchable. TTC does NOT appear in Alaska Business Magazine's 2025 Top 49ers ranking (that list is self-reported). USAspending's parent-level rollup returns $47,952,806.33 over 208 transactions on one parent hash and $0 on another, which does not reconcile with the subsidiary-level awards, so NEITHER is treated as a revenue or obligations figure.",
    "locations": [
      "HQ: 561 E 36th Ave, Ste 400, Anchorage, AK 99503, (907) 278-4000 (https://tatitlek.com/contact-us/)",
      "Arlington, VA: 2121 Crystal Drive Suite 510, Arlington, VA 22202",
      "Dahlgren, VA: 4485 Danube Drive, King George, VA 22485",
      "Huntsville, AL: 641 Wynn Drive NW Suite 201, Huntsville, AL 35816",
      "Oklahoma City, OK: 10701 West Garnett, Oklahoma City, OK 73114",
      "Native Village of Tatitlek, Prince William Sound, AK, plus 108,166 acres of TTC land",
      "Valdez, AK: Chugach Naswik Suites, 23,000 sq ft, 36 units, opened September 5, 2024, jointly owned with Chenega Corporation and Chugach Alaska Corporation",
      "Work sites in current job listings: NSWC Dahlgren VA (~33 of 150 listings), Arlington VA, Portsmouth VA, Blackstone VA, Fort Belvoir VA, Quantico VA, Sterling VA, Washington DC incl. the Harry S. Truman Building, Fort Meade MD, Aberdeen Proving Ground MD, Bethesda MD, Hanover MD, USCG Yard Baltimore MD, USCG Base Elizabeth City NC, Atlantic Beach NC, Moorestown NJ, USCG TRACEN Cape May NJ, Charleston SC, Philadelphia PA, Fort Worth TX, El Paso TX, San Diego CA, Mountain View CA, Redstone Arsenal AL, Birmingham AL, Tinker AFB OK, Fort Sill OK, Lawton OK, Joint Base Lewis-McChord WA",
      "Alaska-performed federal work does exist: a US Coast Guard C5I Division 3 Portsmouth communications-systems support contract to Tatitlek Federal Services LLC, place of performance Anchorage AK 99503, $3,411,236.94, August 30 2024 to August 29 2027, NAICS 541330"
    ],
    "revenue_model": "Four streams. (1) The dominant one is federal services contracting through the subsidiaries, sold on set-aside and GWAC vehicles rather than open competition. Their own capability list is 'ISO 9001:2015, ANC 8(a) Sole Source Contracting, SEAPORT NXG, GSA STARS III, OASIS+ 8(a) and SB' (https://tatitlek.com/our-company/). They market the 8(a) sole-source path directly to contracting officers: 'Reduce procurement cycle time with a direct 8(a) sole-source award, ideal when schedule sensitivity is paramount' (https://tatitlek.com/anc-8a-sole-source-contracting/). A live example of scale and of the model: Tatitlek Management Services LLC holds MDA award HQ085826CE001, set-aside type 8(A) SOLE SOURCE, Number of Offers Received: 1, potential value $99,981,096.40, obligated to date $11,707,278.07, period of performance October 8 2025 through October 7 2027 with options to April 7 2033, place of performance Huntsville AL. Work sold spans three declared lines: Professional and Administrative Support Services, Technical Services, Installation Support Services. (2) The TCC joint venture with Chenega and Chugach Alaska, holding Alyeska SERVS oil spill response work in Prince William Sound since 1994, a union employer with Laborers 341, Teamsters 959 and Operating Engineers 302. (3) Land and real estate, 108,166 acres plus the 36-unit Chugach Naswik Suites in Valdez, workforce housing for shareholder employees involved in oil spill response under Trans-Alaska Pipeline System contracts. (4) Distribution to 300+ shareholders as dividends and special distributions. GeoNorth also sells commercially and to intelligence customers, e.g. a five-year $15 million NGA contract for Arctic persistent surveillance with Lockheed Martin and UAF as partners.",
    "pains": [
      {
        "pain": "Business development and capture is under-resourced relative to the vehicle count. They are hiring a $130,000+ Strategic Proposal Support and Capture Manager expected to carry the whole front half of the pipeline alone, while a separate team owns the back half. The posting also reveals capture strategy has to be reconciled against delivery capacity, the classic ANC squeeze.",
        "evidence_quote": "support the full opportunity lifecycle, from early identification and qualification through capture strategy execution ... Maintain an individual pipeline of assigned opportunities in GovEagle, logging, staging, and updating each pursuit ... Coordinate with operations, contracts, pricing, and program staff to align capture strategy with business goals and execution capacity ... the Bid and Proposal team owns the proposal process, scheduling, and compliance",
        "source_url": "https://careers-tatitlek.icims.com/jobs/2731/strategic-proposal-support-%26-capture-manager/job?in_iframe=1",
        "kind": "fact"
      },
      {
        "pain": "Proposal work itself is described as data calls and resume scrubbing, the two most manual, lowest-leverage tasks in federal capture, and they are being assigned to a single senior hire.",
        "evidence_quote": "participation in any and all data call activities as needed ... Support the development and scrubbing of key personnel resumes ... Develop capture plans, price to win analysis, and gate review materials for assigned pursuits",
        "source_url": "https://careers-tatitlek.icims.com/jobs/2731/strategic-proposal-support-%26-capture-manager/job?in_iframe=1",
        "kind": "fact"
      },
      {
        "pain": "Requisitions sit unfilled for a long time. Of the 150 open listings on September 19, 2026, 22 still carry 2025-series requisition numbers, the oldest visible being 2025-2195. iCIMS requisition IDs are year-prefixed, so these were opened in the prior calendar year and are still live.",
        "evidence_quote": "Still open with 2025 requisition numbers: Human Resources Specialist | US-MD-Fort Meade | 2025-2195, Service Desk Analyst Tier 1 | US-DC | 2025-2206, Armed Security Officer | US-NJ-USCG TRACEN Cape May | 2025-2225, Armed Security Officer | US-NC-USCG Base Elizabeth City | 2025-2229, Journeyman HVAC Technician | US-VA-Arlington | 2025-2312, Human Resources Specialist | US-VA-Fort Belvoir | 2025-2383, Quality Control Manager | US-OK-Lawton | 2025-2452",
        "source_url": "https://careers-tatitlek.icims.com/jobs/search?ss=1&in_iframe=1&pr=2",
        "kind": "fact"
      },
      {
        "pain": "Hiring is almost entirely Outside, which sits awkwardly against a written shareholder hiring preference and an Anchorage headquarters. Zero of the 150 current openings list an Alaska location.",
        "evidence_quote": "The Tatitlek Corporation gives hiring, promotion, training and retention preference to shareholders, shareholder descendants and shareholder spouses who meet job qualifications.",
        "source_url": "https://tatitlek.com/careers-page/",
        "kind": "fact"
      },
      {
        "pain": "Single-site concentration risk at NSWC Dahlgren. Roughly 33 of the 150 open listings are Dahlgren, VA, spanning sysadmins, engineering technicians, cost analysts, technical writers, schedulers and program analysts. They have also already litigated a lost bid there.",
        "evidence_quote": "GAO decision B-416711 et al., November 28, 2018: Tatitlek Technologies, Inc. protested award of a task order valued over $25 million for Administrative and clerical support services for Naval Surface Warfare Center Dahlgren Division under RFP No. N0017817R3058. Outcome: Protest denied.",
        "source_url": "https://www.gao.gov/products/b-416711,b-416711.2,b-416711.3,b-416711.4",
        "kind": "fact"
      },
      {
        "pain": "Their largest new award is an 8(a) sole-source over $20 million, awarded with one bidder, at exactly the moment the Pentagon announced a review of every sole-source 8(a) contract over $20 million. This is a dated, direct threat to the revenue model they advertise on their own site.",
        "evidence_quote": "Secretary Hegseth, reported January 22, 2026: We're actually taking a sledgehammer to the oldest DEI program in the federal government ... Second, we're doing away with these pass-through schemes. ... We'll make sure that every small business getting a contract is the one actually doing the work. The Pentagon would review all sole-source 8(a) contracts worth more than $20 million. Tatitlek Management Services' MDA award HQ085826CE001 is 8(A) SOLE SOURCE, Number of Offers Received: 1, potential value $99,981,096.40.",
        "source_url": "https://www.adn.com/business-economy/2026/01/22/pentagon-to-take-sledgehammer-to-contracting-program-central-to-many-alaska-native-corporations/",
        "kind": "fact"
      },
      {
        "pain": "Shareholder records are manual, deadline-driven and incomplete. They are publicly asking people to help locate shareholders they have lost contact with, and address changes are gated on a hard pre-dividend cutoff, which is where dividend replacement requests come from.",
        "evidence_quote": "Thank you for taking the time to help us find our missing shareholders! ... all address changes must be received no less than two-weeks prior to the dividend distribution date ... In order to change your direct deposit information, you will need complete the Direct Deposit form ... E-mail it to Shareholderservices@tatitlek.com. The services list itself includes Dividend Replacement Requests.",
        "source_url": "https://tatitlek.com/resources/",
        "kind": "fact"
      },
      {
        "pain": "The delivered work itself is high-volume manual records and compliance processing under contractual clocks, the exact shape of work that burns billable hours. Two live postings spell out the throughput obligations in their own contract language.",
        "evidence_quote": "HR Specialist, Fort Meade (req 2025-2195): Shall review and process award recommendations NLT (2) working days upon receipt for accuracy ... Must process awards within 5 working days upon receipt of approval ... Shall maintain award files IAW the Army Records Information Management Systems (ARIMS) and statistical data ... Shall execute award distribution runs three times a week or as necessary.",
        "source_url": "https://careers-tatitlek.icims.com/jobs/2195/human--resources-specialist/job?in_iframe=1",
        "kind": "fact"
      },
      {
        "pain": "Same shape on the security side. Clearance adjudication support is caseload management across multiple federal databases with paperwork accuracy checks done by hand.",
        "evidence_quote": "Clearance Coordinator, DC (req 2026-2758, $49.09/hourly): Utilizes various federal databases and resources to research candidates' investigative history ... Manages an assigned caseload to direct the timely initiation of investigations ... Evaluates submitted paperwork for accuracy in compliance with prescribed Federal Investigative Standards and criteria ... Conducts and analyzes results of a variety of National Agency Checks including NCIC, TECS, CCD, and NSC",
        "source_url": "https://careers-tatitlek.icims.com/jobs/2758/clearance-coordinator-%28dc%29/job?in_iframe=1",
        "kind": "fact"
      },
      {
        "pain": "They are on the buying side of procurement too, running their own open solicitation for the village with a live deadline six days out. That means an evaluation burden, not just a bidding burden.",
        "evidence_quote": "THE TATITLEK CORPORATION REQUEST FOR PROPOSALS Infrastructure Improvement Opportunity Study - RFP No. 26-01, issued on behalf of TTC and the Native Village of Tatitlek, amended August 26, 2026, proposals due September 25, 2026, 5:00 p.m. Alaska Time. No named point of contact or inquiry email is published on the notice page.",
        "source_url": "https://tatitlek.com/uncategorized/student-spotlight-lincoln-shanks-2/",
        "kind": "fact"
      },
      {
        "pain": "Shareholder base is small and the descendant pipeline is the growth mechanism, so shareholder services, scholarships, apprenticeships and the portal carry disproportionate weight relative to a 1,300-person operating company.",
        "evidence_quote": "Homepage: Shareholders 300+ against Global employees 1,300. Careers page programs: an Apprenticeship Program for original shareholders and registered descendants 18+ with HS diploma, and an Internship Program. Marci Cornell is listed as Shareholder Services Manager (2026-Present).",
        "source_url": "https://tatitlek.com/leadership/",
        "kind": "inference"
      },
      {
        "pain": "Employee-sentiment evidence could not be verified. Both Glassdoor and Indeed returned HTTP 403 to a direct fetch, so there is no quotable review text. Search snippets referenced roughly 3.6/5 on Glassdoor across about 98 reviews and about 140 Indeed reviews, but neither page was fetched and those numbers are NOT treated as established.",
        "evidence_quote": "Glassdoor: The server returned HTTP 403 Forbidden. Indeed: The server returned HTTP 403 Forbidden.",
        "source_url": "https://www.glassdoor.com/Reviews/Tatitlek-Corporation-Reviews-E386536.htm",
        "kind": "fact"
      }
    ],
    "reputation_screen": {
      "showrunner_verdict": "CLEARED at the Phase 2 RESEARCH GATE, on primary federal contract data, with the residual uncertainty recorded rather than hidden.",
      "the_flag_the_analyst_raised": {
        "finding": "Anchorage Daily News, July 24, 2018, names a Tatitlek subsidiary in a list of Alaska Native corporations that have held ICE contracts.",
        "exact_quote": "Companies that have had contracts over the last 15 years include NANA and subsidiaries, K'oyitl'ots'ina Ltd., Tatitlek Native Corp. subsidiary GeoNorth, Old Harbor and Barling Bay, and Doyon.",
        "source_url": "https://www.adn.com/business-economy/2018/07/24/alaska-native-corporations-are-a-billion-dollars-deep-in-border-control-contracts/",
        "what_the_article_does_NOT_say": "No contract type, no agency office, no dollar amount, no start or end date, and no detention-facility role for Tatitlek or GeoNorth specifically. They appear only in a list. The legal name is The Tatitlek Corporation, not Tatitlek Native Corp., so even the corporate name is inexact.",
        "analyst_corroboration_failed": "Three other ICE/ANC investigations were fetched and NONE names Tatitlek or GeoNorth: Alaska Public Media July 19 2018, El Paso Matters January 26 2021, Alaska Public Media October 23 2025."
      },
      "showrunner_primary_data_check": {
        "method": "Queried the USAspending prime-award API directly, four recipient searches, award types A/B/C/D: the Tatitlek parent family FY2015 to present (top 100 rows by value), GeoNorth FY2008 to present (100 rows), Tatitlek Support Services (33 rows), Tatitlek Training Services (39 rows). Roughly 270 award rows across 19 years.",
        "result": "ZERO immigration, customs, border or detention awards at any Tatitlek entity or at GeoNorth. Every Department of Homeland Security dollar in the data is U.S. Coast Guard, and the descriptions are explicit: Rescue 21 Alaska sustainment including the Alaska VHF communication system, Digital Selective Calling and Vessel Traffic Service, plus national security guard services at Coast Guard locations. Rescue 21 is the Coast Guard's maritime search-and-rescue distress calling system. GeoNorth's single largest customer by row count is the Indian Health Service (52 of 100 rows); its DoD work is imagery libraries and web content management.",
        "false_positives_noted": "An initial keyword screen flagged five GeoNorth rows and two Tatitlek Training rows. All seven are artifacts of the matcher finding the substring ICE inside SERVICE and PRICE. None is an immigration contract."
      },
      "reasoning": "The bar this routine has actually applied to the seventeen suppressed Alaska Native corporations is CURRENT, SUBSTANTIAL and DETENTION-SPECIFIC work: Bering Straits with shareholders publicly asking it to divest, NANA and Aleut through Akima at Krome and Guantanamo, Ahtna with a reported $35M guard contract at Port Isabel, Doyon operating the 800-bed El Paso Service Processing Center, Koniag with a GSA ICE ERO award six days before its run, Chenega providing detention operation services, ASRC with an $11M DHS CBP award. Tatitlek meets none of that. The single adverse item is one undetailed sentence in a list, eight years old, using the wrong corporate name, uncorroborated by three parallel investigations, and unsupported by any award record across nineteen years of primary data. Suppressing on that evidence would apply a standard to Tatitlek that none of the shipped leads was held to.",
      "b_federal_contracting_fraud_fca_8a_misconduct_self_dealing": {
        "finding": "NOTHING FOUND. No False Claims Act settlement, no DOJ, GSA OIG or SBA OIG action, no debarment or suspension, and no 8(a) size-protest or self-dealing finding against The Tatitlek Corporation or any subsidiary name identified.",
        "what_was_searched": "DOJ and oversight.gov False Claims Act coverage; GSA OIG small-business-fraud releases; the specific subsidiary names Tatitlek Federal Services, Tatitlek Government Services, Tatitlek Management Services, Tatitlek Technologies, Tatitlek Professional Services, Tatitlek Universal Services, Tatitlek Support Services, Tatitlek Training Services, and GeoNorth, each paired with fraud, settlement, debarment, suspension, investigation and inspector general; and GAO's bid-protest docket.",
        "what_was_found_instead_and_it_is_not_fraud": [
          "A 2012 WAGE AND HOUR class action settlement against Tatitlek Support Services Inc. in the US District Court for the Central District of California, covering role players and similar positions at USMC Twentynine Palms and other sites between November 6 2004 and January 24 2011, described by plaintiffs' counsel as a $2.4 Million Class Action Settlement regarding Unpaid Overtime, Mis-classification and Other Wage and Hour Violations. Settlement checks issued January 27 2012. This is a labor misclassification matter, not federal-contracting fraud, and it is fourteen years old. Source is a plaintiffs' firm page, so partisan, and no court docket could be fetched.",
          "GAO bid protest B-416711 et al., decided November 28 2018. Tatitlek Technologies was the PROTESTER, not the accused, and the protest was denied.",
          "GAO's programmatic criticism of ANC 8(a) sole-source authority generally (GAO-06-399, GAO-16-113) does NOT name Tatitlek. It is a critique of the program and of SBA oversight, not of this company."
        ],
        "limits": "SAM.gov exclusions, PACER and SBA size-determination records could not be queried directly. Glassdoor and Indeed both returned HTTP 403, so there are no employee-reported allegations either way."
      },
      "residual_uncertainty_recorded": "What GeoNorth's 2018-era border-control work actually was remains unestablished. It does not appear in prime-award data for the period, which leaves a subcontract or an expired pre-2008 award as possibilities neither confirmed nor excluded. This does not reach the suppression bar and it is written down rather than dropped."
    },
    "notable_context": "Leadership is stable and named publicly (https://tatitlek.com/leadership/). Roy Totemoff has been CEO since 2006 and on the board since 1992. Dick Hobbs became President in July 2026 after joining the executive team in 2018, previously President and CEO of Afognak Native Corporation and Alutiiq LLC 2006-2014, a Naval Academy graduate with eight years in the Navy (Alaska Business Magazine, July 7 2026). Dean Clowers moved from President to COO in spring 2026. Mark Wamsher is VP of Business Development and is listed as the BD contact on every single subsidiary page, a real single-point-of-contact signal for the pipeline. Sheri Buretta, board Treasurer since 2005, is simultaneously a longtime Chugach Alaska Corporation figure, the connective tissue behind TCC and the Naswik hotel. Board Vice President Nanci Lee Robart is concurrently President of the Tatitlek Village IRA Council and is the liaison between TTC and the village. VERIFIED PUBLIC EMAIL ADDRESSES, all seen on fetched pages, none guessed: Shareholderservices@tatitlek.com, tatitlekland@tatitlek.com, mwamsher@tatitlek.com for Mark Wamsher VP Business Development with phone (256) 759-9349 on every subsidiary page, rtodd@tatitlek.com, rruggiero@tatitlek.com, rdulin@tatitlek.com, jhayes@tatitlek.com. NO published email exists for Hobbs, Totemoff, Clowers or any other executive on any page fetched. Cultural and timing notes: the Exxon Valdez ran aground on Bligh Reef just two miles away from the village in 1989, cutting subsistence activity by roughly 89 percent, and the 1994 formation of TCC with Chugach and Chenega was the direct response. The annual shareholders meeting runs in August in Anchorage. Their in-house software work is real but small, one remote Junior Software Developer at $95,000 building web-based environmental data management modules on ASP.NET and React for Navy environmental clients under Tatitlek Federal Services. They also carry an internal TTC Help Desk (888) 216-7228 and a shareholder portal at portal.tatitlek.com.",
    "confidence": "HIGH on what they do, the subsidiary map, contract vehicles, locations, leadership, the live job board and the contract awards pulled from the USAspending API. Every one of those was fetched, not snippet-read. MEDIUM on scale, because 1,300 employees and 46 locations are self-reported on their own site and no revenue figure is published anywhere reachable, including the Alaska Business Top 49ers list they are absent from. LOW on customer and employee sentiment, because Glassdoor and Indeed both blocked the fetch with HTTP 403 and no review text was quoted. The ICE flag was raised at MEDIUM-LOW by the analyst and has since been checked by the showrunner against roughly 270 primary award rows over 19 years, which found nothing; the residual uncertainty is recorded above."
  },
  "people": {
    "leaders": [
      {
        "name": "Roy Totemoff",
        "role": "CEO (listed under Board of Directors)",
        "source_url": "https://tatitlek.com/leadership/"
      },
      {
        "name": "Dick Hobbs",
        "role": "President (Executive Leadership, 2018 - Present)",
        "source_url": "https://tatitlek.com/leadership/"
      },
      {
        "name": "Dean Clowers",
        "role": "Chief Operating Officer (2015 - Present)",
        "source_url": "https://tatitlek.com/leadership/"
      },
      {
        "name": "Mark Wamsher",
        "role": "Vice President of Business Development (2016 - Present)",
        "source_url": "https://tatitlek.com/leadership/"
      },
      {
        "name": "Kristel Komakhuk",
        "role": "Chairman of the Board (2018 - Present)",
        "source_url": "https://tatitlek.com/leadership/"
      },
      {
        "name": "Patty Miller",
        "role": "Senior Vice President of Administration (2021 - Present)",
        "source_url": "https://tatitlek.com/leadership/"
      },
      {
        "name": "Nicole Christopherson",
        "role": "Senior Vice President of Finance (2009 - Present)",
        "source_url": "https://tatitlek.com/leadership/"
      },
      {
        "name": "Robert C. (Chris) Viramontes, P.E.",
        "role": "Vice President of Operations (2016 - Present)",
        "source_url": "https://tatitlek.com/leadership/"
      },
      {
        "name": "Paul Fondren",
        "role": "Vice President of Operations; General Manager, Tatitlek Technologies",
        "source_url": "https://tatitlek.com/tatitlek-technologies-llc/"
      }
    ],
    "best_contact": {
      "type": "email",
      "value": "mwamsher@tatitlek.com",
      "name": "Mark Wamsher",
      "role": "Vice President of Business Development",
      "source_url": "https://tatitlek.com/geonorth-information-systems-llc/",
      "corroborating_url": "https://tatitlek.com/tatitlek-technologies-llc/"
    },
    "rejected_contacts": [
      {
        "value": "info@tatitlek.com",
        "why": "asserted by a search engine summary, appears on NONE of the live pages fetched, traces to a stale legacy netsolhost.com site. Unverified, must not ship."
      },
      {
        "value": "support@tatitlek.com",
        "why": "real, on the privacy policy page, but it is a CCPA and privacy-inquiry inbox and outreach there is a misuse of a legal channel"
      },
      {
        "value": "Shareholderservices@tatitlek.com",
        "why": "real, on the resources page, but shareholders only and an ANC would rightly take a sales approach there badly"
      },
      {
        "value": "pfondren@tatitlek.com",
        "why": "real, but a subsidiary operating contact rather than the parent"
      }
    ],
    "decision_maker_note": "The leadership page splits Board from Executive Leadership. Roy Totemoff (CEO) sits under BOARD OF DIRECTORS with Chairman Kristel Komakhuk, while Dick Hobbs (President) heads EXECUTIVE LEADERSHIP. Hobbs and COO Dean Clowers run the operating business day to day. Neither has a published email anywhere on the site and none was constructed.",
    "constraint_flagged": "GeoNorth Information Systems is an in-house information-systems subsidiary, so the parent already holds IT capability. The engineering room must treat this as a real build-versus-buy constraint.",
    "fallback": "https://tatitlek.com/contact-us/ routes a categorised contact form including Business Development",
    "confidence": "high"
  },
  "competitors": {
    "competitors": [
      {
        "name": "Chugach Government Solutions (Chugach Alaska Corporation)",
        "note": "Anchorage. The ANCSA REGIONAL corporation for Prince William Sound, the same region Tatitlek village sits in, so this is the closest geographic and cultural peer in the field. Overlaps Tatitlek on five lines at once: Base Operations and Facilities, Training and Education, Supply Chain and Logistics, Construction, Professional Services, across Defense, Civilian, Intelligence, Space and International markets.",
        "ai_usage": "None found. Homepage and service-area content name C5ISR, Cybersecurity, Enterprise IT and Sustainment and System Integration as offerings, with no mention of artificial intelligence, machine learning, automation or digital transformation anywhere fetched. Treat as none found rather than proven absent, only the top-level site was checked.",
        "evidence_tier": "none found, bounded fetch",
        "source_url": "https://www.chugachgov.com/"
      },
      {
        "name": "Koniag Government Services (Koniag, Inc.)",
        "note": "Alaska Native regional corporation, Kodiak. About 750 employees, about $800M annual revenue, 280+ active contracts across 80+ federal organizations. Overlaps Tatitlek on professional and administrative support, IT and management services. The most AI-forward ANC found in this field by a wide margin.",
        "ai_usage": "SUBSTANTIATED, and independently corroborated by AWS. Built for the Office of the Deputy Assistant Secretary of the Army for Procurement: DORA (Determination of Responsibility Assistant), an automation bot on EC2 pulling SAM.gov compliance data that cuts vendor responsibility assessment from about one hour to 2 minutes; Jumpstarter document generators powered by Amazon Bedrock and LLMs that draft J and A justifications in minutes instead of hours and Performance Work Statements in minutes instead of days; contracting-regulation chatbots, compliance monitoring bots and more than 150 automated workflows. AWS states 687,000 hours saved annually and $37 million in annual cost avoidance, with a 2026 ACT-IAC Innovation Impact Award. Separately, their own May 27th, 2025 release names CASPER, an enterprise LLM platform in a secure AWS environment, org-wide prompt-engineering training, a new subsidiary Koniag AI Solutions, and claims a 75 percent reduction in contract requirements analysis time, a 50 percent reduction in human time for language determination over 10,000+ documents, and $29.3M in savings. The self-published metrics are unnamed-customer marketing; the AWS case study is the substantiated half.",
        "evidence_tier": "vendor case study with a NAMED customer (AWS + US Army), plus self-published marketing clearly separated",
        "source_url": "https://aws.amazon.com/solutions/case-studies/us-army-koniag-gov-services/",
        "corroborating_url": "https://www.koniag-gs.com/ai-investments-deliver-powerful-results-for-koniag-government-services-and-federal-customers/"
      },
      {
        "name": "ASRC Federal (Arctic Slope Regional Corporation)",
        "note": "ANC-owned, 9,000 employees. Overlaps Tatitlek on Professional Services, Supply Chain and Logistics, Infrastructure Operations and IT modernization, in Space, Civilian, Defense and Intelligence, National Security and Health.",
        "ai_usage": "SUBSTANTIATED, with three named federal deployments on a dedicated AI page. NOAA: their Advanced Analytics Platform (A2P) is the framework for NOAA's Financial Management Data System, using a commercially developed custom AI module and AI/ML to examine data from prior spending cycles to predict future spending needs, rolled out across the whole NOAA budget community (press release dated April 22nd, 2026). NOAA GOES-R: an AI/ML tool that identifies calibration issues in near real time flagging spacecraft health anomalies. USGS EROS: AI/ML solutions provide evapotranspiration predictions showing increased risk areas for famine. Also claims synthetic data generation for model training and a stated complementary human-machine approach. Named customers and named systems put this well past capability marketing.",
        "evidence_tier": "operator-reported with named federal customers and dated release",
        "source_url": "https://www.asrcfederal.com/ai/",
        "corroborating_url": "https://www.asrcfederal.com/asrc-federal-selected-by-noaa-to-provide-ai-enabled-financial-management/"
      },
      {
        "name": "Bering Straits Native Corporation (Bering Straits Professional Services, LLC)",
        "note": "ANC, Nome region, with Anchorage operations. SBA 8(a) certified, competes in the same small-business federal services lanes as Tatitlek across logistics, professional services and base support.",
        "ai_usage": "SUBSTANTIATED as active build, evidenced by hiring rather than by a case study. An open AI Software Engineer requisition in ANCHORAGE, Alaska, for Bering Straits Professional Services, names Azure OpenAI, OpenAI and Google Gemini, and describes designing, developing, and implementing AI-powered capabilities using Large Language Models (LLMs) across LogIT applications, developing and integrating conversational interfaces, copilots, and intelligent assistants into logistics and operational systems, building and maintaining retrieval-augmented generation (RAG) pipelines leveraging enterprise data sources, plus LLM observability and evaluation. A separate BSNC AI Automation Analyst listing names Microsoft Copilot Studio and Power Platform inside a secure GCC High environment. This is an Alaska-based competitor staffing production LLM work into a delivered contract system, not a brochure claim.",
        "evidence_tier": "operator-reported via its own job requisition",
        "source_url": "https://freehire.me/jobs/ai-software-engineer-bering-straits-native-corporation-a3gfljel"
      },
      {
        "name": "Akima, LLC (NANA Regional Corporation)",
        "note": "ANC-owned, Anchorage parent. Overlaps Tatitlek on installation logistics, facilities, IT, cybersecurity, construction and training. Holds the Missile Defense Agency SHIELD IDIQ.",
        "ai_usage": "CLAIMED, THINLY SUBSTANTIATED. Akima Emerging Technologies states it harnesses the power of artificial intelligence, machine learning, and robotic process automation to drive efficiency, and lists AI/ML, Intelligent Automation/RPA, Data Processing and Management, Business Intelligence and Modeling and Simulation as offerings. No named customer, contract or deployed system appears on that page. Subsidiaries Cloud Lake Technology and Compass Point Federal are named as the delivery arms, and the MDA SHIELD announcement says Akima companies will apply artificial intelligence and machine learning alongside digital engineering and MBSE, which is forward-looking scope language rather than evidence of a fielded system. Read this as capability marketing with a real contract vehicle behind it.",
        "evidence_tier": "vendor marketing with NO named customer",
        "source_url": "https://www.akima.com/opcos/aet/"
      },
      {
        "name": "Chenega Corporation",
        "note": "The closest structural analogue in the whole field. An Alaska Native VILLAGE corporation, Anchorage, from a Prince William Sound village, roughly 5,000 employees, four strategic business units. Overlaps Tatitlek directly: MIOS carries Training and eLearning, Language Analysis, Facilities Operation and Management and IT; EHF carries Base Operations and Maintenance and professional staffing; Professional Services carries Training Development. Same 8(a)/ANC sole-source lane, same customers. NOTE FOR THE SHOWRUNNER: chenega.com is already on this routine's suppression list, it appears here only as a competitor datapoint and is never a candidate.",
        "ai_usage": "MIXED. Substantiated as an internal operational tool, thin as a delivered capability. A hireEZ vendor case study quotes Matthew Keller, Senior Director of Talent Acquisition, using an AI sourcing platform, with claimed results of 10 percent reduction in time to hire, 50 percent less time spent sourcing, 30 percent higher response rate and 40 percent more qualified candidates sourced. Keller's quote is explicit about what the AI does: hireEZ's artificial intelligence piece is the most appealing because we can put in our search parameters and then walk away, while it aggregates profiles. That is a customer testimonial published by the vendor, not third-party audited. Separately, Chenega Professional and Technical Services supports FDA work on measuring data representation and diversity in AI-enabled devices and on mitigating algorithmic bias, which is AI-adjacent consulting rather than AI in their own delivery. Chenega's own strategic-business-unit pages mention no AI, ML or automation at all.",
        "evidence_tier": "vendor case study with a named customer; percentages NOT independently audited",
        "source_url": "https://hireez.com/resources/case-studies/chenega-case-study/"
      },
      {
        "name": "SOS International LLC (SOSi)",
        "note": "Conventional federal services contractor, not Alaskan, included because it is the direct competitor in Tatitlek's language-and-culture lane rather than a national giant in general. SOSi has led the federal language services market for 30+ years, has deployed thousands of cleared and uncleared linguists in 20+ countries with 200+ languages, and holds DoD, DOJ and DEA language contracts. That is the same buying center Tatitlek's 6,000-person role-player and foreign-language-speaker database serves.",
        "ai_usage": "SUBSTANTIATED by a capital commitment, which is stronger evidence than a webpage. SOSi's owners acquired a non-controlling equity interest in AppTek, LLC, an AI/ML firm in automatic speech recognition, machine translation and natural language understanding, and SOSi became the EXCLUSIVE RESELLER of AppTek products to U.S. federal, state and local government, with the two companies to jointly develop solutions for a variety of classified and unclassified use cases. CEO Julian Setian framed it as customer-driven: As our customers' appetites for A.I. driven solutions have increased, this is the latest of a series of investments we're making in market-leading commercial technologies. SOSi markets AI, neural machine translation, ASR and NLU across hundreds of language pairs in real time. Note the date, June 2020, so this is a six-year-old position that is now mature, not a new announcement.",
        "evidence_tier": "capital transaction, publicly announced",
        "source_url": "https://www.apptek.ai/news/sosi-invests-in-apptek-to-advance-artificial-intelligence-and-machine-learning-for-its-speech-recognition-and-translation-offerings"
      },
      {
        "name": "Valiant Integrated Services",
        "note": "Conventional contractor, about 5,000 employees, and the single most direct competitor for Tatitlek's core live-training and role-player work. Training, Simulation and Readiness portfolio covers joint and multinational exercises, wargaming, range operations and support, training analysis and exercise support, aviation and simulator instruction, and digital/managed learning. Holds the U.S. Army Korea Battle Simulation Center support work and a $118.5M PACAF simulator and academic instructor pilot contract.",
        "ai_usage": "None found. The training and readiness page lists Live Virtual Constructive (LVC) Training and Synthetic Training Integration as capabilities, which are simulation categories and not AI claims, and offers no elaboration. No mention of artificial intelligence, machine learning, adaptive learning or automated training anywhere on that page. The 60 years of immersive and simulation-based solutions framing is experience language. Marked none found on the page fetched, not proven absent company-wide.",
        "evidence_tier": "none found, bounded fetch",
        "source_url": "https://www.onevaliant.com/training-readiness"
      },
      {
        "name": "Alutiiq, LLC (Afognak Native Corporation)",
        "note": "ANC, Kodiak, 20+ subsidiaries. Overlaps Tatitlek closely on Facility Maintenance and Improvements, Industrial Health/Safety/Security, Professional and Business Management, Training and Program Support, and Engineering and Technical Services. Same 8(a) federal lane. NOTE FOR THE SHOWRUNNER: alutiiq.com and afognak.com are already on this routine's suppression list, they appear here only as a competitor datapoint.",
        "ai_usage": "AUTOMATION, NOT AI, and honest about it. A published Salesforce customer story documents a deployed bid-and-capture application on Salesforce Government Cloud using Sales Cloud to track opportunities, develop proposals and manage contract bids, with a 360-degree view of opportunities and real-time dashboards. Measured outcomes: deployed in two months, 100 percent user adoption within one year, user seats up 44 percent in the first six months. The case study names no Einstein or Agentforce and makes no AI claim; it lists automated status updates and automated internal and external communications as ROADMAP items, not shipped. So the correct read is a modern capture CRM in production with automation queued, and no AI.",
        "evidence_tier": "vendor case study with a named customer",
        "source_url": "https://www.salesforce.com/customer-success-stories/alutiiq/"
      }
    ],
    "target_markets_as_fetched": "Fetched from tatitlek.com, Tatitlek competes in four markets: (1) live and pre-deployment training support, role players, OPFOR, civilians-on-the-battlefield and language/culture instruction, run out of Tatitlek Training Services and Tatitlek Support Services, whose PRIMARY NAICS is 561320 Temporary Help Services and whose stated asset is a vetted database of over 6,000 role players and foreign-language speakers across Arabic, Pashto, Dari, Urdu, Kurdish, Farsi and more, delivered to the Marines at Twentynine Palms and the Army at Fort Bliss; (2) base operations support, facility O and M, engineering and construction, and environmental management; (3) professional and administrative support; (4) IT, information assurance and cyber, plus remote-sensing and geospatial production through GeoNorth Information Systems. Vehicles are OASIS+ 8(a) and Small Business, GSA STARS III, SeaPort NxG, ANC 8(a) sole source, ISO 9001:2015, 1,300 employees across Alaska and 46 worldwide locations.",
    "where_target_is_behind": "EXPOSURE ONE, A ZERO PUBLIC POSTURE WHILE NAMED PEERS PUBLISH MEASURED RESULTS. Five Tatitlek pages were fetched, the homepage, Our Company, Operations, Tatitlek Federal Services and GeoNorth, and not one contains the words artificial intelligence, machine learning, AI, data analytics or digital modernization. The strongest technology language in the entire group is GeoNorth's expertise in highly automated, global-scale, 2D/3D geospatial production for DoD and civilian applications, which is pipeline automation and reads as such. Against that, Koniag publishes an AWS-corroborated 687,000 hours and $37M annual cost avoidance for the Army with named tools, and ASRC Federal publishes three named federal AI deployments at NOAA, GOES-R and USGS EROS. Both are Alaska Native corporations selling into the same agencies on the same vehicles. A source-selection board or a partner comparing ANC capability statements today sees measured AI from two peers and silence from Tatitlek.\n\nEXPOSURE TWO, THE CAPTURE AND PROPOSAL MACHINE, WHERE TWO ANCs HAVE ALREADY MOVED IN DIFFERENT DIRECTIONS. Koniag's Bedrock-powered Jumpstarters draft Performance Work Statements in minutes rather than days and J and A justifications in minutes rather than hours, and DORA cuts a vendor responsibility determination from an hour to two minutes. Alutiiq, a much closer size and profile match to Tatitlek, put a bid-and-capture application on Salesforce Government Cloud live in two months and hit 100 percent adoption in a year. Both of those are the same back-office work Tatitlek must do to win and hold OASIS+ and STARS III task orders. Nothing public shows Tatitlek with either. Note the asymmetry that matters: Koniag SELLS its procurement AI to a federal customer, Alutiiq RUNS its CRM internally. Those are two distinct competitive threats and only one of them is visible in a capability statement.\n\nEXPOSURE THREE, THE LANGUAGE LANE IS BEING ATTACKED WITH CAPITAL, NOT WITH BROCHURES. SOSi took an equity position in AppTek and became the exclusive federal reseller of its ASR and machine translation, explicitly because customers' appetites for A.I. driven solutions have increased. SOSi sells cleared linguists and interpretation to DoD, DOJ and DEA, which is adjacent to and partly overlapping with Tatitlek's language-and-culture instruction and foreign-language role players. That position has been maturing since June 2020. Tatitlek's language offering, as published, rests entirely on the human database.\n\nEXPOSURE FOUR, THE OPERATING CONSTRAINT IS RECRUITING AND ONE COMPETITOR HAS PUBLICLY AUTOMATED IT. Tatitlek's primary NAICS is temporary help and the business is the ability to screen, security-vet, culturally vet and field bodies on a rotation calendar. Chenega, the nearest structural twin, an Alaska Native village corporation of about 5,000 people, has a published account of AI sourcing producing 10 percent faster time to hire, 50 percent less sourcing time and 40 percent more qualified candidates. Those numbers are vendor-published and not audited, so weight them accordingly, and the direction still matters because it is exactly Tatitlek's bottleneck.\n\nEXPOSURE FIVE, THE ALASKA TECHNICAL LABOR POOL. Bering Straits is recruiting an AI Software Engineer IN ANCHORAGE to build LLM copilots and RAG pipelines into LogIT logistics applications. That is the same small hiring pool Tatitlek draws from, and the competitor is bidding for it first.",
    "where_target_could_lead": "Stated strictly as observed white space in the field, with no build implied.\n\nONE, THE LIVE HUMAN TRAINING LANE IS UNCONTESTED BY AI AMONG THE PEOPLE WHO ACTUALLY COMPETE FOR IT, while the surrounding defense market moves publicly. Valiant, the most direct role-player and live-training competitor found, lists Live Virtual Constructive (LVC) Training and Synthetic Training Integration on its training page and makes no AI, ML or adaptive-learning claim anywhere on it. Chenega's MIOS lists Training and eLearning and Language Analysis with no AI language on its business-unit pages. Chugach lists Training and Education with no AI language. SOSi's AI is pointed at translation, transcription and localization, not at running live human role-player operations. Meanwhile the wider market is visibly moving, AI OpFor as an AI-controlled simulated adversary, EDF 2026 calls for AI-generated synthetic terrain and operation orders with automated after-action analysis, and generative platforms for tactical training of junior officers, all published, none of it owned by anyone in Tatitlek's actual competitive set. Nobody in this field has planted a flag between the human role-player business and that wave.\n\nTWO, NOBODY IN THE ANC SET PUBLISHES AI APPLIED TO A LARGE CONTINGENT LABOR POOL. Chenega's documented use is sourcing only, at the front of the funnel. Across all nine competitors fetched, no one claims AI applied to vetting, clearance tracking, language-proficiency assessment, rotation scheduling or surge fill for a standing pool of thousands. Tatitlek's 6,000-person screened and culturally vetted database is the largest such published asset in this field and it is proprietary data, which is the one thing competitors cannot copy off a website.\n\nTHREE, GEOSPATIAL AI IS OPEN GROUND INSIDE THIS SPECIFIC FIELD. GeoNorth already runs high-performance and cloud geospatial production for DoD and intelligence customers in agriculture, defense, energy, maritime and natural resources, which is precisely the domain where ML is now mainstream across the broader defense market. Among the competitors fetched, ASRC Federal's AI sits in space operations and financial forecasting, Koniag's sits in procurement, Akima's is unnamed, and no one in the set claims ANC-owned geospatial AI. Tatitlek is the only one of the nine holding that particular asset.\n\nFOUR, THERE IS NO VEHICLE BARRIER. Tatitlek already holds OASIS+ 8(a) and Small Business, GSA STARS III, SeaPort NxG and ANC 8(a) sole-source authority, which are the same instruments Koniag and Akima route AI-flavoured work through. Whatever the gap is, it isn't contractual access.\n\nFIVE, THE HONEST COUNTERWEIGHT. Two of the nine, Chugach and Valiant, show nothing, and Alutiiq is explicit that its automation is roadmap rather than shipped. So the field is not uniformly ahead. The split is clean and worth saying plainly: the IT-and-professional-services ANCs (Koniag, ASRC Federal, Bering Straits, Akima) have moved, and the facilities-and-live-training houses (Chugach, Valiant, Alutiiq, Chenega's delivery side) have not. Tatitlek straddles both halves, so it is simultaneously behind in one of its markets and standing in open ground in another.",
    "confidence": "HIGH on market definition and on competitor identity. Tatitlek's four markets, subsidiaries, vehicles, headcount and primary NAICS 561320 were read off tatitlek.com and a HigherGov awardee profile. All nine competitors were verified from their own or a partner's live pages, and each was selected for a named overlap with a specific Tatitlek line rather than for size.\n\nHIGH on the POSITIVE AI findings. Koniag is corroborated by AWS with named tools and figures, which is the strongest evidence in the set; ASRC Federal names three federal customers and systems on its own AI page plus a dated April 22nd, 2026 NOAA release; SOSi's AppTek equity stake and exclusive federal reseller arrangement is a capital fact; Bering Straits' Anchorage LLM/RAG requisition quotes the responsibilities verbatim; Alutiiq's Salesforce deployment is a vendor-published customer story with metrics. Chenega's recruiting metrics are HIGH that the tool is in use and LOW that the percentages are audited, since hireEZ published them from its own customer's quotes. Akima's AI is explicitly graded as capability marketing, its own page names no deployment.\n\nMEDIUM, AND DELIBERATELY SO, ON EVERY NONE FOUND. Chugach, Valiant, Olgoonik and Doyon were checked at homepage, capability-page and search level only, not across every subsidiary site, careers board, capability statement PDF, SAM.gov entry or trade-press archive. Absence of evidence in a bounded fetch is not evidence of absence, and any of them could hold an unpublished internal tool. The same caveat applies to Tatitlek's own zero posture, five pages showed nothing, which establishes that nothing is PUBLIC, not that nothing exists.\n\nLOW on Tatitlek's revenue split across its four markets. HigherGov's contract tables rendered as No Results and Calculating on the fetch, so the relative dollar weight of training support versus base operations versus IT is NOT established from a primary contract database, and the ordering above is inferred from capability pages and known role-player placements at Twentynine Palms and Fort Bliss. A USAspending or SAM.gov pull would firm that up and is the obvious next verification step.\n\nNot checked, and worth naming as a known hole: Doyon Government Group and Olgoonik got only a single search pass each, no primary page was fetched for either, so neither is reported as a competitor above. Tatitlek Technologies, Tatitlek Government Services, Tatitlek Management Services, Tatitlek Professional Services and Tatitlek Universal Services were not individually fetched, so a stray AI mention on one of those pages would soften Exposure One."
  },
  "industry": {
    "industry": "Federal government services contracting at the small-to-mid prime and subcontractor scale (professional/technical services, IT, security and facilities, military training and range support), plus the back office that carries it: capture and proposal production, past-performance and capability documentation, contract compliance, recruiting for contract ramps, and timekeeping/invoicing against federal contracts.",
    "in_production": [
      {
        "who": "K Corp, described in the case study as a 100 percent Native-owned, Alaska-based government contractor with a lean BD team",
        "what_ai": "GovDash, an AI proposal and capture platform purpose-built for GovCon. Used for RFP analysis and first-draft generation from a company content library, with the writer editing rather than starting blank.",
        "outcome": "TIER: vendor_case_study (named customer, vendor-published). 60 percent reduction in proposal preparation time, monthly proposal submissions up from 2 to 6 (3x), zero new hires to absorb the increase. Named operator quoted: Cheyanne Richard, Technical Writer for Business Development, 'Without GovDash, there's no way we could put out the number of proposals we do.' Published March 25th, 2025. NOTE: this is the closest structural match in the entire evidence base to an Alaska Native corporation's federal services subsidiary, and it is still a vendor-published number with no independent audit of the baseline.",
        "source_url": "https://www.govdash.com/blog/how-k-corp-3x-d-proposal-output-using-govdash",
        "reliability": "vendor_claim"
      },
      {
        "who": "SPATHE Systems, an 8(a) and SDVOSB federal contractor in Tampa FL, founded 2014, IT/cyber/software/infrastructure support services, with ONE proposal manager",
        "what_ai": "GovDash, adopted September 2024, across RFP analysis, key-personnel qualification matching, and proposal generation. Human review retained (the claim is a Red Team-ready draft in 24 hours, not a submission-ready one).",
        "outcome": "TIER: vendor_case_study (named customer and named executive). Draft turnaround from 2.5-3 weeks to 24 hours (about 90 percent). Monthly RFP submissions from 2 to 7-8 (4x) without new proposal staff. Quoted: Darren Williams, VP Solution Development, 'GovDash has become a force multiplier for SPATHE Systems.' Published July 30th, 2025. The case study itself notes results depended on team adoption and AI-literacy training, not on the tool alone.",
        "source_url": "https://www.govdash.com/blog/from-3-weeks-to-24-hours-how-spathe-systems-4x-d-rfp-output-with-govdash",
        "reliability": "vendor_claim"
      },
      {
        "who": "Sumaria Systems, defense engineering services contractor founded 1982, nationwide, DoD and national security customers",
        "what_ai": "GovDash, piloted December 2024 then expanded across the growth team. Two distinct jobs: (1) technical RFI response drafting with SMEs validating, (2) bulk resume reformatting into a standard proposal format.",
        "outcome": "TIER: vendor_case_study (named customer, two named executives). A 13-page technical RFI that historically took up to 2.5 weeks was submitted in 3 days, with the first draft in roughly 90 minutes and SME review inside 24 hours. Nearly 400 resumes standardized, conversion time down from hours to about 10 minutes each. Quoted: Donna Kerstis, Senior Proposal Manager, and Michelle Nixon, Chief Growth Officer ('It has unified company documents and processes, and that was an unforeseen benefit'). Published January 3rd, 2026. The resume-standardization result is the most transferable item here for a multi-subsidiary staffing-heavy contractor.",
        "source_url": "https://www.govdash.com/blog/how-sumaria-systems-reduced-rfi-response-time-by-80-percent-with-govdash",
        "reliability": "vendor_claim"
      },
      {
        "who": "The Brite Group, federal IT and data solutions firm in Washington DC serving DoD, DHS and law enforcement, with a TWO-PERSON BD team",
        "what_ai": "GovDash Word Assistant, drafting RFI and RFP responses off a past-performance corpus.",
        "outcome": "TIER: vendor_case_study (named customer and principal). 50 percent of initial proposal drafts produced automatically; a 2-person team absorbing a larger RFI/RFP load; a stated target of 30 percent less manual rework by year end (a TARGET, not a measured result, and it is presented as one). Quoted: Suraj Sharma, Principal. Published May 16th, 2025.",
        "source_url": "https://www.govdash.com/blog/how-the-brite-group-cut-proposal-drafting-time-by-50-with-govdash",
        "reliability": "vendor_claim"
      },
      {
        "who": "Additional named GovDash customers listed on the vendor's customer-stories index (Total Systems Technologies, PowerTrain, OneZero Solutions, AQE Solutions, Schatz Strategy Group, Cape Fox FCG, Endurion, Aurex, JANUS)",
        "what_ai": "Same platform, spread across capture/pipeline, proposal drafting, and color-team review.",
        "outcome": "TIER: vendor_case_study headlines (customers named, numbers un-detailed on the index page). Total Systems Technologies doubles RFI volume; PowerTrain increased proposal efficiency by 3x; OneZero Solutions cut time to Pink Team drafts by 50 percent; Schatz Strategy Group saved $75K per year; Cape Fox FCG listed under increase BD output (AI agents). Cape Fox FCG is an Alaska Native corporation subsidiary, which makes it the second ANC-shaped name in this dataset, BUT the underlying case study page could not be retrieved, so treat it as a listing and nothing more. NOTE FOR THE SHOWRUNNER: capefoxcorp.com is on this routine's suppression list, it appears here only as an industry datapoint. The cluster matters more than any single entry: this is roughly a dozen named small-to-mid GovCons reporting the same direction of result on the same job.",
        "source_url": "https://www.govdash.com/customer-stories",
        "reliability": "vendor_claim"
      },
      {
        "who": "An unnamed SDVOSB cybersecurity firm in Washington DC (GovDash customer)",
        "what_ai": "GovDash for full proposal development, displacing outside proposal consultants.",
        "outcome": "TIER: vendor_marketing (no named customer). Estimated $50,000 saved per proposal cycle, 50 percent shorter proposal timelines, 2x annual proposal output. The vendor does not publish the calculation behind the $50K. The mechanism named is reduced reliance on external consultants, which is a real and checkable line item for any GovCon, so the mechanism is more useful than the number. Published March 26th, 2025.",
        "source_url": "https://www.govdash.com/blog/how-a-cybersecurity-company-saved-50k-per-proposal-cycle-with-govdash",
        "reliability": "vendor_claim"
      },
      {
        "who": "An unnamed mid-sized government contractor (Procurement Sciences 'Awarded' customer)",
        "what_ai": "Awarded AI for RFP analysis, resume evaluation and proposal drafting.",
        "outcome": "TIER: vendor_marketing (customer not named, quote anonymous). Two contract wins under tight deadlines; the only quote is an anonymous team member on resumes: 'I will never go back to reviewing resumes by hand.' Published February 3rd, 2025. Included deliberately as the contrast case: same claimed capability as the GovDash set, one tier weaker in evidence because nobody is named.",
        "source_url": "https://www.procurementsciences.com/case-studies/case-study-mid-sized-govcon-secures-two-wins-with-awarded-ai",
        "reliability": "vendor_claim"
      },
      {
        "who": "US Army PEO Enterprise and Army Contracting Command (Aberdeen Proving Ground, Detroit Arsenal, Rock Island)",
        "what_ai": "SBIR-funded AI prototypes that assemble Acquisition Requirement Packages, the requirements documents that precede a solicitation. Three prototypes funded September 2024; testing at the three contracting centers began January 2026 under the Smart Contracting Initiative.",
        "outcome": "TIER: operator_reported, government-published. ARP development time reduced from weeks to hours, or, in some cases, minutes. PEO Enterprise used one prototype in FY2025 to produce TWO ACTUAL SUPPLY-TYPE CONTRACT AWARDS, which is a production outcome rather than a pilot metric. Two more AI source-selection tools anticipated in FY2026. This is the buyer moving, and it changes the tempo a bidder has to match.",
        "source_url": "https://www.army.mil/article/290573/army_ai_prototypes_speed_up_acquisition_enable_faster_capability_delivery",
        "reliability": "proven"
      },
      {
        "who": "Army Contracting Command, Rock Island Arsenal and ACC G6 Huntsville (Army MAX)",
        "what_ai": "Army MAX (Marketplace, Automation and eXecution), an AI-assisted services acquisition platform that validates requirements, flags missing documentation, builds solicitation packages and posts notices to SAM.gov.",
        "outcome": "TIER: operator_reported (Army announcement, trade-press write-up). Pilot announced August 6th, 2026; officials named (Ben Graw, contract specialist, Strategic Competitions and Innovations Branch). IMPORTANT CAVEAT: the Army has stated a design intent of shorter services-contracting timelines but has published NO quantified time saving for Army MAX. The widely repeated months to days figure is an aspiration in the coverage, not a measurement. Relevant to Tatitlek because services acquisition is exactly the lane its subsidiaries bid in.",
        "source_url": "https://www.executivegov.com/articles/army-max-ai-assisted-service-acquisition",
        "reliability": "proven"
      },
      {
        "who": "Federal agencies generally (11 agencies with published AI inventories, DoD exempt)",
        "what_ai": "Generative AI across mission support, including written communications and information access.",
        "outcome": "TIER: independent_measurement (GAO, report GAO-25-107653, July 29th, 2025). Total reported AI use cases nearly doubled from 571 in 2023 to 1,110 in 2024. Generative AI use cases rose about ninefold, 32 to 282. GAO also records the drag: officials at 10 of 12 agencies cited existing federal policy as a potential obstacle, alongside data-privacy compliance and insufficient technical budget. This is the only genuinely independent measurement found anywhere in this industry's AI story, and it measures the CUSTOMER, not the contractor.",
        "source_url": "https://www.gao.gov/products/gao-25-107653",
        "reliability": "proven"
      },
      {
        "who": "US Army source selection at White Sands Missile Range, and TRAX International (the protester) versus Southwest Range Services (the awardee)",
        "what_ai": "AI tooling used inside the Army's proposal evaluation for a roughly $450 million mission support services contract.",
        "outcome": "TIER: independent (litigation record reported by Nextgov/FCW, August 2026). TRAX alleges the AI hallucinated multiple times, producing a weakness against TRAX with made-up references to TRAX's proposal, that no one on the Source Selection Evaluation Board checked. The Army conceded one identified weakness is not supported by the record. The Army's records to GAO did not explain whether assigned strengths for the Southwest Range Services bid came from a human or an AI tool. GAO denied the initial protest in May 2026; TRAX filed in the Court of Federal Claims in late July 2026; price delta $29.4 million. THIS IS RANGE SUPPORT SERVICES, the exact segment Tatitlek works in. It is the single most segment-specific AI fact available and it is about the buyer's AI, not the bidder's.",
        "source_url": "https://www.nextgov.com/acquisition/2026/08/contractor-alleges-army-inappropriately-used-ai-make-450m-contract-award/415225/",
        "reliability": "proven"
      },
      {
        "who": "Booz Allen Hamilton (large prime, used here only as a directional operator report)",
        "what_ai": "AI applied internally to recruiting, specifically matching job descriptions against technical requirements and security clearance levels.",
        "outcome": "TIER: operator_reported, NO MEASUREMENT. Leadership described a lot of work last fiscal year in automating a lot of those processes and getting much better at matching algorithms. CFO Matt Calderone framed revenue-per-employee gains as a future expectation. No metric, no date, no named tool was given to investors. Reported July 2025. Included precisely because it is the honest state of the cleared-recruiting category: the biggest firm in the space is doing it and has published nothing measurable.",
        "source_url": "https://www.washingtontechnology.com/companies/2025/07/booz-allens-ai-blueprint-customers-and-company-itself/406992/",
        "reliability": "vendor_claim"
      },
      {
        "who": "Unanet (ERP used by GovCons for DCAA-compliant timekeeping, billing and project accounting), 4,200+ clients",
        "what_ai": "ChampAI, OpportuneAI (opportunity identification), ProposalAI (proposal generation), Wyatt agentic framework, AP/AR automation, vendor invoice automation. Announced December 9th, 2025.",
        "outcome": "TIER: vendor_marketing (NO named customers, NO quantified outcomes in the release). Fetched specifically to test the back-office pocket and it came back empty of measurement. Claims are directional only (accelerating cash flow, saving business development teams hours each week). The 20 percent cash-flow / 66 percent DSO figures circulating in search results do not appear in this release and could not be sourced to a fetched page, so they should not be repeated.",
        "source_url": "https://www.prnewswire.com/news-releases/unanets-product-innovations-advance-intelligence-and-automation-for-govcon-and-aec-firms-302635959.html",
        "reliability": "vendor_claim"
      },
      {
        "who": "Deltek (the dominant GovCon software vendor), on its own AI opportunity-and-proposal tooling",
        "what_ai": "AI-generated proposal outlines, RFP requirement extraction, Shipley color-team workflow support.",
        "outcome": "TIER: vendor_marketing with nothing in it. Fetched expecting customer numbers and found NONE: no named customers, no measured outcomes, no Clarity statistics, only feature description and 30,000 organizations trust Deltek. Worth knowing before a sales call: the largest vendor in this market publishes weaker customer evidence on its AI than a Series B startup does.",
        "source_url": "https://www.deltek.com/en/blog/govcon-ai-opportunity-proposal-tools",
        "reliability": "vendor_claim"
      }
    ],
    "state_of_play": "CATEGORIES WORKED (so the reader knows what was and was not searched): capture and opportunity discovery; proposal production and RFP shredding; past-performance, resume and knowledge reuse; contract compliance (FAR overhaul, CMMC/CUI, the new GSA AI clause); cleared recruiting and staffing for contract ramps; timekeeping, invoicing, AP/AR and DCAA accounting; service delivery on contract (IT service desk, facilities and O and M predictive maintenance, security guard operations, military training and range support); the government buyer's own AI; and the legal/protest risk layer. Nine categories, and they are not equally populated.\n\nADOPTION IS NOT THE QUESTION ANYMORE. The 17th annual Deltek GovCon Clarity study surveyed 917 government contractors in January 2026 and found 90 percent using AI in some capacity, up from 45 percent the prior year, with 92 percent using generative AI specifically. Whatever a contractor decides, it is not deciding early. The same study found only 5 percent describe their AI capability as fully developed, only about 25 percent report mature governance, and 45 percent say they are unclear on the ROI. That is a vendor-published survey and should be read as one, but its sample is large and its findings cut against the vendor's interest, which is the tell that it is worth citing.\n\nWHERE THE GROUND IS ACTUALLY SOLID: ONE POCKET, AND IT IS NARROW AND DEEP. Every measured win found in a business shaped like a Tatitlek subsidiary sits in PRE-AWARD DOCUMENT PRODUCTION, and specifically in getting a compliant FIRST DRAFT out of an existing corpus of past performance, resumes and boilerplate. Four named companies with named executives on the record report the same shape of result within about eighteen months of each other. SPATHE Systems (8(a)/SDVOSB, one proposal manager) went from 2.5-3 weeks to 24 hours on draft turnaround and from 2 to 7-8 monthly RFP submissions. K Corp (Native-owned, Alaska-based) reports 60 percent less proposal prep time and 2 to 6 submissions a month with no new hires. Sumaria Systems took a 13-page technical RFI from 2.5 weeks to 3 days and reformatted nearly 400 resumes from hours each to about ten minutes each. The Brite Group's two-person BD team gets 50 percent of first drafts automatically. Add the index-page entries and this is roughly a dozen named small-to-mid GovCons pointing the same direction on the same job. Every one of these is a vendor_case_study, published by GovDash. Not one is independently audited, none discloses the baseline measurement method, and the selection is obviously favourable. That is the honest ceiling on this evidence. It is also the strongest evidence base in the industry, and a dozen named customers with named executives is real information.\n\nNOTE THE SHAPE OF THE CLAIM, because it is unusually consistent and unusually modest. Not one of these operators claims a higher win RATE. They claim THROUGHPUT: more bids submitted, from the same people, in less elapsed time, with a human still doing review and SME validation. SPATHE's is explicitly a Red Team-ready draft, not a submission. Sumaria's SMEs still validate before submission. That is a claim about a bottleneck being moved, and it is far more credible than a win-rate claim would be. Deltek's survey supplies the matching baseline: an average of 84 hours per proposal, and 83 percent of contractors missed opportunities in 2025 because they found them late.\n\nTHE BUYER IS MOVING TOO, AND FASTER THAN MOST CONTRACTORS REALIZE. GAO (independent) recorded federal generative-AI use cases rising about ninefold from 32 to 282 across eleven agencies between 2023 and 2024. The Army has AI prototypes assembling Acquisition Requirement Packages in hours instead of weeks, tested at Aberdeen, Detroit Arsenal and Rock Island since January 2026, and PEO Enterprise already used one to produce two real contract awards in FY2025. Army MAX, announced August 6th, 2026, drafts services solicitations and posts them to SAM.gov. For a services contractor this is the point: solicitation cadence on the buyer's side is accelerating while proposal capacity on the bidder's side is still the same humans.\n\nWHAT YOU CAN BUY TODAY, WITH REAL PRICING SIGNAL. GovCon-native proposal AI is almost entirely demo-gated. Sweetspot's pricing page publishes no price at all, only a demo booking; a fetched market comparison lists GovDash, Inventive AI, Arphie, Ombud, QorusDocs, SteerLab and Tribble as contact sales with no published starting price, against generic RFP tools that do publish ($49 to $899 a month, with AutogenAI estimated at $30K+ a year). Adjacent GovCon data tools DO publish: Deltek GovWin IQ averages around $29,000 a year (enterprise to $119,000), HigherGov starts at $500 a year for one seat with tiers at $2,500 and $5,000, GovTribe federal-only runs roughly $100 to $300 a month. Practical read: budget a five-figure annual commitment for a GovCon-native proposal platform, expect to negotiate blind, and know that the opportunity-discovery layer is cheap and transparently priced while the drafting layer is not.\n\nTWO PROCUREMENT FACTS THAT DECIDE WHICH TOOLS ARE EVEN ELIGIBLE. GovSignals announced FedRAMP High authorization for a proposal AI on November 24th, 2025, and Procurement Sciences achieved FedRAMP Moderate on March 13th, 2026. If any part of the corpus a tool touches is CUI, the authorization boundary is the first filter, not the feature list, and it eliminates most of the market before a demo.",
    "the_gap": "WHERE IT IS WORKING VERSUS WHERE A CONTRACTOR THIS SIZE WOULD EXPECT IT TO, in four gaps.\n\nGAP 1, THE BIG ONE. The measured wins are ALL in PRE-AWARD BACK OFFICE, not in delivery on contract. Tatitlek's revenue comes from delivering IT, security, facilities and range support. Nothing in the delivery categories produced a named operator with a measured outcome. Federal IT service desk AI returned generic ITSM deflection benchmarks with no federal contractor named; facilities and O and M predictive maintenance figures trace to a single vendor content operation with no named customer at all, and should not be repeated as fact; security guard workforce AI returned vendor blogs and one anecdote with no fetchable source page; military training and range support has real and large 2026 awards (Booz Allen's $696.7M Army MCTP award among them) but those are contracts to DELIVER training, not evidence of AI making an incumbent's range support cheaper. If someone pitches AI into the delivery line of a federal services contract, there is currently no measured public precedent to lean on, and the CDRL, CUI and government-furnished-environment constraints are why. That is a genuine gap, not a thin search.\n\nGAP 2. THE CLEARED RECRUITING POCKET LOOKS RIPE AND IS EVIDENCE-EMPTY. For a 1,300-person, many-location contractor that ramps staff against contract awards, recruiting feels like the obvious AI target. Booz Allen, the largest firm in the market, told investors it is doing exactly this (matching job descriptions to technical requirements and clearance levels) and published NO metric, NO date and NO tool name. The circulating numbers in this category (35-45 percent faster hires, a named-but-obscure contractor screening 2,000 resumes in 48 hours) trace to staffing-agency marketing pages that could not be verified by fetching, and they should be treated as vendor_marketing. Notably, the one adjacent result that IS documented by a named customer is Sumaria's RESUME STANDARDIZATION, which is a proposal-production job, not a recruiting job. The evidence points at formatting resumes for bids, not at sourcing people.\n\nGAP 3. THE COMPLIANCE AND ACCOUNTING BACK OFFICE IS THE OPPOSITE OF WHAT THE MARKETING SAYS. Deltek's Clarity study finds contractors averaging dozens of audits a year and 96 percent expecting compliance costs to stay elevated or rise, and the Revolutionary FAR Overhaul (first proposed rules June 23rd, 2026, over 1,100 pages) is rewriting the rulebook underneath everyone. That is a screaming demand signal. The supply side has no measured deliveries against it. Unanet's own December 2025 AI product release names no customer and quantifies nothing. Deltek's AI proposal page names no customer and quantifies nothing. The CMMC-AI tools publish prices (FutureFeed at $99/month plus $168/month for Level 2 add-ons for firms under 25 employees, Vanta-class platforms at $12,000-$25,000 a year) but not outcomes. Highest demand, thinnest evidence, in the category where a wrong answer is most expensive.\n\nGAP 4, AND THE ONE TO READ TWICE. THE MOST CONSEQUENTIAL AI IN THIS INDUSTRY RIGHT NOW IS THE GOVERNMENT'S, NOT THE CONTRACTOR'S, AND IT HAS ALREADY MISFIRED IN TATITLEK'S OWN SEGMENT. In the White Sands Missile Range mission support competition, TRAX alleges the Army's AI hallucinated a weakness into its proposal with made-up references that nobody on the source selection board checked, on a roughly $450 million award with a $29.4 million price delta. The Army conceded one weakness is unsupported by the record and could not tell GAO whether the awardee's strengths came from a human or a tool. GAO denied the protest in May 2026; it is now in the Court of Federal Claims. The practical implication for a bidder is unglamorous and actionable: proposals are increasingly being READ by machines, so traceability, explicit requirement mapping and unambiguous cross-referencing are now a scoring variable, and debrief records are worth scrutinizing for AI provenance.\n\nAND THE COMPLIANCE TRAP ON THE OTHER SIDE. GSA posted an AI-specific acquisition rule to the Federal Register on June 17th, 2026 (comments closed August 3rd, 2026), applying to government-wide vehicles including the Federal Supply Schedule and OASIS+. It splits contractors into four roles (LLM developer, service provider, systems integrator, system operator), and would require disclosure of every LLM used in contract performance within 120 days of commencing work, identification of every entity filling each role, and 72-hour incident notification for LLM-related events touching government data. An earlier GSA proposal drew contractor alarm over irrevocable government use rights, data segregation, and a bar on AI components controlled by non-US entities. Read together with the CUI rule (do not put CUI in a tool that is not FedRAMP authorized at the right level; a CUI incident can reach contract termination or debarment), the honest conclusion is that a GovCon's AI decision is a COMPLIANCE decision wearing a productivity decision's clothes, and the disclosure obligation means the tool choice has to be defensible on paper before it ever has to be defensible on ROI.",
    "grounding_facts": [
      {
        "fact": "17th annual Deltek GovCon Clarity study, 917 government contractors surveyed in January 2026, published May 13th, 2026: 90 percent of government contractors now use AI in some capacity, up from 45 percent the year prior, and 92 percent report using generative AI tools.",
        "source_url": "https://www.govconwire.com/articles/clarity-report-2026-deltek-govcon-kevin-plexico",
        "reliability": "vendor"
      },
      {
        "fact": "Same Deltek Clarity study: only 5 percent describe AI capability as fully developed, most are still piloting (37 percent) or scaling (38 percent), just 25 percent report mature governance structures, and 45 percent say they are unclear on the ROI of leveraging AI.",
        "source_url": "https://www.deltek.com/company/news/latest-deltek-clarity-industry-studies-highlight-ai-challenges/",
        "reliability": "vendor"
      },
      {
        "fact": "Same study, the operational baseline a proposal-AI business case would be measured against: average proposal development runs 84 hours per proposal, and 83 percent of contractors missed opportunities in 2025 because they discovered them late.",
        "source_url": "https://www.govconwire.com/articles/clarity-report-2026-deltek-govcon-kevin-plexico",
        "reliability": "vendor"
      },
      {
        "fact": "Same study, the financial pressure behind the AI push: contractors averaged 15 percent revenue growth in 2025 and expect 16 percent in 2026, while profit margins fell from 20 percent to 17 percent, and nearly nine in ten firms saw at least one financial metric decline. Top AI concerns were data privacy and security risk (37 percent) and inaccurate AI-generated forecasts (34 percent).",
        "source_url": "https://www.govconwire.com/articles/clarity-report-2026-deltek-govcon-kevin-plexico",
        "reliability": "vendor"
      },
      {
        "fact": "Same study: 96 percent of contractors expect compliance costs to remain elevated or increase in the coming year, and firms average dozens of audits annually across financial, cybersecurity and contract domains.",
        "source_url": "https://www.deltek.com/resources/articles/deltek-clarity-govcon-five-contracting-trends/",
        "reliability": "vendor"
      },
      {
        "fact": "GAO-25-107653, published July 29th, 2025: across 11 federal agencies with published AI inventories (DoD exempt), total reported AI use cases nearly doubled from 571 in 2023 to 1,110 in 2024, while generative AI use cases rose roughly ninefold from 32 to 282. Officials at 10 of 12 agencies cited existing federal policy as a potential obstacle to adoption.",
        "source_url": "https://www.gao.gov/products/gao-25-107653",
        "reliability": "authoritative"
      },
      {
        "fact": "US Army: three SBIR-funded AI prototypes for Acquisition Requirement Packages, funded September 2024, reduce ARP development from weeks to hours, or, in some cases, minutes. PEO Enterprise used one in FY2025 to produce two supply-type contract awards. Testing at Army Contracting Command Aberdeen Proving Ground, Detroit Arsenal and Rock Island began January 2026 under the Smart Contracting Initiative; two more AI source-selection tools anticipated in FY2026.",
        "source_url": "https://www.army.mil/article/290573/army_ai_prototypes_speed_up_acquisition_enable_faster_capability_delivery",
        "reliability": "authoritative"
      },
      {
        "fact": "Army MAX (Marketplace, Automation and eXecution), announced August 6th, 2026, is an AI-assisted services acquisition platform built by ACC-Rock Island Arsenal and ACC G6 Huntsville that validates requirements, identifies missing documentation, supports solicitation package development and posts notices to SAM.gov. No quantified time saving has been published by the Army; the widely repeated months to days figure is stated intent, not measurement.",
        "source_url": "https://www.executivegov.com/articles/army-max-ai-assisted-service-acquisition",
        "reliability": "authoritative"
      },
      {
        "fact": "TRAX International alleges in the US Court of Federal Claims (filed late July 2026) that the Army's AI evaluation tooling hallucinated multiple times during source selection for roughly $450 million in mission support services at White Sands Missile Range, producing a classic AI hallucination, with made-up references to TRAX's proposal, that no one on the Source Selection Evaluation Board checked. The Army conceded one assigned weakness is not supported by the record; its records to GAO did not explain whether the awardee's strengths came from a human or an AI tool. GAO denied the initial protest in May 2026. Price delta between bids: $29.4 million.",
        "source_url": "https://www.nextgov.com/acquisition/2026/08/contractor-alleges-army-inappropriately-used-ai-make-450m-contract-award/415225/",
        "reliability": "authoritative"
      },
      {
        "fact": "GSA posted an AI-specific acquisition rule to the Federal Register on June 17th, 2026 (listening session July 14th, comments closed August 3rd, 2026), applying to GSA government-wide vehicles including the Federal Supply Schedule and OASIS+. It defines four contractor roles (LLM developer, LLM service provider, LLM systems integrator, LLM system operator) and would require disclosure of all LLMs used within 120 days of commencing work, identification of every entity filling each role, and notification within 72 hours of discovering an LLM-related incident involving government data.",
        "source_url": "https://www.washingtontechnology.com/contracts/2026/06/gsa-unveils-new-ai-specific-acquisition-rule/414351/",
        "reliability": "authoritative"
      },
      {
        "fact": "An earlier GSA AI procurement proposal (comments due March 20th, 2026) would have applied to MAS contractors and broadly defined Service Providers including subcontractors, requiring an irrevocable government license to use AI systems for any lawful purpose, disclosure within 30 days of award of all AI systems used in performance, logical segregation of government data from other customers' data with no use for training models for others, and a bar on AI components manufactured, developed or controlled by non-US entities.",
        "source_url": "https://www.gibsondunn.com/gsa-ai-procurement-rules-would-introduce-new-disclosure-and-use-rights-requirements-for-federal-contractors/",
        "reliability": "authoritative"
      },
      {
        "fact": "FedRAMP status is the eligibility filter for any AI tool touching CUI in this market. GovSignals announced FedRAMP High authorization for a defense-contractor proposal AI on November 24th, 2025 (its only named customer reference, Loft Federal, carries a testimonial and no metric). Procurement Sciences achieved FedRAMP Moderate on March 13th, 2026 and is listed on the FedRAMP Marketplace.",
        "source_url": "https://www.prnewswire.com/news-releases/procurement-sciences-achieves-fedramp-moderate-authorization-302713703.html",
        "reliability": "vendor"
      },
      {
        "fact": "Pricing signal, GovCon-native proposal AI is demo-gated. Sweetspot's own pricing page publishes no price and routes to a 30-minute demo; its customer logos (Oshkosh Defense, Strider Technologies, OWT Global, Crayon, Vantiq, The Saratoga Group) carry no quantified outcome, and its only outcome testimonial is from an unnamed Senior Executive at a $2B+ Federal IT Contractor.",
        "source_url": "https://www.sweetspot.so/pricing/",
        "reliability": "vendor"
      },
      {
        "fact": "Pricing signal, comparative. GovDash, Inventive AI, ContraVault AI, Arphie, SiftHub, SteerLab, Ombud, QorusDocs and Tribble all publish no starting price. Generic (non-GovCon) RFP tools do: Proposify $49/month, PandaDoc $65/month, DeepRFP $89/user/month, Bidara $299/month, RFP360 $500/month, AutoRFP.ai $899/month, with Loopio about $1,200/month, Responsive about $1,160/month, Qvidian about $2,000/month and AutogenAI about $30K+/year as estimates.",
        "source_url": "https://www.bidara.ai/comparison/ai-proposal-software",
        "reliability": "vendor"
      },
      {
        "fact": "Pricing signal, the opportunity-discovery layer, which IS transparently priced. Deltek GovWin IQ averages around $29,000 annually with enterprise packages to $119,000; HigherGov starts at $500/year for a single user with Standard at $2,500 and Leader at $5,000; GovTribe federal-only plans run roughly $100 to $300 per month, federal plus SLED from about $1,800/year.",
        "source_url": "https://www.sweetspot.so/blog/govcon-ai-tools-small-business-federal-contractors/",
        "reliability": "vendor"
      },
      {
        "fact": "Proposal-profession adoption benchmark, cited secondhand: the Loopio/APMP RFP Trends and Benchmarks report (seventh annual, 2026) found 79 percent of proposal teams used generative AI in 2025, up from 34 percent in 2023. Loopio's own page returned empty and its Businesswire release returned 403, so this is a SECONDARY citation from a fetched industry-report page and should be attributed that way, not repeated as a direct Loopio/APMP citation.",
        "source_url": "https://proposalconnect.io/annual-govcon-industry-report-2026",
        "reliability": "vendor"
      },
      {
        "fact": "GSA's own chief AI officer, Zach Whitman, on federal AI ROI in May 2026: The big issue that we're facing is how do we calculate ROI, with questions about AI's effectiveness, utility, efficiency gains and service-delivery impact remaining very open, though we know something is there. The same report notes only 6 percent of executives in a Deloitte survey of 1,850 global leaders could measure an AI use case's ROI within one year of deployment.",
        "source_url": "https://fedscoop.com/gsa-ai-roi-usai-platform-adoption/",
        "reliability": "authoritative"
      },
      {
        "fact": "Negative finding, recorded because it qualifies the vendor tier. Deltek's own AI opportunity-and-proposal page, fetched in full, contains no named customers, no measured outcomes and no Clarity statistics about AI results, only feature description and the claim that 30,000 organizations trust Deltek. Unanet's December 9th, 2025 AI product release likewise names no customer and quantifies no outcome. The two largest GovCon software vendors publish weaker AI customer evidence than the venture-backed newcomers do.",
        "source_url": "https://www.deltek.com/en/blog/govcon-ai-opportunity-proposal-tools",
        "reliability": "vendor"
      },
      {
        "fact": "Negative finding, the opportunity-discovery claims are unattributed. GovDash's own AI-agent pipeline page presents 250 to 500 recovered analyst hours annually per BD FTE and $36,000 to $92,000 in recovered labor annually per BD analyst as industry figures with NO named customer behind them, in contrast to its proposal-drafting case studies which do name customers. Treat the pipeline-discovery numbers as vendor_marketing and the drafting numbers as vendor_case_study; they are not the same tier even from the same vendor.",
        "source_url": "https://www.govdash.com/blog/ai-agents-government-contract-opportunity-discovery",
        "reliability": "vendor"
      }
    ],
    "confidence": "MEDIUM-HIGH on where the ground is solid, MEDIUM on how solid it is, HIGH on where it is empty.\n\nHigh confidence that pre-award document production (RFP shred to compliant first draft, resume and past-performance reformatting, RFI turnaround) is the one pocket in this industry with repeated, named, dated, same-direction results in companies of Tatitlek's shape, including two Alaska Native-owned names (K Corp, and Cape Fox FCG as a customer listing only). High confidence that the claim being made is THROUGHPUT and not win rate, and that human review is retained in every named case.\n\nMedium confidence on the magnitude. The entire named-customer cluster comes from ONE vendor's published case studies, and the strongest single corroborating survey (917 contractors) is also published by a vendor. No independent audit of any contractor-side number exists that could be found. The 60 percent, 90 percent and 3x figures should be quoted as what named operators reported to their vendor, never as established fact, and the honest planning assumption is materially below the case-study headline.\n\nHigh confidence, and the most valuable half, on the empty categories. Nine categories were worked. Delivery-side AI (federal IT service desk, facilities and O and M, security guard operations, training and range support) produced NO named operator with a measured outcome, only vendor content marketing, reported as a real gap rather than a thin search. Cleared recruiting produced one unmeasured operator statement from Booz Allen and nothing else verifiable. Compliance and DCAA accounting produced the loudest demand signal and the thinnest evidence in the whole study.\n\nHigh confidence on the buyer-side and regulatory facts, which are the best-sourced items here (GAO, army.mil, the Court of Federal Claims record via Nextgov, the Federal Register posting). The TRAX/Southwest Range Services matter is the single most segment-specific AI fact available for a range-support contractor and it is authoritative.\n\nTwo verification failures to be transparent about: Federal News Network and Businesswire both returned 403 and their content is NOT relied on here, and the Integrity Management Consulting 60-percent-win-rate claim and the AGS Pro underbilling-recovery anecdote both appeared in search results but are excluded entirely because no source page could be fetched for either."
  },
  "_meta": {
    "company": "The Tatitlek Corporation",
    "domain": "tatitlek.com",
    "date": "2026-09-19",
    "segment": "Alaska Native corporations and tribal enterprises",
    "place": "Anchorage, Alaska"
  }
}
```
