from unittest import TestCase
from ..sine_controller import SineController
controller = SineController()


class TestSineController(TestCase):

    def test_create_steps_0_to_12(self):
        actual = controller.create_steps(0, 12)
        expected = [0, 1, 3, 6, 9, 11, 12]
        self.assertListEqual(expected, actual)

    def test_create_steps_10_to_22(self):
        actual = controller.create_steps(10, 22)
        expected = [10, 11, 13, 16, 19, 21, 22]
        self.assertListEqual(expected, actual)

    def test_create_steps_0_to_24(self):
        actual = controller.create_steps(0, 24)
        expected = [0, 2, 6, 12, 18, 22, 24]
        self.assertListEqual(expected, actual)

    def test_create_steps_10_to_34(self):
        actual = controller.create_steps(10, 34)
        expected = [10, 12, 16, 22, 28, 32, 34]
        self.assertListEqual(expected, actual)

    def test_create_steps_0_to_6(self):
        actual = controller.create_steps(0, 6)
        expected = [0, 0.5, 1.5, 3, 4.5, 5.5, 6]
        self.assertListEqual(expected, actual)

    def test_move(self):
        controller.current = 0
        actual = []
        function = lambda x: actual.append(x)
        expected = [0, 1, 3, 6, 9, 11, 12]

        controller.move(12, function, 0)

        self.assertListEqual(expected, actual)
        self.assertEqual(12, controller.current)
