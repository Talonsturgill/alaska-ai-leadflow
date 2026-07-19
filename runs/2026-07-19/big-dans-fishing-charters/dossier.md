# Dossier, Big Dan's Fishing Charters (2026-07-19)

## Pick
Fit 23 (highest of 21 candidates across tourism, healthcare, ANC, other-SMB segments).
Family-owned, four-vessel, three-location (Homer/Seward/Soldotna) Kenai Peninsula
charter and lodging operator. Owners Dan and Sarah Spies. Verified contact
bigdansfishing@gmail.com, sourced from https://bigdansfishing.com/big-dans-crew/.

## The pain (cited)
"For dates not showing availability online, your best bet is to call Sarah at
907-598-3391." Sarah is the sole named fallback across 4 boats, 3 locations, 5
cabins, river trips, and hunting transport, during a compressed 4-month season.
A second cited quirk, the FareHarbor calendar hides other trip types once one is
selected for a date.

## Competitive field
No competitor in Homer, Seward, or Soldotna runs anything AI-driven. Homer Halibut
Hunters has a human-staffed live chat (not AI). Everyone else is FareHarbor-only,
phone-only, or a standard booking button.

## Industry grounding
Two named small-operator AI chatbot case studies (Destin Party Boat Fishing,
Black Cat Cruises) show real conversion/call-deflection gains, vendor-reported.
Accommodation/food services has the lowest AI adoption of any sector measured
(Fed data ~8%, Census data confirms small firms lag badly). MIT (~95% no P&L
impact) and RAND (~80% project failure) base rates cited honestly.

## Discovery (product-strategist)
Outcome: cut the share of booking inquiries dependent on Sarah's phone callback.
Target opportunity merges the two highest Ulwick-scored jobs (13 and 10):
fast answers to off-calendar/after-hours questions. Four candidates generated,
ranked by RICE: (1) AI front-desk chat/phone agent [picked], (2) RAG FAQ
assistant [weak, does not touch the bottleneck], (3) structured intake workflow
[kept as backbone, not primary], (4) fully autonomous digital employee
[confidence 0.2, killed].

## Feasibility (ai-feasibility-engineer)
Verdict: downscope. Workflow tier (not an agent), deterministic FareHarbor
lookups plus model-judged intent-parse/reply only. Killed the RAG FAQ candidate
and the fully autonomous candidate (compounding-error estimate ~48% end-to-end,
no small-operator precedent). Named two real open dependencies: FareHarbor
API/webhook access unconfirmed, telephony integration unconfirmed. Where not to
use AI: the FAQ layer, the go/no-go booking decision, and any weather or
hunting-transport safety call, all hard rules, never model judgment.

## Locked pick
AI front-desk chat agent, FareHarbor-integrated, chat-first MVP (phone gated on
a later telephony confirmation). Cagan four-risks check passed (feasibility,
value, usability, viability all clear, conditioned on the escalation guardrail
staying load-bearing).

## Engineering room
Staff-engineer: C4 design, named components (FareHarbor, chat widget, escalation
router, notification service), riskiest assumption is FareHarbor API access,
retired by a 3-5 day spike. Walking skeleton 1-2 weeks, MVP 3-6 weeks.
Product-manager: proposal-grade PRD, 4 falsifiable metrics (all with assumed
baselines pending a real call-log spot check), 5 non-goals with reasons.
Delivery-lead: Now/Next/Later roadmap, staged gates, phone gated on Now-phase
results plus telephony confirmation.

## ROI (roi-analyst), the reason this run stopped here
First pass quoted a 5-year TCO ($16k-29k) against which the conservative case
did not clear. Study-critic flagged this (verdict: fix). Rescoped to an honest
near-term ask (a no-cost 2-4 week baseline check, then an $8k-14k chat-only
MVP for one season, not a 5-year commitment). Even at this honestly smaller
scope, the conservative case still does not recover cost in cash alone at any
modeled horizon (most-likely payback ~20-30 months, aggressive ~10-14 months,
conservative never clears). This is a structural finding, no real call-volume
baseline exists for this company, not a modeling error, and the roi-analyst
refused to manufacture a pass.

## Study-critic (ship gate)
Pass 1: fix (ROI framing, 2 unsourced claims). All three corrected.
Pass 2: fix again, specifically on ROI_METHOD's hard rule that the conservative
case must clear on its own. Per the routine's one-fix-and-recheck-cycle rule,
this is the terminal state. Study does not ship as outreach today.

## Disposition
Recorded as status "researched," not suppressed. Available to revisit by hand,
for instance if Talon wants to pitch the free baseline check itself as the
first ask rather than a dollar figure, which is exactly what the study
recommends. Full package (study.json, field-study.html/.pdf, demo.html) archived
alongside this dossier. Gmail draft note to Talon: r4015728434867913776.
Nothing sent. No contact fabricated.
