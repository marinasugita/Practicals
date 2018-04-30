"""
CP1404 Practical
Unreliable Car class.
"""
from prac_08.car import Car
from random import randint

class UnreliableCar(Car):
    """A version of a Car that is unreliable."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string like a Car but with reliability."""
        return "{}, reliability = {}%".format(super().__str__(), self.reliability)

    def drive(self, distance):
        random_number = randint(0, 100)
        if random_number < self.reliability:
