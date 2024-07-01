"""
Raspberry Pi Pico W LESSON 5: Reading Analog Voltages Using a Potentiometer
https://www.youtube.com/watch?v=ODWwErH_iGA&list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5&index=5
"""

from time import sleep
import machine  # pylint: disable=import-error

PIN_READ: machine.ADC = machine.ADC(28)

X_MIN: int = 96  # min readings
X_MAX: int = 65535

V_MAX: float = 3.3  # max voltage
V_MIN: float = 0.0

SLOPE: float = (V_MAX - V_MIN) / (X_MAX - X_MIN)

if __name__ == '__main__':

    while True:
        X: int = PIN_READ.read_u16()  # pylint: disable=E1111
        VOLTAGE: float = (SLOPE * X) - (SLOPE * X_MIN)
        print(f'voltage: {round(VOLTAGE, 2)}, x: {X}')
        sleep(0.3)
