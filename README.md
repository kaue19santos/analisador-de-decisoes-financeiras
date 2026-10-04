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

## 4. Entradas

O usuário deverá informar os dados necessários para realizar a comparação.

### Dados gerais

* Taxa de juros;
* Período utilizado na análise;
* Data ou momento de referência.

### Dados de cada alternativa

* Nome da alternativa;
* Valor financeiro;
* Prazo;
* Unidade do prazo;
* Tipo da operação: recebimento ou pagamento.

Inicialmente, a aplicação trabalhará com **duas alternativas**.

### Exemplo de entrada

```text
Taxa de juros: 8% ao ano

Alternativa A
Nome: Receber hoje
Valor: R$ 10.000
Prazo: 0 anos
Tipo: Recebimento

Alternativa B
Nome: Receber daqui a 2 anos
Valor: R$ 12.000
Prazo: 2 anos
Tipo: Recebimento
```

---

## 5. Cálculos

A aplicação utilizará os conceitos de Valor do Dinheiro no Tempo apresentados na disciplina.

### 5.1 Valor Futuro

Quando for necessário determinar o valor futuro de um montante atual:

$$
VF = VP(1+i)^n
$$

Onde:

* `VF` = valor futuro;
* `VP` = valor presente;
* `i` = taxa de juros por período;
* `n` = número de períodos.

### 5.2 Valor Presente

Quando for necessário determinar quanto um valor futuro representa no momento atual:

$$
VP = \frac{VF}{(1+i)^n}
$$

Onde:

* `VP` = valor presente;
* `VF` = valor futuro;
* `i` = taxa de juros por período;
* `n` = número de períodos.

### 5.3 Comparação

Após calcular os valores equivalentes das alternativas, o sistema deverá:

1. Colocar as alternativas na mesma referência temporal;
2. Comparar os valores equivalentes;
3. Calcular a diferença entre as alternativas;
4. Calcular, quando aplicável, a diferença percentual;
5. Determinar qual alternativa apresenta maior valor financeiro.

---

## 6. Regra de decisão

A regra principal da aplicação será:

> **A alternativa que apresentar o maior valor equivalente na mesma data de referência será considerada financeiramente mais vantajosa.**

Por exemplo, considerando:

* Alternativa A: R$ 10.000 hoje;
* Alternativa B: R$ 12.000 daqui a 2 anos;
* Taxa: 8% ao ano.

O sistema calcula:

$$
VP_B = \frac{12.000}{(1+0,08)^2}
$$

$$
VP_B \approx R\$ 10.288
$$

A comparação será:

```text
Alternativa A: R$ 10.000,00
Alternativa B: R$ 10.288,00
```

Nesse cenário, a **Alternativa B** será considerada mais vantajosa.

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
Valor presente: R$ 10.288,33

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

Funcionalidades adicionais poderão ser consideradas posteriormente, caso sejam necessárias e não prejudiquem o objetivo principal do trabalho.
