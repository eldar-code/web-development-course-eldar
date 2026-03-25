a = 3
b = 2
total = a + b + 1
expected = 5

try:
    assert total == expected
    print("Test Success")
except AssertionError as e:
    print("Test Failure: Wrong total value")

print("=== End ===")
