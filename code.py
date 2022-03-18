# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT
#
# Blink
#
# Turns an LED on for one second, then off for one second, repeatedly.
# But the interval increases each time by 1 more second
#
# created by Infinity de Guzman on March 2022

"""
LED example for Pico. Blinks external LED on and off.

REQUIRED HARDWARE:
* LED on pin GP14.
"""
import time
import board
import digitalio

led = digitalio.DigitalInOut(board.GP14)
led.direction = digitalio.Direction.OUTPUT
blink_time = (1)

while True:
    led.value = True
    time.sleep(blink_time)
    led.value = False
    time.sleep(1)
    blink_time = blink_time + 1

