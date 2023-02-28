import time
import wiringpi
import sys

def blink():
    wiringpi.digitalWrite(0, 1)
    wiringpi.digitalWrite(1, 0)
    wiringpi.digitalWrite(2, 1)
    wiringpi.digitalWrite(3, 0)
    time.sleep(1)
    wiringpi.digitalWrite(0, 0)
    wiringpi.digitalWrite(1, 1)
    wiringpi.digitalWrite(2, 0)
    wiringpi.digitalWrite(3, 1)
    time.sleep(1)


#SETUP
print("Start blinking")
pin = 0
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin, 1)


#MAIN
while True:
    blink()

