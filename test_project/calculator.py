def add(a, b):
    """Adds two numbers and returns the result."""
    return a + b

def subtract(a, b):
    """Subtracts two numbers and returns the result."""
    return a - b

def multiply(a, b):
    """Multiplies two numbers and returns the result."""
    return a * b

def divide(a, b):
    """Divides two numbers and returns the result. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def matrix_add(matrix1, matrix2):
    """Adds two matrices and returns the result."""
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions to be added.")
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def matrix_multiply(matrix1, matrix2):
    """Multiplies two matrices and returns the result."""
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix.")
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

def matrix_transpose(matrix):
    """Transposes a matrix and returns the result."""
    result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return result

def matrix_determinant(matrix):
    """Calculates the determinant of a 2x2 or 3x3 matrix."""
    if len(matrix) == 2 and len(matrix[0]) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    elif len(matrix) == 3 and len(matrix[0]) == 3:
        det = 0
        det += matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        det -= matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        det += matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
        return det
    else:
        raise ValueError("Determinant can only be calculated for 2x2 or 3x3 matrices.")