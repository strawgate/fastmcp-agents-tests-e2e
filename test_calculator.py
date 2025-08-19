"""
Tests for the calculator module.
This test file has some intentional gaps and areas for improvement.
"""

import pytest
from src.calculator import Calculator, matrix_add, matrix_multiply, matrix_transpose, matrix_determinant

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
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]
    expected = [[6, 8], [10, 12]]
    assert matrix_add(matrix1, matrix2) == expected

    matrix3 = [[1, 2, 3], [4, 5, 6]]
    matrix4 = [[7, 8, 9], [10, 11, 12]]
    expected2 = [[8, 10, 12], [14, 16, 18]]
    assert matrix_add(matrix3, matrix4) == expected2

    with pytest.raises(ValueError):
        matrix_add([[1]], [[1, 2]])

def test_matrix_multiply():
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]
    expected = [[19, 22], [43, 50]]
    assert matrix_multiply(matrix1, matrix2) == expected

    matrix3 = [[1, 2, 3]]
    matrix4 = [[7], [8], [9]]
    expected2 = [[50]]
    assert matrix_multiply(matrix3, matrix4) == expected2

    with pytest.raises(ValueError):
        matrix_multiply([[1, 2]], [[1], [2], [3]])

def test_matrix_transpose():
    matrix1 = [[1, 2], [3, 4]]
    expected = [[1, 3], [2, 4]]
    assert matrix_transpose(matrix1) == expected

    matrix2 = [[1, 2, 3], [4, 5, 6]]
    expected2 = [[1, 4], [2, 5], [3, 6]]
    assert matrix_transpose(matrix2) == expected2

def test_matrix_determinant():
    matrix1 = [[1]]
    assert matrix_determinant(matrix1) == 1

    matrix2 = [[1, 2], [3, 4]]
    assert matrix_determinant(matrix2) == -2

    matrix3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert matrix_determinant(matrix3) == 0

    with pytest.raises(ValueError):
        matrix_determinant([[1, 2, 3], [4, 5, 6]])