import unittest
from Loops import ex01


class MyTestCase(unittest.TestCase):
    def test_successful_soma_impares_mult_3(self):
        self.assertEqual(ex01.soma_impares_mult_3(1, 10), 12)


if __name__ == '__main__':
    unittest.main()
