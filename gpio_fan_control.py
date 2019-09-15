''' IoT Greenhouse - GPIO Fan Control
    GPIO activity for Connecting the Raspberry Pi workshop

    Keith E. Kelly
    K2 Creatives, LLC
    9/15/19
'''
from time import sleep
import RPi.GPIO as GPIO

print("IoT Greenhouse - Introduction to GPIO.")
print("Control fan using GPIO code")
print()

# Use board pin numbers
GPIO.setmode(GPIO.BOARD)
# Set pin 13 as toggle switch input
GPIO.setup(13, GPIO.IN)
# Set pin 15 as fan output
GPIO.setup(15, GPIO.OUT)

while True:
    switch_state = GPIO.input(13)  #get switch state
    print(switch_state)
    if switch_state == False:
        GPIO.output(15, True)   #Toggle is on, turn fan on
    else:
        GPIO.output(15, False)   #Toggle is off, turn fan off
    sleep(.5)
    
