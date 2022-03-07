import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

dac=[26, 19, 13, 6, 5, 11, 9, 10]
#number=[1,1,1,1,1,1,1,1] #255
#number=[0,1,1,1,1,1,1,1] #127
#number=[0,1,0,0,0,0,0,0] #64
#number=[0,0,1,0,0,0,0,0] #32
#number=[0,0,0,0,0,1,0,1] #5
#number=[0,0,0,0,0,0,0,0] #0
number=[0,0,0,0,0,0,1,0]
GPIO.setup(dac, GPIO.OUT)
GPIO.output(dac, number)
time.sleep(10)
GPIO.output(dac, 0)
GPIO.cleanup()