"""
Raspberry Pi Pico W LESSON 12: Understanding and Controlling an RGB LED in MicroPython
https://www.youtube.com/watch?v=yZkx-KWbATY&list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5&index=15
"""

from time import sleep
from machine import (Pin, PWM)  # pylint: disable=import-error

colors: dict = {'red': (255, 0, 0),
                'green': (0, 128, 0),
                'blue': (0, 0, 255),
                'cyan': (0, 255, 255),
                'magenta': (255, 0, 255),
                'yellow': (255, 255, 0),
                'orange': (255, 165, 0),
                'white': (255, 255, 255)}

pins: dict = {'RED': 13,
              'GREEN': 14,
              'BLUE': 15}

pwms: tuple = (PWM(Pin(pins['RED'])),
               PWM(Pin(pins['GREEN'])),
               PWM(Pin(pins['BLUE'])))


def calc_pwm(color_value) -> int:
    """
    Calculate PWM value
    :param color_value:
    :return:
    """
    return int(color_value * (65550 / 255))


def pwms_off() -> None:
    """
    Turn all colors off
    :return:
    """
    # noinspection PyTypeChecker
    for pwm in pwms:
        pwm.duty_u16(0)


def initial_setup(val=1000) -> None:
    """
    Initial frequency setup
    :param val:
    :return:
    """
    # noinspection PyTypeChecker
    for pwm in pwms:
        pwm.freq(val)


def led_on(led_color: str) -> None:
    """
    Turn led on based on user choose
    :param led_color:
    :return:
    """
    rgb: list = [0, 0, 0]
    # noinspection PyTypeChecker
    for i, c in enumerate(colors[led_color]):
        x: int = calc_pwm(c)
        pwms[i].duty_u16(x)
        rgb[i] = x

    print(f"\nDEBUG -> R: {rgb[0]}, G: {rgb[1]}, B: {rgb[2]}\n")


def get_color() -> str:
    """
    Ask user to choose a color
    :return:
    """
    while True:
        # noinspection PyTypeChecker
        all_colors = '\n'.join(c for c in colors)
        rgb_color = input("\nPlease enter color of your choice "
                          f"from the list below:\n\n{all_colors}\n\ntype here -> ").lower()

        if rgb_color == 'exit':
            return rgb_color

        if rgb_color in colors:
            return rgb_color

        print("\nPlease choose your color only from the listed options "
              "or type 'exit' to stop the execution.")
        sleep(2)


if __name__ == '__main__':

    initial_setup()

    while True:
        # noinspection PyTypeChecker
        color: str = get_color()
        if color == 'exit':
            print('\nThe program will stop the execution now...')
            break
        pwms_off()
        led_on(color)
