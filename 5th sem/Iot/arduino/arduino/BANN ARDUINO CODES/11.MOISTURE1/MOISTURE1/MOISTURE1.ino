#include <Wire.h>  
#include <LiquidCrystal_I2C.h>    
LiquidCrystal_I2C lcd(0x27,16,2);
int moisturesensor=A3;
int relay=3;
int moistvalue=0;

void setup() 
{
  lcd.begin();    
  lcd.backlight();
  Serial.begin(9600);
  pinMode(moisturesensor,INPUT);
  pinMode(relay,OUTPUT);
  }
void loop() 
{
   moistvalue=analogRead(moistvalue);
// Serial.println(irvalue);
if (moistvalue>=400)
{
  digitalWrite(relay,HIGH);
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("MOIST VALUE:");lcd.print(moistvalue);
  lcd.setCursor(0,1);
  lcd.print("TURN ON FAN");


}

else 
{

  digitalWrite(relay,LOW);
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("MOIST VALUE:");lcd.print(moistvalue);
  lcd.setCursor(0,1);
  lcd.print("TURN OFF FAN");

}
delay(2000);
}