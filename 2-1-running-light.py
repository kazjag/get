import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds=[21, 20, 16, 12, 7, 8, 25, 24]
GPIO.setup(leds, GPIO.OUT)
count=0
while count<3:
    for i in leds:
        GPIO.output(i, 1)
        time.sleep(0.2)
        GPIO.output(i, 0)
    count+=1
GPIO.output(leds, 0)
GPIO.cleanup()