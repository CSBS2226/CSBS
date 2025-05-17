import RPi.GPIO as GPIO 
import pyrebase 
from time import sleep
import Adafruit_DHT
import time
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
config = {     
  "apiKey": "AIzaSyCSoqWpwTjkQXhutegwO3nUvFrpA3htREI",
    "authDomain": "pk24-d7f90.firebaseapp.com",
    "databaseURL": "https://pk24-d7f90-default-rtdb.asia-southeast1.firebasedatabase.app",
    "storageBucket": "pk24-d7f90.appspot.com",
}

firebase = pyrebase.initialize_app(config)

LED22 = 23         # Terminal by number, el 22 es el GPIO25.
PushButton18 = 18  # Terminal by number, el 18 es el GPIO24.
sensor=0                  # El otro terminal a GND.

GPIO.setmode(GPIO.BCM)   # Terminal by number.
GPIO.setwarnings(False)
GPIO.setup(LED22,GPIO.OUT)
GPIO.setup(PushButton18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
                                                            
print("Inicio. (CTRL + C para salir.")

try:
    while True:      # Bucle principal

        database = firebase.database()
        ProjectBucket = database.child("PK24")                          
        LEDDATA = ProjectBucket.child("LED").get().val()
        sensor=sensor+1
        sensor=sensor/3
        ProjectBucket.child("PK24").child("Sensor").set(sensor)
        print(LEDDATA)
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
        
        if humidity is not None and temperature is not None:
            print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
            ProjectBucket.child("Weather").child("Humidity").set(humidity)
            ProjectBucket.child("Weather").child("Temperature").set(temperature)
        else:
            print("DATA READING....");
            time.sleep(1);                                                             
        if str(LEDDATA) == "1":
            print("LED22 now is ON.")
            GPIO.output(LED22, GPIO.HIGH)
        else:
            print("LED22 now is ON.")
            GPIO.output(LED22, GPIO.LOW)
            
        if GPIO.input(PushButton18) == GPIO.LOW  :
            print("PushButton not pressed.")
            ProjectBucket.child("PK24").child("PushButton").set("no_pressed.")
        else:
            print("PushButton pressed.")
            ProjectBucket.child("PK24").child("PushButton").set("PRESSED.")
       
except KeyboardInterrupt:    
     GPIO.cleanup()            


