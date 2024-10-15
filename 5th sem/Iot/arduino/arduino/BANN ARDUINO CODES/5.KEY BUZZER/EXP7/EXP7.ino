int buzzer = 5;
int key1 = 6;
void setup()
{
pinMode(buzzer , OUTPUT);
pinMode(key1 , INPUT);
}
void loop()
{
if(digitalRead(key1)==1)
digitalWrite(buzzer, HIGH);
else
digitalWrite(buzzer, LOW);
} 
