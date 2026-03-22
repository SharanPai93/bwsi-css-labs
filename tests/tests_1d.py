"""
tests_1d.py

This module contains unit tests for the two_sum function defined in lab_1d.py.
"""

import pytest
from labs.lab_1.lab_1d import two_sum

def test_valid():
    assert two_sum([1, 4, 2, 5], 6) == [0, 3] or two_sum([1, 4, 2, 5], 6) == [1, 2]
    assert two_sum([1,2,3,4,5,6], 11) == [4, 5]
    assert two_sum([3, 9, 10, 2, 5], 11) == [1, 3]

def test_invalid():
    assert two_sum([2, 5, 3, 6], 100) == []
    assert two_sum([5, 10, 15], 5) == []

if __name__ == "__main__":
    pytest.main()