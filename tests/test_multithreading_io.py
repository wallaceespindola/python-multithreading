import sys
import threading
import unittest
from io import StringIO
from typing import cast

from python_multithreading import multithreading_io as mio


class TestMultithreadingIO(unittest.TestCase):
    def setUp(self):
        # Redirect stdout to capture print statements
        self.held_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        # Reset stdout after each test method
        sys.stdout = self.held_stdout

    def test_read_file(self):
        # Test reading from a real file
        file_path = "../resources/file1.txt"
        mio.read_file(file_path)
        output = cast(StringIO, sys.stdout).getvalue().strip().split('\n')
        expected_first_line = "==>name: file1.txt"  # Adjust according to actual content
        self.assertIn(f"Read from {file_path}: {expected_first_line}", output[0])

    def test_thread_operations(self):
        # This will test the thread-based execution with real files
        files = ["../resources/file1.txt", "../resources/file2.txt", "../resources/file3.txt"]
        threads = []

        for file in files:
            thread = threading.Thread(target=mio.read_file, args=(file,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        output = cast(StringIO, sys.stdout).getvalue().strip().split('\n')
        self.assertEqual(len(output), 3)  # Assuming each file read results in one output line
        for i, file in enumerate(files):
            # Assuming each file starts with "==>name: xxxx.txt"
            # file.split('/'): This splits the string stored in file at each slash (/).
            # The result is a list of all the components in the file path. For example, "resources/file1.txt"
            # would be split into ["resources", "file1.txt"].
            # file.split('/')[-1]: The [-1] accesses the last element of the list produced by split.
            # This is typically used to get the last part of the path, which is the filename.
            # In the example, it would be "file1.txt".
            expected_first_line = f"==>name: {file.split('/')[-1]}"  # getting file name
            self.assertIn(f"Read from {file}: {expected_first_line}", output[i])


if __name__ == '__main__':
    unittest.main()
