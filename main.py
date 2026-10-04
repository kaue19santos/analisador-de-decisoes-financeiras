from modelos import Alternativa


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


def pedir_alternativa(nome):
    print(f"\n--- ALTERNATIVA {nome} ---")

    return Alternativa(
        nome=pedir_texto("Nome: "),
        valor=pedir_numero("Valor: ", 0.01),
        prazo=pedir_numero("Prazo: "),
        unidade_prazo=pedir_opcao("Unidade (meses/anos): ", ["meses", "anos"]),
        tipo=pedir_opcao(
            "Tipo (recebimento/pagamento): ",
            ["recebimento", "pagamento"]
        )
    )


def pedir_taxa():
    print("\n--- TAXA DE JUROS ---")
    taxa = pedir_numero("Taxa (%): ")
    periodicidade = pedir_opcao(
        "Periodicidade (mensal/anual): ",
        ["mensal", "anual"]
    )
    return taxa, periodicidade


def menu():
    while True:
        print("\n" + "=" * 40)
        print("ANALISADOR DE DECISÕES FINANCEIRAS")
        print("=" * 40)
        print("1 - Nova análise")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            alternativa_a = pedir_alternativa("A")
            alternativa_b = pedir_alternativa("B")
            taxa, periodicidade = pedir_taxa()

            print("\nDados recebidos com sucesso.")
            print(alternativa_a)
            print(alternativa_b)
            print(f"Taxa: {taxa}% ao {periodicidade}")

        elif opcao == "0":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()