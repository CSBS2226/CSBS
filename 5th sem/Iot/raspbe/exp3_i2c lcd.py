import lcddriver
from time import *

lcd = lcddriver.lcd()

try:
    while True:
        lcd.lcd_display_string("OM TECHNOCRAFTS", 1)
        lcd.lcd_display_string("  CORPORATION", 2)
        sleep(1)
        lcd.lcd_clear()
        sleep(1)

             
             
except:






