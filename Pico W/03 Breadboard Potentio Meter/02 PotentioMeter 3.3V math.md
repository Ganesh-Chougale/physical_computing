## 1. Get Min & max of rading
```python
import machine;
from time import sleep;

potentioMeterPinNum = 28; # pico pin slot: 3V3(OUT)

myPot = machine.ADC(potentioMeterPinNum)
# ADC: Analogue Digital Convertor

while True:
    potVal = myPot.read_u16()
    print(potVal)
    sleep(0.5)

```  
then get analogue min reading & max reading.  

```
current reading
min: 280
max: 65550
```
we only need 2 things.
1. max value of reading (`66550`)
2. max value of voltage we want to assign (V`3.3`)
- `voltage = (potVal / maxReading) * maxVoltage`  
- `voltage = (potVal / 65535) * 3.3`
```python
import machine
from time import sleep

potPin = 28
myPot = machine.ADC(potPin)

while True:
    potVal = myPot.read_u16()
    voltage = (potVal / 65535) * 3.3 # used the formula
    print(voltage)
    sleep(0.5)
```  
now play with analogue knob it will range to voltage from 0 to 3.3 v