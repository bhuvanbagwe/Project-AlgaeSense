#include "Arduino_RouterBridge.h"

const int LIGHT_PIN = D5;
const int PUMP_PIN = D6;
const int AERATOR_PIN = D9;

int toPWM(int percent) {
  percent = constrain(percent, 0, 100);
  return map(percent, 0, 100, 0, 255);
}

void setLight(int percent) {
  analogWrite(LIGHT_PIN, toPWM(percent));
}

void setAerator(int percent) {
  analogWrite(AERATOR_PIN, toPWM(percent));
}

void samplePump(int durationMs) {
  durationMs = constrain(durationMs, 100, 10000);

  analogWrite(PUMP_PIN, 255);
  delay(durationMs);
  analogWrite(PUMP_PIN, 0);
}

void allOff() {
  analogWrite(LIGHT_PIN, 0);
  analogWrite(PUMP_PIN, 0);
  analogWrite(AERATOR_PIN, 0);
}

void setup() {
  analogWriteResolution(8);

  allOff();

  Bridge.begin();

  Bridge.provide_safe("light", setLight);
  Bridge.provide_safe("aerator", setAerator);
  Bridge.provide_safe("sample", samplePump);
  Bridge.provide_safe("all_off", allOff);
}

void loop() {
}
