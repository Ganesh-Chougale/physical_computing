```python
from machine import Pin

myLed = Pin('LED', Pin.OUT);

while True:
    cmd = input("you want to turn LED on? ")
    if(cmd.lower() == 'yes' or cmd.lower() == 'y' or cmd == '1'):
        print(f"input: {cmd}")
        print("Turning led on")
        myLed.value(1)
    elif(cmd.lower() == 'no' or cmd.lower() == 'n' or cmd == '0'):
        print(f"input: {cmd}")
        print("Turning led off")
        myLed.value(0)
    else:
        print(f"input: {cmd}")
        print("invalid input")
```  