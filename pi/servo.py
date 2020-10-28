"""
Controller for a camera Pan-Tilt assembly.
Provides PWM for a pair of servos controlling pan and tilt.
On the Pi zero, pins 18, 12 and 13 support PWM on a hardware level (BCM numbering)
"""

from time import sleep
import RPi.GPIO as GPIO
import time
from pi.sine_controller import SineController


class Servo:

    degrees = 0
    pin = 0
    frequency = 500
    pwm = None

    def __init__(self, pin):

        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, self.frequency)
        self.start()

    def move_to(self, degrees):
        """
        Given an angle in degrees, this method sets the PWM duty cycle accordingly.
        :param degrees: The angle, in degrees, to set it to.
        """
        duty_cycle = float(degrees) / 1.8
        self.pwm.start(self.degrees)
        self.pwm.ChangeDutyCycle(duty_cycle)

    def start(self):
        self.pwm.start(self.degrees)

    def stop(self):
        self.pwm.stop()


