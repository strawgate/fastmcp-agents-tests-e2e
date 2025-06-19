import unittest
from test_project.calculator import add, subtract, multiply, divide, matrix_add, matrix_multiply, matrix_transpose, matrix_determinant

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(2, 5), -3)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 5), -5)
        self.assertEqual(multiply(0, 10), 0)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(5, 2), 2.5)
        with self.assertRaises(ValueError):
            divide(1, 0)

    def test_matrix_add(self):
        matrix1 = [[1, 2], [3, 4]]
        matrix2 = [[5, 6], [7, 8]]
        expected = [[6, 8], [10, 12]]
        self.assertEqual(matrix_add(matrix1, matrix2), expected)

        matrix3 = [[1, 2, 3], [4, 5, 6]]
        matrix4 = [[7, 8, 9], [10, 11, 12]]
        expected2 = [[8, 10, 12], [14, 16, 18]]
        self.assertEqual(matrix_add(matrix3, matrix4), expected2)

        with self.assertRaises(ValueError):
            matrix_add([[1]], [[1, 2]])

    def test_matrix_multiply(self):
        matrix1 = [[1, 2], [3, 4]]
        matrix2 = [[5, 6], [7, 8]]
        expected = [[19, 22], [43, 50]]
        self.assertEqual(matrix_multiply(matrix1, matrix2), expected)

        matrix3 = [[1, 2, 3], [4, 5, 6]]
        matrix4 = [[7, 8], [9, 10], [11, 12]]
        expected2 = [[58, 64], [139, 154]]
        self.assertEqual(matrix_multiply(matrix3, matrix4), expected2)

        with self.assertRaises(ValueError):
            matrix_multiply([[1, 2]], [[1], [2, 3]])

    def test_matrix_transpose(self):
        matrix1 = [[1, 2], [3, 4]]
        expected = [[1, 3], [2, 4]]
        self.assertEqual(matrix_transpose(matrix1), expected)

        matrix2 = [[1, 2, 3], [4, 5, 6]]
        expected2 = [[1, 4], [2, 5], [3, 6]]
        self.assertEqual(matrix_transpose(matrix2), expected2)

    def test_matrix_determinant(self):
        matrix2x2 = [[1, 2], [3, 4]]
        self.assertEqual(matrix_determinant(matrix2x2), -2)

        matrix3x3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(matrix_determinant(matrix3x3), 0)

        with self.assertRaises(ValueError):
            matrix_determinant([[1]])
        with self.assertRaises(ValueError):
            matrix_determinant([[1, 2, 3, 4], [5, 6, 7, 8]])

if __name__ == '__main__':
    unittest.main()