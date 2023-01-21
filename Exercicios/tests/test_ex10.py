import unittest
from Loops import ex10


class MyTestCase(unittest.TestCase):
    def test_fatorial(self):
        self.assertEqual(ex10.fatorial(5), 120)


if __name__ == '__main__':
    unittest.main()
