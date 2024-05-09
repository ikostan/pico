# Raspberry Pi Pico W LESSON 5: Reading Analog Voltages Using a Potentiometer
# https://www.youtube.com/watch?v=ODWwErH_iGA&list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5&index=5

"""
In this introductory video, I will show how to read analog voltages using
the Raspberry Pi PIco W. Fortunately, this is much easier than on the
Raspberry PI, sine the Pico has a built in analog to digital converter.
I will show how to read voltages using a potentiometer. This class is  for absolute
beginners, and I do not assume you already understand the material I am presenting.
My goal is not to 'Show Off', but to genuinely teach you how you can do this type
of work and projects on your own. I will show all work step-by-step, with clear instructions.
Enjoy!
"""

from time import sleep
import machine  # pylint: disable=import-error


pin_read = machine.ADC(28)
# bit_to_volt_ratio = 19859.09  # 65,535 / 3.3

X_MIN = 96  # min readings
X_MAX = 65535

V_MAX = 3.3  # max voltage
V_MIN = 0.0

SLOPE = (V_MAX - V_MIN) / (X_MAX - X_MIN)


if __name__ == '__main__':

    while True:
        x = pin_read.read_u16()
        voltage = (SLOPE * x) - (SLOPE * X_MIN)
        print(f'voltage: {round(voltage, 2)}, x: {x}')
        sleep(0.3)
