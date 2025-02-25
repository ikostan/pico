"""
Raspberry Pi Pico W LESSON 9: Getting Analog Output Using PWM (Pulse Width Modulation)
https://www.youtube.com/watch?v=GXA1Y6lA14A&list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5&index=10

Raspberry Pi Pico W LESSON 10: Create a Dimmable LED in Micropython
https://www.youtube.com/watch?v=DJhoUklKidc&list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5&index=11
"""
from builtins import Exception
from time import sleep
from machine import (PWM, Pin)  # pylint: disable=import-error


class VoltageError(Exception):
    """
    Custom exception.
    Raises an error in regard to voltage input.
    """

    def __init__(self, message) -> None:
        """
        Call the base class constructor with the parameters it needs
        :param message:
        """
        super().__init__(message)


PIN_NUM: int = 16
analogOut: PWM = PWM(Pin(PIN_NUM))
analogOut.freq(1000)
analogOut.duty_u16(0)

if __name__ == '__main__':

    while True:

        try:
            user_input: str = input("Please enter voltage output between"
                                    " 0 and 3.3 or type exit to stop the execution: ")

            if user_input.lower() == 'exit':
                print("Exiting program now...")
                analogOut.duty_u16(0)
                break

            user_input_flt: float = float(user_input)
            if user_input_flt < 0.0 or user_input_flt > 3.3:
                raise VoltageError(f"Invalid voltage value -> {user_input}.")

            pwm_val: int = int((65550 / 3.3) * user_input_flt)
            analogOut.duty_u16(pwm_val)

        except VoltageError as e:
            print(e)

        finally:
            sleep(0.4)
