'''
Design Qs:
- How does rack get assigned to players?
'''

import pytest
# from rack import Rack

def test_init_empty():
    rack = Rack()
    assert rack.isEmpty() == True

