''' IoT Greenhouse - LED Control Example
    GPIO LED Control code for Connecting the Raspberry Pi workshop

    Keith E. Kelly
    K2 Creatives, LLC
    9/15/19
'''
from time import sleep
import RPi.GPIO as GPIO

print("IoT Greenhouse - Introduction to GPIO.")
print("Control LED with switch")
print()

# Use board pin numbers
GPIO.setmode(GPIO.BOARD)
# Set pin 37 as switch input
GPIO.setup(37, GPIO.IN)
# Set pin 3 as LED output
GPIO.setup(3, GPIO.OUT)

while True:
    switch_state = GPIO.input(37)  #get switch state
    print(switch_state)
    if switch_state == False:
        GPIO.output(3, False)   #Switch is on, turn LED on
    else:
        GPIO.output(3, True)    #Switch is off, turn LED off
    sleep(.5)
    
