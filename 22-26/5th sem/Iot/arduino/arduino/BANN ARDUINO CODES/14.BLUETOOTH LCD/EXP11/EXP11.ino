#include <Wire.h>  
#include <LiquidCrystal_I2C.h>    
LiquidCrystal_I2C lcd(0x27,16,2);
String read_data;
void setup()
{
 Serial.begin(9600);
  lcd.begin();
  lcd.backlight();
  lcd.clear();
}
void loop()
{
while (Serial.available())
  {
delay(10);
char c = Serial.read();
read_data+= c; 

}
if (read_data.length() > 0)
{
Serial.print("RECIEVED DATA:");
Serial.println(read_data);
lcd.clear();
lcd.setCursor(0,0);
lcd.print("RECIEVED DATA");
lcd.setCursor(0,1);
lcd.print(read_data);
delay(1000);
}
read_data=""; 
}