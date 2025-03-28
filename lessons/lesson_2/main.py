"""
Raspberry Pi Pico W LESSON 2: Understanding and Using Breadboards
https://www.youtube.com/watch?v=eGdrtikKc5U&list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5&index=2
"""

import time
from machine import Pin  # pylint: disable=import-error

# Led config: pin, out
LED = Pin(15, Pin.OUT)

if __name__ == '__main__':
    # Main loop
    while True:
        # OFF
        print("LED is off")
        LED.value(0)
        time.sleep(0.5)
        # ON
        print("LED is on")
        LED.value(1)
        time.sleep(1)
