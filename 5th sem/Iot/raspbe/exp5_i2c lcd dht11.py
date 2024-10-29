import lcddriver
from time import *
lcd = lcddriver.lcd()
import Adafruit_DHT
import time
 
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
lcd.lcd_display_string("OM TECHNOCRAFTS", 1)
lcd.lcd_display_string("  CORPORATION", 2)
sleep(1)
        
 
while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
        lcd.lcd_clear()
        lcd.lcd_display_string("Temp: %d%s C" % (temperature, chr(223)), 1)
        lcd.lcd_display_string("Humidity: %d %%" % humidity, 2)
    else:
        print("DATA READING....");
        lcd.lcd_clear()
        lcd.lcd_display_string("DATA READING...",1)
        lcd.lcd_display_string("    ****" , 2)
    time.sleep(3);