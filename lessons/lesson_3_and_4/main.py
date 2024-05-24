"""
# Raspberry Pi Pico W LESSON 3: Understanding and Using Binary Numbers
# https://www.youtube.com/watch?v=C_xiDka0Nm0&list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5&index=3

# Raspberry Pi Pico W LESSON 4: Create a Binary Counter Using the Pico W
# https://www.youtube.com/watch?v=P1dzHNgAtvg&list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5&index=4
"""

import time
from machine import Pin  # pylint: disable=import-error


pin1 = Pin(13, Pin.OUT)
pin2 = Pin(12, Pin.OUT)
pin4 = Pin(11, Pin.OUT)
pin8 = Pin(10, Pin.OUT)
pins = [pin8, pin4, pin2, pin1]

numbers = {
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


def set_all_pins(all_pins, vals):
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
        for i in range(0, 16):
            n = numbers[i]
            set_all_pins(pins, n)
            print(f"number: {i}, pins: {n}")
            time.sleep(3)
