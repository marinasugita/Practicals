"""
CP1404 Practical
Client code for Taxi Simulator which uses the Taxi and SilverServiceTaxi classes.
"""

from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi
MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    total_bill = 0
    taxis = [Taxi("Pruis", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU)
    menu_choice = input("").upper()
    while menu_choice != "Q":
        if menu_choice == "C":
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            taxi = taxis[taxi_choice]
        elif menu_choice == "D":
            distance_to_drive = int(input("Drive how far? "))
            taxi.start_fare()
            taxi.drive(distance_to_drive)
            cost = taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(taxi.name, cost))
            total_bill += cost
        else:
            print("Invalid menu choice")
        print("Bill to date: ${:.2f}".format(total_bill))
        print(MENU)
        menu_choice = input("").upper()

    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, str(taxi)))


main()
