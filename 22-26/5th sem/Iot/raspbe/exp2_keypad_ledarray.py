import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
LED_PIN1 = 18
LED_PIN2 = 23
LED_PIN3 = 24
LED_PIN4 = 25
BUTTON1 = 8
BUTTON2= 7
BUTTON3 = 1
BUTTON4 = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)
GPIO.setup(LED_PIN3, GPIO.OUT)
GPIO.setup(LED_PIN4, GPIO.OUT)
GPIO.setup(BUTTON1, GPIO.IN)
GPIO.setup(BUTTON2, GPIO.IN)
GPIO.setup(BUTTON3, GPIO.IN)
GPIO.setup(BUTTON4, GPIO.IN)

try:
    while True:
         button_state1 = GPIO.input(BUTTON1)
         button_state2 = GPIO.input(BUTTON2)
         button_state3 = GPIO.input(BUTTON3)
         button_state4 = GPIO.input(BUTTON4)
         if button_state1 == True:
             GPIO.output(LED_PIN1, GPIO.HIGH)
             print('Button1 Pressed...')
             time.sleep(1)
         else:
             GPIO.output(LED_PIN1, GPIO.LOW)
         
        
         if button_state2 == True:
             GPIO.output(LED_PIN2, GPIO.HIGH)
             print('Button2 Pressed...')
             time.sleep(1)
         else:
             GPIO.output(LED_PIN2, GPIO.LOW)
          
         if button_state3 == True:
             GPIO.output(LED_PIN3, GPIO.HIGH)
             print('Button3 Pressed...')
             time.sleep(1)
         else:
             GPIO.output(LED_PIN3, GPIO.LOW)
          
         if button_state4 == True:
             GPIO.output(LED_PIN4, GPIO.HIGH)
             print('Button4 Pressed...')
             time.sleep(1)
         else:
             GPIO.output(LED_PIN4, GPIO.LOW)
             
             
except:
    GPIO.cleanup()