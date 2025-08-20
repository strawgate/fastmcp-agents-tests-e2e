import doctest
import unittest
from calculator import Calculator

class TestCalculatorDocumentation(unittest.TestCase):
    def test_doctests(self):
        # Run doctests from the calculator module
        results = doctest.testmod(Calculator)
        self.assertEqual(results.failed, 0)