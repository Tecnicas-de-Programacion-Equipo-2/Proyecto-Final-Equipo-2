#include <Servo.h>

Servo DoorsMotor;

void setup() {
  DoorsMotor.attach(9);
  Serial.begin(115200);
}

void loop() { }

void serialEvent(){
  String input = Serial.readString();
  
  if (input == "DoorO" or input == "DoorC"){
    DoorHandler(input);
    }
  }
  
void DoorHandler(String DoorState){
  int state = DoorState == "DoorO" ? 90 : 0;
  DoorsMotor.write(state);
  }
