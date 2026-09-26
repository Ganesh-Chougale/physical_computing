```python
from machine import Pin
from time import sleep

l4 = Pin(12, Pin.OUT)
l3 = Pin(13, Pin.OUT)
l2 = Pin(14, Pin.OUT)
l1 = Pin(15, Pin.OUT)

while True:
    # Binary 0 (0000)
    l1.value(0); l2.value(0); l3.value(0); l4.value(0); sleep(2)
    
    # Binary 1 (0001)
    l1.value(0); l2.value(0); l3.value(0); l4.value(1); sleep(2)

    # Binary 2 (0010)
    l1.value(0); l2.value(0); l3.value(1); l4.value(0); sleep(2)    

    # Binary 3 (0011)
    l1.value(0); l2.value(0); l3.value(1); l4.value(1); sleep(2)  

    # Binary 4 (0100)
    l1.value(0); l2.value(1); l3.value(0); l4.value(0); sleep(2)  

    # Binary 5 (0101)
    l1.value(0); l2.value(1); l3.value(0); l4.value(1); sleep(2)  

    # Binary 6 (0110)
    l1.value(0); l2.value(1); l3.value(1); l4.value(0); sleep(2)  

    # Binary 7 (0111)
    l1.value(0); l2.value(1); l3.value(1); l4.value(1); sleep(2)  

    # Binary 8 (1000)
    l1.value(1); l2.value(0); l3.value(0); l4.value(0); sleep(2)  

    # Binary 9 (1001)
    l1.value(1); l2.value(0); l3.value(0); l4.value(1); sleep(2)  

    # Binary 10 (1010)
    l1.value(1); l2.value(0); l3.value(1); l4.value(0); sleep(2)  

    # Binary 11 (1011)
    l1.value(1); l2.value(0); l3.value(1); l4.value(1); sleep(2)  

    # Binary 12 (1100)
    l1.value(1); l2.value(1); l3.value(0); l4.value(0); sleep(2)  

    # Binary 13 (1101)
    l1.value(1); l2.value(1); l3.value(0); l4.value(1); sleep(2)  

    # Binary 14 (1110)
    l1.value(1); l2.value(1); l3.value(1); l4.value(0); sleep(2)  

    # Binary 15 (1111)
    l1.value(1); l2.value(1); l3.value(1); l4.value(1); sleep(2)  
```  