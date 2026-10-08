# Contributing to AlgaeSense

Thanks for your interest. AlgaeSense is a small maker project. Contributions of any size help: a typo fix, a wiring diagram, a build report, a sensor driver, a review of the biology, or a component quote.

## Ground rules

1. **Evidence over enthusiasm.** Every technical claim in code comments, docs or PRs should be traceable to one of: the code, git history, the [Instructables article](https://www.instructables.com/AlgaeSense-Grow-Algae-Automatically-As-an-Off-Grid), a cited source (add it to [docs/references.md](docs/references.md)), or your own documented measurement (with date and method).
2. **Keep "done" and "planned" separate.** Mark proposals clearly. Don't describe planned features as working.
3. **No exaggerated claims** about AI, autonomy, yields or food safety.
4. **Food safety is unresolved.** Don't add content that suggests biomass from this system is safe to eat.
5. **No secrets or private data.** No Wi-Fi passwords, API keys, personal addresses or phone numbers in commits.

## Getting set up

1. Read the [README](README.md), then [docs/architecture.md](docs/architecture.md) and [docs/software.md](docs/software.md).
2. For code changes you need an **Arduino UNO Q** with **Arduino App Lab** ([docs](https://docs.arduino.cc/software/app-lab/)). Documentation changes need only a text editor.
3. Fork the repository and clone your fork:

   ```bash
   git clone https://github.com/<your-username>/Project-AlgaeSense.git
   cd Project-AlgaeSense
   git checkout -b docs/short-description   # or fix/..., feat/..., hw/...
   ```

## Branch and pull request flow

- Branch from `main`. Use a prefix: `docs/`, `fix/`, `feat/`, `hw/` (hardware/CAD), `bio/` (cultivation notes).
- Keep each PR **small and focused**: one topic, ideally under ~300 changed lines of prose or code.
- Write clear commit messages: a short summary line, then a blank line and the *why*.
- In the PR description, say **what changed**, **why**, and **how you tested it**. For hardware changes, say which board and what wiring you used.
- Update [CHANGELOG.md](CHANGELOG.md) under **Unreleased**.
- The maintainer reviews and merges. Please don't merge your own PR.

## Docs vs code changes

| Change type | Where | Extra expectations |
|---|---|---|
| Documentation | `README.md`, `docs/`, `JOURNAL.md` | Cite sources; mark unverified things as such |
| Linux-side app | `python/main.py` | Test on a UNO Q; note the App Lab version; no new dependencies without discussion |
| MCU firmware | `sketch/` | **Actuator safety first:** keep timeouts and safe defaults in firmware. Don't change pin assignments without an issue first |
| Dashboard | `assets/` | Keep it light; describe only what actually runs |
| App manifest | `app.yaml` | Test on hardware; explain why the change is needed |
| CAD / hardware files | a new `hardware/` or `cad/` folder (open an issue first) | Include source files (e.g. Fusion 360 export or STEP) and printable exports (STL) |

**Please do not move the App Lab files** (`app.yaml`, `python/`, `sketch/`, `assets/`) away from the repository root.

## Safety notes for contributors

- **Water and electricity:** keep electronics and mains equipment above the water line, use fused supplies and RCD protection, and never power motors directly from board pins.
- **Chemicals:** Spirulina media are strongly alkaline. Wear eye protection.
- **Biology:** use a known, clean starter culture. Do not collect "wild" cyanobacteria. Report anything unusual you see under the microscope in a build report.
- **Food:** don't eat or share biomass unless it has been tested by an accredited laboratory.

## Labels

| Label | Use for |
|---|---|
| `good first issue` | Small, well-defined tasks for newcomers |
| `help wanted` | Tasks where outside expertise is welcome |
| `documentation` | Docs-only changes |
| `hardware` | Mechanical, electrical, wiring, CAD |
| `firmware` | MCU sketch (`sketch/`) |
| `computer-vision` | Microscope imaging, OpenCV, models, datasets |
| `biology` | Cultivation, contamination, food safety |
| `lighting` | LED design, photoperiod, light penetration |
| `harvesting` | Pumps, filtration, filtrate return |
| `bug` / `enhancement` / `question` | As usual |

## Good first contributions

- Wiring diagram for the current pin map (D5 LEDs, D6 pump) with a suitable driver stage.
- Test whether the dashboard needs `bricks: - arduino:web_ui` in `app.yaml`, and report the result.
- Make the pump-cycle log message match the real timing (about 25 s per cycle).
- Add timestamped CSV logging of pump cycles in `python/main.py`.
- Turn the 2026-08-25 density heuristic into an optional, documented function with sample images.
- Send a hardware build report using the issue template.

## Reporting issues

Use the issue templates: **Bug report**, **Feature request**, **Hardware build report**. Include photos and logs where you can.

## License

By contributing, you agree that your contributions are licensed under the repository's [LGPL-2.1](LICENSE). A separate license for documentation, CAD and hardware files has not been decided yet. If you contribute CAD files, say so in your PR so the maintainer can confirm the license.
