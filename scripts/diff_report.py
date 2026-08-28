#!/usr/bin/env python3
"""Compare old vs new database.json and write a human-readable diff summary
for the update PR body. Usage: diff_report.py old.json new.json out.md"""
import json, sys

old = json.load(open(sys.argv[1]))
new = json.load(open(sys.argv[2]))
lines = ["## Automated TripSit data refresh", ""]

op, np_ = old.get("subPairs", {}), new.get("subPairs", {})
added = sorted(set(np_) - set(op))
removed = sorted(set(op) - set(np_))
changed = sorted(k for k in np_ if k in op and np_[k] != op[k])

if not (added or removed or changed):
    lines.append("No changes in substance-pair data.")
else:
    if added:
        lines.append(f"### Added pairs ({len(added)})")
        lines += [f"- `{k}` → {np_[k]['risk']}" for k in added] + [""]
    if removed:
        lines.append(f"### Removed pairs ({len(removed)}) — REVIEW CAREFULLY")
        lines += [f"- `{k}` (was {op[k]['risk']})" for k in removed] + [""]
    if changed:
        lines.append(f"### Changed pairs ({len(changed)})")
        for k in changed:
            o, n = op[k], np_[k]
            what = []
            if o.get("risk") != n.get("risk"):
                what.append(f"risk {o.get('risk')} → **{n.get('risk')}**")
            if o.get("note") != n.get("note"):
                what.append("note text changed")
            lines.append(f"- `{k}`: {', '.join(what) or 'metadata changed'}")
        lines.append("")

lines += [
    "---",
    "**Review checklist before merging:**",
    "- [ ] No risk level was silently DOWNGRADED without a good reason",
    "- [ ] Removed pairs are intentional upstream, not vandalism/errors",
    "- [ ] Spot-check 2–3 changed notes against tripsit.me",
    "",
    "Curated medication layer and dose bands are NOT touched by this automation — those are reviewed manually/with Claude.",
]
open(sys.argv[3], "w").write("\n".join(lines))
print("\n".join(lines[:12]))
