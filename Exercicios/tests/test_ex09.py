import unittest
from Loops import ex09


class MyTestCase(unittest.TestCase):
    def test_successful_progressao_geometrica(self):
        expected_value = [2, 10, 50, 250, 1250, 6250, 31250, 156250, 781250, 3906250]
        self.assertEqual(ex09.progressao_geometrica(2, 5), expected_value)


if __name__ == '__main__':
    unittest.main()
