### Problema B

# Bactérias

Mateus é obcecado por bactérias. Para estudar o comportamento reprodutivo delas, ele criou um ambiente e colocou algumas bactérias e deseja saber as áreas contaminadas ao final do processo. 

O ambiente é representado por uma matriz formada pelos caracteres X, O, B. Um campo com um X representa uma barreira que as bactérias não conseguem atravessar. Um campo com O representa um ambiente no qual uma bactéria consegue se reproduzir. Por fim, um B representa um ambiente já contaminado por bactérias.

Através do processo reprodutivo das bactérias, elas conseguem contaminar todos os campos propícios ao redor dela. Veja o exemplo seguinte:

```
OOXO   OBXO   BBXO
XBOX → XBBX → XBBX
XXXO   XXXO   XXXO 
```

Observe que no terceiro estágio, não há mais lugar para as bactérias se reproduzirem, por causa barreiras que estão ao redor.

## Entrada

A primeira linha da entrada contém dois inteiros ​N ​e ​M ​(1​ ≤ ​N​, ​M​ ≤ ​100) indicando a quantidade de linhas e colunas da matriz. Cada uma das próximas​ N ​linhas contém ​M caracteres cada (cada caractere é uma letra B, O ou X, com significado de acordo com o descrito acima).

## Saída

A saída deve conter a matriz ao final do processo de reprodução das bactérias.

## Exemplos

| Entrada | Saída |
|---------|-------|
| 3 4  | BBXO |
| OOXO | XBBX |
| XBOX | XXXO |
| XXXO | |
