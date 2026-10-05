def calcular_valor_presente(valor_futuro, taxa, periodos):
    return valor_futuro / (1 + taxa) ** periodos


def calcular_valor_futuro(valor_presente, taxa, periodos):
    return valor_presente * (1 + taxa) ** periodos


def calcular_diferenca(valor_a, valor_b):
    return abs(valor_a - valor_b)


def calcular_diferenca_percentual(valor_a, valor_b):
    return ((valor_b - valor_a) / valor_a) * 100


def comparar_alternativas(valor_a, valor_b, tipo):
    if valor_a == valor_b:
        return "equivalentes"

    if tipo == "recebimento":
        return "A" if valor_a > valor_b else "B"

    return "A" if valor_a < valor_b else "B"