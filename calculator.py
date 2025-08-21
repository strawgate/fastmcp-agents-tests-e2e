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
        if isinstance(x, list) and isinstance(y, list):
            return self.matrix_multiply(x, y)
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

    def matrix_add(self, matrix_a: list[list[float]], matrix_b: list[list[float]]) -> list[list[float]]:
        """Add two matrices."""
        if not (isinstance(matrix_a, list) and all(isinstance(row, list) for row in matrix_a) and
                isinstance(matrix_b, list) and all(isinstance(row, list) for row in matrix_b)):
            raise TypeError("Inputs must be matrices (list of lists).")

        if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
            raise ValueError("Matrices must have the same dimensions for addition.")
        
        result = [[matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))] for i in range(len(matrix_a))]
        self.last_result = result
        self.history.append(('matrix_add', matrix_a, matrix_b, result))
        return result

    def matrix_multiply(self, matrix_a: list[list[float]], matrix_b: list[list[float]]) -> list[list[float]]:
        """Multiply two matrices."""
        if not (isinstance(matrix_a, list) and all(isinstance(row, list) for row in matrix_a) and
                isinstance(matrix_b, list) and all(isinstance(row, list) for row in matrix_b)):
            raise TypeError("Inputs must be matrices (list of lists).")

        if len(matrix_a[0]) != len(matrix_b):
            raise ValueError("Number of columns in the first matrix must match the number of rows in the second matrix for multiplication.")

        result = [[sum(matrix_a[i][k] * matrix_b[k][j] for k in range(len(matrix_b)))
                   for j in range(len(matrix_b[0]))] for i in range(len(matrix_a))]
        self.last_result = result
        self.history.append(('matrix_multiply', matrix_a, matrix_b, result))
        return result

    def matrix_transpose(self, matrix: list[list[float]]) -> list[list[float]]:
        """Transpose a matrix."""
        if not (isinstance(matrix, list) and all(isinstance(row, list) for row in matrix)):
            raise TypeError("Input must be a matrix (list of lists).")

        result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        self.last_result = result
        self.history.append(('matrix_transpose', matrix, result))
        return result

    def matrix_determinant(self, matrix: list[list[float]]) -> float:
        """Calculate the determinant of a square matrix."""
        if not (isinstance(matrix, list) and all(isinstance(row, list) for row in matrix)):
            raise TypeError("Input must be a matrix (list of lists).")

        n = len(matrix)
        if n != len(matrix[0]):
            raise ValueError("Matrix must be square to calculate the determinant.")

        if n == 1:
            return matrix[0][0]
        elif n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        
        determinant = 0
        for c in range(n):
            minor_matrix = [row[:c] + row[c+1:] for row in (matrix[:0] + matrix[1:])]
            determinant += ((-1) ** c) * matrix[0][c] * self.matrix_determinant(minor_matrix)
        
        self.last_result = determinant
        self.history.append(('matrix_determinant', matrix, determinant))
        return determinant