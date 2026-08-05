# Alaska AI - Lead Flow

Private. A daily Claude Code Routine that finds one high-fit Alaska business, puts
two rooms of specialist agents on it, and produces a real, personalized Field
Study, the actual work a serious shop does before a first call, done for free. It
leaves a Gmail DRAFT that carries it, a very short email carrying the study as one
live link, for Talon to review and send. It never sends anything itself.

## The law
Draft only. A human reads and sends every message. Legit process, no AI hype. See
CLAUDE.md.

## One-time setup

   (schema `leadflow`). It is namespaced and reversible, and the study columns are
   an additive, re-runnable migration.
2. Repo. This one, private. The shipped studies and dossiers live under runs/ here,
   the private paper trail. Prospect data never goes in the public repo or site.
3. Routine. At claude.ai/code/routines, create a new routine.
   - Point it at this repo.
   - Paste prompts/ROUTINE_PROMPT.txt as the prompt.
   - Set a weekday or daily schedule and a strong model.
   - Connect Gmail AS docket@alaskaaihq.com (the Google Workspace mailbox on the
     domain). Drafts then land in that mailbox already from the right address, so
     you just read and send. Connecting a different account instead means drafts
     come from that account and you set the sender by hand every time.
4. Test. Click Run now, then read the transcript, open the Gmail draft, and open the
   attached Field Study before trusting it on a schedule.

## How it works
The showrunner run orchestrates two rooms of agents in .claude/agents.
- Research room. Scouts find the day's company, then company-analyst, people-finder,
  competitor-analyst, and industry-analyst learn it cold, and a fact-checker turns
  it into a verified claims file.
- Engineering room. A real discovery-to-delivery process, product-strategist
  (outcome, Jobs To Be Done, opportunity scoring, candidate builds),
  ai-feasibility-engineer (the do-you-even-need-AI conscience), staff-engineer (the
  C4 design), product-manager (the PRD), roi-analyst (an honest ROI range), and
  delivery-lead (the roadmap).
- A study-critic audits the finished study for hype and defaults to reject.
- scripts/build_study_page.py renders it into a single self-contained HTML page
  with an inline architecture diagram, plus a PDF, and outreach-writer writes the
  very short email that carries it.

is documented and sourced in knowledge/ENGINEERING_METHOD.md, AI_SCOPING.md, and
ROI_METHOD.md.

## Tuning
- config/icp.yaml, who it chases and how it scores fit.
- knowledge/ENGINEERING_METHOD.md, AI_SCOPING.md, ROI_METHOD.md, the grounded
  process the engineering room follows.
- knowledge/FIELD_STUDY_SPEC.md, the deliverable contract and the study.json shape.
- knowledge/OUTREACH_CRAFT.md, how the carrier email writes (the no-AI-tells rules
  live here).
- knowledge/LEAD_RESEARCH.md and ALASKA_MARKET.md, how it researches and the market
  it grounds in.

## Layout
- prompts/         routine_instructions.md (master) and ROUTINE_PROMPT.txt
- config/          icp.yaml (targeting and scoring)
- knowledge/       the research notes, the engineering method, and the study spec
- .claude/agents/  the two rooms, the critics, and the writer
- scripts/         build_study_page.py (renders the Field Study)
- runs/            the shipped Field Study and dossier per company, private

## The database

It is git. `ledger/*.json`, read and written only through `scripts/ledger.py`.
Schema and rationale in `db/SCHEMA.md`. Supabase was retired on 2026-08-05.

Structured fields live in the ledger. Large documents (the study object, the
dossier, the rendered page, the demo) live as files under `runs/<date>/<slug>/`
and are referenced by `study_path`, because git stores documents better than a
jsonb column does.

```
python scripts/ledger.py stats          what the dashboard used to answer
python scripts/ledger.py check <domain> exit 1 if we may not contact them
python scripts/ledger.py inbound-next   exit 1 when the opt-in queue is clear
```
