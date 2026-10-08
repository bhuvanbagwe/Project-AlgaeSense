# Hardware (10 L prototype)

This page covers the hardware of the 10 L prototype described on Instructables [P1], and the pin assignments in this repo's firmware. For the proposed 1,000 L system, see [ibc-1000l/electronics.md](ibc-1000l/electronics.md) and [ibc-1000l/mechanical.md](ibc-1000l/mechanical.md).

> Some details are **not yet documented anywhere**: wiring, driver circuits, power supply, tank dimensions, pump flow rate and the microscope model. Each gap is marked _not documented_ below. Please don't guess; send a build report or ask the maintainer.

## Parts list (as published)

From the Instructables supplies list [P1] ("excluding basic tools"):

| # | Part | Notes from [P1] |
|---|---|---|
| 1 | Arduino UNO Q | Main controller: Linux processor + MCU [A1] |
| 2 | BO motor | Drives the DIY peristaltic pump |
| 3 | Peristaltic pump (3D printable) | DIYed "since buying one was 10x more expensive" |
| 4 | Aerator motor | "aerator pump (12v DC, used in aquariums)" |
| 5 | 4 × 5 V 1 W COB LEDs | Light source in place of sunlight |
| 6 | Temperature probe sensor | No sensor code in this repo |
| 7 | pH sensor | "(Future addition)" |
| 8 | TDS sensor | "(Future addition)" |

Also used in the build [P1]:

- A **USB microscope**: "a normal PCB soldering USB microscope", refocused to see filaments (see [microscopy.md](microscopy.md)). Model: _not documented_.
- A **surgical food-safe tube** dipped into the tank, feeding a **3D-printed measuring/sampling chamber** with an **acrylic slit** on one end for viewing.
- A **laser-cut acrylic** tank inside a **3D-printed frame**, designed in **Fusion 360**.

## Tank and frame

- Capacity: **10 L** ("current system of 10 Liters", [P1] Step 4). Internal dimensions: _not documented_.
- Construction: acrylic sheets were laser cut and first joined with silicone adhesive. They leaked repeatedly: about 6 hours of curing per attempt, over about three days ([P1] Step 6). The Instructables text cuts off at "I ended up ditching the silicon plan and"; the final sealing method is _not documented_.
- CAD: Step 5 of [P1] says the current CAD files are open-sourced and future versions will go in this repository. **No CAD files are in this repo yet.**

## Pin map (current firmware, `sketch/sketch.ino`)

| Arduino pin | Signal | Load | Firmware |
|---|---|---|---|
| D5 | PWM 0–255 (`set_light`, 0–100 %) | LED lighting | `LIGHT_PIN` |
| D6 | 0 or 255 (`start_sample` / `stop_sample`) | Sampling peristaltic pump | `PUMP_PIN` |

History: the first firmware (2026-08-25, commit `6d0451c`) also had **D9 = aerator (PWM)**. It was removed on 2026-09-13. In the current firmware the aerator is not software-controlled. How it is powered in the current build is _not documented_.

## Driving loads safely

The UNO Q's GPIO pins cannot power motors or LED arrays directly. Photos in [P1] show a red driver/relay board next to the pump. Its type is _not documented_.

If you build your own:

- Use a **logic-level MOSFET module or motor driver** for each load (pump, LEDs, aerator), with a **flyback diode** across each motor.
- Use a **separate supply** for the 12 V aerator and other motors, with a **common ground** to the board.
- **Fuse** each supply and keep electronics **above and away from the water line**.

These are general electronics practices, not a description of the original build.

## Things the prototype does not have (yet)

- pH, TDS, dissolved CO₂ and turbidity sensors (listed as future in [P1] and in the README).
- A heater ("In Future, a heater module will be integrated", [P1] Step 7).
- Nutrient-dosing and harvesting pumps.
