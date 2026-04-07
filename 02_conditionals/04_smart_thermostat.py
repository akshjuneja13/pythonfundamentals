# Building a Smart Thermostat Alert System

device_status = input("Enter device status (active/offline): ")

if device_status == "active":
    temperature = float(input("Enter temperature: "))

    if temperature > 35:
        print("High temperature! Turn on AC")
    else:
        print("Temperature is normal")
else:
    print("Device is offline")