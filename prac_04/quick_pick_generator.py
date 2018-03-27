import random

MINIMUM = 1
MAXIMUM = 20
PICKS_PER_ROW = 6


def main():
    number_of_quick_picks = int(input("How many picks? "))
    for number in range(number_of_quick_picks):
        quick_pick = []
        for i in range(PICKS_PER_ROW):
            random_number = random.randint(MINIMUM, MAXIMUM)
            while random_number in quick_pick:
                random_number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(random_number)
        quick_pick.sort()
        print("{:>3} {:>3} {:>3} {:>3} {:>3} {:>3}".format(*quick_pick))
        # print(
        #     "{:>3} {:>3} {:>3} {:>3} {:>3} {:>3}".format(quick_pick[0], quick_pick[1], quick_pick[2], quick_pick[3],
        #                                                  quick_pick[4], quick_pick[5]))


main()
