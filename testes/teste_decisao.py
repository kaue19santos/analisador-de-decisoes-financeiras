import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculos import comparar_alternativas

class TestDecisao(unittest.TestCase):
    def test_alternativa_a_melhor(self):
        """Testar Alternativa A melhor"""
        # Recebimento: A(1000) > B(900)
        self.assertEqual(comparar_alternativas(1000, 900, "recebimento"), "A")
        # Pagamento: A(900) < B(1000)
        self.assertEqual(comparar_alternativas(900, 1000, "pagamento"), "A")
        
    def test_alternativa_b_melhor(self):
        """Testar Alternativa B melhor"""
        # Recebimento: A(900) < B(1000)
        self.assertEqual(comparar_alternativas(900, 1000, "recebimento"), "B")
        # Pagamento: A(1000) > B(900)
        self.assertEqual(comparar_alternativas(1000, 900, "pagamento"), "B")
        
    def test_alternativas_equivalentes(self):
        """Testar Alternativas equivalentes"""
        self.assertEqual(comparar_alternativas(1000, 1000, "recebimento"), "equivalentes")
        self.assertEqual(comparar_alternativas(1000, 1000, "pagamento"), "equivalentes")

if __name__ == '__main__':
    unittest.main()
