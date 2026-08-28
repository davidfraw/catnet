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

NEW_SUB_FILLS = {
 # synthetic cannabinoids
 "alcohol|synth-cann": {"risk": "high", "note": "Heavy sedation, vomiting and collapse — a common bad-outcome pairing in emergency reports.", "tpl": ["CNSDEP"], "src": "curated"},
 "cannabis|synth-cann": {"risk": "caution", "note": "Users often don't know their material is synthetic. THC on top tells you nothing about total dose — treat mixed or unknown 'weed' as synthetic.", "src": "curated"},
 "mdma|synth-cann": {"risk": "high", "note": "Stimulant load on top of a convulsant, psychosis-prone cannabinoid.", "tpl": ["CARDIO", "PSYCH", "SEIZURE"], "src": "curated"},
 "amphetamine|synth-cann": {"risk": "high", "note": "Agitation, heart strain and paranoia all amplified; seizure risk adds up.", "tpl": ["CARDIO", "PSYCH", "SEIZURE"], "src": "curated"},
 "cocaine|synth-cann": {"risk": "high", "note": "As with other stimulants — cardiovascular and psychosis load amplified.", "tpl": ["CARDIO", "PSYCH"], "src": "curated"},
 "mephedrone|synth-cann": {"risk": "high", "note": "Stimulant + convulsant cannabinoid — agitation and seizure risk.", "tpl": ["CARDIO", "PSYCH", "SEIZURE"], "src": "curated"},
 "lsd|synth-cann": {"risk": "high", "note": "Two unpredictable psychoactives — difficult trips and psychotic reactions much more likely.", "tpl": ["PSYCH"], "src": "curated"},
 "mushrooms|synth-cann": {"risk": "high", "note": "As LSD — psychological risk multiplies.", "tpl": ["PSYCH"], "src": "curated"},
 "2c-x|synth-cann": {"risk": "high", "note": "Unpredictable × unpredictable — avoid.", "tpl": ["PSYCH"], "src": "curated"},
 "ketamine|synth-cann": {"risk": "caution", "note": "Sedation and dissociation stack; falls and vomiting.", "src": "curated"},
 "ghb|synth-cann": {"risk": "high", "note": "Sedation stacks unpredictably with a substance that can itself cause collapse.", "tpl": ["CNSDEP"], "src": "curated"},
 "nitrous|synth-cann": {"risk": "caution", "note": "Blackout and fall risk on top of an unpredictable substance; sit down.", "src": "curated"},
 "dxm|synth-cann": {"risk": "high", "note": "Dissociation + delirium-prone cannabinoid — confusion and psychological distress likely.", "tpl": ["PSYCH"], "src": "curated"},
 "opioids-rec|synth-cann": {"risk": "high", "note": "Additive sedation on an unpredictable base.", "tpl": ["CNSDEP"], "src": "curated"},
 "benzos-rec|synth-cann": {"risk": "caution", "note": "Benzos are what medics use for synthetic-cannabinoid agitation — but self-dosed on top, watch sedation depth and breathing.", "src": "curated"},
 "caffeine|synth-cann": {"risk": "caution", "note": "Extra heart-rate load and jitteriness on a substance already straining the heart.", "src": "curated"},
 "synth-cann|kratom": {"risk": "high", "note": "Unpredictable convulsant + opioid-type sedation — no data, treat as unsafe.", "tpl": ["CNSDEP", "SEIZURE"], "src": "curated"},
 # kratom
 "alcohol|kratom": {"risk": "high", "note": "A common real-world pairing that ends in heavy sedation and vomiting; opioid-type breathing depression stacks with alcohol.", "tpl": ["CNSDEP"], "src": "curated"},
 "cannabis|kratom": {"risk": "caution", "note": "Additive sedation and nausea.", "src": "curated"},
 "mdma|kratom": {"risk": "caution", "note": "Kratom adds mild serotonergic and stimulant load; watch agitation and overheating.", "tpl": ["SS"], "src": "curated"},
 "amphetamine|kratom": {"risk": "caution", "note": "Additive stimulation at low kratom doses; at high doses kratom's sedation is masked until the stimulant fades.", "src": "curated"},
 "cocaine|kratom": {"risk": "caution", "note": "As amphetamine — masking dynamic.", "src": "curated"},
 "mephedrone|kratom": {"risk": "caution", "note": "Additive stimulant/serotonergic load.", "tpl": ["SS"], "src": "curated"},
 "lsd|kratom": {"risk": "caution", "note": "Little data; kratom's opioid sedation may blunt or muddle the trip.", "src": "curated"},
 "mushrooms|kratom": {"risk": "caution", "note": "Little data; additive nausea is the practical issue.", "src": "curated"},
 "2c-x|kratom": {"risk": "caution", "note": "Little data — keep doses of both low.", "src": "curated"},
 "ketamine|kratom": {"risk": "caution", "note": "Additive sedation and nausea; vomiting while dissociated is an airway risk.", "tpl": ["CNSDEP"], "src": "curated"},
 "ghb|kratom": {"risk": "danger", "note": "Opioid-type sedation + GHB is respiratory-depression stacking.", "tpl": ["CNSDEP"], "src": "curated"},
 "nitrous|kratom": {"risk": "caution", "note": "Additive sedation; sit down.", "src": "curated"},
 "dxm|kratom": {"risk": "high", "note": "Serotonergic + opioid overlap on both sides — agitation, sedation and breathing concerns together.", "tpl": ["SS", "CNSDEP"], "src": "curated"},
 "opioids-rec|kratom": {"risk": "danger", "note": "Kratom is opioid-active — doses stack into respiratory depression.", "tpl": ["CNSDEP"], "src": "curated"},
 "benzos-rec|kratom": {"risk": "high", "note": "Opioid-type sedation + benzos — breathing and airway watch.", "tpl": ["CNSDEP"], "src": "curated"},
 "caffeine|kratom": {"risk": "low", "note": "Common pairing; mild extra stimulation.", "src": "curated"},
}

sub_pairs = dict(tripsit)
sub_pairs.update(FILLS)
sub_pairs.update(NEW_SUB_FILLS)

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
        "disclaimer": "Decision-support for trained harm-reduction volunteers. Not medical advice, not a diagnosis tool. When in doubt, hand over to on-site medics or call 112 (EU) / your local emergency number.",
        "sources": [
            "TripSit combination database. github.com/TripSit/drugs (combos.json), retrieved 2026-08-28",
            "Papaseit E, et al. MDMA interactions with pharmaceuticals and drugs of abuse. Expert Opin Drug Metab Toxicol. 2020;16(5):357–369. doi:10.1080/17425255.2020.1749262",
            "Sarparast A, Thomas K, Malcolm B, Stauffer CS. Drug-drug interactions between psychiatric medications and MDMA or psilocybin: a systematic review. Psychopharmacology. 2022;239:1945–1976. doi:10.1007/s00213-022-06083-y",
            "Liechti ME, Baumann C, Gamma A, Vollenweider FX. Acute psychological effects of MDMA are attenuated by the serotonin uptake inhibitor citalopram. Neuropsychopharmacology. 2000;22(5):513–521. doi:10.1016/S0893-133X(99)00148-7",
            "Richards JR, et al. β-Blockers, cocaine, and the unopposed α-stimulation phenomenon. J Cardiovasc Pharmacol Ther. 2017;22(3):239–249. doi:10.1177/1074248416681644",
            "Mann SK, et al. Beta blocker therapy in heart failure patients with active cocaine use: a systematic review. Cardiol Res Pract. 2020. doi:10.1155/2020/1985379",
            "Dose bands: PsychonautWiki (psychonautwiki.org, CC BY-SA) + TripSit factsheets (drugs.json), both retrieved 2026-08-28; cross-checked, conservative value where they disagree; calibrated against clinical doses (MDMA trials, sodium oxybate/Xyrem SmPC, dexamfetamine SmPC, EFSA caffeine opinion 2015, doi:10.2903/j.efsa.2015.4102)",
            "SmPC/SPC texts of listed medications; Erowid interaction summaries (cross-check only)",
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
