"""
CP1404 Practical
Client code for Taxi Simulator which uses the Taxi and SilverServiceTaxi classes.
"""

from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi
MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    taxis = [Taxi("Pruis", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
