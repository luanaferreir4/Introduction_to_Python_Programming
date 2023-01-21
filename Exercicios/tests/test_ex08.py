import unittest
from Loops import ex08


class MyTestCase(unittest.TestCase):
    def test_successful_progressao_aritmetica(self):
        expected_value = [200, 420, 640, 860, 1080, 1300, 1520, 1740, 1960, 2180]
        self.assertEqual(ex08.progressao_aritmetica(200, 220), expected_value)


if __name__ == '__main__':
    unittest.main()
