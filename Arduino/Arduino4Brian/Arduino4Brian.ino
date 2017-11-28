const int Trigger = 2;  
const int Echo = 3;   

void setup() {
  Serial.begin(9600);
  pinMode(Trigger, OUTPUT); 
  pinMode(Echo, INPUT);  
  digitalWrite(Trigger, LOW);
}

void loop(){

  long tiempo; 
  long distancia;
  
  distancia = tiempo*0.017;
  if (distancia<0 || distancia > 30){
    distancia = 0;
    sendData(distancia);
  }
  else{
    sendData(distancia);
  }
}

void sendData(int distancia){
  Serial.println(distancia);
  delay(50);
}

