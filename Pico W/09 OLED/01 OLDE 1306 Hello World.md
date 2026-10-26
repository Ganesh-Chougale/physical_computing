##### Install micro python library:  
`Tools` => `Manage Packages` 
![](../0_images/002/04.png)  
![](../0_images/002/05.jpg)  
```python
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

myConfig = I2C(1, sda=Pin(2), scl=Pin(3), freq=400000)
display = SSD1306_I2C(128, 64, myConfig)
msg = 'Hello World!'
display.text(msg, 0, 0)
display.show()
```  
![](../0_images/002/06.jpg)  

useful methods
```python
# Invert color
display.invert(1)

# Draw Horizontal Line
display.hline(20,20,40,1)
# Draw Vertical Line
display.vline(20,20,40,1)
# Draw Random Line
display.line(20, 20, 118, 54, 1)

# Draw Rectangle
display.rect(45, 25, 30, 20, 1)
# Draw Filled Rectangle
display.fill_rect(45, 25, 30, 20, 1)
```  