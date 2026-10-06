"""
Módulo Principal (Main)
Objetivo: Ponto de entrada (Entrypoint) da aplicação.
Gerencia a interação com o usuário via terminal, capturando e validando as entradas, 
orquestrando o fluxo das análises financeiras e as exibições dos resultados/relatórios.
"""

from modelos import Alternativa
from calculos import calcular_valor_presente
from relatorio import gerar_relatorio, salvar_relatorio


def pedir_texto(mensagem):
    """
    Função auxiliar para capturar entrada de texto.
    Valida se o usuário não deixou o campo em branco.
    """
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("Entrada inválida. Informe um valor.")


def pedir_numero(mensagem, minimo=0):
    """
    Função auxiliar para capturar entrada numérica (floats).
    - Substitui vírgulas por pontos, permitindo padrão BR.
    - Garante que a entrada seja um número e maior ou igual ao parâmetro 'minimo'.
    """
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
            if valor >= minimo:
                return valor
        except ValueError:
            pass

        print(f"Informe um número maior ou igual a {minimo}.")


def pedir_opcao(mensagem, opcoes):
    """
    Função auxiliar para capturar uma escolha a partir de uma lista fechada.
    Validação: Permite apenas as respostas predefinidas, forçando repetição em caso de erro.
    """
    while True:
        valor = input(mensagem).strip().lower()
        if valor in opcoes:
            return valor
        print(f"Opção inválida. Escolha entre: {', '.join(opcoes)}.")


def pedir_alternativa(nome, periodicidade):
    """
    Guia o usuário no preenchimento de todos os dados necessários para montar o objeto Alternativa.
    Valida as regras de negócio: O valor não pode ser negativo ou nulo, o prazo precisa ser preenchido
    e o tipo da operação só aceita as strings restritas ("recebimento" ou "pagamento").
    """
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
    """
    Captura e valida a Taxa de Juros global utilizada na Análise.
    Retorna a taxa (float) e a periodicidade escolhida.
    """
    print("\n--- TAXA DE JUROS ---")
    taxa = pedir_numero("Taxa (%): ")
    periodicidade = pedir_opcao(
        "Periodicidade (mensal/anual): ",
        ["mensal", "anual"]
    )
    return taxa, periodicidade


def nova_analise():
    """
    Função core que orquestra a execução da análise.
    Passos:
    1. Captura a taxa base.
    2. Captura os dados das Alternativas A e B.
    3. Verifica se são da mesma natureza (ambos recebimentos ou ambos pagamentos).
    4. Chama o módulo de cálculos para descapitalizar os valores ao t=0 (Valor Presente).
    5. Passa os valores para o módulo de relatórios para formatar e exibir na tela.
    6. Permite que o usuário salve a análise.
    """
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

    conteudo_relatorio = gerar_relatorio(
        alternativa_a,
        alternativa_b,
        vp_a,
        vp_b,
        taxa,
        periodicidade,
    )
    
    print("\n" + conteudo_relatorio)
    
    salvar = pedir_opcao("\nDeseja salvar este relatório em um arquivo texto? (s/n): ", ["s", "n"])
    if salvar == "s":
        salvar_relatorio(conteudo_relatorio)


def menu():
    """
    Loop principal do programa. Responsável por exibir opções iniciais e permitir que o usuário faça 
    múltiplas análises sem reiniciar a aplicação, ou encerre de forma controlada.
    """
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