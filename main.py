# This program "blinks" LED on for one second and off for one second
#
# Created by: Daki Anrango-Boada
# Created on: March 2025

import time
import board
import digitalio

# Set LED to output
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# Looping LED on for one second and off for one second
while True:
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(1)

