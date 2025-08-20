# Calculator Project

A simple calculator implementation in Python.

## Features

- Basic arithmetic operations (add, subtract, multiply, divide)
- Operation history tracking
- Last result storage

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
from calculator import Calculator

calc = Calculator()
result = calc.add(2, 3)  # Returns 5
print(f"Add: {result}")

result = calc.subtract(5, 2)
print(f"Subtract: {result}")

result = calc.multiply(4, 5)
print(f"Multiply: {result}")

result = calc.divide(10, 2)
print(f"Divide: {result}")

print(f"History: {calc.get_history()}")
calc.clear_history()
print(f"History after clearing: {calc.get_history()}")
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


## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

## License

MIT