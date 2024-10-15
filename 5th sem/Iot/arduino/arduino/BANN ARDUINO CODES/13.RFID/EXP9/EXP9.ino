#include <Wire.h> 
#include <LiquidCrystal_I2C.h>   
LiquidCrystal_I2C lcd(0x27,16,2); 

int buzzer = 2;     // Connect LED to D6
int relay1 = 15;     // Connect LED to D6

String readdata;


void setup() {
Serial.begin(9600); 
lcd.begin();
lcd.backlight();//To Power ON the back light
lcd.clear();//Clean the screen
lcd.setCursor(0,0); 
lcd.print(" WAITING FOR");
lcd.setCursor(0,1);
lcd.print("    CARD");delay(2000);
pinMode(buzzer,OUTPUT);
pinMode(relay1,OUTPUT);
}


void loop() 

{  
 
  while (Serial.available())
  { //Check if there is an available byte to read
delay(10); //Delay added to make thing stable
char c = Serial.read(); //Conduct a serial read
readdata += c; //
}
if (readdata.length() > 0) {
int n=readdata.length();
if(readdata=="4900F4F71953")//KARTHI
{
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("  PERMISSION");
  lcd.setCursor(0,1);
  lcd.print("   GRANTED");
   digitalWrite(relay1,HIGH);
    delay(3000);
   digitalWrite(relay1,LOW);
 }
 else 
 {
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("   PERMISSION");
  lcd.setCursor(0,1);
  lcd.print("     DENIED");
  digitalWrite(buzzer,HIGH);
  delay(3000);
  digitalWrite(buzzer,LOW);
 }
 
 }

readdata=""; //Reset the variable
 }
  
