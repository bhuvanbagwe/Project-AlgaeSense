# Roadmap

Everything on this page is **planned**, not done. Items are ordered so that each step makes the next one checkable. For what exists today, see the [README](../README.md#what-is-demonstrated-vs-planned).

## 1. Make the 10 L prototype reproducible

- [ ] Wiring diagram and driver circuit for D5 (LEDs) and D6 (pump), plus how the aerator is powered.
- [ ] Publish CAD files (tank frame, peristaltic pump, sampling chamber), as promised in [P1] Step 5.
- [ ] Record the microscope model and settings.
- [ ] Confirm whether `app.yaml` needs `bricks: - arduino:web_ui` ([software.md](software.md#open-question-appyaml-bricks)).
- [ ] Fix the cycle-timing message (about 25 s, not 20 s), or make the timing start-to-start.

## 2. Measure and log

- [ ] Temperature probe code (the probe is listed in [P1]; no code yet).
- [ ] Data logging (CSV) of pump cycles, sensor readings and image metrics, with timestamps.
- [ ] A reference growth measurement (dry weight, optical density or Secchi disk, see [J1] p. 5) to calibrate image metrics.
- [ ] pH sensor (listed as "future addition" in [P1]); Spirulina media run at high pH ([F1] p. 4; [J1] p. 9).
- [ ] TDS / conductivity sensor; dissolved CO₂ and turbidity sensors later.

## 3. Microscopy pipeline

- [ ] Timestamped frame capture after each settle period.
- [ ] OpenCV preprocessing and filament segmentation ([microscopy.md](microscopy.md#planned-pipeline)).
- [ ] Publish the dataset and model described on Instructables, or retrain one openly.
- [ ] Contaminant **flags for human review** (not automatic verdicts).

## 4. Control

- [ ] Restore the day/night lighting schedule (it existed in the 2026-08-25 code) as an option in the configuration.
- [ ] Closed-loop lighting, aeration and dosing based on logged measurements, with safe limits in firmware.
- [ ] Fault monitoring: pump-stall detection, sensor-out-of-range alarms, safe shutdown.
- [ ] Dashboard: show the latest measurements and system state, not only the camera.

## 5. Harvesting (10 L)

- [ ] Test harvesting through a fine filter cloth (30–50 µm is the range given in [J1] p. 6), with the filtrate returned to the tank.
- [ ] Record harvested wet and dry mass per run.

## 6. 1,000 L IBC proposal

- [ ] Design review of the [IBC proposal](ibc-1000l/overview.md), focused on light penetration, mixing, temperature and harvesting flow.
- [ ] Get quotes for the [draft BOM](ibc-1000l/bom.csv).
- [ ] Find collaborators, especially for biology/food safety and mechanical work.
- [ ] Present at Logos x Zu-Grama Field Station, Rajasthan, 23–31 Oct 2026 [P3].

## Not on the roadmap (yet)

- Any claim that harvested biomass is safe to eat. Food safety needs laboratory testing and expert review ([F1] pp. 17, 19), and this project does not yet have either.
