-- Alaska AI Lead Flow schema.
-- Apply to the Alaska AI Supabase project (alaska-ai-dashboard) with the
-- Supabase MCP apply_migration, or run it directly. Namespaced in its own
-- schema so it never collides with existing data. Fully reversible with
-- drop schema leadflow cascade.

create schema if not exists leadflow;

-- Per-run audit trail. One row each time the routine fires.
create table if not exists leadflow.runs (
  id               uuid primary key default gen_random_uuid(),
  ran_at           timestamptz not null default now(),
  run_date         date not null default (now() at time zone 'America/Anchorage')::date,
  shortlist_count  int,
  status           text not null default 'success',   -- success | no_lead | failed
  notes            text
);

-- The pipeline. One row per company we engage. The dedupe memory of record.
create table if not exists leadflow.leads (
  id                uuid primary key default gen_random_uuid(),
  created_at        timestamptz not null default now(),
  updated_at        timestamptz not null default now(),
  company           text not null,
  domain            text,
  segment           text,               -- tourism | healthcare | anc | other
  location          text,
  status            text not null default 'researched',
                    -- researched | drafted | sent | replied | meeting | won | lost | suppressed
  fit_score         int,
  why_picked        text,
  contact_name      text,
  contact_role      text,
  contact_email     text,
  contact_source    text,
  competitors       jsonb,
  ai_opportunities  jsonb,
  sources           jsonb,
  dossier_md        text,
  -- The Field Study the room produced for this company.
  outcome           text,        -- the business outcome the build moves
  recommended_build text,        -- plain-language name of the one pick
  roi_summary       text,        -- the honest ROI range, one line, never a hero number
  study_json        jsonb,       -- the full study object (see FIELD_STUDY_SPEC.md)
  study_path        text,        -- runs/<date>/<slug>/field-study.html in this repo
  draft_subject     text,
  draft_body        text,
  gmail_draft_id    text,
  outreach_sent_at  timestamptz,
  notes             text,
  run_id            uuid references leadflow.runs(id) on delete set null
);

-- Additive migration for an already-created leadflow.leads (safe to re-run).
alter table leadflow.leads add column if not exists outcome           text;
alter table leadflow.leads add column if not exists recommended_build text;
alter table leadflow.leads add column if not exists roi_summary       text;
alter table leadflow.leads add column if not exists study_json        jsonb;
alter table leadflow.leads add column if not exists study_path        text;

-- Hard dedupe: one company (by domain) can never be picked twice.
create unique index if not exists leads_domain_unique
  on leadflow.leads (lower(domain)) where domain is not null;
create index if not exists leads_status_idx  on leadflow.leads (status);
create index if not exists leads_created_idx on leadflow.leads (created_at desc);

-- Never-contact list: competitors, anyone who said no, bad fits.
create table if not exists leadflow.suppressions (
  id          uuid primary key default gen_random_uuid(),
  created_at  timestamptz not null default now(),
  company     text,
  domain      text,
  reason      text
);
create unique index if not exists suppressions_domain_unique
  on leadflow.suppressions (lower(domain)) where domain is not null;

-- Keep updated_at fresh on leads.
create or replace function leadflow.touch_updated_at()
  returns trigger language plpgsql as $$
begin
  new.updated_at = now();
  return new;
end $$;

drop trigger if exists leads_touch on leadflow.leads;
create trigger leads_touch before update on leadflow.leads
  for each row execute function leadflow.touch_updated_at();

-- Lock it down. RLS on with no anon policies: the public/anon key sees nothing.
-- The routine reaches these tables through the privileged Supabase connector,
-- which is unaffected. This keeps prospect data off any public client.
alter table leadflow.runs         enable row level security;
alter table leadflow.leads        enable row level security;
alter table leadflow.suppressions enable row level security;
