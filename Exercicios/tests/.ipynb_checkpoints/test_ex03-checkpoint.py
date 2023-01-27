import unittest
from Loops import ex03


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.valores = [-1, 2, 3, 2]

    def test_successful_media_aritmetica(self):
        self.assertEqual(ex03.media_aritmetica(self.valores), {'Media aritmetica': 1.5})

    def test_successful_quantidade_positivos_negativos(self):
        expected_value = {'Quantidade de valores positivos': 3, 'Quantidade de valores negativos': 1}
        self.assertEqual(ex03.quantidade_positivos_negativos(self.valores), expected_value)

    def test_successful_percentual_valores_negativos_positivos(self):
        expected_value = {'Percentual de valores positivos': 75.0, 'Percentual de valores negativos': 25.0}
        self.assertEqual(ex03.percentual_valores_negativos_positivos(self.valores), expected_value)


if __name__ == '__main__':
    unittest.main()
