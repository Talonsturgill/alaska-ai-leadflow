# Internal dossier, North Country Charters, 2026-08-02

PRIVATE. Never published. The public package is the study page and demo only.

## The lead

North Country Charters, northcountrycharters.com, 4287 Homer Spit Rd. #10,
Homer, Alaska 99603. Family fishing charter operator, "since 1979" by their own
home page. Four products published: Halibut Fishing, Combo Fishing, Salmon
Fishing, and a Guest Room. Already running FareHarbor.

Contact used: northcountrycharters@gmail.com, a general business inbox verified
verbatim on two of their own pages. Named owners with site-published titles,
Brian Ritchie (Owner and Captain of The Irish) and Kathy Brennan (co-owner and
office manager). No personal address exists for either and none was constructed.

## How it was picked

Four lead-scouts, one per ICP segment, 21 page-verified candidates. All 21
dedupe-checked in code with `ledger.py check`, all clean. North Country and
Alaska Escrow and Title tied at 22. The contract tiebreak settled it,
reachability tied at 5 and offer_fit broke it 5 against 4. Escrow and Title
heads the replacement queue and was never needed.

## What the rooms concluded

The obvious pitch for a Homer charter operator in August is a guest-facing voice
agent. Both rooms killed it independently. The strategist scored it RICE 6.6
against 85. The feasibility engineer killed it outright on four grounds, it
duplicates FareHarbor Agent on a platform they already pay for, its only outcome
evidence anywhere is a vendor-published car-rental case study, 25 to 35
sequential model steps on a booking call puts end-to-end success in single
digits, and the one peer-reviewed tourism study argues against a bot on exactly
the channel where weather and refunds land.

The survivor was downscoped six ways before it was let through. Email only,
voicemail cut because no transcription is evidenced on their line. No deadline
stamping in v1, because days-to-departure can't be derived from an email. The
guest acknowledgement ungated from the classifier. The class narrowed to
cancellation and no-show only. A measurement gate in front of the whole thing.

Ask: 2,800 dollars for a two-week measurement fortnight, with a written
"build nothing further" exit that we would take.

## The finding that shaped everything

Their FAQ cancellation paragraph opens with "We have phenomenal office staff and
we do everything we can to resell cancelled seats" and ends with "IF YOU NEED TO
CANCEL please call us and confirm over the phone with us that you are
cancelling. We don't always see voicemails or emails right away and every minute
counts." It also says "If we can resell cancelled spaces, then we do not retain
the deposit."

Both halves are true at once. A good office and a slow channel are different
problems. The study says channel, never strain, and there is NO first-party
statement anywhere that this business is overwhelmed.

## The drift, which is the real lesson of this run

The first fact-checker rejected eleven research claims and every single one
leaned the same direction, toward making the operational strain look more proven
than the sources support. That pattern, not the individual errors, was the
finding, and it was recorded at the top of claims.json so every downstream room
read it before starting.

It survived anyway, three times, wearing different clothes each time.
- Round 1 of the study critique found it in the GRAMMAR. Prepositions, metric
  baselines, an invented absent owner, a Today column that narrated an office
  nobody watched.
- Round 2 found it in the ARITHMETIC. A three-year avoided commitment sitting in
  a row labelled year one, an undisclosed fifteen percent multiplier, freed hours
  counted as cash, six numeric defects all making the ask look cheaper and faster.
- Round 3 found it in the EXPOSITION. The cost row silently omitted its ongoing
  line, which made an hour of their time look like 62.50 when the model uses 50.

Round 4 shipped. Four critic rounds, two fact-checks.

The biggest single catch was an OMISSION rather than a rejection. The study
quoted the tail of their cancellation paragraph and skipped the head, which is
the same manoeuvre as an ellipsis-trim executed at the other end. Quoting the
head made the study better and made the argument honest.

## The arithmetic, all computed in scripts/roi_math.py

Conservative: cost (2800 + 400 setup + 100 ongoing) x 1.20 = 3,960. Benefit
9,500 x 40 percent = 3,800, plus 180, plus 480, plus 375 of first-touch time,
totals 4,835, cut 15 percent as risk adjustment = 4,110. Recovery 104 percent.
Counting only year one of the avoided build it is 83 percent, which does NOT
clear, and that row is printed in the table beside the 104.

Clock break-even: 19 to 54 recovered seats a season, from 10,925 and 16,800
three-year costs against half-seats at 250, 350 and 450, all three assumed
because no charter rate is published anywhere.

## What we refused to sell

A voice agent. A guest question bot, because FareHarbor already ships one and we
told them to go ask for the free pilot. The standby seat filler as an AI product,
because it is a database query and a text message. The off-season desk as a
chatbot. Five of six candidates cleared at the rules tier with no model in them.

## Replacement queue, unused

Alaska Escrow and Title (22), King of the River (21), Koniag (21), Doyon (21),
Twin Cities Veterinary (19), RB Logistics (19), Associated Insurance (19),
Alaska Property Managers (19), Alaska Executive Search (19), ASRC (19), and ten
more in selection.md.

## Note carried to the next run

VOICE_DELTAS flags "lengthened" as READY TO PROMOTE, four consecutive sends where
Talon warmed and lengthened the closing line. OUTREACH_CRAFT.md was NOT edited.
That promotion is a human decision.

The study shipped at about 3,640 words against a 2,000 to 3,000 budget, which
study_qa reports as a NOTE while passing 17 of 17 enforced budgets. The critic
judged it second-order and named the two places that would give back most
without losing honesty, the feasibility paragraphs and the roadmap Next lane.
