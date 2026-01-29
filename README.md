# Diagnóstico de Bases de Dados - Python

Este programa realiza um **diagnóstico rápido de bases de dados brutas** (CSV ou Excel) e gera um relatório com informações importantes sobre a qualidade e estrutura dos dados.

## O que ele faz

- Mostra o **número de linhas e colunas** da base, incluindo os nomes das colunas.  
- Mostra **células vazias por coluna** e total de nulos.  
- Mostra **linhas duplicadas**.  
- Indica **colunas potencialmente compostas** (ex.: status/modelo).  
- Detecta **possíveis inconsistências de texto** (ex.: “RJ” vs “Rio de Janeiro”).  
- Mostra o **tipo de dado** de cada coluna.  

> IMPORTANTE: O programa **não limpa nem transforma** os dados. Ele serve apenas para análise.

## Requisitos

Antes de rodar o script, você precisa ter instalado na sua máquina:

- Python 3.7 
- pandas
- openpyxl

## Como usar
  1. Coloque o arquivo da base de dados na mesma pasta do diagnostico.py.
  2. Abra o terminal (ou Git Bash) dentro dessa pasta.
  3. Rode o script: ```python diagnostico.py```
  4. Quando solicitado, digite o nome do arquivo que deseja analisar.
  5. O programa vai gerar:
     - Um relatório no terminal.
     - Um arquivo chamado relatorio_diagnostico.txt na mesma pasta.
## Conhecimentos aprofundados
Construi um artigo falando mais detalhadamente sobre esse programa.

Artigo: https://medium.com/@heraldo.c.alves/arquitetando-um-script-modular-em-python-para-diagnóstico-de-dados-befb3de4342d
