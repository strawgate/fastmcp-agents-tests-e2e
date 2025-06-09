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
from src.calculator import Calculator

calc = Calculator()
result = calc.add(2, 3)  # Returns 5
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
- [ ] Improve error handling
- [ ] Add more comprehensive tests
- [ ] Add type hints
- [ ] Add documentation for all methods

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

## License

MIT