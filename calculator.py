"""
A simple calculator module with basic arithmetic operations.
This module has some intentional issues and areas for improvement.
"""

class Calculator:
    """A simple calculator class that supports basic arithmetic operations and keeps a history.
    Usage Patterns:
        1. Instantiate the calculator:
            >>> calc = Calculator()
        2. Perform operations:
            >>> calc.add(10, 5)
            15.0
            >>> calc.subtract(calc.last_result, 3)
            12.0
        3. View and clear history:
            >>> calc.get_history()
            [('add', 10.0, 5.0, 15.0), ('subtract', 15.0, 3.0, 12.0)]
            >>> calc.clear_history()
            >>> calc.get_history()
            []
    """
    def __init__(self):
        self.last_result = None
        self.history = []

    def add(self, x: float, y: float) -> float:
        """Add two numbers.
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
        self.history.append(('add', x, y, result))
        return result

    def subtract(self, x: float, y: float) -> float:
        """Subtract y from x.
        Args:
            x (float): The number to subtract from.
            y (float): The number to subtract.
        Returns:
            float: The difference between x and y.
        Example:
            >>> calc = Calculator()
            >>> calc.subtract(5, 2)
            3.0
        """
        result = x - y
        self.last_result = result
        self.history.append(('subtract', x, y, result))
        return result

    def multiply(self, x: float, y: float) -> float:
        """Multiply two numbers.
        Args:
            x (float): The first number.
            y (float): The second number.
        Returns:
            float: The product of x and y.
        Example:
            >>> calc = Calculator()
            >>> calc.multiply(4, 5)
            20.0
        """
        # TODO: Add support for matrix multiplication
        result = x * y
        self.last_result = result
        self.history.append(('multiply', x, y, result))
        return result

    def divide(self, x: float, y: float) -> float:
        """Divide x by y.
        Args:
            x (float): The numerator.
            y (float): The denominator.
        Returns:
            float: The quotient of x and y.
        Raises:
            ValueError: If y is 0 (division by zero).
        Example:
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

    def get_history(self) -> list:
        """Get calculation history.
        Returns:
            list: A list of tuples, where each tuple represents an operation
                  in the format (operation_name, operand1, operand2, result).
        Example:
            >>> calc = Calculator()
            >>> calc.add(1, 1)
            2.0
            >>> calc.get_history()
            [(\'add\', 1.0, 1.0, 2.0)]
        """
        return self.history

    def clear_history(self):
        """Clear calculation history.
        Returns:
            None
        Example:
            >>> calc = Calculator()
            >>> calc.add(1, 1)
            2.0
            >>> calc.clear_history()
            >>> calc.get_history()
            []
        """
        self.history = []
        self.last_result = None