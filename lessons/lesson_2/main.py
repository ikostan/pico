
"""
Raspberry Pi Pico W LESSON 2: Understanding and Using Breadboards
https://www.youtube.com/watch?v=eGdrtikKc5U&list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5&index=2
"""
import time
from machine import Pin


led = Pin(15, Pin.OUT)

if __name__ == '__main__':

    while True:
        led.value(0)
        time.sleep(0.5)
        led.value(1)
        time.sleep(1)
