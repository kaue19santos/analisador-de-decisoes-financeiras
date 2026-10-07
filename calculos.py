import math

"""
Módulo de Cálculos Financeiros
Objetivo: Encapsular toda a lógica matemática e financeira responsável por calcular o valor do dinheiro no tempo, 
bem como calcular diferenças (absolutas e percentuais) e determinar a melhor alternativa com base nas regras de negócio.
"""

def calcular_valor_presente(valor_futuro, taxa, periodos):
    """
    Calcula o Valor Presente (VP) de uma quantia futura, aplicando desconto financeiro.
    
    Fórmula utilizada: VP = VF / (1 + i)^n
    Onde:
    - VF (valor_futuro): O valor monetário da alternativa na data futura.
    - i (taxa): A taxa de juros a ser utilizada no desconto, em formato decimal (ex: 0.08 para 8%).
    - n (periodos): O número de períodos até o fluxo de caixa ocorrer.
    
    Retorna o valor equivalente descapitalizado na data de referência (t = 0).
    """
    return valor_futuro / (1 + taxa) ** periodos


def calcular_valor_futuro(valor_presente, taxa, periodos):
    """
    Calcula o Valor Futuro (VF) de uma quantia presente, aplicando capitalização.
    
    Fórmula utilizada: VF = VP * (1 + i)^n
    (Esta função não está sendo ativamente utilizada na comparação principal atual, 
    que prioriza o VP, mas existe para extensões futuras do analisador)
    """
    return valor_presente * (1 + taxa) ** periodos


def calcular_diferenca(valor_a, valor_b):
    """
    Calcula a diferença financeira absoluta entre os valores equivalentes das duas alternativas.
    Útil para mostrar ao usuário quanto uma opção é monetariamente superior à outra.
    """
    return abs(valor_a - valor_b)


def calcular_diferenca_percentual(valor_a, valor_b):
    """
    Calcula a diferença percentual de valor_b em relação a valor_a.
    Permite visualizar a diferença de proporção entre as escolhas.
    """
    return ((valor_b - valor_a) / valor_a) * 100


def comparar_alternativas(valor_a, valor_b, tipo):
    """
    Determina a alternativa mais vantajosa aplicando as Regras de Decisão Financeiras.
    
    Regra de Decisão:
    1. Se as alternativas possuem valores descapitalizados iguais, são 'equivalentes'.
    2. Se a operação for um 'recebimento': 
       A melhor alternativa é a que tem o MAIOR Valor Presente (maximiza o ganho).
    3. Se a operação for um 'pagamento': 
       A melhor alternativa é a que tem o MENOR Valor Presente (minimiza a perda/saída).
       
    Retorna:
    - 'equivalentes' se os valores são iguais.
    - 'A' se a primeira alternativa for a vencedora.
    - 'B' se a segunda alternativa for a vencedora.
    """
    if math.isclose(valor_a, valor_b, rel_tol=1e-9):
        return "equivalentes"

    if tipo == "recebimento":
        return "A" if valor_a > valor_b else "B"

    return "A" if valor_a < valor_b else "B"