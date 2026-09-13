#include <Arduino_RouterBridge.h>

const int LIGHT_PIN = D5;
const int PUMP_PIN = D6;

const int MAX_PUMP_TIME = 10000;

bool pumpRunning = false;
unsigned long pumpStopTime = 0;

int pwmFromPercent(int percent) {
  percent = constrain(percent, 0, 100);
  return map(percent, 0, 100, 0, 255);
}

bool setLight(int percent) {
  analogWrite(LIGHT_PIN, pwmFromPercent(percent));
  return true;
}

bool startSample(int durationMs) {
  durationMs = constrain(durationMs, 100, MAX_PUMP_TIME);

  analogWrite(PUMP_PIN, 255);

  pumpRunning = true;
  pumpStopTime = millis() + durationMs;

  return true;
}

bool stopSample() {
  analogWrite(PUMP_PIN, 0);
  pumpRunning = false;
  return true;
}

bool allOff() {
  analogWrite(LIGHT_PIN, 0);
  analogWrite(PUMP_PIN, 0);
  pumpRunning = false;
  return true;
}

bool isPumpRunning() {
  return pumpRunning;
}

void setup() {
  Bridge.begin();
  Monitor.begin(115200);

  analogWrite(LIGHT_PIN, 0);
  analogWrite(PUMP_PIN, 0);

  Bridge.provide_safe("set_light", setLight);
  Bridge.provide_safe("start_sample", startSample);
  Bridge.provide_safe("stop_sample", stopSample);
  Bridge.provide_safe("all_off", allOff);
  Bridge.provide_safe("pump_running", isPumpRunning);

  Monitor.println("AlgaeSense MCU ready");
}

void loop() {
  if (pumpRunning &&
      (long)(millis() - pumpStopTime) >= 0) {
    stopSample();
  }
}
