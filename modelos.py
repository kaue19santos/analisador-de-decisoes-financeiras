from dataclasses import dataclass

@dataclass
class Alternativa:
    nome: str
    valor: float
    prazo: float
    unidade_prazo: str
    tipo: str