```python
from machine import Pin
from time import sleep

# button pins numbers
btnNumRed = 15;
btnNumGreen = 14;
btnNumBlue = 13;

# led pins numbers
ledNumRed = 16;
ledNumGreen = 17;
ledNumBlue = 18;

# declare btns
btnRed = Pin(btnNumRed, Pin.IN, Pin.PULL_UP);
btnGreen = Pin(btnNumGreen, Pin.IN, Pin.PULL_UP);
btnBlue = Pin(btnNumBlue, Pin.IN, Pin.PULL_UP);

# declare leds
ledRed = Pin(ledNumRed, Pin.OUT);
ledGreen = Pin(ledNumGreen, Pin.OUT);
ledBlue = Pin(ledNumBlue, Pin.OUT);

while True:
    redBtnState = not btnRed.value()
    greenBtnState = not btnGreen.value()
    blueBtnState = not btnBlue.value()

    print(f"red: {redBtnState} || green: {greenBtnState} || blue: {blueBtnState}")

    ledRed.value(redBtnState)
    ledGreen.value(greenBtnState)
    ledBlue.value(blueBtnState)
    sleep(0.1)
```  
<video src="../0_images/001/17.mp4" controls width="640"></video>
![](../0_images/001/17.mp4)

