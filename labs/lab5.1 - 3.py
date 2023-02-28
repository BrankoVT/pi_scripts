import time
import wiringpi
import sys

def blink(_pin):
    wiringpi.digitalWrite(_pin, 1)
    time.sleep(0.1)
    wiringpi.digitalWrite(_pin, 0)


#SETUP
print("Start blinking")
pin = 3
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin, 1)


#MAIN
while True:
    blink(0)
    blink(1)
    blink(2)
    blink(3)

