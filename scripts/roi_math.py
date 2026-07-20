#!/usr/bin/env python3
"""Deterministic ROI arithmetic for the Field Study.

The roi-analyst returns drivers as numbers. This script computes every derived
figure so the study never prints a number a reader's calculator can contradict.
The showrunner runs it, pastes the computed results into study.json, and the
study states the ramp so the arithmetic is reproducible from the page.

Usage:
  python scripts/roi_math.py --drivers out/<date>/roi_drivers.json

Drivers file shape (one entry per scenario):
{
  "scenarios": {
    "<name>": {
      "pursuits_per_year": 24,
      "benefit_lines": [
        {"label": "PE/PM drafting", "hours_per_pursuit": 15, "rate": 90, "cut": 0.25},
        {"label": "BD compliance",  "hours_per_pursuit": 6,  "rate": 45, "cut": 0.50}
      ],
      "avoided_cost_lines": [
        {"label": "disqualification risk", "events_per_year": 1, "cost_per_event": 8000, "reduction": 0.5}
      ],
      "implementation": 95000,
      "training": 18000,
      "run_cost_per_year": 30000,
      "run_cost_years": 4.5,
      "contingency": 0.20,
      "year1_ramp": 0.30,
      "years": 5
    }
  }
}
"""
import argparse
import json


def compute(name, s):
    run_rate = 0.0
    for b in s.get("benefit_lines", []):
        run_rate += b["hours_per_pursuit"] * b["rate"] * b["cut"] * s["pursuits_per_year"]
    for a in s.get("avoided_cost_lines", []):
        run_rate += a["events_per_year"] * a["cost_per_event"] * a["reduction"]

    years = s.get("years", 5)
    ramp = s["year1_ramp"]
    cumulative_benefit = run_rate * (ramp + (years - 1))

    tco = (s["implementation"] + s["training"]
           + s["run_cost_per_year"] * s["run_cost_years"]) * (1 + s["contingency"])

    recovered = cumulative_benefit / tco if tco else 0.0

    # Payback month: cumulative benefit crosses cumulative cost. Implementation,
    # training, and contingency land in year one, run cost accrues monthly over
    # run_cost_years starting mid-year-one (month 7), matching a mid-year go-live.
    upfront = (s["implementation"] + s["training"]) * (1 + s["contingency"])
    run_monthly = s["run_cost_per_year"] * (1 + s["contingency"]) / 12.0
    payback_month = None
    cum_b = 0.0
    for m in range(1, years * 12 + 1):
        cum_b += run_rate * (ramp if m <= 12 else 1.0) / 12.0
        run_months = max(0, m - 6)
        cum_c = upfront + run_monthly * min(run_months, s["run_cost_years"] * 12)
        if cum_b >= cum_c:
            payback_month = m
            break

    return {
        "scenario": name,
        "annual_run_rate_benefit": round(run_rate),
        "cumulative_benefit_%dyr" % years: round(cumulative_benefit),
        "tco_%dyr" % years: round(tco),
        "percent_of_tco_recovered": round(recovered * 100),
        "payback_month": payback_month,
        "pays_back_within_horizon": payback_month is not None,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--drivers", required=True)
    args = ap.parse_args()
    with open(args.drivers) as f:
        drivers = json.load(f)
    out = [compute(n, s) for n, s in drivers["scenarios"].items()]
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
