"""
Raspberry Pi Pico W LESSON 12: Understanding and Controlling an RGB LED in MicroPython
https://www.youtube.com/watch?v=yZkx-KWbATY&list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5&index=15
"""

from time import sleep
from machine import (Pin, PWM)

RED = 0
GREEN = 1
BLUE = 2

pins = (13, 14, 15)

pwms = [PWM(Pin(pins[RED])),
        PWM(Pin(pins[GREEN])),
        PWM(Pin(pins[BLUE]))]

def pwms_off():
    # noinspection PyTypeChecker
    for pwm in pwms:
        pwm.duty_u16(0)

def initial_setup(val=1000):
    # noinspection PyTypeChecker
    for pwm in pwms:
        pwm.freq(val)

def red_on(val=65550):
   pwms_off()
   pwms[RED].duty_u16(val)
   print('Red')

def green_on(val=65550):
   pwms_off()
   pwms[GREEN].duty_u16(val)
   print('Green')

def blue_on(val=65550):
   pwms_off()
   pwms[BLUE].duty_u16(val)
   print('Blue')


if __name__ == '__main__':

    initial_setup()
    
    while True:
        red_on()
        sleep(0.5)

        green_on()
        sleep(0.5)

        blue_on()
        sleep(0.5)
