"""
Raspberry Pi Pico W LESSON 12: Understanding and Controlling an RGB LED in MicroPython
https://www.youtube.com/watch?v=yZkx-KWbATY&list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5&index=15
"""

from time import sleep
from machine import (Pin, PWM)


colors = {'red': (255,0,0),
          'green': (0,128,0),
          'blue': (0,0,255),
          'cyan': (0,255,255),
          'magenta': (255,0,255),
          'yellow': (255,255,0),
          'orange': (255,165,0),
          'white': (255,255,255)}

pins = {'RED': 13,
        'GREEN': 14,
        'BLUE': 15}

pwms = [PWM(Pin(pins['RED'])),
        PWM(Pin(pins['GREEN'])),
        PWM(Pin(pins['BLUE']))]


def calc_pwm(color_value):
    """
    Calculate PWM value
    """
    return (65550 * color_value) // 100


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


def led_on(led_color, val=65550):
    """
    Turn led on based on user choose
    """
    pwms_off()
    # noinspection PyTypeChecker
    for i, c in enumerate(colors[led_color]):
        pwms[i].duty_u16(calc_pwm(c))
       

def get_color():
    """
    Ask user to choose a color
    """
    while True:
        all_colors = '\n'.join(c for c in colors.keys())
        color = input(f"\nPlease enter color of your choice \
                      from the list below:\n\n{all_colors}\n\ntype here -> ").lower()
        
        if color == 'exit':
            return color
        
        if color in colors:
            return color
        
        print("\nPlease choose your color only from the listed options "
              "or type 'exit' to stop the execution.")
        sleep(2)


if __name__ == '__main__':

    initial_setup()

    while True:
        # noinspection PyTypeChecker
        color = get_color()
        if color == 'exit':
            print('\nThe program will stop the execution now...')
            break
        led_on(color)
