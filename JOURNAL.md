# AlgaeSense project journal

A dated history of the project, using **verified evidence only**. Each entry names its source:

- **git**: this repository's commit history (times in IST, +05:30)
- **Instructables**: the [AlgaeSense article](https://www.instructables.com/AlgaeSense-Grow-Algae-Automatically-As-an-Off-Grid)
- **brief**: the maintainer's project brief (October 2026)

Where something is not documented, this journal says so instead of filling the gap.

---

## Phase 1: ~1 L experiment

**Status: details pending from the maintainer.**

- **brief:** AlgaeSense started as a 1 L experiment.
- Dates, organism, setup, photos and results are **not documented** in this repository or in the Instructables article.

*Maintainer: please add dated notes, photos or other evidence here.*

---

## Phase 2: 10 L automated prototype

| Date (IST) | Event | Evidence |
|---|---|---|
| 2026-08-21 09:47 | Repository created; initial commit with LGPL-2.1 license and one-line README | git `73c7297` |
| 2026-08-21 | README expanded with the concept: "Edge-AI" monitoring, sensor list, control diagram | git `b498cb5` … `2d16f40` |
| 2026-08-25 | First MCU firmware: D5 light, D6 sampling pump, D9 aerator | git `6d0451c`, `d83a624` |
| 2026-08-25 | First Linux app: day/night schedule (06:00–22:00 IST), 60 s sampling cycle, dark-pixel density heuristic, threshold decisions; `AI_ENABLED = False` | git `ecbac5b` |
| 2026-08-25 | App Lab manifest and sketch profile added | git `551dd34`, `e3e3836` |
| 2026-08-31 | Instructables article published ("Off the Grid" contest entry, per Instructables metadata) | Instructables |
| 2026-09-01 | Instructables article last modified | Instructables |
| 2026-09-13 | App simplified to live microscope stream + timed pump; dashboard page added; firmware gets non-blocking pump timer; D9 aerator removed | git `d48128b`, `9585071`, `78c2541` |

### Facts reported in the Instructables article (no dates given)

- Starter: "50 ml of Spirulina mother culture, along with the essential nutrients", sourced from Algreen (Step 3).
- Scale: "current system of 10 Liters" (Step 4).
- Sensors: "limited to temperature sensor and a USB microscope"; pH and dissolved CO₂ planned (Step 4).
- Parts: Arduino UNO Q, BO motor, 3D-printable peristaltic pump, aerator, 4 × 5 V 1 W COB LEDs, temperature probe (Supplies).
- Tank: laser-cut acrylic, Fusion 360 design. Silicone sealing failed repeatedly over "around three days" with "around 6 hours" curing per attempt (Steps 5–6).
- Sampling: food-safe tube → 3D-printed peristaltic pump → 3D-printed chamber with acrylic slit; pump off for 5 s to let the sample settle (Step 7).
- Microscope: a PCB-soldering USB microscope, refocused to see filaments (Step 8).
- Model: a dataset of "around 100 images", labelled manually (Step 10). **Not in this repository.**
- The Instructables page shows a "Runner Up" prize level for the "Off the Grid" contest in its data, but this was **not confirmed on the visible page**.

### Not documented for Phase 2

Growth rates, biomass concentration, harvest quantities, sensor logs, run duration, contamination events.

---

## Phase 3: 1,000 L IBC proposal

**Status: proposal, not built.**

| Date | Event | Evidence |
|---|---|---|
| 2026-10 | 1,000 L indoor IBC design inputs defined; proposal docs and draft BOM written (this PR) | brief; [docs/ibc-1000l/](docs/ibc-1000l/overview.md) |
| 2026-10-23 → 2026-10-31 | Proposal to be presented at Logos x Zu-Grama Field Station, Rajasthan | brief |

Goals for the presentation [brief]: funding, equipment sourcing, collaborators.

---

## How you can help

- **Engineering:**
  - lid and top-entry layout;
  - mixing with air diffusers in a ~1 m deep tank;
  - harvest pump and filter sizing;
  - power and enclosure design;
  - CAD for the 10 L parts.

  See [docs/ibc-1000l/mechanical.md](docs/ibc-1000l/mechanical.md) and [docs/ibc-1000l/electronics.md](docs/ibc-1000l/electronics.md).
- **Biology:**
  - Spirulina culture practice at depth;
  - contamination monitoring;
  - medium recipes;
  - a food-safety testing plan with an accredited lab.

  See [docs/ibc-1000l/cultivation.md](docs/ibc-1000l/cultivation.md) and [docs/ibc-1000l/harvesting.md](docs/ibc-1000l/harvesting.md).
- **Testing:**
  - reproduce the 10 L build and file a [hardware build report](.github/ISSUE_TEMPLATE/hardware_build_report.md);
  - check the `app.yaml` WebUI brick question;
  - calibrate image metrics against dry weight or Secchi depth.
- **Component sourcing:** get quotes for the many "Quote needed" rows in the [draft BOM](docs/ibc-1000l/bom.csv), especially a food-grade IBC, submersible lighting, harvest pump and filter media.

See [CONTRIBUTING.md](CONTRIBUTING.md) to get started.
