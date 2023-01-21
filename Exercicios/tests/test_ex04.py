import unittest
from Loops import ex04


class MyTestCase(unittest.TestCase):
    def test_successful_entre_intervalos(self):
        expected_value = {'0-25': 1, '26-50': 0, '51-75': 0, '76-100': 3}
        self.assertEqual(ex04.entre_intervalos([76, 100, 100, 1]), expected_value)


if __name__ == '__main__':
    unittest.main()
