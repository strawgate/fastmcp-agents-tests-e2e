"""
A simple calculator module with basic arithmetic operations.
This module has some intentional issues and areas for improvement.
"""

class Calculator:
    def __init__(self):
        self.last_result = None
        self.history = []

    def add(self, x: float, y: float) -> float:
        """Add two numbers."""
        result = x + y
        self.last_result = result
        self.history.append(('add', x, y, result))
        return result

    def subtract(self, x: float, y: float) -> float:
        """Subtract y from x."""
        result = x - y
        self.last_result = result
        self.history.append(('subtract', x, y, result))
        return result

    def multiply(self, x: float, y: float) -> float:
        """Multiply two numbers."""
        # TODO: Add support for matrix multiplication
        result = x * y
        self.last_result = result
        self.history.append(('multiply', x, y, result))
        return result

    def divide(self, x: float, y: float) -> float:
        """Divide x by y."""
        if y == 0:
            raise ValueError("Division by zero")
        result = x / y
        self.last_result = result
        self.history.append(('divide', x, y, result))
        return result

    def get_history(self) -> list:
        """Get calculation history."""
        return self.history

    def clear_history(self):
        """Clear calculation history."""
        self.history = []
        self.last_result = None

    def _is_valid_matrix(self, matrix):
        if not isinstance(matrix, list) or not matrix:
            return False
        if not all(isinstance(row, list) for row in matrix):
            return False
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        if not all(len(row) == num_cols for row in matrix):
            return False
        if not all(isinstance(val, (int, float)) for row in matrix for val in row):
            return False
        return True

    def matrix_add(self, matrix1, matrix2):
        if not (self._is_valid_matrix(matrix1) and self._is_valid_matrix(matrix2)):
            raise ValueError("Invalid matrix input. Both inputs must be valid matrices.")
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            raise ValueError("Matrices must have the same dimensions for addition.")

        result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
        self.last_result = result
        self.history.append(("matrix_add", matrix1, matrix2, result))
        return result

    def matrix_multiply(self, matrix1, matrix2):
        if not (self._is_valid_matrix(matrix1) and self._is_valid_matrix(matrix2)):
            raise ValueError("Invalid matrix input. Both inputs must be valid matrices.")
        if len(matrix1[0]) != len(matrix2):
            raise ValueError("Number of columns in the first matrix must match the number of rows in the second matrix for multiplication.")

        result = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix1[0])))
                   for j in range(len(matrix2[0]))] for i in range(len(matrix1))]
        self.last_result = result
        self.history.append(("matrix_multiply", matrix1, matrix2, result))
        return result

    def matrix_transpose(self, matrix):
        if not self._is_valid_matrix(matrix):
            raise ValueError("Invalid matrix input. Input must be a valid matrix.")

        result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        self.last_result = result
        self.history.append(("matrix_transpose", matrix, result))
        return result

    def matrix_determinant(self, matrix):
        if not self._is_valid_matrix(matrix):
            raise ValueError("Invalid matrix input. Input must be a valid matrix.")
        if len(matrix) != len(matrix[0]):
            raise ValueError("Matrix must be square for determinant calculation.")

        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        elif n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        elif n == 3:
            return (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
                    matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
                    matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]))
        else:
            raise ValueError("Determinant calculation supported only for 1x1, 2x2, and 3x3 matrices.")