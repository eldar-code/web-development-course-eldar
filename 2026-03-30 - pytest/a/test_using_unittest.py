from unittest import TestCase
import a.calculator as calculator


class TestCalculator(TestCase):

    def test_add(self):
        result = calculator.add(2, 4)
        self.assertEqual(6, result)

    def test_subtract(self):
        result = calculator.subtract(2, 4)
        self.assertEqual(-2, result)
