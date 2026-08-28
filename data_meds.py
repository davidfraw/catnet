# Curated medication-class x recreational-substance interactions.
# risk: low | caution | high | danger
# ev (evidence): est = well documented | case = case reports / expert consensus | theo = theoretical / limited data
# tpl: mechanism templates from data_core.TEMPLATES
# Sources: TripSit combos DB; Papaseit 2020 (MDMA drug interactions); Sarparast 2022 (psychedelics+psych meds);
# Hysek 2012 (SSRI blunting of MDMA); Richards 2017 & CMAJ 2022 (beta-blockers+stimulants); SPC texts; Erowid/PsychonautWiki summaries.

MED_PAIRS = {
 "ssri": {
  "default": {"risk": "low", "ev": "est", "note": "SSRIs are generally not acutely dangerous with most substances, but they blunt serotonergic drugs — the person may redose chasing an effect that won't come."},
  "pairs": {
   "mdma": {"risk": "high", "ev": "est", "tpl": ["SS", "HYPERTHERMIA"], "note": "SSRIs largely block MDMA's effects (redosing spiral is the practical danger) AND raise serotonin-syndrome risk, especially with redosing or high doses. Case reports of severe outcomes exist.", "donot": ["Do NOT let them redose because 'it isn't working' — that is the SSRI blocking it; more MDMA = more toxicity with no high"]},
   "dxm": {"risk": "danger", "ev": "est", "tpl": ["SS"], "note": "High risk of serotonin syndrome — DXM is a strong serotonin reuptake inhibitor itself."},
   "mephedrone": {"risk": "high", "ev": "case", "tpl": ["SS", "CARDIO"], "note": "Strongly serotonergic stimulant on top of an SSRI — serotonin syndrome risk at recreational doses."},
   "lsd": {"risk": "low", "ev": "est", "note": "Usually just a markedly weakened trip. Do not redose to 'break through'. No major safety signal."},
   "mushrooms": {"risk": "low", "ev": "est", "note": "Usually a markedly weakened trip. Do not redose to 'break through'."},
   "2c-x": {"risk": "caution", "ev": "theo", "note": "Likely blunted; 2C-x series is less predictable than classic psychedelics."},
   "cocaine": {"risk": "caution", "ev": "case", "note": "Mild serotonergic overlap; mainly cocaine undermines the condition the SSRI treats. Watch mood crash after."},
   "amphetamine": {"risk": "caution", "ev": "case", "note": "Generally tolerated acutely; serotonin risk mainly with methamphetamine or high doses."},
   "opioids-rec": {"risk": "caution", "ev": "case", "tpl": ["SS"], "note": "Fentanyl and some opioids add serotonergic load; case reports of serotonin syndrome."},
   "alcohol": {"risk": "caution", "ev": "est", "note": "Additive impairment and judgement effects; hangover + SSRI can worsen mood swings. Not acutely dangerous at moderate intake."},
  }},
 "snri": {
  "default": {"risk": "caution", "ev": "est", "note": "As SSRIs, plus a noradrenergic component — adds heart-rate/blood-pressure load with stimulants."},
  "pairs": {
   "mdma": {"risk": "high", "ev": "est", "tpl": ["SS", "CARDIO", "HYPERTHERMIA"], "note": "Blunted effect (redose temptation) + serotonin syndrome risk + additive blood-pressure/heart-rate load. Venlafaxine is repeatedly implicated in case reports."},
   "dxm": {"risk": "danger", "ev": "est", "tpl": ["SS"], "note": "High serotonin-syndrome risk."},
   "mephedrone": {"risk": "high", "ev": "case", "tpl": ["SS", "CARDIO"], "note": "Serotonergic + cardiovascular double load."},
   "cocaine": {"risk": "high", "ev": "case", "tpl": ["CARDIO"], "note": "Additive noradrenergic strain — blood pressure and heart rate."},
   "amphetamine": {"risk": "high", "ev": "case", "tpl": ["CARDIO"], "note": "Additive cardiovascular strain; monitor pulse and agitation."},
   "lsd": {"risk": "low", "ev": "case", "note": "Usually blunted trip; no major safety signal."},
   "mushrooms": {"risk": "low", "ev": "case", "note": "Usually blunted trip."},
   "alcohol": {"risk": "caution", "ev": "est", "note": "Additive impairment; venlafaxine + heavy drinking raises blood-pressure spikes."},
  }},
 "tca": {
  "default": {"risk": "caution", "ev": "est", "note": "Old-generation antidepressants: cardiotoxic, lower the seizure threshold, strongly sedating/anticholinergic. Treat any combo more seriously than with SSRIs."},
  "pairs": {
   "mdma": {"risk": "danger", "ev": "case", "tpl": ["SS", "CARDIO"], "note": "Serotonin syndrome plus arrhythmia risk — TCAs destabilise cardiac conduction; MDMA adds massive sympathetic load."},
   "amphetamine": {"risk": "high", "ev": "case", "tpl": ["CARDIO", "SEIZURE"], "note": "Arrhythmia and hypertensive risk; TCAs also lower seizure threshold."},
   "cocaine": {"risk": "high", "ev": "case", "tpl": ["CARDIO", "SEIZURE"], "note": "Both destabilise cardiac conduction (sodium-channel effects) — arrhythmia risk well above either alone."},
   "dxm": {"risk": "danger", "ev": "case", "tpl": ["SS"], "note": "Serotonin syndrome risk plus additive anticholinergic delirium."},
   "alcohol": {"risk": "high", "ev": "est", "tpl": ["CNSDEP"], "note": "Strong additive sedation; TCA + alcohol is significantly more impairing than either alone."},
   "ketamine": {"risk": "caution", "ev": "theo", "tpl": ["CARDIO"], "note": "Additive blood-pressure rise and sedation."},
   "ghb": {"risk": "high", "ev": "theo", "tpl": ["CNSDEP"], "note": "Additive CNS depression."},
   "opioids-rec": {"risk": "high", "ev": "case", "tpl": ["CNSDEP"], "note": "Additive sedation and respiratory depression."},
  }},
 "maoi": {
  "default": {"risk": "high", "ev": "est", "note": "MAOIs (including moclobemide) are the single most dangerous medication class for recreational combos. When in doubt, treat any combination as unsafe.", "tpl": ["SS"]},
  "pairs": {
   "mdma": {"risk": "danger", "ev": "est", "tpl": ["SS", "HTN", "HYPERTHERMIA"], "note": "One of the most dangerous festival combinations known — MAOI + MDMA has caused fatal serotonin syndrome and hypertensive crises, including with moclobemide. Absolute avoid; if already taken together, treat as a developing emergency even if they feel fine now."},
   "amphetamine": {"risk": "danger", "ev": "est", "tpl": ["HTN", "CARDIO"], "note": "Hypertensive crisis — MAOIs multiply amphetamine's noradrenaline release."},
   "cocaine": {"risk": "danger", "ev": "case", "tpl": ["HTN", "CARDIO"], "note": "Hypertensive crisis risk; poorly explored, treat as dangerous."},
   "mephedrone": {"risk": "danger", "ev": "case", "tpl": ["SS", "HTN"], "note": "Serotonergic stimulant + MAOI — both serotonin syndrome and hypertensive crisis in play."},
   "dxm": {"risk": "danger", "ev": "est", "tpl": ["SS"], "note": "Classic, well-documented serotonin-syndrome combination."},
   "alcohol": {"risk": "high", "ev": "est", "tpl": ["HTN"], "note": "Tyramine in tap beer and red wine can trigger hypertensive reactions with irreversible MAOIs; moclobemide is more forgiving but caution stands."},
   "opioids-rec": {"risk": "high", "ev": "case", "tpl": ["SS", "CNSDEP"], "note": "Certain opioids (pethidine, fentanyl, tramadol-like) have caused severe reactions with MAOIs."},
   "lsd": {"risk": "caution", "ev": "theo", "note": "MAOIs may blunt or alter the trip; less dangerous than stimulant combos but unpredictable."},
   "mushrooms": {"risk": "caution", "ev": "theo", "note": "MAO inhibition potentiates tryptamines (ayahuasca principle) — trip may be much stronger and longer than expected."},
   "2c-x": {"risk": "danger", "ev": "case", "tpl": ["SS", "HTN"], "note": "MAOIs potentiate phenethylamines unpredictably — treat as dangerous."},
   "ketamine": {"risk": "caution", "ev": "theo", "note": "Limited data; possible potentiation."},
   "cannabis": {"risk": "caution", "ev": "theo", "note": "Possible potentiation of tachycardia; limited data."},
   "caffeine": {"risk": "caution", "ev": "case", "note": "Can add to blood-pressure load; keep intake modest."},
  }},
 "bupropion": {
  "default": {"risk": "caution", "ev": "est", "note": "Bupropion lowers the seizure threshold and blocks CYP2D6 (raises blood levels of MDMA, DXM and codeine-type opioids)."},
  "pairs": {
   "amphetamine": {"risk": "high", "ev": "case", "tpl": ["CARDIO", "SEIZURE", "PSYCH"], "note": "Stimulant-on-stimulant: cardiovascular load, insomnia, seizure risk."},
   "cocaine": {"risk": "high", "ev": "case", "tpl": ["CARDIO", "SEIZURE"], "note": "Additive stimulant strain and lowered seizure threshold."},
   "mephedrone": {"risk": "high", "ev": "theo", "tpl": ["CARDIO", "SEIZURE"], "note": "As with other stimulants — seizure and cardiac risk."},
   "mdma": {"risk": "high", "ev": "est", "tpl": ["CARDIO", "SEIZURE"], "note": "Bupropion raises MDMA blood levels (CYP2D6 block) and adds seizure risk; effects last longer and hit harder than expected."},
   "dxm": {"risk": "high", "ev": "est", "tpl": ["SS", "SEIZURE"], "note": "CYP2D6 block can multiply DXM levels — an 'ordinary' dose can behave like a heavy one."},
   "alcohol": {"risk": "caution", "ev": "est", "tpl": ["SEIZURE"], "note": "Heavy drinking (and especially abrupt withdrawal) plus bupropion raises seizure risk."},
   "lsd": {"risk": "caution", "ev": "theo", "note": "Limited data; mild stimulant overlap."},
  }},
 "sedad": {
  "default": {"risk": "caution", "ev": "est", "note": "Trazodone and mirtazapine are strongly sedating — the main issue is stacking with other downers."},
  "pairs": {
   "alcohol": {"risk": "high", "ev": "est", "tpl": ["CNSDEP"], "note": "Marked additive sedation — a common real-world combo that ends in deep unrousable sleep; airway watch."},
   "ghb": {"risk": "danger", "ev": "theo", "tpl": ["CNSDEP"], "note": "Two strong sedatives with steep curves — high risk of unconsciousness and breathing depression."},
   "opioids-rec": {"risk": "high", "ev": "case", "tpl": ["CNSDEP"], "note": "Additive sedation and respiratory depression."},
   "benzos-rec": {"risk": "high", "ev": "est", "tpl": ["CNSDEP"], "note": "Additive sedation; blackout risk."},
   "ketamine": {"risk": "caution", "ev": "theo", "tpl": ["CNSDEP"], "note": "Additive sedation; falls and airway."},
   "mdma": {"risk": "caution", "ev": "case", "tpl": ["SS"], "note": "Trazodone adds some serotonergic load and may blunt MDMA; mirtazapine may blunt it strongly. Low-grade serotonin-syndrome risk, watch for twitching/agitation."},
   "dxm": {"risk": "high", "ev": "case", "tpl": ["SS", "CNSDEP"], "note": "Serotonergic + sedative stacking."},
  }},
 "lithium": {
  "default": {"risk": "caution", "ev": "est", "note": "Lithium has a narrow safety window: festival dehydration, heavy sweating or vomiting RAISES lithium levels. Watch for lithium toxicity (coarse tremor, vomiting, confusion, unsteady gait) in any scenario.", "donot": ["Do NOT let a person on lithium get dehydrated — regular fluids with electrolytes matter more than any single combo rule"]},
  "pairs": {
   "lsd": {"risk": "danger", "ev": "case", "tpl": ["SEIZURE", "PSYCH"], "note": "Large body of reports of seizures and dangerous trips on lithium + psychedelics — one of the strongest 'do not combine' signals in the psychedelic literature."},
   "mushrooms": {"risk": "danger", "ev": "case", "tpl": ["SEIZURE", "PSYCH"], "note": "Same signal as LSD: seizure and psychosis reports."},
   "2c-x": {"risk": "danger", "ev": "case", "tpl": ["SEIZURE", "PSYCH"], "note": "Seizure risk as with other psychedelics."},
   "mdma": {"risk": "danger", "ev": "case", "tpl": ["SS", "HYPERTHERMIA"], "note": "Serotonin-syndrome risk plus MDMA dehydration concentrating lithium — double mechanism."},
   "dxm": {"risk": "danger", "ev": "case", "tpl": ["SS"], "note": "Serotonin-syndrome risk."},
   "alcohol": {"risk": "caution", "ev": "est", "note": "Dehydration + vomiting can push lithium toward toxic levels; hydrate with electrolytes."},
   "amphetamine": {"risk": "caution", "ev": "theo", "tpl": ["HYPERTHERMIA"], "note": "Sweating/dehydration raising lithium levels is the main concern."},
   "cocaine": {"risk": "caution", "ev": "case", "note": "Lithium may blunt cocaine's effects (redose temptation); dehydration concern stands."},
   "ketamine": {"risk": "low", "ev": "case", "note": "No major acute interaction signal."},
  }},
 "antipsych": {
  "default": {"risk": "caution", "ev": "est", "note": "Antipsychotics blunt stimulants and psychedelics (redose temptation), add sedation, and several (quetiapine, olanzapine) prolong QT and drop blood pressure on standing — fainting in heat is common."},
  "pairs": {
   "alcohol": {"risk": "high", "ev": "est", "tpl": ["CNSDEP"], "note": "Quetiapine + alcohol is heavily sedating; orthostatic fainting in hot crowds."},
   "ghb": {"risk": "danger", "ev": "theo", "tpl": ["CNSDEP"], "note": "Strong additive sedation with a steep-curve depressant."},
   "opioids-rec": {"risk": "high", "ev": "case", "tpl": ["CNSDEP"], "note": "Additive sedation and respiratory depression."},
   "benzos-rec": {"risk": "high", "ev": "est", "tpl": ["CNSDEP"], "note": "Additive sedation."},
   "ketamine": {"risk": "caution", "ev": "theo", "tpl": ["CNSDEP"], "note": "Additive sedation; falls."},
   "mdma": {"risk": "caution", "ev": "case", "tpl": ["CARDIO"], "note": "Blunted effect plus QT-prolongation overlap; the practical risk is redosing and arrhythmia in a dehydrated overheated body."},
   "amphetamine": {"risk": "caution", "ev": "case", "note": "Pharmacological tug-of-war: blunted high, redose temptation, arrhythmia overlap with some agents."},
   "cocaine": {"risk": "caution", "ev": "case", "note": "As amphetamine; also lowers seizure threshold with clozapine-type agents."},
   "lsd": {"risk": "caution", "ev": "case", "note": "May blunt or abort the trip (quetiapine is sometimes used that way clinically) — but unsupervised redosing is the risk."},
  }},
 "anticonv": {
  "default": {"risk": "low", "ev": "est", "note": "Generally low acute interaction. The bigger festival risk is MISSED DOSES + sleep deprivation + stimulants lowering the seizure threshold. Carbamazepine speeds up breakdown of many drugs (weaker, shorter effects — redose temptation).", "donot": ["Do NOT let them skip their anticonvulsant doses during the festival"]},
  "pairs": {
   "alcohol": {"risk": "caution", "ev": "est", "tpl": ["SEIZURE"], "note": "Heavy drinking and especially next-day withdrawal lower the seizure threshold; valproate adds liver load."},
   "amphetamine": {"risk": "caution", "ev": "theo", "tpl": ["SEIZURE"], "note": "Sleep deprivation + stimulants is a classic seizure trigger in people with epilepsy."},
   "mdma": {"risk": "caution", "ev": "theo", "tpl": ["SEIZURE", "HYPERTHERMIA"], "note": "Hyponatremia from water-loading is itself a seizure trigger — fluid advice matters double here."},
   "cocaine": {"risk": "caution", "ev": "case", "tpl": ["SEIZURE"], "note": "Cocaine independently provokes seizures."},
  }},
 "adhd-stim": {
  "default": {"risk": "caution", "ev": "est", "note": "Prescribed stimulants (methylphenidate, lisdexamfetamine, amphetamine salts) add to any other stimulant's cardiovascular load. Common and mostly uneventful with moderation — but the ceiling is lower for everything stimulating."},
  "pairs": {
   "mdma": {"risk": "high", "ev": "est", "tpl": ["CARDIO", "HYPERTHERMIA"], "note": "Very common combo: additive heart-rate/blood-pressure/temperature load. Lisdexamfetamine (Vyvanse/Elvanse) IS amphetamine — effectively double-dosing. Insist on cooling breaks and electrolytes; strongly discourage MDMA redosing."},
   "amphetamine": {"risk": "high", "ev": "est", "tpl": ["CARDIO", "PSYCH"], "note": "Same class on top of prescribed dose — overdose-range stimulation, insomnia, psychosis risk with sleep loss."},
   "cocaine": {"risk": "high", "ev": "est", "tpl": ["CARDIO"], "note": "Additive cardiovascular strain; chest pain must be taken seriously."},
   "mephedrone": {"risk": "high", "ev": "case", "tpl": ["CARDIO", "SS"], "note": "Additive stimulant + serotonergic load."},
   "caffeine": {"risk": "caution", "ev": "est", "note": "Energy drinks on top of ADHD meds: jitteriness, palpitations, panic. Keep to a minimum."},
   "alcohol": {"risk": "caution", "ev": "est", "note": "Stimulant masks drunkenness — people drink past their limit, then the stimulant wears off first. Watch for sudden collapse late at night."},
   "ketamine": {"risk": "caution", "ev": "theo", "note": "Stimulant may mask sedation, inviting ketamine redosing; watch when stimulant fades."},
   "lsd": {"risk": "caution", "ev": "case", "tpl": ["PSYCH", "CARDIO"], "note": "Additive heart-rate load and higher anxiety/thought-loop risk."},
   "mushrooms": {"risk": "caution", "ev": "case", "tpl": ["PSYCH"], "note": "As LSD — anxiety amplification."},
   "dxm": {"risk": "high", "ev": "case", "tpl": ["CARDIO", "SS"], "note": "Sympathetic + serotonergic load; avoid."},
   "ghb": {"risk": "caution", "ev": "theo", "tpl": ["CNSDEP"], "note": "Stimulant masks GHB sedation — when it wears off, the full depressant load lands at once."},
  }},
 "atomoxetine": {
  "default": {"risk": "caution", "ev": "theo", "note": "Non-stimulant but noradrenergic — adds some heart-rate/blood-pressure load; also competes for CYP2D6."},
  "pairs": {
   "mdma": {"risk": "caution", "ev": "theo", "tpl": ["CARDIO"], "note": "Additive noradrenergic load; possible higher MDMA levels via CYP2D6 competition."},
   "amphetamine": {"risk": "caution", "ev": "theo", "tpl": ["CARDIO"], "note": "Additive cardiovascular load."},
   "cocaine": {"risk": "caution", "ev": "theo", "tpl": ["CARDIO"], "note": "Additive cardiovascular load."},
  }},
 "benzo-rx": {
  "default": {"risk": "caution", "ev": "est", "note": "Prescribed benzos behave exactly like street benzos in combos: safe-ish alone, dangerous stacked with other downers."},
  "pairs": {
   "alcohol": {"risk": "danger", "ev": "est", "tpl": ["CNSDEP"], "note": "The classic blackout combination — strong unpredictable potentiation, rapid unconsciousness, vomit-aspiration risk."},
   "ghb": {"risk": "danger", "ev": "est", "tpl": ["CNSDEP"], "note": "Strong potentiation, rapid unconsciousness."},
   "opioids-rec": {"risk": "danger", "ev": "est", "tpl": ["CNSDEP"], "note": "Benzo + opioid is the signature respiratory-depression death combo."},
   "ketamine": {"risk": "high", "ev": "est", "tpl": ["CNSDEP"], "note": "Additive sedation and ataxia; falls and airway."},
   "dxm": {"risk": "caution", "ev": "est", "tpl": ["CNSDEP"], "note": "Additive sedation at higher doses."},
   "benzos-rec": {"risk": "high", "ev": "est", "tpl": ["CNSDEP"], "note": "Stacking doses of the same class — easy to overshoot into blackout."},
   "amphetamine": {"risk": "caution", "ev": "est", "note": "Opposing effects mask each other; overdose risk when one wears off first."},
   "mdma": {"risk": "low", "ev": "est", "note": "Benzo blunts the comedown; main issue is sedation once MDMA fades."},
   "cannabis": {"risk": "caution", "ev": "est", "note": "Additive sedation and impairment."},
  }},
 "z-drug": {
  "default": {"risk": "caution", "ev": "est", "note": "Zolpidem/zopiclone act on the same receptors as benzos — treat all combos like benzodiazepine combos. Zolpidem alone can cause sleep-walking; with alcohol this gets dangerous."},
  "pairs": {
   "alcohol": {"risk": "danger", "ev": "est", "tpl": ["CNSDEP"], "note": "Strong potentiation + amnesia/sleep-walking behaviour; vomit-aspiration risk."},
   "ghb": {"risk": "danger", "ev": "est", "tpl": ["CNSDEP"], "note": "As benzos + GHB — rapid unconsciousness."},
   "opioids-rec": {"risk": "danger", "ev": "est", "tpl": ["CNSDEP"], "note": "Respiratory depression stacking."},
   "ketamine": {"risk": "high", "ev": "theo", "tpl": ["CNSDEP"], "note": "Additive sedation."},
   "benzos-rec": {"risk": "high", "ev": "est", "tpl": ["CNSDEP"], "note": "Same receptor system — doses stack."},
  }},
 "melatonin": {
  "default": {"risk": "low", "ev": "est", "note": "Melatonin has no significant dangerous interaction with recreational substances — mild extra drowsiness with depressants at most."},
  "pairs": {
   "alcohol": {"risk": "low", "ev": "est", "note": "Mild additive drowsiness; not dangerous."},
  }},
 "pregabalin": {
  "default": {"risk": "caution", "ev": "est", "note": "Pregabalin/gabapentin potentiate depressants strongly and have their own seizure quirks at high doses."},
  "pairs": {
   "alcohol": {"risk": "danger", "ev": "est", "tpl": ["CNSDEP"], "note": "Strong, well-documented potentiation — a major factor in pregabalin-related deaths."},
   "opioids-rec": {"risk": "danger", "ev": "est", "tpl": ["CNSDEP"], "note": "Documented multiplier of opioid respiratory depression."},
   "ghb": {"risk": "danger", "ev": "est", "tpl": ["CNSDEP"], "note": "Strong unpredictable potentiation."},
   "benzos-rec": {"risk": "high", "ev": "est", "tpl": ["CNSDEP"], "note": "Additive sedation, memory loss, ataxia."},
   "mdma": {"risk": "high", "ev": "case", "tpl": ["SEIZURE"], "note": "Seizure-risk signal for the combination (TripSit rates it unsafe); stimulant masking of sedation."},
   "amphetamine": {"risk": "high", "ev": "case", "tpl": ["SEIZURE"], "note": "Seizure-risk signal; stimulant masks sedation, which lands when it wears off."},
   "cocaine": {"risk": "high", "ev": "case", "tpl": ["SEIZURE"], "note": "As amphetamine."},
   "ketamine": {"risk": "caution", "ev": "case", "tpl": ["CNSDEP"], "note": "Additive dizziness, nausea, loss of consciousness at higher doses."},
   "dxm": {"risk": "high", "ev": "case", "tpl": ["CNSDEP", "SEIZURE"], "note": "Additive sedation + seizure concerns."},
   "nitrous": {"risk": "caution", "ev": "case", "note": "Additive ataxia/sedation — do it sitting down, watch airway."},
  }},
 "antihist-sed": {
  "default": {"risk": "caution", "ev": "est", "note": "First-generation antihistamines (diphenhydramine, promethazine, doxylamine) are anticholinergic downers: they stack with depressants and add delirium risk at high doses. Promethazine also prolongs QT."},
  "pairs": {
   "alcohol": {"risk": "danger", "ev": "est", "tpl": ["CNSDEP"], "note": "Strong unpredictable potentiation — rapid unconsciousness."},
   "ghb": {"risk": "danger", "ev": "est", "tpl": ["CNSDEP"], "note": "Strong potentiation."},
   "opioids-rec": {"risk": "high", "ev": "est", "tpl": ["CNSDEP"], "note": "Additive CNS depression."},
   "benzos-rec": {"risk": "high", "ev": "est", "tpl": ["CNSDEP"], "note": "Additive sedation and ataxia."},
   "ketamine": {"risk": "high", "ev": "case", "tpl": ["CNSDEP"], "note": "Additive sedation, loss of consciousness at high doses."},
   "dxm": {"risk": "high", "ev": "est", "tpl": ["SS", "CNSDEP"], "note": "Serotonin syndrome + delirium + CNS depression — a genuinely bad combination."},
   "mdma": {"risk": "caution", "ev": "case", "tpl": ["HYPERTHERMIA"], "note": "Anticholinergics impair sweating — worse heat tolerance while dancing. QT overlap with promethazine."},
   "amphetamine": {"risk": "caution", "ev": "case", "note": "Stimulant masks sedation and delirium warning signs."},
   "cocaine": {"risk": "caution", "ev": "case", "note": "Masking as with amphetamine; respiratory-arrest risk if cocaine wears off first after heavy antihistamine doses."},
   "cannabis": {"risk": "caution", "ev": "theo", "note": "Additive drowsiness and dry-mouth/tachycardia."},
  }},
 "antihist-nonsed": {
  "default": {"risk": "low", "ev": "est", "note": "Good news: modern allergy meds (cetirizine, loratadine, levocetirizine, desloratadine, fexofenadine) at normal doses have no meaningful dangerous interaction with recreational substances."},
  "pairs": {
   "alcohol": {"risk": "low", "ev": "est", "note": "Cetirizine can add mild drowsiness with alcohol; loratadine/fexofenadine barely at all. Not dangerous."},
  }},
 "tramadol": {
  "default": {"risk": "high", "ev": "est", "note": "Tramadol is an opioid AND a serotonin/noradrenaline releaser AND lowers the seizure threshold — it interacts badly with almost everything. Treat any tramadol combo as elevated risk.", "tpl": ["SEIZURE"]},
  "pairs": {
   "alcohol": {"risk": "danger", "ev": "est", "tpl": ["CNSDEP", "SEIZURE"], "note": "Heavy CNS depression + seizure risk."},
   "mdma": {"risk": "danger", "ev": "est", "tpl": ["SS", "SEIZURE"], "note": "Serotonin syndrome + seizures — documented combination."},
   "amphetamine": {"risk": "danger", "ev": "est", "tpl": ["SEIZURE", "CARDIO"], "note": "Both lower seizure threshold."},
   "cocaine": {"risk": "danger", "ev": "est", "tpl": ["SEIZURE", "CARDIO"], "note": "Both lower seizure threshold."},
   "mephedrone": {"risk": "danger", "ev": "est", "tpl": ["SS", "SEIZURE", "CARDIO"], "note": "Serotonin syndrome and seizure risk at recreational doses."},
   "dxm": {"risk": "danger", "ev": "est", "tpl": ["SS"], "note": "High serotonin-syndrome risk."},
   "ghb": {"risk": "danger", "ev": "est", "tpl": ["CNSDEP"], "note": "Dangerous respiratory depression."},
   "benzos-rec": {"risk": "danger", "ev": "est", "tpl": ["CNSDEP"], "note": "Additive respiratory depression."},
   "opioids-rec": {"risk": "danger", "ev": "est", "tpl": ["CNSDEP", "SEIZURE"], "note": "Opioid stacking + additive seizure risk."},
   "ketamine": {"risk": "high", "ev": "est", "tpl": ["CNSDEP"], "note": "Additive sedation; seizure signal."},
   "lsd": {"risk": "high", "ev": "case", "tpl": ["SEIZURE"], "note": "Tramadol lowers seizure threshold; psychedelics occasionally provoke seizures."},
   "mushrooms": {"risk": "high", "ev": "case", "tpl": ["SEIZURE"], "note": "As LSD."},
   "2c-x": {"risk": "high", "ev": "case", "tpl": ["SEIZURE"], "note": "As LSD — seizure threshold."},
   "nitrous": {"risk": "caution", "ev": "case", "note": "Additive sedation/ataxia; sit down."},
   "cannabis": {"risk": "low", "ev": "est", "note": "Mild synergy; not a major safety signal."},
  }},
 "opioid-rx": {
  "default": {"risk": "caution", "ev": "est", "note": "Prescribed opioids (codeine, oxycodone, fentanyl patches) carry the same combo risks as street opioids. Heat can increase fentanyl-patch release."},
  "pairs": {
   "alcohol": {"risk": "danger", "ev": "est", "tpl": ["CNSDEP"], "note": "Respiratory depression stacking; unexpected loss of consciousness."},
   "benzos-rec": {"risk": "danger", "ev": "est", "tpl": ["CNSDEP"], "note": "The signature overdose combination."},
   "ghb": {"risk": "danger", "ev": "est", "tpl": ["CNSDEP"], "note": "Rapid unconsciousness, respiratory depression."},
   "ketamine": {"risk": "danger", "ev": "est", "tpl": ["CNSDEP"], "note": "Vomiting + unconsciousness — high aspiration risk outside recovery position."},
   "dxm": {"risk": "danger", "ev": "est", "tpl": ["CNSDEP", "SS"], "note": "CNS depression + serotonergic load; DXM also drops opioid tolerance slightly."},
   "cocaine": {"risk": "high", "ev": "est", "tpl": ["CNSDEP"], "note": "Stimulant masks opioid sedation — respiratory arrest when cocaine wears off first."},
   "amphetamine": {"risk": "caution", "ev": "est", "tpl": ["CNSDEP"], "note": "Masking dynamic as with cocaine."},
   "nitrous": {"risk": "caution", "ev": "case", "tpl": ["CNSDEP"], "note": "Additive sedation; unexpected loss of consciousness at high doses."},
   "cannabis": {"risk": "low", "ev": "est", "note": "Mild synergy, mainly more sedation."},
   "mdma": {"risk": "caution", "ev": "case", "note": "Masking dynamic; some serotonergic opioids (fentanyl) add serotonin load."},
  }},
 "beta-blocker": {
  "default": {"risk": "caution", "ev": "est", "note": "Key field fact: a person on beta-blockers may NOT show a fast pulse even in serious stimulant toxicity — don't use heart rate alone to judge how bad it is."},
  "pairs": {
   "cocaine": {"risk": "high", "ev": "case", "tpl": ["CARDIO"], "note": "Traditional teaching says beta-blockade + cocaine risks 'unopposed alpha' blood-pressure spikes and coronary spasm; recent reviews dispute how real this is — but chest pain here is an unambiguous 112 call. The masking of tachycardia is the certain problem.", "donot": ["Do NOT give extra doses of their beta-blocker during stimulant use — disputed medicine, strictly a hospital decision"]},
   "amphetamine": {"risk": "high", "ev": "theo", "tpl": ["CARDIO"], "note": "Same unopposed-alpha concern and warning-sign masking as cocaine."},
   "mdma": {"risk": "caution", "ev": "theo", "tpl": ["CARDIO", "HYPERTHERMIA"], "note": "Masked tachycardia + reduced exercise tolerance while dancing in heat; fainting risk."},
   "mephedrone": {"risk": "high", "ev": "theo", "tpl": ["CARDIO"], "note": "As other stimulants."},
   "alcohol": {"risk": "caution", "ev": "est", "note": "Additive blood-pressure drop on standing — fainting in hot crowds; alcohol can mask hypoglycemia-like symptoms."},
   "cannabis": {"risk": "caution", "ev": "theo", "note": "Orthostatic hypotension additive with THC — dizziness on standing."},
   "ketamine": {"risk": "low", "ev": "theo", "note": "No major signal at recreational doses."},
  }},
 "antihyp": {
  "default": {"risk": "caution", "ev": "est", "note": "Blood-pressure meds + heat + dancing + alcohol = fainting. Diuretics (hydrochlorothiazide, indapamide) also worsen dehydration and electrolyte loss."},
  "pairs": {
   "mdma": {"risk": "high", "ev": "case", "tpl": ["HYPERTHERMIA", "CARDIO"], "note": "Diuretics + MDMA is a genuinely bad pair: dehydration, electrolyte loss and higher hyponatremia risk. Blood-pressure swings both directions.", "donot": ["Do NOT push plain water — electrolyte drinks in sips; this person's sodium balance is already medicated"]},
   "alcohol": {"risk": "caution", "ev": "est", "note": "Additive hypotension — dizziness, fainting on standing; dehydration."},
   "amphetamine": {"risk": "caution", "ev": "theo", "tpl": ["CARDIO"], "note": "Stimulants push against the medication — blood pressure may spike beyond their controlled baseline."},
   "cocaine": {"risk": "caution", "ev": "theo", "tpl": ["CARDIO"], "note": "As amphetamine."},
   "ghb": {"risk": "caution", "ev": "theo", "tpl": ["CNSDEP"], "note": "Additive hypotension and sedation."},
  }},
 "diabetes": {
  "default": {"risk": "caution", "ev": "est", "note": "The festival pattern — skipped meals, dancing, alcohol — destabilises glucose regardless of the substance. Make sure they eat and can test."},
  "pairs": {
   "alcohol": {"risk": "high", "ev": "est", "tpl": ["HYPOGLY"], "note": "Alcohol blocks the liver's glucose release: delayed hypoglycemia (often hours later or overnight) that looks exactly like being drunk. On insulin or gliclazide this is the top festival risk for this person."},
   "mdma": {"risk": "caution", "ev": "case", "tpl": ["HYPOGLY", "HYPERTHERMIA"], "note": "Appetite suppression + dancing + possible vomiting = glucose chaos; dehydration also matters for metformin."},
   "amphetamine": {"risk": "caution", "ev": "case", "tpl": ["HYPOGLY"], "note": "Appetite suppression and missed meals over many hours."},
   "cocaine": {"risk": "caution", "ev": "case", "tpl": ["HYPOGLY"], "note": "As amphetamine."},
   "ghb": {"risk": "caution", "ev": "theo", "tpl": ["CNSDEP", "HYPOGLY"], "note": "Unconsciousness from GHB vs hypoglycemia can be confused — check glucose if possible, treat breathing first."},
  }},
 "asthma": {
  "default": {"risk": "low", "ev": "est", "note": "Reliever inhalers interact little — the rule is the opposite: make sure the inhaler is WITH them and reachable.", "donot": ["Do NOT separate the person from their inhaler (lockers, lost bags — check early)"]},
  "pairs": {
   "amphetamine": {"risk": "caution", "ev": "theo", "note": "Salbutamol + stimulant = additive tachycardia and tremor; still, never withhold the inhaler in an asthma attack."},
   "mdma": {"risk": "caution", "ev": "theo", "note": "As amphetamine; dusty dancefloors and smoke are the real triggers."},
   "cocaine": {"risk": "caution", "ev": "case", "note": "Smoked/snorted cocaine irritates airways and can trigger bronchospasm; additive tachycardia with salbutamol."},
   "cannabis": {"risk": "caution", "ev": "est", "note": "Smoking anything can trigger bronchospasm in asthmatics; edibles avoid this."},
  }},
 "contraception": {
  "default": {"risk": "low", "ev": "est", "note": "No acute dangerous interaction with recreational substances."},
  "pairs": {
   "alcohol": {"risk": "low", "ev": "est", "note": "Practical note: vomiting within ~3–4 h of taking the pill can reduce contraceptive protection — worth mentioning if they've been sick."},
   "mdma": {"risk": "low", "ev": "est", "note": "Same vomiting caveat; no direct interaction."},
  }},
 "pde5": {
  "default": {"risk": "caution", "ev": "est", "note": "Sildenafil/tadalafil drop blood pressure. NEVER combined with poppers/nitrites — that combination causes life-threatening pressure crashes."},
  "pairs": {
   "cocaine": {"risk": "high", "ev": "case", "tpl": ["CARDIO"], "note": "Both strain the heart in opposite blood-pressure directions; combined with cocaine's coronary spasm this raises cardiac-event risk. Chest pain → 112, and tell the crew sildenafil is on board (matters for their treatment)."},
   "amphetamine": {"risk": "caution", "ev": "theo", "tpl": ["CARDIO"], "note": "Additive cardiac workload."},
   "mdma": {"risk": "caution", "ev": "case", "tpl": ["CARDIO"], "note": "Additive cardiac workload; 'sextasy' combo is common — flag the chest-pain rule."},
   "alcohol": {"risk": "caution", "ev": "est", "note": "Additive blood-pressure drop — dizziness, fainting."},
  }},
 "sjw": {
  "default": {"risk": "caution", "ev": "est", "note": "St John's Wort is a real serotonergic drug and enzyme inducer that people forget to mention. Ask about it specifically."},
  "pairs": {
   "mdma": {"risk": "high", "ev": "case", "tpl": ["SS"], "note": "Additive serotonergic load — serotonin-syndrome case reports; also alters MDMA metabolism."},
   "dxm": {"risk": "high", "ev": "case", "tpl": ["SS"], "note": "Additive serotonergic load."},
   "mephedrone": {"risk": "caution", "ev": "theo", "tpl": ["SS"], "note": "Additive serotonergic load."},
  }},
}

# Critical medication x medication cross-checks (both selected as "takes these meds")
MED_MED = [
 {"a": "maoi", "b": "ssri", "risk": "danger", "ev": "est", "tpl": ["SS"], "note": "MAOI + SSRI is a classic serotonin-syndrome combination — should never be co-prescribed; if reported together, verify and treat any symptoms as urgent."},
 {"a": "maoi", "b": "snri", "risk": "danger", "ev": "est", "tpl": ["SS"], "note": "As MAOI + SSRI."},
 {"a": "maoi", "b": "tca", "risk": "danger", "ev": "est", "tpl": ["SS", "HTN"], "note": "Dangerous serotonergic/hypertensive combination."},
 {"a": "maoi", "b": "tramadol", "risk": "danger", "ev": "est", "tpl": ["SS", "SEIZURE"], "note": "Contraindicated — serotonin syndrome and seizures."},
 {"a": "maoi", "b": "bupropion", "risk": "danger", "ev": "est", "note": "Contraindicated combination."},
 {"a": "maoi", "b": "adhd-stim", "risk": "danger", "ev": "est", "tpl": ["HTN"], "note": "Hypertensive crisis risk — contraindicated."},
 {"a": "maoi", "b": "sjw", "risk": "high", "ev": "case", "tpl": ["SS"], "note": "Additive MAO/serotonergic activity."},
 {"a": "ssri", "b": "tramadol", "risk": "high", "ev": "est", "tpl": ["SS", "SEIZURE"], "note": "Well-documented serotonin-syndrome and seizure risk — a common real-world prescribing clash."},
 {"a": "snri", "b": "tramadol", "risk": "high", "ev": "est", "tpl": ["SS", "SEIZURE"], "note": "As SSRI + tramadol."},
 {"a": "ssri", "b": "sjw", "risk": "high", "ev": "est", "tpl": ["SS"], "note": "Additive serotonergic load — advise against combining."},
 {"a": "snri", "b": "sjw", "risk": "high", "ev": "est", "tpl": ["SS"], "note": "As SSRI + St John's Wort."},
 {"a": "lithium", "b": "tramadol", "risk": "danger", "ev": "est", "tpl": ["SS", "SEIZURE"], "note": "Both raise seizure and serotonin-syndrome risk."},
 {"a": "bupropion", "b": "tramadol", "risk": "high", "ev": "est", "tpl": ["SEIZURE"], "note": "Both lower the seizure threshold; bupropion also raises tramadol levels."},
 {"a": "tca", "b": "tramadol", "risk": "high", "ev": "est", "tpl": ["SS", "SEIZURE"], "note": "Seizure threshold + serotonergic overlap."},
 {"a": "benzo-rx", "b": "opioid-rx", "risk": "danger", "ev": "est", "tpl": ["CNSDEP"], "note": "Prescribed or not, benzo + opioid stacking is the signature respiratory-depression risk."},
 {"a": "benzo-rx", "b": "pregabalin", "risk": "high", "ev": "est", "tpl": ["CNSDEP"], "note": "Additive CNS depression."},
 {"a": "z-drug", "b": "opioid-rx", "risk": "high", "ev": "est", "tpl": ["CNSDEP"], "note": "Additive CNS depression."},
 {"a": "opioid-rx", "b": "pregabalin", "risk": "danger", "ev": "est", "tpl": ["CNSDEP"], "note": "Documented multiplier of opioid respiratory depression."},
 {"a": "antihist-sed", "b": "benzo-rx", "risk": "high", "ev": "est", "tpl": ["CNSDEP"], "note": "Additive sedation."},
 {"a": "antihist-sed", "b": "opioid-rx", "risk": "high", "ev": "est", "tpl": ["CNSDEP"], "note": "Additive CNS depression."},
]
