from unittest.mock import Mock

# this mock is a function that return 5 always
mock_function = Mock(return_value="Welcome to Mock Wold!")
# call the mock function
x = mock_function()
# print what the mock returned
print(x)

