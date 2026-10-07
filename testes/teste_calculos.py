import unittest
import sys
import os

# Adiciona o diretório pai ao sys.path para conseguir importar os módulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculos import (
    calcular_valor_presente,
    calcular_valor_futuro,
    calcular_diferenca,
    calcular_diferenca_percentual,
    comparar_alternativas
)

class TestCalculosFinanceiros(unittest.TestCase):
    
    def test_valor_presente(self):
        """Testar Valor Presente"""
        # VF = 1100, taxa = 10% (0.1), periodo = 1 -> VP deve ser 1000
        vp = calcular_valor_presente(1100, 0.10, 1)
        self.assertAlmostEqual(vp, 1000.0, places=2)
        
    def test_valor_futuro(self):
        """Testar Valor Futuro"""
        # VP = 1000, taxa = 10% (0.1), periodo = 1 -> VF deve ser 1100
        vf = calcular_valor_futuro(1000, 0.10, 1)
        self.assertAlmostEqual(vf, 1100.0, places=2)
        
    def test_diferentes_taxas(self):
        """Testar diferentes taxas"""
        # Testando com taxa de 5% e 15%
        vp_taxa_baixa = calcular_valor_presente(1000, 0.05, 1) # 1000 / 1.05 = 952.38
        vp_taxa_alta = calcular_valor_presente(1000, 0.15, 1)  # 1000 / 1.15 = 869.565...
        self.assertAlmostEqual(vp_taxa_baixa, 952.38, places=2)
        self.assertAlmostEqual(vp_taxa_alta, 869.57, places=2)
        
    def test_diferentes_prazos(self):
        """Testar diferentes prazos"""
        # Testando no prazo 1 e prazo 10
        vp_curto = calcular_valor_presente(1000, 0.10, 1)   # 909.09
        vp_longo = calcular_valor_presente(1000, 0.10, 10)  # 1000 / (1.1^10) = 385.54
        self.assertAlmostEqual(vp_curto, 909.09, places=2)
        self.assertAlmostEqual(vp_longo, 385.54, places=2)
        
    def test_valores_decimais(self):
        """Testar valores decimais"""
        # Valores quebrados para garantir a precisão de float
        vp = calcular_valor_presente(1234.56, 0.085, 3) # 1234.56 / (1.085^3) = 966.547...
        self.assertAlmostEqual(vp, 966.55, places=2)
        
        vf = calcular_valor_futuro(966.547, 0.085, 3)
        self.assertAlmostEqual(vf, 1234.56, places=2)
        
    def test_taxa_zero(self):
        """Testar taxa igual a zero"""
        # Com taxa 0, o VP e o VF devem ser iguais ao valor original
        vp = calcular_valor_presente(1000, 0.0, 5)
        self.assertEqual(vp, 1000.0)
        
        vf = calcular_valor_futuro(1000, 0.0, 5)
        self.assertEqual(vf, 1000.0)
        
    def test_valores_iguais(self):
        """Testar valores iguais (Diferença zero, e comparação 'equivalentes')"""
        # Se as duas alternativas tem o mesmo valor presente
        vp_a = 500.0
        vp_b = 500.0
        
        # Testando diferença (deve ser 0)
        diff = calcular_diferenca(vp_a, vp_b)
        self.assertEqual(diff, 0.0)
        
        # Testando comparação (deve ser equivalentes)
        resultado = comparar_alternativas(vp_a, vp_b, "recebimento")
        self.assertEqual(resultado, "equivalentes")

    def test_diferenca_percentual(self):
        resultado = calcular_diferenca_percentual(100, 120)
        self.assertEqual(resultado, 20.0)

if __name__ == '__main__':
    unittest.main()
