#!/usr/bin/env python3
"""Extract recreational x recreational pairs from TripSit combos.json
into our schema. Output: tripsit_pairs.json"""
import json

# our substance id -> tripsit key
MAP = {
    "alcohol": "alcohol",
    "cannabis": "cannabis",
    "mdma": "mdma",
    "cocaine": "cocaine",
    "amphetamine": "amphetamines",
    "ketamine": "ketamine",
    "lsd": "lsd",
    "mushrooms": "mushrooms",
    "ghb": "ghb/gbl",
    "nitrous": "nitrous",
    "2c-x": "2c-x",
    "dxm": "dextromethorphan",
    "opioids-rec": "opioids",
    "mephedrone": "mephedrone",
    "benzos-rec": "benzodiazepines",
    "caffeine": "caffeine",
}

STATUS_MAP = {
    "Low Risk & No Synergy": ("low", None),
    "Low Risk & Synergy": ("low", "Effects reinforce each other — start lower than usual."),
    "Low Risk & Decrease": ("low", "One substance blunts the other; risk of redosing to compensate."),
    "Caution": ("caution", None),
    "Unsafe": ("high", None),
    "Dangerous": ("danger", None),
}

d = json.load(open("tripsit-combos.json"))
out = {}
ids = list(MAP.keys())
for i, a in enumerate(ids):
    for b in ids[i + 1:]:
        ta, tb = MAP[a], MAP[b]
        info = d.get(ta, {}).get(tb) or d.get(tb, {}).get(ta)
        if not info:
            continue
        risk, extra = STATUS_MAP[info["status"]]
        note = (info.get("note") or "").strip()
        if extra and not note:
            note = extra
        elif extra:
            note = note + " " + extra
        key = f"{a}|{b}"
        out[key] = {"risk": risk, "note": note, "src": "tripsit"}

json.dump(out, open("tripsit_pairs.json", "w"), indent=1, ensure_ascii=False)
print(f"{len(out)} pairs extracted")
from collections import Counter
print(Counter(v["risk"] for v in out.values()))
