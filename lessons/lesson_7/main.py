"""
Raspberry Pi Pico W LESSON 7: Controlling 3 LED with a Potentiometer in Micropython
https://www.youtube.com/watch?v=YqvcSnGd_HQ&list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5&index=7
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
    for color in COLORS:
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

    for color, values in COLORS.items():
        if v_value in values:
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
        # Read potentiometer value -> v
        V = potentiometer.read_u16()                 # pylint: disable=E1111
        # Convert potentiometer value into integer between 0 and 100
        VALUE = converter(V)
        LED_COLOR = value_to_color(VALUE)            # Get color based on converted value
        turn_led_on(LED_COLOR)                       # Turn ON corresponding LED
        print(f'value: {VALUE}, LED: {LED_COLOR}')   # DEBUG output
        sleep(0.25)                                  # Sleep 0.25 seconds
