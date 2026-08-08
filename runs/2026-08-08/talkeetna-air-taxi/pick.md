# THE LOCKED PICK, 2026-08-08, Talkeetna Air Taxi

## THE BUILD

**The Facts Spine first, then the Conditions Board, shipped as one thing.**

Phase one contains **NO AI AT ALL**. That is a finding, not a hedge, and it is
the ai-feasibility-engineer's recommended pick after auditing all five
candidates.

- **The Facts Spine.** One structured source of truth for the facts customers
  ask about, hours, fares, the glacier add-on, the park fee, the gear allowance
  and overweight rate, the base camp fee, the two tax lines, passenger minimums
  and the check-in window. Every page renders from it. Three pages currently
  publish three different staffed-hours answers.
- **The Conditions Board.** One mobile page on their own domain, served at the
  /denali-webcam/ path that currently 301s to the homepage. Public FAA weather
  camera imagery, current observations and the NWS forecast, side by side and
  auto-refreshing, with one CURRENT status field the counter flips, stamped with
  a clock time and auto-expiring to their own existing FAQ sentence.

Roughly 4.5 person-weeks combined.

## HOW THE FEASIBILITY AUDIT CHANGED IT

The conscience cut in both directions, which is the point of having one.

1. **It killed the guest-facing assistant outright**, and then inverted the
   reason into something worth more than the build was. FareHarbor Agent is not
   just a reason for them not to buy that from us. It is a RISK TO THEM. If their
   own booking vendor's assistant starts answering "is it flying today" in their
   name, the vendor will have automated the one decision their reputation rests
   on keeping human, in a channel they do not control, under a refund policy they
   pay for.
2. **It killed a model the strategist had smuggled into a different build.** The
   expedition desk placed an LLM parse on the inbound form. Seven of that form's
   eight verified fields are already structured. Version one is tier one, no
   model, and the estimate falls with it.
3. **It corrected the status field from a forecast back into a status.** "One
   field flipped per tour block" set hours ahead is a forward-looking statement
   published on their own domain. Current status only.
4. **It inverted the cost-of-error direction.** Under an unconditional 100
   percent refund, a false Flying creates no new refund liability. A stale
   Holding manufactures one, plus a seat that can no longer be sold.
5. **It found the geography exposure nobody had named.** A camera in the
   Talkeetna valley reports the valley. The tours are about a mountain 40 to 60
   miles away.
6. **It re-gated the AI phase on the right variable.** The strategist gated the
   copilot on contact volume. Volume decides whether it is WORTH it. The corpus
   and a season-captured eval set decide whether it WORKS, and only those are
   blockers.

## CAGAN'S FOUR RISKS, CHECKED BEFORE LOCKING

- **Feasibility.** The engineer walked it. Tier one on the ladder, clears, with
  six binding conditions recorded in feasibility.json. Two are genuine unknowns
  that must be checked before the estimate hardens, FAA camera coverage on the
  actual routes, and hosting or DNS access for the path recovery.
- **Value.** The top-scoring opportunity at 15 on the Ulwick scale, and the only
  one where three separately verified facts converge rather than one inferred
  pain. Their own FAQ manufactures the contact this removes.
- **Usability.** A mobile page and one field. The weak point is honestly named,
  the status field is an eleventh duty on the one person the build exists to
  unload, so its acceptance bar is that flipping it costs less time than the
  single call it deflects.
- **Business viability for THIS owner.** An operator with ten aircraft, 21 named
  people, one of four federal Denali glacier landing concessions, tours at $275
  to $547 and expedition drops to $1,200 a person can afford four and a half
  person-weeks. Adoption is the real risk and it is mitigated by the imagery
  half needing no human input at all. Nothing here touches a regulated function,
  so there is no certification path to clear before they can use it.

Viability holds. The pick is locked.

## ECONOMICS PRE-CHECK, AND THE HONEST PROBLEM WITH IT

**The ask is sized here at a fixed-price phase one in the low five figures, for
roughly 4.5 person-weeks, plus a small annual run cost.** The roi-analyst builds
the case for THAT ask and no larger one.

The honest difficulty has to be stated plainly rather than modelled around.
**There is no verified figure anywhere in this package for how many calls this
would deflect.** No call volume, no flightseeing volume, no share of the 981
registered 2026 Denali climbers. The feasibility audit went further and ruled
that no return may be modelled on the human status field at all, because its
deflection is negatively correlated with need.

So a conventional benefit stack would be invented, and inventing one is exactly
what this routine exists not to do.

**The ask therefore clears its bar in the shape the method already allows, a
phase one whose honest return is decision data plus one verifiable defect
fixed.** Two things carry it:

- The Facts Spine repairs a defect that is already verified. Three pages publish
  three different answers to one question today. That does not need a volume
  estimate to be worth fixing.
- The Conditions Board's case is stated as a BREAK-EVEN, not a projection. The
  study prints the number of deflected contacts per staffed day at which phase
  one pays for itself, computed in code, so the owner can hold it against one
  week of tally marks and decide for himself which side of the line he is on.

That is a more honest instrument than a benefit stack and it is also a better
one, because it hands him a test rather than a claim.

**The free action comes first and costs a notepad.** The 2026 season is open
until September 15, about five weeks out. One week of tally marks at the desk
now produces the 2026 baseline, makes a genuine before and after possible for
2027, and starts the question capture the copilot's eval set later depends on.
If that tally comes back small, the study says plainly that phase one is not
worth buying, and we would rather say that than sell it.

## WHAT PHASE ONE DELIBERATELY GIVES UP

The highest-ticket revenue line is untouched for a season, and this is the least
impressive thing we could have proposed. Both accepted on purpose. The
expedition desk and the counter copilot ride the Next lane, and the safety
management system question, the seasonal onboarding angle and the weather-day
seat recovery hypothesis ride Later, so nothing the opportunity map found is
wasted.
