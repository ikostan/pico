"""
Raspberry Pi Pico W LESSON 6: Understanding If Statements in MicroPython
https://www.youtube.com/watch?v=mS4YcJ0FcOU&list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5&index=6
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
