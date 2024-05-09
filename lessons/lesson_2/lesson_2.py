# Raspberry Pi Pico W LESSON 2: Understanding and Using Breadboards
# https://www.youtube.com/watch?v=eGdrtikKc5U&list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5&index=2

"""
In this introductory video, I will show you how to build your first circuit using the breadboard,
and connecting it to the Pico W. We will blink an external LED from the Pico W. My goal is not to
'Show Off', but to genuinely teach you how you can do this type of work and projects on your own.
Enjoy!
"""
import time
from machine import Pin  # pylint: disable=import-error


led = Pin(15, Pin.OUT)

if __name__ == '__main__':

    while True:
        led.value(0)
        time.sleep(0.5)
        led.value(1)
        time.sleep(1)
