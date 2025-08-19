"""A simple calculator module with basic arithmetic operations.
This module has some intentional issues and areas for improvement.
"""

import math

class Calculator:
    def __init__(self):
        self.last_result = None
        self.history = []

    def _record_history(self, operation: str, *operands, result):
        """Helper to record operations in history."""
        self.history.append((operation, *operands, result))
        self.last_result = result

    def add(self, x, y):
        """Add two numbers or two matrices."""
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            result = x + y
            self._record_history('add', x, y, result=result)
            return result
        elif isinstance(x, list) and isinstance(y, list):
            return self.matrix_add(x, y)
        else:
            raise TypeError("Unsupported operand types for add")

    def subtract(self, x: float, y: float) -> float:
        """Subtract y from x."""
        result = x - y
        self._record_history('subtract', x, y, result=result)
        return result

    def multiply(self, x, y):
        """Multiply two numbers or two matrices."""
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            result = x * y
            self._record_history('multiply', x, y, result=result)
            return result
        elif isinstance(x, list) and isinstance(y, list):
            return self.matrix_multiply(x, y)
        else:
            raise TypeError("Unsupported operand types for multiply")

    def divide(self, x: float, y: float) -> float:
        """Divide x by y."""
        if y == 0:
            raise ValueError("Division by zero")
        result = x / y
        self._record_history('divide', x, y, result=result)
        return result

    def get_history(self) -> list:
        """Get calculation history."""
        return self.history

    def clear_history(self):
        """Clear calculation history."""
        self.history = []
        self.last_result = None

    def matrix_add(self, matrix_a: list[list[float]], matrix_b: list[list[float]]) -> list[list[float]]:
        """Adds two matrices. Returns a new matrix."""
        if not self._is_valid_matrix(matrix_a) or not self._is_valid_matrix(matrix_b):
            raise ValueError("Inputs must be valid matrices (lists of lists of numbers).")

        rows_a = len(matrix_a)
        cols_a = len(matrix_a[0])
        rows_b = len(matrix_b)
        cols_b = len(matrix_b[0])

        if rows_a != rows_b or cols_a != cols_b:
            raise ValueError("Matrices must have the same dimensions for addition.")

        result_matrix = []
        for i in range(rows_a):
            row = []
            for j in range(cols_a):
                row.append(matrix_a[i][j] + matrix_b[i][j])
            result_matrix.append(row)

        self._record_history('matrix_add', matrix_a, matrix_b, result=result_matrix)
        return result_matrix

    def matrix_multiply(self, matrix_a: list[list[float]], matrix_b: list[list[float]]) -> list[list[float]]:
        """Multiplies two matrices. Returns a new matrix."""
        if not self._is_valid_matrix(matrix_a) or not self._is_valid_matrix(matrix_b):
            raise ValueError("Inputs must be valid matrices (lists of lists of numbers).")

        rows_a = len(matrix_a)
        cols_a = len(matrix_a[0])
        rows_b = len(matrix_b)
        cols_b = len(matrix_b[0])

        if cols_a != rows_b:
            raise ValueError("Number of columns in the first matrix must match number of rows in the second for multiplication.")

        result_matrix = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
        for i in range(rows_a):
            for j in range(cols_b):
                for k in range(cols_a):
                    result_matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]

        self._record_history('matrix_multiply', matrix_a, matrix_b, result=result_matrix)
        return result_matrix

    def matrix_transpose(self, matrix: list[list[float]]) -> list[list[float]]:
        """Transposes a matrix. Returns a new matrix."""
        if not self._is_valid_matrix(matrix):
            raise ValueError("Input must be a valid matrix (list of lists of numbers).")

        rows = len(matrix)
        cols = len(matrix[0])

        transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                transposed_matrix[j][i] = matrix[i][j]

        self._record_history('matrix_transpose', matrix, result=transposed_matrix)
        return transposed_matrix

    def matrix_determinant(self, matrix: list[list[float]]) -> float:
        """Calculates the determinant of a square matrix."""
        if not self._is_valid_matrix(matrix):
            raise ValueError("Input must be a valid matrix (list of lists of numbers).")

        n = len(matrix)
        if n == 0:
            return 1.0 # Determinant of an empty matrix is 1 by convention
        if n != len(matrix[0]):
            raise ValueError("Matrix must be square to calculate determinant.")

        if n == 1:
            return matrix[0][0]
        elif n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        else:
            determinant = 0
            for c in range(n):
                determinant += ((-1) ** c) * matrix[0][c] * self._get_minor(matrix, 0, c)
            return determinant

    def _get_minor(self, matrix: list[list[float]], row: int, column: int) -> list[list[float]]:
        """Helper to get the minor of a matrix for determinant calculation."""
        return [row_[:column] + row_[column+1:] for i, row_ in enumerate(matrix) if i != row]

    def _is_valid_matrix(self, matrix) -> bool:
        """Helper to validate if an input is a matrix (list of lists of numbers) and is not ragged."""
        if not isinstance(matrix, list) or not matrix:
            return False
        num_cols = len(matrix[0])
        if num_cols == 0:
            return False # Empty rows are not valid
        for row in matrix:
            if not isinstance(row, list) or len(row) != num_cols:
                return False
            for item in row:
                if not isinstance(item, (int, float)):
                    return False
        return True