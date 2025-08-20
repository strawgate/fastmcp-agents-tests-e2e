"""
A simple calculator module with basic arithmetic operations.
This module has some intentional issues and areas for improvement.
"""

class Calculator:
    def __init__(self):
        """Initializes a new Calculator instance.

        Attributes:
            last_result (float | None): Stores the result of the last performed calculation. Initially None.
            history (list[tuple]): A list of tuples, where each tuple represents a past calculation.
                                   Each tuple contains (operation_name, operand1, operand2, result).
        """
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
        """Multiplies two numbers and returns the product.

        Args:
            x (float): The first number.
            y (float): The second number.

        Returns:
            float: The product of x and y.

        Examples:
            >>> calc = Calculator()
            >>> calc.multiply(6, 7)
            42.0
            >>> calc.multiply(-2, 8)
            -16.0
        """
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

    def get_history(self) -> list[tuple[str, float, float, float]]:
        """Retrieves the history of all calculations performed.

        Returns:
            list[tuple[str, float, float, float]]: A list of tuples, each containing the operation name,
                                                   operands, and result of a past calculation.

        Examples:
            >>> calc = Calculator()
            >>> calc.add(1, 2)
            3.0
            >>> calc.subtract(5, 1)
            4.0
            >>> calc.get_history()
            [("add", 1.0, 2.0, 3.0), ("subtract", 5.0, 1.0, 4.0)]
        """
        """Get calculation history."""
        return self.history

    def clear_history(self):
        """Clear calculation history."""
        self.history = []
        self.last_result = None calculation history."""
        return self.history

    def clear_history(self):
        """Clear calculation history."""
        self.history = []
        self.last_result = Noneulation history."""
        return self.history

    def clear_history(self):
        """Clear calculation history."""
        self.history = []
        self.last_result = None calculation history."""
        return self.history

    def clear_history(self):
        """Clear calculation history."""
        self.history = []
        self.last_result = Noneelf.history = []
        self.last_result = None