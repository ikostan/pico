from machine import Pin
import time

pin1 = Pin(13, Pin.OUT)
pin2 = Pin(12, Pin.OUT)
pin4 = Pin(11, Pin.OUT)
pin8 = Pin(10, Pin.OUT)
pins = [pin8, pin4, pin2, pin1]
# binary = [8, 4, 2, 1]  # binary values

numbers = {
    0: [False, False, False, False],
    1: [False, False, False, True],
    2: [False, False, True, False],
    3: [False, False, True, True],
    4: [False, True, False, False],
    5: [False, True, False, True],
    6: [False, True, True, False],
    7: [False, True, True, True],
    8: [True, False, False, False],
    9: [True, False, False, True],
    10: [True, False, True, False],
    11: [True, False, True, True],
    12: [True, True, False, False],
    13: [True, True, False, True],
    14: [True, True, True, False],
    15: [True, True, True, True],
}


def get_val(n):
    return 1 if n is True else 0


def set_pin_val(pin, val):
    pin.value(val)


def set_all_pins(all_pins, vals):
    for i, v in enumerate(vals):
        val = get_val(v)
        pin = all_pins[i]
        set_pin_val(pin, val)


if __name__ == '__main__':

    while True:
        for i in range(0, 16):
            n = numbers[i]
            set_all_pins(pins, n)
            print(f"number: {i}, pins: {n}")
            time.sleep(3)
