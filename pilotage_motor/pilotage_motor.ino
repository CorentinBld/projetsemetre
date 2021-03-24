// Constants
const int enableBridge = 2;
const int MotorForward = 3;
const int MotorReverse = 5;

// Variables
int Power = 255; //Vitesse du moteur entre 0 et 255

void setup(){
  dcBegin();
}

void loop(){
  dcForward(Power);
  delay(2000);
  
  dcReverse(Power);
  delay(3000);
  
  dcStop();
  delay(1000);
}

void dcBegin(){
  // Initialise les pines utilisées pour le moteur
  pinMode(MotorForward,OUTPUT);
  pinMode(MotorReverse,OUTPUT);
  pinMode(enableBridge,OUTPUT);
  }

void dcForward(int P){
  digitalWrite(enableBridge,HIGH); // Active pont en H
  // Tourne dans le sens Forward à la vitesse spécifiée par P
  analogWrite(MotorForward,P);
  analogWrite(MotorReverse,0);
}

void dcReverse(int P){
  digitalWrite(enableBridge,HIGH); // Active pont en H
  // Tourne dans le sens Reverse à la vitesse spécifiée par P
  analogWrite(MotorForward,0);
  analogWrite(MotorReverse,P);
}

void dcStop(){
  // Arrête le moteur et désactive le pont en H
  analogWrite(MotorForward,0);
  analogWrite(MotorReverse,0);
  digitalWrite(enableBridge,LOW); 
}
