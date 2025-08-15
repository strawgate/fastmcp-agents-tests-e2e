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

    def matrix_add(self, matrix1: list[list[float]], matrix2: list[list[float]]) -> list[list[float]]:
        """Add two matrices."""
        if not matrix1 or not matrix2:
            raise ValueError("Input matrices cannot be empty.")
        rows1 = len(matrix1)
        cols1 = len(matrix1[0])
        rows2 = len(matrix2)
        cols2 = len(matrix2[0])
        if rows1 != rows2 or cols1 != cols2:
            raise ValueError("Matrices must have the same dimensions for addition.")
        result = [[0 for _ in range(cols1)] for _ in range(rows1)]
        for i in range(rows1):
            for j in range(cols1):
                result[i][j] = matrix1[i][j] + matrix2[i][j]
        self.last_result = result
        self.history.append(('matrix_add', matrix1, matrix2, result))
        return result

    def matrix_multiply(self, matrix1: list[list[float]], matrix2: list[list[float]]) -> list[list[float]]:
        """Multiply two matrices."""
        if not matrix1 or not matrix2:
            raise ValueError("Input matrices cannot be empty.")
        rows1 = len(matrix1)
        cols1 = len(matrix1[0])
        rows2 = len(matrix2)
        cols2 = len(matrix2[0])
        if cols1 != rows2:
            raise ValueError("Number of columns in the first matrix must match the number of rows in the second matrix for multiplication.")
        result = [[0 for _ in range(cols2)] for _ in range(rows1)]
        for i in range(rows1):
            for j in range(cols2):
                for k in range(cols1):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]
        self.last_result = result
        self.history.append(('matrix_multiply', matrix1, matrix2, result))
        return result

    def matrix_transpose(self, matrix: list[list[float]]) -> list[list[float]]:
        """Transpose a matrix."""
        if not matrix:
            raise ValueError("Input matrix cannot be empty.")
        rows = len(matrix)
        cols = len(matrix[0])
        result = [[0 for _ in range(rows)] for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                result[j][i] = matrix[i][j]
        self.last_result = result
        self.history.append(('matrix_transpose', matrix, result))
        return result

    def matrix_determinant(self, matrix: list[list[float]]) -> float:
        """Calculate the determinant of a square matrix."""
        if not matrix:
            raise ValueError("Input matrix cannot be empty.")
        n = len(matrix)
        if any(len(row) != n for row in matrix):
            raise ValueError("Matrix must be square to calculate the determinant.")
        if n == 1:
            return matrix[0][0]
        if n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        determinant = 0
        for c in range(n):
            minor = [row[:c] + row[c+1:] for row in matrix[1:]]
            determinant += ((-1) ** c) * matrix[0][c] * self.matrix_determinant(minor)
        self.last_result = determinant
        self.history.append(('matrix_determinant', matrix, determinant))
        return determinant

    def get_history(self) -> list:
        """Get calculation history."""
        return self.history

    def clear_history(self):
        """Clear calculation history."""
        self.history = []
        self.last_result = None