"""
Raspberry Pi Pico W LESSON 1: Write Your First Program for Absolute Beginners
https://www.youtube.com/watch?v=SL4_oU9t8Ss&list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5
"""

import time
from machine import Pin  # pylint: disable=import-error


LED = Pin(6, Pin.OUT)
is_on = 0


def toggle_led(val) -> None:
    """
    Toggle LED
    """
    LED.value(val)


if __name__ == '__main__':
    while True:
        toggle_led(is_on)
        time.sleep(0.3)
        IS_ON = 1 if IS_ON == 0 else 0
