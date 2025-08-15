"""
A simple calculator module with basic arithmetic operations.
This module has some intentional issues and areas for improvement.
"""

class Calculator:
    def __init__(self):
        self.last_result = None
        self.history = []
        self.matrix_history = []

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

    def matrix_add(self, matrix1: list[list[float]], matrix2: list[list[float]]) -> list[list[float]]:
        """Adds two matrices."""
        import numpy as np
        result_matrix = (np.array(matrix1) + np.array(matrix2)).tolist()
        self.last_result = result_matrix
        self.matrix_history.append(('matrix_add', matrix1, matrix2, result_matrix))
        return result_matrix

    def matrix_multiply(self, matrix1: list[list[float]], matrix2: list[list[float]]) -> list[list[float]]:
        """Multiplies two matrices."""
        import numpy as np
        result_matrix = (np.array(matrix1) @ np.array(matrix2)).tolist()
        self.last_result = result_matrix
        self.matrix_history.append(('matrix_multiply', matrix1, matrix2, result_matrix))
        return result_matrix

    def matrix_transpose(self, matrix: list[list[float]]) -> list[list[float]]:
        """Transposes a matrix."""
        import numpy as np
        result_matrix = np.array(matrix).T.tolist()
        self.last_result = result_matrix
        self.matrix_history.append(('matrix_transpose', matrix, result_matrix))
        return result_matrix

    def matrix_determinant(self, matrix: list[list[float]]) -> float:
        """Calculates the determinant of a matrix."""
        import numpy as np
        result = np.linalg.det(np.array(matrix))
        self.last_result = result
        self.matrix_history.append(('matrix_determinant', matrix, result))
        return float(result)

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
        return self.history + self.matrix_history

    def clear_history(self):
        """Clear calculation history."""
        self.history = []
        self.matrix_history = []
        self.last_result = None