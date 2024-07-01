"""
Raspberry Pi Pico W LESSON 7: Controlling 3 LED with a Potentiometer in Micropython
https://www.youtube.com/watch?v=YqvcSnGd_HQ&list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5&index=7

Raspberry Pi Pico W LESSON 8: Compound Conditionals and If Statements in MicroPython
https://www.youtube.com/watch?v=uTwm3ydI69w&list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5&index=8
"""
from time import sleep
from machine import Pin, ADC  # pylint: disable=import-error


# Mapping pins by color/name
Pins: dict = {
    'READ': 28,      # Potentiometer
    'GREEN': 10,     # Green LED
    'YELLOW': 11,    # Yellow LED
    'RED': 12,       # Red LED
}

# Mapping colors to potentiometer values
COLORS: dict = {
    'GREEN': range(0, 80),
    'YELLOW': range(80, 95),
    'RED': range(95, 101),
}

# Set up pin for potentiometer
potentiometer: ADC = ADC(Pins['READ'])


def all_led_off() -> None:
    """
    Turns all leds off
    :return:
    """
    for color in COLORS:
        pin = Pin(Pins[color], Pin.OUT)
        pin.value(0)


def value_to_color(v_value) -> str:
    """
    Mapping pin name/color by potentiometer number
    COLORS[color] => range of integers
    :param v_value:
    :return:
    """
    new_color: str = ''

    for color, values in COLORS.items():
        if v_value in values:
            new_color = color
            break

    return new_color


def turn_led_on(color) -> None:
    """
    Turns LED on based on color/name
    :param color:
    :return:
    """
    pin: Pin = Pin(Pins[color], Pin.OUT)
    pin.value(1)


def converter(read_value) -> int:
    """
    Converts potentiometer value to integer between 0 and 100
    x min = 0, x max = 65535
    y min = 0, y max = 100
    :param read_value:
    :return:
    """
    slope: float = (100 - 0) / (65535 - 0)  # calculate slope
    return int(slope * (read_value - 0))    # calculate Y and converted to integer value


if __name__ == '__main__':
    # Main loop
    while True:
        all_led_off()                                # Turn off all LEDs
        # Read potentiometer value -> v
        V: int = potentiometer.read_u16()            # pylint: disable=E1111
        # Convert potentiometer value into integer between 0 and 100
        VALUE: int = converter(V)
        LED_COLOR: str = value_to_color(VALUE)       # Get color based on converted value
        turn_led_on(LED_COLOR)                       # Turn ON corresponding LED
        print(f'value: {VALUE}, LED: {LED_COLOR}')   # DEBUG output
        sleep(0.25)                                  # Sleep 0.25 seconds
