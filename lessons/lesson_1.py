# This is a sample Python script.
# Raspberry Pi Pico W LESSON 1: Write Your First Program for Absolute Beginners
# https://www.youtube.com/watch?v=SL4_oU9t8Ss&list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5

"""
In this introductory video, I will show you how to install micropython on the Raspberry Pi Pico W,
I will show you how to install Thonny, the IDE, on your PC.
Thonny will allow you to interact with the Pico W. Then in today's short introductory video,
you will write your first four programs, and will get a homework assignment. This class is  for
absolute beginners, and I do not assume you already understand the material I am presenting.
My goal is not to 'Show Off', but to genuinely teach you how you can do this type of work and projects on your own.
Enjoy!
"""

from machine import Pin
import time
import random

random.randrange(0,1)

led = Pin("LED", Pin.OUT)
val = 0

if __name__ == '__main__':
    while True:
        t = random.random()
        t = round(t, 2)
        led.value(val)
        time.sleep(t)
        val = 1 if val == 0 else 0
        print(f"sleep: {t}, LED:{'ON' if val == 1 else 'OFF'}")
