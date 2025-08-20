"""
A simple calculator module providing basic arithmetic operations and history tracking.
"""

class Calculator:
    """Represents a simple calculator with basic arithmetic operations and a calculation history.

    Attributes:
        last_result (float | None): Stores the result of the last calculation.
        history (list[tuple]): A list of tuples, where each tuple represents a past operation
                               (operation_name, operand1, operand2, result).
    """
    def __init__(self):
        """Initializes the Calculator with no last result and an empty history."""
        self.last_result: float | None = None
        self.history: list[tuple[str, float, float, float]] = []

    def add(self, x: float, y: float) -> float:
        """Adds two numbers and returns the sum.

        Args:
            x (float): The first number.
            y (float): The second number.

        Returns:
            float: The sum of x and y.

        Example:
            >>> calc = Calculator()
            >>> calc.add(2, 3)
            5.0
        """
        result = x + y
        self.last_result = result
        self.history.append(("add", x, y, result))
        return result

    def subtract(self, x: float, y: float) -> float:
        """Subtracts the second number from the first number and returns the difference.

        Args:
            x (float): The number to subtract from.
            y (float): The number to subtract.

        Returns:
            float: The difference between x and y.

        Example:
            >>> calc = Calculator()
            >>> calc.subtract(5, 3)
            2.0
        """
        result = x - y
        self.last_result = result
        self.history.append(("subtract", x, y, result))
        return result

    def multiply(self, x: float, y: float) -> float:
        """Multiplies two numbers and returns the product.

        Args:
            x (float): The first number.
            y (float): The second number.

        Returns:
            float: The product of x and y.

        Example:
            >>> calc = Calculator()
            >>> calc.multiply(2, 3)
            6.0
        """
        result = x * y
        self.last_result = result
        self.history.append(("multiply", x, y, result))
        return result

    def divide(self, x: float, y: float) -> float:
        """Divides the first number by the second number and returns the quotient.

        Args:
            x (float): The dividend.
            y (float): The divisor.

        Returns:
            float: The quotient of x divided by y.

        Raises:
            ValueError: If y is zero (division by zero).

        Example:
            >>> calc = Calculator()
            >>> calc.divide(6, 2)
            3.0
            >>> calc.divide(5, 0)
            Traceback (most recent call last):
                ...
            ValueError: Division by zero
        """
        if y == 0:
            raise ValueError("Division by zero")
        result = x / y
        self.last_result = result
        self.history.append(("divide", x, y, result))
        return result

    def get_history(self) -> list[tuple[str, float, float, float]]:
        """Retrieves the history of all calculations performed.

        Returns:
            list[tuple[str, float, float, float]]: A list of tuples, where each tuple contains
                                                  the operation name, the operands, and the result.
                                                  Example: [("add", 2.0, 3.0, 5.0)]

        Example:
            >>> calc = Calculator()
            >>> calc.add(1, 2)
            3.0
            >>> calc.get_history()
            [("add", 1.0, 2.0, 3.0)]
        """
        return self.history

    def clear_history(self) -> None:
        """Clears the entire calculation history and resets the last result to None.

        Example:
            >>> calc = Calculator()
            >>> calc.add(1, 2)
            3.0
            >>> calc.clear_history()
            >>> calc.get_history()
            []
        """
        self.history = []
        self.last_result = None