import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
MOTOR1 = 24
MOTOR2 = 25
BUTTON1 = 18
BUTTON2 = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR1, GPIO.OUT)
GPIO.setup(MOTOR2, GPIO.OUT)
GPIO.setup(BUTTON1, GPIO.IN)
GPIO.setup(BUTTON2, GPIO.IN)

try:
    while True:
         button_state1 = GPIO.input(BUTTON1)
         button_state2 = GPIO.input(BUTTON2)
         
         if (button_state1 == True)and(button_state2 == False):
             GPIO.output(MOTOR1, GPIO.HIGH)
             GPIO.output(MOTOR2, GPIO.LOW)
             print('MOTOR FORWARD...')
             time.sleep(1)
         elif (button_state1 == False)and(button_state2 == True):
             GPIO.output(MOTOR1, GPIO.LOW)
             GPIO.output(MOTOR2, GPIO.HIGH)
             print('MOTOR REVERSE...')
             time.sleep(1)
         else:
             GPIO.output(MOTOR1, GPIO.LOW)
             GPIO.output(MOTOR2, GPIO.LOW)
             print('MOTOR STOP...')
             time.sleep(1)
         
                    
             
except:
    GPIO.cleanup()
