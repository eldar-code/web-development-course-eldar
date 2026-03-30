from unittest import TestCase
import a.calculator as calculator


class TestCalculator(TestCase):

    def setUp(self):
        print("--------- runs before each test")

    def tearDown(self):
        print("--------- runs after each test")

    def test_add(self):
        print("==test add")
        result = calculator.add(2, 4)
        self.assertEqual(6, result)

    def test_subtract(self):
        print("==test subtract")
        result = calculator.subtract(2, 4)
        self.assertEqual(-2, result)
