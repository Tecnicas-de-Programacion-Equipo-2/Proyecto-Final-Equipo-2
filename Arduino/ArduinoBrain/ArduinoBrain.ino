#include <DHT.h>

#define SENSOR1PIN 2
#define SENSOR2PIN 3
#define DHTYPE DHT11

#define MOTOR1 5
#define MOTOR2 6

String data;

DHT sensor_room1(SENSOR1PIN, DHTYPE);
DHT sensor_room2(SENSOR2PIN, DHTYPE);

void setup() {
  pinMode(MOTOR1, OUTPUT);
  pinMode(MOTOR2, OUTPUT);
  Serial.begin(115200);
  sensor_room1.begin();
  sensor_room2.begin();
}

void loop() {
  int temperature_room1 = sensor_room1.readTemperature();
  int temperature_room2 = sensor_room2.readTemperature();
  
  sendData(temperature_room1, false);
  sendData(temperature_room2, true);
}

void sendData(int value, bool is_complete) {
  Serial.print(value);
  if (is_complete) {
    Serial.print("\n");
  }
  else {
    Serial.print(", ");
  }
}

void serialEvent(){
  String data = Serial.readString();
  
  if(data == "1_on") {
      digitalWrite(MOTOR1, HIGH);
  }
  if(data == "2_on") {
    digitalWrite(MOTOR2, HIGH);
  }
  if(data == "1_off") {
    digitalWrite(MOTOR1, LOW);
  }
  if(data == "2_off") {
    digitalWrite(MOTOR2, LOW);
  }
}
