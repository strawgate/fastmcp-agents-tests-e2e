"""
A simple calculator module with basic arithmetic operations.
This module has some intentional issues and areas for improvement.
"""

class Calculator:
    def matrix_add(self, a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
        """Adds two matrices."""
        if len(a) != len(b) or len(a[0]) != len(b[0]):
            raise ValueError("Matrices must have the same dimensions for addition")
        result = [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
        self.last_result = result
        self.history.append(('matrix_add', a, b, result))
        return result

    def matrix_multiply(self, a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
        """Multiplies two matrices."""
        if len(a[0]) != len(b):
            raise ValueError("Number of columns in first matrix must equal number of rows in second matrix for multiplication")
        result_matrix = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    result_matrix[i][j] += a[i][k] * b[k][j]
        self.last_result = result_matrix
        self.history.append(('matrix_multiply', a, b, result_matrix))
        return result_matrix

    def matrix_transpose(self, a: list[list[float]]) -> list[list[float]]:
        """Transposes a matrix."""
        result = [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]
        self.last_result = result
        self.history.append(('matrix_transpose', a, result))
        return result

    def matrix_determinant(self, m: list[list[float]]) -> float:
        """Calculates the determinant of a square matrix."""
        if len(m) != len(m[0]):
            raise ValueError("Matrix must be square to calculate determinant")
        n = len(m)
        if n == 1:
            result = m[0][0]
            self.last_result = result
            self.history.append(('matrix_determinant', m, result))
            return result
        if n == 2:
            result = m[0][0] * m[1][1] - m[0][1] * m[1][0]
            self.last_result = result
            self.history.append(('matrix_determinant', m, result))
            return result
        determinant = 0
        for c in range(n):
            minor = [row[:c] + row[c+1:] for row in m[1:]]
            determinant += ((-1) ** c) * m[0][c] * self.matrix_determinant(minor)
        self.last_result = determinant
        self.history.append(('matrix_determinant', m, determinant))
        return determinant
    def __init__(self):
        self.last_result = None
        self.history = []

    def clear_history(self):
        """Clear calculation history."""
        self.history = []
        self.last_result = None

def matrix_add(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    """Adds two matrices."""
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError("Matrices must have the same dimensions for addition")
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def matrix_multiply(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    """Multiplies two matrices."""
    if len(a[0]) != len(b):
        raise ValueError("Number of columns in first matrix must equal number of rows in second matrix for multiplication")
    result_matrix = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result_matrix[i][j] += a[i][k] * b[k][j]
    return result_matrix

def matrix_transpose(a: list[list[float]]) -> list[list[float]]:
    """Transposes a matrix."""
    return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]

def matrix_determinant(m: list[list[float]]) -> float:
    """Calculates the determinant of a square matrix."""
    if len(m) != len(m[0]):
        raise ValueError("Matrix must be square to calculate determinant")
    n = len(m)
    if n == 1:
        return m[0][0]
    if n == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    determinant = 0
    for c in range(n):
        minor = [row[:c] + row[c+1:] for row in m[1:]]
        determinant += ((-1) ** c) * m[0][c] * matrix_determinant(minor)
    return determinant