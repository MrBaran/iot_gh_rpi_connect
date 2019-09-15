''' IoT Greenhouse - LED Blinky Example
    GPIO LED Control code for Connecting the Raspberry Pi workshop

    Keith E. Kelly
    K2 Creatives, LLC
    9/15/19
'''
from time import sleep
import RPi.GPIO as GPIO

print("IoT Greenhouse - Introduction to GPIO.")
print("Blink an LED")
print()

# Use board pin numbers
GPIO.setmode(GPIO.BOARD)
# Set pin 3 as LED output
GPIO.setup(3, GPIO.OUT)

for i in range(0, 50):
    GPIO.output(3,True)
    sleep(1)
    GPIO.output(3,False)
    sleep(1)

GPIO.cleanup()