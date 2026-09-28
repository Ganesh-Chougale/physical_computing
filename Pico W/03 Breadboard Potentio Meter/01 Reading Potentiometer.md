```python
import machine;
from time import sleep;

potentioMeterPinNum = 28; # pico pin slot: GP28 / ADC2

myPot = machine.ADC(potentioMeterPinNum)
# ADC: Analog-to-Digital Converter

while True:
    potentioMeterVal = myPot.read_u16()
    print(potentioMeterVal)
    sleep(0.5)

```  
- Potentio Meter wire mapping
```txt
        POT
       ┌───┐
3V3 ───┤ 1 │
       │   │
GP28 ──┤ 2 │  ← wiper/middle
       │   │
GND ───┤ 3 │
       └───┘
```  
##### Preview:  
![](../0_images/001/04.jpg)  
#### Output:  
```Terminal
304
288
288
288
288
```  
getting lowest reading because the knob is all down
##### Preview:  
![](../0_images/001/05.jpg)  
#### Output:  
```Terminal
65535
65535
65535
65535
```  
getting highest reading because the knob is all up

2 ^ 16 = `65536`  

