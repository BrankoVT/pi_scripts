import time
import wiringpi
import sys

def blink(_pin):
    wiringpi.digitalWrite(_pin, 1)
    time.sleep(0.5)
    wiringpi.digitalWrite(_pin, 0)
    time.sleep(0.5)


#SETUP
print("Start blinking")
pin = 1
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin, 1)


#MAIN
while True:
    blink(pin)

