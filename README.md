# Alaska AI - Lead Flow

Private. A daily Claude Code Routine that finds one high-fit Alaska business,
puts a room of specialist agents on it, and leaves a deeply personalized outreach
as a Gmail DRAFT for Talon to review and send. It never sends anything itself.

## The law
Draft only. A human reads and sends every message. See CLAUDE.md.

## One-time setup

1. Database. Apply db/schema.sql to the Supabase project alaska-ai-dashboard
   (schema `leadflow`). It is namespaced and reversible.
2. Repo. This one, private.
3. Routine. At claude.ai/code/routines, create a new routine.
   - Point it at this repo.
   - Paste prompts/ROUTINE_PROMPT.txt as the prompt.
   - Include the Gmail and Supabase connectors, and only what it needs.
   - Set a weekday or daily schedule and a strong model.
   - For the from-address to read docket@alaskaaihq.com, add docket@ as a send-as
     alias in the connected Gmail account. Otherwise it drafts from the connected
     account and you set the sender when you send.
4. Test. Click Run now, then read the transcript and the Gmail draft it leaves
   before trusting it on a schedule.

## How it works
The showrunner run orchestrates a room of agents in .claude/agents. Scouts find
the day's company, a research room learns it, a thinking room of three
strategists finds the angle, a skeptic verifies every word, a writer gives it
Talon's voice, and a critic guards against anything generic. Only the showrunner
touches Supabase and Gmail.

## Tuning
- config/icp.yaml, who it chases and how it scores fit.
- knowledge/OUTREACH_CRAFT.md, how it writes (the strict no-AI-tells rules live
  here).
- knowledge/LEAD_RESEARCH.md, how it researches.
- knowledge/ALASKA_MARKET.md, the market context it grounds in.
The Supabase leadflow tables are the memory that keeps it from repeating itself.

## Layout
- prompts/         routine_instructions.md (master) and ROUTINE_PROMPT.txt
- config/          icp.yaml (targeting and scoring)
- knowledge/       research, outreach, and Alaska market notes
- .claude/agents/  the specialist room
- db/              schema.sql (the Supabase leadflow schema of record)
- runs/            optional per-day dossier snapshots
