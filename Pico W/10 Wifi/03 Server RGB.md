## 1. `myPicoRGBserver.py`
save this file on picoW
![](../0_images/002/11.jpg)  

```python
import socket
from time import sleep
import time
import network
import machine
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C as myDisplay

# 1. Configuring RGB leds
redLedPin = 22
greenLedPin = 16
blueLedPin = 17

redLed = Pin(redLedPin, Pin.OUT)
greenLed = Pin(greenLedPin, Pin.OUT)
blueLed = Pin(blueLedPin, Pin.OUT)

# testing the flow so far
# redLed.value(0)
# greenLed.value(0)
# blueLed.value(0) 

# 2. Configuring Led Display
i2cBus = I2C(1, sda=Pin(2), scl=Pin(3), freq=400000)
display = myDisplay(128, 64, i2cBus)

# testing the flow so far
# display.text('Hello World', 0, 0)
# display.show()

# 3. Configuring Wifi
wifiName = 'CE5'
wifiPassword = '12345678'
wifi = network.WLAN(network.STA_IF)
sleep(0.5)
wifi.active(True)
sleep(0.5)
wifi.connect(wifiName, wifiPassword)
count = 0
while wifi.isconnected() == False:
    print('Waiting.....')
    display.text('.....waiting', 0, 0)
    display.text(str(count), 0, 16)
    display.show()
    sleep(1)
    count = count + 1
    display.fill(0)
display.fill(0)

wifiAddress = wifi.ifconfig()
usableAddress = wifiAddress[0]
print(usableAddress)
display.text('Connected', 0, 0)
display.text(usableAddress, 0, 16)
display.show()
```  
## 2. Save this second file at local Computer as `myClient.py`
```python
import socket as localSocket

serverIpAddress = '10.161.66.250' # found in first program terminal
serverListenerPort = 2222
serverConfig = (serverIpAddress, serverListenerPort)

bufferSize = 1024

UDPclient = localSocket.socket(localSocket.AF_INET, localSocket.SOCK_DGRAM)

while True:
    userInput = input('What is your color?: ')
    cmdEncoded = userInput.encode('utf-8')
    UDPclient.sendto(cmdEncoded, serverConfig)
```  

Note: to work this both local machine & pico w should be connected on same wifi network
<video src="../0_images/002/12.mp4" controls width="acutal"></video>
