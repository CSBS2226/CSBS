#include <Wire.h>  
#include <LiquidCrystal_I2C.h>   
LiquidCrystal_I2C lcd(0x27,16,2);
int gassensor=A1;
int buzzer = 10;
int relay = 2;
int gasvalue=0;
void setup()
{
pinMode(buzzer , OUTPUT);
pinMode(relay , OUTPUT);
lcd.begin();
lcd.backlight();
}
void loop()
{
gasvalue= analogRead(gassensor);
lcd.clear();
lcd.setCursor(0,0);
lcd.print("GAS: "); lcd.print(gasvalue);
if (gasvalue > 120)
{
digitalWrite(relay, HIGH);
digitalWrite(buzzer, HIGH);
lcd.setCursor(0,1);
lcd.print("FAN: ON"); 
}
else
{
digitalWrite(relay, LOW);
digitalWrite(buzzer, LOW);
lcd.setCursor(0,1);
lcd.print("FAN: OFF"); 
}
delay(3000);
} 
