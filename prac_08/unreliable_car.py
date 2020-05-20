"""
CP1404 Practical

"""
from car import Car
import random


class UnrealiableCar(Car):
    """A unreliable version of car"""

    def __init__(self, name, fuel, reliability):
        """
        Initialize a unreliable car base on Car class
        """
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """
        drive the car randomly
        """
        random_number = random.randint(0, 100)  # generate a random number
        if random_number >= self.reliability:   # not drive the car when random number is larger than reliability
            distance = 0

        distance_driven = super().drive(distance)   # call parent class
        return distance_driven  # return a distance
