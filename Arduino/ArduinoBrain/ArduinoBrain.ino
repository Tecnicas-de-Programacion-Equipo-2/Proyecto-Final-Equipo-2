#include <DHT.h>

#define SENSOR1PIN 2
//#define SENSOR2PIN 3
#define DHTYPE DHT11
DHT sensor_room1(SENSOR1PIN, DHTYPE);
//DHT sensor_room2(SENSOR2PIN, DHTYPE);

void setup() {
  Serial.begin(115200);
  sensor_room1.begin();
  //sensor_room2.begin();
}

void loop() {
  int temperature_room1 = sensor_room1.readTemperature();
  //int temperature_room2 = sensor_room2.readTemperature();
  sendData(temperature_room1, false);
  sendData(temperature_room1, true);
}

void sendData(int value, bool isComplete) {
  Serial.print(value);
  if (isComplete) {
    Serial.print("\n");
  }
  else {
    Serial.print(", ");
  }
}
