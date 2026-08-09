"""Resolve a relative path against the REPO ROOT, not the shell's cwd.

Written 2026-08-09, closing the backlog item first raised on 2026-08-07 on its
SECOND appearance, per the retro rule that a twice-seen defect is the work.

THE DEFECT. On 2026-08-07 Phase 1 wrote selection.md, shortlist.json and all four
scout outputs to /home/user/out/2026-08-07/ instead of into the repo, because an
earlier command had cd'd to the sibling checkout and the working directory
persisted. Every write succeeded, nothing warned, and it was only caught at Phase
8 when the archive step could not find selection.md.

IT CAME BACK TODAY. Mid-run, a `cd /home/user/alaskaaicarousels` to check the
public repo left the shell there, and the next command reported that
.claude/agents/staff-engineer.md did not exist and that this was not a git
repository. That is the same failure wearing the same clothes, and it cost a
confused diagnosis in the middle of Phase 4.

THE FIX. Scripts resolve their path arguments through resolve(). An absolute path
is returned untouched. A relative path is tried against the cwd first, so normal
use is unchanged, and falls back to the repo root when that misses. So
`python scripts/study_lint.py --study out/2026-08-09/study.json` now works from
anywhere, which is what everyone already assumed it did.
"""
import os

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def resolve(path):
    """Absolute paths pass through. Relative ones fall back to the repo root."""
    if not path or os.path.isabs(path):
        return path
    if os.path.exists(path):
        return path
    candidate = os.path.join(REPO_ROOT, path)
    if os.path.exists(candidate):
        return candidate
    # Neither exists. Return the repo-root form, because a run's artifacts belong
    # in the repo and the error message should point there rather than at whatever
    # directory the shell happens to be sitting in.
    return candidate
