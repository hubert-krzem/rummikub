'''
File defining the tile object within rummikub

Tiles just need to hold a colour and a value,
Once initiated these values cannot be modified
'''

# from dataclasses import dataclass
# @dataclass(frozen=True)
class Tile:
    # Only accept: values -> 1 - 13 ; colour -> Red, Black, Blue, Orange
    validColours = ["Red", "Blue", "Black", "Orange"]
    validValues = [i for i in range(1, 14)]

    def __init__(self, colour, value):

        if not isinstance(colour, str):
            raise TypeError(f"Colour must be a string")
        colour = colour.capitalize()

        if not colour in self.validColours:
            raise ValueError(f"Colour must be one of {self.validColours}")
        
        if not isinstance(value, int):
            raise TypeError(f"Value must be an int")
        if not value in self.validValues:
            raise ValueError(f"Value must be within range {[self.validValues[0], self.validValues[-1]]}")
        
        self.colour = colour
        self.value = value

    def __str__(self):
        return f"{self.colour} {self.value}"