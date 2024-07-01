"""
Raspberry Pi Pico W LESSON 13: User Specified RGB LED Colors Using Micropython
https://www.youtube.com/watch?v=FLMPjwXqXVw&list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5&index=14
"""

from time import sleep
from machine import (PWM, Pin, ADC)


pot_red = ADC(26)
pot_green = ADC(27)
pot_blue = ADC(28)

led_red = PWM(Pin(13))
led_red.freq(1000)
led_red.duty_u16(0)

led_green = PWM(Pin(14))
led_green.freq(1000)
led_green.duty_u16(0)                                                 

led_blue = PWM(Pin(15))
led_blue.freq(1000)
led_blue.duty_u16(0)


while True:
    READ_R = pot_red.read_u16()
    READ_G = pot_green.read_u16()
    READ_B = pot_blue.read_u16()

    led_red.duty_u16(READ_R)
    led_green.duty_u16(READ_G)
    led_blue.duty_u16(READ_B)

    print(f"R: {READ_R}, G: {READ_G}, B: {READ_B}")

    sleep(0.3)
