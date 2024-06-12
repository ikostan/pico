"""
Raspberry Pi Pico W LESSON 9: Getting Analog Output Using PWM (Pulse Width Modulation)
https://www.youtube.com/watch?v=GXA1Y6lA14A&list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5&index=12
"""

from machine import (PWM, Pin)
from time import sleep

pin_num = 16
analogOut = PWM(Pin(pin_num))
analogOut.freq(1000)
analogOut.duty_u16(0)

while True:
    try:
        user_input = input("Please enter voltage output between"
                           " 0 and 3.3 or type exit to stop the execution: ")

        if user_input.lower() == 'exit':
            print("Exiting program now...")
            analogOut.duty_u16(0)
            break
        else:
            user_input = float(user_input)

            if user_input < 0 or user_input > 3.3:
                raise Exception(f"Invalid voltage value -> {user_input}.")

        pwm_val = int((65550 / 3.3) * user_input)
        analogOut.duty_u16(pwm_val)

    except Exception as e:
        print(e)

    finally:
        sleep(0.4)
