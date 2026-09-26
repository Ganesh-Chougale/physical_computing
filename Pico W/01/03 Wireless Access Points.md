```python
import network

wlan=network.WLAN(network.STA_IF)
wlan.active(True)
accesspoints = wlan.scan()

for ap in accesspoints:
    print(ap)
```  
save as `wireless_access_points.py` & then run

#### Output:  
```Terminal
>>> %Run -c $EDITOR_CONTENT

MPY: soft reboot
(b'JioPrivateNet', b'\x00\x06\xae\xec\x7f\x9a', 11, -85, 5, 3)
(b'Jio network Sumit', b'\xfe\xbfwE\x8a~', 11, -55, 5, 3)
(b'Jio Network Sumit', b'4\n3s\x10f', 11, -91, 5, 1)
```  