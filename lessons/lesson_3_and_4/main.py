"""
# Raspberry Pi Pico W LESSON 3: Understanding and Using Binary Numbers
# https://www.youtube.com/watch?v=C_xiDka0Nm0&list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5&index=3

# Raspberry Pi Pico W LESSON 4: Create a Binary Counter Using the Pico W
# https://www.youtube.com/watch?v=P1dzHNgAtvg&list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5&index=4
"""

import time
from machine import Pin  # pylint: disable=import-error


PIN1 = Pin(13, Pin.OUT)
PIN2 = Pin(12, Pin.OUT)
PIN4 = Pin(11, Pin.OUT)
PIN8 = Pin(10, Pin.OUT)
PINS = [PIN8, PIN4, PIN2, PIN1]

NUMBERS = {
    0: (False, False, False, False),
    1: (False, False, False, True),
    2: (False, False, True, False),
    3: (False, False, True, True),
    4: (False, True, False, False),
    5: (False, True, False, True),
    6: (False, True, True, False),
    7: (False, True, True, True),
    8: (True, False, False, False),
    9: (True, False, False, True),
    10: (True, False, True, False),
    11: (True, False, True, True),
    12: (True, True, False, False),
    13: (True, True, False, True),
    14: (True, True, True, False),
    15: (True, True, True, True),
}


def get_val(n_val):
    """
    Convert TRUE to 1 and FALSE to 0
    :param n_val:
    :return:
    """
    return 1 if n_val is True else 0


def set_pin_val(pin, val):
    """
    Set Pin value -> ON/OFF
    :param pin:
    :param val:
    :return:
    """
    pin.value(val)


def set_all_pins(vals, all_pins=PINS):
    """
    Turn all pins OFF
    :param all_pins:
    :param vals:
    :return:
    """
    for index, v in enumerate(vals):
        val = get_val(v)
        pin = all_pins[index]
        set_pin_val(pin, val)


if __name__ == '__main__':

    while True:
        for i, item in enumerate(NUMBERS.items()):
            set_all_pins(NUMBERS[i])
            print(f"number: {i}, pins: {item}")
            time.sleep(3)
