#include <Wire.h>
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,16,2);
void setup()
{
lcd.begin();
  lcd.backlight();
  lcd.setCursor(0,0);
  lcd.print(" WELCOME TO EXCEL   ");   
}
void loop()
{
   lcd.setCursor(16,1);
   lcd.autoscroll();    // Set diplay to scroll automatically
   lcd.print(" ");      // set characters
   delay(700);    
}