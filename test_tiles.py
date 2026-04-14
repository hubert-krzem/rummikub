import pytest
from tiles import Tile

# Valid string input
def test_str_valid():
    tile = Tile("Red", 5)
    assert (str(tile) == "Red 5")

# Test invalid inputs
def test_invalid_colour():
    with pytest.raises(ValueError):
        tile = Tile("Purple", 5)

def test_invalid_value_14():
    with pytest.raises(ValueError):
        tile = Tile("Red", 14)

def test_invalid_value_0():
    with pytest.raises(ValueError):
        tile = Tile("Red", 0)

def test_invalid_colour_type():
    with pytest.raises(TypeError):
        tile = Tile(1, 0)

def test_invalid_value_type():
    with pytest.raises(TypeError):
        tile = Tile("Red", "1")


# Valid colour input tests
def test_init_red():
    tile = Tile("Red", 5)
    assert tile.colour == "Red"

def test_init_black():
    tile = Tile("Black", 5)
    assert tile.colour == "Black"

def test_init_blue():
    tile = Tile("Blue", 5)
    assert tile.colour == "Blue"

def test_init_orange():
    tile = Tile("Orange", 5)
    assert tile.colour == "Orange"

def test_str_capitalization():
    tile = Tile("red", 5)
    assert tile.colour == "Red"