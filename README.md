# Analisador de Decisões Financeiras

## 1. Sobre o projeto

O **Analisador de Decisões Financeiras** é uma aplicação desenvolvida para o Trabalho 1 da disciplina **Administração Financeira (CAD 167)**.

A aplicação aborda o tema **Valor do Dinheiro no Tempo**, permitindo comparar alternativas financeiras que possuem valores e prazos diferentes.

O sistema utiliza conceitos de **Valor Presente (VP), Valor Futuro (VF), taxa de juros, capitalização e desconto** para transformar as alternativas para uma mesma referência temporal e auxiliar na tomada de decisão financeira.

---

## 2. Objetivo

O objetivo da aplicação é auxiliar o usuário a determinar qual, entre duas alternativas financeiras, é mais vantajosa considerando o efeito do tempo e da taxa de juros sobre o dinheiro.

A aplicação não pretende apenas realizar cálculos isolados, mas utilizar esses cálculos para **comparar alternativas e apresentar uma conclusão financeira**.

### Exemplo

O usuário pode comparar:

* **Alternativa A:** receber R$ 10.000 hoje;
* **Alternativa B:** receber R$ 12.000 daqui a 2 anos;
* **Taxa de referência:** 8% ao ano.

O sistema calcula o valor equivalente das alternativas em uma mesma data e apresenta qual possui maior valor financeiro.

---

## 3. Problema que a aplicação resolve

Valores financeiros que acontecem em momentos diferentes não podem ser comparados diretamente sem considerar o valor do dinheiro no tempo.

Por exemplo, receber R$ 10.000 hoje e receber R$ 10.000 daqui a dois anos não representam a mesma situação financeira, pois o dinheiro disponível hoje pode ser aplicado e gerar rendimento.

Dessa forma, a aplicação resolve o problema de **comparar alternativas financeiras que ocorrem em momentos diferentes**, convertendo seus valores para uma mesma referência temporal.

---

## 4. Entradas da Aplicação

A aplicação solicitará ao usuário os dados necessários para realizar a comparação entre as alternativas financeiras.

### 4.1 Dados gerais da análise

| Entrada                    | Descrição                                     |
| -------------------------- | --------------------------------------------- |
| Quantidade de alternativas | Número de alternativas que serão comparadas   |
| Taxa de juros              | Taxa utilizada como referência para a análise |

Na primeira versão, o sistema trabalhará com **duas alternativas**.

### 4.2 Dados de cada alternativa

Para cada alternativa, o usuário deverá informar:

| Entrada          | Descrição                                  | Exemplo      |
| ---------------- | ------------------------------------------ | ------------ |
| Nome             | Identificação da alternativa               | Receber hoje |
| Valor            | Valor financeiro da alternativa            | R$ 10.000,00 |
| Prazo            | Tempo até o recebimento ou pagamento       | 2            |
| Unidade do prazo | Unidade utilizada para representar o prazo | Anos         |
| Tipo             | Natureza da operação                       | Recebimento  |

### 4.3 Exemplo de entrada

```text
Quantidade de alternativas: 2

Taxa de juros: 8% ao ano

Alternativa 1
Nome: Receber hoje
Valor: R$ 10.000,00
Prazo: 0
Unidade: anos
Tipo: Recebimento

Alternativa 2
Nome: Receber daqui a 2 anos
Valor: R$ 12.000,00
Prazo: 2
Unidade: anos
Tipo: Recebimento
```

---

## 5. Cálculos da Aplicação

A aplicação utilizará os conceitos de Valor Presente e Valor Futuro para transformar e comparar valores financeiros que ocorrem em diferentes momentos.

### 5.1 Valor Presente

Será utilizado quando uma alternativa possuir um valor futuro que precise ser convertido para a data de referência da análise.

Fórmula:

VP = VF / (1 + i)^n

Onde:

* VP = Valor Presente;
* VF = Valor Futuro;
* i = taxa de juros por período;
* n = número de períodos.

### 5.2 Valor Futuro

Será utilizado quando for necessário projetar um valor presente para uma data futura.

Fórmula:

VF = VP × (1 + i)^n

Onde:

* VF = Valor Futuro;
* VP = Valor Presente;
* i = taxa de juros por período;
* n = número de períodos.

### 5.3 Utilização dos cálculos

Para a comparação principal da aplicação, os valores das alternativas serão convertidos para uma mesma data de referência, priorizando o cálculo do Valor Presente.

### 5.4 Diferença absoluta

Após a conversão dos valores, o sistema calculará a diferença absoluta:

Diferença = |Valor A - Valor B|

O resultado será apresentado em reais.

### 5.5 Diferença percentual

A aplicação também calculará a diferença percentual entre as alternativas, utilizando a Alternativa A como referência:

Diferença % = ((Valor B - Valor A) / Valor A) × 100

### 5.6 Arredondamento

Os cálculos intermediários não serão arredondados.

Os resultados apresentados ao usuário serão formatados com:

* 2 casas decimais para valores monetários;
* 2 casas decimais para percentuais.

Os valores monetários serão apresentados no formato brasileiro, por exemplo:

R$ 10.288,33

---

## 6. Regra de Decisão

A aplicação determinará a alternativa mais vantajosa com base nos **valores equivalentes calculados na mesma data de referência**, utilizando a taxa de juros e o prazo informados pelo usuário.

Antes da comparação, as alternativas serão convertidas para uma mesma data de referência, permitindo comparar valores que ocorrem em momentos diferentes.

### Regra de decisão

A regra de decisão dependerá do tipo da operação:

* Para **recebimentos**, será considerada mais vantajosa a alternativa que apresentar o **maior Valor Presente**.
* Para **pagamentos**, será considerada mais vantajosa a alternativa que apresentar o **menor Valor Presente**.

### Compatibilidade entre alternativas

Para garantir uma comparação financeiramente coerente, as alternativas comparadas deverão possuir o mesmo tipo de operação.

São permitidas:

* Recebimento × Recebimento;
* Pagamento × Pagamento.

Não será permitida:

* Recebimento × Pagamento.

Caso o usuário informe alternativas de tipos diferentes, o sistema deverá informar que as alternativas não podem ser comparadas e solicitar novos dados.

### Data de referência

A **data de referência será o momento presente (t = 0)**.

Dessa forma, os valores futuros serão convertidos para **Valor Presente (VP)** antes da comparação.

A aplicação deverá utilizar a seguinte relação:

**VP = VF / (1 + i)^n**

Onde:

* **VP** = Valor Presente;
* **VF** = Valor Futuro;
* **i** = taxa de juros por período;
* **n** = número de períodos.

A taxa de juros e o prazo deverão utilizar a mesma periodicidade. Quando necessário, o prazo será convertido para a periodicidade utilizada pela taxa.

### Empate

Caso os valores equivalentes das alternativas sejam iguais, o sistema deverá informar que as alternativas são **financeiramente equivalentes**, considerando a taxa de juros, o prazo e as demais condições informadas.

### Resumo da decisão

| Situação                    | Regra                                     |
| --------------------------- | ----------------------------------------- |
| Recebimento                 | Maior Valor Presente = melhor alternativa |
| Pagamento                   | Menor Valor Presente = melhor alternativa |
| Valores equivalentes iguais | Alternativas financeiramente equivalentes |
| Tipos diferentes            | Comparação não permitida                  |

---

## 7. Saída esperada

Após o processamento, a aplicação deverá apresentar um relatório contendo:

* Dados informados pelo usuário;
* Taxa de juros utilizada;
* Prazo de cada alternativa;
* Valor original de cada alternativa;
* Valor equivalente calculado;
* Diferença entre as alternativas;
* Alternativa considerada mais vantajosa;
* Justificativa da decisão.

### Exemplo de saída

```text
========================================
ANÁLISE DE DECISÃO FINANCEIRA
========================================

Taxa utilizada: 8,00% ao ano

ALTERNATIVA A
Descrição: Receber hoje
Valor: R$ 10.000,00
Prazo: 0 anos
Valor equivalente: R$ 10.000,00

ALTERNATIVA B
Descrição: Receber daqui a 2 anos
Valor: R$ 12.000,00
Prazo: 2 anos
Valor equivalente: R$ 10.288,33

----------------------------------------
RESULTADO
----------------------------------------

Diferença: R$ 288,33

Alternativa mais vantajosa:
ALTERNATIVA B

Justificativa:
Considerando a taxa de 8,00% ao ano,
a Alternativa B apresenta maior valor
equivalente na data de referência.
========================================
```

---

## 8. Conceitos financeiros utilizados

O projeto será fundamentado nos seguintes conceitos:

* Valor do Dinheiro no Tempo;
* Valor Presente;
* Valor Futuro;
* Taxa de juros;
* Capitalização;
* Desconto.

---
