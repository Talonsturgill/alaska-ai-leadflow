# This study.json is the OLD schema

Shipped 2026-07-29, before the study rebuild in PR #13 was merged. That change
rewrote both scripts/build_study_page.py and knowledge/FIELD_STUDY_SPEC.md
around a new object shape, notably roi.table and roi.lede_body in place of the
older roi.scenarios and roi.benefits.

Re-rendering this file with the current builder will produce a page MISSING its
ROI figures, the pain quote, the competitor and industry blocks, and several
architecture labels. The builder warns loudly when that happens, which is how it
was caught, so nothing fails silently.

The shipped artifacts in this folder are the record. field-study.html,
field-study.pdf and demo.html were all rendered by the builder as it stood that
day and they are correct as they are. Do not regenerate them.

The published copy at alaskaaihq.com/awesomeproposal/allen-marine-tours/ is a
static copy of that same render and is unaffected.
