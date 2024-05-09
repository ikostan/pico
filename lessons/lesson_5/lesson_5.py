# Raspberry Pi Pico W LESSON 5: Reading Analog Voltages Using a Potentiometer
# https://www.youtube.com/watch?v=ODWwErH_iGA&list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5&index=5

"""
In this introductory video, I will show how to read analog voltages using the Raspberry Pi PIco W.
Fortunately, this is much easier than on the Raspberry PI, sine the Pico has a built in analog to
digital converter. I will show how to read voltages using a potentiometer. This class is  for absolute
beginners, and I do not assume you already understand the material I am presenting. My goal is not to 'Show Off',
but to genuinely teach you how you can do this type of work and projects on your own. I will show all work
step-by-step, with clear instructions.
Enjoy!
"""

from time import sleep
import machine  # pylint: disable=import-error


pin_read = machine.ADC(28)
# bit_to_volt_ratio = 19859.09  # 65,535 / 3.3

x_min = 96  # min readings
x_max = 65535

min_read = x_max

max_v = 3.3  # max voltage
min_v = 0.0

slope = (max_v - min_v) / (x_max - x_min)


if __name__ == '__main__':

    while True:
        x = pin_read.read_u16()
        voltage = (slope * x) - (slope * x_min)
        if min_read > x:
            min_read = x
        print(f'voltage: {round(voltage, 2)}, x: {x}, min: {min_read}')
        sleep(0.3)
