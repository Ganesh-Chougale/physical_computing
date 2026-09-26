```python
import machine
import time


led = machine.Pin("LED", machine.Pin.OUT)

cycle = 10

while (cycle > 0):
    led.on()
    time.sleep(0.5)  
    led.off()
    time.sleep(0.5)  
    cycle -= 1 
```  
Save this into pico w as `Blink.py` & run