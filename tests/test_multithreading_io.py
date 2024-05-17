import os
import sys
import threading
import unittest
from io import StringIO
from typing import cast

from python_multithreading import multithreading_io as mt


class TestMultithreadingIO(unittest.TestCase):

    def setUp(self):
        # Redirect stdout to capture print statements
        self.original_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        # Reset stdout after each test method
        sys.stdout = self.original_stdout
        print("Cleanup completed, all threads joined.")  # Debug statement

    def test_read_file(self):
        # Construct the file path
        file_path = os.path.join(os.path.dirname(__file__), '..', 'resources', 'file1.txt')

        # Call the function which reads the file and prints the output
        mt.read_file(file_path)

        # Capture the output
        output = cast(StringIO, sys.stdout).getvalue()

        # Expected output line based on your read_file function's print statement
        expected_first_line = "This is file1.txt"

        # Check if any line in the output starts with the expected output
        self.assertIn(expected_first_line, output)

    def test_thread_operations(self):

        # Set up file paths and threads
        base_path = os.path.join(os.path.dirname(__file__), '..', 'resources')
        files = ["file1.txt", "file2.txt", "file3.txt"]
        threads = []

        # Create and start a thread for each file
        for filename in files:
            file_path = os.path.join(base_path, filename)
            thread = threading.Thread(target=mt.read_file, args=(file_path,))
            threads.append(thread)
            thread.start()

        # Wait for all threads to finish
        for thread in threads:
            thread.join()

        # Capture the output and split into lines
        output = cast(StringIO, sys.stdout).getvalue().strip().split('\n')

        # Check the number of output lines
        self.assertEqual(len(output), 3)

        # Check that each output line contains the expected text
        for line in output:
            self.assertRegex(line, r"This is file\d\.txt")


if __name__ == '__main__':
    unittest.main()
