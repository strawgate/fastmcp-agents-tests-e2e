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

    def matrix_add(self, a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
        """Add two matrices."""
        if len(a) != len(b) or len(a[0]) != len(b[0]):
            raise ValueError("Matrices must have the same dimensions for addition")
        result = [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
        self.last_result = result
        self.history.append(('matrix_add', a, b, result))
        return result

    def matrix_multiply(self, a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
        """Multiply two matrices."""
        if len(a[0]) != len(b):
            raise ValueError("Number of columns in the first matrix must equal the number of rows in the second matrix for multiplication")
        result = [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
        self.last_result = result
        self.history.append(('matrix_multiply', a, b, result))
        return result

    def matrix_transpose(self, a: list[list[float]]) -> list[list[float]]:
        """Transpose a matrix."""
        result = [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]
        self.last_result = result
        self.history.append(('matrix_transpose', a, result))
        return result

    def matrix_determinant(self, matrix: list[list[float]]) -> float:
        """Calculate the determinant of a square matrix."""
        n = len(matrix)
        if n == 0:
            raise ValueError("Cannot calculate determinant of an empty matrix")
        for row in matrix:
            if len(row) != n:
                raise ValueError("Matrix must be square")
        if n == 1:
            result = matrix[0][0]
        elif n == 2:
            result = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        else:
            determinant = 0
            for c in range(n):
                determinant += ((-1)**c) * matrix[0][c] * self._get_minor(matrix, 0, c)
            result = determinant
        self.last_result = result
        self.history.append(('matrix_determinant', matrix, result))
        return result

    def _get_minor(self, matrix: list[list[float]], i: int, j: int) -> list[list[float]]:
        return [row[:j] + row[j+1:] for k, row in enumerate(matrix) if k != i]

    def get_history(self) -> list:
        """Get calculation history."""
        return self.history

    def clear_history(self):
        """Clear calculation history."""
        self.history = []
        self.last_result = None