"""
tests_1c.py

This module contains unit tests for the max_subarray_sum function defined in lab_1c.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_positive():
    assert max_subarray_sum([1,2,3,-5]) == 6
    assert max_subarray_sum([3,5,-4,2,8]) == 14
    assert max_subarray_sum([1,2,-3,4]) == 4

def test_negative():
    assert max_subarray_sum([-2,-5,-1,-10]) == -1

if __name__ == "__main__":
    pytest.main()