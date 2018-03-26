import random

MINIMUM = 1
MAXIMUM = 20
PICKS_PER_ROW = 6


def main():
    number_of_quick_picks = int(input("How many picks? "))
    for number in range(number_of_quick_picks):
        quick_picks = []
        for line in range(PICKS_PER_ROW):
            random_number = random.randint(MINIMUM, MAXIMUM)
            while random_number in quick_picks:
                random_number = random.randint(MINIMUM, MAXIMUM)
            quick_picks.append(random_number)
        quick_picks.sort()
        print(
            "{:>3} {:>3} {:>3} {:>3} {:>3} {:>3}".format(quick_picks[0], quick_picks[1], quick_picks[2], quick_picks[3],
                                                         quick_picks[4], quick_picks[5]))


main()
