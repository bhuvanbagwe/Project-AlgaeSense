import time
import threading

from arduino.app_utils import App, Bridge
from arduino.app_bricks.web_ui import WebUI
from arduino.app_peripherals.camera import Camera


# =========================================================
# CONFIG
# =========================================================

PUMP_ON_TIME_MS = 5000
PUMP_INTERVAL_SECONDS = 20


# =========================================================
# CAMERA + WEB DASHBOARD
# =========================================================

camera = Camera(
    resolution=(640, 480),
    fps=10
)

ui = WebUI()

camera.start()

# Working live microscope feed
ui.expose_camera(
    "/camera",
    camera
)


# =========================================================
# PUMP LOOP
# =========================================================

def run_pump_once():

    print(
        "[AlgaeSense] Peristaltic pump ON for 5 seconds",
        flush=True
    )

    Bridge.call(
        "start_sample",
        PUMP_ON_TIME_MS
    )


    timeout = (
        time.time()
        + 7
    )


    while time.time() < timeout:

        try:

            running = Bridge.call(
                "pump_running"
            )

            if not running:
                break

        except Exception as error:

            print(
                "[AlgaeSense] Pump status error:",
                error,
                flush=True
            )

            break


        time.sleep(0.1)


    # Safety stop
    try:

        Bridge.call(
            "stop_sample"
        )

    except Exception:
        pass


    print(
        "[AlgaeSense] Peristaltic pump OFF",
        flush=True
    )


def pump_loop():

    print()
    print(
        "========================================"
    )
    print(
        "AlgaeSense started"
    )
    print(
        "Camera dashboard: ACTIVE"
    )
    print(
        "Pump cycle: 5 sec ON every 20 sec"
    )
    print(
        "========================================"
    )
    print()


    # Wait before first pump cycle
    time.sleep(
        PUMP_INTERVAL_SECONDS
    )


    while True:

        try:

            run_pump_once()

        except Exception as error:

            print(
                "[AlgaeSense] Pump loop error:",
                error,
                flush=True
            )


        # 20 seconds between pump activations
        time.sleep(
            PUMP_INTERVAL_SECONDS
        )


# =========================================================
# START BACKGROUND PUMP LOOP
# =========================================================

threading.Thread(
    target=pump_loop,
    daemon=True
).start()


# =========================================================
# KEEP APP RUNNING
# =========================================================

App.run()
