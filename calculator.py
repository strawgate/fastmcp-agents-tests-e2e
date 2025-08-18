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
        # TODO: Add support for matrix operations (addition, multiplication, transposition, determinant)
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

    def matrix_add(self, a, b):
        """Add two matrices."""
        if len(a) != len(b) or len(a[0]) != len(b[0]):
            raise ValueError("Matrices must have the same dimensions for addition")
        result = [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
        self.last_result = result
        self.history.append(('matrix_add', a, b, result))
        return result

    def matrix_multiply(self, a, b):
        """Multiply two matrices."""
        if len(a[0]) != len(b):
            raise ValueError("Number of columns in first matrix must equal number of rows in second matrix for multiplication")
        
        result = [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
        self.last_result = result
        self.history.append(('matrix_multiply', a, b, result))
        return result

    def matrix_transpose(self, a):
        """Transpose a matrix."""
        result = [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]
        self.last_result = result
        self.history.append(('matrix_transpose', a, result))
        return result

    def matrix_determinant(self, a):
        """Calculate the determinant of a 2x2 or 3x3 matrix."""
        if len(a) != len(a[0]):
            raise ValueError("Matrix must be square for determinant calculation")
        if len(a) == 2:
            result = a[0][0] * a[1][1] - a[0][1] * a[1][0]
        elif len(a) == 3:
            result = (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1]) -
                      a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0]) +
                      a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))
        else:
            raise ValueError("Determinant calculation supported for 2x2 and 3x3 matrices only")
        self.last_result = result
        self.history.append(('matrix_determinant', a, result))
        return result

    def get_history(self) -> list:
        """Get calculation history."""
        return self.history

    def clear_history(self):
        """Clear calculation history."""
        self.history = []
        self.last_result = None