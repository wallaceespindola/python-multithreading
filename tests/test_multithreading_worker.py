import sys
import unittest
from io import StringIO
from typing import cast

from python_multithreading import multithreading_worker as mt


class TestThreadPoolWorker(unittest.TestCase):

    def setUp(self):
        # Redirect stdout to capture print statements
        self.original_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        # Reset stdout after each test method
        sys.stdout = self.original_stdout

    def test_run_workers(self):
        mt.run_workers()
        # Explicitly cast sys.stdout to StringIO to resolve the type hint issue
        output = cast(StringIO, sys.stdout).getvalue().strip().split('\n')
        self.assertEqual(len(output), 3)  # Check if 5 lines are printed
        self.assertIn('Worker thread running', output[0])  # Check first worker output
        self.assertIn('Worker thread running', output[1])  # Check second worker output
        self.assertIn('Main thread continuing to run', output[-1])  # Check the last output


if __name__ == '__main__':
    unittest.main()
