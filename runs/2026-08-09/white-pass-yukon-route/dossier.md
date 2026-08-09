# Internal dossier, White Pass & Yukon Route Railway, 2026-08-09

PRIVATE. Prospect data. Never publish this file or anything in this folder except
the designed exception, the study package at docs/awesomeproposal/white-pass-yukon-route/.

## The pick
White Pass & Yukon Route Railway, wpyr.com, Skagway. Segment tourism, fit 23 of 25,
highest of 24 page-verified candidates from four parallel scouts. Dedupe computed by
ledger.py check, clear.

Ownership was checked BEFORE locking because the ICP disqualifies chain outposts.
Klondike Holdings LLC bought it on 2018-08-01. The company's own page calls Survey
Point Holdings the majority partner with affiliates "based in Seattle", while
Carnival's release quotes its own executive calling it "an Alaskan company". Those
pull opposite ways and neither analyst resolved it. RULING: the study never claims
Alaska ownership and never characterises their size at all.

## Contact
Bob Berto, President, bobb@surveypt.com, read in plain text off
https://wpyr.com/company-info/contact-us/ by the people-finder and independently
re-verified by the fact-checker. The surveypt.com domain is consistent with Berto
also being a Survey Point director, and eight other named staff on the same page
carry wpyr.com addresses, which makes it a deliberate published address rather than
a pattern guess. The visible first-initial-plus-surname pattern was deliberately NOT
used to construct anything.

## SECURITY FINDING, DELIBERATELY WITHHELD FROM EVERYTHING PUBLISHED
The company-analyst found a live reservation detail page on their hosted ticketing
system reachable WITHOUT AUTHENTICATION and indexed by a search engine, returning a
specific booking's excursion, departure time, travel date, party composition and
dollar total. No name or payment data was visible.

It is excluded from study.json, demo.html, the carrier email and the published
package. Three reasons. It is a third party's personal booking data and the study
publishes to a public URL, so printing it would AMPLIFY the exposure rather than
report it, which cuts against the PRIVATE DATA law. It is a defect rather than a
fact about how the business operates, which OUTREACH_CRAFT bans as a gotcha.
Responsible disclosure of a security finding is a human decision and belongs in a
private channel, never in a cold marketing document.

The showrunner did NOT re-fetch the URL and it is NOT recorded anywhere in this
repo. Talon is told in the delivery summary so a human can decide whether and how
to tell them. If it is disclosed, the honest channel is a direct note to Bob Berto
or their ticketing vendor, not this study.

## The room
Research room, 4 parallel plus fact-checker. The fact-checker returned FIX with
ELEVEN rejections and named a DRIFT PATTERN running one direction, four
embellishments all making the prospect look more prominent and further behind than
their pages support. All eleven applied into claims.json with the corrections
pinned so they cannot quietly return.

Discovery room mapped TWENTY areas of the business before picking anything. The
strategist scored the voice agent fourth of five at RICE 1.28 and rejected it.

The ai-feasibility-engineer killed TEN capabilities and returned ai_role NONE for
phase one. The most important kill is runtime machine translation of policy text,
because their cancellation terms carry two clauses that are opposites separated by a
preposition and no published staff member is confirmed to read Spanish or Japanese
back.

Engineering room, 4 parallel. room_collect.py assembled engineering.json from
files, all four sections at full contracted key count. room_reconcile exit 0.

## The gates
- room_reconcile exit 0 (after a gate fix, see the retro)
- study_qa 19/19
- study_lint 0 failures 0 warnings
- claim_sweep read, three items judged benign
- study-critic returned FIX with 17 findings, all applied, then re-audited
- lead-critic shipped on round 5, after a BRIEF change at round 4

## What the study-critic caught that nothing else did
The brief's worked example used a Sunday departure decided Saturday evening, which
is ALREADY inside the 24 hour forfeiture window and therefore disproved the study's
own thesis. It also proved direction_pass.md's central claim false, that the drift
pattern had not survived into the prose. It had, in two places the pass had itself
certified as clean. direction_pass.md now records that correction.

## The honest shape of the offer
Phase one has NO AI in it. A form, a server-written timestamp, a queue, an
out-of-hours greeting, a governed policy file. Conservative case nets about $7,346
over five seasons on a $28,800 first-year cheque and pays back in month 50, which
the study calls slow in its own voice. The study prints the 2,960 contact breakeven
at which the reader should decline, and names two cheaper alternatives including one
we are not paid for.
