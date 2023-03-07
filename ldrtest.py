import time
import wiringpi
import sys
#SETUP
print("Start")
pinLed = 2
pinSwitch = 1
wiringpi.wiringPiSetup() 
wiringpi.pinMode(pinLed, 1)            # Set pin to mode 1 ( OUTPUT )
wiringpi.pinMode(pinSwitch, 0)         # Set pin to mode 0 ( INPUT )
#infinite loop - stop using CTRL-C
while True:
    if(wiringpi.digitalRead(pinSwitch) == 0): #input is active low
        print("Dark")
        time.sleep(0.5) #anti bouncing
    else:
        print("Light")
        time.sleep(0.5) #anti bouncing
