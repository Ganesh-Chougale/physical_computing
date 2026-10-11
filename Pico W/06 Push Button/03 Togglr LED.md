```python
from machine import Pin
from time import sleep

buttonPin = 15
myButton = Pin(buttonPin, Pin.IN, Pin.PULL_UP)
myLed = Pin(16, Pin.OUT)

ledState = False
lastButtonState = False

myLed.value(ledState)

while True:
    currentButtonState = not myButton.value()
    
    if currentButtonState and not lastButtonState:
        ledState = not ledState  
        myLed.value(ledState)    
        print(f"LED Toggled: {ledState}")
        sleep(0.05)              
        
    lastButtonState = currentButtonState
    
    sleep(0.01)
```  