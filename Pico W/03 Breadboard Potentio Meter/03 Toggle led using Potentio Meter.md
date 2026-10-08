```python
from machine import Pin;
from time import sleep;

redLed = Pin(13, Pin.OUT);
blueLed = Pin(14, Pin.OUT);
greenLed = Pin(15, Pin.OUT);

redLed.value(0);
blueLed.value(0);
greenLed.value(0);

PotentioMeterPinNum = 28
myPotentioMeter = machine.ADC(PotentioMeterPinNum)

while True:
    potVal = myPotentioMeter.read_u16()
    percentage = (potVal / 65535) * 100 # used the formula
    print(percentage)
    
    if(percentage < 79):
        greenLed.value(1);
        blueLed.value(0);
        redLed.value(0);
    elif(percentage > 79 and percentage < 94):
        greenLed.value(0);
        blueLed.value(1);
        redLed.value(0);
    elif(percentage > 94):
        greenLed.value(0);
        blueLed.value(0);
        redLed.value(1);
        
    sleep(0.5)
```  