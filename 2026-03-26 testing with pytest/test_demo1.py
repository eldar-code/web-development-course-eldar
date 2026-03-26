from unittest import TestCase


def add(a, b):
    return a + b


class Test1(TestCase):

    def test_add(self):
        self.assertEqual(5, add(3, 2))


