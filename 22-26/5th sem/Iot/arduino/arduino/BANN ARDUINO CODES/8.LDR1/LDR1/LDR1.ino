#include <Wire.h>  
#include <LiquidCrystal_I2C.h>   
LiquidCrystal_I2C lcd(0x27,16,2);
int lightsensor=A0;
int led = 2;
int lightvalue=0;
void setup()
{
pinMode(led , OUTPUT);
lcd.begin();
lcd.backlight();
}
void loop()
{
lightvalue= analogRead(lightsensor);
lcd.clear();
lcd.setCursor(0,0);
lcd.print("LIGHT: "); lcd.print(lightvalue);
if (lightvalue < 800)
{
digitalWrite(led, HIGH);
lcd.setCursor(0,1);
lcd.print("LAMP: ON"); 
}
else
{
digitalWrite(led, LOW);
lcd.setCursor(0,1);
lcd.print("LAMP: OFF"); 
}
delay(3000);
} 
