import unittest
from Loops import ex07
from Loops.ex07 import expected


class MyTestCase(unittest.TestCase):
    def test_successful_tabuada(self):
        num = 10
        self.assertEqual(ex07.tabuada(num), expected)
# corrigir!


if __name__ == '__main__':
    unittest.main()
