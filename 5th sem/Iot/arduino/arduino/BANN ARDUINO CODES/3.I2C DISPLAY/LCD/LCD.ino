#include<Wire.h>
#include<LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,16,2);

void setup()
{
  lcd.begin();
  lcd.backlight();
  lcd.clear();
}
void loop()
{
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("  welcome to");
  lcd.setCursor(0,1);
  lcd.print("    PMC   ");
  delay(2000);
  lcd.clear();
  delay(2000);
}