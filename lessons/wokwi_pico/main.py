"""
WOKWI testing library for Pi Pico
"""

from time import sleep
from machine import Pin

sleep(0.25)
led = Pin(5, Pin.OUT)

while True:
    led.toggle()
    sleep(0.5)
    print("Hello, Pi Pico!")
