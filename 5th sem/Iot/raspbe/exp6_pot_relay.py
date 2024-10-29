import RPi.GPIO as GPIO
GPIO.setwarnings(False)
import busio
import time
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
LED_PIN1 = 18
LED_PIN2 = 23
# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D8)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
POT1 = AnalogIn(mcp, MCP.P0)
POT2 = AnalogIn(mcp, MCP.P1)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)
try:
    while True:
        print('POT1_ADC VALUE: ', POT1.value)
        print('POT_1 VOLT: ' + str(POT1.voltage) + 'V')
        time.sleep(0.5)
        print('POT2_ADC VALUE: ', POT2.value)
        print('POT_2 VOLT: ' + str(POT2.voltage) + 'V')
        time.sleep(0.5)
        
        if POT1.voltage >= 2:
                 GPIO.output(LED_PIN1, GPIO.HIGH)
                 print('Relay_1 ON')
                 time.sleep(1)
        else:
                 GPIO.output(LED_PIN1, GPIO.LOW)
        
        if POT2.voltage >= 2:
                 GPIO.output(LED_PIN2, GPIO.HIGH)
                 print('Relay_2 ON')
                 time.sleep(1)
        else:
                 GPIO.output(LED_PIN2, GPIO.LOW)
except:
    
    GPIO.cleanup()