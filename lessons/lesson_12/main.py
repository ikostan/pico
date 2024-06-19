"""
Raspberry Pi Pico W LESSON 12: Understanding and Controlling an RGB LED in MicroPython
https://www.youtube.com/watch?v=yZkx-KWbATY&list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5&index=15
"""

from time import sleep
from machine import (Pin, PWM)

pins = {'RED': 13,
        'GREEN': 14,
        'BLUE': 15}

pwms = [PWM(Pin(pins['RED'])),
        PWM(Pin(pins['GREEN'])),
        PWM(Pin(pins['BLUE']))]


def pwms_off():
    """
    Turn all colors off
    """
    # noinspection PyTypeChecker
    for pwm in pwms:
        pwm.duty_u16(0)


def initial_setup(val=1000):
    """
    Initial frequency setup
    """
    # noinspection PyTypeChecker
    for pwm in pwms:
        pwm.freq(val)


def led_on(color, val=65550):
    """
    Turn led on
    """
    pwms_off()
    i = list(pins.keys()).index(color)
    pwms[i].duty_u16(val)
    print(f"i: {i}, color: {color}")


if __name__ == '__main__':

    initial_setup()

    while True:
        # noinspection PyTypeChecker
        for c in pins:
            led_on(c)
            sleep(0.5)
