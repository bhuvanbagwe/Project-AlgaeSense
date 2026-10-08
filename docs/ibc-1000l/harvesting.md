# 1,000 L IBC — harvesting and filtration

> **⚠️ PROPOSAL — NOT BUILT.** No harvesting has been automated or documented in this project, at any scale. Numbers marked **Estimate** are back-of-envelope figures with the working shown. **Food safety is unresolved:** nothing harvested by this system should be eaten unless it has been tested. See [overview.md](overview.md).

## Validated (from the 10 L prototype)

- **Nothing about harvesting.** The Instructables article talks about harvesting as the goal ([P1] Step 11). It does not document a harvesting method, harvested quantity or test results.
- The DIY peristaltic pump moved culture for **sampling** ([P1] Step 7), not for harvesting.

## Existing research

| Topic | What the literature says | Source |
|---|---|---|
| Filament size | Trichomes 50–500 µm long, 3–4 µm wide | [F1] p. 3 |
| When to harvest (small scale) | Let concentration reach about 0.5 g/L (Secchi disk about 2 cm) before harvesting | [J1] p. 5 |
| Pre-screening | Pass culture through a sieve of about 200 µm to remove insects, larvae, debris, lumps | [J1] p. 6 |
| Filter medium (small scale) | Polyamide or polyester cloth, mesh about 30–50 µm, gravity-driven; filter can sit above the pond to recycle filtrate directly | [J1] p. 6 |
| Straight filaments | Straight Spirulina is more difficult to harvest | [J1] p. 6 |
| Commercial screens | Inclined screens of 380–500 mesh, 2–4 m² each, handle 10–18 m³/h; up to 95 % removal | [F1] p. 17 |
| Pumping damage | Pumping culture to filters can physically damage filaments. Repeated harvesting can enrich the culture with short filaments or unicellular algae that pass through the screen | [F1] p. 17 |
| Processing | Stages include filtration, washing, concentration, drying, packing and hygienic storage | [F1] p. 17 |
| Drying (small scale) | Limit drying to 68 °C and 7 hours | [J1] p. 11 |
| Quality control | Food-standard spirulina is tested for microbiology, chemical composition, heavy metals, pesticides and extraneous material | [F1] p. 17 |
| Contamination timing | "Contaminations most generally occur during or after harvesting"; microbiological assay of the product at least yearly | [J1] p. 10 |

## Estimates

**How much biomass is in a partial harvest** (illustration, not a yield prediction):

- harvest 10 % of the volume = 100 L;
- at the ~0.5 g/L harvest concentration from [J1]: 100 L × 0.5 g/L ≈ **50 g dry-matter equivalent** per such harvest.

*Estimate.* Real values depend entirely on growth, which has not been measured.

**Pump time for 100 L at different flow rates:**

| Pump class | Flow | Time for 100 L | Working |
|---|---|---|---|
| Small dosing peristaltic (e.g. the 2–17 ml/min Robu listing in [bom.csv](bom.csv)) | 0.017 L/min | ≈ 98 h | 100 ÷ 0.017 ≈ 5,880 min |
| Hypothetical harvest pump | 1 L/min | 100 min | 100 ÷ 1 |
| Hypothetical harvest pump | 5 L/min | 20 min | 100 ÷ 5 |

*Estimates.* The point: **dosing-class pumps cannot harvest** at this scale. A peristaltic pump in the **L/min** range is needed, and whether it damages filaments ([F1] p. 17) is untested.

**Filter area.** Not estimated. No filtration-rate data for 30–50 µm cloth with this culture exists in the project. Needs a bench test at 10 L.

## Engineering assumptions

- Harvesting is **batch, partial**: only part of the volume each time, with filtrate returned so nutrients are not wasted [P3].
- All harvest flow goes through **top-entry** tubes; no wall openings [P3].
- The harvest pump is a **peristaltic** pump [P3]. The culture only touches food-safe tubing, and the pump can be stopped instantly by the MCU.
- The harvest line takes culture from a depth chosen to avoid sediment at the bottom.

## Proposed features

1. **Harvest sequence** (MCU-controlled, Linux-initiated):
   1. check interlocks (filter not full, return line clear, level OK);
   2. run the harvest pump for a bounded time or volume;
   3. pass through a ~200 µm pre-sieve, then a 30–50 µm filter ([J1] p. 6);
   4. return the filtrate to the IBC through the lid;
   5. stop on timeout, a fault or a level alarm;
   6. log volumes and times.
2. **Harvest trigger**: initially **manual** (button or dashboard). Automation comes later, once growth measurement is calibrated (see [../microscopy.md](../microscopy.md)).
3. **Biomass handling**: manual removal of the filter cake; washing, dewatering and drying as separate, documented steps.
4. **Logging** of harvest volume, wet mass and (once measured) dry mass, linked to microscope images before and after.

## Unresolved issues

1. **Flow rate vs filament damage**: which pump size and tubing keep filaments intact?
2. **Mesh size**: 30–50 µm cloth ([J1]) vs commercial 380–500 mesh screens ([F1]). What retention and clogging rate do we see with this culture? Short or straight filaments may pass through or clog.
3. **Filtrate return**: risk of carrying contaminants back into the tank, and of build-up of unicellular contaminants that pass the filter ([F1] p. 17).
4. **Hygiene of the harvest path**: cleaning and sanitising tubing, sieve and filter between harvests.

## Food safety

**Unresolved; must be addressed before any human consumption.**

- FAO warns of possible contamination of spirulina with **toxin-producing cyanobacteria** (microcystins). It notes that safety levels and hazards "have not been established beyond doubt", with special precautions for at-risk groups ([F1] p. 19).
- Food-standard spirulina needs **microbiological, chemical, heavy-metal, pesticide and extraneous-matter testing** ([F1] p. 17). AlgaeSense does none of this.
- A microscope image **cannot** detect dissolved toxins, heavy metals or bacterial load (see [../microscopy.md](../microscopy.md#what-microscopy-cannot-do)).
- Applicable Indian food regulations have **not been reviewed** by this project.
- Needed before any consumption: a testing plan with an accredited laboratory, hygienic handling procedures, and expert review.
