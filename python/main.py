import time
import numpy as np

from datetime import datetime
from zoneinfo import ZoneInfo

from arduino.app_utils import App, Bridge
from arduino.app_peripherals.camera import Camera


DAY_START = 6
DAY_END = 22

DAY_LIGHT = 65
DAY_AERATOR = 55
NIGHT_AERATOR = 35

SAMPLE_INTERVAL = 60
PUMP_TIME_MS = 4000
SETTLE_TIME = 3

IMAGE_COUNT = 5
IMAGE_INTERVAL = 0.4

AI_ENABLED = False


camera = Camera(resolution=(640, 480))
camera.start()

started = False
last_sample = 0


def is_day():
    hour = datetime.now(
        ZoneInfo("Asia/Kolkata")
    ).hour

    return DAY_START <= hour < DAY_END


def set_growth_mode():
    if is_day():
        Bridge.call("light", DAY_LIGHT)
        Bridge.call("aerator", DAY_AERATOR)
    else:
        Bridge.call("light", 0)
        Bridge.call("aerator", NIGHT_AERATOR)


def image_density(frame):
    h, w = frame.shape[:2]

    frame = frame[
        h // 20:h - h // 20,
        w // 20:w - w // 20
    ]

    if frame.ndim == 3:
        gray = frame.mean(axis=2)
    else:
        gray = frame.astype(float)

    background = np.median(gray)

    algae_pixels = gray < (background - 18)

    return float(
        np.mean(algae_pixels) * 100
    )


def analyse_sample():
    densities = []

    for _ in range(IMAGE_COUNT):
        frame = camera.capture()

        density = image_density(frame)
        densities.append(density)

        time.sleep(IMAGE_INTERVAL)

    return float(np.median(densities))


def make_decision(density):
    if not is_day():
        return 0, NIGHT_AERATOR

    if density < 5:
        return 70, 50

    if density < 15:
        return 60, 55

    return 50, 65


def sample_cycle():
    print("Sampling")

    Bridge.call("aerator", 0)
    time.sleep(2)

    Bridge.call("sample", PUMP_TIME_MS)

    time.sleep(SETTLE_TIME)

    density = analyse_sample()

    light, aerator = make_decision(density)

    Bridge.call("light", light)
    Bridge.call("aerator", aerator)

    print(
        "Relative density:",
        round(density, 2),
        "%",
        "Light:",
        light,
        "Aerator:",
        aerator
    )


def loop():
    global started
    global last_sample

    if not started:
        Bridge.call("all_off")
        time.sleep(1)

        set_growth_mode()

        started = True
        last_sample = time.time()

        print("AlgaeSense running")

    if time.time() - last_sample >= SAMPLE_INTERVAL:
        sample_cycle()
        last_sample = time.time()

    time.sleep(0.2)


App.run(user_loop=loop)
