"""
Raspberry Pi Pico W LESSON 1: Write Your First Program for Absolute Beginners
https://www.youtube.com/watch?v=SL4_oU9t8Ss&list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5
"""

import time
import random
from machine import Pin


random.randrange(0, 1)
led = Pin(6, Pin.OUT)

if __name__ == '__main__':
    while True:
        is_on = 1
        led.value(is_on)
        t = random.random()
        t = round(t, 2)
        print(f"sleep: {t}, LED: {is_on}.")
        time.sleep(t)
        is_on = 0
        led.value(is_on)
        print(f"sleep: {t}, LED: {is_on}.")

