#include <DHT.h>

#define SENSOR1PIN 2
#define SENSOR2PIN 3
#define DHTYPE DHT11

#define MOTOR1 5
#define MOTOR2 6

const int Trigger = 9;
const int Echo = 8;
const int delay_time = 0;

String data;
long Time;
long Distance;

DHT sensor_room1(SENSOR1PIN, DHTYPE);
DHT sensor_room2(SENSOR2PIN, DHTYPE);

void setup() {
  pinMode(MOTOR1, OUTPUT);
  pinMode(MOTOR2, OUTPUT);
  pinMode(Trigger, OUTPUT);
  pinMode(Echo, INPUT);
  
  Serial.begin(115200);
  sensor_room1.begin();
  sensor_room2.begin();
}

void loop() {
  int temperature_room1 = sensor_room1.readTemperature();
  //delayMicroseconds(delay_time);
  int temperature_room2 = sensor_room2.readTemperature();
  //delayMicroseconds(delay_time);
  int humidity_room1 = sensor_room1.readHumidity();
  //delayMicroseconds(delay_time);
  int humidity_room2 = sensor_room2.readHumidity();
  //delayMicroseconds(delay_time);

  int distance = ultrasonicEvent();
  
  sendData(temperature_room1, false);
  sendData(temperature_room2, false);
  sendData(humidity_room1, false);
  sendData(humidity_room2, false);
  sendData(distance, true);
  //delayMicroseconds(delay_time);
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

void serialEvent() {
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
  //delayMicroseconds(delay_time);
}

int ultrasonicEvent() {
  digitalWrite(Trigger, LOW);
  //delayMicroseconds(delay_time);
  digitalWrite(Trigger, HIGH);
  //delayMicroseconds(delay_time);
  Time = pulseIn(Echo, HIGH);
  Distance = int(0.017 * Time);
  return Distance;
}

