from unittest.mock import Mock

# mock function that raises error:
# 1. create an error object - with error message
e = ValueError("Error raised by mock")
# create the mock
mock_error_function = Mock(side_effect=e)

# use the mock to get an error
try:
    mock_error_function()
except ValueError as e:
    print(e) # Error raised by mock


