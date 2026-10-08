# 1,000 L IBC — electronics, sensors and control

> **⚠️ PROPOSAL — NOT BUILT.** Nothing here has been built or tested. No pin assignments for the 1,000 L system have been decided. See [overview.md](overview.md).

## Validated (from the 10 L prototype)

From the code [P2]:

- Arduino UNO Q running an App Lab app.
- Linux side: USB-camera MJPEG stream on a local dashboard, port 7000 [A3].
- MCU side: PWM output for LEDs (D5); pump output (D6) with a firmware-enforced 100–10,000 ms run limit and automatic stop.
- Python ↔ MCU calls over Bridge RPC.

Built and described on Instructables, but without code in this repo [P1]:

- Temperature probe.
- 12 V aquarium aerator. Software-controlled on D9 only in the 2026-08-25 code.

**Not demonstrated:** sensor readings in code, logging, dosing, harvesting control, fault monitoring.

## Existing research relevant to sensing

- Spirulina grows best at **high pH (8.5–11)** and tolerates **high salinity** ([F1] p. 4). FAO lists **dissolved solids of 10–60 g/L** among the productivity factors ([F1] p. 8). Sensors therefore sit in a **strongly alkaline, salty** medium.
- Temperature is the most important climatic factor ([J1] p. 2), so temperature logging is a priority.
- Jourdan describes a simple **Secchi disk** for measuring culture density ([J1] p. 5). It is a useful manual reference for calibrating any automatic density estimate.

## Engineering assumptions

- The **same core architecture** as the 10 L system [P3]:
  - the Linux side handles camera, image analysis (OpenCV, planned), logging, dashboard and decisions;
  - the MCU side handles every actuator, with **timeouts and safe defaults in firmware**.
- **Low-voltage DC** (12 V) for pumps, LEDs and sensors where possible. Any **mains-powered** equipment (e.g. larger air pumps) is switched through properly rated relays or contactors, behind an **RCD/RCCB**, in an enclosure above the water line.
- Every motor load goes through a driver (MOSFET module or motor driver), never directly from a GPIO pin.
- Probes enter **from the top** [P3]. Cable lengths must allow about 1 m+ immersion depth plus routing to the enclosure.

## Proposed I/O budget (no pins assigned)

| Function | Type | Notes |
|---|---|---|
| Lighting (lid LEDs and/or submersible tubes) | PWM output(s) via driver | Several channels for zones/schedules |
| Air pump(s) | On/off (relay) or PWM (DC pump) | Fault if off for too long |
| Sampling pump | Digital/PWM output | Reuse the existing `start_sample` pattern |
| Dosing pumps (1–3) | Digital/PWM outputs | Firmware limit on maximum dose per day |
| Harvest pump | Digital/PWM output | Interlock with filter-full / level sensors |
| Temperature (1–2 probes) | 1-Wire or analogue | Top and bottom of the tank, to detect stratification |
| pH | Analogue (isolated module preferred) | Needs regular calibration |
| Conductivity / TDS | Analogue | **Range check needed**, see below |
| Turbidity / optical density | Analogue | Calibrate against dry weight or Secchi disk |
| Liquid level / overflow / leak | Digital | Interlocks for harvest return and dosing |
| USB microscope | USB | As in the 10 L system |

## Sensor compatibility notes

- **TDS range:** a common hobby TDS module (e.g. DFRobot SEN0244) is listed with a **0–1000 ppm** range (see [bom.csv](bom.csv)). FAO's 10–60 g/L dissolved solids is about **10,000–60,000 mg/L**, far beyond that range. *Estimate: 10 g/L = 10,000 mg/L.* A conductivity probe rated for saline media, or a diluted-sample method, will likely be needed.
- **pH probes** in pH ~10 media drift and need regular calibration. Check the probe's rating for continuous immersion before buying.
- **Turbidity sensors** made for clean water may saturate in dense green culture. Calibrate them, or sample through a diluting chamber.
- **Biofouling:** any immersed optical or electrochemical sensor will foul over time and needs a cleaning schedule.

## Proposed features

- **Logging:** timestamped CSV (or SQLite) of every actuator action, sensor reading and image metric, stored on the board and exported over the local network.
- **Dashboard:** live microscope stream, latest readings, actuator states, active faults, and charts of recent history.
- **Fault monitoring:**
  - pump running longer than its limit;
  - sensor out of plausible range or not responding;
  - temperature outside its band;
  - level or leak sensor triggered;
  - air pump off.

  Each fault moves the system to a **safe state**: lights to schedule, dosing and harvest stopped, aeration kept on.
- **Watchdog:** the MCU puts outputs into the safe state if it hears nothing from the Linux side for a set time.
- **Manual override:** physical switches for the air pump and a master stop.

## Unresolved issues

1. **Power budget:** depends on the lighting design (see the estimate in [cultivation.md](cultivation.md)) and the air pump size, neither chosen yet.
2. **Sensor selection** for high-pH, high-salinity media that can run unattended for long periods.
3. **Data retention and backup** for logs and images.
4. **Electrical safety review** of the whole setup by a qualified person before running unattended.
