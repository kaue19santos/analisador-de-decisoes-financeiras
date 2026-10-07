# Analisador de Decisões Financeiras

## 1. Sobre o projeto

O **Analisador de Decisões Financeiras** é uma aplicação desenvolvida para o Trabalho 1 da disciplina **Administração Financeira (CAD 167)**.

A aplicação aborda o tema **Valor do Dinheiro no Tempo**, permitindo comparar duas alternativas financeiras que possuem valores e prazos diferentes.

O sistema utiliza conceitos de **Valor Presente (VP), Valor Futuro (VF), taxa de juros, capitalização e desconto** para transformar valores para uma mesma referência temporal e auxiliar na tomada de decisão financeira.

---

## 2. Objetivo

O objetivo da aplicação é determinar qual, entre duas alternativas financeiras, é mais vantajosa considerando o efeito do tempo e da taxa de juros sobre o dinheiro.

A aplicação não realiza apenas cálculos isolados. Ela transforma os valores para uma mesma referência temporal, compara as alternativas e apresenta uma conclusão financeira.

### Exemplo

O usuário pode comparar:

- **Alternativa A:** receber R$ 10.000 hoje;
- **Alternativa B:** receber R$ 12.000 daqui a 2 anos;
- **Taxa de referência:** 8% ao ano.

O sistema calcula o Valor Presente das alternativas e identifica qual possui maior valor financeiro.

---

## 3. Problema que a aplicação resolve

Valores financeiros que acontecem em momentos diferentes não podem ser comparados diretamente sem considerar o valor do dinheiro no tempo.

Por exemplo, receber R$ 10.000 hoje e receber R$ 10.000 daqui a dois anos não representam a mesma situação financeira, pois o dinheiro disponível hoje pode ser aplicado e gerar rendimento.

Dessa forma, a aplicação resolve o problema de **comparar alternativas financeiras que ocorrem em momentos diferentes**, convertendo seus valores para uma mesma referência temporal.

---

## 4. Entradas da aplicação

A aplicação solicita ao usuário os dados necessários para realizar a comparação entre as alternativas financeiras.

### 4.1 Dados gerais

| Entrada | Descrição |
|---|---|
| Taxa de juros | Taxa utilizada como referência |
| Periodicidade | Periodicidade da taxa: mensal ou anual |

O sistema trabalha exclusivamente com **duas alternativas**.

### 4.2 Dados de cada alternativa

| Entrada | Descrição | Exemplo |
|---|---|---|
| Nome | Identificação da alternativa | Receber hoje |
| Valor | Valor financeiro da alternativa | R$ 10.000,00 |
| Prazo | Tempo até o recebimento ou pagamento | 2 |
| Unidade do prazo | Mensal ou anual, igual à periodicidade da taxa | anos |
| Tipo | Recebimento ou pagamento | recebimento |

O sistema exige que a unidade do prazo seja compatível com a periodicidade da taxa informada.

### 4.3 Exemplo de entrada

```text

Taxa (%): 8
Periodicidade (mensal/anual): anual

--- ALTERNATIVA A ---
Nome: Receber hoje
Valor: 10000
Prazo (anual): 0
Tipo (recebimento/pagamento): recebimento

--- ALTERNATIVA B ---
Nome: Receber daqui a 2 anos
Valor: 12000
Prazo (anual): 2
Tipo (recebimento/pagamento): recebimento
```

---

## 5. Cálculos da aplicação

A aplicação utiliza os conceitos de Valor Presente e Valor Futuro para trabalhar com valores financeiros em diferentes momentos.

### 5.1 Valor Presente

O Valor Presente é utilizado para trazer um valor futuro para a data de referência da análise.

Fórmula:

```text
VP = VF / (1 + i)^n
```

Onde:

- **VP** = Valor Presente;
- **VF** = Valor Futuro;
- **i** = taxa de juros por período;
- **n** = número de períodos.

### 5.2 Valor Futuro

O sistema também possui a função de cálculo do Valor Futuro, utilizada para projetar um valor presente para uma data futura.

Fórmula:

```text
VF = VP × (1 + i)^n
```

Onde:

- **VF** = Valor Futuro;
- **VP** = Valor Presente;
- **i** = taxa de juros por período;
- **n** = número de períodos.

Na comparação principal da aplicação, o **Valor Presente** é utilizado como referência.

### 5.3 Diferença absoluta

Após a conversão dos valores, o sistema calcula:

```text
Diferença = |Valor A - Valor B|
```

### 5.4 Diferença percentual

A diferença percentual utiliza a Alternativa A como referência:

```text
Diferença % = ((Valor B - Valor A) / Valor A) × 100
```

### 5.5 Arredondamento

Os cálculos intermediários não são arredondados.

Os resultados apresentados ao usuário utilizam:

- 2 casas decimais para valores monetários;
- 2 casas decimais para percentuais.

Os valores monetários são apresentados no formato brasileiro:

```text
R$ 10.288,33
```

---

## 6. Regra de decisão

A aplicação compara os **Valores Presentes das duas alternativas**, considerando a mesma data de referência.

### Recebimentos

Para recebimentos, a alternativa com o **maior Valor Presente** é considerada mais vantajosa.

### Pagamentos

Para pagamentos, a alternativa com o **menor Valor Presente** é considerada mais vantajosa.

### Compatibilidade entre alternativas

As alternativas precisam possuir o mesmo tipo de operação.

São permitidas:

- Recebimento × Recebimento;
- Pagamento × Pagamento.

Não é permitida:

- Recebimento × Pagamento.

Quando os tipos são diferentes, o sistema informa que as alternativas não podem ser comparadas.

### Data de referência

A data de referência utilizada pelo sistema é o **momento presente (t = 0)**.

Os valores são convertidos para essa referência utilizando:

```text
VP = VF / (1 + i)^n
```

A taxa de juros e o prazo devem possuir a **mesma periodicidade**. O sistema não realiza conversão automática entre mensal e anual.

### Empate

Caso os Valores Presentes sejam iguais, as alternativas são consideradas **financeiramente equivalentes**, considerando a taxa de juros, o prazo e as demais condições informadas.

### Resumo da decisão

| Situação | Regra |
|---|---|
| Recebimento | Maior Valor Presente = melhor alternativa |
| Pagamento | Menor Valor Presente = melhor alternativa |
| Valores equivalentes | Alternativas financeiramente equivalentes |
| Tipos diferentes | Comparação não permitida |

---

## 7. Relatório

Após o processamento, o sistema gera um relatório contendo:

- título da análise;
- data e horário da análise;
- taxa de juros utilizada;
- dados das alternativas;
- tipo da operação;
- prazo;
- valor original;
- fórmula utilizada;
- memória de cálculo;
- Valor Presente de cada alternativa;
- diferença absoluta;
- diferença percentual;
- alternativa mais vantajosa;
- justificativa da decisão.

O relatório é exibido diretamente no terminal após a análise.

O usuário também pode escolher salvar o relatório em um arquivo `.txt`.

Os arquivos são gerados automaticamente com data e horário no nome.

---

## 8. Estrutura do projeto

```text
analisador-decisoes-financeiras/
│
├── README.md
├── main.py
├── calculos.py
├── modelos.py
├── relatorio.py
│
└── testes/
    ├── teste_calculos.py
    ├── teste_decisao.py
    └── teste_entrada.py
```

### Responsabilidade dos arquivos

- **main.py:** entrada de dados, validações e fluxo principal da aplicação.
- **modelos.py:** definição do modelo `Alternativa`.
- **calculos.py:** fórmulas e regras matemáticas da análise financeira.
- **relatorio.py:** geração e salvamento dos relatórios.
- **testes/:** testes automatizados do sistema.

---

## 9. Como executar a aplicação

### Pré-requisito

É necessário ter o **Python 3** instalado.

Para verificar a instalação:

```bash
python --version
```

ou, dependendo do sistema:

```bash
python3 --version
```

### Executar a aplicação

Na pasta raiz do projeto, execute:

```bash
python main.py
```

ou:

```bash
python3 main.py
```

O menu inicial será exibido:

```text
========================================
ANALISADOR DE DECISÕES FINANCEIRAS
========================================
1 - Nova análise
0 - Sair
```

Selecione `1` para iniciar uma análise.

Após informar os dados das duas alternativas, o sistema exibirá o relatório da análise e perguntará se o usuário deseja salvá-lo em um arquivo `.txt`.

---

## 10. Como executar os testes

Na pasta raiz do projeto, execute:

```bash
python -m unittest discover
```

ou:

```bash
python3 -m unittest discover
```

ou 

```bash
python3 -m unittest discover -s testes -p "teste_*.py"
```

Os testes verificam:

- cálculo do Valor Presente;
- cálculo do Valor Futuro;
- diferentes taxas;
- diferentes prazos;
- valores decimais;
- taxa igual a zero;
- valores equivalentes;
- diferença percentual;
- regras de decisão;
- validação de entradas;
- campos vazios;
- valores negativos;
- textos em campos numéricos;

O resultado esperado é a execução dos testes sem falhas, indicando:

```text
OK
```

---

## 11. Documentação e comentários

O código-fonte foi documentado para facilitar a compreensão da aplicação.

Foram adicionadas Docstrings explicativas no início dos módulos, funções e classes.

A documentação apresenta:

- objetivo de cada módulo;
- funcionamento das principais funções;
- fórmulas financeiras utilizadas;
- variáveis importantes;
- regras de decisão;
- validações das entradas;
- funcionamento do relatório.

---

## 12. Conceitos financeiros utilizados

O projeto é fundamentado nos seguintes conceitos:

- Valor do Dinheiro no Tempo;
- Valor Presente;
- Valor Futuro;
- Taxa de juros;
- Capitalização;
- Desconto.