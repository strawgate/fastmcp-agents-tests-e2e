"""
A simple calculator module with basic arithmetic operations.
This module has some intentional issues and areas for improvement.
"""

class Calculator:
    def __init__(self):
        """
        Initializes the Calculator with a clear history and no previous result.
        """
        self.last_result = None
        self.history = []

    def add(self, x: float, y: float) -> float:
        """
        Adds two numbers and returns the sum.

        Args:
            x (float): The first number.
            y (float): The second number.

        Returns:
            float: The sum of x and y.

        Examples:
            >>> calc = Calculator()
            >>> calc.add(2, 3)
            5.0
        """
        result = x + y
        self.last_result = result
        self.history.append(('add', x, y, result))
        return result

    def subtract(self, x: float, y: float) -> float:
        """
        Subtracts the second number from the first and returns the difference.

        Args:
            x (float): The number to subtract from.
            y (float): The number to subtract.

        Returns:
            float: The difference between x and y.

        Examples:
            >>> calc = Calculator()
            >>> calc.subtract(5, 2)
            3.0
        """
        result = x - y
        self.last_result = result
        self.history.append(('subtract', x, y, result))
        return result

    def multiply(self, x: float, y: float) -> float:
        """
        Multiplies two numbers and returns the product.

        Args:
            x (float): The first number.
            y (float): The second number.

        Returns:
            float: The product of x and y.

        Examples:
            >>> calc = Calculator()
            >>> calc.multiply(4, 2)
            8.0

        # TODO: Add support for matrix multiplication
        """
        result = x * y
        self.last_result = result
        self.history.append(('multiply', x, y, result))
        return result

    def divide(self, x: float, y: float) -> float:
        """
        Divides the first number by the second and returns the quotient.

        Args:
            x (float): The numerator.
            y (float): The denominator.

        Returns:
            float: The quotient of x divided by y.

        Raises:
            ValueError: If the denominator y is zero.

        Examples:
            >>> calc = Calculator()
            >>> calc.divide(10, 2)
            5.0
            >>> calc.divide(5, 0)
            Traceback (most recent call last):
                ...
            ValueError: Division by zero
        """
        if y == 0:
            raise ValueError("Division by zero")
        result = x / y
        self.last_result = result
        self.history.append(('divide', x, y, result))
        return result

    def get_history(self) -> list[tuple[str, float, float, float]]:
        """
        Retrieves the history of all calculations performed.

        Returns:
            list[tuple[str, float, float, float]]: A list of tuples, where each tuple
            represents a past operation in the format (operation_name, operand1, operand2, result).

        Examples:
            >>> calc = Calculator()
            >>> calc.add(1, 1)
            2.0
            >>> calc.get_history()
            [('add', 1, 1, 2.0)]
        """
        return self.history

    def clear_history(self):
        """
        Clears the calculation history and resets the last result.

        Examples:
            >>> calc = Calculator()
            >>> calc.add(1, 1)
            2.0
            >>> calc.clear_history()
            >>> calc.get_history()
            []
        """
        self.history = []
        self.last_result = None

    # General usage pattern example
    """
    Usage Pattern:

    The Calculator class can be used to perform a series of arithmetic operations.
    The `last_result` attribute stores the result of the most recent operation,
    and `history` keeps a log of all operations performed.

    Example:
        >>> calc = Calculator()
        >>> calc.add(10, 5)
        15.0
        >>> calc.subtract(calc.last_result, 3)
        12.0
        >>> calc.get_history()
        [('add', 10, 5, 15.0), ('subtract', 15.0, 3, 12.0)]
        >>> calc.clear_history()
        >>> calc.get_history()
        []
    """