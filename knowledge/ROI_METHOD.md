# ROI Method, the honest business case

The roi-analyst owns this. A skeptical owner or CFO sees through optimism instantly,
so the ROI section wins trust by being conservative and auditable, not by being big.
Never present a raw or single-number ROI. Present a risk-adjusted range with stated,
calibrated assumptions.

## The four-part frame (not just cost vs benefit)

Model the investment across four parts, the shape of Forrester's Total Economic
Impact, used for over twenty years. Benefits, Costs, Flexibility (the option value
of future capability), and Risk. Apply a risk-adjustment to every benefit and cost
line, haircut benefits that may not fully land, pad costs that may overrun, then
report a risk-adjusted range. https://www.forrester.com/policies/tei/

## The cost side, total cost of ownership, not sticker price

Model over a five-year horizon (Gartner TCO). A defensible AI cost stack,
- Build or subscription cost.
- Implementation and integration, usually the biggest and most underestimated line.
- Training and change management, state the hours, never "included."
- Ongoing run cost, and for AI specifically, inference and token cost, monitoring,
  evaluation, human-in-the-loop review, and model refresh.
- A contingency reserve of 15 to 20 percent, because most failures come from
  organizational factors, scope creep, thin training, no owner, not from the
  software. https://www.gartner.com/en/information-technology/glossary/total-cost-of-ownership-tco

## The benefit side, quantify only what converts, and label which kind it is

The most important honesty move, distinguish capacity created from cash saved.
Automating a task creates real capacity, but it only becomes dollars if you can
defer a hire, avoid a backfill, or redeploy the person to higher-value work. Say
which situation this is. Every benefit line is computed from the company's own
baseline, never vendor or industry averages.

- Labor time saved equals hours saved per task times task volume times the
  fully-loaded hourly cost, converted to cash only through the redeploy or defer or
  avoid test above.
- Error and rework reduction equals cost per error times volume times a modeled
  percent reduction.
- Revenue or throughput lift, capacity gained without new headcount, kept separate
  from actual cost reduction.
- Qualitative benefits (morale, brand, employee experience) go in a separate
  labeled section, NOT in the ROI formula. Owners respect honesty about what is
  hard to quantify.

Cap the benefit stack at about five lines. A case is only as strong as its weakest
benefit, and stacking outliers adds skepticism, not value.

## The verdict, phased, as a range

- Report payback period and, where it helps, a multi-year view, but always as a
  range.
- Phase the benefit curve. Year one is partial, bake in about a ninety-day
  stabilization ramp. Year two is full run-rate. Year three compounds. Assuming
  day-one full benefit is the most common inflation error.
- Realistic payback bands, vary by scope, a well-scoped automation often 6 to 12
  months, a larger platform build 12 to 30. Under 6 months implies unusually high
  volume or tiny scope, over about 18 to 24 should trigger "is this even the right
  solution."

## State it as a range with calibrated assumptions

Douglas Hubbard, How to Measure Anything, is the basis. Untrained estimators are
wildly overconfident, their "90 percent" ranges hold the truth only about half the
time, so express every uncertain input as a range with a confidence level. Present
at minimum three scenarios, conservative, most-likely, aggressive, varying the few
drivers that actually move the answer. The decision rule that signals honesty, the
CONSERVATIVE case still clears the hurdle. A program that only works under
aggressive assumptions carries more risk, and we say so.

## Guard against inflation, the outside view

Point estimates from the inside view systematically underestimate cost and
overestimate benefit. Correct with reference-class forecasting (Kahneman, Tversky,
Flyvbjerg). Identify a class of similar past projects, establish the range of
outcomes across that class, and position this build against it. On mandated road
projects this cut average cost overruns from 38 percent to 5. For AI the reference
class is the MIT 95 percent and RAND 80 percent failure data, so every ROI section
states explicitly why this build is designed to beat the base rate, workflow-
embedded, adoption-owned, measured, rather than pretending the base rate does not
apply. https://en.wikipedia.org/wiki/Reference_class_forecasting

Flyvbjerg's distinction to respect, much overrun is not honest optimism but numbers
reverse-engineered to clear approval. Our case must be defensible against exactly
that suspicion, which is why the conservative case has to stand on its own.

## The hype-vs-honest table (self-audit before shipping)

| Hype pattern | Honest guard |
|---|---|
| Single hero ROI number | A range with named assumptions, risk-adjusted |
| Day-one full benefits | Phase the curve with an adoption ramp |
| Freed hours counted as cash | Apply redeploy or defer-hire or avoid-backfill, label capacity vs cash |
| Vendor or industry benchmark as baseline | Use the company's own measured baseline, or state it is assumed |
| Kitchen-sink benefit stacking | Cap at about five, drop the weak ones |
| Soft benefits inflating the formula | Quarantine qualitative benefits, unquantified |
| Inside-view estimate | Reference-class or base-rate sanity check |
| Numbers with no owner | Name a value owner and a variance-tracking plan |

## Close the loop, or it is fantasy

The marker of a credible case is that it plans to be checked. Define the baseline
in the study, document the assumptions behind every estimate, name a single value
owner accountable for the benefit, and describe the variance check (actual vs
baseline) after go-live. A case with no owner and no post-hoc measurement is
fantasy by construction, so the Field Study always names who owns the number and
how we would know it worked.

## The three levers, if the analyst internalizes only these

One, never a single number, a risk-adjusted range with stated calibrated
assumptions. Two, anchor to the outside-view base rate (for AI, MIT 95) and phase
benefits with an adoption ramp instead of day one. Three, the conservative case
clears the bar on its own, with a named owner who tracks actual against baseline.
