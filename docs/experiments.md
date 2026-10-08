# Experiments

This page lists **only** what has been documented. Each fact has a source ([references.md](references.md)). Measurements or results that are not documented are left out on purpose.

## Phase 1 — ~1 L experiment

**Details pending.** The maintainer's brief [P3] says AlgaeSense started as a 1 L experiment. Its dates, organism, setup and results are not documented in this repository or in the Instructables article. If you are the maintainer, please add them here with photos or notes as evidence.

## Phase 2 — 10 L automated prototype

Source: Instructables article [P1], published 2026-08-31, unless noted otherwise.

### Setup

| Item | Documented value | Source |
|---|---|---|
| Organism | Spirulina (*Arthrospira*) | [P1] Intro, Step 3 |
| Starter culture | "50 ml of Spirulina mother culture, along with the essential nutrients", sourced from Algreen | [P1] Step 3 |
| Culture volume | "current system of 10 Liters" | [P1] Step 4 |
| Lighting | 4 × 5 V 1 W COB LEDs | [P1] Supplies |
| Aeration | 12 V DC aquarium aerator | [P1] Step 4 |
| Sensors | Temperature sensor and USB microscope ("current sensor stack") | [P1] Step 4 |
| Tank | Laser-cut acrylic, 3D-printed frame, Fusion 360 design | [P1] Steps 5–6 |
| Sampling | DIY peristaltic pump → 3D-printed chamber with acrylic slit | [P1] Step 7 |

### Observations reported

- **Tank sealing:** silicone-sealed acrylic leaked repeatedly. The author cured each attempt for "around 6 hours" over "around three days" ([P1] Step 6).
- **Microscope focus:** moving the USB microscope's focus forward gave usable images ([P1] Step 8; before/after photos in the article).
- **Detection model:** a dataset of "around 100 images", labelled manually ([P1] Step 10). No accuracy figures appear in the text. The model is not in this repo.
- **Control behaviour:** the article says AlgaeSense "works reliably and controls the Photobioreactor autonomously" ([P1] Step 11). No logged data, duration of operation or growth measurements are published to support this, so treat it as the author's qualitative assessment.

### Not documented

- Growth rate, biomass concentration or harvested quantity.
- Temperature, pH or light-intensity readings.
- How long the culture ran, or any culture crashes or contamination events.
- Whether any biomass was eaten or tested.

Contributions of real data (with dates and methods) are very welcome; see [CONTRIBUTING.md](../CONTRIBUTING.md).

### Code during this phase

The code the 10 L prototype ran when the article was published (2026-08-31) matches the 2026-08-25 commits: day/night schedule plus the density heuristic. The code was simplified on 2026-09-13. See [software.md](software.md#version-history-of-the-code).

## Phase 3 — 1,000 L IBC

A **proposal**, not an experiment. See [ibc-1000l/overview.md](ibc-1000l/overview.md).

## How to record a new experiment

When you add a run, please include:

- Start and end dates, culture volume, strain and source of the starter culture.
- Medium recipe and any additions, with dates.
- Light (type, power, hours per day), temperature range, and pH if measured.
- How growth was measured (e.g. dry weight per litre, optical density, Secchi depth) and the raw numbers.
- Problems seen (contaminants, foam, sticking, crashes) and microscope images.
- The git commit of the code used.
