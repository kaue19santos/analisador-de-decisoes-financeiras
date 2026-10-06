import unittest
from unittest.mock import patch
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import pedir_texto, pedir_numero, pedir_quantidade_alternativas

class TestEntradas(unittest.TestCase):
    
    @patch('builtins.input', side_effect=['', '   ', 'Texto Válido'])
    def test_campo_vazio(self, mock_input):
        """Testar campo vazio"""
        # Vai falhar 2 vezes nas entradas vazias/brancas, e aceitar a terceira
        resultado = pedir_texto("Mensagem: ")
        self.assertEqual(resultado, "Texto Válido")
        self.assertEqual(mock_input.call_count, 3)

    @patch('builtins.input', side_effect=['abc', 'xyz', '10.5'])
    def test_texto_onde_deveria_ser_numero(self, mock_input):
        """Testar Texto onde deveria ser número"""
        # Vai ignorar os ValueError e pegar o '10.5'
        resultado = pedir_numero("Valor: ")
        self.assertEqual(resultado, 10.5)
        self.assertEqual(mock_input.call_count, 3)

    @patch('builtins.input', side_effect=['-5', '-10.5', '100'])
    def test_valor_negativo(self, mock_input):
        """Testar Valor negativo"""
        # A função pedir_numero com minimo=0 deve rejeitar os negativos
        resultado = pedir_numero("Valor: ", minimo=0)
        self.assertEqual(resultado, 100.0)
        self.assertEqual(mock_input.call_count, 3)

    @patch('builtins.input', side_effect=['-2', 'abc', '12'])
    def test_prazo_invalido(self, mock_input):
        """Testar Prazo inválido"""
        # Prazo exige minimo 0
        resultado = pedir_numero("Prazo: ", minimo=0)
        self.assertEqual(resultado, 12.0)
        self.assertEqual(mock_input.call_count, 3)

    @patch('builtins.input', side_effect=['-1', 'texto', '8.5'])
    def test_taxa_invalida(self, mock_input):
        """Testar Taxa inválida"""
        # Taxa exige minimo 0
        resultado = pedir_numero("Taxa: ", minimo=0)
        self.assertEqual(resultado, 8.5)
        self.assertEqual(mock_input.call_count, 3)

    @patch('builtins.input', side_effect=['3', '1', 'a', '2'])
    def test_quantidade_invalida_de_alternativas(self, mock_input):
        """Testar Quantidade inválida de alternativas"""
        # Deve rejeitar números diferentes de 2
        resultado = pedir_quantidade_alternativas()
        self.assertEqual(resultado, 2)
        # 3 (inválido), 1 (inválido), 'a' (ValueError handled in pedir_numero), 2 (válido)
        self.assertEqual(mock_input.call_count, 4)

if __name__ == '__main__':
    unittest.main()
