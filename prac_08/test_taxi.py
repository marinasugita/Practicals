"""
CP1404 Practical
Test for Taxi class.
"""

from prac_08.taxi import Taxi


def main():
    """Test Taxi."""
    prius_1 = Taxi("Prius 1", 100)
    prius_1.drive(40)
    print(prius_1)
    print("Current fare is ${}".format(prius_1.get_fare()))

    prius_1.start_fare()
    prius_1.drive(100)
    print(prius_1)
    print("Current fare is ${}".format(prius_1.get_fare()))


main()
