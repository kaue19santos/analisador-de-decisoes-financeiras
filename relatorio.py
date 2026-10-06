"""
Módulo de Relatórios
Objetivo: Gerar e exibir a saída formatada contendo todas as análises, cálculos parciais e conclusões,
bem como persistir (salvar) esses dados em arquivos de texto se o usuário desejar (Etapa 5).
"""

import datetime
from calculos import (
    calcular_diferenca,
    calcular_diferenca_percentual,
    comparar_alternativas,
)

def formatar_moeda(valor):
    """
    Formata um valor numérico flutuante em uma string de representação monetária brasileira.
    Exemplo: 1234.56 vira 'R$ 1.234,56'
    """
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def gerar_relatorio(a, b, vp_a, vp_b, taxa, periodicidade):
    """
    Gera o texto completo do relatório com as seguintes seções estruturadas:
    - Título e Data da Análise
    - Taxa utilizada
    - Dados originais das Alternativas A e B
    - A memória de cálculo documentando as fórmulas utilizadas
    - Diferença (absoluta e percentual)
    - A conclusão clara de qual é a alternativa mais vantajosa (Regra de decisão)
    """
    diferenca = calcular_diferenca(vp_a, vp_b)
    diferenca_percentual = calcular_diferenca_percentual(vp_a, vp_b)
    resultado = comparar_alternativas(vp_a, vp_b, a.tipo)
    
    data_analise = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    linhas = [
        "=" * 50,
        "RELATÓRIO DE ANÁLISE DE DECISÃO FINANCEIRA",
        "=" * 50,
        f"Data da análise: {data_analise}",
        "",
        f"Taxa de juros utilizada: {taxa:.2%} ao {periodicidade}",
        "",
        "--- DADOS DAS ALTERNATIVAS ---"
    ]
    
    for alternativa in [a, b]:
        linhas.append(f"\nALTERNATIVA {alternativa.nome}")
        linhas.append(f"Tipo: {alternativa.tipo.capitalize()}")
        linhas.append(f"Valor original: {formatar_moeda(alternativa.valor)}")
        linhas.append(f"Prazo: {alternativa.prazo:g} {alternativa.unidade_prazo}")
    
    linhas.append("\n--- CÁLCULOS DOS VALORES PRESENTES ---")
    linhas.append("Fórmula utilizada: VP = VF / (1 + i)^n")
    for alternativa, vp in [(a, vp_a), (b, vp_b)]:
        linhas.append(f"\nAlternativa {alternativa.nome}:")
        linhas.append(f"Cálculo: VP = {alternativa.valor:.2f} / (1 + {taxa:.4f})^{alternativa.prazo:g}")
        linhas.append(f"Valor Presente Equivalente: {formatar_moeda(vp)}")
        
    linhas.append("\n--- COMPARAÇÃO ---")
    linhas.append(f"Diferença absoluta: {formatar_moeda(diferenca)}")
    linhas.append(f"Diferença percentual: {diferenca_percentual:.2f}%")
    
    linhas.append("\n--- CONCLUSÃO ---")
    if resultado == "equivalentes":
        linhas.append("As alternativas são financeiramente equivalentes.")
    else:
        vencedora = a if resultado == "A" else b
        regra = "maior" if a.tipo == "recebimento" else "menor"
        linhas.append(f"A Alternativa {resultado} ({vencedora.nome}) é mais vantajosa.")
        linhas.append(f"Justificativa: Para {a.tipo}s, a melhor alternativa é aquela que")
        linhas.append(f"apresenta o {regra} valor presente na data de referência.")
    
    linhas.append("=" * 50)
    
    return "\n".join(linhas)

def salvar_relatorio(conteudo):
    """
    Grava o conteúdo textual do relatório finalizado em um arquivo (.txt) na pasta raiz do projeto.
    O nome do arquivo é gerado de forma única, com base na data e hora atuais.
    Utiliza encoding utf-8 para preservar a acentuação e formatação (ex: 'R$').
    """
    nome_arquivo = f"relatorio_analise_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            f.write(conteudo)
        print(f"\nRelatório salvo com sucesso no arquivo: {nome_arquivo}")
    except Exception as e:
        print(f"\nErro ao salvar o relatório: {e}")

