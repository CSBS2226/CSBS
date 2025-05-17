import lcddriver
from time import *
lcd = lcddriver.lcd()
import busio
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
POT1 = AnalogIn(mcp, MCP.P0)
POT2 = AnalogIn(mcp, MCP.P1)

while True:
    print('POT1_ADC VALUE: ', POT1.value)
    print('POT_1 VOLT: ' + str(POT1.voltage) + 'V')
    time.sleep(0.25)
    print('POT2_ADC VALUE: ', POT2.value)
    print('POT_2 VOLT: ' + str(POT2.voltage) + 'V')
    time.sleep(0.25)
    lcd.lcd_clear()
    lcd.lcd_display_string("P1_ADC: %d" % (POT1.value), 1)
    lcd.lcd_display_string("P1_VOLT: %f V" % (POT1.voltage), 2)
    time.sleep(2)
    lcd.lcd_clear()
    lcd.lcd_display_string("P2_ADC: %d" % (POT2.value), 1)
    lcd.lcd_display_string("P2_VOLT: %f V" % (POT2.voltage), 2)
    time.sleep(2)