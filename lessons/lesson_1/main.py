
"""
Raspberry Pi Pico W LESSON 1: Write Your First Program for Absolute Beginners
https://www.youtube.com/watch?v=SL4_oU9t8Ss&list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5
"""

import time
from machine import Pin  # pylint: disable=import-error


LED = Pin(6, Pin.OUT)
# fmt: off
# Black will not reformat lines that contain fmt: skip or blocks that start with 
IS_ON = 0
# fmt: on


def toggle_is_on(val: int) -> int:
    """
    Update IS_ON value
    """
    return 1 if val == 0 else 0


def toggle_led(val: int) -> None:

    """
    Toggle LED
    """
    LED.value(val)


if __name__ == '__main__':
    while True:
        toggle_led(IS_ON)
        time.sleep(0.3)
        # fmt: off
        IS_ON = toggle_is_on(IS_ON)
