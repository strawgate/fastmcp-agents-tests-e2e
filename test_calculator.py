"""
Tests for the calculator module.
This test file has some intentional gaps and areas for improvement.
"""

import pytest
import numpy as np
from src.calculator import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0

def test_subtract():
    calc = Calculator()
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(1, 1) == 0
    # TODO: Add more test cases for negative numbers

def test_multiply():
    calc = Calculator()
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(-2, 3) == -6
    assert calc.multiply(0, 5) == 0


def test_divide():
    calc = Calculator()
    assert calc.divide(6, 2) == 3
    assert calc.divide(5, 2) == 2.5

    with pytest.raises(ValueError):
        calc.divide(5, 0)

def test_history():
    calc = Calculator()
    calc.add(2, 3)
    calc.subtract(5, 2)

    history = calc.get_history()
    assert len(history) == 5
    assert history[0][0] == 'add'
    assert history[1][0] == 'subtract'
    assert history[2][0] == 'matrix_add'
    assert history[3][0] == 'matrix_multiply'
    assert history[4][0] == 'matrix_transpose'

def test_clear_history():
    calc = Calculator()
    calc.add(2, 3)
    calc.clear_history()
    assert len(calc.get_history()) == 0
    assert calc.last_result is None


def test_matrix_add():
    calc = Calculator()
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]
    expected_result = [[6, 8], [10, 12]]
    assert calc.matrix_add(matrix1, matrix2) == expected_result
    assert calc.last_result == expected_result

def test_matrix_multiply():
    calc = Calculator()
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]
    expected_result = [[19, 22], [43, 50]]
    assert calc.matrix_multiply(matrix1, matrix2) == expected_result
    assert calc.last_result == expected_result

def test_matrix_transpose():
    calc = Calculator()
    matrix = [[1, 2], [3, 4]]
    expected_result = [[1, 3], [2, 4]]
    assert calc.matrix_transpose(matrix) == expected_result
    assert calc.last_result == expected_result

def test_matrix_determinant():
    calc = Calculator()
    matrix = [[1, 2], [3, 4]]
    expected_result = -2.0
    # Using numpy to calculate the determinant for comparison
    assert calc.matrix_determinant(matrix) == expected_result
    assert calc.last_result == expected_result