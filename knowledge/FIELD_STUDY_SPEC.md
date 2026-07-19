# The Field Study, deliverable contract

What the room actually ships. The Field Study is a real, free, personalized piece
of work we already did FOR the prospect, published as its own page on the site (at
alaskaaihq.com/awesomeproposal/<slug>/) and carried by a short, self-aware email that
holds ONE link to it. It is the whole pitch, because it is the work, not a
description of the work.

The room fills a strict JSON object, out/<date>/study.json, and
scripts/build_study_page.py renders it. Keeping the data and the rendering separate
is what makes the page reliable and every claim traceable. This doc is the contract
for both.

A sibling deliverable embeds into the study page when it earns its place,
out/<date>/demo.html, the demo-builder's self-contained interactive demonstration of
the recommended build. It is published at <slug>/demo/index.html and folded into the
study page as a "See it working" section (build_study_page.py --demo-embed), so the
prospect still has just one link to click. Scripted from verified facts, honest about
being a demo, performing nothing the study did not scope, and audited by the
study-critic like everything else. The study stands alone if the demo fails.

## The through-line

A prospect who opens this should think, quietly, "these people already did the job,
and they were honest with me." Specific and flattering about their business,
grounded in sources, honest about what is hard, and clear about the one thing worth
doing first. Not a brochure. A study.

## Page sections (in order)

1. COVER. "Field Study prepared for {Company}" and the Alaska AI mark. A one-line
   thesis, the single finding, in plain language. The date and a quiet line that
   this was researched and drafted by Alaska AI's agent team, then reviewed by a
   human before it reached them. Owning that we are an AI shop that eats its own
   dog food is the hook, not a thing to hide.

2. THE FINDING. The one insight that makes them lean in, in their words, one short
   paragraph. Sourced. This is the opportunity stated as their outcome, not our
   product.

3. WHAT WE SAW (the homework). Three compact blocks, each sourced.
   - The business, what they do, size, how they make money, in a few honest lines.
   - The real pain, ideally a quote from their own site, a job post open for
     months, or a review, with the source. This is the gold.
   - The field around them, what their Alaska competitors already do with AI, and
     what AI is genuinely doing in their industry right now (real deployments, real
     outcomes, cited). No hand-waving, no "AI is transforming everything."

4. THE OPPORTUNITY. The target job we chose and WHY this one, honestly. High
   importance to them, low current satisfaction, fits where they are going. Name
   the current workaround it competes with (a spreadsheet, a phone, a person). One
   or two sentences on the Four Forces, why a switch is realistic here.

5. THE RECOMMENDED BUILD. The single pick, in plain language, what it does for
   them. Then the honesty that earns trust,
   - The feasibility call. Why AI genuinely fits this part, AND where we would NOT
     use AI because a rule or their existing software does it cheaper and safer.
   - The architecture, a clean SVG diagram (rendered by the builder) of named
     components, their systems it touches, and the data flow. Real names, their
     booking system, their EHR, their phone provider, not "an AI platform."
   - Build vs buy in one honest line, what we buy off the shelf and what we build
     because it is their edge.

6. THE PLAN (PRD highlights, proposal-grade). Kept tight and skimmable.
   - Problem restated in their world, plus the evidence it is real.
   - Goals and non-goals, non-goals explicit and each with a reason (the honest
     scope edge).
   - Success metrics, two to four, each falsifiable, a baseline, a target, and a
     timeframe. If a baseline is unknown, say assumed and name what we would
     measure.
   - Phase-1 scope, a small must-have list and a clearly-labeled later list.
   - What we would need from you, the prospect-side dependencies, their data,
     their people, their sign-offs, stated plainly because unstated ones blow
     timelines.
   - Risks and honest mitigations, including what happens if it underperforms.
   - Open questions, the real unknowns with who resolves them. Signals competence,
     not weakness.

7. THE NUMBERS (honest ROI). Never a single hero figure. See ROI_METHOD.md.
   - A short cost picture, five-year TCO shape with contingency and run cost.
   - Benefits, at most a few, capacity vs cash labeled, phased with an adoption
     ramp.
   - Three scenarios, conservative, most-likely, aggressive, and the line that the
     conservative case still clears the bar.
   - A payback range, not a point.
   - The base-rate honesty, plainly, most AI pilots show no P&L impact, here is
     precisely why this one is built to be in the small share that does, embedded
     in the workflow, owned, and measured. Name the value owner.

8. THE ROADMAP. Now, Next, Later by confidence, each tied to a metric. Phase one is
   the walking skeleton, the thinnest end-to-end slice that runs, carrying the
   fastest hard-dollar win. Staged funding gates, the next phase is earned by the
   last phase's results.

9. THE HONEST PART. A short, plain block naming what could make this not work,
   data that is not ready, adoption that does not happen, an accuracy ceiling,
   latency, cost at volume. A study that names its own failure modes is the one a
   skeptic believes.

10. WHAT THIS IS, AND THE NEXT STEP. One honest paragraph, this study is the free
    version of how we work, a real Field Study. If they want it built, the path is
    the Build, and ongoing it is the Partnership (do not hard-sell, just name the
    ladder). The next step is small, a reply, not a commitment. Point to
    alaskaaihq.com/services for the full picture.

11. SOURCES. Every claim in the study, numbered, with its URL. This footer is the
    proof that the homework is real. If a claim has no source, it is not in the
    study.

## Design and build rules

- Self-contained, no third parties. All CSS inline, the diagram inline SVG, any image
  a data URI. ZERO third-party calls, no CDN, no web fonts fetched, no analytics. The
  ONLY permitted load is the same-site demo iframe (demo/index.html) when a demo
  embeds, and the demo file is itself fully self-contained. The page renders on its
  own and leaks nothing to anyone but the prospect.
- On brand with the public site, dark, restrained, confident. A constellation or
  aurora accent is fine, subtle. It should look like alaskaaihq.com made it. Match
  the palette and type feel of the public site, do not invent a loud new theme.
- House voice everywhere in the visible page. No em or en dashes, no emojis,
  straight quotes. Colons are allowed in the STUDY page (it is a document with
  labeled sections), but the EMAIL that carries it obeys the stricter outreach
  kill-list in OUTREACH_CRAFT.md (no colons, no semicolons).
- Responsive and printable, because it also renders to PDF. No horizontal scroll,
  wide tables and the diagram scroll inside their own box.
- Honest by construction. If the room could not verify a section, the builder omits
  it rather than faking it. A shorter true study beats a padded invented one.

## The email that carries it (see OUTREACH_CRAFT.md for the voice)

Short. The self-aware AI-agent-team opener, honest and a little funny, we are
Alaska AI's agent team, our job was to find standout {segment} companies in {place}
and actually do the work instead of pitching, so we did, it is one link away. Carry
only the headline finding, the one-line recommended build, and the honest ROI range
as a teaser, then point at the one link to the study, the demo is embedded inside it.
One small reply-first ask. It obeys every
punctuation and AI-tell rule. The study does the heavy lifting, the email just gets
it opened.

## The study.json contract (what the room assembles, the builder renders)

The showrunner assembles this from the verified room outputs. Fields map one to one
to the sections above. Anything not verified is left null and its section is
dropped by the builder.

```
{
  "meta": {
    "company": "",           // display name
    "domain": "",            // normalized
    "segment": "",           // tourism | healthcare | anc | other
    "place": "",             // Anchorage, Fairbanks, statewide, etc
    "date": "",              // America/Anchorage YYYY-MM-DD
    "prepared_for_first": "" // decision-maker first name if verified, else null
  },
  "thesis": "",              // the one-line finding
  "finding": "",             // section 2 paragraph
  "homework": {
    "business": "",          // what they do, honest lines
    "pain": { "quote": "", "context": "", "source": "" },
    "competitors": [ { "name": "", "what_ai": "", "source": "" } ],
    "industry_ai": [ { "point": "", "source": "" } ]
  },
  "opportunity": {
    "job": "",               // the target job, their outcome
    "why": "",               // importance high, satisfaction low, strategy fit
    "current_workaround": "",
    "forces": ""             // one or two lines, push/pull vs anxiety/habit
  },
  "build": {
    "name": "",              // plain-language name of the pick
    "what_it_does": "",
    "feasibility": "",       // why AI here, and where we would NOT use AI
    "build_vs_buy": "",      // one honest line
    "architecture": {
      "nodes": [ { "id": "", "label": "", "kind": "system|ai|data|external|user" } ],
      "edges": [ { "from": "", "to": "", "label": "" } ],
      "caption": ""
    }
  },
  "plan": {
    "problem": "",
    "goals": [ "" ],
    "non_goals": [ { "item": "", "reason": "" } ],
    "metrics": [ { "metric": "", "baseline": "", "target": "", "timeframe": "" } ],
    "phase1_must": [ "" ],
    "phase1_later": [ "" ],
    "need_from_you": [ "" ],
    "risks": [ { "risk": "", "mitigation": "" } ],
    "open_questions": [ { "q": "", "owner": "" } ]
  },
  "roi": {
    "cost_note": "",         // TCO shape, contingency, run cost
    "benefits": [ { "benefit": "", "kind": "capacity|cash", "note": "" } ],
    "scenarios": { "conservative": "", "most_likely": "", "aggressive": "" },
    "conservative_clears": true,
    "payback_range": "",
    "base_rate_note": "",    // the MIT/RAND honesty and why we beat it
    "value_owner": ""
  },
  "roadmap": {
    "now": [ { "item": "", "metric": "" } ],
    "next": [ { "item": "", "metric": "" } ],
    "later": [ { "item": "", "metric": "" } ],
    "gates": ""              // one line on staged funding
  },
  "honest_part": [ "" ],     // the failure modes, plainly
  "next_step": "",           // the small ask
  "sources": [ { "n": 1, "claim": "", "url": "" } ]
}
```

Every URL in sources must have been fetched and verified by the fact-checker. The
study-critic audits the finished object against ROI_METHOD and AI_SCOPING before it
renders. If either critic says no, it does not ship, the run degrades honestly and
drafts Talon a note.
