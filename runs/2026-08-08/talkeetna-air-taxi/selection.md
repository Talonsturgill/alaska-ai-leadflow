# Phase 1 selection, 2026-08-08

Four lead-scouts ran in parallel, one per ICP segment. 23 candidates came back
page-verified, 17 of them clean after the values screen and the exclude-set check.
`ledger.py check` was run over all 17 and every one returned clear, so dedupe is
computed rather than eyeballed. The shortlist gate (3 clean candidates) passed with
room, so no fifth scout was spawned.

## THE PICK

**Talkeetna Air Taxi**, talkeetnaair.com, Talkeetna (Denali / Alaska Range),
tourism and visitor industry. Fit total **24**.

Scored 5 / 4 / 5 / 5 / 5 on ai_solvable_pain, ability_to_pay, reachability,
offer_fit, alaska_signal.

## THE TIE, AND HOW IT BROKE

The day came back with a **24-24 tie** between Talkeetna Air Taxi and The Kuskokwim
Corporation, and both were scored 5 on reachability and 5 on offer_fit, so
tie-breaks (a) and (b) did not separate them on their face.

The showrunner re-fetched both companies' own sites before committing the room,
because the Kuskokwim scout had flagged a caveat that goes to exactly the criterion
the first tie-break names.

- `https://www.talkeetnaair.com/team-tat/` renders and names its decision-makers on
  the company's own page. Paul Roderick, Operations Director since 1996. Courtney
  Shaffer, General Manager since 2017. Twenty-two named staff with start years.
  Email addresses are present but Cloudflare-obfuscated, so an address is likely
  reachable and is not yet confirmed. That is people-finder's job in Phase 2.
- `https://www.kuskokwim.com/` returns an **empty body**. So does tumeq.com. Both
  are JS-rendered and neither serves content to a fetcher. Every fact the scout
  returned about Kuskokwim traces to a third-party page, and the CEO name with it.

That is the tie-break. Reachability under the ICP is whether we can VERIFY a real
decision-maker and a real contact, and one of these two companies can be verified
against its own pages and the other cannot. It also runs straight into the Phase 2
RESEARCH GATE, which requires the company be confirmed from at least two
independent pages, and into the whole premise of the deliverable. A Field Study
that says we did the homework on YOU, sourced entirely to profiles other people
wrote about you, is a weaker piece of work whatever its fit score says.

Kuskokwim is not disqualified. It is first on the replacement queue, and a future
run should try a rendered fetch or work through the subsidiary sites.

## WHY IT IS A GOOD PICK ON THE MERITS

Mid-August is the last full month of the visitor season and Talkeetna Air Taxi is
a weather-driven operation, so the exact thing the ICP calls a repeating expensive
pain is at its annual peak right now. The staff page shows unusually long tenure
for a seasonal industry, several people fifteen and twenty years in, which is a
fact worth understanding rather than assuming. No conclusion is being handed to
any room, see the ANCHORING LAW. The rooms get claims.json and map the whole
business themselves.

## REPLACEMENT QUEUE (ranked, use in this order if a gate disqualifies the lead)

| # | Company | Domain | Segment | Fit |
|---|---|---|---|---|
| 1 | The Kuskokwim Corporation | kuskokwim.com | ANC | 24 |
| 2 | Craig Taylor Equipment | craigtaylorequipment.com | other | 23 |
| 3 | Alyeska Title Guaranty Agency, Inc. | alyeskatitle.com | other | 23 |
| 4 | Advanced Physical Therapy | aptak.com | healthcare | 23 |
| 5 | Old Harbor Native Corporation | oldharbornativecorp.com | ANC | 23 |
| 6 | Solstice Alaska Consulting, Inc. | solsticeak.com | other | 22 |
| 7 | Major Marine Tours | majormarine.com | tourism | 22 |
| 8 | Alaska Premier Dental Group | smilealaska.com | healthcare | 22 |
| 9 | Gana-A'Yoo, Limited | ganaayoo.com | ANC | 22 |
| 10 | Alaska Logistics LLC | alaskalogistics.net | other | 21 |
| 11 | Cook Inlet Region, Inc. (CIRI) | ciri.com | ANC | 21 |
| 12 | Four Corners Dental Group | fourcornersdentalgroup.com | healthcare | 20 |
| 13 | Aspen Hotels of Alaska | aspenhotelsak.com | tourism | 20 |
| 14 | Alaska Village Electric Cooperative | avec.org | other | 20 |
| 15 | UNIT Company | unitcompany.com | other | 19 |
| 16 | Northern Alaska Tour Company | northernalaska.com | tourism | 19 |
| 17 | Alaska Home Care | alaskahomecare.com | healthcare | 19 |
| 18 | Sealaska | sealaska.com | ANC | 19 |
| 19 | Whaler's Cove Lodge | whalerscovelodge.com | tourism | 18 |
| 20 | Ophthalmic Associates | akeyedoc.com | healthcare | 18 |
| 21 | Alaskan Home Health, Inc. | alaskanhomehealth.com | healthcare | 18 |

Names the scouts surfaced but could not page-verify, worth a retry on a later run
rather than a suppression: Alaska Urology (alaskaurology.com, 403 then 503),
Trinion Quality Care Services (trinionqcs.com, 503), Olgoonik Corporation
(olgoonik.com, 403, and its values screen came back CLEAN), Stan Stephens Cruises
(stephenscruises.com, fleet page 403), Premier Alaska Tours (premieralaskatours.com,
verified but sells only to cruise lines and wholesalers).

## DROPPED AT PHASE 1, AND WHY

**Alaska Coach Tours** (alaskacoachtours.com, fit 20) was dropped by the showrunner,
not by the scout, which flagged it for a decision. Their own page states the company
is owned by Na-Dena', a joint venture of Doyon, Limited and Huna Totem Corporation.
doyon.com is suppressed for operations, transportation and food services at the
800-bed El Paso Service Processing Center. The Afognak precedent already holds that
the subsidiary rule runs upward as well as downward, and a joint venture a
suppressed parent co-owns is the same relationship. Not pursued, and not separately
suppressed, because the parent record already covers it.

**Alaskan Dream Cruises** was dropped by the tourism scout as the Allen family's
sister company to Allen Marine Tours, which is already in leads. Different domain,
the same people.

Six ANC names were dropped by the values screen and RECORDED AS SUPPRESSIONS this
run, with sources, so no future scout spends the search again: Chenega Corporation,
The Aleut Corporation, Arctic Slope Regional Corporation, Sitnasuak Native
Corporation, Shee Atika Incorporated, and Central Council Tlingit and Haida Indian
Tribes of Alaska. Two of those carry a note for a human. The ASRC suppression is
THINNER than the others, firing on CBP technology support with no detention
operations found, and is flagged for Talon to reverse if he judges that materially
different. The CCTHITA suppression is by the upward parent rule alone, with no
independent conduct finding against the tribal government itself.

Suppressions went from 13 to 19 on this run.
