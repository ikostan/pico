# Raspberry Pi Pico W LESSON 7: Controlling 3 LED with a Potentiometer in Micropython
# https://www.youtube.com/watch?v=YqvcSnGd_HQ&list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5&index=7

"""
In this introductory video, I will show you how to use If Statements and
conditionals in microPython to turn on and off three different LED. I will
start with simple examples, and then show how we can control the state of an
LED using If Statements. I will also show how to get input from the user in
micropython using a potentiometer and the analog read function. This class is
for absolute beginners, and I do not assume you already understand the material
I am presenting. My goal is not to 'Show Off', but to genuinely teach you how
you can do this type of work and projects on your own. I will show all work
step-by-step, with clear instructions.
Enjoy!
"""

from time import sleep
from machine import Pin, ADC  # pylint: disable=import-error


# Mapping pins by color/name
Pins = {
    'READ': 28,      # Potentiometer
    'GREEN': 10,     # Green LED
    'YELLOW': 11,    # Yellow LED
    'RED': 12,       # Red LED
}

# Mapping colors to potentiometer values
COLORS = {
    'GREEN': range(0, 80),
    'YELLOW': range(80, 95),
    'RED': range(95, 101),
}

# Set up pin for potentiometer
potentiometer = ADC(Pins['READ'])


def all_led_off():
    """
    Turns all leds off
    :return:
    """
    for color in COLORS.keys():
        pin = Pin(Pins[color], Pin.OUT)
        pin.value(0)


def value_to_color(v_value):
    """
    Mapping pin name/color by potentiometer number
    COLORS[color] => range of integers
    :param v_value:
    :return:
    """
    new_color = ''

    for color in COLORS.keys():
        if v_value in COLORS[color]:
            new_color = color
            break

    return new_color


def turn_led_on(color):
    """
    Turns LED on based on color/name
    :param color:
    :return:
    """
    pin = Pin(Pins[color], Pin.OUT)
    pin.value(1)


def converter(read_value):
    """
    Converts potentiometer value to integer between 0 and 100
    x min = 0, x max = 65535
    y min = 0, y max = 100
    :param read_value:
    :return:
    """
    slope = (100 - 0) / (65535 - 0)       # calculate slope
    return int(slope * (read_value - 0))  # calculate Y and converted to integer value


if __name__ == '__main__':
    # Main loop
    while True:
        all_led_off()                                # Turn off all LEDs
        v = potentiometer.read_u16()                 # Read potentiometer value -> v
        # Convert potentiometer value into integer between 0 and 100
        value = converter(v)
        led_color = value_to_color(value)            # Get color based on converted value
        turn_led_on(led_color)                       # Turn ON corresponding LED
        print(f'value: {value}, LED: {led_color}')   # DEBUG output
        sleep(0.25)                                  # Sleep 0.25 seconds
