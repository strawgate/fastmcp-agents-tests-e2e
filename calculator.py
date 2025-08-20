"""A simple calculator module with basic arithmetic operations.

This module provides fundamental arithmetic operations like addition, subtraction,
multiplication, and division, along with features to track operation history and
store the last calculated result.

The `Calculator` class is designed for basic numerical computations and includes
error handling for operations like division by zero. It also maintains a history
of all operations performed during its lifetime, which can be retrieved or cleared.

Example:
    >>> calc = Calculator()
    >>> calc.add(10, 5)
    15.0
    >>> calc.subtract(10, 5)
    5.0
    >>> calc.multiply(10, 5)
    50.0
    >>> calc.divide(10, 5)
    2.0
    >>> calc.get_history()
    [(\'add\', 10, 5, 15.0), (\'subtract\', 10, 5, 5.0), (\'multiply\', 10, 5, 50.0), (\'divide\', 10, 5, 2.0)]
    >>> calc.clear_history()
    >>> calc.get_history()
    []

This module is intended to be straightforward for basic use cases but also highlights
areas where more advanced features (e.g., matrix operations) or more sophisticated
error handling could be implemented.
"""

class Calculator:
    def __init__(self):
        self.last_result = None
        self.history = []

    def add(self, x: float, y: float) -> float:
        """Adds two numbers together and returns the sum.

        This method takes two floating-point numbers, `x` and `y`, and returns their sum.
        The operation is recorded in the calculator\'s history, and the result is stored
        as the `last_result`.

        Args:
            x (float): The first number.
            y (float): The second number.

        Returns:
            float: The sum of `x` and `y`.

        Example:
            >>> calc = Calculator()
            >>> calc.add(5.0, 3.0)
            8.0
            >>> calc.last_result
            8.0
        """
        result = x + y
        self.last_result = result
        self.history.append(('add', x, y, result))
        return result

    def subtract(self, x: float, y: float) -> float:
        """Subtracts the second number from the first and returns the difference.

        This method takes two floating-point numbers, `x` and `y`, and returns the result
        of `x` minus `y`. The operation is recorded in the calculator\'s history, and the
        result is stored as the `last_result`.

        Args:
            x (float): The number from which to subtract.
            y (float): The number to subtract.

        Returns:
            float: The difference between `x` and `y`.

        Example:
            >>> calc = Calculator()
            >>> calc.subtract(10.0, 4.0)
            6.0
            >>> calc.last_result
            6.0
        """
        result = x - y
        self.last_result = result
        self.history.append(('subtract', x, y, result))
        return result

    def multiply(self, x: float, y: float) -> float:
        """Multiplies two numbers and returns the product.

        This method takes two floating-point numbers, `x` and `y`, and returns their product.
        The operation is recorded in the calculator\'s history, and the result is stored
        as the `last_result`.

        Args:
            x (float): The first number.
            y (float): The second number.

        Returns:
            float: The product of `x` and `y`.

        Example:
            >>> calc = Calculator()
            >>> calc.multiply(6.0, 7.0)
            42.0
            >>> calc.last_result
            42.0
        """
        result = x * y
        self.last_result = result
        self.history.append(('multiply', x, y, result))
        return result

    def divide(self, x: float, y: float) -> float:
        """Divides the first number by the second and returns the quotient.

        This method takes two floating-point numbers, `x` and `y`, and returns the result
        of `x` divided by `y`. It raises a `ValueError` if `y` is zero to prevent
        division by zero errors. The operation is recorded in the calculator\'s history,
        and the result is stored as the `last_result`.

        Args:
            x (float): The dividend.
            y (float): The divisor.

        Returns:
            float: The quotient of `x` divided by `y`.

        Raises:
            ValueError: If `y` is 0.

        Example:
            >>> calc = Calculator()
            >>> calc.divide(10.0, 2.0)
            5.0
            >>> calc.last_result
            5.0
            >>> try:
            >>>     calc.divide(10.0, 0.0)
            >>> except ValueError as e:
            >>>     print(e)
            Division by zero
        """
        if y == 0:
            raise ValueError("Division by zero")
        result = x / y
        self.last_result = result
        self.history.append(('divide', x, y, result))
        return result

    def get_history(self) -> list[tuple[str, float, float, float]]:
        """Retrieves the complete history of operations performed by the calculator.

        Each entry in the history is a tuple containing the operation name (str),
        the two operands (float), and the result (float). The history is maintained
        in the order operations were performed.

        Returns:
            list[tuple[str, float, float, float]]: A list of tuples, each representing
            a recorded operation.

        Example:
            >>> calc = Calculator()
            >>> calc.add(1, 1)
            2.0
            >>> calc.subtract(5, 2)
            3.0
            >>> calc.get_history()
            [(\'add\', 1, 1, 2.0), (\'subtract\', 5, 2, 3.0)]
        """
        return self.history

    def clear_history(self) -> None:
        """Clears the entire calculation history and resets the `last_result`.

        This method reinitializes the `history` list to empty and sets `last_result` to `None`.

        Example:
            >>> calc = Calculator()
            >>> calc.add(1, 2)
            3.0
            >>> calc.get_history()
            [(\'add\', 1, 2, 3.0)]
            >>> calc.clear_history()
            >>> calc.get_history()
            []
            >>> calc.last_result is None
            True
        """
        self.history = []
        self.last_result = None