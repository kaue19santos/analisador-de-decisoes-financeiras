from modelos import Alternativa
from calculos import (
    calcular_valor_presente,
    calcular_diferenca,
    calcular_diferenca_percentual,
    comparar_alternativas,
)


def pedir_texto(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("Entrada inválida. Informe um valor.")


def pedir_numero(mensagem, minimo=0):
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
            if valor >= minimo:
                return valor
        except ValueError:
            pass

        print(f"Informe um número maior ou igual a {minimo}.")


def pedir_opcao(mensagem, opcoes):
    while True:
        valor = input(mensagem).strip().lower()
        if valor in opcoes:
            return valor
        print(f"Opção inválida. Escolha entre: {', '.join(opcoes)}.")

def formatar_moeda(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def pedir_alternativa(nome, periodicidade):
    print(f"\n--- ALTERNATIVA {nome} ---")

    return Alternativa(
        nome=pedir_texto("Nome: "),
        valor=pedir_numero("Valor: ", 0.01),
        prazo=pedir_numero(f"Prazo ({periodicidade}): "),
        unidade_prazo=periodicidade,
        tipo=pedir_opcao(
            "Tipo (recebimento/pagamento): ",
            ["recebimento", "pagamento"],
        ),
    )


def pedir_taxa():
    print("\n--- TAXA DE JUROS ---")
    taxa = pedir_numero("Taxa (%): ")
    periodicidade = pedir_opcao(
        "Periodicidade (mensal/anual): ",
        ["mensal", "anual"]
    )
    return taxa, periodicidade


def exibir_resultado(a, b, vp_a, vp_b, taxa, periodicidade):
    diferenca = calcular_diferenca(vp_a, vp_b)
    diferenca_percentual = calcular_diferenca_percentual(vp_a, vp_b)
    resultado = comparar_alternativas(vp_a, vp_b, a.tipo)

    print("\n" + "=" * 40)
    print("RESULTADO DA ANÁLISE")
    print("=" * 40)
    print(f"\nTaxa utilizada: {taxa:.2%} ao {periodicidade}")

    for alternativa, vp in [(a, vp_a), (b, vp_b)]:
        print(f"""
ALTERNATIVA {alternativa.nome}
Valor original: {formatar_moeda(alternativa.valor)}
Prazo: {alternativa.prazo:g} {alternativa.unidade_prazo}
Valor equivalente: {formatar_moeda(vp)}""")

    print(f"\nDiferença: {formatar_moeda(diferenca)}")
    print(f"Diferença percentual: {diferenca_percentual:.2f}%")

    print("\nDECISÃO:")

    if resultado == "equivalentes":
        print("As alternativas são financeiramente equivalentes.")
        return

    vencedora = a if resultado == "A" else b
    regra = "maior" if a.tipo == "recebimento" else "menor"

    print(f"Alternativa {resultado} ({vencedora.nome}) é mais vantajosa.")
    print(
        f"Justificativa: para {a.tipo}s, a melhor alternativa "
        f"é aquela que apresenta o {regra} valor presente."
    )


def nova_analise():
    taxa, periodicidade = pedir_taxa()

    alternativa_a = pedir_alternativa("A", periodicidade)
    alternativa_b = pedir_alternativa("B", periodicidade)

    if alternativa_a.tipo != alternativa_b.tipo:
        print("\nAs alternativas possuem tipos diferentes e não podem ser comparadas.")
        return

    vp_a = calcular_valor_presente(
        alternativa_a.valor, taxa, alternativa_a.prazo
    )
    vp_b = calcular_valor_presente(
        alternativa_b.valor, taxa, alternativa_b.prazo
    )

    exibir_resultado(
        alternativa_a,
        alternativa_b,
        vp_a,
        vp_b,
        taxa,
        periodicidade,
    )


def menu():
    while True:
        print("\n" + "=" * 40)
        print("ANALISADOR DE DECISÕES FINANCEIRAS")
        print("=" * 40)
        print("1 - Nova análise")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nova_analise()
        elif opcao == "0":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()