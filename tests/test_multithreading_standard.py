import sys
import unittest
from io import StringIO
from typing import cast

from python_multithreading import multithreading_standard as ms


class TestMultithreadingStandard(unittest.TestCase):

    def setUp(self):
        # Redirect stdout to capture print statements
        self.held_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        # Reset stdout after each test method
        sys.stdout = self.held_stdout

    def test_print_numbers(self):
        ms.print_numbers()
        # Explicitly cast sys.stdout to StringIO to resolve the type hint issue
        output = cast(StringIO, sys.stdout).getvalue().strip().split('\n')
        self.assertEqual(len(output), 5)  # Check if 5 lines are printed
        self.assertIn('Number: 5', output[-1])  # Check the last output

    def test_print_letters(self):
        ms.print_letters()
        # Explicitly cast sys.stdout to StringIO to resolve the type hint issue
        output = cast(StringIO, sys.stdout).getvalue().strip().split('\n')
        self.assertEqual(len(output), 5)  # Check if 5 lines are printed
        self.assertIn('Letter: e', output[-1])  # Check the last output


if __name__ == '__main__':
    unittest.main()
