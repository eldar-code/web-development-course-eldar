from unittest import TestCase
from unittest.mock import patch, Mock

import app.service
from app import service


class TestService(TestCase):

    # {'id': 1, 'name': 'John Doe', 'age': 20}
    @patch("app.service.db.get_student")
    def test_get_student_positive(self, mock_get_student: Mock):
        # AAA
        # Arrange - set up the mock object
        mock_get_student.return_value = {'id': 1, 'name': 'Mock Student'}
        # Act - use the mock
        result = service.get_student(1)
        # Assert
        self.assertEqual({'id': 1, 'name': 'Mock Student'}, result)
        # Validation - make sure we actually used the mock
        mock_get_student.assert_called_once_with(1)

    @patch("app.service.db.get_student")
    def test_get_student_negative(self, mock_get_student: Mock):
        # arrange
        mock_get_student.side_effect = KeyError("not found: 1")
        # act, assert
        self.assertRaises(KeyError, service.get_student, 111)
        # Validation - make sure we actually used the mock
        mock_get_student.assert_called_once_with(111)

    @patch("app.service.db.add_student")
    def test_add_student_positive(self, mock_add_student: Mock):
        # arrange
        mock_add_student.return_value = {'name': 'Mock Student', 'age': 25, 'id': 101}

        # create students with age cases
        students = [
            {'name': 'Mock Student', 'age': 18, 'id': 101},
            {'name': 'Mock Student', 'age': 30, 'id': 101},
            {'name': 'Mock Student', 'age': 120, 'id': 101}]

        for student in students:
            # act
            result = service.add_student(student)
            # assert
            self.assertEqual({'name': 'Mock Student', 'age': 25, 'id': 101}, result)

        # validate
        self.assertEqual(3, mock_add_student.call_count)
