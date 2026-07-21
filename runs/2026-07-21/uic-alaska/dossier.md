# Internal dossier — UIC Government Services (uicalaska.com) — 2026-07-21

Private paper trail for this run. Prospect data, not for the public repo or site.

## Pick and why

Today's lead came from the ANC segment scout, tied for the highest total (22) in a
three-way tie, and won the reachability tie-break. See out/2026-07-21/selection.md
(archived below) for the full shortlist and replacement queue.

**First pick, Alutiiq LLC, was DISQUALIFIED and suppressed.** Research surfaced a
verified reputation conflict, a 2019 False Claims Act settlement over alleged sham
8(a) subsidiaries and a 2020 kickback-scheme non-prosecution agreement, both
directly on point with the proposed compliance/proposal AI build. Suppressed in
leadflow.suppressions (reason: values). Replaced with the next-ranked candidate,
UIC Alaska / UIC Government Services.

**UIC Government Services** passed a dedicated, thorough reputation re-check (no
FCA, fraud, kickback, or debarment findings; a similar-sounding case belonged to a
different, unrelated ANC). Confirmed as a real, operating business from multiple
independent sources (uicalaska.com, bowhead.com, GAO records, Alaska Business
Magazine).

## Research summary

Company: Ukpeagvik Inupiat Corporation / UIC Government Services (Bowhead Family of
Companies). 30+ mostly 8(a)-certified subsidiaries, 300+ prime and subcontracts,
3,000+ employees at Bowhead alone. Direct ANC 8(a) peers Koniag Government Services
and ASRC Federal have shipped and marketed named AI platforms with published
results; Akima also lists AI/ML as a capability line. Chenega and Doyon Government
Group show no public AI capability. Full detail in research.json and claims.json
(archived in out/2026-07-21/, not copied here to keep this folder to the shipped
package plus this summary).

Contact: Lori Schendel, Senior Director of Sole Source Contracts, UIC Government
Services. No email found anywhere fetched, only a phone ((540) 640-1650) and a web
contact form (https://uicalaska.com/our-companies/uic-commercial-services/anc-sole-source-contracting/).
Per Phase 8, this routes the Gmail draft to Talon rather than the prospect directly.

## Discovery and feasibility

Product-strategist mapped the whole business (7 areas) and picked the RFP
shredding/first-draft-assembly opportunity (Ulwick score 15, highest of 4 scored
opportunities) over three other candidates. ai-feasibility-engineer downscoped it
to a checkpointed workflow (never an agent) requiring a mandatory human sign-off
gate and an upfront CUI-classification discovery phase, and killed two other
candidates (cross-subsidiary compliance assistant, full capture-to-proposal
agentic OS) for the reasons in feasibility.json.

## Engineering room

staff-engineer, product-manager, roi-analyst, and delivery-lead outputs are in
out/2026-07-21/engineering.json. Key honest finding: **the conservative ROI case
does not clear** (only the aggressive scenario pays back, 18-24 months; most-likely
does not clear within 5 years; conservative does not pay back at all). This was
disclosed plainly in the study rather than hidden, per HONESTY.

## Ship gate

fact-checker (Phase 6) found 4 unsourced/misframed claims on the assembled study
(the 84hrs/margin-compression stat needed its own source entry, the 4,700-employee
figure needed its own source entry, the ANCSA/1973 founding detail was dropped as
unverified, and the GAO "acquisition workflows" framing was softened to match its
source). All fixed and re-rendered.

study-critic verdict: **fix** (not kill). Two concrete issues, an org-fit question
between Lori Schendel's page (nested under "UIC Commercial Services" in the URL)
and the Bowhead/Government Services entity the study addresses (resolved by citing
her verified title, which itself says "UIC Government Services"), and a payback-
range inconsistency (18-20 vs 18-24 months, reconciled to 18-24). study-critic
explicitly weighed the weak ROI and called it "the study's strongest piece of
honesty, not a defect," consistent with ROI_METHOD's guidance to say so plainly
when only the aggressive case clears.

## Outreach

outreach-writer + lead-critic ran 2 rounds (cap respected). Round 1: ship false, one
fix (split an overloaded sentence). Round 2 (revised): ship true, no further issues.
Final email in out/2026-07-21/outreach.json.

## Delivery

No verified email exists for this prospect, so per Phase 8's "no verified contact"
branch, the Gmail draft was addressed to Talon (Talon.sturgill@gmail.com), subject
prefixed "[needs contact] UIC Government Services", with a note on the contact form
and phone number, and the outreach email body below it for his reference. The
Field Study HTML, PDF, and demo could not be attached directly to the draft (the
Gmail connector's create_draft tool does not support attachments), so the draft
body points to this archived package in the private repo instead. Talon needs to
attach the three files by hand from runs/2026-07-21/uic-alaska/ before sending, or
send the repo files directly.
