# Selection, 2026-08-10

## The pick

**Major Marine Tours** (majormarine.com), Seward, Alaska.
Segment: Tourism and visitor industry. **Fit total 24 of 25.**

Scores: ai_solvable_pain 5, ability_to_pay 4, reachability 5, offer_fit 5, alaska_signal 5.

### Why it won

Highest total across 23 page-verified candidates from four ICP segments, and the
only candidate in the whole field scoring 5 on reachability, offer_fit and
alaska_signal at once.

It tied at 24 with Huna Totem Corporation. **The tie broke on the contract's first
tie-breaker, reachability**, 5 against 4. Major Marine publishes a full leadership
roster with titles and a business email on its own site. Huna Totem publishes a
general address and named executives across two domains, which is good but a step
further from a decision-maker.

Two further things separated them, neither of which was needed to decide it.
Huna Totem's HunaTek arm carries a published "National Security" service line that
the scout flagged as an unresolved residual against this desk's immigration-
enforcement suppression rule, which would have cost a research pass to clear.
Major Marine's reputation screen came back clean, with Adventure Green Alaska
certification since 2017 and Whale SENSE participation.

### What the scouts verified about it

Two independent structural facts, both published by the company itself, both about
how the business actually runs rather than anything on its website.

1. Sixty seasonal employees in Seward, hired in a window that closes in April.
   "During our cruise season we employ about 60 seasonal employees in Seward. Our
   peak hiring time for seasonal positions is January 15th - April 15th."
   https://majormarine.com/employment/
2. Three different refund clocks running at once against that annually-rebuilt
   crew. 72 hours for cruise only, 7 days for cruise-and-hotel packages, 21 days
   for packages carrying motorcoach or rail, with one free reschedule and a $15
   per person fee after that, plus captain-initiated re-routes that trigger
   partial refunds.
   https://majormarine.com/refund-policy/

Contact evidence: info@majormarine.com, published on both
https://majormarine.com/meet-the-team/ and https://majormarine.com/employment/.
Named leadership: Tom Tougas (Owner), Colby Lawrence (VP), Kori Goertz (Director
of Sales), Kirsten McNeil (Director of Shoreside Operations), Tayja Wright
(Operations Manager). No personal address for Tougas was seen anywhere and none
was invented.

Dedupe: `ledger.py check majormarine.com` returned clear. All 23 candidates were
checked in code, all clear.

## The replacement queue, in order

When a later gate disqualifies the lead, take the next name here. Re-scout
under-covered segments only when this runs dry.

| # | Total | Company | Domain | Segment | Note |
|---|---|---|---|---|---|
| 1 | 24 | Huna Totem Corporation | hunatotem.com | ANC | Clear the HunaTek "National Security" line first |
| 2 | 23 | Chena Hot Springs Resort | chenahotsprings.com | Tourism | Owner on record that hiring is "impossible"; do not build the case on staff treatment |
| 3 | 23 | Gastineau Guiding Company | stepintoalaska.com | Tourism | Published 7 AM to 7 PM phone window, ~80 seasonal guides |
| 4 | 23 | Beacon Occupational Health | beaconohss.com | Healthcare | BBB D- for not answering 2 complaints; no named leader verified |
| 5 | 22 | Alaska Logistics LLC | alaskalogistics.net | Paperwork | 2021 KYUK frozen-barge reporting, USCG investigated; no published email |
| 6 | 21 | Anchorage Veterinary Clinic | anchoragevetclinic.com | Healthcare | Outside HIPAA entirely; says it is "fully staffed", so no labor wedge |
| 7 | 21 | Aspen Hotels of Alaska | aspenhotelsak.com | Tourism | Do not repeat their "Alaska-owned" line, HQ address is Lake Mary FL |
| 8 | 21 | Gana-A'Yoo, Limited | ganaayoo.com | ANC | Nine companies on one Anchorage back office |
| 9 | 21 | Choggiung Limited | choggiung.com | ANC | 15 corporate staff; brushes BBNC via minority stake in Bristol Industries |
| 10 | 21 | Alaska Sleep Clinic | alaskasleep.com | Healthcare | Ten-document intake packet, four fax lines, no published email |
| 11 | 20 | Midnight Sun Animal Hospital | midnightsunanimalhospital.com | Healthcare | BBB B-; grief-handling complaints, read before writing |
| 12 | 20 | LCG Lantech, Inc. | lcgak.com | Paperwork | Four platting authorities, published info@ address |
| 13 | 20 | Advanced Physical Therapy of Alaska | aptak.com | Healthcare | Employee-owned, pays for documentation time; no published email |
| 14 | 20 | Rust's Flying Service | flyrusts.com | Tourism | 2018 K2 Aviation crash killed five; never touch flight safety as a use case |
| 15 | 20 | The Kuskokwim Corporation | kuskokwim.com | ANC | Site does not render to a fetcher, no contact verifiable |
| 16 | 20 | Altman, Rogers & Co. | altrogco.com | Paperwork | Audit independence limits the offer; no named human readable |
| 17 | 19 | NORTECH, Inc. | nortechengr.com | Paperwork | Do not cite the 24-employee figure, it is broker data |
| 18 | 19 | Salmon Berry Travel & Tours | salmonberrytours.com | Tourism | Pain is inferred, not published |
| 19 | 18 | Ounalashka Corporation | ounalashka.com | ANC | Cleanest reputation in the ANC set, smallest pain |
| 20 | 18 | Conrad-Houston Insurance | conradhouston-insurance.com | Paperwork | Confirm canonical domain vs chialaska.com before any ledger write |
| 21 | 18 | PND Engineers, Inc. | pndengineers.com | Paperwork | Best ability to pay, thinnest published pain |
| 22 | 18 | Old Harbor Native Corporation | oldharbornativecorp.com | ANC | Unresolved DHS/CBP proximity flag, clear before any outreach |

## Segment coverage note

Tourism is already the heaviest segment in the ledger, 8 of 21 leads. That did not
influence the pick, because the contract ranks on fit total and the first
tie-breaker settled it before segment history was ever reached. Worth watching,
though: if tourism keeps winning on reachability alone, the ICP is measuring how
well a company publishes its staff page as much as how well it fits.


## CORRECTION, made at Phase 2 (2026-08-10)

The Phase 1 scout described Major Marine as operating from "Seward and Whittier".
**That is wrong and the company-analyst caught it.** Every current page on
majormarine.com is Seward-only: the homepage, the all-cruises index, all six tour
pages and the tour sitemap. The all-cruises page states verbatim "We offer
multiple cruise options departing from the beautiful harbor town of Seward,
Alaska", and the site's full internal link inventory contains no Whittier page.
The competitor-analyst independently reached the same conclusion.

A legacy TripAdvisor entity titled "Major Marine Tours - Prince William Sound
Glacier Cruise, Whittier, AK" still exists, which is almost certainly where the
scout picked it up, and it returned HTTP 403 so neither agent could check it for a
closed flag. No company statement resolving when or whether the Whittier product
ended was found.

TREAT MAJOR MARINE AS A SEWARD-ONLY OPERATOR. Whittier and Prince William Sound
must not appear in the study, the demo or the email. The honest framing if it ever
comes up is that we could find no current Seward-page reference to a Whittier
departure, not that they stopped running one.

This is worth recording as a process note. The error entered through a scout brief
that asserted a location, and it travelled two phases before a researcher who
actually fetched the product pages caught it. A location is a fact like any other
and it should have carried a URL from the start.
