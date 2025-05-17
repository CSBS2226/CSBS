#include <Wire.h>  
#include <LiquidCrystal_I2C.h>    
LiquidCrystal_I2C lcd(0x27,16,2);
int ir=A2;
int relay=3;
int irvalue=0;

void setup() 
{
  lcd.begin();    
  lcd.backlight();

  
  Serial.begin(9600);
  pinMode(ir,INPUT);
  pinMode(relay,OUTPUT);
  }
void loop() 
{
   irvalue=analogRead(ir);
// Serial.println(irvalue);
if (irvalue>=450)
{
  digitalWrite(relay,HIGH);
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("IR VALUE:");lcd.print(irvalue);
  lcd.setCursor(0,1);
  lcd.print("OPENING DOOR...");


}

else 
{

  digitalWrite(relay,LOW);
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("IR VALUE:");lcd.print(irvalue);
  lcd.setCursor(0,1);
  lcd.print("CLOSING DOOR...");

}
delay(2000);
}