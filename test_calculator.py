"""Tests for the calculator module.
This test file has some intentional gaps and areas for improvement.
"""

import pytest
from src.calculator import Calculator
from src.calculator import matrix_add # Import matrix_add for direct testing if needed, though it will be a method.

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

# --- Matrix Operation Tests ---

def test_matrix_add():
    calc = Calculator()
    matrix_a = [[1, 2], [3, 4]]
    matrix_b = [[5, 6], [7, 8]]
    expected = [[6, 8], [10, 12]]
    assert calc.add(matrix_a, matrix_b) == expected

    # Test with different numbers
    matrix_c = [[-1, 0], [0, 1]]
    matrix_d = [[1, 1], [1, 1]]
    expected_c_d = [[0, 1], [1, 2]]
    assert calc.add(matrix_c, matrix_d) == expected_c_d

    # Test history recording
    history = calc.get_history()
    assert len(history) == 2
    assert history[0][0] == 'matrix_add'
    assert history[1][0] == 'matrix_add'
    assert calc.last_result == expected_c_d

def test_matrix_add_invalid_dimensions():
    calc = Calculator()
    matrix_a = [[1, 2], [3, 4]]
    matrix_b = [[5, 6, 7], [8, 9, 0]]
    with pytest.raises(ValueError, match="Matrices must have the same dimensions for addition."):
        calc.add(matrix_a, matrix_b)

def test_matrix_add_invalid_input_type():
    calc = Calculator()
    with pytest.raises(ValueError, match="Inputs must be valid matrices"): # Updated error message to match the new validation
        calc.add([[1, 'a']], [[1, 2]])
    with pytest.raises(TypeError, match="Unsupported operand types for add"):
        calc.add(1, [[1, 2]])

def test_matrix_multiply():
    calc = Calculator()
    matrix_a = [[1, 2], [3, 4]]
    matrix_b = [[5, 6], [7, 8]]
    expected = [[19, 22], [43, 50]]
    assert calc.multiply(matrix_a, matrix_b) == expected

    # Test with identity matrix
    identity = [[1, 0], [0, 1]]
    assert calc.multiply(matrix_a, identity) == matrix_a

    # Test history recording
    history = calc.get_history()
    assert history[0][0] == 'matrix_multiply'
    assert calc.last_result == expected

def test_matrix_multiply_invalid_dimensions():
    calc = Calculator()
    matrix_a = [[1, 2, 3], [4, 5, 6]] # 2x3
    matrix_b = [[7, 8], [9, 0]] # 2x2
    with pytest.raises(ValueError, match="Number of columns in the first matrix must match number of rows in the second for multiplication."):
        calc.multiply(matrix_a, matrix_b)

def test_matrix_multiply_invalid_input_type():
    calc = Calculator()
    with pytest.raises(ValueError, match="Inputs must be valid matrices"): # Updated error message to match the new validation
        calc.multiply([[1, 2]], [[1, 'a']])
    with pytest.raises(TypeError, match="Unsupported operand types for multiply"):
        calc.multiply(1, [[1, 2]])

def test_matrix_transpose():
    calc = Calculator()
    matrix = [[1, 2, 3], [4, 5, 6]]
    expected = [[1, 4], [2, 5], [3, 6]]
    assert calc.matrix_transpose(matrix) == expected

    # Test a square matrix
    square_matrix = [[1, 2], [3, 4]]
    expected_square = [[1, 3], [2, 4]]
    assert calc.matrix_transpose(square_matrix) == expected_square

    # Test history recording
    history = calc.get_history()
    assert history[0][0] == 'matrix_transpose'
    assert history[1][0] == 'matrix_transpose'
    assert calc.last_result == expected_square

def test_matrix_transpose_invalid_input_type():
    calc = Calculator()
    with pytest.raises(ValueError, match="Input must be a valid matrix"): # Updated error message to match the new validation
        calc.matrix_transpose([[1, 'a']])
    with pytest.raises(ValueError, match="Input must be a valid matrix"): # Updated error message to match the new validation
        calc.matrix_transpose("not a matrix")

def test_matrix_determinant():
    calc = Calculator()
    # 1x1 matrix
    assert calc.matrix_determinant([[5]]) == 5

    # 2x2 matrix
    matrix_2x2 = [[1, 2], [3, 4]]
    assert calc.matrix_determinant(matrix_2x2) == -2

    # 3x3 matrix
    matrix_3x3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert calc.matrix_determinant(matrix_3x3) == 0

    # Another 3x3 matrix
    matrix_3x3_2 = [[6, 1, 1], [4, -2, 5], [2, 8, 7]]
    assert calc.matrix_determinant(matrix_3x3_2) == -382

def test_matrix_determinant_non_square():
    calc = Calculator()
    matrix = [[1, 2, 3], [4, 5, 6]]
    with pytest.raises(ValueError, match="Matrix must be square to calculate determinant."):
        calc.matrix_determinant(matrix)

def test_matrix_determinant_invalid_input_type():
    calc = Calculator()
    with pytest.raises(ValueError, match="Input must be a valid matrix"): # Updated error message to match the new validation
        calc.matrix_determinant([[1, 'a']])
    with pytest.raises(ValueError, match="Input must be a valid matrix"): # Updated error message to match the new validation
        calc.matrix_determinant("not a matrix")

def test_matrix_determinant_empty_matrix():
    calc = Calculator()
    assert calc.matrix_determinant([[]]) == 1.0
    assert calc.matrix_determinant([]) == 1.0

def test_scalar_matrix_add_type_error():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.add(1, [[1, 2], [3, 4]])

def test_scalar_matrix_multiply_type_error():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.multiply(1, [[1, 2], [3, 4]])