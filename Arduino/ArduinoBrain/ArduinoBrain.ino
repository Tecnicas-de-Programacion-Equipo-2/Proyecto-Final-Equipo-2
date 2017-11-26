#include <DHT.h>

#define SENSOR1PIN 2
//#define SENSOR2PIN 3
#define DHTYPE DHT11

#define MOTOR1LEFT 5
#define MOTOR1RIGHT 6
#define MOTOR2LEFT 10
#define MOTOR2RIGHT 11

DHT sensor_room1(SENSOR1PIN, DHTYPE);
//DHT sensor_room2(SENSOR2PIN, DHTYPE);

void setup() {
  pinMode(MOTOR1LEFT, OUTPUT);
  pinMode(MOTOR1RIGHT, OUTPUT);
  pinMode(MOTOR2LEFT, OUTPUT);
  pinMode(MOTOR2RIGHT, OUTPUT);
  Serial.begin(115200);
  sensor_room1.begin();
  //sensor_room2.begin();
}

void loop() {
  int temperature_room1 = sensor_room1.readTemperature();
  //int temperature_room2 = sensor_room2.readTemperature();
  
  while(Serial.available()) {
    String data = String(Serial.readString());
    if(data == "1_on") {
      digitalWrite(MOTOR1LEFT, HIGH);
      digitalWrite(MOTOR1RIGHT, HIGH);
    }
    if(data == "2_on") {
      digitalWrite(MOTOR2LEFT, HIGH);
      digitalWrite(MOTOR2RIGHT, HIGH);
    }
    if(data == "1_off") {
      digitalWrite(MOTOR1LEFT, LOW);
      digitalWrite(MOTOR1RIGHT, LOW);
    }
    if(data == "2_off") {
      digitalWrite(MOTOR2LEFT, LOW);
      digitalWrite(MOTOR2RIGHT, LOW);
    }
  }

  sendData(temperature_room1, false);
  sendData(temperature_room1, true);
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
