from machine import Pin
from time import sleep

sleep(0.25)
led = Pin(5, Pin.OUT)

while True:
  led.toggle()
  sleep(0.5)
  print("Hello, Pi Pico!")