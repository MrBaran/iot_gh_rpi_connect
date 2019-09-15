''' IoT Greenhouse - GHS Fan Control
    GHS Fan Control code for Connecting the Raspberry Pi workshop

    Keith E. Kelly
    K2 Creatives, LLC
    9/15/19
'''
from time import sleep
from iot_gh.IoTGreenhouseService import IoTGreenhouseService

ghs = IoTGreenhouseService()

print("IoT Greenhouse - Introduction to GPIO.")
print("Control fan using IoT Greenhouse Service code")
print()

while True:
    #switch_state = ghs.switches.toggle.get_state()
    #print("state =", switch_state)
    switch_status = ghs.switches.toggle.get_status()
    print("status =", switch_status)
    if ghs.switches.toggle.is_on():
        ghs.fan.on()
    else:
        ghs.fan.off()
    sleep(.5)
