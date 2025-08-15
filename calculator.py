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

    def matrix_add(self, a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
        """Add two matrices."""
        if len(a) != len(b) or len(a[0]) != len(b[0]):
            raise ValueError("Matrices must have the same dimensions for addition.")
        result = [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
        self.last_result = result
        self.history.append(('matrix_add', a, b, result))
        return result

    def matrix_multiply(self, a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
        """Multiply two matrices."""
        if len(a[0]) != len(b):
            raise ValueError("Number of columns in the first matrix must equal the number of rows in the second matrix for multiplication.")
        rows_a = len(a)
        cols_a = len(a[0])
        rows_b = len(b)
        cols_b = len(b[0])
        result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
        for i in range(rows_a):
            for j in range(cols_b):
                for k in range(cols_a):
                    result[i][j] += a[i][k] * b[k][j]
        self.last_result = result
        self.history.append(('matrix_multiply', a, b, result))
        return result

    def matrix_transpose(self, a: list[list[float]]) -> list[list[float]]:
        """Transpose a matrix."""
        if not a or not a[0]:
            raise ValueError("Cannot transpose an empty matrix.")
        rows = len(a)
        cols = len(a[0])
        result = [[0 for _ in range(rows)] for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                result[j][i] = a[i][j]
        self.last_result = result
        self.history.append(('matrix_transpose', a, result))
        return result

    def matrix_determinant(self, a: list[list[float]]) -> float:
        """Calculate the determinant of a square matrix."""
        n = len(a)
        if n == 0:
            return 1.0
        if any(len(row) != n for row in a):
            raise ValueError("Matrix must be square for determinant calculation.")
        if n > 3:
            raise ValueError("Determinant calculation for matrices larger than 3x3 is not supported.")
        if n == 1:
            return a[0][0]
        if n == 2:
            return a[0][0] * a[1][1] - a[0][1] * a[1][0]
        if n == 3:
            return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1]) -
                    a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0]) +
                    a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))
        # No self.last_result and self.history.append for determinant as it returns a single float and not a matrix.
        return result

    def get_history(self) -> list:
        """Get calculation history."""
        return self.history

    def clear_history(self):
        """Clear calculation history."""
        self.history = []
        self.last_result = None