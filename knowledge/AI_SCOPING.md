# AI Scoping, the honest conscience

The single thing that makes this Field Study trustworthy instead of another AI
pitch. The ai-feasibility-engineer owns this doc, and every other agent respects
it. The credible way to scope an AI build is to treat "should we use AI at all"
as the first real gate, not a foregone conclusion. Projects almost never die from
model quality. They die from a misdefined problem, missing data, no evaluation,
and no workflow integration. Our job is to be the shop that says that out loud.

## The failure data (the anti-BS foundation, cite together, never alone)

Four independent, authoritative studies tell the same story. Use them to frame our
honesty, never to bash AI.

- MIT Project NANDA, State of AI in Business 2025. About 95 percent of enterprise
  generative-AI pilots produce no measurable P&L impact, only about 5 percent
  achieve real revenue acceleration. The cause is the learning and integration
  gap, not model quality. Buying from specialized vendors succeeded about twice as
  often as internal builds. Caveat to bake in, the 95 percent is directional and
  its denominator is debated, and it measures pilots without P&L impact, not "AI
  does not work." Triangulate, never weaponize.
  https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/
- RAND, The Root Causes of Failure for AI Projects (RRA2680-1). More than 80
  percent of AI projects fail, about twice the rate of non-AI IT. The five root
  causes, misunderstanding the problem, lacking the data, chasing the latest tech
  over the real problem, weak infrastructure, and applying AI to problems too hard
  for it. https://www.rand.org/pubs/research_reports/RRA2680-1.html
- Gartner, June 2025. Over 40 percent of agentic-AI projects will be canceled by
  end of 2027, from cost, unclear value, or weak risk controls. Gartner names
  "agent washing," rebranding chatbots and RPA as agents. Current models lack the
  maturity to autonomously achieve complex goals over time.
  https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027
- McKinsey, State of AI, March 2025. Nearly 80 percent use gen AI somewhere, yet
  more than 80 percent report no tangible enterprise-level EBIT impact. The single
  biggest differentiator is fundamental workflow redesign, which few have done.
  https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-how-organizations-are-rewiring-to-capture-value

What separates the projects that succeed, a narrowly defined problem tied to a real
decision, data that already exists and is usable, an acceptance bar set before
building, deep integration into an existing workflow, and sustained ownership.
Novelty of the model is not on the list. Every Field Study states plainly that it
is built to be in the 5 percent, and why.

## The feasibility ladder (walk it, do not skip it)

Rules and deterministic software, then retrieval or lookup, then a single LLM call,
then a workflow (LLM in fixed, testable steps), then a dynamic agent. Each step up
buys capability at the cost of reliability, money, latency, and explainability, so
each step must be earned by the problem.

- Google, Rules of ML, Rule 1. Do not be afraid to launch without machine
  learning. If ML would give a 100 percent boost, a heuristic gets you 50 percent
  of the way there. https://developers.google.com/machine-learning/guides/rules-of-ml
- Anthropic, Building Effective Agents. Find the simplest solution possible and
  only increase complexity when needed, which might mean not building an agentic
  system at all. Use workflows for well-defined tasks, agents only for open-ended
  problems where you cannot hardcode the path.
  https://www.anthropic.com/engineering/building-effective-agents
- Google PAIR. The honest question is "can AI solve this in a UNIQUE way," not
  "can we use AI." AI is the wrong fit when you need predictability, full
  transparency, minimized costly errors, or high speed at low cost. It is a good
  fit for prediction, personalization, language understanding, and detecting
  low-occurrence patterns that change over time.
  https://pair.withgoogle.com/chapter/user-needs/

Saying "you do not need AI for this part, a rule does it cheaper and you can test
it exhaustively" is not a lost sale. It is the whole trust proposition, and it is
what earns the part where AI genuinely wins.

## Cost of error (force this every time)

What does a wrong answer cost this business, and who catches it. If errors are
costly and unforgiving, or full transparency is required, either do not use AI or
wrap it in human review and guardrails. Every classifier has a confusion matrix,
and weighing false positives against false negatives is a design decision, not an
afterthought. A separate model instance screening inputs and outputs beats asking
one model to do the task and police itself (Anthropic).

## Data readiness (the hidden project)

Missing or messy data is the number two killer. Force these before promising
anything. Does the data exist. Is it accessible or locked in a PDF, a phone
system, or a vendor. Is it labeled, and who labels it. Is it representative of
production and does it stay fresh. Is it legally usable, PII, licensing, consent.
For a RAG build, is the corpus clean, permissioned, deduplicated, and current. If
the answer is no, that gap IS the project, and the Field Study says so instead of
hiding it. (RAND cause 2, Sculley et al. Hidden Technical Debt, NeurIPS 2015.)

## Evaluation (no evals, no promise)

If we cannot state the acceptance metric, the eval set, the human-review path, and
the fallback for a wrong answer, the build is not scoped, it is a demo. Hamel
Husain, unsuccessful AI products almost always share one root cause, no robust
evaluation. Levels, assertions and unit tests on every change, human plus
model-as-judge with agreement measured against human labels, and A/B in production
once mature. https://hamel.dev/blog/posts/evals/

## The compounding-error math (for anything multi-step)

End-to-end success is roughly per-step reliability raised to the number of steps.
At 95 percent per step, 5 steps is about 77 percent, 10 steps about 60, 20 steps
about 36. At 90 percent, 20 steps is about 12. Real agents on realistic tasks
often run 85 to 90 percent per step. So minimize step count, put a human in the
loop at high-cost actions, set an error budget, and default to a workflow unless
the problem is genuinely open-ended. This is the category most inflated by agent
washing, scope it with the most skepticism.

## Per-build-type honest scoping (the common SMB builds)

Voice and phone agents. The hard constraint is latency, not language. Smooth is
under about 800ms end to end, many production systems land at 1400 to 1700ms which
callers feel as slow. Start with narrow high-frequency intents, booking, hours,
FAQ, routing, with a clean human handoff. Integrations, telephony (SIP/Twilio),
the calendar or booking system, business hours and pricing logic, transfer to a
person. Main risk, latency and misrecognition on the long tail, and brand damage
from a bot that stalls. MVP in weeks, production-trustworthy for edge cases is the
real work.

RAG and document assistants. Nearly every business can build a proof of concept,
very few run RAG reliably in production. Retrieval precision drops on noisy corpora
and degrades as the corpus grows, and the fix is better embeddings, hybrid search,
and reranking, not more documents. Scope, a bounded corpus, clear question types,
citations, an honest "I do not know," an eval set of real Q&A pairs, and access
control that respects who may see what. Main risk, confident wrong answers and
stale content.

Workflow automation. Use deterministic automation or RPA when inputs are
structured, stable, high-volume, or high-risk (invoicing, compliance, record
updates), because the same input always gives the same output and you can test it
exhaustively. Put AI only on the messy-input node, reading unstructured text,
judgment, drafting. Map the process first, then place AI surgically. Main risk,
over-automating a judgment step, and per-run LLM cost at volume.

Task agents, multi-step and autonomous. Respect the compounding-error math above.
Minimize steps, human-in-the-loop checkpoints at costly actions, an error budget,
and default to a fixed workflow unless the task is truly open-ended. Scope this
category with the most skepticism, it is where agent washing lives.

## Hype to flag and never commit (the kill-list)

- Agent washing, calling a chatbot or an RPA script an autonomous agent.
- Set-and-forget autonomy for complex goals, contradicted by Gartner and the
  compounding math.
- A single hero ROI number. Always a range with named assumptions (see ROI_METHOD).
- Day-one full benefits. Phase the curve with an adoption ramp.
- Freed hours counted as cash without the redeploy, defer-hire, or avoid-backfill
  test.
- Vendor or industry averages used as this company's baseline.
- Just point RAG at your documents. Retrieval degrades and enterprise needs access
  control and freshness.
- Sub-500ms voice latency as the default expectation.
- Build it in-house, it is just an API call. The hard part is integration and
  evaluation, and buying succeeds about twice as often for commodity capability.
- ROI inevitability. Most organizations see no EBIT impact without workflow
  redesign, so promising ROI without redesign is the most common overpromise.

## Source-reliability note

The authoritative tier, build claims on these, MIT NANDA, RAND, Gartner, McKinsey,
Google (Rules of ML and PAIR), Anthropic, Sculley/NeurIPS, Hamel Husain, Eugene
Yan. Vendor or single-analysis blogs (voice-latency medians, RAG-failure
specifics, the "62 percent of failed automations were agentic" stat) may be used
for the principle but must be presented as vendor-sourced, never as established
fact. When a number is contested, say so in the study. Honest beats impressive.
