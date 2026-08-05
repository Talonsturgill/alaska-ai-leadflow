# The machine backlog

Improvements to the routine itself, each one earned by something that actually
went wrong or cost rounds in a real run. Ordered by leverage, not by effort.

Rules for this file. Nothing goes in it without EVIDENCE from a dated run. No
speculative "would be nice." When an item ships, move it to SHIPPED with the run
that proved it worked. A run may add to this file. A run may not quietly delete
from it.

---

## 1. study_qa measures the wrong thing, and every run fights it

**Evidence.** 2026-08-05 shipped at 3,858 words against a 3,000 target, and three
separate trimming passes moved it about 250 words while the study-critic
independently judged the prose spine to be roughly 2,400 words, a nine-minute
read. The critic then withdrew its own cut request, saying "counting a table cell
against a reading-time budget is the wrong instrument." Roughly 1,400 of the count
was an eight-row ROI table, a thirteen-item roadmap table, a five-row before and
after ledger and fourteen source lines. None of it is read linearly.

**The cost.** Every run burns showrunner effort trimming toward a number that does
not mean what it says, and the pressure runs AGAINST the honesty disclosures the
critics demand, which is the worst possible direction for it to run.

**The fix.** Split the metric. Count PROSE words against the 2,000 to 3,000 budget,
which is what Nielsen's reading-time model was ever about. Report table cells,
source lines and figure labels separately as STRUCTURE, with their own budget.
FIELD_STUDY_SPEC's budget table gets a second row.

**Why it is first.** It is small, it is mechanical, and it stops a recurring fight
between two gates that are both right.

---

## 2. There is no self-improvement loop in this repo

**Evidence.** The sibling carousel routine runs a Phase 12 upgrade-engineer and
keeps `ledger/upgrades.json`, an automation-change trail surfaced in every dated
email. This repo has neither. Every lesson from every run of this routine lives
only in a commit message, where nothing reads it.

**The cost.** The compounding one. Seven critic rounds on 2026-07-29 produced two
rules that made it into CLAUDE.md only because a human wrote them down. The
2026-08-05 drift pattern has now been independently rediscovered by the
fact-checker and the study-critic in the same run and in earlier runs, which means
the machine keeps paying to relearn it.

**The fix.** A Phase 10 retro. Diff what the run actually did against the contract,
name what cost rounds, and make 0 to 3 bounded, verified changes to the machine,
logged to `ledger/upgrades.json` and surfaced in the delivery summary. Bounded and
verified are the important words, an unbounded self-editing routine is how a
machine rewrites the rules it is judged by.

**Guard.** It may never edit OUTREACH_CRAFT.md, CLAUDE.md's laws, or its own
quality bars. Those are hand-authored on purpose. It proposes those, it does not
apply them.

---

## 3. Half the study-critic's blocking items are machine-checkable

**Evidence.** 2026-08-05 round one returned twelve blocking items. At least five
were mechanical and would have been caught by a linter, an unsourced factual claim
(the MIT and RAND figures had no entry in sources[]), a provenance mark asserting
`verified` on an absence, two unverifiable negative assertions about the
prospect's internal tooling, and an ROI note whose stated arithmetic did not
reconcile with its own table.

**The cost.** Each critic round is expensive and slow. Every mechanical item that
reaches a critic is a round spent on something a script could have caught in
milliseconds, and it buries the judgement calls that actually need a critic.

**The fix.** `scripts/study_lint.py`, run before any critic sees the study.
- Every sentence stating a fact about the company maps to a claim id in claims.json
- Every URL in the body appears in sources[], and every source is cited somewhere
- No `verified` provenance mark without a matching high-confidence claim
- Flag unverifiable negatives, the pattern "no X exists / nothing does Y / they
  have no Z" where the subject is the prospect's own operation
- ROI table internal reconciliation, recompute every derived cell from the driver
  rows and fail on mismatch

The last one is the highest value. The 2026-08-05 table shipped a recovery row and
a break-even row sitting on different bases, and only a careful fact-checker caught
it. That is arithmetic, and arithmetic belongs in code.

---

## 4. The drift pattern is systemic, not a per-run accident

**Evidence.** Named as a `drift_pattern` by the fact-checker on 2026-08-05, then
independently rediscovered by the study-critic on the same study after one round of
fixes, then found AGAIN in a milder form on round two. Every rejection leaned the
same way, toward making the prospect look more strained and further behind than
their own pages support. Earlier runs show the same shape.

**The diagnosis.** This is not carelessness. It is the pipeline's incentive
gradient. A pitch is easier to write when the prospect is in trouble, so every
agent shades microscopically in that direction and the errors compound because they
all lean together.

**The fix, two parts.**
1. Mechanical, in study_lint, per item 3. Unverifiable negatives about the prospect
   are the specific tell and they are greppable.
2. Doctrinal. The showrunner does one explicit DIRECTION PASS before the critic,
   reading the study asking only "does this make them look worse than the evidence
   does." That is already in CLAUDE.md as a principle. It should be a named step
   with an artifact, because principles get skipped and steps do not.

---

## 5. The email brief is the defect, and nothing enforces that

**Evidence.** The 2026-08-05 email took three lead-critic rounds. Round two found
that round one's fix had MOVED the defect rather than killed it. VOICE_DELTAS has
carried "fix the brief, not the individual email" for weeks, and `lengthened` has
been READY TO PROMOTE across five separate sends without ever being promoted,
because promotion is correctly a human decision that nothing surfaces at the right
moment.

**The fix.** When the lead-critic returns `fix` twice on the same email, the
showrunner must rewrite the BRIEF and say what it changed, rather than passing the
same brief back with one more instruction stapled on. And a READY TO PROMOTE
pattern should appear in the delivery summary as a decision request with the
suggested wording already drafted, so the human is approving a diff rather than
being handed homework.

---

## 6. The rooms cannot see each other's constraints

**Evidence.** On 2026-08-05 the product-manager wrote its PRD before the
staff-engineer's design existed, flagged that itself, and correctly noted the two
would need reconciling. They happened to agree. They might not have.

**The fix.** Cheap version, the Phase 4 agents that depend on a design run after it
rather than beside it, accepting the wall-clock cost. Better version, the
showrunner reconciles the four outputs against each other before assembling
study.json, with an explicit contradiction check. `claim_sweep.py` already does
this for the finished study and finds real conflicts, so run something like it one
stage earlier, on the engineering outputs.

---

## 7. Nothing measures whether any of this works

**Evidence.** Seventeen leads, sixteen drafts, one confirmed send, and no recorded
reply, meeting or outcome anywhere in the ledger. The routine optimises study
quality with total rigor and has no idea whether study quality moves the thing it
exists to move.

**The fix.** An `outcome` field on the lead that a human can set with one command,
`ledger.py record-outcome --domain <d> --outcome replied|meeting|won|ignored`.
Then `ledger.py stats` reports reply rate by segment, by opening type and by
whether the study recommended a build or advised against one. That last cut is the
interesting one, because the honest-restraint thesis is currently an article of
faith and it is testable.

**Why it is last on this list and possibly first in reality.** It needs Talon to do
something after each send, which nothing else here does. Everything above makes the
output better. This one tells us whether better output matters, which is worth more
than all of them and costs the most to get.

---

## SHIPPED

- **2026-08-05, item 6, scripts/room_reconcile.py.** Cross-checks the room's four
  parallel outputs before they become a study. Killed capability promised anyway,
  non-goal delivered by the roadmap, pick drift, AI role drift. Validated against
  four injected contradictions, caught all four, after four rounds of false
  positives that are recorded in the upgrades ledger because they are the failure
  mode of a checker like this.
- **2026-08-05, item 4, THE DIRECTION PASS.** The mechanical half shipped inside
  study_lint. The doctrinal half is now a named Phase 6 step with a required
  artifact, out/<date>/direction_pass.md, because it was a principle for weeks and
  principles get skipped while steps do not.

- **2026-08-05, item 3, scripts/study_lint.py.** Runs before any critic. Catches
  forbidden strings the fact-checker rejected coming back, URLs in the body with
  no sources entry, a `verified` mark on something nobody verified, an ROI table
  whose printed cells do not reconcile with its own drivers, and unverifiable
  negatives about the prospect. Validated against five reconstructions of the
  defects that actually shipped or were blocked that day, caught all five, zero
  false positives on the clean study. Wired into the Phase 6 ship gate.
- **2026-08-05, item 2, the self-improvement loop.** Phase 10 retro in the run
  contract plus ledger/upgrades.json. At most three bounded, verified changes per
  run, each with the evidence that earned it, surfaced in the delivery summary.
  Hard guard: a run may never edit OUTREACH_CRAFT.md, CLAUDE.md, or any bar it is
  judged against. It proposes those with wording drafted and a human decides.
- **2026-08-05, item 7, outcome tracking.** ledger.py record-outcome and
  scoreboard, cutting reply rate by segment, by named-human versus general inbox,
  by fit score, and by whether we recommended AGAINST a build, which is the cut
  that tests the honest-restraint thesis instead of believing it.

- **2026-08-05, gotcha openings banned.** The email opened on a website
  inconsistency, which passed every rule and was still worthless. OUTREACH_CRAFT
  gained WHAT THE FIRST SENTENCE IS ABOUT, with a nod test and a meeting test.
- **2026-08-05, the research came back jaded.** A briefing error weighted the
  industry pass toward failure data. AI_SCOPING gained THE CONSCIENCE CUTS BOTH
  WAYS, the industry-analyst was rebriefed as the scout rather than the skeptic,
  and OUTREACH_CRAFT gained CARRY ONE PIECE OF REAL INDUSTRY PROOF.
- **2026-08-05, Supabase retired.** Three consecutive runs owed a write the
  connector could not retry. The database is git, large documents are files, and
  inbound intake is a GitHub issue queue.
