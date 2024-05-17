"""
Raspberry Pi Pico W LESSON 1: Write Your First Program for Absolute Beginners
https://www.youtube.com/watch?v=SL4_oU9t8Ss&list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5
"""

import time
import random
from machine import Pin


random.randrange(0, 1)

led = Pin("LED", Pin.OUT)
PIN_VALUE = 0

if __name__ == '__main__':
    while True:
        t = random.random()
        t = round(t, 2)
        led.value(PIN_VALUE)
        time.sleep(t)
        PIN_VALUE = 1 if PIN_VALUE == 0 else 0
        print(f"sleep: {t}, LED:{'ON' if PIN_VALUE == 1 else 'OFF'}")
