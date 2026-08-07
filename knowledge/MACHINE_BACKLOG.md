# The machine backlog

Improvements to the routine itself, each one earned by something that actually
went wrong or cost rounds in a real run. Ordered by leverage, not by effort.

Rules for this file. Nothing goes in it without EVIDENCE from a dated run. No
speculative "would be nice." When an item ships, move it to SHIPPED with the run
that proved it worked. A run may add to this file. A run may not quietly delete
from it.

---

## OPEN

- **2026-08-06, item 8, the 54 against 12 measurement figure has no primary
  source we could reach.** BLOCKED ON A HUMAN DECISION, not on effort.

  EVIDENCE. The 10b frontier scan checked whether ROI_METHOD's outside-view base
  rate is still current. It is: MIT 95 percent and RAND 80 percent both still
  read as the standing numbers in August 2026, so nothing there needed changing.
  The scan did surface one figure that would be genuinely useful to us, that AI
  projects with quantified success metrics defined upfront succeed at 54 percent
  against 12 percent for those without, attributed everywhere to a 2025 MIT Sloan
  study. It is the outside-view argument for the exact thing this routine keeps
  selling as phase one, instrumentation and baselines before any model, and this
  run had to make that argument entirely on its own reasoning.

  WHY IT IS NOT SHIPPED. Every page carrying it inside the timebox was a
  secondary content-marketing restatement. No primary paper was located. A number
  in knowledge/ROI_METHOD.md is a number every future study is allowed to cite,
  and HONESTY says a fact traces to a page that was fetched, so putting an
  untraced figure into the file that governs our honesty is precisely backwards.

  WHAT UNBLOCKS IT. Someone locating the primary study, or the maintainer
  deciding a well-attributed secondary source is acceptable for a base-rate
  anchor. A run cannot make that second call for itself, because ROI_METHOD is a
  bar this routine is judged against.

  A related figure from the same scan, that 61 percent of enterprise AI projects
  are approved on projected ROI nobody ever measures after launch, has the same
  problem and the same fix.

- **2026-08-07, the prose budget is enforced without being addressable.**
  BIGGER THAN ONE RUN, and it damaged the deliverable rather than merely
  costing time.

  EVIDENCE. study_qa reports a single prose word count and the study failed it
  on almost every iteration, so this run made roughly twenty seven separate
  trimming passes to hold 3,000 words across five critic rounds. The count is
  computed from the RENDERED HTML by subtracting table cells, sources and
  captions, so nothing tells the showrunner which study.json field contributes
  what. Every trim was therefore a guess, and most landed five to ten words
  short of useful, which is why there were so many.

  The cost was not the passes. In EVERY critic round a caveat was lost or
  garbled in the cutting, and the critics named it each time. Round two lost the
  sentence that kept eleven job openings from reading as distress. Round three
  lost the positive half of the industry evidence and left three orphaned
  citations behind, all three of which cut against our own recommendation.
  Round four lost the sentence naming what the CMMC certification actually
  constrains. Round five did not delete a caveat but GARBLED two, a verb that
  captured its object and an appositive that no longer resolved, which the
  critic correctly called harder to see because the words are still on the page.
  Trimming removes qualifying clauses first, because qualifiers read as slack,
  and that is a mechanism rather than an accident.

  WHY IT IS NOT SHIPPED. The obvious fix, a per-field prose contribution report,
  needs the builder to attribute rendered text back to its source key, which is
  a real change to build_study_page rather than a helper beside it. Doing it
  badly would produce a number that looks authoritative and is wrong, which is
  the failure mode of the word count itself. The deeper question, whether a
  study that has to be cut twenty seven times is too long or the budget is too
  tight for a document carrying this many honesty disclosures, is a maintainer
  call and not a run's to make.

- **2026-08-07, the shell working directory drifts and nothing notices.**
  SMALL BUT IT ALMOST LOST THE RUN'S REPLACEMENT QUEUE.

  EVIDENCE. Phase 1 wrote selection.md, shortlist.json and all four scout
  outputs to /home/user/out/2026-08-07/ instead of the repo, because an earlier
  command had cd'd to the sibling checkout and the working directory persisted.
  Every write succeeded, nothing warned, and it was only caught at Phase 8 when
  the archive step could not find selection.md. Three later commands failed
  outright with FileNotFoundError for the same reason. Had the run crashed
  before the archive, the shortlist and the entire replacement queue would have
  been outside the repo and invisible to a resume.

  WHAT WOULD FIX IT. Either every phase writes through a helper that resolves
  paths against the repo root rather than the cwd, or the run contract says to
  use absolute paths for every artifact write. The second is a contract change
  and the first touches every write in the run, so neither belongs in the tail
  of a run that has already shipped.

The rules at the top still bind: evidence from a dated run, no speculative "would
be nice", and a run may add but may never quietly delete.

---

## SHIPPED

- **2026-08-05, item 1, study_qa counts prose separately from structure.** Table
  cells, source lines and figure labels are no longer charged against a
  reading-time budget, because none of them is read linearly. The study that
  triggered this measured 3,858 words against a 3,000 target while its actual
  prose spine was roughly 2,400, so three trimming passes fought a number that
  did not mean what it said, and the pressure ran against the honesty
  disclosures the critics demand.

- **2026-08-05, item 2, the self-improvement loop.** Phase 10 retro in the run
  contract plus ledger/upgrades.json. At most three bounded, verified changes per
  run, each with the evidence that earned it, surfaced in the delivery summary.
  Hard guard: a run may never edit OUTREACH_CRAFT.md, CLAUDE.md, or any bar it is
  judged against. It proposes those with wording drafted and a human decides.

- **2026-08-05, item 3, scripts/study_lint.py.** Runs before any critic. Catches
  forbidden strings the fact-checker rejected coming back, URLs in the body with
  no sources entry, a `verified` mark on something nobody verified, an ROI table
  whose printed cells do not reconcile with its own drivers, and unverifiable
  negatives about the prospect. Validated against five reconstructions of the
  defects that actually shipped or were blocked that day, caught all five, zero
  false positives on the clean study. Wired into the Phase 6 ship gate.

- **2026-08-05, item 4, THE DIRECTION PASS.** The mechanical half shipped inside
  study_lint. The doctrinal half is now a named Phase 6 step with a required
  artifact, out/<date>/direction_pass.md, because it was a principle for weeks and
  principles get skipped while steps do not.

- **2026-08-05, item 5, the Phase 7 escalation ladder.** Rounds are refinement
  and nothing caps them. What changes at the FOURTH fix verdict is where the run
  looks: the defect is in the brief, not in the sentences it keeps moving, so
  change the brief and hand the writer the draft it already has. Continued fix
  verdicts after that condemn the opening FACT. The four-round threshold is the
  maintainer's, over a draft that escalated at two, because forty words
  legitimately need a few passes and an early fix verdict says nothing. Phase 7
  also now surfaces a READY TO PROMOTE voice pattern in the delivery summary with
  the OUTREACH_CRAFT wording already drafted, so the human approves a diff rather
  than being handed homework. `lengthened` sat at six sends before anyone did.

- **2026-08-05, item 6, scripts/room_reconcile.py.** Cross-checks the room's four
  parallel outputs before they become a study. Killed capability promised anyway,
  non-goal delivered by the roadmap, pick drift, AI role drift. Validated against
  four injected contradictions, caught all four, after four rounds of false
  positives that are recorded in the upgrades ledger because they are the failure
  mode of a checker like this.

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
