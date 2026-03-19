from unittest.mock import Mock

mock_function = Mock(side_effect=[2, 4, 6, 8])

print(mock_function()) # 2
print(mock_function()) # 4
print(mock_function()) # 6
print(mock_function()) # 8