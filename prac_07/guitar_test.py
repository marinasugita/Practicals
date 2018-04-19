"""CP1404 Practical - Simple test for the Guitar class."""
from prac_07.guitar import Guitar


def run_tests():
    guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2012)

    print("{} get_age() - Expected 96. Got {}".format(guitar.name, guitar.get_age()))
    assert guitar.get_age() == 96, "get_age is broken"

    print("{} get_age() - Expected 6. Got {}".format(guitar2.name, guitar2.get_age()))
    assert guitar2.get_age() == 6, "get_age is broken"

    print("{} is_vintage() - Expected True. Got {}".format(guitar.name, guitar.is_vintage()))
    assert guitar.is_vintage() == True, "is_vintage is broken"

    print("{} is_vintage() - Expected False. Got {}".format(guitar2.name, guitar2.is_vintage()))
    assert guitar2.is_vintage() == False, "is_vintage is broken"


run_tests()
