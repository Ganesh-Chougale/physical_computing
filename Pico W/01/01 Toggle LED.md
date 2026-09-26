right into thonny CLI  
```python
>>> import machine
>>> led = machine.Pin("LED", machine.Pin.OUT);
>>> led.on();
>>> led.off();
```  
in IDE
```python
from machine import Pin

myLed = Pin("LED", Pin.OUT)

myLed.value(1)
```  

`.on()` works same is `.value(1)`  
`.off()` works same is `.value(0)`