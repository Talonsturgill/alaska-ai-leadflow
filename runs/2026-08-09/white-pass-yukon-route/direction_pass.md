# The direction pass, 2026-08-09

One question, asked of the whole study and nothing else. **Does this make White
Pass look worse than the evidence actually does?**

This run had a named drift pattern before the study was written. The fact-checker
rejected eleven claims and four of them leaned the same way, toward making the
prospect look more prominent and further behind than their pages support. So this
pass is not a formality here, it is checking whether the same lean survived into
the prose after the individual claims were corrected.

Every sentence that asserts something unflattering, what licenses it, and the
verdict.

| # | Sentence | What licenses it | Verdict |
|---|---|---|---|
| 1 | "Your refund clock runs every hour of the week. The only published way to stop it runs forty." | c10 on two independent product pages, c11, c12. Both halves are their own published policy. | **KEEP.** This is arithmetic between two documents they wrote. It is also the whole study, so if it is unfair the study should not ship. It passes the meeting test, an owner would say "we only staff reservations weekdays" out loud. |
| 2 | "There is no online path." | c11, their cancellation page directs to the phone with no alternative offered. | **KEEP.** Stated as an absence on a published page, which is a thing we could see from outside. |
| 3 | "A guest with a Monday departure who decides on Saturday evening has no path that reaches you before their own cutoff passes." | c10, c11, c12 together. | **SOFTENED, and it was.** An earlier draft said the guest "has nowhere to put that decision", which is close to asserting an outcome inside their building. The shipped line is about the published path, which is what we can actually see. |
| 4 | "Nothing records that they tried." | Nothing. This asserted a fact about their internal systems that we could not possibly know from outside. | **CUT.** study_lint caught it as an unverifiable negative and it was right. Replaced with "No published route records when they tried", which is a statement about their published routes and is true. This is the drift pattern in miniature and it got into the figure despite the pattern being named twice earlier in the run. |
| 5 | "The person who would take that call is often on the platform." | c30, their own job posting, which lists train loading and crossing guard duties for the Reservation Agent. | **KEEP.** It is their own description of the role. "Often" is our word and it is doing modest work, since the posting lists it as a standing duty rather than an exception. |
| 6 | "A guest who wants to do the right thing inside your window can read that page end to end and still not learn when somebody picks up." | c11 and c18, both pages carry no hours, c10 carries them elsewhere. | **KEEP, and it is load-bearing.** It is the direct justification for the governed policy file, which is a real deliverable rather than decoration. It is also framed as a gap between pages rather than as carelessness. |
| 7 | "The newest passenger figure you publish yourselves is from 2012." | c35 and the snapshot page. | **KEEP but not promoted.** It sits inside the section explaining why we can't size this, where it is a fact about our evidence rather than a criticism. It is never a headline. |
| 8 | "On the day we looked it returned an unavailable message." | c19, three independent same-day observations. | **KEEP, heavily hedged, and the hedge ships everywhere.** It appears in the study exactly once, inside WHAT WOULD MAKE US WRONG, framed as a limit on our own reading. It is never in the brief, never in the finding, never the opening, and it is explicitly labelled possibly transient. Nothing in the recommendation depends on it. |
| 9 | The FAQ nav link pointing at the blog. | c34. | **CUT ENTIRELY, and it never entered.** claims.json bans it as a headline and OUTREACH_CRAFT bans gotcha openings. It is a website defect, and it appears nowhere in the study, the demo or the email. |
| 10 | "No CIO or IT lead appears on your directory." | An absence, and an unverified inference about capability. | **CUT ENTIRELY.** It appears nowhere in the study. It shaped delivery privately, toward managed low-maintenance components, which is the only legitimate use claims.json permits. |
| 11 | "Skagway's largest private employer." | Nothing. The KTOO article says "one of Skagway's largest employers". | **CUT.** Caught by the fact-checker. Neither the corrected phrase nor the original appears in the study, because the study never needed to characterise their size at all. |
| 12 | "Only 12 percent of tour and attraction operators actively use AI." | c42, a survey of more than 7,000 operators. | **KEEP.** This is about their industry, not about them, and it cuts in their favour. It says nobody in this field has proved this works, which is an argument for measuring before spending. |

## The three questions, applied to the study as a whole

**Could we actually KNOW this from outside their building?** After the fix at row
four, yes, everywhere. Every unflattering sentence in the shipped study is about
something they published or something we observed and dated. The one internal
assertion that slipped through was caught by a script, which is exactly why the
script exists.

**Is the unflattering reading load-bearing, or decoration?** The hours, the
phone-only route and the 24 hour clock are the entire argument and cannot be
removed. The page-level gap in row six justifies a real deliverable. Everything
that was decoration is gone: the stale news page, the stale updates page, the
dock-info page, the FAQ link, the missing IT lead, the four disagreeing season
date ranges. None of those appears anywhere, and each of them would have been an
easy paragraph.

**Would they recognise themselves, or get defensive?** The test case is Bob Berto
reading the first screen. He already knows the office runs weekdays and that
cancellations come by phone, because he approved both. What he probably has not
seen written down is the 40 against 168 next to his own 24 hour refund clause.
That is a recognition rather than an accusation.

## The counter-check, because this pass can also drift the other way

A study that only flatters is as useless as one that only criticises. Three
places where the study argues AGAINST our own interest, and all three shipped:

- The section that says the conservative case pays back in **month 50** and calls
  that slow, in the study's own words, "slower than most things we would sell you".
- The **2,960 breakeven** printed as a callout, which is the number at which the
  reader should decline to buy this. Handing that over is the opposite of drift.
- The honest complication that **easier cancellation can cost them money**,
  because today an unreachable office means a forfeited fare they keep. A
  proposal showing only the upside would have buried it.

## Verdict, and a correction this pass has to make about itself

**The central claim above was WRONG and the study-critic proved it.** This pass
originally concluded that the pattern did not survive into the prose. It did, in
two more places, and both were inside sections this pass had already certified as
clean.

- **The brief still carried "has nowhere to put that decision"**, the exact wording
  row 3 records as softened. The softening reached found.body_2 and never reached
  the brief. That is the fix-the-sentence-not-the-claim failure the run contract
  names by name, committed inside a document written to catch it.
- **The brief's worked example was also arithmetically wrong** in a way that
  disproved the study's own thesis. It used a Sunday departure decided Saturday
  evening, which is already inside the 24 hour forfeiture window, so an open office
  on Saturday would not have helped that guest at all.
- **Row six of the before/after figure carried "Nobody can say how often any of
  this happens"**, an assertion about what White Pass knows internally, and it was
  contradicted twice elsewhere in the same study, which says their own phone log
  settles it in an afternoon. This pass cleared that figure after fixing row four
  and stopped looking at it.

All three are now fixed. Row six reads "No published route leaves a record of how
often this happens", the brief uses the Monday scenario and the softened wording,
and the counters claim now concedes that their phone log can already produce the
out of hours volume.

**The lesson, recorded because it cost a critic round.** This pass checked
sentence by sentence and certified section by section, so once a section was
cleared it stopped being read. The drift pattern does not respect section
boundaries. Fixing row four made row six feel handled, which is the same
mechanism as fixing a quoted span and believing the claim is dead.

What stands after the correction: the study describes a company that published two
policies which do not line up in time. It does not describe a company in trouble,
and there is no evidence that it is.
