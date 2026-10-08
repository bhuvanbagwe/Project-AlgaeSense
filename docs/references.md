# References

Sources cited across the AlgaeSense docs. Every source listed here was read when the docs were written (October 2026). Page numbers refer to the printed page numbers in each PDF.

## Project sources

| ID | Source | What it supports |
|---|---|---|
| [P1] | Bhuvan Bagwe (bhuvanmakes), *AlgaeSense : Grow Algae Automatically As an Off Grid Protein and Nutrient Source Using Machine Learning*, Instructables, published 2026-08-31, modified 2026-09-01. <https://www.instructables.com/AlgaeSense-Grow-Algae-Automatically-As-an-Off-Grid> (article licensed CC BY-NC-SA 4.0) | 10 L prototype: build, parts, sampling method, microscope, algorithm description, model training |
| [P2] | Git history of this repository (`git log`), commits from 2026-08-21 to 2026-09-13 | What the code did, and when |
| [P3] | Maintainer's project brief (October 2026) | 1 L phase existence; 1,000 L IBC design inputs; Logos x Zu-Grama Field Station presentation, Rajasthan, 23–31 Oct 2026 |

## Platform documentation

| ID | Source | What it supports |
|---|---|---|
| [A1] | Arduino, *UNO Q* documentation. <https://docs.arduino.cc/hardware/uno-q/> | QRB2210 Linux processor + STM32U585 MCU |
| [A2] | Arduino, *App Lab* documentation. <https://docs.arduino.cc/software/app-lab/> | App Lab setup and app management |
| [A3] | Arduino, `app-bricks-py` WebUI brick README. <https://github.com/arduino/app-bricks-py/blob/main/src/arduino/app_bricks/web_ui/README.md> | Default port 7000, static files served from `assets/`, `expose_camera()` MJPEG stream |
| [A4] | Arduino, `app-bricks-examples`, *Web UI Camera Stream* example. <https://github.com/arduino/app-bricks-examples/tree/main/core-and-foundational/08-web-ui-basics/05-web-ui-camera-stream> | Reference `app.yaml` declaring `bricks: - arduino:web_ui` |

## Spirulina cultivation literature

| ID | Source | What it supports |
|---|---|---|
| [F1] | Habib, M.A.B.; Parvin, M.; Huntington, T.C.; Hasan, M.R. (2008). *A review on culture, production and use of spirulina as food for humans and feeds for domestic animals and fish.* FAO Fisheries and Aquaculture Circular No. 1034. Rome, FAO. <https://www.fao.org/4/i0424e/i0424e.pdf> | Filament size (p. 3); pH 8.5–11 and temperature range (p. 4); environmental factors and 16 h photoperiod for a Jaipur isolate (p. 8); raceway depth 15–18 cm, paddle-wheel mixing, self-shading at 12–15 cm (p. 13); contamination (p. 14); harvesting screens, filament damage from pumping, quality-control tests (p. 17); food safety and microcystins (p. 19) |
| [J1] | Jourdan, J.-P. *Grow Your Own Spirulina* (condensed manual, revised 30 Aug 2011). <https://www.technap-spiruline.fr/images/pdf/GROW_YOUR_OWN_SPIRULINA.pdf> | Temperature limits (p. 2); harvest at ~0.5 g/L (p. 5); 30–50 µm filter cloth and ~200 µm pre-sieve (p. 6); culture depth 10–20 cm (p. 9); contamination and safety checks (p. 10); drying limits (p. 11) |

## Reference data

| ID | Source | What it supports |
|---|---|---|
| [D1] | ibc-container.org, *IBC container & tote sizes*. <https://ibc-container.org/en/ibc-sizes/> | Typical 1,000 L IBC: 1200 × 1000 × 1160 mm, ~1.2 m² footprint, ~1,055 kg when full of water (values vary by manufacturer) |
