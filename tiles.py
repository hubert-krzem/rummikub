'''
File defining the tile object within rummikub

Tiles just need to hold a colour and a value,
Once initiated these values cannot be modified
'''

from enum import Enum

class Colour(Enum):
    RED = "Red"
    BLUE = "Blue"
    BLACK = "Black"
    ORANGE = "Orange"

class Tile:
    # Only accept: values -> 1 - 13;
    # Valid colours defined in the colours class
    validValues = list(range(1,14))

    def __init__(self, colour, value):

        if not isinstance(colour, Colour):
            raise TypeError(f"Colour must be a Colour enum member from: {[colour.value for colour in Colour]}")
        
        if not isinstance(value, int):
            raise TypeError(f"Value must be an integer")
        if not value in self.validValues:
            raise ValueError(f"Value must be within range {[self.validValues[0], self.validValues[-1]]}")
        
        self.colour = colour
        self.value = value

    def __str__(self):
        return f"{self.colour.value} {self.value}"