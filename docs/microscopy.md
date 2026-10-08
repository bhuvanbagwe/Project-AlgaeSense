# Microscopy-based monitoring

AlgaeSense's main idea is to **look at the culture under a microscope** and base decisions on what the camera sees. This page separates what is running now, what existed earlier, what was shown on Instructables, and what is planned.

## Why a microscope?

Spirulina filaments (trichomes) are about **50–500 µm long and 3–4 µm wide** ([F1] p. 3). A cheap USB microscope can make them visible ([P1] Step 8). Under magnification you can see whether the filaments are present, what shape they are, and whether other organisms are present. A simple colour or turbidity reading cannot show those things.

## Sampling path (10 L prototype, [P1] Step 7)

1. A food-safe surgical tube dips into the tank.
2. The 3D-printed peristaltic pump draws culture into a 3D-printed measuring chamber. One end of the chamber has an acrylic slit to look through.
3. The pump stops and the sample is left to settle. The Instructables text says "switched off for 5 seconds to let algae samples settle".
4. The USB microscope captures several frames.

In the current code, step 2 runs on a timer (5 s on, then 20 s wait) and step 4 is a live stream only. No frames are captured for analysis. See [software.md](software.md).

## Getting a usable image from a cheap USB microscope

From [P1] Step 8: the author did not know the magnification number. The first images were not usable. Moving the microscope's focus "a little bit forward" gave images good enough to label and use for training. The microscope was "a normal PCB soldering USB microscope". The exact model and magnification are _not documented_.

Tips for reproducing this (general advice, not measured):

- Keep the viewing slit clean and scratch-free. Bubbles from aeration can look like objects.
- Use steady, diffuse back-lighting through the chamber if possible.
- Record the camera resolution and focus position so results can be compared across runs.

## Stage 1 — live stream (current)

`python/main.py` opens the camera at 640 × 480, 10 fps. `WebUI.expose_camera()` serves it as an MJPEG stream at `/camera` [A3], which `assets/index.html` displays. This lets a person watch the sample. It is **not** automated monitoring.

## Stage 0 — dark-pixel "relative density" (history, 2026-08-25)

The first `main.py` (commit `ecbac5b`) estimated density without OpenCV:

1. Crop 5 % from each edge of the frame.
2. Convert to grey by averaging the colour channels.
3. Take the **median grey level** as the background.
4. Count pixels darker than `background − 18`.
5. Report the percentage of such pixels. Take the median over 5 frames, 0.4 s apart.

The result drove fixed light/aerator levels: below 5 % → LED 70 %, aerator 50 %; below 15 % → 60 %/55 %; otherwise 50 %/65 %.

Limitations: the number depends on focus, lighting, bubbles and debris. It was never calibrated against a reference measurement. This code was removed on 2026-09-13.

## Detection model shown on Instructables (not in this repo)

From [P1] Steps 2, 9 and 10:

- "Currently the AI operating our photobioreactor is limited to video object detection".
- "I generated a dataset of around 100 images currently, each containing our individual algae cells in different orientations". Individual Spirulina strains were labelled manually. Screenshots show bounding boxes labelled "Spirulina".
- The article says the model "also detects for possible contaminants" and judges sample health "based on coloration, expected growth levels and other parameters". It mentions a confusion matrix.

**Status:** the model, dataset, training settings and evaluation results are **not in this repository**. The claims above cannot be reproduced from the repo and are reported here only as written in [P1]. With about 100 images, any accuracy figure should be treated as preliminary.

## Planned pipeline

Proposed, in order of difficulty:

1. **Frame capture and logging:** save timestamped frames after each settle period.
2. **Preprocessing (OpenCV):** flat-field/background correction, denoising, bubble rejection.
3. **Segmentation:** threshold or adaptive threshold → contours → filter by size and elongation to keep filament-like objects.
4. **Metrics per sample:** filament count, covered area, and a straight vs helical ratio. Straight filaments are relevant because they are harder to harvest ([J1] p. 6).
5. **Calibration:** compare image metrics with a reference such as dry weight per litre, optical density or a Secchi-disk reading ([J1] p. 5). Without this, image numbers are relative only.
6. **Contaminant flags:** objects that don't look like filaments (e.g. single round cells) flagged for **human review**. Jourdan notes Chlorella can invade a culture that is too dilute ([J1] p. 10).
7. **Model publishing:** if a learned detector is used, publish the dataset, labels, training configuration and evaluation, so results can be checked.

### What microscopy cannot do

A microscope image **cannot confirm that biomass is safe to eat**. It cannot detect dissolved toxins (e.g. microcystins), heavy metals or bacterial load. Those need laboratory tests ([F1] pp. 17, 19; [J1] p. 10). Treat any "contamination detection" from images as an early warning only.
