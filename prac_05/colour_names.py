"""
CP1404/CP5632 Practical
Colour names in a dictionary
"""

COLOUR_NAMES = {"burlywood": "#deb887", "chocolate": "#d2691e", "coral": "#ff7f50", "pink": "#ffc0cb",
                "grey": "#bebebe", "plum": "#dda0dd", "khaki": "#f40e68c", "lavender": "#e6e6fa", "maroon": "#b03060",
                "orchid": "da70d6"}

colour = input("Enter colour: ").lower()
while colour != "":
    if colour in COLOUR_NAMES:
        print(colour, "is", COLOUR_NAMES[colour])
    else:
        print("Invalid colour")
    colour = input("Enter colour: ").lower()

for colour, value in COLOUR_NAMES.items():
    print("{:<10} is {}".format(colour, value))
