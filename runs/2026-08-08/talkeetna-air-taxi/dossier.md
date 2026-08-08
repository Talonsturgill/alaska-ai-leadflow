# Talkeetna Air Taxi, internal dossier, 2026-08-08

PRIVATE. Prospect data lives here and never in the public repo.

## THE PICK

Talkeetna Air Taxi, talkeetnaair.com, Talkeetna, Alaska. Tourism and visitor
industry. Fit total 24, the highest of 23 page-verified candidates across four
segments.

The day came back with a **24-24 tie** against The Kuskokwim Corporation, and
both were scored 5 on reachability and 5 on offer_fit, so the first two
tie-breaks did not separate them. The showrunner re-fetched both companies' own
sites before committing the room. talkeetnaair.com/team-tat/ renders and names
its decision-makers. kuskokwim.com returns an EMPTY BODY, and so does its
subsidiary tumeq.com, so every fact about Kuskokwim traced to a page other
people wrote about them. Reachability under the ICP is whether we can VERIFY a
real decision-maker, and one of the two could be verified against its own pages.
Kuskokwim is not disqualified and sits first on the replacement queue.

Full reasoning and the ranked replacement queue in selection.md.

## THE ROOMS

Research room: company-analyst, people-finder, competitor-analyst,
industry-analyst in parallel, then fact-checker. 64 verified claims, in
claims.json, which is the only thing anything downstream cited.

The fact-checker found a **drift pattern** and it shaped the rest of the run.
Seven rejections all leaned the same way, toward making this operator look more
primitive and more troubled than its own fetched pages support. A paraphrase had
been tightened into a quotation. An office-hours contradiction was pinned on the
wrong page. A TripAdvisor complaints theme was written up as a pain with a
source_url pointing at a page that had returned 403. A fatal crash that killed
five people was attributed to a competitor with HIGH confidence on the strength
of sources that would not load.

Ten hard guardrails came out of that and are recorded at the top of claims.json.
The most important: the August 4 2018 Thunder Mountain crash may not appear
anywhere in any direction, because no page attributing it to any operator could
be opened.

Discovery room: product-strategist mapped 14 areas of the business before any
build was chosen, then ai-feasibility-engineer audited all five candidates.

## WHAT THE CONSCIENCE DID, AND IT CUT BOTH WAYS

1. **Killed the guest-facing assistant**, then inverted the reason into the most
   valuable sentence we hand them. FareHarbor Agent is not just a reason not to
   buy from us. If their own booking vendor's assistant starts answering "is it
   flying today" in their name, the vendor will have automated the one decision
   their reputation rests on keeping human, in a channel they do not control,
   under a refund policy they pay for.
2. **Killed a model the strategist had smuggled into a different build.** The
   expedition desk put an LLM parse on the inbound form. Seven of that form's
   eight verified fields are already structured.
3. **Corrected the pick's own spec three times**, including turning a
   per-tour-block status back into a current-hour status, because a status set
   on a future block is a forecast published under their name.
4. **Inverted the cost-of-error direction.** Under an unconditional 100 percent
   refund, a false Flying creates no new refund liability. A stale Holding
   manufactures one, plus a seat that can no longer be sold.

## THE LOCKED PICK

The Facts Spine first, then the Conditions Board, shipped as one thing.
**Phase one contains no AI at all.** Roughly 4.5 person-weeks.

## THE ECONOMICS, AND THE HONEST PROBLEM WITH THEM

There is NO measured baseline. No verified call volume, no passenger volume, no
share of the 981 registered 2026 Denali climbers. So the case is built as a
BREAK-EVEN rather than a projection.

Computed in roi_math.py, never narrated:

| | Conservative | Most likely | Aggressive |
|---|---|---|---|
| Five year cost | $45,240 | $40,946 | $38,123 |
| Five year benefit | $20,027 | $54,648 | $138,138 |
| Recovered | 44% | 133% | 362% |
| Payback | never | month 45 | month 19 |
| Counter minutes recovered | 2% | 11% | 47% |

Break-even sits between 0.50 and 0.75 retained seats per staffed day, about one
seat every other staffed day.

The full 24,000 dollar phase one's conservative case DOES NOT clear. The ask is
therefore staged, 9,500 for the record and 14,500 for the page, with the page
released only by their own counted week. The study says outright that we have
not modelled a return on the 9,500 and will not pretend to one.

The counter-minutes row is printed precisely because it argues against us. Staff
time recovered never covers this build at any believable volume, which is the
direct rebuttal of the vendor formula this industry is sold.

## THE CRITIC LOOPS

**study-critic: three rounds.** Round 1 returned fix with twelve failures. The
largest was mechanical and real, the five-year totals could not be rebuilt from
the drivers the footer published, because training and the 4.5-year run accrual
were missing. Round 2 returned fix with four blockers, including that the gate
was stated in a unit the counted week cannot produce. Round 3 returned fix on a
single string, an unsourced "40 to 60 miles" in the demo sitting two inches above
a slot saying the distance was unmeasured.

Round 2's most useful observation: after the round 1 fixes the surviving lean had
REVERSED, and now pointed toward flattering us rather than them. Round 3
confirmed it closed, and that what remains runs against our own case.

**lead-critic: three rounds.** Round 1 rejected on two real grounds. The email
carried "one phone line", which the study-critic had already made us cut as
unverified, and stripped of that phrase its opening fact fitted K2 or Sheldon
equally well. Round 2 fixed the opening with the four-operator concession, then
OVERRULED ITS OWN round 1 flag about naming the company, on the evidence that
Talon adds the name by hand on four consecutive sends.

## THE CONTACT

info@talkeetnaair.com, DECODED from Cloudflare email-protection obfuscation on
three of the company's own pages. Not a fallback. Their team page publishes no
individual staff addresses at all, so this is the address the company itself
publishes as the way to reach its named leaders.

courtney@talkeetnaair.com was surfaced by an aggregator with the local part
masked. REJECTED and never used.

## WHAT WE COULD NOT VERIFY, AND SAID SO

Call volume. Passenger volume. Their share of the 981 climbers. Which FAA camera
sites see the routes they fly. What runs behind their counter for climbers and
charters. Their safety management system posture. Any review content at all,
because TripAdvisor and Yelp both returned 403.

Every one of those is a question to ask on the call, and not one was inferred
into a number.
