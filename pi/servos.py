'''
Controller for a camera Pan-Tilt assembly.
Provides PWM for a pair of servos controlling pan and tilt.
On the Pi zero, pins 18, 12 and 13 support PWM on a hardware level (BCM numbering)
'''
from time import sleep
import RPi.GPIO as GPIO

class PanTilt(object):

 
	def __init__(self, pan_pin, tilt_pin):
		'''
		Pins use BCM numbering
		pan_pin: this is the PWM pin connected to the pan axis.
		tilt_pin: this is the PWM pin connected to the tilt axis.
		'''
		self.tilt_pin = tilt_pin
		self.pan_pin = pan_pin
		# setup GPIO
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup(self.tilt_pin, GPIO.OUT)
		GPIO.setup(self.pan_pin, GPIO.OUT)
		print('PanTilt initialized, pan_pin is %s, tilt_pin is %s' % (self.pan_pin, self.tilt_pin))

	def set_servo(self, servo, angle):
		dutyCycle = float(angle) / 18 + 3
		print('pin %s, angle %s, dutyCycle %.2f' % (servo, angle, dutyCycle))
		pwm = GPIO.PWM(servo, 50)
		pwm.start(8)
		pwm.ChangeDutyCycle(dutyCycle)
		sleep(0.3)
		pwm.stop()

	def pan(self, angle):
		'''
		Pan through this angle (degrees)
		'''
		self.set_servo(self.pan_pin, angle)

	def tilt(self, angle):
		'''
		Tilt through this angle (degrees)
		'''
		self.set_servo(self.tilt_pin, angle)