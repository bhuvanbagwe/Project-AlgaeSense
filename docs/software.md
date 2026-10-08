# Software

AlgaeSense is an **Arduino App Lab** app for the **Arduino UNO Q**. The app has a Python part that runs on the board's Linux side and an Arduino sketch that runs on its microcontroller. The two talk over Arduino's Bridge RPC. See [architecture.md](architecture.md) for the system diagram.

## Files

| File | Runs on | Purpose |
|---|---|---|
| `app.yaml` | App Lab | App name (`AlgaeSense`), description, icon 🌱. No `bricks:` entry (see below). |
| `python/main.py` | Linux (Debian, QRB2210) | Entry point. Starts the camera and web UI, runs the pump timer thread, calls `App.run()` |
| `sketch/sketch.ino` | MCU (STM32U585, Zephyr) | Pump and LED outputs, Bridge functions, pump timeout |
| `sketch/sketch.yaml` | App Lab build | Profile `default`, platform `arduino:zephyr`, no extra libraries listed |
| `assets/index.html` | Browser | Static dashboard; shows `/camera` |

## Dependencies

Everything comes from the App Lab / UNO Q platform. No `pip` or Library Manager installs are needed for the current code.

| Side | Import / include | Used for |
|---|---|---|
| Python | `arduino.app_utils.App`, `Bridge` | App lifecycle; RPC to the MCU |
| Python | `arduino.app_bricks.web_ui.WebUI` | Web server for `assets/` and the `/camera` MJPEG stream [A3] |
| Python | `arduino.app_peripherals.camera.Camera` | USB camera capture |
| Python | `time`, `threading` (standard library) | Timer thread |
| Sketch | `Arduino_RouterBridge.h` | `Bridge.begin()`, `Bridge.provide_safe()`, `Monitor` serial |

The 2026-08-25 version also imported `numpy`, `datetime` and `zoneinfo` for the density heuristic and day/night schedule.

## Configuration

At the top of `python/main.py`:

| Constant | Value | Meaning |
|---|---|---|
| `PUMP_ON_TIME_MS` | 5000 | Pump run per cycle (ms) |
| `PUMP_INTERVAL_SECONDS` | 20 | Wait before the first cycle and between cycles (s) |

In `sketch/sketch.ino`: `MAX_PUMP_TIME = 10000` caps any pump run. `start_sample` also enforces a minimum of 100 ms.

Note: the start banner says "Pump cycle: 5 sec ON every 20 sec". The code actually waits 20 s **after** each pump run, so one full cycle is about 25 s.

## Running

See [Install and run](../README.md#install-and-run) in the README. In short: run the app from App Lab, then open `http://<board-ip>:7000/`. Port 7000 is the WebUI default [A3].

### Open question: `app.yaml` bricks

Arduino's camera-stream example declares the WebUI brick in its `app.yaml` [A4]:

```yaml
bricks:
  - arduino:web_ui
```

This repo's `app.yaml` has no `bricks:` entry. Nobody has checked on hardware whether this stops the dashboard from loading. If you test it, please report what you find in an issue. Changes to `app.yaml` should come as a separate, tested pull request.

## Console output

- MCU monitor (115200 baud): `AlgaeSense MCU ready`
- Python console: a start banner, then `[AlgaeSense] Peristaltic pump ON for 5 seconds` and `... OFF` for each cycle, plus error messages if a Bridge call fails.

No data is written to disk; there is no logging yet.

## Version history of the code

| Date | Commit | Change |
|---|---|---|
| 2026-08-25 | `6d0451c`, `d83a624` | First sketch: D5 light, D6 pump (blocking `delay()`), D9 aerator. Moved into `sketch/` |
| 2026-08-25 | `ecbac5b` | First `main.py`: IST day/night schedule, 60 s sampling cycle, numpy density heuristic, threshold decisions |
| 2026-08-25 | `551dd34`, `e3e3836` | `app.yaml`, `sketch.yaml` |
| 2026-09-13 | `d48128b` | `main.py` simplified to camera stream + timed pump |
| 2026-09-13 | `9585071` | `assets/index.html` dashboard added |
| 2026-09-13 | `78c2541` | Sketch: non-blocking pump timer, `pump_running`, `stop_sample`; D9 aerator removed |

To see an old version: `git show ecbac5b:python/main.py`.
