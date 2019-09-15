''' IoT Greenhouse - Introduction to Webservices
    Introduction to Webservices activity for Connecting the Raspberry Pi workshop

    Keith E. Kelly
    K2 Creatives, LLC
    9/15/19
'''
from time import sleep
from iot_gh.IoTGreenhouseService import IoTGreenhouseService
from iot_gh.GHTextingService import GHTextingService

print("\nGroupMe SMS Texting for IoT Greenhouse.\n")
print("\nOpen your dev.groupme.com page. Access your token and copy here.")
token = (input("GroupMe token: ")).strip()
print()

last_message_id = None

ghs = IoTGreenhouseService()
ts = GHTextingService(token, ghs)

while True:
    message = ts.last_message
    if message.id != last_message_id:
        print(message.name + "   " + message.text)
        print()

        last_message_id = message.id
    sleep(.5)
