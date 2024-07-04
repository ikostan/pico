"""
Raspberry Pi Pico W LESSON 1: Write Your First Program for Absolute Beginners
https://www.youtube.com/watch?v=SL4_oU9t8Ss&list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5
"""

import time
from machine import Pin  # pylint: disable=import-error

LED: Pin = Pin(6, Pin.OUT)
IS_ON: int = 0


def check_toggle_val(val: int) -> (None, ValueError):
    """
    Valid val: 1, 0.
    Raises exception in case of invalid val.
    :param val:
    :return:
    """
    if val not in (0, 1):
        raise ValueError(f"Invalid parameter: {val}! Only 1 and 0 allowed.")


def toggle_is_on(val: int) -> (int, ValueError):
    """
    Convert 1 to 0 and vice versa.
    :param val:
    :return:
    """
    check_toggle_val(val)
    return 1 if val == 0 else 0


def toggle_led(val: int) -> (None, ValueError):
    """
    Toggle LED
    :param val:
    :return:
    """
    check_toggle_val(val)
    LED.value(val)


if __name__ == '__main__':
    while True:
        toggle_led(IS_ON)
        time.sleep(0.3)
        IS_ON = toggle_is_on(IS_ON)
