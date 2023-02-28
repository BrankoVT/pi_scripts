import time
import wiringpi
import sys


def sMorse(_pin):
    for i in range(0,3):
        wiringpi.digitalWrite(_pin, 1)
        time.sleep(0.1)
        wiringpi.digitalWrite(_pin, 0)
        time.sleep(0.1)


def oMorse(_pin):
    for i in range(0,3):
        wiringpi.digitalWrite(_pin, 1)
        time.sleep(0.2)
        wiringpi.digitalWrite(_pin, 0)
        time.sleep(0.2)


def blink(_pin):
    sMorse(_pin)
    time.sleep(0.3)
    oMorse(_pin)
    time.sleep(0.2)
    sMorse(_pin)
    time.sleep(0.5)



#SETUP
print("Start blinking")
pin = 1
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin, 1)


#MAIN
while True:
    blink(pin)

