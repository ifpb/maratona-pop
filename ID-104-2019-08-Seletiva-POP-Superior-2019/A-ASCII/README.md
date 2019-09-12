### Problema A

# ASCII

Um assembler é um programa que pega um texto do código de um programa (escrito em assembly) e converte em linguagem binária. Uma das etapas desse processo de montagem é a conversão de caracteres em dados binários através de uma codificação, como a ASCII. 

Sua tarefa é escrever um programa que dada uma sequência de caracteres minúsculos, imprima o código ASCII binário de cada uma delas, conforme a tabela seguinte. 

| Caractere | Código |
|---------|-------|
| a | 01100001 |
| b | 01100010 |
| c | 01100011 |
| d | 01100100 |
| e | 01100101 |
| f | 01100110 |
| g | 01100111 |
| h | 01101000 |
| i | 01101001 |
| j | 01101010 |
| k | 01101011 |
| l | 01101100 |
| m | 01101101 |
| n | 01101110 |
| o | 01101111 |
| p | 01110000 |
| q | 01110001 |
| r | 01110010 |
| s | 01110011 |
| t | 01110100 |
| u | 01110101 |
| v | 01110110 |
| w | 01110111 |
| x | 01111000 |
| y | 01111001 |
| z | 01111010 |


## Entrada

A entrada é composta por uma única palavra, formada apenas por caracteres minúsculos. A palavra pode ter até 1000 caracteres.

## Saída

Para cada caractere na entrada, imprima uma linha contendo o código binário do caractere. 

## Exemplos

| Entrada | Saída |
|---------|-------|
| pop  | 01110000 |
| | 01101111 |
| | 01110000 |

| Entrada | Saída |
|---------|-------|
| abcxyz | 01100001 |
| | 01100010 |
| | 01100011 |
| | 01111000 |
| | 01111001 |
| | 01111010 |
