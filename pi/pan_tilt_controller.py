from servo import Servo
from sine_controller import SineController


class PanTiltController(object):

    pan_controller = None
    tilt_controller = None
    duration = 5

    def __init__(self, pan_pin, tilt_pin):
        """
        Pins use BCM numbering
        :param pan_pin: this is the PWM pin connected to the pan axis.
        :param tilt_pin: this is the PWM pin connected to the tilt axis.
        """
        self.pan_controller = SineController(Servo(pan_pin))
        self.tilt_controller = SineController(Servo(tilt_pin))
        print('PanTilt initialized, pan_pin is %s, tilt_pin is %s' % (pan_pin, tilt_pin))

    def pan(self, angle):
        """
        Pan to this angle (degrees)
        """
        self.pan_controller.move(angle, self.duration)

    def tilt(self, angle):
        """
        Tilt to this angle (degrees)
        """
        self.tilt_controller.move(angle, self.duration)
