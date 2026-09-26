## 1. Base Version
```python
import network

wlan=network.WLAN(network.STA_IF)
wlan.active(True)
# wlan.connect("WIFI_NAME", "PASSWORD")
wlan.connect("CE5", "12345678")

print(wlan.isconnected())
```  
save this `check_connection.py` & run

#### Output:  
```Terminal
>>> %Run -c $EDITOR_CONTENT

MPY: soft reboot
True
>>> 
```  

## 2. Advance Version
```python
import network
import time

# Set up the Wi-Fi interface as a station (client)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Initiate the connection
wlan.connect("CE5", "12345678")

print("Connecting to Wi-Fi...")

# Wait for the connection to establish
while not wlan.isconnected() and wlan.status() >= 0:
    print(".")
    time.sleep(1)

# Check if connected and print the IP address
if wlan.isconnected():
    print("Connected successfully!")
    print("Your Pico's IP Address is:", wlan.ifconfig()[0])
else:
    print("Failed to connect.")
```  

#### Output:  
```Terminal
>>> %Run -c $EDITOR_CONTENT

MPY: soft reboot
Connecting to Wi-Fi...
Connected successfully!
Your Pico's IP Address is: 192.168.138.107
```  

