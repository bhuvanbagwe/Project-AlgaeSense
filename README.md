# 🌱 AlgaeSense

**An open-source, microscope-assisted controller for growing Spirulina, built on the Arduino UNO Q.**

AlgaeSense is a maker project for monitoring and controlling an algae culture. It pumps small samples into a viewing chamber, shows them under a USB microscope, and drives pumps and lights from the Arduino UNO Q. The aim is a system that grows and harvests algae with as little manual work as possible.

The project is at an early stage. Some parts are working, some exist only in older code or in the Instructables write-up, and some are only planned. This README keeps those separate. See [What is demonstrated vs planned](#what-is-demonstrated-vs-planned).

> **Food safety:** AlgaeSense has **not** been validated for producing food. Contamination detection, food-safety testing and hygienic harvesting are **unresolved**. Do not eat biomass grown with this system unless it has been properly tested. See [Safety notes](#safety-notes).

---

## Contents

- [Why algae?](#why-algae)
- [Project evolution](#project-evolution)
- [How it works today](#how-it-works-today)
- [What is demonstrated vs planned](#what-is-demonstrated-vs-planned)
- [Repository layout](#repository-layout)
- [Hardware and software stack](#hardware-and-software-stack)
- [Install and run](#install-and-run)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [Safety notes](#safety-notes)
- [Links and documentation](#links-and-documentation)
- [License](#license)

---

## Why algae?

Spirulina (*Arthrospira*) is a filamentous cyanobacterium. It is grown commercially as a protein-rich food and feed ingredient ([FAO Fisheries and Aquaculture Circular No. 1034, 2008](https://www.fao.org/4/i0424e/i0424e.pdf)). It can be grown in tanks rather than fields. But the culture needs regular attention: light, mixing, temperature, pH and nutrients all matter, and contamination has to be watched for.

AlgaeSense is about the **monitoring and control layer**. The questions are:

- Can a low-cost edge computer look at the culture through a microscope?
- Can it decide what the tank needs?
- Can it act on that decision through pumps and lights?

## Project evolution

| Phase | Scale | Status | Evidence |
|---|---|---|---|
| 1 | ~1 L experiment | Done before this repository existed. **Details not yet documented here.** | Maintainer's description; see [JOURNAL.md](JOURNAL.md) |
| 2 | 10 L automated prototype | Built and described publicly | [Instructables article](https://www.instructables.com/AlgaeSense-Grow-Algae-Automatically-As-an-Off-Grid) (published 2026-08-31) and this repo's code (2026-08-25 onward) |
| 3 | 1,000 L indoor IBC system | **Proposal only. Not built.** | [docs/ibc-1000l/](docs/ibc-1000l/overview.md); to be presented at Logos x Zu-Grama Field Station, Rajasthan, 23–31 Oct 2026 |

The full dated history is in [JOURNAL.md](JOURNAL.md).

## How it works today

The 10 L prototype is an acrylic tank with a 3D-printed frame. It runs an **Arduino App Lab** app on the **Arduino UNO Q**. The UNO Q has two processors: a Linux processor (Qualcomm QRB2210) and a microcontroller (STM32U585) ([Arduino UNO Q docs](https://docs.arduino.cc/hardware/uno-q/)). This repo has code for both.

```text
                ┌──────────────────────────── Arduino UNO Q ───────────────────────────┐
 USB microscope │ Linux side: python/main.py                MCU side: sketch/sketch.ino │
 ──────────────►│  • Camera 640×480 @ 10 fps                 • D6 → sampling pump       │──► pump driver
                │  • Web dashboard (/camera MJPEG stream)    • D5 → LED PWM (available, │──► LED driver
 browser  ◄─────│  • Pump timer: 5 s ON, then 20 s wait  ──►   not used by main.py yet) │
                │        (Bridge RPC: start_sample, pump_running, stop_sample)          │
                └──────────────────────────────────────────────────────────────────────┘
```

What the **current code** (commit `78c2541`, 2026-09-13) does:

1. Streams the USB microscope to a local web page (`assets/index.html`, image source `/camera`).
2. Every cycle, it asks the microcontroller to run the peristaltic sampling pump for 5 s. The MCU limits any run to 100–10,000 ms and switches the pump off when time is up. Python then sends an extra safety stop.
3. It waits 20 s and repeats. A full cycle is therefore about 25 s plus pump time, not exactly "every 20 s".

The current code does **not** analyse images, read sensors, log data or change the lights. Those features are described in the next section.

## What is demonstrated vs planned

| Capability | Status | Where it is documented |
|---|---|---|
| Live USB microscope stream on a local web page | ✅ In current code | `python/main.py`, `assets/index.html` |
| Timed peristaltic sampling pump with MCU-side timeout | ✅ In current code | `python/main.py`, `sketch/sketch.ino` |
| LED PWM output (D5) | ⚙️ Firmware function exists (`set_light`), not called by current Python | `sketch/sketch.ino` |
| Day/night LED and aerator schedule (IST 06:00–22:00) | 🕘 History: in the 2026-08-25 code, removed on 2026-09-13 | commit `ecbac5b`, see [docs/software.md](docs/software.md) |
| "Relative density" from dark pixels (numpy threshold) | 🕘 History: 2026-08-25 code, removed on 2026-09-13 | commit `ecbac5b`, see [docs/microscopy.md](docs/microscopy.md) |
| Spirulina detection model (~100 labelled images) | 📄 Described on Instructables; **model and dataset are not in this repo** | [Instructables, Step 10](https://www.instructables.com/AlgaeSense-Grow-Algae-Automatically-As-an-Off-Grid) |
| Temperature probe | 📄 Listed on Instructables; **no sensor code in this repo** | Instructables supplies list |
| pH, TDS, dissolved CO₂, turbidity sensors | 🔭 Planned | [docs/roadmap.md](docs/roadmap.md) |
| OpenCV image analysis, cell counting, contamination detection | 🔭 Planned | [docs/microscopy.md](docs/microscopy.md) |
| Data logging, nutrient dosing, harvesting, fault monitoring | 🔭 Planned | [docs/roadmap.md](docs/roadmap.md) |
| 1,000 L IBC system | 🔭 Proposal, not built | [docs/ibc-1000l/](docs/ibc-1000l/overview.md) |

Legend: ✅ in current code · ⚙️ partly there · 🕘 existed earlier in git history · 📄 described elsewhere, not reproducible from this repo · 🔭 planned

## Repository layout

```text
Project-AlgaeSense/
├── app.yaml            # Arduino App Lab app manifest (name, icon, description)
├── python/main.py      # Linux-side app: camera stream, web UI, pump timer
├── sketch/
│   ├── sketch.ino      # MCU firmware: pump and LED outputs, Bridge functions
│   └── sketch.yaml     # Build profile (platform arduino:zephyr)
├── assets/index.html   # Dashboard page served by the WebUI brick
├── docs/               # Architecture, hardware, software, microscopy, experiments, roadmap
│   └── ibc-1000l/      # 1,000 L IBC proposal (not built) and draft BOM
├── CONTRIBUTING.md  CHANGELOG.md  JOURNAL.md
└── LICENSE             # LGPL-2.1
```

The root layout is the standard Arduino App Lab app structure. Please do not move these files.

## Hardware and software stack

**10 L prototype hardware** (from the Instructables supplies list and photos; details in [docs/hardware.md](docs/hardware.md)):

- Arduino UNO Q
- USB digital microscope (a PCB-inspection type, refocused to see Spirulina filaments)
- DIY 3D-printed peristaltic pump driven by a BO gear motor, with a 3D-printed sampling chamber that has an acrylic viewing slit
- 12 V DC aquarium-style aerator
- 4 × 5 V 1 W COB LEDs
- Temperature probe
- Laser-cut acrylic tank with a 3D-printed frame (Fusion 360 design)

**Pin map (current firmware):**

| Pin | Function | Notes |
|---|---|---|
| D5 | LED lighting (PWM, 0–100 % → 0–255) | `set_light` Bridge function |
| D6 | Sampling peristaltic pump (on = 255, off = 0) | `start_sample`, `stop_sample`, `pump_running` |
| ~~D9~~ | Aerator (PWM) | Only in the 2026-08-25 firmware; **not in current firmware** |

The repo does not document the driver circuit between these pins and the motors or LEDs. Photos on Instructables show a driver board, but its type is not documented.

**Software:** Arduino App Lab app. The Python side imports `arduino.app_utils` (App, Bridge), `arduino.app_bricks.web_ui` (WebUI) and `arduino.app_peripherals.camera` (Camera). The MCU side uses `Arduino_RouterBridge` on the `arduino:zephyr` platform. There are no other dependencies. Details in [docs/software.md](docs/software.md).

## Install and run

> These steps are based on the files in this repo and Arduino's public documentation. They have not been re-tested on hardware for this README. If something fails, please [open an issue](https://github.com/bhuvanbagwe/Project-AlgaeSense/issues).

1. **Set up the board.** Install [Arduino App Lab](https://docs.arduino.cc/software/app-lab/) and connect your Arduino UNO Q as described there.
2. **Get the code.**

   ```bash
   git clone https://github.com/bhuvanbagwe/Project-AlgaeSense.git
   ```

   Bring the app folder (with `app.yaml`, `python/`, `sketch/` and `assets/` at its root) into App Lab, or copy it onto the board. App Lab's [documentation](https://docs.arduino.cc/software/app-lab/) covers both.
3. **Wire the outputs.** Connect D5 (LEDs) and D6 (sampling pump) through suitable driver stages. Do not drive motors directly from the board's pins. Plug the USB microscope into the UNO Q.
4. **Run the app** from App Lab. The MCU prints `AlgaeSense MCU ready` on its monitor (115200 baud). The Python console prints the start banner and a `Peristaltic pump ON/OFF` line for each cycle.
5. **Open the dashboard** at `http://<board-ip>:7000/`. Port 7000 is the WebUI brick's default port, per Arduino's [WebUI brick README](https://github.com/arduino/app-bricks-py/blob/main/src/arduino/app_bricks/web_ui/README.md).

**Known setup question (unverified):** this repo's `app.yaml` does not declare any bricks. Arduino's official [camera-stream example](https://github.com/arduino/app-bricks-examples/tree/main/core-and-foundational/08-web-ui-basics/05-web-ui-camera-stream) declares `bricks: - arduino:web_ui`. If the dashboard does not load, try adding the WebUI brick in App Lab, which writes this entry to `app.yaml`. Please report the result in an issue. This README deliberately does not change `app.yaml`.

**Adjusting timing:** the pump timing is set by `PUMP_ON_TIME_MS` and `PUMP_INTERVAL_SECONDS` at the top of `python/main.py`. The firmware caps any single pump run at 10 s (`MAX_PUMP_TIME`).

## Roadmap

In short (full list in [docs/roadmap.md](docs/roadmap.md)):

1. **Make the 10 L prototype reproducible:** wiring diagram, driver circuit, CAD files, sensor code, logging.
2. **Measure before automating:** image-based estimates checked against a reference method such as dry weight or optical density.
3. **Microscopy pipeline:** OpenCV preprocessing, filament counting and contamination flags, with the model and dataset published.
4. **Closed-loop control:** lighting, aeration and dosing driven by logged measurements, with safe defaults.
5. **1,000 L IBC proposal:** design review, sourcing and collaborators. See [docs/ibc-1000l/overview.md](docs/ibc-1000l/overview.md).

## Contributing

Contributions are welcome: code, documentation, biology know-how, build reports and testing. Start with [CONTRIBUTING.md](CONTRIBUTING.md). Small, well-scoped changes are easiest to review.

## Safety notes

- **Food safety is unresolved.** FAO notes the risk of contamination of spirulina with toxin-producing cyanobacteria and lists quality-control tests for food-standard spirulina (microbiological, chemical, heavy metals, pesticides, extraneous material) ([FAO 2008, pp. 17, 19](https://www.fao.org/4/i0424e/i0424e.pdf)). AlgaeSense performs none of these tests.
- **Biological contamination:** the microscope can show the culture, but nothing in the current code detects contaminants.
- **Electrical safety:** keep mains-powered equipment and electronics away from water. Use properly rated power supplies, fuses and drivers.
- **Chemicals:** Spirulina media are strongly alkaline (FAO cites pH 8.5–11 for good production). Wear eye protection when mixing nutrients.

## Links and documentation

- Instructables write-up (10 L prototype): <https://www.instructables.com/AlgaeSense-Grow-Algae-Automatically-As-an-Off-Grid>
- Repository: <https://github.com/bhuvanbagwe/Project-AlgaeSense>
- Docs: [architecture](docs/architecture.md) · [hardware](docs/hardware.md) · [software](docs/software.md) · [microscopy](docs/microscopy.md) · [experiments](docs/experiments.md) · [roadmap](docs/roadmap.md) · [references](docs/references.md)
- 1,000 L IBC proposal: [overview](docs/ibc-1000l/overview.md) · [mechanical](docs/ibc-1000l/mechanical.md) · [electronics](docs/ibc-1000l/electronics.md) · [cultivation](docs/ibc-1000l/cultivation.md) · [harvesting](docs/ibc-1000l/harvesting.md) · [draft BOM](docs/ibc-1000l/bom.csv)
- History: [JOURNAL.md](JOURNAL.md) · [CHANGELOG.md](CHANGELOG.md)

## License

- **Code and repository content:** GNU Lesser General Public License v2.1. See [LICENSE](LICENSE).
- **Instructables article:** published separately on Instructables under **CC BY-NC-SA 4.0**. That license covers the article text and images on Instructables, not this repository.
- A separate license for documentation, CAD and hardware files has not been decided yet.
