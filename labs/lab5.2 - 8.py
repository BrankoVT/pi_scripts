import time
import wiringpi

#SETUP
print("Start Setup")
delay = 10
d = delay/1000
blue = 3
pink = 4
yellow = 6
orange = 9
wiringpi.wiringPiSetup()
wiringpi.pinMode(blue, 1)
wiringpi.pinMode(pink, 1)
wiringpi.pinMode(yellow, 1)
wiringpi.pinMode(orange, 1)

#MAIN
while True:
    #STEP 0
    print("Step 0")
    wiringpi.digitalWrite(blue, 1)
    wiringpi.digitalWrite(pink, 1)
    wiringpi.digitalWrite(yellow, 0)
    wiringpi.digitalWrite(orange, 0)
    time.sleep(d)

    #STEP 1
    print("Step 1")
    wiringpi.digitalWrite(blue, 0)
    wiringpi.digitalWrite(pink, 1)
    wiringpi.digitalWrite(yellow, 1)
    wiringpi.digitalWrite(orange, 0)
    time.sleep(d)

    #STEP 2
    print("Step 2")
    wiringpi.digitalWrite(blue, 0)
    wiringpi.digitalWrite(pink, 0)
    wiringpi.digitalWrite(yellow, 1)
    wiringpi.digitalWrite(orange, 1)
    time.sleep(d)

    #STEP 3
    print("Step 3")
    wiringpi.digitalWrite(blue, 1)
    wiringpi.digitalWrite(pink, 0)
    wiringpi.digitalWrite(yellow, 0)
    wiringpi.digitalWrite(orange, 1)
    time.sleep(d)
