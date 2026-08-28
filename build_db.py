#!/usr/bin/env python3
"""Merge TripSit rec-x-rec pairs + curated med data into database.json"""
import json, datetime
from data_core import SUBSTANCES, MEDS, TEMPLATES, FACTORS
from data_meds import MED_PAIRS, MED_MED
from data_doses import DOSES, TIME_OPTS

tripsit = json.load(open("tripsit_pairs.json"))

# Curated fills for pairs TripSit lacks (all mephedrone)
FILLS = {
 "alcohol|mephedrone": {"risk": "caution", "note": "Masks drunkenness; dehydration and next-day crash. Alcohol worsens cathinone comedowns.", "src": "curated"},
 "cannabis|mephedrone": {"risk": "caution", "note": "THC can amplify stimulant anxiety and racing thoughts.", "src": "curated"},
 "cocaine|mephedrone": {"risk": "high", "note": "Double stimulant load — additive cardiovascular strain and compulsive redosing.", "src": "curated"},
 "amphetamine|mephedrone": {"risk": "high", "note": "Double stimulant load — additive cardiovascular strain, hyperthermia, psychosis risk with sleep loss.", "src": "curated"},
 "ketamine|mephedrone": {"risk": "caution", "note": "Stimulant masks ketamine sedation; watch when the stimulant fades.", "src": "curated"},
 "nitrous|mephedrone": {"risk": "caution", "note": "Falls and brief blackout on top of stimulant load; sit down.", "src": "curated"},
 "2c-x|mephedrone": {"risk": "high", "note": "Additive stimulant/serotonergic load with an unpredictable psychedelic — cardiovascular and anxiety risk.", "src": "curated"},
 "mephedrone|benzos-rec": {"risk": "caution", "note": "Opposing effects mask each other; benzo redosing during comedown risks oversedation once the stimulant clears.", "src": "curated"},
}

sub_pairs = dict(tripsit)
sub_pairs.update(FILLS)

# Attach mechanism templates to rec-x-rec pairs by category logic
CAT = {s["id"]: s["cat"] for s in SUBSTANCES}
SEROTONERGIC = {"mdma", "mephedrone", "dxm"}
for key, v in sub_pairs.items():
    a, b = key.split("|")
    tpl = []
    if CAT[a] == "depressant" and CAT[b] == "depressant":
        tpl.append("CNSDEP")
    if v["risk"] in ("high", "danger"):
        if CAT[a] == "depressant" or CAT[b] == "depressant":
            if "CNSDEP" not in tpl:
                tpl.append("CNSDEP")
        if CAT[a] == "stimulant" and CAT[b] == "stimulant":
            tpl.append("CARDIO")
        if a in SEROTONERGIC and b in SEROTONERGIC:
            tpl.append("SS")
    if {a, b} & {"mdma"} and v["risk"] != "low":
        if "HYPERTHERMIA" not in tpl and (CAT[a] == "stimulant" and CAT[b] == "stimulant"):
            tpl.append("HYPERTHERMIA")
    if tpl:
        v["tpl"] = tpl
    # evidence: tripsit = expert consensus DB
    v.setdefault("ev", "case" if v["src"] == "curated" else "est")

db = {
    "meta": {
        "version": open("VERSION").read().strip(),
        "built": datetime.date.today().isoformat(),
        "language": "en",
        "disclaimer": "Decision-support for trained harm-reduction volunteers. Not medical advice, not a diagnosis tool. When in doubt, escalate to on-site medics or call 112.",
        "sources": [
            "TripSit combination database (github.com/TripSit/drugs), retrieved 2026-08-28",
            "Papaseit et al. 2020, MDMA interactions with pharmaceuticals (Expert Opin Drug Metab Toxicol)",
            "Sarparast et al. 2022, Psychedelics and psychiatric medications (Psychopharmacology)",
            "Hysek et al. 2012, SSRI pretreatment and MDMA response (Clin Pharmacol Ther)",
            "Richards et al. 2017 (J Cardiovasc Pharmacol Ther) & CMAJ 2022 — beta-blockers and stimulants",
            "SmPC/SPC texts of listed medications; Erowid & PsychonautWiki interaction summaries (cross-check only)",
            "Dose bands: PsychonautWiki + TripSit factsheets (retrieved 2026-08-28), cross-checked, conservative value where they disagree; calibrated against clinical doses (MDMA trials, sodium oxybate, dexamfetamine, EFSA caffeine)",
        ],
    },
    "substances": SUBSTANCES,
    "meds": MEDS,
    "factors": FACTORS,
    "doses": DOSES,
    "timeOpts": TIME_OPTS,
    "templates": TEMPLATES,
    "subPairs": sub_pairs,
    "medPairs": MED_PAIRS,
    "medMed": MED_MED,
}

json.dump(db, open("database.json", "w"), indent=1, ensure_ascii=False)
size = len(json.dumps(db))
n_med_pairs = sum(len(m["pairs"]) for m in MED_PAIRS.values())
print(f"database.json written: {size/1024:.0f} KB, {len(sub_pairs)} substance pairs, {n_med_pairs} med-substance pairs, {len(MED_MED)} med-med pairs")

# sanity checks
sub_ids = {s["id"] for s in SUBSTANCES}
med_ids = {m["id"] for m in MEDS}
errs = []
for mid, m in MED_PAIRS.items():
    if mid not in med_ids: errs.append(f"unknown med {mid}")
    for sid, e in m["pairs"].items():
        if sid not in sub_ids: errs.append(f"{mid}: unknown substance {sid}")
        for t in e.get("tpl", []):
            if t not in TEMPLATES: errs.append(f"{mid}|{sid}: unknown tpl {t}")
    for t in m["default"].get("tpl", []):
        if t not in TEMPLATES: errs.append(f"{mid} default: unknown tpl {t}")
for mm in MED_MED:
    if mm["a"] not in med_ids or mm["b"] not in med_ids: errs.append(f"medMed unknown: {mm['a']}|{mm['b']}")
for k in sub_pairs:
    a, b = k.split("|")
    if a not in sub_ids or b not in sub_ids: errs.append(f"subPair unknown: {k}")
for f in FACTORS:
    for t in f.get("triggers", []):
        for sid in t["when"].get("subs", []):
            if sid not in sub_ids: errs.append(f"factor {f['id']}: unknown sub {sid}")
        for mid in t["when"].get("meds", []):
            if mid not in med_ids: errs.append(f"factor {f['id']}: unknown med {mid}")
        for tp in t.get("tpl", []):
            if tp not in TEMPLATES: errs.append(f"factor {f['id']}: unknown tpl {tp}")
for sid, dd in DOSES.items():
    if sid not in sub_ids: errs.append(f"dose: unknown substance {sid}")
    if not dd.get("noNumeric"):
        vids = {v["id"] for v in dd["variants"]}
        for v in dd["variants"]:
            bands = v["bands"]
            if not (bands["light"] < bands["common"] < bands["strong"] < bands["heavy"] <= v["danger"]):
                errs.append(f"dose {sid}/{v['id']}: bands not monotonic")
        for e in dd.get("estimates", []):
            if e["variant"] not in vids: errs.append(f"dose {sid}: estimate variant {e['variant']} unknown")
no_dose = sub_ids - set(DOSES.keys())
if no_dose: errs.append(f"substances without dose entry: {no_dose}")
missing_meds = med_ids - set(MED_PAIRS.keys())
if missing_meds: errs.append(f"meds without pair data: {missing_meds}")
print("ERRORS:" if errs else "sanity: OK")
print("\n".join(errs))
