"""
Tests for the calculator module.
This test file has some intentional gaps and areas for improvement.
"""

import pytest
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
    # TODO: Add test cases for zero multiplication

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
    assert len(history) == 2
    assert history[0][0] == 'add'
    assert history[1][0] == 'subtract'

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
    expected = [[6, 8], [10, 12]]
    assert calc.matrix_add(matrix1, matrix2) == expected

    # Test with different dimensions (should raise ValueError)
    matrix3 = [[1, 2]]
    with pytest.raises(ValueError):
        calc.matrix_add(matrix1, matrix3)

def test_matrix_multiply():
    calc = Calculator()
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]
    expected = [[19, 22], [43, 50]]
    assert calc.matrix_multiply(matrix1, matrix2) == expected

    # Test with non-multipliable dimensions (should raise ValueError)
    matrix3 = [[1, 2, 3]]
    with pytest.raises(ValueError):
        calc.matrix_multiply(matrix1, matrix3)

def test_matrix_transpose():
    calc = Calculator()
    matrix = [[1, 2, 3], [4, 5, 6]]
    expected = [[1, 4], [2, 5], [3, 6]]
    assert calc.matrix_transpose(matrix) == expected

def test_matrix_determinant():
    calc = Calculator()
    matrix1 = [[1]]
    assert calc.matrix_determinant(matrix1) == 1

    matrix2 = [[1, 2], [3, 4]]
    assert calc.matrix_determinant(matrix2) == -2

    matrix3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert calc.matrix_determinant(matrix3) == 0

    # Test with non-square matrix (should raise ValueError)
    matrix4 = [[1, 2], [3, 4], [5, 6]]
    with pytest.raises(ValueError):
        calc.matrix_determinant(matrix4)
