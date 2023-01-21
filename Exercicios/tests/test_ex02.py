import unittest
from Loops import ex02


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.lista = [1.52, 1.28, 1.77, 1.78]

    def test_successful_maior_menor_altura(self):
        maior_menor_altura_esperada = {'maior altura': 1.78, 'menor altura': 1.28}
        self.assertEqual(ex02.maior_menor_altura(self.lista), maior_menor_altura_esperada)


if __name__ == '__main__':
    unittest.main()
