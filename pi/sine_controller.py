from time import sleep


class SineController:

    current = 0
    # summing the roughly sinusoidal sequence 1,2,3,3,2,1
    increments = [0, 1, 3, 6, 9, 11, 12]
    num_increments = len(increments)
    max = increments[-1]

    def __init__(self):
        ...

    def create_steps(self, current, target):
        """
        Given a current and target location, scales the 'increments'
        list across the interval, and returns the new list.

        :param current: current value.
        :param target: target value.
        :return: The scaled list.
        """
        distance = target - current
        delta = distance / self.max
        steps = map(
            lambda x: current + x * delta,
            self.increments
        )
        return list(steps)

    def move(self, target, position_function, duration):
        """
        Pass this the servo's PWM function and a target position.
        It will invoke the PWM function smoothly until
        the target position is reached.

        :param target: The desired end position of the servo.
        :param position_function: The function that moves the servo, e.g. a PWM function.
        :param duration: Duration of the movement. A short duration makes for a jerky movement.
        :return: None
        """
        sleep_time = duration / self.num_increments
        steps = self.create_steps(self.current, target)
        for i in range(self.num_increments):
            step = steps[i]
            position_function(step)
            self.current = step
            sleep(sleep_time)