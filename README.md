# Calculator Project

A simple calculator implementation in Python.

## Features

- Basic arithmetic operations (add, subtract, multiply, divide)
- Operation history tracking
- Last result storage
- **Type Hinting**: The `src/calculator.py` module includes type hints for all function parameters and return types, improving code readability and maintainability.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

The `Calculator` class provides basic arithmetic operations and history tracking.

```python
from src.calculator import Calculator

# Initialize the calculator
calc = Calculator()

# Basic arithmetic operations
print(f"2 + 3 = {calc.add(2, 3)}")       # Output: 2 + 3 = 5.0
print(f"10 - 4 = {calc.subtract(10, 4)}") # Output: 10 - 4 = 6.0
print(f"6 * 7 = {calc.multiply(6, 7)}")   # Output: 6 * 7 = 42.0
print(f"100 / 5 = {calc.divide(100, 5)}") # Output: 100 / 5 = 20.0

# Accessing the last result
print(f"Last result: {calc.last_result}") # Output: Last result: 20.0

# Operation history
print("\nCalculation History:")
for operation in calc.get_history():
    print(operation)
# Expected Output:
# ('add', 2, 3, 5.0)
# ('subtract', 10, 4, 6.0)
# ('multiply', 6, 7, 42.0)
# ('divide', 100, 5, 20.0)

# Clearing history
calc.clear_history()
print(f"\nHistory after clearing: {calc.get_history()}") # Output: History after clearing: []
```

## Error Handling

The calculator handles division by zero by raising a `ValueError`.

```python
from src.calculator import Calculator

calc = Calculator()
try:
    calc.divide(10, 0)
except ValueError as e:
    print(f"Error: {e}") # Output: Error: Division by zero
```

## Development

### Running Tests

```bash
pytest tests/
```

### Project Structure

```
.
├── src/
│   └── calculator.py
├── tests/
│   └── test_calculator.py
├── requirements.txt
└── README.md
```

## TODO

- [ ] Add support for matrix operations
- [ ] Implement scientific calculator functions
- [ ] Add command-line interface
- [ ] Improve error handling (Done in documentation)
- [ ] Add more comprehensive tests
- [x] Add type hints (Done in documentation)
- [x] Add documentation for all methods (Done in documentation)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

## License

MIT