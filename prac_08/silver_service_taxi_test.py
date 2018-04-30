"""
CP1404 Practical
Test for Silver Service Taxi class.
"""

from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceClass."""
    luxury_taxi = SilverServiceTaxi("Luxury Taxi", 100, 2)
    print(luxury_taxi)
    luxury_taxi.drive(18)
    print(luxury_taxi.get_fare())


main()