import time
import wiringpi

#SETUP
print("Start")
pinCap = 2
startTime = 0
stopTime = 0
totalTime = 0
wiringpi.wiringPiSetup() 

#infinite loop - stop using CTRL-C
while True:
    wiringpi.pinMode(pinCap, 1) # Set pin to mode 1 ( OUTPUT )
    time.sleep(0.5)

    wiringpi.pinMode(pinCap, 0) # Set pin to mode 0 ( INPUT )
    startTime = time.time()
    while wiringpi.digitalRead(pinCap) == 0:
        True

    stopTime = time.time()
    totalTime = stopTime - startTime
    print(totalTime)
