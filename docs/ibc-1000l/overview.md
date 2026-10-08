# 1,000 L IBC system — overview

> **⚠️ PROPOSAL — NOT BUILT.** Nothing on this page has been built or tested at 1,000 L. It is a design proposal based on the 10 L prototype, published research and stated engineering assumptions. Numbers marked **Estimate** are back-of-envelope figures with the working shown, not measurements. Food safety is **unresolved**.

## Purpose

AlgaeSense proposes scaling from the 10 L prototype to a single **1,000 L indoor system built around a standard food-grade IBC** (intermediate bulk container). The proposal will be presented at the **Logos x Zu-Grama Field Station, Rajasthan, 23–31 Oct 2026** [P3]. The project is looking for:

- **funding**
- **equipment sourcing**: see the [draft BOM](bom.csv)
- **collaborators**: especially in algal biology, food safety, mechanical/fluid design and electronics

## Design inputs (from the maintainer's brief [P3])

- One standard **food-grade 1,000 L IBC** tank; **indoor** cultivation.
- Lighting **mounted on the lid**, or **appropriately rated submersible tube lights**.
- **Air pumps and diffusers** for aeration and circulation.
- **No additional holes in the IBC walls.** All sensor, air and fluid connections enter **from the top**.
- **Automated microscope sampling**.
- **MCU-controlled nutrient dosing**.
- **Peristaltic-pump harvesting**, **fine-mesh biomass filtration**, and **return of filtered medium** to the IBC.
- **Local control, logging and fault monitoring**.
- **Same core architecture as the 10 L system:** Arduino UNO Q, USB microscope, OpenCV-based analysis (planned), sensors, pumps, aeration, logging, local dashboard.

## Proposed architecture

```text
                       ┌─────────────── top opening / lid ───────────────┐
  lid LEDs ───────────►│  sensor probes   air lines   sampling, dosing,  │
                       │  (T, pH, …)      (diffusers)  harvest & return  │
                       └──────┬──────────────┬──────────────┬────────────┘
                              │              │              │
                    ┌─────────▼──────────────▼──────────────▼─────────┐
                    │          food-grade 1,000 L IBC (indoor)         │
                    │  optional submersible, rated LED tube lights     │
                    └─────────────────────────────────────────────────┘
   sampling pump ──► microscope chamber ──► USB microscope ──┐
   harvest pump ──► ~200 µm pre-sieve ──► 30–50 µm filter ──► biomass
                                                │
                                                └── filtrate returned to IBC
                                                                   │
                       ┌──────────────────── Arduino UNO Q ────────▼────┐
                       │ Linux: camera, analysis (planned), logging,    │
                       │        dashboard, decisions                    │
                       │ MCU:   pump/LED/air drivers, timeouts, faults  │
                       └────────────────────────────────────────────────┘
```

The filter mesh sizes come from Jourdan's manual ([J1] p. 6). They are a starting point, not a validated choice. See [harvesting.md](harvesting.md).

## What carries over from the 10 L prototype

| Item | 10 L status | Source |
|---|---|---|
| UNO Q split: Linux app + MCU firmware over Bridge | Working in code | [P2] |
| Live USB-microscope stream to a local dashboard | Working in code | [P2] |
| Timed peristaltic sampling with an MCU-side timeout | Working in code | [P2] |
| Sampling chamber with viewing slit; refocused USB microscope shows filaments | Built and described | [P1] Steps 7–8 |
| LED lighting and aquarium aerator on a 10 L tank | Built and described | [P1] |
| Image-based detection model (~100 images) | Described; not in repo | [P1] Step 10 |
| Growth rate, yield, sensor control loop, harvesting | **Not demonstrated** | — |

## Key unresolved issues

| Issue | Why it matters | Details |
|---|---|---|
| **Light penetration** | Liquid depth is about 0.8–1 m+. Commercial raceways run at 15–18 cm and are already light-limited by self-shading ([F1] p. 13) | [cultivation.md](cultivation.md) |
| **Mixing** | Air diffusers in a deep, square tank may leave dead zones; productivity depends on mixing ([F1] p. 8) | [mechanical.md](mechanical.md) |
| **Thermal management** | Optimum about 35 °C; growth practically nil below 20 °C; danger above 38 °C ([J1] p. 2). About 1 t of water plus LED heat | [cultivation.md](cultivation.md) |
| **Sensor compatibility** | High-pH, high-salt medium; long cables for top entry; TDS sensors with low ranges | [electronics.md](electronics.md) |
| **Harvesting flow rate** | Dosing-class peristaltic pumps move ml/min; harvesting needs L/min | [harvesting.md](harvesting.md) |
| **Filtration** | Pumping can damage filaments, and short filaments pass through screens ([F1] p. 17) | [harvesting.md](harvesting.md) |
| **Biological safety / contamination / food safety** | Toxin-producing cyanobacteria and other contaminants; food-standard testing needed ([F1] pp. 17, 19; [J1] p. 10) | [cultivation.md](cultivation.md), [harvesting.md](harvesting.md) |

## Pages in this proposal

- [mechanical.md](mechanical.md): IBC, lid, top-entry layout, mixing, weight
- [electronics.md](electronics.md): controller, drivers, power, sensors, I/O budget, faults
- [cultivation.md](cultivation.md): light, temperature, pH, medium, contamination
- [harvesting.md](harvesting.md): pumping, filtration, return of medium, flow-rate estimates, food safety
- [bom.csv](bom.csv): draft bill of materials (mostly "quote needed")

Sources: [../references.md](../references.md).
