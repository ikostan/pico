# Raspberry Pi Pico W LESSON 6: Understanding If Statements in MicroPython
# https://www.youtube.com/watch?v=mS4YcJ0FcOU&list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5&index=6

"""
In this introductory video, I will show you how to do If Statements and conditionals
in microPython. I will start with simple examples, and then show how we can control
the state of an LED using If Statements.I will also show how to get input from the
user in micropython. This class is  for absolute beginners, and I do not assume you
already understand the material I am presenting. My goal is not to 'Show Off',
but to genuinely teach you how you can do this type of work and projects on your own.
I will show all work step-by-step, with clear instructions Enjoy!

Find more great content at my website,
"""

from machine import Pin  # pylint: disable=import-error

PIN_N = 14
led = Pin(PIN_N, Pin.OUT)


if __name__ == '__main__':
    led.value(0)

    while True:
        cmd_input = input("What would you like LED to be (On/Off/Toggle)? ")
        print(cmd_input)
        if cmd_input.lower() == 'on':
            led.value(1)
        elif cmd_input.lower() == 'off':
            led.value(0)
        elif cmd_input.lower() == 'toggle':
            led.toggle()
        else:
            print(f"{cmd_input} is unspecified...")
