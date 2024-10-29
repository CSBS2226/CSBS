import lcddriver
from time import *
lcd = lcddriver.lcd()
import busio
import RPi.GPIO as GPIO 
import pyrebase 
from time import sleep
import time
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D8)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
MOISTURE = AnalogIn(mcp, MCP.P0)

config = {     
  "apiKey": "wgsNjBl7qvzVY0KiezCBplSlRxLI9OiPwEschMfh",
  "authDomain": "rasptest-2fdb7.firebaseapp.com",
  "databaseURL": "https://rasptest-2fdb7-default-rtdb.firebaseio.com/",
  "storageBucket": "rasptest123"
}

firebase = pyrebase.initialize_app(config)

pump = 18         # Terminal by number, el 22 es el GPIO25.
                 # El otro terminal a GND.

GPIO.setmode(GPIO.BCM)   # Terminal by number.
GPIO.setwarnings(False)
GPIO.setup(pump,GPIO.OUT)

                                                            

try:
    while True:      # Bucle principal

        database = firebase.database()
        print('MOISTUR_VALUE: ', MOISTURE.value)
        print('MOISTUR_VOLT: ' + str(MOISTURE.voltage) + 'V')
        time.sleep(0.5)
        lcd.lcd_clear()
        lcd.lcd_display_string("MOI_ADC: %d" % (MOISTURE.value), 1)
        lcd.lcd_display_string("MOI_VOL: %f V" % (MOISTURE.voltage), 2)
        time.sleep(2)
        ProjectBucket = database.child("IOTLAB")                          
        ProjectBucket.child("IOTLAB").child("MOIS_ADC").set(MOISTURE.value)
        ProjectBucket.child("IOTLAB").child("MOIS_VLT").set(MOISTURE.voltage)
        time.sleep(0.5);                                                             
                   
        if MOISTURE.voltage >=1.5  :
            print("Moisture High... Pump Off...")
            ProjectBucket.child("IOTLAB").child("Pump:").set("OFF")
            GPIO.output(pump, GPIO.LOW)
        else:
           print("Moisture Low... Pump On...")
           ProjectBucket.child("IOTLAB").child("Pump:").set("On")
           GPIO.output(pump, GPIO.HIGH)
        time.sleep(0.5); 
except KeyboardInterrupt:    
     GPIO.cleanup()            


