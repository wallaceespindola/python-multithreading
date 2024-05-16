import unittest

from python_multithreading.main_module import add


class TestMainModule(unittest.TestCase):

    def test_add(self):
        """Test the add function with various inputs."""
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(1.5, 2.5), 4.0)


if __name__ == "__main__":
    unittest.main()
