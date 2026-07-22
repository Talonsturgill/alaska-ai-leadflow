# Publish Big Dan's live (one-page study, single-link draft)

Big Dan's was built before the one-page embed and the site plumbing existed, so it is
the one lead that needs a manual republish. Everything is ready in this folder. Run
this from a session (or machine) that has WRITE access to Talonsturgill/alaskaaicarousels.

## 1. Publish the one-page study + demo to the site
The study here (field-study.html) already embeds the demo inline (a "See it working"
section that loads demo/index.html), so the prospect gets ONE page at ONE URL.

    # from a clone of alaskaaicarousels, main branch, up to date
    mkdir -p docs/awesomeproposal/big-dans-fishing-charters/demo
    cp <leadflow>/runs/2026-07-19/big-dans-fishing-charters/field-study.html \
       docs/awesomeproposal/big-dans-fishing-charters/index.html
    cp <leadflow>/runs/2026-07-19/big-dans-fishing-charters/demo/index.html \
       docs/awesomeproposal/big-dans-fishing-charters/demo/index.html
    git add docs/awesomeproposal
    git commit -m "awesomeproposal: Big Dan's one-page study with embedded demo"
    git push        # only docs/awesomeproposal/ is touched, nothing else

Live at https://alaskaaihq.com/awesomeproposal/big-dans-fishing-charters/ after the
Pages deploy (a couple of minutes). The demo is inside that page, and also reachable
at .../big-dans-fishing-charters/demo/ for the full-screen link.

## 2. Swap the Gmail draft to a single link
The live draft (r-7973169061408695746) currently carries two links. Replace it with
the single-link body in out/2026-07-19/outreach.json (or runs/.../ this folder's
sibling record). Gmail has no in-place edit, so create the new draft, verify, then
trash the old one. Never send, draft only.

The one link the body points at:
https://alaskaaihq.com/awesomeproposal/big-dans-fishing-charters/

## Guardrail
Only docs/awesomeproposal/big-dans-fishing-charters/ is ever written. Nothing else in
the carousel repo is touched.
