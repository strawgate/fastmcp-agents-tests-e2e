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
    matrix_a = [[1, 2], [3, 4]]
    matrix_b = [[5, 6], [7, 8]]
    expected_result = [[6, 8], [10, 12]]
    assert calc.matrix_add(matrix_a, matrix_b) == expected_result

    # Test with different dimensions (should raise ValueError)
    matrix_c = [[1, 2]]
    with pytest.raises(ValueError):
        calc.matrix_add(matrix_a, matrix_c)

def test_matrix_multiply():
    calc = Calculator()
    matrix_a = [[1, 2], [3, 4]]
    matrix_b = [[5, 6], [7, 8]]
    expected_result = [[19, 22], [43, 50]]
    assert calc.matrix_multiply(matrix_a, matrix_b) == expected_result

    # Test with non-matching dimensions (should raise ValueError)
    matrix_c = [[1], [2], [3]]
    with pytest.raises(ValueError):
        calc.matrix_multiply(matrix_a, matrix_c)

    # Test with identity matrix
    identity = [[1, 0], [0, 1]]
    assert calc.matrix_multiply(matrix_a, identity) == matrix_a

def test_matrix_transpose():
    calc = Calculator()
    matrix_a = [[1, 2, 3], [4, 5, 6]]
    expected_result = [[1, 4], [2, 5], [3, 6]]
    assert calc.matrix_transpose(matrix_a) == expected_result

    # Test square matrix
    matrix_b = [[1, 2], [3, 4]]
    expected_result_b = [[1, 3], [2, 4]]
    assert calc.matrix_transpose(matrix_b) == expected_result_b

    # Test empty matrix
    empty_matrix = []
    with pytest.raises(ValueError):
        calc.matrix_transpose(empty_matrix)

def test_matrix_determinant():
    calc = Calculator()

    # 1x1 matrix
    matrix_1x1 = [[5]]
    assert calc.matrix_determinant(matrix_1x1) == 5

    # 2x2 matrix
    matrix_2x2 = [[1, 2], [3, 4]]
    assert calc.matrix_determinant(matrix_2x2) == -2

    # 3x3 matrix
    matrix_3x3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert calc.matrix_determinant(matrix_3x3) == 0  # Example: a singular matrix

    # Non-square matrix (should raise ValueError)
    non_square_matrix = [[1, 2, 3], [4, 5, 6]]
    with pytest.raises(ValueError):
        calc.matrix_determinant(non_square_matrix)

    # Matrix larger than 3x3 (should raise ValueError)
    large_matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    with pytest.raises(ValueError):
        calc.matrix_determinant(large_matrix)

    # Empty matrix
    empty_matrix = [[]]
    with pytest.raises(ValueError):
        calc.matrix_determinant(empty_matrix)

    # Test matrix multiplication via the multiply method
    matrix_a = [[1, 2], [3, 4]]
    matrix_b = [[5, 6], [7, 8]]
    expected_result = [[19, 22], [43, 50]]
    assert calc.multiply(matrix_a, matrix_b) == expected_result
