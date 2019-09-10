# This file is executed on every boot (including wake-boot from deepsleep)
# import esp
# esp.osdebug(None)
# import webrepl
# webrepl.start()

## Connects to wifi and sets time through NTP
import network
import time
import ntptime

# WiFi code
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('esp32_test', 'dannydannydanny')
while not sta_if.isconnected():
    pass

# Setting time to UTC
ntptime.settime()
