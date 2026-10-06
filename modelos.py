"""
Módulo de Modelos de Dados
Objetivo: Define as estruturas de dados fundamentais utilizadas pelo Analisador de Decisões Financeiras.
"""

from dataclasses import dataclass

@dataclass
class Alternativa:
    """
    Representa uma alternativa financeira a ser analisada e comparada.

    Atributos:
    - nome (str): Identificação da alternativa (ex: 'Receber hoje').
    - valor (float): O valor financeiro nominal (futuro ou presente) associado à alternativa.
    - prazo (float): Tempo até a ocorrência da alternativa (se for 0, ocorre hoje).
    - unidade_prazo (str): Unidade de tempo do prazo ('mensal' ou 'anual').
    - tipo (str): Natureza da operação, podendo ser 'recebimento' (entrada de caixa) ou 'pagamento' (saída de caixa).
    """
    nome: str
    valor: float
    prazo: float
    unidade_prazo: str
    tipo: str