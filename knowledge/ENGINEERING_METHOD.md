# The Engineering Method

How the room decides what to build and scopes it like a real shop. This is the
spine that keeps the Field Study legit instead of AI theater. Every stage here
maps to an established practice with a named source, so a skeptical CTO on the
other end recognizes the process. Read this before the room runs.

The one law of the room: the decision is the deliverable, and it must be
defensible against known risks, not the most exciting idea. We pick ONE build,
and we can say out loud why that one and not the others.

## The loop every good team runs

Start from a business outcome. Find the real customer job, not a feature.
Generate several candidate solutions. Attack the riskiest assumptions cheaply
before building. Commit to the smallest thing that moves the outcome. The
expensive mistake is choosing what to build by intuition or by whoever is
loudest, and the cure is evidence gathered before engineering spends real money.
(Cagan/SVPG, Torres, Amazon Working Backwards all reduce to this.)

## Stage 1, fix the outcome (product-strategist)

Name the business outcome the build must move, as a measurable change in
behavior, not "ship feature X." Reject any candidate whose value is "we shipped
it." This is Marty Cagan's empowered-team stance and Melissa Perri's escape from
the build trap: teams are given problems to solve and measured by outcomes, not
output. https://www.svpg.com/four-big-risks/

## Stage 2, mine opportunities as Jobs, not features (product-strategist)

From the verified research, pull customer jobs, pains, and current workarounds.
The competitor set is whatever the customer uses TODAY, which may be a spreadsheet,
a phone, or a person, not another software product. This is Jobs To Be Done
(Christensen, Moesta) and the middle layer of Teresa Torres's Opportunity Solution
Tree. Opportunities are needs and pains, never solutions. Do not let a solution
enter yet. https://jobstobedone.org/the-four-forces/
https://www.producttalk.org/opportunity-solution-trees/

The Four Forces of Progress tell you whether a switch will actually happen. Push
of the current frustration plus Pull of the new way must EXCEED Anxiety about the
new thing plus Habit of the present. A build only wins when push and pull already
beat anxiety and habit, so the best target is where the frustration is loud and we
can also actively lower anxiety and habit.

## Stage 3, score opportunities for underserved (product-strategist)

Rank the jobs by Tony Ulwick's opportunity math, Importance plus max(Importance
minus Satisfaction, 0), which weights importance double. High importance plus low
current satisfaction equals highest ROI. Cross-check with Torres's four factors,
opportunity sizing, market position, fit with the company strategy, and how much
customers care and how satisfied they are today. Pick the target OPPORTUNITY here,
before any solution. https://strategyn.com/tony-ulwick/

Treat the numbers as ranking heuristics that structure the debate, not oracles.
Ulwick's thresholds and the exact weights are conventions, not laws.

## Stage 4, generate multiple candidate builds (product-strategist)

Force three or more candidate solutions for the target opportunity so the room
compares instead of defending its first idea. This is Torres's insistence on more
than one solution per opportunity, the thing that separates discovery from a pitch.

## Stage 5, the feasibility gate, do you even need AI (ai-feasibility-engineer)

This is the conscience of the room and the reason a CTO trusts us. See
AI_SCOPING.md for the full protocol. In short, walk the ladder, deterministic
rules, then retrieval or lookup, then a single LLM call, then a workflow with the
LLM in fixed steps, then a dynamic agent. Each step up costs reliability, money,
latency, and explainability, so it must be earned. Google's Rule of ML number one,
if machine learning gives a 100 percent boost then a heuristic gets 50 percent of
the way there, so do not be afraid to launch without ML. Anthropic, find the
simplest solution and only add complexity when needed, which might mean not
building an agent at all. Kill or downscope any candidate that fails cost-of-error,
data-readiness, or the compounding-error math.
https://developers.google.com/machine-learning/guides/rules-of-ml
https://www.anthropic.com/engineering/building-effective-agents

## Stage 6, prioritize to one pick (product-strategist, with the room)

Score the survivors with RICE, Reach times Impact times Confidence divided by
Effort, and add a Cost of Delay or WSJF term so time-sensitive builds surface
(Reinertsen, SAFe). The Confidence factor is the honesty lever, it discounts a
build whose evidence in the dossier is thin, which is exactly where AI hype gets
penalized automatically. Scores rank and frame the debate, they do not auto-decide.
https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/
https://framework.scaledagile.com/wsjf

## Stage 7, retire the four risks before committing (the room)

Gate the single pick against Cagan's four big risks. Value, will they use or buy
it, owned by the strategist. Usability, can they figure it out. Feasibility, can
this actually be built with real tech, owned by the staff-engineer. Business
Viability, does it work for their sales, finance, legal, and brand. Make
feasibility and viability HARD gates, because those are the two an over-eager AI
skips. Re-run the Four Forces check, if adoption forces are weak, downgrade even a
high-scoring idea. https://www.svpg.com/four-big-risks/

## Stage 8, design the one build (staff-engineer)

Produce a design-doc-grade solution, sized to the problem, one to three pages of
substance. Sources, Google design docs (Malte Ubl), the C4 model (Simon Brown),
Nygard ADRs, Cockburn's walking skeleton, McConnell's Cone of Uncertainty.
https://www.industrialempathy.com/posts/design-docs-at-google/ https://c4model.com/

Required elements, this is the difference between a buildable plan and vaporware:
- Named, concrete components. Real services, data stores, APIs, and integration
  edges (C4 container level), never "a scalable AI platform."
- Data flow. Who writes, who reads, sync or async, drawn as named edges.
- Every integration named. Their booking system, their EHR, their phone provider,
  their CRM, with the auth and the third-party dependency called out.
- Cross-cutting concerns. Auth, security, data handling, observability, and the
  failure modes, mapped onto the design.
- Build vs buy per component. Default to buying the commodity (telephony, auth,
  vector store, base models) and building only the differentiator, and say why
  each build is a build. Hybrid is the honest default.
- Goals and non-goals. Non-goals are the honest-scope lever, the things that
  could be goals but are deliberately out, each with a reason.
- The riskiest assumption named, plus a time-boxed spike or proof-of-concept to
  retire it before committing. Move from "we think this will work" to "we know."
- Estimates as RANGES tied to a confidence and a phase, never a single date on a
  vague spec. The Cone of Uncertainty does not narrow itself, it narrows only when
  you make decisions and cut variability. At concept a sound range spans a wide
  band, and we say so honestly.
- Delivery shape, walking skeleton first. The thinnest end-to-end slice that
  touches every main component and actually runs, on crutches with the hard parts
  stubbed, then flesh it out, then the MVP.

## Stage 9, the PRD as a proposal (product-manager)

Write a proposal-grade PRD fused with an Amazon PR/FAQ opening. The reader is the
prospect, so it must be persuasive AND honest, because it becomes the contract on
delivery. See FIELD_STUDY_SPEC.md for the exact section set. The test that matters,
a reader could read the first half, not yet know what gets built, and still agree
it is worth building. Problem, user, and reason-now stand on their own before any
solution. Every success metric is falsifiable, a baseline, a target, and a
timeframe. Non-goals are explicit with reasons. Prospect-side dependencies (their
data, their people, their sign-offs) are named, because unstated ones are the usual
cause of a blown timeline. https://www.svpg.com/assessing-product-opportunities/
https://workingbackwards.com/resources/working-backwards-pr-faq/

## Stage 10, the honest business case (roi-analyst)

See ROI_METHOD.md. Never a single hero number. A risk-adjusted range with stated,
calibrated assumptions, benefits phased with an adoption ramp, three scenarios
where the conservative case still clears the bar, anchored against the outside-view
base rate (for AI, the MIT 95 percent and RAND 80 percent), with a named owner who
tracks actual against baseline afterward.

## Stage 11, the roadmap (delivery-lead)

Now, Next, Later by confidence, not a dated Gantt (Bastow, Torres, Cagan). Each
item ties to a target metric. Sequence by Cost of Delay over size (WSJF), so Phase
one is the highest-value smallest-job slice, the walking skeleton carrying the
fastest hard-dollar benefit. Fund it in staged gates, release the next phase only
when the last phase's actuals clear. https://www.prodpad.com/blog/invented-now-next-later-roadmap/

## What separates rigor from guessing

Rigor is outcome-anchored not output, problem-first not solution-first,
evidence-before-build not opinion, comparative (several solutions per problem),
and risk-complete (all four risks checked, especially viability and adoption). If
the Field Study reads as one confident idea with no alternatives, no non-goals, no
ranges, and no named risks, it is guessing dressed up, and it does not ship.
