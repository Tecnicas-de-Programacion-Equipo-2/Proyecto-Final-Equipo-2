#include <Servo.h>

int latchPin = 5;
int clockPin = 6;
int dataPin = 4;
int outputEnablePin = 3;
Servo DoorsMotor;
bool Room1 = false;
bool Room2 = false;

void setup() {
  DoorsMotor.attach(9);
  
  pinMode(latchPin, OUTPUT); 
  pinMode(dataPin, OUTPUT);  
  pinMode(clockPin, OUTPUT);
  pinMode(outputEnablePin, OUTPUT);
   
  Serial.begin(115200);
}

void loop() { }

void serialEvent(){
  String input = Serial.readString();
  
  if (input == "DoorO" or input == "DoorC"){
    DoorHandler(input);
    }
  
  if (input == "Room1On" or input == "Room1Off"){
    LightHandlerRoom1(input);
    }
    
  if (input == "Room2On" or input == "Room2Off"){
    LightHandlerRoom2(input);
    }
  }
  
void DoorHandler(String DoorState){
  int state = DoorState == "DoorO" ? 90 : 0;
  DoorsMotor.write(state);
  }
void LightHandlerRoom1(String LightState){
    byte bitsToSend = 0;
    
    if (LightState == "Room1On" and Room2 == false){
      digitalWrite(latchPin, LOW);
      bitWrite(bitsToSend, 0, HIGH);
      bitWrite(bitsToSend, 1, HIGH);
      bitWrite(bitsToSend, 2, HIGH);
      shiftOut(dataPin, clockPin, MSBFIRST, bitsToSend);
      digitalWrite(latchPin, HIGH);
      setBrightness(50);
      Room1 = true;
    }
     else if (LightState == "Room1On" and Room2 == true){
      digitalWrite(latchPin, LOW);
      bitWrite(bitsToSend, 0, HIGH);
      bitWrite(bitsToSend, 1, HIGH);
      bitWrite(bitsToSend, 2, HIGH);
      bitWrite(bitsToSend, 3, HIGH);
      bitWrite(bitsToSend, 4, HIGH);
      bitWrite(bitsToSend, 5, HIGH);
      shiftOut(dataPin, clockPin, MSBFIRST, bitsToSend);
      digitalWrite(latchPin, HIGH);
      setBrightness(255);
      Room1 = true;
    }
    else if (LightState =="Room1Off" and Room2 == false){
      digitalWrite(latchPin, LOW);
      shiftOut(dataPin, clockPin, MSBFIRST, bitsToSend);
      digitalWrite(latchPin, HIGH);
      Room1 = false;
    }
    else if (LightState =="Room1Off" and Room2 == true){
      digitalWrite(latchPin, LOW);
      bitWrite(bitsToSend, 0, LOW);
      bitWrite(bitsToSend, 1, LOW);
      bitWrite(bitsToSend, 2, LOW);
      bitWrite(bitsToSend, 3, HIGH);
      bitWrite(bitsToSend, 4, HIGH);
      bitWrite(bitsToSend, 5, HIGH);
      shiftOut(dataPin, clockPin, MSBFIRST, bitsToSend);
      digitalWrite(latchPin, HIGH);
      setBrightness(150);
      Room1 = false;
    }
    
  
  }

void LightHandlerRoom2(String LightState){
    byte bitsToSend = 0;
    
    if (LightState == "Room2On" and Room1 == false){
      digitalWrite(latchPin, LOW);
      bitWrite(bitsToSend, 3, HIGH);
      bitWrite(bitsToSend, 4, HIGH);
      bitWrite(bitsToSend, 5, HIGH);
      shiftOut(dataPin, clockPin, MSBFIRST, bitsToSend);
      digitalWrite(latchPin, HIGH);
      Room2 = true;
    }
     else if (LightState == "Room2On" and Room1 == true){
      digitalWrite(latchPin, LOW);
      bitWrite(bitsToSend, 0, HIGH);
      bitWrite(bitsToSend, 1, HIGH);
      bitWrite(bitsToSend, 2, HIGH);
      bitWrite(bitsToSend, 3, HIGH);
      bitWrite(bitsToSend, 4, HIGH);
      bitWrite(bitsToSend, 5, HIGH);
      shiftOut(dataPin, clockPin, MSBFIRST, bitsToSend);
      digitalWrite(latchPin, HIGH);
      Room2 = true;
    }
    else if (LightState =="Room2Off" and Room1 == false){
      digitalWrite(latchPin, LOW);
      shiftOut(dataPin, clockPin, MSBFIRST, bitsToSend);
      digitalWrite(latchPin, HIGH);
      Room2 = false;
    }
     else if (LightState == "Room2Off" and Room1 == true){
      digitalWrite(latchPin, LOW);
      bitWrite(bitsToSend, 0, HIGH);
      bitWrite(bitsToSend, 1, HIGH);
      bitWrite(bitsToSend, 2, HIGH);
      shiftOut(dataPin, clockPin, MSBFIRST, bitsToSend);
      digitalWrite(latchPin, HIGH);
      Room2 = false;
    }
  
  }

void setBrightness(byte brightness)
{
  analogWrite(outputEnablePin, 255-brightness);
}
