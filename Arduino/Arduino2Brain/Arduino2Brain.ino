#include <SPI.h>
#include <MFRC522.h>
#include <Servo.h>

#define RST_PIN  9    
#define SS_PIN  10 

int RoomLight1 = 3;
int RoomLight2 = 5;
int RoomLight3 = 6;
int RoomLight4 = 11;

Servo DoorsMotor;
MFRC522 Lector1(SS_PIN, RST_PIN);

void setup() {
  Serial.begin(115200);
  
  SPI.begin();       
  Lector1.PCD_Init(); 
  
  DoorsMotor.attach(6);
  
  pinMode(RoomLight1, OUTPUT); 
  pinMode(RoomLight2, OUTPUT);  
  pinMode(RoomLight3, OUTPUT);
  pinMode(RoomLight4, OUTPUT);
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
  int room_3 = getValue(input, ' ', 2).toInt();
  int room_4 = getValue(input, ' ', 3).toInt();
  String door_status = getValue(input, ' ', 4);

  DoorHandler(door_status);
  
  LightHandler(room_1,room_2,room_3,room_4);
}

void DoorHandler(String DoorState) {
  int state = DoorState == "DoorO" ? 90 : 0;
  DoorsMotor.write(state);
}

void LightHandler(int room_1, int room_2, int room_3, int room_4) {
   analogWrite(RoomLight1,room_1);
   analogWrite(RoomLight2,room_2);
   analogWrite(RoomLight3,room_3);
   analogWrite(RoomLight4,room_4);
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
