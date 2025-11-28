import pytest
from Cal_Speed import calculate_speed

def test_calculate_speed_case1():
    result = calculate_speed(100, 2)
    expected = 50
    assert result == expected

def test_calculate_speed_case2():
    result = calculate_speed(150, 2)
    expected = 75
    assert result == expected
