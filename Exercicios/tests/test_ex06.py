import unittest
from Loops import ex06


class MyTestCase(unittest.TestCase):
    def test_impares(self):
        self.assertEqual(ex06.impares(10, 20), [11, 13, 15, 17, 19])


if __name__ == '__main__':
    unittest.main()
