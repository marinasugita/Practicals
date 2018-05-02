"""
CP1404 Practical
Silver Service Taxi class.
"""
from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """A version of a Taxi that includes fanciness."""

    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a Silver Service Taxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = self.price_per_km * fanciness

    def __str__(self):
        """Return a string like a Taxi but with flagfall."""
        return "{}, plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Return the price for the Silver Service Taxi trip."""
        return super().get_fare() + self.flagfall
