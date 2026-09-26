```python
from machine import Pin;
from time import sleep as s;

redLED = Pin(15, Pin.OUT);

while True:
    redLED.value(0);
    s(0.2);
    redLED.value(1);
    s(0.2);
```  