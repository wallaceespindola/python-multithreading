import unittest

from python_multithreading import multithreading_worker_counter as mt


class TestThreadPoolWorkerCounter(unittest.TestCase):

    def test_run_workers(self):
        counter = mt.run_workers()
        self.assertEqual(counter, 2000000)  # 2 workers * 1.000.000 increments each


if __name__ == '__main__':
    unittest.main()
