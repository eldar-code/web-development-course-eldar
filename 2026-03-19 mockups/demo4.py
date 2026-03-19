from unittest.mock import Mock
# to create a mock function with parameters use a function
def add(a, b):
    return a + b

# send the function to the mock
add_mock = Mock(side_effect=add)

x = add_mock(2, 7)
print(x)

print(add_mock(100, 200))
print(add_mock(2, 9))
print(add_mock(10, 20))

print("====================")
def max_val(val1, val2):
    if val1 > val2:
        return val1
    else:
        return val2

max_mock = Mock(side_effect=max_val)
print(max_mock(5, 7))
print(max_mock(9, 5))
print(max_mock(5, 5))
print(max_mock(-5, -2))