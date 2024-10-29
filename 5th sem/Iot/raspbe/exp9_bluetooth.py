import time
from serial import (
    Serial,
    PARITY_NONE,
    STOPBITS_ONE,
    EIGHTBITS,
)

ser = Serial(
    port="/dev/serial0",
    baudrate=9600,
    parity=PARITY_NONE,
    stopbits=STOPBITS_ONE,
    bytesize=EIGHTBITS,
    timeout=1,
)

while 1:
    ser.write("Hello from Raspberry Pi!\n".encode('utf-8'))
    line = ser.readline().decode('utf-8').rstrip()
    print(line)
    time.sleep(1)
    
    
  