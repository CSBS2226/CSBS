#include <Wire.h>  
#include <LiquidCrystal_I2C.h>   
LiquidCrystal_I2C lcd(0x27,16,2);
int led1 = 2;
int led2 = 3;
int relay1 = 4;
int relay2 = 5;
int led1data=0;
int led2data=0;
int relay1data=0;
int relay2data=0;
char data;
void setup()
{
  Serial.begin(9600);
pinMode(led1 , OUTPUT);
pinMode(led2 , OUTPUT);
pinMode(relay1 , OUTPUT);
pinMode(relay2 , OUTPUT);
lcd.begin();
lcd.backlight();
}
void loop()
{
if (Serial.available())
{
data = Serial.read();
if(data=='1')
{
led1data=1;
//l1=1;
}
else if(data=='2')
{
led1data=0;
//l1=0;
}
else if(data=='3')
{
led2data=1;
//l2=1;
}
else if(data=='4')
{
led2data=0;
//l2=0;
}
else if(data=='5')
{
relay1data=1;
//r1=1;
}
else if(data=='6')
{
relay1data=0;
//r1=0;
}
else if(data=='7')
{
relay2data=1;
//r2=1;
}
else if(data=='8')
{
relay2data=0;
//r2=0;
}
else if(data=='9')
{

led1data=0;led2data=0;relay1data=0;relay2data=0;
}
else 
{

delay(100);
}
}
lcd.clear();
lcd.setCursor(0,0);
if(led1data==1)
{
lcd.print("L1: ON  |"); 
digitalWrite(led1, HIGH);
}
else
{
lcd.print("L1: OFF |"); 
digitalWrite(led1, LOW);
}
if(led2data==1)
{
lcd.print("L2: ON  |"); 
digitalWrite(led2, HIGH);
}
else
{
lcd.print("L2: OFF |"); 
digitalWrite(led2, LOW);
}
lcd.setCursor(0,1);
if(relay1data==1)
{
lcd.print("R1: ON  |"); 
digitalWrite(relay1, HIGH);
}
else
{
lcd.print("R1: OFF |"); 
digitalWrite(relay1, LOW);
}
if(relay2data==1)
{
lcd.print("R2: ON  |"); 
digitalWrite(relay2, HIGH);
}
else
{
lcd.print("R2: OFF |"); 
digitalWrite(relay2, LOW);
}
delay(2000);
}
