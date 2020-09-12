"""
Controller for a camera Pan-Tilt assembly.
Provides PWM for a pair of servos controlling pan and tilt.
On the Pi zero, pins 18, 12 and 13 support PWM on a hardware level (BCM numbering)
"""

from time import sleep
import RPi.GPIO as GPIO
from pi.sine_controller import SineController


class PanTilt(object):

    tilt_controller = SineController()
    pan_controller = SineController()
    tilt_degrees = 0
    pan_degrees = 0

    def __init__(self, pan_pin, tilt_pin):
        """
        Pins use BCM numbering
        :param pan_pin: this is the PWM pin connected to the pan axis.
        :param tilt_pin: this is the PWM pin connected to the tilt axis.
        """
        self.tilt_pin = tilt_pin
        self.pan_pin = pan_pin
        # setup GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.tilt_pin, GPIO.OUT)
        GPIO.setup(self.pan_pin, GPIO.OUT)
        print('PanTilt initialized, pan_pin is %s, tilt_pin is %s' % (self.pan_pin, self.tilt_pin))

    @staticmethod
    def __set_servo(servo, degrees):
        """
        Given an angle in degrees, this method sets the PWM duty cycle accordingly.

        :param servo: The servo pin to set the PWM ratio on.
        :param degrees: The angle, in degrees, to set it to.
        :except: Exception if the angle is not between 0 and 180.
        """
        if not 0 < degrees < 180:
            raise Exception('Servo angle must be between 0 and 180')

        duty_cycle = float(degrees) / 18 + 3
        print('pin %s, angle %s, duty cycle %.2f' % (servo, degrees, duty_cycle))
        pwm = GPIO.PWM(servo, 500)
        pwm.start(8)
        pwm.ChangeDutyCycle(duty_cycle)
        sleep(0.3)
        pwm.stop()

    def pan(self, angle):
        """
        Pan to this angle (degrees)
        """
        self.pan_degrees = angle
        self.__set_servo(self.pan_pin, self.pan_degrees)

    def tilt(self, angle):
        """
        Tilt to this angle (degrees)
        """
        self.tilt_degrees = angle
        self.__set_servo(self.tilt_pin, self.tilt_degrees)


