import unittest
from Loops import ex05


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.lista = [10, 3, 1, 2]
        self.lista_error = [0, 1, 2]

    def test_successful_quantidade_pares_impares(self):
        self.assertEqual(ex05.quantidade_pares_impares(self.lista), {'pares': 2, 'ímpares': 2})

    def test_unsuccessful_quantidade_pares_impares(self):
        def error():
            ex05.quantidade_pares_impares(self.lista_error)

        self.assertRaises(Exception, error, msg='Apenas aceitamos números maiores que 0.')
        # Quero lançar uma exceção Exception para isso chamo error que vai afirmar que o que vai acontecer
        # é um erro e a mensagem pode ser como a de 'msg'.

    def test_successful_media_valores_pares(self):
        self.assertEqual(ex05.media_valores_pares(self.lista), 6.0)

    def test_unsuccessful_media_valores_pares(self):
        def error():
            ex05.media_valores_pares(self.lista_error)

        self.assertRaises(Exception, error, msg='Apenas aceitamos números maiores que 0.')

    def test_successful_media_geral(self):
        self.assertEqual(ex05.media_geral(self.lista), 4.0)

    def test_unsuccessful_media_geral(self):
        def error():
            ex05.media_geral(self.lista_error)

        self.assertRaises(Exception, error, msg='Apenas aceitamos números maiores que 0.')


if __name__ == '__main__':
    unittest.main()
