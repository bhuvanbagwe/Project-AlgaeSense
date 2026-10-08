# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). The project has no tagged releases yet, so earlier entries are grouped by commit date (IST, from `git log`).

## [Unreleased]

### Added

- `docs/`: architecture, hardware, software, microscopy, experiments, roadmap and references pages.
- `docs/ibc-1000l/`: 1,000 L IBC **proposal (not built)**, with overview, mechanical, electronics, cultivation and harvesting pages, plus a draft `bom.csv`.
- `CONTRIBUTING.md`, GitHub issue templates (bug report, feature request, hardware build report), `CHANGELOG.md`, `JOURNAL.md`.

### Changed

- `README.md` rewritten: current status, demonstrated vs planned, pin map, install/run steps, safety notes, links and license note.
- `assets/index.html`: wording only. The dashboard no longer claims that OpenCV analysis, contour detection, measurements or diagnostics are running; image analysis is marked as planned.

### Not changed

- `python/main.py`, `sketch/`, `app.yaml`, pin assignments, control logic, `LICENSE`.

## 2026-09-13

### Changed

- `python/main.py` simplified to a live camera stream (640×480, 10 fps, `/camera`) plus a timed sampling pump (5 s on, 20 s wait). The day/night schedule and density heuristic were removed. (`d48128b`)
- `sketch/sketch.ino`: non-blocking pump timer with `start_sample`, `stop_sample`, `pump_running`, `set_light` and `all_off`. Pump runs clamped to 100–10,000 ms. D9 aerator output removed. (`78c2541`)

### Added

- `assets/index.html` dashboard page. (`9585071`)

## 2026-08-25

### Added

- `sketch/sketch.ino`: first firmware with D5 light PWM, D6 sampling pump and D9 aerator PWM (`6d0451c`); moved into `sketch/` (`d83a624`).
- `python/main.py`: IST day/night lighting and aeration schedule, 60 s sampling cycle, numpy dark-pixel "relative density" heuristic, threshold-based light/aerator decisions. (`ecbac5b`)
- `app.yaml` (`551dd34`) and `sketch/sketch.yaml` (`e3e3836`).

## 2026-08-21

### Added

- Repository created with LGPL-2.1 `LICENSE` and initial `README.md` (`73c7297`). README expanded with the project concept and diagram (`b498cb5`, `e1807a1`, `417a859`, `2d16f40`).
