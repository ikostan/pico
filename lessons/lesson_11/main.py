"""
Raspberry Pi Pico W LESSON 11: Controlling a Dimmable LED with a Potentiometer
https://www.youtube.com/watch?v=MCo5nXAKyUU&list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5&index=11
"""
from time import sleep
from machine import (PWM, Pin, ADC)


# Set up pin for potentiometer
potentiometer = ADC(28)

# Set up PWM
PIN_NUM = 16
analogOut = PWM(Pin(PIN_NUM))
analogOut.freq(1000)
analogOut.duty_u16(0)

steps = 50            # n of steps for max brightness
max_read_val = 65550  # max potentiometer value
constant = 1.248336   # (constant) ** steps = max_read_val

while True:
        
    read = potentiometer.read_u16()         # pylint: disable=E1111
    exp = (steps / max_read_val) * read
    brightness = round(constant ** exp)
    analogOut.duty_u16(brightness)
    print(f"read: {read}, exp: {exp}, brightness: {brightness}")
    sleep(0.1)
