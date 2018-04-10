"""CP1404 Practical - Programming Language class"""


class ProgrammingLanguage:
    """Represent a Programming Language object."""

    def __init__(self, name="", typing="", reflection=False, year=0):
        """Initialise a Programming Language instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        else:
            return False