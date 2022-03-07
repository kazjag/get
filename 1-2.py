import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.IN)
for i in range(10000):
    GPIO.output(17, 1)
    GPIO.output(17, 0)