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
        IS_ON = 0
        led.value(IS_ON)
        t = random.random()
        t = round(t, 2)
        print(f"sleep: {t}, LED: {IS_ON}.")
        time.sleep(t)
        IS_ON = 1
        led.value(IS_ON)
        print(f"sleep: {t}, LED: {IS_ON}.")
