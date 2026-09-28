```python
from machine import Pin;
from time import sleep;

redLed = Pin(13, Pin.OUT);
blueLed = Pin(14, Pin.OUT);
greenLed = Pin(15, Pin.OUT);

redLed.value(0);
blueLed.value(0);
greenLed.value(0);

potPin = 28
myPot = machine.ADC(potPin)

while True:
    potVal = myPot.read_u16()
    percentage = (potVal / 65535) * 100 # used the formula
    print(percentage)
    
    if(percentage < 79):
        #print(percentage +": Green")
        greenLed.value(1);
        blueLed.value(0);
        redLed.value(0);
    elif(percentage > 80 and percentage < 94):
        #print(percentage +": Blue")
        greenLed.value(0);
        blueLed.value(1);
        redLed.value(0);
    elif(percentage > 94):
        #print(percentage +": Red")
        greenLed.value(0);
        blueLed.value(0);
        redLed.value(1);
        
    sleep(0.5)
```  