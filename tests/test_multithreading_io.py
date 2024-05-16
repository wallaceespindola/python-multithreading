import os
import sys
import threading
import unittest
from io import StringIO
from typing import cast

from python_multithreading import multithreading_io as mio


class TestMultithreadingIO(unittest.TestCase):

    def setUp(self):
        self.original_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = self.original_stdout
        print("Cleanup completed, all threads joined.")  # Debug statement

    def test_read_file(self):
        # Construct the file path
        file_path = os.path.join(os.path.dirname(__file__), '..', 'resources', 'file1.txt')

        # Call the function which reads the file and prints the output
        mio.read_file(file_path)

        # Capture the output
        output = cast(StringIO, sys.stdout).getvalue().strip().split('\n')

        # Expected output line based on your read_file function's print statement
        expected_first_line = "==>name: file1.txt"  # Adjust according to actual content
        expected_output = f"Read from {file_path}: {expected_first_line}"

        # Assertion
        self.assertIn(expected_output, output)

    def test_thread_operations(self):
        # This will test the thread-based execution with real files
        base_path = os.path.join(os.path.dirname(__file__), '..', 'resources')
        files = ["file1.txt", "file2.txt", "file3.txt"]
        threads = []

        # Build the full path for each file and create a thread to read each file
        for filename in files:
            file_path = os.path.join(base_path, filename)  # Construct the full path
            thread = threading.Thread(target=mio.read_file, args=(file_path,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        output = cast(StringIO, sys.stdout).getvalue().strip().split('\n')
        self.assertEqual(len(output), 3)  # Assuming each file read results in one output line
        for i, filename in enumerate(files):
            full_path = os.path.join(base_path, filename)  # This is the full path used in the output
            # Assuming each file starts with "==>name: xxxx.txt"
            # file.split('/'): This splits the string stored in file at each slash (/).
            # The result is a list of all the components in the file path.
            # For example, "resources/file1.txt" would be split into ["resources", "file1.txt"].
            # file.split('/')[-1]: The [-1] accesses the last element of the list produced by split.
            # This is typically used to get the last part of the path, which is the filename.
            # In the example, it would be "file1.txt".
            extracted_filename = filename.split('/')[-1]  # getting the file name
            expected_first_line = f"==>name: {extracted_filename}"
            expected_output = f"Read from {full_path}: {expected_first_line}"
            self.assertIn(expected_output, output[i])


if __name__ == '__main__':
    unittest.main()
