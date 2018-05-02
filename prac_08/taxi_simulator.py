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
    print(MENU)
    menu_choice = input("").upper()
    while menu_choice != "Q":
        if menu_choice == "C":
            for index, taxi in enumerate(taxis):
                print("{} - {}".format(index, taxi))
                taxi_choice = int(input("Choose taxi: "))
        elif menu_choice == "D":
            pass
            distance = int(input("Drive how far? "))


        else:
            print("Invalid menu choice")
        menu_choice = input("").upper()
    print("Taxis are now:")


main()