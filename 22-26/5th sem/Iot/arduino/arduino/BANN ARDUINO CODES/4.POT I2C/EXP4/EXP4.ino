#include <Wire.h>  
#include <LiquidCrystal_I2C.h>   
LiquidCrystal_I2C lcd(0x27,16,2);
int pot1=A0;
int pot1value=0;
void setup()
{
lcd.begin();
lcd.backlight();
}
void loop()
{
pot1value= analogRead(pot1);
lcd.clear();
lcd.setCursor(0,0);
lcd.print("POT_1: "); lcd.print(pot1value);
if(pot1value==1023)
{
  lcd.clear();
lcd.setCursor(0,0);
lcd.print("POT_1: "); lcd.print(pot1value);
lcd.setCursor(0,1);
lcd.print("    FULL ");
}
else if(pot1value>=600)
{
  lcd.clear();
lcd.setCursor(0,0);
lcd.print("POT_1: "); lcd.print(pot1value);
lcd.setCursor(0,1);
lcd.print("    FINE ");
}
else
{lcd.clear();
lcd.setCursor(0,0);
lcd.print("POT_1: "); lcd.print(pot1value);
lcd.setCursor(0,1);
lcd.print("    LOW ");
}
delay(3000);
} 
