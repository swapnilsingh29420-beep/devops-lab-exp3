import pytest
import math
from basic_calc import add, subtract, multiply, divide
from advanced_calc import square_root, power, sine

# Basic operations test

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-4, -6) == -10

def test_subtract_numbers():
    assert subtract(10, 4) == 6

def test_multiply_numbers():
    assert multiply(5, 3) == 15

# Division Tests

def test_divide_normal():
    assert divide(10, 2) == 5

def test_divide_float_result():
    assert divide(7, 2) == 3.5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
        
def test_complex_expr():
    assert (square_root(16) * sine(0)) == 0
    
# Square Root Tests

def test_square_root_perfect_square():
    assert square_root(16) == 4

def test_square_root_float():
    assert square_root(2) == math.sqrt(2)

# Power Function Tests

def test_power_positive():
    assert power(2, 3) == 8

def test_power_zero_exponent():
    assert power(5, 0) == 1

# Sine Function Tests

def test_sine_90_degrees():
    assert pytest.approx(sine(90), 0.0001) == 1

