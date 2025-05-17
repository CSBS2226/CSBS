import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
LED_PIN1 = 18
LED_PIN2 = 23
LED_PIN3 = 24
LED_PIN4 = 25 
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)
GPIO.setup(LED_PIN3, GPIO.OUT)
GPIO.setup(LED_PIN4, GPIO.OUT)

while True:
    GPIO.output(LED_PIN1, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED_PIN2, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED_PIN3, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED_PIN4, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED_PIN4, GPIO.LOW)
    time.sleep(1)
    GPIO.output(LED_PIN3, GPIO.LOW)
    time.sleep(1)
    GPIO.output(LED_PIN2, GPIO.LOW)
    time.sleep(1)
    GPIO.output(LED_PIN1, GPIO.LOW)
    time.sleep(1)

GPIO.cleanup()
