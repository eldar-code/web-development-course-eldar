import a.calculator as calculator


def test_add():
    assert calculator.add(2, 4) == 6

def test_subtract():
    assert calculator.subtract(2, 6) == -4

