import pytest
from tiles import Tile, Colour

# Valid string input
def test_str_valid():
    tile = Tile(Colour.RED, 5)
    assert (str(tile) == "Red 5")

# Test invalid inputs
def test_invalid_colour():
    with pytest.raises(TypeError):
        tile = Tile("Purple", 5)

def test_invalid_value_14():
    with pytest.raises(ValueError):
        tile = Tile(Colour.RED, 14)

def test_invalid_value_0():
    with pytest.raises(ValueError):
        tile = Tile(Colour.RED, 0)

def test_invalid_colour_type():
    with pytest.raises(TypeError):
        tile = Tile(1, 5)

def test_invalid_value_type():
    with pytest.raises(TypeError):
        tile = Tile(Colour.RED, "1")


# Valid colour input tests
def test_init_red():
    tile = Tile(Colour.RED, 5)
    assert tile.colour == Colour.RED

def test_init_blue():
    tile = Tile(Colour.BLUE, 5)
    assert tile.colour == Colour.BLUE

def test_init_black():
    tile = Tile(Colour.BLACK, 5)
    assert tile.colour == Colour.BLACK

def test_init_orange():
    tile = Tile(Colour.ORANGE, 5)
    assert tile.colour == Colour.ORANGE