"""
Raspberry Pi Pico W LESSON 6: Understanding If Statements in MicroPython
https://www.youtube.com/watch?v=mS4YcJ0FcOU&list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5&index=6
"""

from machine import Pin  # pylint: disable=import-error

PIN_N = 14
LED = Pin(PIN_N, Pin.OUT)


if __name__ == '__main__':
    LED.value(0)

    while True:
        CMD_INPUT = input("What would you like LED to be (On/Off/Toggle)? ")
        print(CMD_INPUT)
        if CMD_INPUT.lower() == 'on':
            LED.value(1)
        elif CMD_INPUT.lower() == 'off':
            LED.value(0)
        elif CMD_INPUT.lower() == 'toggle':
            LED.toggle()
        else:
            print(f"{CMD_INPUT} is unspecified...")
