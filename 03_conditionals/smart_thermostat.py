# You're building a smart thermostat aler system:
# if the device status is "active"
# And temperature > 35 -> Warn: "High temperature alert"
# Else temperature normal
# if device is off -> device is offline

device_status = 'active'
temperature = 33

if device_status == 'active':
    if temperature > 35:
        print("High temperature alert!")
    else: 
        print("Temperature is normal")
else: 
    print(f"Device is offline")