#include <Ultrasonic.h>
int Trigger = 12;
int Echo = 13;
Ultrasonic ultrassom(Trigger, Echo);

long distancia;
void setup() {
  Serial.begin(9600);
}

void loop() {
   distancia = ultrassom.Ranging(CM); 
   Serial.println(distancia);
   delay(250);
   
}
