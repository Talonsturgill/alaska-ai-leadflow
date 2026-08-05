# The database, and it is git

Supabase was retired on 2026-08-05 by the maintainer. This file replaces
`db/schema.sql`, which described the old Postgres schema.

The database is now `ledger/*.json` in this private repo, read and written only
through `scripts/ledger.py`. It ships with the checkout, so it is always
readable, it can never be down, and every change to it arrives as a reviewable
diff attached to the run that made it.

## Why it moved

Three reasons, all of them earned.

1. **The routine kept losing writes it could not retry.** The study object is
   about 25KB of JSON and the only write path available was re-emitting the whole
   thing verbatim inside a tool call. Three consecutive runs owed that column and
   never paid it. That is a machine limitation, not an outage, and it was never
   going to fix itself.
2. **An outage cost inbound priority.** On 2026-07-29 the connector returned
   28P01 for three hours and the run went blind to the consented opt-in queue.
3. **The data was already in git and better there.** Every study, dossier and
   rendered page lives under `runs/<date>/<slug>/`. Supabase held a second,
   staler copy in a jsonb column nobody diffed.

## The shape

**Structured fields live in `ledger/`. Large documents live as files.**

That split is the whole design and it is the part Postgres got wrong for us. A
25KB study object is a document. Git stores documents well, diffs them, reviews
them and never asks you to re-emit one inside a tool call. So the ledger holds a
`study_path` and the document stays a file.

### `ledger/leads.json`
The pipeline and the record of authority for every company we have touched.
Upserted on normalized domain, so a run is always safe to retry.

| field | what it is |
|---|---|
| `company`, `domain`, `segment`, `location` | identity. `domain` is normalized, see below |
| `run_date` | the run that picked it |
| `status` | `researched`, `drafted`, `sent`, `suppressed` |
| `fit_score`, `why_picked` | the ICP total and the reason it won |
| `contact_name`, `contact_role`, `contact_email`, `contact_source` | the verified contact. `contact_source` is the page it was READ on |
| `outcome`, `recommended_build`, `roi_summary` | what the study concluded |
| `study_path` | **the pointer to the documents**, `runs/<date>/<slug>/` |
| `live_url` | the published unlisted study |
| `draft_subject`, `gmail_draft_id` | the draft of record |
| `notes` | anything a later run needs to know |

### `ledger/runs.json`
One row per run. `run_date`, `status` (`success`, `no_lead`, `failed`),
`shortlist_count`, `notes`. This is what `ran-today` reads to stop a double fire.

### `ledger/suppressions.json`
The never-contact list. `company`, `domain`, `reason`, `date`. A domain here is
excluded forever and the reason is written down so a later run does not
re-litigate it.

### `ledger/inbound.json`
The consented Bottleneck Scanner opt-in queue. See INBOUND below.

### `ledger/voice_deltas.json`
Every edit Talon made between what the routine drafted and what he sent. Written
by `scripts/voice_diff.py`, rendered to `knowledge/VOICE_DELTAS.md`.

### `ledger/inbound_watch.json`
The consecutive-skip counter for INBOUND FIRST, kept so a repeated failure to
check the queue escalates loudly rather than passing silently.

## INBOUND, the one thing that needed a real replacement

A public form has to write somewhere, and git cannot accept an anonymous POST.
So intake is a **GitHub issue on this repo labelled `scan-opt-in`**.

That is a real queue. It has an API, timestamps, state, labels, an audit trail
and access control, it is free, and it lives in the same place as everything
else. The scanner backend creates the issue. The run reads it, serves it, and
closes it.

The issue body carries, one per line:

```
domain: example-lodge.com
email: owner@example-lodge.com
company: Example Lodge
```

The run then does:

```
python scripts/ledger.py inbound-add --domain <d> --email <e> --company <c> --issue <n>
python scripts/ledger.py inbound-next          # exit 0 = serve this one, exit 1 = queue clear
python scripts/ledger.py inbound-serve --domain <d>   # then close the issue
```

`inbound-next` computes the answer rather than leaving it to judgement. It
returns the OLDEST unserved opt-in, and it skips anything already suppressed or
already in leads, so a disqualified opt-in can never come back around.

**THE ONE OPEN HANDOFF.** The scanner backend lives in the `alaska-ai-scanner`
repo, which this routine has no access to, and it still writes opt-ins to the old
Postgres `scanner.scans` table. Until someone repoints it at the GitHub issue
queue, opt-ins will not arrive automatically and the queue will read clear. The
change on that side is small, create an issue with the label and the three lines
above instead of an insert. Until it lands, an opt-in can be queued by hand with
`inbound-add`, and `inbound-status` still escalates if the queue goes unchecked.
This is written down rather than papered over because a silently empty inbound
queue is the exact failure the counter exists to catch.

## Domain normalization, used everywhere we dedupe

Lowercase, drop the scheme, drop a leading `www.`, drop any path and trailing
slash, keep the registrable host. So `https://www.Denali-Lodge.com/about`
becomes `denali-lodge.com`. Two records match when their normalized domains
match. Computed in `scripts/ledger.py`, never eyeballed by the model.

## The commands

```
ledger.py normalize <domain>
ledger.py exclude-set [--json]          every domain we may not contact
ledger.py check <domain> ...            exit 1 if ANY is excluded
ledger.py ran-today [--date]            exit 0 if a run already shipped
ledger.py add-lead --json <file|->      idempotent upsert on normalized domain
ledger.py add-suppression --domain --company --reason
ledger.py add-run --status --shortlist --notes
ledger.py inbound-add --domain --email [--company] [--issue]
ledger.py inbound-next [--json]         exit 1 when the queue is clear
ledger.py inbound-serve --domain
ledger.py inbound-skipped --reason      the queue could not be checked
ledger.py inbound-ok                    the queue was checked, clear the counter
ledger.py inbound-status                exit 1 once the skip streak escalates
ledger.py stats [--json]                the analytics the database used to answer
```

## Analytics

`ledger.py stats` computes what the dashboard queried: counts by status and
segment, mean fit score, how many leads carry a verified contact, how many
carry a draft, how many were actually sent, and the inbound queue depth. It
reads the same files everything else does, so it can never disagree with them.

## Backups

The repo is the backup. Every row has full history, every change is attributed
to a commit and a run, and any state is recoverable with `git checkout`. There
is nothing to restore from and nothing to pay for.
