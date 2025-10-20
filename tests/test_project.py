"""
-
"""
import unittest
from unittest.mock import patch, Mock
from my_app import project

class TestApp(unittest.TestCase):
    """
    -
    """

    def setUp(self):
        self.input = 'The Moon'
        self.amount = 5

    def tearDown(self):
        #return super().tearDown()
        pass

    def test_empty_input(self):
        """
        Testing how our code handles empty user inputs.
        Passes if a value error was raised
        """
        with self.assertRaises(ValueError):
            project.get_user_input('')



    def test_correct_input(self):
        """
        Testing how our code handles valid user inputs.
        Passes if no exceptions raised
        """

        self.assertEqual(project.get_user_input(self.input), True)


    def test_input_splitting(self):
        """
        Testing how our code splits valid user inputs.
        Passes if user input has been split correctly.
        """

        result = project.split_user_input(self.input)
        self.assertEqual(result, ['The', 'Moon'])


    def test_input_formatting(self):
        """
        Testing how our code formats valid user inputs to create a query.
        Passes if user input has been formatted correctly.
        """
        split_query = project.split_user_input(self.input)
        result = project.format_user_query(split_query)

        self.assertEqual(result, 'The%20Moon')


    def test_duplicate_word(self):
        """Tests function integrity when input contains duplicate words."""

        input_list = ['The', 'Moon', 'The']
        expected_output = 'The%20Moon%20The' # Expected correct output

        actual_output = project.format_user_query(input_list)
        self.assertEqual(actual_output, expected_output)


    @patch('my_app.project.arxiv.Client')  # Replace 'my_module' with the actual path
    def test_client_is_initialized(self, MockClient):
        """Tests that the arxiv.Client is called."""

        mock_client_instance = Mock()
        MockClient.return_value = mock_client_instance

        #creates the fake connection
        result = project.arxiv_connection()

        #ensures that the Mock Object has ran at least once
        MockClient.assert_called_once()
        #checks to see if when it ran, it returns the correct value
        self.assertEqual(result, mock_client_instance)