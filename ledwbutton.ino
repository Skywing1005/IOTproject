int pinButton = 4;
int LED = 13;
void setup() {
  // put your setup code here, to run once:
pinMode(pinButton,INPUT);
pinMode(LED,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
int stateButton = digitalRead(pinButton);
if(stateButton == 1)
{
  digitalWrite(LED,HIGH);
  }
  else{
    digitalWrite(LED,LOW);
    }
}
