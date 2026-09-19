# The machine backlog

Improvements to the routine itself, each one earned by something that actually
went wrong or cost rounds in a real run. Ordered by leverage, not by effort.

Rules for this file. Nothing goes in it without EVIDENCE from a dated run. No
speculative "would be nice." When an item ships, move it to SHIPPED with the run
that proved it worked. A run may add to this file. A run may not quietly delete
from it.

---

## OPEN

- **2026-09-19, TAKE THIS ONE FIRST. The demo-builder brief says nothing about
  deriving its artifacts, and that cost three review rounds and seven findings
  in one run.** Written, verified, and then DEFERRED rather than shipped,
  because shipping it would have been a fourth machine change against a ceiling
  of three. The diff is below, ready to apply.

  EVIDENCE. The Tatitlek demo took three Codex rounds. Round one, the log named
  a hard-coded owner while the cutoff note followed the viewer's pick, and the
  board clipped on phones. Round two, the recipient counts claimed seven
  approved while the board correctly showed one held, and the log listed four
  of twelve submissions under a caption reading "Every state change carries a
  name and a time". Round three, the chase tile said two rounds when the log
  had honestly emitted none, the log consumed draft state and recorded it as
  approved, the morning note named two bounced items when there could be three,
  and the contributor's mail showed a message to somebody the board said was
  never written to. Seven findings, one defect: an artifact written out by hand
  while its siblings derive from state.

  Rounds two and three existed only because each fix corrected the artifact
  that was caught and left the hard-coded ones beside it. That is FIX THE
  CLAIM, NOT THE SENTENCE failing in a file claim_sweep.py can't read, because
  the claim lives in JavaScript rather than in prose.

  WHY IT IS NOT FIXED HERE, and this is the honest part. The run DID write it,
  logged it as a sixth upgrade, and justified the excess by calling it a
  repeat-offender fix, which the retro law says outranks the ceiling. Codex
  caught that the justification was false. A repeat is a defect RECORDED IN A
  PREVIOUS RUN, and this one had never been recorded anywhere. It cost three
  rounds inside a single run, which is expensive and is not the same thing. So
  the run was over the ceiling with a bad reason, and the ceiling exists
  precisely to stop a run deciding its own judgement outranks a bound it does
  not get to rewrite. It came out.

  It is now recorded. If the next demo repeats it, the repeat rule applies for
  real and it becomes the work rather than a note.

  THE DIFF, verified against the real file before it was reverted. Append to
  `.claude/agents/demo-builder.md`, before `# THE BAR`:

  > **ONE STATE MODEL, AND EVERY ARTIFACT DERIVES FROM IT.** If the demo is
  > interactive, this is the rule that decides whether it survives a reader who
  > pokes at it. Nothing a viewer can see may be written out by hand when the
  > viewer can change what it describes. One state object, one set of derived
  > readers, and every tile, note, log, message and count computed from them.
  > No constant holding a name, a count, a date or a list that the viewer's own
  > choices can contradict.
  >
  > Two traps, both paid for on 2026-09-19. **Derive the whole set, not the one
  > that was caught**, because a finding on one artifact is a finding on every
  > sibling that shares its data. **A draft is not a send**, so if the demo has
  > an approval step, freeze what was approved and let the artifacts read that;
  > an artifact rendered from state the viewer is still editing depicts a send
  > that never happened, which breaks the exact guarantee the demo exists to
  > make.
  >
  > This is an honesty rule, not a polish rule. A demo whose own screens
  > disagree with each other reads as a mock-up dressed as a system, and the
  > study it rides with is selling the opposite of that.

  And to `# THE BAR`, after the existing closing line: "Then they poke at it,
  change something, and every screen still agrees."

  THE STRONGER VERSION, if a later run has ceiling room for it. A brief line
  binds only as well as the agent reads it. The mechanical check is a linter
  that loads the demo's script, sweeps a state space (each recipient held, each
  hand assignment, approved and not), renders every artifact at each point and
  fails on any disagreement between them. The 2026-09-19 run drove exactly that
  by hand in node and it found all four of round three's findings, so the
  approach is proven and only the harness is missing.

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

- ~~**2026-08-07, the shell working directory drifts and nothing notices.**~~
  **CLOSED 2026-08-09 on its second appearance, see SHIPPED.** It recurred in the
  middle of Phase 4 that day, exactly as described below.

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

- ~~**2026-08-08, the four Phase 4 agents can't write their own output, so the
  showrunner retypes it.**~~ **CLOSED 2026-08-09 on its second appearance, see
  SHIPPED.** One thing the fix taught us is written into the SHIPPED entry: agent
  definitions are resolved from the registry loaded at SESSION START, so a
  frontmatter change cannot take effect in the run that makes it.

  EVIDENCE. The run contract says the room's four outputs go into
  engineering.json VERBATIM, and room_reconcile fails the run if they do not,
  because on 2026-08-05 a showrunner summary dropped six of nine keys from a
  design and eight of nine from an ROI, and the fields it dropped were the
  caveats. staff-engineer, product-manager, roi-analyst and delivery-lead all
  carry `tools: Read`. demo-builder carries `tools: Read, Write`. So the four
  agents whose output MUST be persisted verbatim are the only ones that cannot
  persist it, and the showrunner transcribes roughly 40KB of JSON by hand.

  That transcription IS the mechanism the 2026-08-05 defect came through. A
  gate now catches the failure, which is better than nothing, and the cheaper
  answer is to remove the step that produces it.

  WHY IT IS NOT SHIPPED. Adding Write to four agent definitions is one line
  each and it is not the risky part. The risky part is that every one of those
  agents would then need a briefed output path, the showrunner would need to
  handle a file that did not appear, and room_reconcile's shape check would be
  reading files written by a different actor. Doing that in the tail of a run
  that has already drafted is how a working pipeline breaks. It wants its own
  session with the four agents exercised end to end.

- **2026-09-19, the two Phase 3 agents still can't persist their own output.**
  NOT BLOCKED, and deliberately deferred ONCE under the retro's ceiling of three.
  It is eligible to be fixed on the next run and should be the first thing that
  run picks up.

  EVIDENCE. product-strategist and ai-feasibility-engineer both carry
  `tools: Read`. Both said so out loud this run, the strategist opening its
  handback with "Write is disabled in this session, so I can't save to
  out/2026-09-19/discovery.json", and the showrunner transcribed roughly 40KB of
  JSON by hand across the two of them, twice for the engineer because its pick
  was re-run on corrected GovEagle facts. That transcription is the exact
  mechanism the 2026-08-05 summary defect came through, which is why the four
  Phase 4 agents got Write and a PERSIST block on 2026-08-09.

  WHY IT WAS NOT FIXED THIS RUN. The retro ceiling is three and this run already
  shipped three verified gate fixes plus two ship-blocking renderer and
  arithmetic changes. It is also the lowest-value of the candidates, because
  room_collect.py already exists as the pattern and the hand transcription was
  checked against the agents' returned JSON both times. And the in-flight
  discovery recorded in the 2026-08-09 SHIPPED entry applies: agent definitions
  resolve from the registry loaded at SESSION START, so adding Write could not
  have taken effect in the run that made the change anyway.

  WHAT WOULD FIX IT. `tools: Read, Write` on both agent definitions, a PERSIST
  block naming the output path, and a showrunner fallback for a file that does
  not appear, copying exactly what the four Phase 4 agents already do.

- **2026-09-19, dup_clause is unusable against the rendered study page.**
  SMALLER THAN A RUN, and arguably not a defect at all.

  EVIDENCE. Run against out/<date>/field-study.html it returned 77 duplicate
  clauses, every one of them on "line 231", because build_study_page emits the
  entire document body as a single 38,573-character line. The tool's own rule is
  that one line is one edit unit and that cross-unit repetition is normal in a
  document and is not flagged, so the renderer collapses that rule and every
  legitimate cross-section repeat gets reported. The brief is REQUIRED by
  FIELD_STUDY_SPEC to restate the body so it survives being forwarded alone, so
  those repeats are the contract working as designed. Pointed at the demo, which
  is what the tool was built for on 2026-08-10, it is clean.

  WHY IT IS NOT SHIPPED. The contract does not list dup_clause as a Phase 6
  gate, and pointing it at the rendered page was the showrunner's choice rather
  than a required step, so this is a usability trap rather than a broken check.
  The fix if it ever earns one is to run it over study.json's strings, where the
  edit units are real.

- **2026-09-19, study_qa counts a figure caption as PROSE.**
  A QUESTION ABOUT A BAR, so it is not a run's to change.

  EVIDENCE. The prose-versus-structure split says in its own comment that
  "table cells, source lines and figure labels are scanned, not read", and its
  structural regex matches `<td>`, `<th>`, `<ol class="srcs">`, `<text>` and
  `<caption>`. It does NOT match `<p class="figcap">`, which is what the
  architecture diagram and the embedded demo both use. So every figure caption
  this renderer emits is charged against a reading-time budget the comment says
  it should be outside of. On this run it cost 25 words, which was the whole
  difference between the embedded page passing at 2,986 and failing at 3,011.

  WHY IT IS NOT FIXED HERE. It was found while the embedded page was failing
  the gate, and changing a budget gate to make the current artifact pass is the
  exact move THE ITERATION LAW forbids: the standard never bends to make a loop
  converge, the artifact bends. So the artifact was trimmed instead and the
  question is written down cold, for a run that is not under the gate at the
  time. It also shifts the count for every past study, which is a decision
  about a bar rather than a bug fix.

- **2026-09-19, room_reconcile's money sweep counts ISO standard numbers.**
  A false positive in a WARN, so it cost nothing this run, and it is exactly
  the failure mode that teaches a reader to skim past a warning.

  EVIDENCE. The final reconcile printed `WARN many distinct money figures
  across the room's outputs (13)` and listed `9001` among them. There is no
  such fee anywhere in the room. It is `ISO 9001:2015`, one of the five
  certifications Tatitlek publishes, and it appears twice in study.json, once
  in a roadmap item and once in a verified claim. The sweep matches a bare
  four-figure number with no currency mark in front of it.

  WHY IT IS NOT FIXED HERE. The fix is small, require a currency mark or a
  money word adjacent to the figure, but the check is a fee-drift detector and
  tightening its matcher is the kind of change that wants its own negative
  case, a genuine fee written bare as `we would charge 9000`, tested against
  the tightened rule. This run had spent its upgrade ceiling and was inside the
  delivery gate. Cheap, isolated, and better done cold.

- **2026-09-19, `ledger.py stats` splits one segment across three rows.**
  The by-segment cut is the one number the stats command exists to give, and
  right now it can't be read.

  EVIDENCE. `stats` after this run's add-lead prints nine segment rows for
  four real segments. Tourism is `tourism` 5 and `Tourism and visitor
  industry` 4. ANCs are `anc` 4 and `Alaska Native corporations and tri` 3.
  The catch-all is `other` 2, `other labor-scarce or paperwork-he` 2 and
  `Other labor-scarce or paperwork-he` 1, which is three spellings of one
  thing including a case difference. Healthcare is split two ways. Some rows
  predate config/icp.yaml's current segment names and some differ only in
  case. `add-lead` validates the segment against icp.yaml, which is why this
  run's first attempt was rejected and corrected, so new rows are clean and
  only the history is not.

  WHY IT IS NOT FIXED HERE. It is a data migration over ledger/leads.json,
  which is the record of authority for every company ever touched, and it
  wants its own run and its own before-and-after count rather than a
  dictionary bolted onto the stats printer. Do it as a one-off normalizer
  that maps each historical spelling to the icp.yaml name, asserts the lead
  count is unchanged, and leaves the diff reviewable. Nothing depends on the
  segment for dedupe, so nothing is at risk while it waits.

The rules at the top still bind: evidence from a dated run, no speculative "would
be nice", and a run may add but may never quietly delete.

---

## SHIPPED

- **2026-08-09, the room writes its own output.** scripts/room_collect.py plus
  Write and a PERSIST block on the four Phase 4 agents. Closed on its SECOND
  appearance. Verified with negatives first, a missing file and a 2-of-9-key
  summary both refused while good sections still collected. IN-FLIGHT DISCOVERY
  worth more than the fix, agent definitions load at session start, so the
  frontmatter half could not take effect in the same session and the collector's
  fallback carried the run. That is the negative case exercised for real.

- **2026-08-09, room_reconcile failed two documents for obeying the contract.**
  It now reads the parent object, so a killed capability named in a label field
  whose sibling refuses it is compliance, and it understands deferral containers
  and deferral verbs. Verified by confirming a genuine promise still fails, and
  that a sibling which PROMISES rather than refuses still fails.

- **2026-08-09, the shell working directory drift is now harmless.**
  scripts/_paths.py resolve(), wired into the eight path-taking scripts. Closed on
  its SECOND appearance, the day it bit a run for the second time. Verified by
  running study_lint and room_reconcile from the sibling checkout with
  repo-relative paths, both exit 0, then re-running from the repo root, both still
  exit 0.

- **2026-08-08, the prose budget is addressable.** scripts/prose_budget.py
  attributes the rendered prose count back to the study.json field that
  produced it, by rendering once per field with a sentinel substituted, so it
  re-implements neither the word counter nor the template. It also separates
  NOT ON PAGE from structure, which catches the renamed-key defect for free.
  Closed on its SECOND appearance, per the rule that a twice-deferred item is
  the work. Testing it on real data found two bugs in the first version, both
  of which would have produced an authoritative wrong number.

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
