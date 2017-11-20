#include <DHT.h>

#define DHTPIN 2
#define DHTYPE DHT11
DHT dht(DHTPIN, DHTYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();
}

void loop() {
  int temperature = dht.readTemperature();
  sendData(temperature, true);
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
