#!/usr/bin/env python3
"""Assemble study.json for Major Marine Tours, 2026-08-10.

Sources are pulled FROM claims.json rather than retyped, because the fact-checker
named a sharpening reflex on this run: every quote the research package rebuilt
from memory got rebuilt in the direction of the point it was making.
"""
import json, os

BASE = "/home/user/alaska-ai-leadflow/out/2026-08-10"
claims = json.load(open(os.path.join(BASE, "claims.json")))
eng = json.load(open(os.path.join(BASE, "engineering.json")))

# ---- sources, built from claims.json so no URL can appear that was not verified
src = []
seen = set()

# FIELD_STUDY_SPEC makes sources[] the claim-to-source map, every claim one
# click from its source. The reverse also binds: an entry asserting a claim the
# study never makes is a bare assertion backing nothing, and two of these were
# the website defects claims.json restricts to evidence at most, which left them
# sitting in the list as criticism with no argument attached to it.
DROPPED = {
    # the 12-hour online booking cutoff, trimmed out of the body
    "https://majormarine.com/book-now/3-5-hour-kenai-fjords-wildlife-cruise-reservation/",
    # Tom Tougas and the First National Bank chair, trimmed out of the body
    "https://www.fnbalaska.com/team/tom-tougas/",
    # the owner's awards, trimmed out of the body
    "https://majormarine.com/our-company/",
    # WEBSITE DEFECT, restricted by claims.json, and the body no longer says it
    "https://majormarine.com/book-now/6-hour-kenai-fjords-national-park-morning-cruise-reservation/",
}

def add(claim, url):
    if url and url not in seen and url not in DROPPED:
        seen.add(url); src.append({"claim": claim, "url": url})

_FAQ = "https://majormarine.com/faq/"
for c in claims["verified_company_facts"]:
    add(c["claim"], c["url"])
# sources[] is the claim-to-source map and the map has to name what the body
# actually draws off each page, not just the first fact taken from it. On the
# first pass this treatment was applied to the FAQ alone, which left the
# refund page backing one of the six clocks it carries and the callout's
# 0.6 miles, the biggest type in the document, named nowhere. Every line below
# is transcribed from a verified claim in claims.json, never restated from
# memory, because the fact-checker named a sharpening reflex on this run.
RETITLE = {
    # accessibility by vessel (c20) plus the parking contradiction (c36).
    # Rain or shine went out with the trim and is no longer claimed.
    _FAQ: ("Wheelchair accessibility differs vessel by vessel and no vessel takes a motorized "
           "wheelchair. A vegetarian sandwich on the 6 Hour, 7.5 Hour and 8.5 Hour cruises must be "
           "requested at the time of reservation, and guests stay aboard for the whole cruise. This "
           "page prices parking at $10 per vehicle per day, which is the first half of the "
           "contradiction."),
    # c4, c6, c7, c8, c5, c9. The body draws all six off this one page.
    "https://majormarine.com/refund-policy/": (
        "Three refund clocks, 72 hours cruise-only, 7 days on a hotel package and 21 days on a "
        "transportation package. One free date change up to 24 hours prior and then a fee per "
        "person, a 3 percent card processing fee retained on cancellations, and no-shows "
        "completely non-refundable."),
    # c13, c14, c15, c16, c17.
    "https://majormarine.com/seward-check-in/": (
        "An advance reservation is required for the shuttle, and the page asks guests to call at "
        "least 24 hours ahead. The shuttle is excluded from the 8:00 a.m. cruise. The terminal "
        "loop runs a 165-minute window on a 15-minute headway, the terminal distances are 0.6 and "
        "0.8 miles, and all cruises board at the Harbor 360 Hotel office. This page prices public "
        "parking at $15 for the day, against the FAQ's $10 per vehicle per day."),
    # c24 plus c26, the roles named first on their own list.
    "https://majormarine.com/employment/": (
        "About 60 seasonal employees in Seward, hired in a window closing in April, with Customer "
        "Service/Sales Staff first on the list of seasonal roles, ahead of deckhands, engineering, "
        "dock support and cooks."),
    # c27 plus c28.
    "https://majormarine.com/": (
        "2026 cruise season runs March 7th to October 11th, on a locally owned family company of "
        "over 30 years."),
    # c2. The verified quote carries no annual scope, so "year round" comes off.
    "https://majormarine.com/contact-us/": (
        "Customer service hours are 8:00 a.m. to 6:00 p.m., seven days a week."),
    # c39. This page is reached first by the Seward-only negative the body never
    # asserts. It carries the three verified adult fares instead, which back the
    # one table row marked verified and the cost per refund error behind it.
    "https://majormarine.com/all-cruises/": (
        "Adult fares of $149.00 on the 4 Hour, $239.00 on the 6 Hour and $309.00 on the 8.5 Hour "
        "Northwestern Fjord, the three figures behind the error cost."),
}
for _e in src:
    if _e["url"] in RETITLE:
        _e["claim"] = RETITLE[_e["url"]]


for k in ("i1", "i5", "i7"):
    for c in claims["verified_industry_claims"]:
        if c["id"] == k:
            add(c["claim"], c["url"])
_SHUTTLE_FIX = "An advance reservation is required for the shuttle, and the page asks guests to call at least 24 hours ahead."
for _e in src:
    if _e["claim"].startswith("The shuttle must be added by phone"):
        _e["claim"] = _SHUTTLE_FIX
add("About 95 percent of enterprise generative AI pilots produce no measurable P and L impact.", "https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/")
add("More than 80 percent of AI projects fail, about twice the rate of non-AI IT.", "https://www.rand.org/pubs/research_reports/RRA2680-1.html")
add("2026 season dates and the locally owned family description.", "https://majormarine.com/")
add("Eight vessels with published passenger capacities.", "https://majormarine.com/our-vessels/")
add("Six shoreside leaders and thirteen captains, with tenures.", "https://majormarine.com/meet-the-team/")

# Two claims the body makes had no entry at all. The departure count is COMPUTED
# rather than published, so it is worded as computed and every page the
# arithmetic ran over is one click away.
add("Seven departures fall inside their published date ranges on August 10th, 2026, counted across four tour "
    "pages. Two are on this one, the 8:00 a.m. morning sailing and the 11:30 a.m., at a $239.00 adult fare.",
    "https://majormarine.com/tour/6-hour-kenai-fjords-national-park-cruise/")
add("Published season, the $309.00 adult fare, and an 8:30 a.m. departure, one of the seven counted.",
    "https://majormarine.com/tour/8-5-hour-northwestern-fjord-cruise/")
add("Published season and a 9:30 a.m. departure, one of the seven counted.",
    "https://majormarine.com/tour/7-5-hour-kenai-fjords-national-park-cruise/")
add("Published season, the $149.00 adult fare, and three departures on the run date, 10:00 a.m., 12:30 p.m. and 3:00 p.m.",
    "https://majormarine.com/tour/4-hour-kenai-fjords-wildlife-cruise/")

# The room's output stays verbatim in engineering.json. The STUDY page may not carry
# banned jargon, so the labels are translated here, at render time, and only here.
arch = json.loads(json.dumps(eng["design"]["architecture"]))
_swap = {
  "GATED OPTION, not funded, snippet retrieval": "GATED OPTION, not funded, looks things up in your other pages",
  "never reach a retriever": "never reach the part that looks things up in your other pages",
  "enforced by a contract test rather than by a prompt":
      "enforced by a test that fails the build if it ever happens, rather than by an instruction anyone can override",
  "Red list router, runs first": "Question sorter, runs first",
  "Decision table, four branches, default deny":
      "Decision table, four branches, no rule means no answer",
  "Policy canon and vessel map, dated and season scoped": "One dated policy source and the vessel map, season by season",
}
for n in arch["nodes"]:
    n["label"] = _swap.get(n["label"], n["label"])
for k, v in _swap.items():
    arch["caption"] = arch["caption"].replace(k, v)
arch["caption"] = arch["caption"].replace("red list router", "question sorter").replace("policy canon", "dated policy source")
# The search gate has three homes and this was the third wording. later[1].metric
# and roadmap.gates both say three numbers, so this one says three numbers too.
arch["caption"] = arch["caption"].replace(
    "only ever discussed if the miss log clears a number agreed in writing beforehand",
    "only ever discussed if the miss log clears the three numbers agreed in writing beforehand")
# The sorter writes its own line, so a question the table was never built for is
# counted rather than lost, which is what gives the search gate a denominator.
arch["edges"].append({"from": "router", "to": "misslog"})
arch["caption"] = arch["caption"].replace("The funded path has no model in it. ", "")
arch["caption"] = arch["caption"].replace(", which is built from Major Marine's own published pages, carries", ", which carries")
arch["caption"] = arch["caption"].replace(" for the agent to read out loud", "")
arch["caption"] = arch["caption"].replace(
    "It writes only to the miss log.",
    "It writes only to the miss log, and the sorter counts every question and logs the ones it has no "
    "branch for, so questions outside the table get counted rather than lost.")

_MM = sum(1 for _e in src if "majormarine.com" in _e["url"])
_MM_WORD = {13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",
            18:"eighteen",19:"nineteen",20:"twenty"}.get(_MM, str(_MM))

study = {
  "meta": {
    "company": "Major Marine Tours",
    "domain": "majormarine.com",
    "segment": "Alaska visitor industry",
    "place": "Seward, Alaska",
    "date": "August 10th, 2026",
    "prepared_for_first": "Colby Lawrence"
  },

  "thesis": "Major Marine rebuilds its reservations desk every spring and hands it four rule sets to hold in mind.",

  "brief": (
    "You employ about 60 seasonal people in Seward, your peak hiring runs January 15th to April 15th, and Customer "
    "Service/Sales Staff is first on your own list. So the desk that answers your phone from 8:00 a.m. "
    "to 6:00 p.m., seven days a week, is largely rebuilt every spring.\n\n"
    "That desk applies rules you have already written down and written down correctly. Three refund clocks, depending "
    "on what is inside the booking. A shuttle with two conditions and one departure it does not serve. Wheelchair "
    "access that depends on which vessel is running that sailing. A vegetarian meal that has to be asked for at "
    "the moment of booking.\n\n"
    f"We read about twenty of your public pages and drew on {_MM_WORD}, listed at the end. What we found is not a "
    "problem with your policies, which are exact. "
    "It is that four questions carry a high cost when the answer is wrong, and nothing you publish shows anyone "
    "downstream to catch a mistake on three of them, the fourth at the gangway, which is already too late.\n\n"
    "What we would build first has no AI in it. A decision table over those four questions, tested against every "
    "possible input, handing the agent the published sentence to read out loud.\n\n"
    "Then the honest part, and it changed the ask. We priced that build at eighteen thousand dollars. Across three scenarios it returns between a sixth and about three times its five-year cost, "
    "and it pays back only in the most aggressive one. We can't recommend it today, because the thing it would "
    "improve has never been counted.\n\n"
    "So we are proposing four thousand five hundred dollars for a stage with no software in it. One dated policy "
    "source, the vessel map that exists nowhere in one place, a specification for logging what your desk gets "
    "asked, and a paper tally sheet you can start this week. It recovers about forty three percent of its five-year "
    "cost, thirteen percent counting hard cash only, because most of the rest is time freed inside shifts you are "
    "already paying for rather than money you stop spending. It does not pay back either.\n\n"
    "What we could not verify: how many people work that desk, how many questions it takes, and how often the wrong "
    "clock gets quoted. Every benefit figure here rests on a named assumption, and the free tally sheet is what "
    "starts replacing them."
  ),

  "found": {
    "title": "Your rules are exact, and they are spread across three pages and one person's memory",
    "lede": "Nothing here is a problem with your policies. It is where the answer lives at 4:40 p.m. on a Sunday.",
    "body": (
      "A cruise-only reservation is refundable up to 72 hours before departure. Add a hotel and the clock becomes 7 "
      "days. Add motorcoach or train and it becomes 21 days. A date change is free once, up to 24 hours before "
      "departure, then $15 per person.\n\n"
      
      "The shuttle needs an advance reservation, your page asks for 24 hours notice rather than requiring it, and it "
      "is not available for the 8:00 a.m. 6 Hour cruise. Wheelchair access is first deck and inside the main cabin "
      "only, it differs by vessel, and no vessel takes a motorized wheelchair. A vegetarian sandwich on the three "
      "long cruises has to be asked for at the time of reservation, not after."
    ),
    "callout_big": "Four",
    "callout_note": "rule sets a first-season agent has to apply correctly, spread across your refund policy page, your FAQ and your check-in page.",
    "body_2": (
      "On August 10th, seven departures leave the Harbor 360 office in a single day. In the weeks after a March "
      "opening, the person answering the phone is often somebody in their first weeks. They are not failing to read. They are deciding "
      "which of three pages holds the answer, with somebody on the line."
    )
  },

  "costing": {
    "title": "Three of these four questions have nothing published that catches a wrong answer before it reaches a guest or the bank",
    "lede": "The refund clock costs cash. The shuttle and the gangway cost a guest a day, and the sandwich costs them lunch at sea on a boat they can't get off.",
    "body": (
      "Quote the 72-hour cruise-only clock to a guest who holds a 21-day transportation package, and you refund money "
      "you did not owe, on a booking whose train or motorcoach seat you may already be committed to. Nobody catches "
      "that in the moment, because the wrong clock sounds as authoritative as the right one. It surfaces after the "
      "money has moved. We assume no supervisor signs a refund before it is issued, because nothing published says "
      "one does. If somebody already does, that line of the model collapses and the sheet shows it inside nine "
      "weeks. The same error the other way, refusing a refund your policy grants, is one your own page "
      "settles against you."
    ),
    "callout_big": "0.6 miles",
    "callout_note": "from the cruise terminal to the Harbor 360 office, a walk the terminal loop covers.",
    "body_2": (
      "Every link in the shuttle chain is your own published rule. A guest is told the shuttle covers "
      "the 8:00 a.m. 6 Hour cruise. It doesn't. The terminal loop runs 7:00 a.m. to 9:45 a.m., a fallback for a "
      "cruise-ship guest and none at all for one who parked. A guest who misses the sailing is a no-show, and a "
      "no-show is completely non-refundable.\n\n"
      "We want to be precise, because it is easy to dress up as lost revenue and it isn't. You keep the "
      "fare. What it costs you is goodwill, on a brand whose position in that harbour is being the locally owned "
      "family company. The accessibility question is the only one of the four we can see caught at all, and it "
      "gets caught at the gangway, which is the latest a catcher can arrive."
    )
  },

  "opportunity": {
    "title": "What changes is where the answer comes from, not who decides",
    "lede": "One real call, walked step by step. The last row is the one we deliberately left alone.",
    "outcome_body": (
      "A guest calls to move a booking with a hotel and the train in it. Here is that call today, and with one "
      "dated source behind it."
    ),
    "before_after": {
      "headline": "One call to move a booking",
      "before_title": "Today",
      "after_title": "After",
      "note": (
        "The last row is identical on purpose. Whether to grant an exception is a judgement about a guest and about "
        "your business, and it should stay with a person who knows both. We are not proposing to automate it, and any "
        "tool that offered to would be selling you something worse than what you have."
      ),
      "rows": [
        {"today": "Guest asks whether they can still move it and what it will cost.", "after": "Same question, same phone call.", "gone": False},
        {"today": "Agent opens the refund policy page and reads past three different clocks.", "after": "Agent enters what the booking contains.", "gone": True},
        {"today": "Agent works out which clock applies to this particular booking.", "after": "The lookup returns the clock, the fee, and the sentence it came from.", "gone": True},
        {"today": "Agent puts the guest on hold to ask somebody who has done a few seasons.", "after": "Agent reads the published sentence aloud.", "gone": True},
        {"today": "A veteran stops what they are doing at the counter.", "after": "The veteran is not interrupted.", "gone": True},
        {"today": "If nobody is certain, the agent makes a call and hopes it was right.", "after": "No published rule for this case, so it goes to a named person by design.", "gone": True},
        {"today": "You decide whether to make an exception.", "after": "You decide whether to make an exception.", "gone": False}
      ]
    },
    "after_body": (
      "The strongest independent measurement we have is about a "
      "different tool, an AI assistant rather than a lookup, so read it for direction only. It studied 5,179 support "
      "agents and found a 34 percent gain for novices with minimal impact on experienced staff. That is where help of "
      "this shape goes, so this is built for your March cohort and not for people who have already done ten or "
      "twenty seasons.\n\n"
      "A day-cruise operator in Akaroa, New Zealand, running a bot wired "
      "to their booking system, reports ten staff hours saved a month and sixty percent of questions answered. That "
      "is their vendor's own case study with the customer named. The same vendor's homepage says ninety-five "
      "percent, so the gap between what a vendor advertises and what its named customer measured is what to watch "
      "when somebody sells you one of these."
    )
  },


  "build": {
    "title": "What we would build first has no AI in it",
    "lede": "The four expensive questions are finite and already answered on your own pages.",
    "plain_parts": (
      "A dated copy of your own policy pages, contradictions settled. A list of which boat runs which "
      "departure. A lookup that hands back the answer with the "
      "sentence from your page to read out loud. A log of every question it could not answer, "
      "and the paper sheet."
    ),
    "what_it_does": (
      "An agent picks the branch, enters what the booking contains, and gets the answer with its source. Anything with "
      "no published rule escalates to a named person and writes a log line. It never guesses."
    ),
    "feasibility": (
      "This is the rare build whose acceptance bar can be certified. The input space is finite, so "
      "the table can be tested against every possible combination and shipped at 100 percent agreement with your "
      "published policy rather than at a percentage from a sample.\n\n"
      "Where we would not use AI: not on refund clocks, not on the change fee, not on a wheelchair question, not on "
      "shuttle eligibility, not on a dietary window. Those are finite, already written, and expensive when "
      "wrong.\n\n"
      "We would not put a voice agent on your reservations line at any price. That line is a revenue channel, packages "
      "are bookable by phone only, and the callers who most need a person are the ones a machine would meet first."
    ),
    "build_vs_buy": (
      "Hosting, access control and the log store are bought. The decision "
      "table is built, because it encodes your policy and nobody sells that. What we would not build yet is search "
      "over the rest of your pages. They contradict each other in more than one place, and search can't resolve a "
      "contradiction. It returns whichever passage ranks higher, and a citation guarantees where a sentence came "
      "from, never that it is right."
    ),
    "architecture": arch
  },

  "roi": {
    "title": "The build only pays back under our most aggressive assumptions and the small stage never does, so we are asking for the small one and telling you why",
    "lede": "Every driver below is an assumption, because the thing this would improve has never been counted.",
    "lede_body": (
      "Three scenarios on the eighteen thousand dollar build. Only the aggressive one pays back, on an error "
      "frequency nobody has counted.\n\n"
      "Three of the four benefit lines are capacity rather than cash, kept apart in the table. Your crew is hired in a "
      "fixed window for a fixed season, so there is no hire to defer and no backfill to avoid. Reading freed hours as "
      "a smaller payroll would make this look twice as good as it is.\n\n"
      "One thing about the four thousand five hundred dollar figure. We did not scope a stage and then price it. We "
      "worked out what a conservative benefit could carry and cut the scope to fit under that ceiling. Three drivers "
      "are cut back against the larger build, the hours recovered by more than half and the refund errors prevented "
      "from fifty percent down to twenty. One moved the other way and you should see that too. The pre-season "
      "reconciliation is credited at sixty percent here against forty in the larger build, because this stage is the "
      "reconciliation, and at about five hundred and forty dollars a year it is its biggest line.\n\n"
      "What the model can't price is the part you keep. A dated policy source with every contradiction settled, and the "
      "vessel map beside it, is what your March cohort is handed on day one whether or not anything is built on top. "
      "Neither shows up as a dollar above, and neither stops being worth having."
    ),
    "table_caption": "The eighteen thousand dollar build, five-year view, which lands between about forty two and fifty two thousand all in, or roughly eight and a half to ten thousand a year. Every figure computed rather than estimated.",
    "table_head": ["", "Conservative", "Most likely", "Aggressive"],
    "table": [
      {"label": "Adult fare used to build the error cost", "cells": ["$149", "$239", "$309"], "emphasis": False, "mark": "verified"},
      {"label": "First-season desk agents a year", "cells": ["6", "10", "15"], "emphasis": False, "mark": "assumed"},
      {"label": "Wrong-clock refunds a season", "cells": ["6", "14", "26"], "emphasis": False, "mark": "assumed"},
      {"label": "Share of those prevented", "cells": ["50%", "70%", "85%"], "emphasis": False, "mark": "assumed"},
      {"label": "Share of the agent's lost hours given back", "cells": ["25%", "40%", "55%"], "emphasis": False, "mark": "assumed"},
      {"label": "Annual benefit at run rate", "cells": ["$2,024", "$9,539", "$29,505"], "emphasis": False, "mark": "modelled"},
      {"label": "Of that, hard cash you stop losing", "cells": ["$894", "$4,684", "$13,658"], "emphasis": False, "mark": "modelled"},
      {"label": "Of that, time freed inside a shift you already pay for", "cells": ["$1,130", "$4,855", "$15,847"], "emphasis": False, "mark": "modelled"},
      {"label": "Five-year total cost", "cells": ["$51,720", "$45,784", "$42,320"], "emphasis": False, "mark": "modelled"},
      {"label": "Share of cost recovered", "cells": ["17%", "93%", "321%"], "emphasis": False, "mark": "modelled"},
      {"label": "The same measured on hard cash only", "cells": ["7%", "46%", "148%"], "emphasis": True, "mark": "modelled"},
      {"label": "Payback", "cells": ["None in 5 years", "None in 5 years", "Month 18 (roughly autumn 2029)"], "emphasis": True, "mark": "modelled"}
    ],
    "table_note": (
      "Every assumption behind those drivers, in full. Six to fifteen first-season desk agents, an assumed 10 to 25 "
      "percent of your verified 60 seasonal people, because the desk share is not published. Twelve to thirty hours "
      "per agent lost finding answers in weeks one to six, roughly one and a half to four working days per new hire, and we assume "
      "the build gives back a quarter to just over half of those. Add four to eleven hours of a veteran's time per "
      "first-season agent over the same weeks, of which we assume thirty to sixty percent comes back, a higher share "
      "because the veteran is answering a question they already know. Loaded rates of $26 to $34 for a seasonal agent "
      "and $42 to $58 for a veteran, from an assumed "
      "wage plus burden. Cost per refund error is two adults at a verified fare, with the transportation component "
      "excluded because it is not published, which understates it. The capacity row carries a third line, a pre-season "
      "reconciliation across your site, two hotel front desks and the dock, at an assumed $360 to $1,690 a year. Five-year horizon, contingency 15 to 20 percent, training of $3,500 to $6,200 and upkeep of $4,800 a year conservative down to $2,800 aggressive, which is why the cost row falls as the case improves, year-one benefit discounted to 30, 45 and 60 percent "
      "across the three columns and to 70 percent for the smaller stage.\n\n"
      "The smaller stage costs $4,500 to build, $2,100 to train against, and about $1,000 a year to keep current, which "
      "is re-dating the policy source and re-issuing the vessel map each season. With contingency that is about "
      "$13,300 over five years. Four thousand five hundred of that is our invoice. The $2,100 is your own people's "
      "time learning the source, about fifty hours at the $42 an hour this model uses for a supervisor. Another "
      "$4,500 is upkeep you carry whoever does it, four and a half years of it inside the five-year window because "
      "the first half year is the build. The balance is the 20 percent contingency this model puts on every "
      "line.\n\n"
      "One line we took out. An earlier version counted the money you would not pay us if the search gate failed, and "
      "it made the small stage look like it paid back. It does not belong in your column, because we promise that "
      "outcome anyway and you should not be asked to buy it."
    ),
    "payback_big": "43%",
    "payback_range": (
      "What the four thousand five hundred dollar stage returns conservatively, against a five-year cost of about "
      "thirteen thousand three hundred once training, upkeep and contingency are in, of which four thousand five "
      "hundred is what you pay us. It does not pay back on that full cost, and on hard cash alone it returns thirteen "
      "percent."
    ),
    "base_rate_note": (
      "The outside view says this should not work. MIT puts about 95 percent of generative AI pilots at no measurable "
      "P and L impact, RAND puts AI project failure near 80 percent. That 95 percent is directional, its denominator "
      "is argued over, and it counts pilots with no measurable profit impact rather than AI that does not work. Four "
      "things put this one outside that class. There is no model in the funded scope, so the dominant failure mode "
      "there is absent by construction. The acceptance bar is every possible combination, not a sample. With no "
      "published rule it answers nothing and hands the call to a person. The baseline is "
      "a deliverable, so the check can run.\n\n"
      "None of that beats a base rate on its own. Design does not beat a base rate, execution does, and the "
      "largest risk here is that nobody runs a paper tally for nine weeks. If that happens the outcome is "
      "unmeasurable, and unmeasurable is not a smaller claim, it is a different kind of claim."
    ),
    "value_owner": (
      "We propose the number sits with your Director of Shoreside Operations, because an owner who does not control "
      "the workflow can't move it. It is yours to assign. The check is the same sheet run again from the March 2027 "
      "opening through the first six weeks, the only window the ramp hours can be counted in, and again in the same "
      "late-season weeks."
    )
  },

  "roadmap": {
    "title": "Start with the sheet of paper, because it is free and the window shuts on October 11th",
    "lede": "Sequenced against your calendar, not ours. The season ends in nine weeks and the next cohort starts in March.",
    "body": (
      "Your peak hiring runs January 15th to April 15th and the "
      "season opens in March, so anything meant to help that cohort is in their hands before then or much of "
      "its value waits for the next cohort. That is why the free thing with the closing window goes first."
    ),
    "now": [
      {"item": "A paper tally sheet on the desk for the rest of the 2026 season. Five columns. Question asked, the answer given and the page it came from, time to answer, escalated or not, to whom. The answer column is the one that matters, because without it the sheet can count questions but never a wrong one. Zero cost, and you can start it whether or not you ever hire us.", "metric": "A sheet for every staffed day to October 11th, plus two supervisor-logged days a month, which are where the answers given get read back against the policy source. That is what turns a misquote into a count rather than a feeling. It produces three of the counts this study had to assume, how many people work the desk, how many questions it takes, and how often an answer given differs from the published rule on the days somebody checks. The fourth, the ramp hours, needs a March window and is counted when the sheet runs again in March 2027."},
      {"item": "One dated policy source, with a named owner of yours settling each contradiction. The known starting set starts with two pages giving different parking prices.", "metric": "Every conflict adjudicated, dated and signed, zero unresolved on the four branches."},
      {"item": "The vessel-to-departure map, with a named owner and a date, plus a ruling on whether assignment is stable across maintenance and charters.", "metric": "Either a signed map, or a written decision that it is not stable enough to publish, in which case accessibility ships as always-escalate. Both are a pass. An unowned map is not."},
      {"item": "The log specification, including what gets redacted at capture, how long entries are kept and who may read them.", "metric": "Agreed before the first entry, because the log will capture mobility and dietary details."}
    ],
    "next": [
      {"item": "Re-price the decision table against the measured baseline in autumn 2027, with the arithmetic shown again on real numbers.", "metric": "A rate of answers that differed from the published rule, counted on the checked days, plus the escalation rate and the ramp hours from the March 2027 window, substituted into this model in place of the assumptions."},
      {"item": "If it clears, build and certify the four-branch table for the March 2028 cohort. The 2027 cohort is too early, because the number that justifies the build only accrues while a season runs.", "metric": "100 percent agreement across every possible combination, signed cell by cell, and zero answers returned without a dated source and URL."}
    ],
    "later": [
      {"item": "Staff-facing search over the reconciled pages, for the March 2029 cohort at the earliest, because the count that opens this gate only accrues while the table runs a season. We would price it when the gate is reached, and sell it only if the gate clears.", "metric": "Three numbers we propose and you adjust before anything is agreed. At least 15 percent of the questions the sorter counted fall outside the table, 20 question types that keep coming back, and 150 real questions from the log with the right answer written beside each one, which is our work and not yours. If it lands under any one of them, we publish that and do not invoice."},
      {"item": "Disruption handling as a batch of the same entitlement logic, gated on a counted event frequency.", "metric": "A real count of re-routes and late-train transfers over one season. Your own pages suggest this may be rare, and rare is a finding that keeps it unbuilt."},
      {"item": "A guest-facing answering tool, gated on a full season of internal evidence, and never answering a refund, accessibility or shuttle question.", "metric": "A measured refusal rate on questions it should not answer, tested before a guest ever sees it. We would set the threshold with you when the gate is reached, because it depends on what a season of logs turns out to contain."},
      {"item": "The package question, a conversation and not a build. We assumed phone-only packages are a deliberate sales decision and scoped nothing against it.", "metric": "One answer from your Director of Sales. If it is deliberate this dies here, and that is the right outcome."}
    ],
    "gates": (
      "Every stage is an off-ramp. If nobody runs the tally, we say the outcome can't be measured rather than promise a "
      "measured result. If the sheets show a desk that rarely escalates and rarely misquotes, that is grounds to stop "
      "before a line of code is written, and we would tell you so. If the search gate misses on any one of its three "
      "numbers, we publish that this business needed a rule set and not an AI, and nothing is invoiced.\n\n"
      "One conflict we should name rather than leave in the room. We design the table that decides what counts as a "
      "question it could not answer, and a narrower table produces a longer list. So its boundaries get agreed with "
      "you first, the gate numbers are yours to set, and the log is your data in your format. You can take it to any "
      "vendor, including one that is not us, or to nobody."
    ),
    "need_from_you": (
      "One person to run the paper sheet for nine weeks. A named owner to rule which parking price is "
      "correct. A named owner and a date for the vessel map. A decision on the log's redaction and retention before "
      "the first entry. This stage needs no system access and no guest data."
    )
  },

  "honest": {
    "title": "The largest risk in this document is that nobody runs the sheet of paper",
    "lede": "Four things, and this is the order they would actually bite in.",
    "body": (
      "The tally sheet never runs. This sits on your side of the line. Every benefit figure in this study is an "
      "assumption. The 2026 sheet measures the desk size and the question volume in full and samples the misquote rate, and the ramp "
      "hours wait for a March window. If it does not run, we "
      "would call the outcome unproven rather than substitute a modelled number.\n\n"
      "The wrong clock is quoted less than six times a season. That single driver moves this analysis more than any "
      "other. If your desk almost never misquotes, the correct answer is that you should not buy the table at any "
      "price, and nine weeks of paper answers that before anybody builds anything.\n\n"
      "The desk is smaller than we assumed. How many of your 60 seasonal people work the phones is not published "
      "anywhere we can see, and we assumed 10 to 25 percent. We take deckhands, "
      "cooks, engineering and dock support to be the bulk of that 60. If the desk is three people and two return every "
      "year, both ramp lines shrink toward nothing and the honest recommendation shrinks with them.\n\n"
      "The vessel map turns out not to exist in a usable form. Accessibility depends on knowing which boat runs which "
      "sailing. If assignment moves with maintenance and charters, that branch ships as always-escalate, and we would "
      "put that in writing in week one rather than at delivery."
    )
  },

  "next_step_title": "The next step is a sheet of paper",
  "next_step": (
    "Start the tally. It costs nothing, it needs no decision about us, and it is the only thing here that expires. We "
    "will send the sheet and the five column headings, and you can run it either way."
  ),

  "sources": src
}

out = os.path.join(BASE, "study.json")
json.dump(study, open(out, "w"), indent=2)
print("study.json written,", os.path.getsize(out), "bytes,", len(src), "sources")
