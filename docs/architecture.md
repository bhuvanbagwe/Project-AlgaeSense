# Architecture

This page describes how AlgaeSense is put together. Each part is marked as **current**, **history** or **planned**. "Current" means it is in the code at commit `78c2541` (2026-09-13). Sources are listed in [references.md](references.md).

## System overview

```text
            ┌──────────────── culture tank (10 L prototype) ────────────────┐
            │  LEDs (D5)        aerator (12 V)        temperature probe *    │
            └───────┬──────────────────────────────────────────────────────┘
                    │ food-safe tube
                    ▼
        DIY peristaltic pump (D6) ──► 3D-printed sampling chamber with acrylic slit
                                                   │
                                                   ▼
                                           USB microscope
                                                   │ USB
┌──────────────────────────────── Arduino UNO Q ───┼──────────────────────────────────┐
│ Linux (QRB2210): python/main.py                  ▼                                  │
│   Camera(640×480, 10 fps) ──► WebUI.expose_camera("/camera") ──► assets/index.html  │
│   pump_loop() thread ── Bridge RPC ──┐                              (port 7000)     │
│                                      ▼                                              │
│ MCU (STM32U585, Zephyr): sketch/sketch.ino                                          │
│   start_sample / stop_sample / pump_running / set_light / all_off                   │
└─────────────────────────────────────────────────────────────────────────────────────┘
 * listed on Instructables [P1]; no sensor code in this repo
```

## Components

| Component | Role | Status | Source |
|---|---|---|---|
| Arduino UNO Q | Linux processor runs the Python app; MCU drives outputs in real time | Current | [A1], code |
| `sketch/sketch.ino` | Pump and LED outputs; non-blocking pump timeout in `loop()` | Current | code |
| `python/main.py` | Camera stream, web UI, pump timer thread | Current | code |
| `assets/index.html` | Static dashboard with live `<img src="/camera">` | Current | code |
| Bridge RPC (`Arduino_RouterBridge`) | Python ↔ MCU function calls | Current | code |
| USB microscope | Images the sample chamber | Current hardware [P1]; stream only in code | [P1], code |
| DIY peristaltic pump + sampling chamber | Moves culture into the viewing chamber | Current hardware [P1] | [P1] |
| Aerator | Mixing and CO₂ supply via air | Hardware [P1]; software control only in 2026-08-25 code (D9) | [P1], [P2] |
| Day/night scheduler | LEDs and aerator by time of day | History (2026-08-25 → 2026-09-13) | [P2] |
| Density heuristic | Percentage of dark pixels → light/aerator levels | History (2026-08-25 → 2026-09-13) | [P2] |
| Spirulina detection model | Object detection on microscope frames | Described on Instructables; not in repo | [P1] |
| Environmental sensors (pH, TDS, CO₂, turbidity) | Feedback for control | Planned | [P1], README |
| Logging, dosing, harvesting, fault monitoring | Closed-loop operation | Planned | [P3] |

## Bridge interface (current firmware)

Functions the MCU exposes with `Bridge.provide_safe(...)`:

| Name | Arguments → return | Behaviour | Called by current `main.py`? |
|---|---|---|---|
| `start_sample` | `int durationMs` → `bool` | Clamps to 100–10,000 ms, sets D6 to 255, records stop time | Yes (5000 ms) |
| `stop_sample` | → `bool` | Sets D6 to 0 | Yes (safety stop) |
| `pump_running` | → `bool` | Returns pump state | Yes (polled every 0.1 s, up to 7 s) |
| `set_light` | `int percent` → `bool` | 0–100 % mapped to PWM 0–255 on D5 | No |
| `all_off` | → `bool` | D5 and D6 to 0 | No |

`loop()` on the MCU stops the pump when `millis()` passes the stop time. The stop does not depend on the Linux side staying responsive.

## Control flow (current)

1. On start: the camera starts, the MJPEG stream is exposed at `/camera`, and a background thread starts.
2. The thread waits 20 s, then calls `start_sample(5000)`.
3. It polls `pump_running` until false (up to 7 s), then calls `stop_sample` as a safety stop.
4. It waits 20 s and repeats.

The thread does not analyse frames and makes no decisions.

## Control flow (history, 2026-08-25, commit `ecbac5b`)

The first `main.py` ran a 60 s cycle:

1. Set lights and aerator by time of day (IST). Day was 06:00–22:00: LED 65 %, aerator 55 %. Night: LED off, aerator 35 %.
2. Turn the aerator off, wait 2 s, run the sampling pump for 4 s, wait 3 s for the sample to settle.
3. Capture 5 frames and take the median "relative density" (see [microscopy.md](microscopy.md)).
4. Choose light and aerator levels from fixed thresholds (< 5 %, < 15 %, otherwise). `AI_ENABLED = False`.

This logic was replaced on 2026-09-13 by the simpler stream-plus-pump version. The repo does not record why.

## Algorithm described on Instructables

Step 9 of [P1] lists this intended loop:

1. Check day/night time and culture age.
2. Run LEDs only during the configured day period.
3. Keep aeration running.
4. Run the sampling pump at fixed intervals.
5. Wait for the sample to become still.
6. Capture several images.
7. Detect Spirulina and contaminants with the AI model.
8. Count detections and calculate area/coverage.
9. Compare with previous samples to estimate growth stage.
10. Adjust lighting, log results, repeat.

Steps 1–6 and 10 (lighting only) roughly match the 2026-08-25 code. Steps 7–9 and logging are **not** implemented in this repository.

## Design principles going forward

- **The MCU owns safety:** actuator timeouts and safe defaults live in firmware, as `start_sample` already does.
- **Measure before you control:** any automated decision should be backed by logged measurements that can be checked.
- **Keep it reproducible:** the App Lab layout at the repo root stays as is, and new dependencies need justification.
