# CatNet 🐈‍⬛

Offline-first interaction checker for festival harm-reduction volunteers. Select the person's factors, medication and substances — CatNet flags risky combinations (worst first), assesses reported intake, and gives watch-for / DO-NOT / escalation guidance.

**Decision-support for trained volunteers. Not medical advice. When in doubt: on-site medics or 112.**

## Structure

- `data_core.py` — substances, medication classes, personal factors, mechanism templates
- `data_meds.py` — curated medication × substance interactions (literature-based, evidence-tagged)
- `data_doses.py` — reported-intake bands (PsychonautWiki + TripSit, cross-checked, clinically calibrated)
- `extract_tripsit.py` — transforms TripSit `combos.json` into substance × substance pairs
- `build_db.py` — merges everything into `database.json` (+ sanity checks); version comes from `VERSION`
- `build_app.py` — injects the database into `app_shell.html` → `dist/` (PWA) and `artifact.html`
- `dist/` — deployable app: `index.html`, service worker, manifest, `version.json`, install page

## Build

```bash
python extract_tripsit.py && python build_db.py && python build_app.py
```

## Updates

Two mechanisms:

1. **Automated (TripSit layer):** `.github/workflows/update-data.yml` runs quarterly (and on demand via the Actions tab). It re-fetches TripSit combo data, rebuilds, and — if anything changed — bumps the patch version and opens a **review PR** with a diff summary and checklist. Nothing deploys without a human merge; a safety tool should not blindly trust upstream.
2. **Curated layers (medications, doses):** reviewed manually with Claude in the "Harm reduction" project — ask for a "CatNet database update"; sources and method are in the project methodology doc.

On merge to `main`, GitHub Pages redeploys `dist/`. Running apps pick the new version up via `version.json` (automatic check on load + "Check for updates" button); the PWA service worker refreshes its cache on the next online open.

## Data sources

TripSit combination DB (CC BY-SA); PsychonautWiki dose summaries (CC BY-SA, cross-checked with TripSit, conservative value where they disagree); published pharmacology literature (Papaseit 2020, Sarparast 2022, Hysek 2012, Richards 2017, CMAJ 2022); official SmPC/product texts; clinical dose anchors (MDMA trials, sodium oxybate, dexamfetamine, EFSA caffeine).

## License

Code: MIT. Interaction and dose data derive from CC BY-SA sources (TripSit, PsychonautWiki) — attribution above, share-alike applies to the data layer.
