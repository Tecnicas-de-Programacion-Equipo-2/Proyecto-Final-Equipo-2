#include <SPI.h>
#include <MFRC522.h>
#include <Servo.h>

//TEst

#define RST_PIN  9    
#define SS_PIN  10 

int latchPin = 5;
int clockPin = 6;
int dataPin = 4;
int outputEnablePin = 3;
bool Room1 = false;
bool Room2 = false;

Servo DoorsMotor;
MFRC522 Lector1(SS_PIN, RST_PIN);

void setup() {
  Serial.begin(115200);
  
  SPI.begin();       
  Lector1.PCD_Init(); 
  
  DoorsMotor.attach(9);
  
  pinMode(latchPin, OUTPUT); 
  pinMode(dataPin, OUTPUT);  
  pinMode(clockPin, OUTPUT);
  pinMode(outputEnablePin, OUTPUT);
}

void loop() {
  if ( Lector1.PICC_IsNewCardPresent())   
  { 
      if ( Lector1.PICC_ReadCardSerial())
      {
        for (byte i = 0; i < Lector1.uid.size; i++) {
          Serial.print(Lector1.uid.uidByte[i], DEC);
        }
        Serial.println(" ");
        //Lector1.PICC_HaltA();
        //Lector1.PCD_StopCrypto1();       
      }
  }
  else{
    Serial.println(0);
  }
}

void serialEvent(){
  String input = Serial.readString();

  int room_1 = getValue(input, ' ', 0).toInt();
  int room_2 = getValue(input, ' ', 1).toInt();
  String room_3 = getValue(input, ' ', 2);
  String room_4 = getValue(input, ' ', 3);
  
  if (input == "DoorO" or input == "DoorC") {
    DoorHandler(input);
  }
  
  if (input == "Room1On" or input == "Room1Off") {
    LightHandlerRoom1(input);
  }
    
  if (input == "Room2On" or input == "Room2Off") {
    LightHandlerRoom2(input);
  }
}

void DoorHandler(String DoorState) {
  int state = DoorState == "DoorO" ? 90 : 0;
  DoorsMotor.write(state);
}

void LightHandlerRoom1(String LightState) {
    byte bitsToSend = 0;
    
    if (LightState == "Room1On" and Room2 == false) {
      digitalWrite(latchPin, LOW);
      bitWrite(bitsToSend, 0, HIGH);
      bitWrite(bitsToSend, 1, HIGH);
      bitWrite(bitsToSend, 2, HIGH);
      shiftOut(dataPin, clockPin, MSBFIRST, bitsToSend);
      digitalWrite(latchPin, HIGH);
      setBrightness(50);
      Room1 = true;
    }
    else if (LightState == "Room1On" and Room2 == true) {
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
    else if (LightState =="Room1Off" and Room2 == false) {
      digitalWrite(latchPin, LOW);
      shiftOut(dataPin, clockPin, MSBFIRST, bitsToSend);
      digitalWrite(latchPin, HIGH);
      Room1 = false;
    }
    else if (LightState =="Room1Off" and Room2 == true) {
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

void LightHandlerRoom2(String LightState) {
    byte bitsToSend = 0;
    
    if (LightState == "Room2On" and Room1 == false) {
      digitalWrite(latchPin, LOW);
      bitWrite(bitsToSend, 3, HIGH);
      bitWrite(bitsToSend, 4, HIGH);
      bitWrite(bitsToSend, 5, HIGH);
      shiftOut(dataPin, clockPin, MSBFIRST, bitsToSend);
      digitalWrite(latchPin, HIGH);
      Room2 = true;
    }
    else if (LightState == "Room2On" and Room1 == true) {
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
    else if (LightState =="Room2Off" and Room1 == false) {
      digitalWrite(latchPin, LOW);
      shiftOut(dataPin, clockPin, MSBFIRST, bitsToSend);
      digitalWrite(latchPin, HIGH);
      Room2 = false;
    }
    else if (LightState == "Room2Off" and Room1 == true) {
      digitalWrite(latchPin, LOW);
      bitWrite(bitsToSend, 0, HIGH);
      bitWrite(bitsToSend, 1, HIGH);
      bitWrite(bitsToSend, 2, HIGH);
      shiftOut(dataPin, clockPin, MSBFIRST, bitsToSend);
      digitalWrite(latchPin, HIGH);
      Room2 = false;
    }
}

void setBrightness(byte brightness) {
  analogWrite(outputEnablePin, 255 - brightness);
}

String getValue(String data, char separator, int index) {
    int found = 0;
    int strIndex[] = { 0, -1 };
    int maxIndex = data.length() - 1;

    for (int i = 0; i <= maxIndex && found <= index; i++) {
        if (data.charAt(i) == separator || i == maxIndex) {
            found++;
            strIndex[0] = strIndex[1] + 1;
            strIndex[1] = (i == maxIndex) ? i+1 : i;
        }
    }
    return found > index ? data.substring(strIndex[0], strIndex[1]) : "";
}
