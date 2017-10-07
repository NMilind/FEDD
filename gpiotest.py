#!usr/bin/env python

import time
import RPi.GPIO as GPIO

# Plug the ground into PIN 9
# Plug the ain into PIN 3

# Set mode to Board Pin Layout
GPIO.setmode(GPIO.BOARD)

# Set up PIN 3 as the main output, with an initial setting of 3.3V
GPIO.setup(3, GPIO.OUT, initial = GPIO.HIGH)

state = GPIO.LOW

# Indefinite Blinking Behavior
try:
    while (True):

        GPIO.output(3, state)
        state = GPIO.LOW if (state == GPIO.HIGH) else state = GPIO.HIGH
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()