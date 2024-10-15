#include <Wire.h>  
#include <LiquidCrystal_I2C.h>    
LiquidCrystal_I2C lcd(0x27,16,2);
#include "DHT.h"  
int DHTPIN=2;//DIGITAL PIN D2  
#define DHTTYPE DHT11   
DHT dht(DHTPIN, DHTTYPE);
unsigned long previousMillis = 0;
const long reportInterval = 1000;
float temp, hum;
void setup()
{
    lcd.begin();
    lcd.backlight();
    dht.begin();delay(500);
}    
void loop()
{

  hum = dht.readHumidity();
  temp = dht.readTemperature();     
unsigned long currentMillis = millis();
 
if (currentMillis - previousMillis >= reportInterval) {
    previousMillis = currentMillis;
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Temp: ");lcd.print(temp);
    lcd.setCursor(0,1);
    lcd.print("Humi: ");lcd.print(hum);
  }
        
  delay(2000);


  
}

