"""
WOKWI testing library for Pi Pico W
"""

import time
from machine import Pin

time.sleep(0.25)  # Wait for USB to become ready
led = Pin(5, Pin.OUT)

while True:
    led.toggle()
    time.sleep(0.5)
    print("Hello, Pi Pico!")
