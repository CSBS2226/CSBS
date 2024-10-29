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
channel1 = AnalogIn(mcp, MCP.P0)
channel2 = AnalogIn(mcp, MCP.P1)

while True:
    print('Raw ADC Value1: ', channel1.value)
    print('ADC Voltage1: ' + str(channel1.voltage) + 'V')
    time.sleep(1)
    print('Raw ADC Value2: ', channel2.value)
    print('ADC Voltage2: ' + str(channel2.voltage) + 'V')
    time.sleep(1)