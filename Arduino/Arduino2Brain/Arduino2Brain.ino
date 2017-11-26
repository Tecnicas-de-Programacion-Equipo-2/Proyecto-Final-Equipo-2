#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN  9    
#define SS_PIN  10   
MFRC522 Lector1(SS_PIN, RST_PIN);

void setup() {
  Serial.begin(115200);
  SPI.begin();       
  Lector1.PCD_Init(); 
}
void loop() {
  if ( Lector1.PICC_IsNewCardPresent())   
    { 
      if ( Lector1.PICC_ReadCardSerial())
      {
        for (byte i = 0; i < Lector1.uid.size; i++) {
          //Serial.print(Lector1.uid.uidByte[i] < 0x10 ? " 0" : " ");
          Serial.print(Lector1.uid.uidByte[i], DEC);
        }
        Serial.println(" ");
        //Lector1.PICC_HaltA();
        //Lector1.PCD_StopCrypto1();       
      }
    }
}

