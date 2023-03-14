import time
import wiringpi
import sys

def blink(_pin):
    wiringpi.digitalWrite(_pin, 1)
    time.sleep(0.1)
    wiringpi.digitalWrite(_pin, 0)


#SETUP
print("Start blinking")
switch = 5
switch2 = 6
wiringpi.wiringPiSetup()
wiringpi.pinMode(0, 1)
wiringpi.pinMode(1, 1)
wiringpi.pinMode(2, 1)
wiringpi.pinMode(3, 1)
wiringpi.pinMode(switch, 0)


#MAIN
while True:
    if wiringpi.digitalRead(switch) == 0:
        print("Relay 0")
        blink(1)

    if wiringpi.digitalRead(switch2) == 0:
        print("Relay 1")
        blink(2)
