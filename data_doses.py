# Reported-intake assessment data.
# Framing: these ranges describe what users REPORT taking (PsychonautWiki + TripSit,
# cross-checked; conservative value chosen where sources disagree) — calibrated against
# clinical trial doses where they exist. This is assessment of reported intake,
# NOT dosing advice.
#
# bands: light [a,b), common [b,c), strong [c,d), heavy >= d ; "danger" = danger_at anchor
# All ranges per single dose in the stated unit for that variant (route/form).

DOSES = {
 "mdma": {
  "variants": [
   {"id": "oral", "label": "Oral (mg)", "unit": "mg",
    "bands": {"light": 20, "common": 80, "strong": 120, "heavy": 150}, "danger": 300,
    "onsetMin": [30, 70], "durH": "3–6", "peakNote": "second wave common at 60–90 min"}],
  "perKg": True,
  "estimates": [
   {"label": "1 pill (unknown)", "amount": 200, "variant": "oral", "note": "EU pills commonly 150–200 mg MDMA, some 300+ — conservative estimate used"},
   {"label": "½ pill", "amount": 100, "variant": "oral"},
   {"label": "1 crystal bomb", "amount": 150, "variant": "oral"}],
  "cal": "Clinical anchor: MDMA-assisted therapy trials use 80–120 mg once, in screened adults, in a clinic.",
  "srcNote": "PW heavy 150 mg+; TripSit 175 mg+ — conservative shown.",
  "redose": "Redosing multiplies hyperthermia and next-day toll far more than it extends the high; strongly discourage a second full dose."},
 "amphetamine": {
  "variants": [
   {"id": "oral-speed", "label": "Oral, speed (mg)", "unit": "mg",
    "bands": {"light": 5, "common": 10, "strong": 25, "heavy": 50}, "danger": 120,
    "onsetMin": [15, 45], "durH": "6–8"},
   {"id": "nasal-speed", "label": "Snorted, speed (mg)", "unit": "mg",
    "bands": {"light": 6, "common": 15, "strong": 30, "heavy": 50}, "danger": 120,
    "onsetMin": [1, 10], "durH": "3–6"},
   {"id": "meth", "label": "Methamphetamine, any route (mg)", "unit": "mg",
    "bands": {"light": 5, "common": 10, "strong": 30, "heavy": 50}, "danger": 100,
    "onsetMin": [1, 20], "durH": "8–12"}],
  "estimates": [
   {"label": "1 line speed (unknown purity)", "amount": 40, "variant": "nasal-speed", "note": "street speed purity varies enormously — often heavily cut"}],
  "cal": "Clinical anchor: prescribed dexamfetamine tops out around 40–60 mg per DAY, divided.",
  "srcNote": "PW oral common 10–25 mg; TripSit 20–50 mg — conservative (PW) shown. Meth bands from TripSit.",
  "redose": "Each redose extends the sleepless window — psychosis risk climbs with hours awake, not just mg."},
 "cocaine": {
  "variants": [
   {"id": "nasal", "label": "Snorted (mg)", "unit": "mg",
    "bands": {"light": 10, "common": 30, "strong": 60, "heavy": 90}, "danger": 200,
    "onsetMin": [3, 10], "durH": "0.5–1.5"}],
  "estimates": [
   {"label": "1 line", "amount": 50, "variant": "nasal", "note": "a typical line is 30–60 mg; purity unknown"},
   {"label": "1 bump/key", "amount": 20, "variant": "nasal"}],
  "srcNote": "PW heavy 90 mg+; TripSit 150 mg+ — conservative shown.",
  "redose": "Short action drives redosing every 30–60 min; the cardiovascular load is cumulative even though the high is not."},
 "ketamine": {
  "variants": [
   {"id": "nasal", "label": "Snorted (mg)", "unit": "mg",
    "bands": {"light": 10, "common": 30, "strong": 75, "heavy": 150}, "danger": 300,
    "onsetMin": [1, 10], "durH": "1–2"},
   {"id": "oral", "label": "Oral (mg)", "unit": "mg",
    "bands": {"light": 50, "common": 100, "strong": 300, "heavy": 450}, "danger": 600,
    "onsetMin": [10, 30], "durH": "3–6"}],
  "perKg": True,
  "estimates": [
   {"label": "1 bump", "amount": 30, "variant": "nasal"},
   {"label": "1 line", "amount": 75, "variant": "nasal", "note": "a fat line can be a k-hole dose for a light or naive user"}],
  "cal": "Clinical anchor: sub-anesthetic infusions ~0.5 mg/kg; anesthesia starts around 1–2 mg/kg IV.",
  "srcNote": "PW nasal common 30–75 mg; TripSit 50–125 mg — conservative shown.",
  "redose": "Tolerance builds within a session; redosing to chase the first effect leads to k-holes and falls."},
 "lsd": {
  "variants": [
   {"id": "oral", "label": "Oral (µg)", "unit": "µg",
    "bands": {"light": 15, "common": 75, "strong": 150, "heavy": 250}, "danger": 500,
    "onsetMin": [15, 90], "durH": "8–12"}],
  "estimates": [
   {"label": "1 tab (unknown)", "amount": 100, "variant": "oral", "note": "tabs are typically 80–120 µg but range up to 300+; content unknowable without testing"},
   {"label": "½ tab", "amount": 50, "variant": "oral"}],
  "srcNote": "PW heavy 300 µg+; TripSit 250 µg+ — conservative shown.",
  "redose": "Physiologically forgiving, psychologically not — a second tab mid-trip doubles the duration of a possibly difficult experience."},
 "mushrooms": {
  "variants": [
   {"id": "oral", "label": "Dried (g)", "unit": "g",
    "bands": {"light": 0.5, "common": 1.5, "strong": 3.5, "heavy": 5}, "danger": 10,
    "onsetMin": [20, 60], "durH": "4–6"}],
  "estimates": [
   {"label": "1 g dried", "amount": 1, "variant": "oral"},
   {"label": "3.5 g (an eighth)", "amount": 3.5, "variant": "oral", "note": "a strong dose for most people"}],
  "srcNote": "TripSit dried-gram bands; PW psilocybin-mg bands are consistent (~1% psilocybin content). Potency varies several-fold between batches.",
  "redose": "Adding more mid-come-up because 'nothing is happening' is the classic route to an overwhelming trip — onset can take a full hour."},
 "2c-x": {
  "variants": [
   {"id": "oral", "label": "Oral, 2C-B (mg)", "unit": "mg",
    "bands": {"light": 10, "common": 15, "strong": 25, "heavy": 45}, "danger": 80,
    "onsetMin": [20, 75], "durH": "5–7"},
   {"id": "nasal", "label": "Snorted, 2C-B (mg)", "unit": "mg",
    "bands": {"light": 5, "common": 8, "strong": 12, "heavy": 23}, "danger": 50,
    "onsetMin": [1, 10], "durH": "4–6"}],
  "srcNote": "PW and TripSit closely agree for 2C-B. Bands apply to 2C-B ONLY — other 2C-x differ; snorted is much stronger per mg and very painful.",
  "redose": "Steep dose–response: the step from strong to overwhelming is a few mg."},
 "ghb": {
  "variants": [
   {"id": "ghb", "label": "GHB (g)", "unit": "g",
    "bands": {"light": 0.5, "common": 1, "strong": 2.5, "heavy": 3.5}, "danger": 7,
    "onsetMin": [5, 30], "durH": "1.5–2.5"},
   {"id": "gbl", "label": "GBL (ml)", "unit": "ml",
    "bands": {"light": 0.3, "common": 0.6, "strong": 1.2, "heavy": 2}, "danger": 5,
    "onsetMin": [5, 20], "durH": "1–2"}],
  "perKg": True,
  "estimates": [
   {"label": "1 cap GHB (~2 g)", "amount": 2, "variant": "ghb"},
   {"label": "1 small cap GBL (~1 ml)", "amount": 1, "variant": "gbl", "note": "GBL is roughly 2× as potent per volume as GHB and hits faster — confusing the two causes overdoses"}],
  "cal": "Clinical anchor: sodium oxybate is prescribed at 2.25–4.5 g per single medical dose. PW: risk of death above ~10 g.",
  "srcNote": "PW heavy 4 g+; TripSit heavy 3.5–5 g, dangerous 7 g+ — conservative shown.",
  "redose": "THE redosing killer: second dose before the first peaks (20–40 min) stacks into sudden unconsciousness. Any redose under 2 h is a red flag."},
 "dxm": {
  "variants": [
   {"id": "oral", "label": "Oral (mg)", "unit": "mg",
    "bands": {"light": 100, "common": 200, "strong": 400, "heavy": 700}, "danger": 1200,
    "onsetMin": [30, 120], "durH": "8–12"}],
  "perKg": True,
  "estimates": [
   {"label": "1 bottle syrup (unknown)", "amount": 300, "variant": "oral", "note": "bottles typically contain 150–350 mg total"}],
  "cal": "Clinical anchor: the antitussive ceiling is 120 mg/DAY — every recreational band is far above medical use.",
  "srcNote": "PW absolute bands; TripSit uses mg/kg (common 2.5–7.5 mg/kg) — both shown via the mg/kg readout.",
  "redose": "Long duration — redosing stacks into delirium territory hours later."},
 "mephedrone": {
  "variants": [
   {"id": "oral", "label": "Oral (mg)", "unit": "mg",
    "bands": {"light": 50, "common": 100, "strong": 200, "heavy": 300}, "danger": 500,
    "onsetMin": [15, 45], "durH": "3–6"},
   {"id": "nasal", "label": "Snorted (mg)", "unit": "mg",
    "bands": {"light": 15, "common": 45, "strong": 80, "heavy": 125}, "danger": 250,
    "onsetMin": [5, 10], "durH": "1.5–3"}],
  "estimates": [
   {"label": "1 bomb (wrapped)", "amount": 150, "variant": "oral"},
   {"label": "1 line", "amount": 60, "variant": "nasal"}],
  "srcNote": "PW and TripSit closely agree.",
  "redose": "Compulsive redosing is the signature of cathinones — totals of 1 g+ per night are common and drive the serotonergic/cardiac harm."},
 "alcohol": {
  "variants": [
   {"id": "oral", "label": "Oral (g of ethanol)", "unit": "g ethanol",
    "bands": {"light": 10, "common": 20, "strong": 50, "heavy": 80}, "danger": 120,
    "onsetMin": [15, 30], "durH": "~1 per 10 g"}],
  "driving": True,
  "helper": "Quick count: beer 0.5 l (5%) ≈ 20 g · small beer 0.33 l ≈ 13 g · strong beer 0.5 l (7%) ≈ 28 g · shot 40 ml (40%) ≈ 13 g · wine glass 150 ml (12%) ≈ 14 g. Add them up.",
  "cal": "Bands are grams of pure ethanol over the evening; the liver clears roughly 10 g per hour, so the same total inside one hour behaves a category higher.",
  "srcNote": "Converted from TripSit unit bands (1 unit ≈ 10 g ethanol); danger anchor 120 g+ (poisoning watch).",
  "redose": "Count grams-per-hour, not totals: roughly 10 g clears per hour."},
 "cannabis": {
  "variants": [
   {"id": "edible", "label": "Edible (mg THC)", "unit": "mg THC",
    "bands": {"light": 2.5, "common": 5, "strong": 15, "heavy": 30}, "danger": 100,
    "onsetMin": [30, 120], "durH": "4–10",
    "bandDesc": {
     "light": "light — mildly relaxed, fully functional, conversation normal",
     "common": "common — clearly high: giggly or quiet, red eyes, slowed reactions, snacky; fine with company",
     "strong": "strong — very high: heavy sedation or anxiety, time distortion, hard to follow conversation; needs a calm space",
     "heavy": "heavy — overwhelmed: for non-regular users expect greening out (pale, sweaty, nauseous, panicky, needs to lie down)",
     "danger": "extreme edible amount — hours of distress ahead; not lethal, but treat like a psychedelic crisis: calm sitter, quiet space, time"}}],
  "helper": "Typical contents: joint ≈ 0.25–0.5 g flower ≈ 30–80 mg THC (smoking absorbs only ~a quarter of it) · gummy/edible piece 5–50 mg THC if unlabelled · dabs/concentrates far higher. When smoked, judge by the person's state, not numbers — it self-titrates within minutes.",
  "estimates": [
   {"label": "1 gummy (unknown)", "amount": 10, "variant": "edible", "note": "unlabelled edibles range 5–50+ mg THC per piece"}],
  "cal": "Clinical anchor: prescription THC starts at 2.5 mg; 10 mg is a lot for a naive user.",
  "srcNote": "Edible bands from clinical/regulatory guidance; smoked left qualitative deliberately.",
  "redose": "Edibles: NO redosing inside 2 hours — delayed onset is how every edible horror story starts."},
 "caffeine": {
  "variants": [
   {"id": "oral", "label": "Oral (mg)", "unit": "mg",
    "bands": {"light": 20, "common": 75, "strong": 250, "heavy": 400}, "danger": 1000,
    "onsetMin": [5, 10], "durH": "3–5"}],
  "estimates": [
   {"label": "Energy drink 250 ml", "amount": 80, "variant": "oral"},
   {"label": "Energy drink 500 ml", "amount": 160, "variant": "oral"},
   {"label": "Espresso", "amount": 63, "variant": "oral"}],
  "cal": "Clinical anchor: EFSA safe single dose ~200 mg, daily ~400 mg.",
  "srcNote": "TripSit and EFSA agree.",
  "redose": "Counts cumulatively across the whole day — ask about total cans, not the last one."},
 "synth-cann": {"noNumeric": True,
  "warn": "No dose bands can exist here: potency varies enormously between batches and even within one bag — one puff of a strong batch can act like a heavy dose. Ask what it looked like and how much was smoked, but do not trust numbers; judge by the person's state."},
 "kratom": {
  "variants": [
   {"id": "oral", "label": "Oral, powder/tea (g)", "unit": "g",
    "bands": {"light": 1, "common": 2, "strong": 4, "heavy": 6}, "danger": 12,
    "onsetMin": [10, 40], "durH": "2–5"}],
  "estimates": [
   {"label": "1 teaspoon (~2.5 g)", "amount": 2.5, "variant": "oral"},
   {"label": "1 capsule (~0.6 g)", "amount": 0.6, "variant": "oral"}],
  "srcNote": "PsychonautWiki/TripSit community bands; potency varies several-fold by strain and vendor, extracts are far stronger per gram.",
  "redose": "Stacked doses build opioid-type sedation and nausea over the day; the stimulant feel of the first dose is a poor guide to the fourth."},
 "nitrous": {"noNumeric": True,
  "warn": "Dose counting adds little here: the acute risks are falls and oxygen deprivation from many balloons in a row without breaks, or bags/masks. Ask about frequency and setting instead of amounts."},
 "opioids-rec": {"noNumeric": True,
  "warn": "No meaningful dose bands for street opioids: fentanyl and nitazenes make milligram numbers meaningless — a 'usual' amount of a different batch kills. Treat ANY reported amount as potentially heavy; focus on breathing, pupils, responsiveness, and naloxone readiness."},
 "benzos-rec": {"noNumeric": True,
  "warn": "No meaningful dose bands for street benzos: pressed bars vary from empty to several-times-normal doses, sometimes with fentanyl or potent analogues (bromazolam). Count pills only to gauge intent; judge severity by sedation level, not reported mg."},
}

TIME_OPTS = [
    {"id": "planned", "label": "Not yet taken"},
    {"id": "lt30", "label": "<30 min ago", "maxMin": 30},
    {"id": "m30-90", "label": "30–90 min ago", "maxMin": 90},
    {"id": "h2-4", "label": "2–4 h ago", "maxMin": 240},
    {"id": "gt4", "label": ">4 h ago", "maxMin": 9999},
    {"id": "repeat", "label": "Repeated doses"},
]
