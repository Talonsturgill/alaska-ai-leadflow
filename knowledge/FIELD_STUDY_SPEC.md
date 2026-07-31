# The Field Study, deliverable contract

What the room actually ships. A real, free, personalized piece of work we already
did FOR the prospect, delivered as one self-contained HTML page (plus a PDF)
published at its own unlisted link on alaskaaihq.com/awesomeproposal/, with the
interactive demo embedded, and carried by a very short email whose one link is
that page.

The room fills a strict JSON object, out/<date>/study.json, and
scripts/build_study_page.py renders it. scripts/study_qa.py then checks the
rendered page against every budget below and exits non-zero if one is missed.
Run it before the study-critic sees anything.

## The reader, and the arithmetic that governs every rule here

One busy person who did not ask for this, is not technical, and is reading cold.

- Nielsen's page-time model: a 4,500 word page earns about 3.7 minutes, which is
  roughly **900 words actually read, about 20 percent**. The job is not to write
  900 words. It is to CHOOSE which 900 get read and put them where the eye lands.
- **81 percent of viewing time falls in the first three screens.** 57 percent above
  the fold. Anything that must land, lands early or not at all.
- 79 percent of readers scan rather than read. Concise beat promotional by 58
  percent on usability; concise plus scannable plus objective beat it by 124.
- Screen reading of expository text is measurably worse than paper and worse still
  under time pressure, which is the exact condition here.

## The through-line

A prospect who opens this should think, quietly, "these people already did the job,
and they were honest with me." The reader is the protagonist. We are, at most, the
mentor. Any passage about our process, our method, or our specialists takes the
lead role away from them and stops the document dead.

## Structure, in this order (Sant's NOSE, the one frame built for unsolicited work)

Need, then Outcome, then Solution, then Evidence. Sant's word for opening on your
own credentials instead: "death moves."

1. **COVER.** The company, one sentence that asserts the finding, the place and the
   date. The thesis is a SENTENCE WITH A VERB, under about 20 words, and it names
   something true only of them. No segment tags, no internal vocabulary.
2. **IN SHORT.** 350 to 450 words, and the most important block in the document.
   It must survive being forwarded alone, because it will be. It carries: what we
   looked at, what we found, what we would build, an honest cost and return range,
   what we could NOT verify, and the ask. A reader who stops here has the whole
   argument.
3. **WHAT WE FOUND.** The complication, in their world, concrete. One callout
   carrying a fact, never a repeated quote.
4. **WHAT IT IS COSTING.** The stakes, in human-scale units. "Two work weeks a
   proposal" beats "84 hours." Where the number is an industry average rather than
   theirs, say so in the same breath and say how we would replace it.
5. **WHAT WOULD CHANGE.** Their future state, in their terms, BEFORE we name the
   build, and the section that carries the document's PRIMARY VISUAL. An
   executive's real question is not how it is wired, it is what work goes away,
   so the before/after ledger outranks the architecture diagram and comes
   earlier. Walk one real task step by step in two columns, Today and After,
   paired row by row. Mark `"gone": true` on the Today steps that disappear;
   those are struck on the TODAY side only, because a strike under After reads
   as something lost. Every After cell must carry real content, never
   commentary on itself. At least one row should be DELIBERATELY IDENTICAL,
   the step we chose not to automate, and the note says why. That row is the
   most persuasive thing in the figure.

   The figure REPLACES prose, it never sits on top of it. Prose that walks the
   same steps is deleted when the figure lands; what survives is what the
   columns cannot carry.
6. **WHAT WE WOULD BUILD.** Opens with `plain_parts`, about 60 words naming the
   moving pieces in plain nouns before any explanation (pre-training, d around
   0.75 to 1.0). Then what it does, the diagram, where AI genuinely fits and where
   we deliberately did not use it, and build vs buy.
7. **WHAT IT COSTS AND RETURNS.** One table, scenario columns and driver rows,
   assumptions in the footer. Never a hero number. If the conservative case does
   not clear, say so in the section heading, not in a footnote.

   Every row carries a PROVENANCE MARK, a 12px glyph LEADING the row label so
   the marks stack into a rail: `verified` (checked against a fetched source),
   `modelled` (computed from stated drivers), `assumed` (a number we chose, and
   named). This is the honesty law rendered as a visual system rather than
   asserted in a sentence, and it is the page's signature device. The key
   explains only the states actually used, so it can never advertise a rigour
   the table did not earn. A table with no `verified` row is a fine and honest
   outcome; it tells the reader plainly that nothing in it is yet a fact about
   their business, which is exactly what a pilot is for. Never mark a row
   `verified` unless the fact-checker verified that specific figure.
8. **HOW WE WOULD START.** Now, Next, Later with a metric each, and what we need
   from them. Staged gates earned by measured results.
9. **WHAT WOULD MAKE US WRONG.** Three or four, each ANSWERED in the same
   paragraph. Never raise a limitation you do not answer.
10. **THE NEXT STEP.** Small, a reply not a commitment.
11. **WHAT WE CHECKED.** Every source, numbered. This is the proof the homework is
    real, and it is also the credibility mechanism: every claim one click from
    its source.

## Budgets, enforced by scripts/study_qa.py

| | Budget | Why |
|---|---|---|
| Words | **2,000 to 3,000** | 4,500 earns ~20 percent read; proposal data shows no evidence longer wins |
| Headings | **12 to 18**, max 3 levels | Butterick; NN/g at most 3 sizes |
| Bullets | **<= 25, never more than paragraphs** | Bullets delete the relationships between ideas. Rows of the before/after figure are parallel by design, so they are reported but not charged |
| Bold | **<= 30 percent** | Bold everywhere is bold nowhere |
| Pull quotes | **zero** | NN/g eyetracking: readers hit one and drop into light scanning |
| Containers | **<= 3 bordered styles** | Everything-is-a-card is why the old one read as a dashboard |
| Measure | **45 to 80 characters** | WCAG 1.4.8, Butterick, Bringhurst |
| Body size | **>= 16px** | The dark-mode reading penalty is worst at small sizes |
| Contrast | **APCA Lc 75 body, 60 captions** | WCAG 2 ratios overstate contrast on dark and pass unreadable greys |

## Writing rules

**Every heading is a full sentence that asserts something.** Run the storyline
test: read only the headings, top to bottom. If they do not tell the whole
argument, the wrong things are headings. This is Minto's rule and it is also the
one with direct experimental support, sentence headlines are recalled better than
topic labels over bullet lists.

**Prose carries relationships. Bullets delete them.** A bullet can only express
"and." If the relationship is because, therefore, despite, or only if, it must be
a sentence. Lists are legitimate only for genuinely parallel items of the same
kind, never nested, never under three items, never over seven, never longer than
one line, and always introduced by a sentence saying what the list is of.

**Do not use the jargon word. Do not use it and define it.** Readers disregard and
resist information containing jargon EVEN WHEN definitions are supplied, and the
penalty is at maximum in low-motivation reading, which is what a cold document is.
Speak THEIR vocabulary precisely, 8(a), past performance, capture, set-aside,
ANCSA, because that is a trust signal. Write OUR domain in plain words. Retrieval,
embeddings, RAG, agentic, precision at k, walking skeleton, red-team: all banned
from the visible page. Say what the thing does.

**Concrete, then bridge, then abstract.** Never open a technical passage with the
mechanism. Open with the specific thing that happens on a Tuesday in their office.

**Human-scale every number.** "Roughly one full-time position" alongside the
dollars. A number nobody can feel does not persuade.

**Caveats interwoven and answered, positive first.** Raising an objection and
answering it beats not raising it (r=.113 credibility). Raising one and leaving it
hanging is WORSE than silence (r=-.049). Caveat-first order kills the gain
entirely (r=.014, not significant). So: make the claim, then the caveat, then the
answer, throughout, and never quarantine all the honesty into a closing section.

**Caveats in our own voice, about our own analysis.** "We could not verify X, so we
assumed Y" moves trust. Generic disclaimers do not.

**Precision with visible assumptions.** A range reads as considered; a round number
reads as a guess. But precision only credentials us if the reader can see why we
chose it, so every driver is stated.

**Never write "cannot". Always "can't".** The rule is absolute and it applies to
every visible string on the page, the demo included. "Cannot" is the formal word
that survives every other contraction rule, and it is what makes a sentence read as
written rather than spoken. A document that has just told a stranger the honest
version of their own numbers should not sound like a memo while it does it.

**Never open a sentence with "And" or "But".** Both announce that the thought was
added afterwards, which is exactly the impression a study built on care should not
give. Join the clause to the sentence before it or give it its own subject.

**Zero errors.** There is no accumulated trust to spend on a typo, and one wrong
fact about their business ends the document.

## Design rules

One self-contained file. All CSS inline, the diagram inline SVG, zero external
calls, renders offline, leaks nothing. Dark and restrained, ONE accent. No em or
en dashes, no emojis, straight quotes. Colons are allowed here (it is a document)
but the carrier email obeys the stricter kill-list in OUTREACH_CRAFT.md.

The diagram is laid out by flow depth, left to right, with no edge labels. Labels
on edges collided and made it unreadable. Keep it under about eight nodes; a
non-technical reader learns nothing from a bigger one except that it looks hard.

A light print theme ships with the page. A dark PDF is unreadable on paper.

## The study.json contract

Anything left null is dropped by the builder. The builder also AUDITS its own
output and warns when any string in study.json never reached the page, because a
renamed key silently dropping an entire section is the worst failure this
pipeline has.

```
{
  "meta": { "company","domain","segment","place","date","prepared_for_first" },
  "thesis": "",                  // cover headline, a sentence with a verb, <20 words
  "brief": "",                   // IN SHORT, 350-450 words, stands alone, \n\n between paragraphs
  "found":   { "title","lede","body","callout_big","callout_note","body_2" },
  "costing": { "title","lede","body","callout_big","callout_note","body_2" },
  "opportunity": {
    "title","lede",
    "outcome_body",              // short, leads INTO the figure
    "before_after": {            // the primary visual, see section 5
      "headline","before_title","after_title","note",
      "rows":[{ "today","after","gone" }]   // gone strikes the TODAY cell
    },
    "after_body"                 // what the columns cannot carry
  },
  "build": {
    "title","lede",
    "plain_parts",               // ~60 words, plain nouns, BEFORE any explanation
    "what_it_does","feasibility","build_vs_buy",
    "architecture": { "nodes":[{id,label,kind}], "edges":[{from,to}], "caption" }
  },              // kind: user|external|system|build|ai|data
                               // build = work WE would do, ai = a gated model layer.
                               // The single accent is spent on build, never on ai, so the
                               // figure cannot imply we are selling a model that is switched off.
  "roi": {
    "title","lede","lede_body",
    "table_caption", "table_head": ["","Conservative","Most likely","Aggressive"],
    "table": [ { "label","cells":["","",""],"emphasis":false,
                 "mark":"verified|modelled|assumed" } ],
    "table_note",                // assumptions live here, in the table
    "payback_big","payback_range","base_rate_note","value_owner"
  },
  "roadmap": {
    "title","lede","body",
    "now":[{item,metric}], "next":[...], "later":[...],
    "gates","need_from_you"
  },
  "honest": { "title","lede","body" },   // each risk ANSWERED in its own paragraph
  "next_step_title": "", "next_step": "",
  "sources": [ { "claim","url" } ]
}
```

Every URL must have been fetched and verified by the fact-checker. The study-critic
audits the finished object against ROI_METHOD and AI_SCOPING, and study_qa.py must
exit 0, before it ships.
