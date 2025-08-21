"""
Tests for the calculator module.
This test file has some intentional gaps and areas for improvement.
"""

import pytest
from calculator import Calculator

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
    matrix_a = [[1, 2], [3, 4]]
    matrix_b = [[5, 6], [7, 8]]
    expected_result = [[6, 8], [10, 12]]
    assert calc.matrix_add(matrix_a, matrix_b) == expected_result
    assert calc.last_result == expected_result
    assert calc.get_history()[-1][0] == 'matrix_add'
    assert calc.get_history()[-1][1] == matrix_a
    assert calc.get_history()[-1][2] == matrix_b
    assert calc.get_history()[-1][3] == expected_result

    with pytest.raises(ValueError):
        calc.matrix_add([[1, 2]], [[1]])
    with pytest.raises(TypeError):
        calc.matrix_add([[1, 2]], "not a matrix")

def test_matrix_multiply():
    calc = Calculator()
    matrix_a = [[1, 2], [3, 4]]
    matrix_b = [[5, 6], [7, 8]]
    expected_result = [[19, 22], [43, 50]]
    assert calc.matrix_multiply(matrix_a, matrix_b) == expected_result
    assert calc.last_result == expected_result
    assert calc.get_history()[-1][0] == 'matrix_multiply'
    assert calc.get_history()[-1][1] == matrix_a
    assert calc.get_history()[-1][2] == matrix_b
    assert calc.get_history()[-1][3] == expected_result

    with pytest.raises(ValueError):
        calc.matrix_multiply([[1, 2]], [[1, 2, 3]])
    with pytest.raises(TypeError):
        calc.matrix_multiply([[1, 2]], "not a matrix")

def test_matrix_transpose():
    calc = Calculator()
    matrix = [[1, 2, 3], [4, 5, 6]]
    expected_result = [[1, 4], [2, 5], [3, 6]]
    assert calc.matrix_transpose(matrix) == expected_result
    assert calc.last_result == expected_result
    assert calc.get_history()[-1][0] == 'matrix_transpose'
    assert calc.get_history()[-1][1] == matrix
    assert calc.get_history()[-1][2] == expected_result

    with pytest.raises(TypeError):
        calc.matrix_transpose("not a matrix")

def test_matrix_determinant():
    calc = Calculator()
    matrix_2x2 = [[1, 2], [3, 4]]
    assert calc.matrix_determinant(matrix_2x2) == -2
    assert calc.last_result == -2
    assert calc.get_history()[-1][0] == 'matrix_determinant'
    assert calc.get_history()[-1][1] == matrix_2x2
    assert calc.get_history()[-1][2] == -2

    matrix_3x3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert calc.matrix_determinant(matrix_3x3) == 0

    with pytest.raises(ValueError):
        calc.matrix_determinant([[1, 2]])
    with pytest.raises(TypeError):
        calc.matrix_determinant("not a matrix")

def test_multiply_scalar_and_matrix():
    calc = Calculator()
    assert calc.multiply(2, 3) == 6
    with pytest.raises(TypeError):
        calc.multiply(2, [[1, 2], [3, 4]])