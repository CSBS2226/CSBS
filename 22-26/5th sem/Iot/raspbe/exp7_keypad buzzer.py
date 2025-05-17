import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
BUZZER = 23
BUTTON1 = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)
GPIO.setup(BUTTON1, GPIO.IN)

try:
    while True:
         button_state1 = GPIO.input(BUTTON1)
         
         if button_state1 == True:
             GPIO.output(BUZZER, GPIO.HIGH)
             print('BUZZER ON...')
             time.sleep(1)
         else:
             GPIO.output(BUZZER, GPIO.LOW)
         
                    
             
except:
    GPIO.cleanup()