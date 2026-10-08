# 1,000 L IBC — cultivation

> **⚠️ PROPOSAL — NOT BUILT.** No Spirulina has been grown at 1,000 L in this project. Numbers marked **Estimate** are back-of-envelope figures with the working shown, **not** predictions of yield. **Food safety is unresolved.** See [overview.md](overview.md).

## Validated (from the 10 L prototype)

From [P1]:

- A 10 L culture was started from **50 ml of Spirulina mother culture** plus nutrients, sourced from Algreen.
- It was lit by **4 × 5 V 1 W COB LEDs** and aerated by a **12 V aquarium aerator**.
- Filaments were visible under a refocused USB microscope.

No growth rate, biomass concentration, temperature log or pH log has been published. The 10 L run therefore shows the setup works mechanically; it does not show performance.

## Existing research

| Parameter | What the literature says | Source |
|---|---|---|
| Temperature | Optimum 35–37 °C (laboratory); minimum around 15 °C during the day | [F1] p. 4 |
| Temperature | Optimum 35 °C; above 38 °C "in danger"; below 20 °C growth practically nil | [J1] p. 2 |
| pH | 8.5–11.0 favours good production | [F1] p. 4 |
| pH | Keep above 10, preferably above 10.3, to limit sticky exopolysaccharide | [J1] p. 9 |
| Light | Continuous 24 h light not recommended | [J1] p. 2 |
| Photoperiod | 16 h/day found optimal for a Jaipur (India) isolate of *S. platensis* (Pareek & Srivastava, 2001) | [F1] p. 8 |
| Light and depth | At 12–15 cm depth, self-shading governs light availability; such cultures are light-limited | [F1] p. 13 |
| Light saturation | About one third of full sun saturates Spirulina's photosynthetic capacity | [J1] p. 9 |
| Depth | Raceways 15–18 cm; small ponds 10–20 cm | [F1] p. 13; [J1] p. 9 |
| Contamination | Chlorella contamination prevented by high bicarbonate (e.g. 0.2 M), low dissolved organic load, and warmth | [F1] p. 14 |
| Contamination | Chlorella can invade if Spirulina concentration is too low; toxic cyanobacteria "do not grow in a well tended spirulina culture", but a microscopic check at least yearly is recommended | [J1] p. 10 |
| Food safety | Risk of contamination with toxin-producing cyanobacteria (microcystins); special precautions for at-risk groups | [F1] p. 19 |

Note: the 2026-08-25 code used a 06:00–22:00 IST light period, i.e. 16 h. That matches the photoperiod above, but the repo does not say whether it was chosen for that reason.

## Estimates

**Illuminated surface per litre (lid lighting only).**

- Top surface about 1.2 m² ([D1]) ÷ 1.0 m³ = **1.2 m²/m³**.
- A 0.15 m raceway: 1 ÷ 0.15 = **6.7 m²/m³**.
- So the IBC lit only from the top has about **5–6 × less lit surface per litre**.

*Estimate.* This is the core reason light penetration is the main open question.

**Naive linear scaling of the 10 L lighting.**

- 4 W electrical ÷ 10 L = 0.4 W/L.
- 0.4 W/L × 1,000 L = **400 W electrical**.

*Estimate, not a design value.* Light needs scale with illuminated **area and depth**, not volume, and 4 W is an LED rating, not a measured light output.

**Heat needed to warm the water.**

- Water is about 1 kg/L, with specific heat about 4.186 kJ/(kg·K).
- 1,000 kg × 4.186 kJ/(kg·K) × 1 K = 4,186 kJ ≈ **1.16 kWh per °C**.
- Raising 25 → 35 °C ≈ **11.6 kWh**, ignoring losses.

*Estimate.*

**LED heat.** Nearly all LED electrical power ends up as heat in or near the tank. At the naive 400 W for 16 h/day: 400 W × 16 h = 6.4 kWh/day. That is roughly enough to warm the tank by about **5.5 °C per day** with no losses (6.4 ÷ 1.16). *Estimate.* Depending on the season, lighting could help or overheat the culture, especially in Rajasthan summers.

## Engineering assumptions

- Indoor operation [P3], with room temperature not controlled beyond what the building provides.
- Start from a known, clean mother culture of *Arthrospira*, as with the 10 L build. Scale up in stages (10 L → intermediate volumes → 1,000 L), not by direct inoculation.
- Use a published medium recipe (e.g. Zarrouk-type or Jourdan's), documented with quantities and dates.

## Proposed features

- **Lighting options to evaluate** (not chosen):
  - (a) lid-mounted LEDs only;
  - (b) lid LEDs plus appropriately rated submersible tube lights to light the depth;
  - (c) lower working volume (shallower depth) at first.
- **Photoperiod schedule** (e.g. 16 h, see above) in firmware/config, with logging.
- **Temperature control:** logging first. Heating and/or cooling only after a season of data. Heater planned per [P1] Step 7.
- **pH and medium management:** pH and conductivity logging; MCU-controlled dosing within hard limits; manual top-up of evaporated water.
- **Culture health checks:** scheduled microscope samples, logged images, and contaminant **flags for human review**.

## Unresolved issues

1. **Light penetration** at ~0.8–1 m+ depth. Most of the volume may be dark unless the culture is very dilute or internal lighting is used.
2. **Thermal management:** heating in winter, overheating from lights and summer ambient.
3. **Mixing** enough to cycle cells between lit and dark zones (see [mechanical.md](mechanical.md)).
4. **Contamination control** in a large indoor tank (airborne, water, tools, grazers). How quickly can it be detected by microscope?
5. **Food safety:** no testing plan, no lab partner, no regulatory review yet. See [harvesting.md](harvesting.md#food-safety).
