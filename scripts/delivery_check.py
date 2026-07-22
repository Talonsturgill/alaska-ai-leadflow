#!/usr/bin/env python3
"""The delivery backstop. Exit 0 or the run has not delivered.

The DELIVERY GATE in Phase 8 is enforced here in code, not just in prose:

  1. The draft of record was READ BACK (list_drafts, DRAFT_VIEW_FULL) and its
     JSON saved to a file. This script verifies that read-back mechanically:
     body present, paragraph breaks intact, no raw markup or base64 blobs,
     recipients and subject present.
  2. Every deliverable link is commit-pinned (a full 40-hex SHA, never a
     branch name), the path EXISTS at that SHA (git cat-file), and the SHA is
     reachable from a pushed remote ref, so the link cannot rot.
  3. Every expected link actually appears in the draft body (Gmail's
     google.com/url?q= rewrapping is unwrapped first, it is normal).

Usage:
  python scripts/delivery_check.py \
    --readback out/<date>/draft_readback.json \
    [--draft-id r123...] \
    --link https://github.com/<owner>/<repo>/tree/<sha>/runs/<date>/<slug> \
    --link https://github.com/<owner>/<repo>/blob/<sha>/runs/<date>/<slug>/field-study.html \
    ...

--readback accepts either the raw list_drafts response ({"drafts":[...]}) or a
single draft object. With --draft-id the matching draft is checked and its
absence is a failure. Prints PASS or every failure found, and exits non-zero on
any failure. The run may not record itself delivered unless this exits 0.
"""
import argparse
import json
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request

GH_LINK = re.compile(
    r"https://github\.com/([^/\s]+)/([^/\s]+)/(blob|tree)/([^/\s]+)(?:/([^\s?#]*))?"
)


def unwrap_gmail_links(text):
    return re.sub(
        r"https://www\.google\.com/url\?q=([^&\s]+)\S*",
        lambda m: urllib.parse.unquote(m.group(1)),
        text,
    )


def git(args, cwd):
    return subprocess.run(["git"] + args, cwd=cwd, capture_output=True, text=True)


def check_github_link(url, repo_dir, failures):
    m = GH_LINK.match(url)
    if not m:
        return  # not a repo artifact link, presence-in-body is checked separately
    _, _, kind, ref, path = m.groups()
    path = (path or "").rstrip("/")
    if not re.fullmatch(r"[0-9a-f]{40}", ref):
        failures.append(f"link not commit-pinned (ref '{ref}' is not a 40-hex sha): {url}")
        return
    if path:
        if git(["cat-file", "-e", f"{ref}:{path}"], repo_dir).returncode != 0:
            failures.append(f"path does not exist at pinned sha: {ref}:{path}")
    elif git(["cat-file", "-e", f"{ref}^{{commit}}"], repo_dir).returncode != 0:
        failures.append(f"pinned sha does not exist locally: {ref}")
    contained = git(["branch", "-r", "--contains", ref], repo_dir)
    if contained.returncode != 0 or not contained.stdout.strip():
        failures.append(f"pinned sha not reachable from any pushed remote ref: {ref}")


def check_live_link(url, failures, tries=6, wait=20):
    """The hosted study must actually serve. Retries absorb Pages deploy lag."""
    last = None
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "alaska-ai-delivery-check"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                body = resp.read(4096).decode("utf-8", "replace")
                if resp.status == 200 and len(body) > 500:
                    return
                last = f"status {resp.status}, {len(body)} bytes"
        except Exception as e:  # noqa: BLE001
            last = str(e)
        if attempt < tries - 1:
            time.sleep(wait)
    failures.append(f"live link not serving after {tries} tries ({last}): {url}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--readback", required=True)
    ap.add_argument("--draft-id")
    ap.add_argument("--link", action="append", default=[])
    ap.add_argument("--live-link", action="append", default=[])
    ap.add_argument("--repo-dir", default=".")
    ap.add_argument("--min-paragraphs", type=int, default=2)
    args = ap.parse_args()

    failures = []

    with open(args.readback) as f:
        data = json.load(f)
    drafts = data.get("drafts", [data]) if isinstance(data, dict) else data
    draft = None
    if args.draft_id:
        draft = next((d for d in drafts if d.get("id") == args.draft_id), None)
        if draft is None:
            failures.append(f"draft of record {args.draft_id} not found in read-back")
    elif drafts:
        draft = drafts[0]
    else:
        failures.append("read-back contains no drafts")

    if draft is not None:
        body = draft.get("plaintextBody") or ""
        if not body.strip():
            failures.append("plaintext body is empty or missing, the draft did not round-trip")
        else:
            normalized = body.replace("\r\n", "\n")
            if normalized.count("\n\n") < args.min_paragraphs:
                failures.append(
                    f"body has fewer than {args.min_paragraphs} paragraph breaks, spacing collapsed"
                )
            if re.search(r"[A-Za-z0-9+/=]{300,}", body):
                failures.append("body contains a raw base64-looking blob, an attachment leaked into text")
            if re.search(r"<(html|body|div|span|style|head)\b", body, re.I):
                failures.append("plaintext body contains raw HTML markup, it will read as code")
        if not draft.get("subject", "").strip():
            failures.append("subject is empty")
        if not draft.get("toRecipients"):
            failures.append("no recipients on the draft")
        unwrapped = unwrap_gmail_links(body)
        for link in args.link:
            if link not in unwrapped:
                failures.append(f"expected link missing from body: {link}")

    for link in args.link:
        check_github_link(link, args.repo_dir, failures)

    for link in args.live_link:
        check_live_link(link, failures)

    if failures:
        print("DELIVERY CHECK FAILED")
        for f_ in failures:
            print(f"  - {f_}")
        sys.exit(1)
    print("DELIVERY CHECK PASSED")


if __name__ == "__main__":
    main()
