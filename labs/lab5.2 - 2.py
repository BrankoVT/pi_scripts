import time
import wiringpi


#SETUP
print("Start blinking")
switch = 2
led = 1
wiringpi.wiringPiSetup()
wiringpi.pinMode(led, 1)
wiringpi.pinMode(switch, 0)


#MAIN
while True:
    if wiringpi.digitalRead(switch) == 0:
        print("LED is not Flashing")
        time.sleep(1)

    else:
        print("LED Blinks")
        wiringpi.digitalWrite(led, 1)
        time.sleep(0.5)
        wiringpi.digitalWrite(led, 0)
        time.sleep(0.5)
