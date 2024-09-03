# Sheet Scan
[![Python Tests](https://github.com/sleonardoaugusto/sheet_scan/actions/workflows/tests.yml/badge.svg)](https://github.com/sleonardoaugusto/sheet_scan/actions/workflows/tests.yml)

A Python script that reads credit card transactions from a CSV file and converts them into a formatted Excel file for [Mobills](https://web.mobills.com.br/) application.

### Features
- CSV to Excel Conversion: Parses a CSV file containing transaction data and outputs it as an Excel file.
- Automatic Table Creation: The Excel file includes a table with headers and properly formatted data.

### Requirements
- Python 3.10 
- install dependencies:

```bash
pip install requirements.txt
```

### Usage
1. Place your CSV file in the project’s root directory. 
2. Run the script:

```bash
python main.py <filename>.csv <template>
```
- Replace `<filename>` with the name of your actual CSV file.
- Replace `<template>` with one of the following options:
  - santander
  - inter


### Inter Bank Example
Input CSV:
```
"Data","Lançamento","Categoria","Tipo","Valor"
"14/05/2024","Jetbrains Americas I","OUTROS","Compra à vista","318,46"
"15/05/2024","Mp *rtcarimport","OUTROS","Parcela 1/3","R$698,00"
```

Output Excel:

| date       | descrição            | valor  | conta | category | installment    |
|------------|----------------------|--------|-------|----------|----------------|
| 2024-05-14 | Jetbrains Americas I | 318.46 |       |          | Compra à vista |
| 2024-05-15 | Mp *rtcarimport      | 698    |       |          | Parcela 1/3    |


### Santander Bank Example
Input CSV:
```
Lançamentos,,,
Cartão,Final 0001,,
Titular,LEONARDO AUGUSTO S.,,
Data,Descrição,Valor (US$),Valor (R$)
10/08/2024,Combustível,0,"454,63"
20/08/2024,Mercearia,0,26
Cartão,Final 0002,,
Titular,LEONARDO AUGUSTO S,,
Data,Descrição,Valor (US$),Valor (R$)
30/08/2024,Mercado,0,"326,45"
30/08/2024,Ifood,0,270
Cartão on-line,Final 0003,,
Titular,@ LEONARDO A SILVA,,
Data,Descrição,Valor (US$),Valor (R$)
30/08/2024,Jornal,0,"9,9"
24/08/2024,Padaria,0,"63,94"
Cartão on-line,Final 0004,,
Titular,@ LEONARDO A SILVA,,
Data,Descrição,Valor (US$),Valor (R$)
07/10/2023,Moveis & Decor (12/12),0,"891,71"
,,,
,Resumo de despesas,,
,Saldo anterior,,"11.111,11"
,Total de pagamentos (-),,"11.111,11"
,Total de créditos (+),,"11.111,11"
,Despesas/Débitos,,"1.111,11"
,Total despesas em US$,0,
,Total convertido em R$,,"1.111,11"
,Cotação do dólar dia 24/06 em R$,,"5,97"
,Limites de crédito,,
,Limite total,,"11.111,00"
,Limite para saque a vista,,"1.111,11"
```

Output Excel:

| date       | descrição                 | valor  | conta | category | installment |
|------------|---------------------------|--------|-------|----------|-------------|
| 2024-08-10 | Combustível               | 454.63 |       |          |             |
| 2024-08-20 | Mercearia                 | 26     |       |          |             |
| 2024-08-30 | Mercado                   | 326.45 |       |          |             |
| 2024-08-30 | Ifood                     | 270    |       |          |             |
| 2024-08-30 | Jornal                    | 9.9    |       |          |             |
| 2024-08-24 | Padaria                   | 63.94  |       |          |             |
| 2023-10-07 | Moveis & Decor            | 891.71 |       |          | 12/12       |

