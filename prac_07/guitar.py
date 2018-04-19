"""CP1404 Practical - Guitar class"""
CURRENT_YEAR = 2018
VINTAGE_AGE = 50


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return guitar name, year, and cost of Guitar."""
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Returns the age of a guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Returns True if the guitar is 50 or more years old and False otherwise."""
        return self.get_age() >= VINTAGE_AGE
