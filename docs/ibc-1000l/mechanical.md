# 1,000 L IBC — mechanical design

> **⚠️ PROPOSAL — NOT BUILT.** Nothing here has been built or tested. Numbers marked **Estimate** are back-of-envelope figures with the working shown. See [overview.md](overview.md).

## Validated (from the 10 L prototype)

- A laser-cut acrylic tank with a 3D-printed frame held 10 L, after repeated sealing problems ([P1] Steps 5–6).
- A food-safe tube dipping into the tank, a 3D-printed peristaltic pump and a 3D-printed sampling chamber worked for sampling at 10 L ([P1] Step 7).
- None of the 10 L mechanical parts have been tested at 1,000 L.

## Existing research and reference data

- **IBC size:** a standard 1,000 L IBC is typically **1200 × 1000 × 1160 mm** (L × W × H), about **1.2 m²** footprint, and about **1,055 kg** when full of water. Dimensions vary by manufacturer [D1].
- **Culture depth in practice:** commercial raceways keep 15–18 cm depth with paddle-wheel mixing ([F1] p. 13). Jourdan recommends 10–20 cm for small ponds ([J1] p. 9).
- **Mixing matters:** FAO summarises work showing that maximal mixing increased productivity at the highest light intensities used ([F1] p. 8).

## Estimates

**Liquid depth.** Volume ÷ footprint: 1.0 m³ ÷ 1.2 m² ≈ **0.83 m**. This is a lower bound, because the inner bottle is smaller than the outer frame and the pallet adds height. The maintainer's brief puts it at **1 m+**. *Estimate.*

**Depth compared with raceways.** 0.83–1.0 m ÷ 0.15–0.18 m ≈ **5–7 × deeper** than a commercial raceway. *Estimate.*

**Floor load.** About 1,055 kg ÷ 1.2 m² ≈ **880 kg/m²**, spread under the pallet [D1]. Point loads under the feet will be higher. *Estimate; check the floor with someone qualified.*

## Engineering assumptions

- The IBC is **new food-grade**, or has only ever held food. A reused chemical IBC is not acceptable.
- **No new holes in the IBC walls** [P3]. Everything enters through the **top opening**, using a custom **lid or cover plate** with sealed glands for cables and tubes.
- The IBC's existing outlet valve (if fitted) is **not** part of the cultivation flow path. Using it for draining or cleaning is an **open question**.
- The system sits indoors on a level floor that can take the load, with a drip tray or bunding in case of leaks.
- Wetted parts are food-safe and tolerate a strongly alkaline medium (pH 8.5–11 per [F1] p. 4).

## Proposed features

- **Top lid / cover plate** carrying:
  - lid-mounted LED lighting, or the mounts for submersible tube lights;
  - cable glands for sensor probes;
  - bulkhead or gland fittings for air lines, sampling, dosing, harvest suction and filtrate return;
  - a removable inspection hatch.
- **Internal mast or rail**, hung from the lid, to hold sensors and tube ends at fixed, known depths.
- **Air diffusers** laid on the bottom, fed from top-entry air lines, to mix the culture and supply air (CO₂).
- **Sampling line** from a fixed depth to the microscope chamber, with a return path so sampled culture is not wasted.
- **Harvest station** next to the IBC: pump, pre-sieve, filter, and a filtrate return line through the lid. See [harvesting.md](harvesting.md).

## Unresolved issues

1. **Mixing with air only.** Can diffusers alone keep a ~1 m deep, square tank mixed without dead zones in the corners? Is there a risk of settling ([J1] p. 10 describes Spirulina sinking and dying when stressed)? Diffuser layout, airflow and the shear on filaments are all untested.
2. **Lid design.** Does "lid" mean the IBC's own fill opening, or a larger cover over the top? This needs the maintainer's decision. The size of the IBC opening limits what can be inserted.
3. **Submersible lights.** They need mounting, cleaning access and a food-safe sleeve. Biofilm on light surfaces will cut light output over time.
4. **Cleaning.** How is the tank cleaned and disinfected between batches without wall openings?
5. **Evaporation and condensation** under a closed lid, and venting of the air pumped in.
