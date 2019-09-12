### Problema F

# Fácil

Cansado de escrever questões para a seletiva do POP, Kerven resolveu ajudar os competidores e fazer uma questão muito fácil de se resolver. 
 
O problema é simples: dado um valor que vai ser dividido igualmente para várias pessoas, diga quanto cada uma vai precisar pagar. Para facilitar ainda mais a vida, os valores serão dados em centavos, assim nem com vírgula é necessário se preocupar. 
 
Note que não é possível alguém pagar menos de um centavo. Então caso a divisão não seja exata, arredonde para cima, mas informe o quanto de dinheiro irá sobrar no final. Por exemplo, se deve-se dividir 9999 centavos para 2 duas pessoas, cada uma irá pagar 5000 centavos e no final sobrará 1 centavo. 

## Entrada
A entrada é composta por uma única linha com dois inteiros​ V (1​ ≤ ​V ​≤ ​10​<sup>7</sup>​), o valor em centavos a ser dividido, e ​P (1​ ≤ ​P​ ≤ ​10<sup>4</sup>​), a quantidade de pessoas que dividirão o valor ​V​. 

## Saída

Caso a divisão seja exata, a saída deve conter um único inteiro informando quanto cada pessoa deve pagar. Caso contrário, a saída deve conter o inteiro indicando quanto cada pessoa deve pagar e, na linha seguinte, a mensagem SOBRA ​X​, onde ​X é o valor excedente ao juntar a contribuição de todas as pessoas. 

## Exemplos

| Entrada | Saída |
|---------|-------|
| 56815 11 | 5165 |

| Entrada | Saída |
|---------|-------|
| 9999 2 | 5000 |
| | SOBRA 1 |

| Entrada | Saída |
|---------|-------|
| 16484 78 | 212 |
| | SOBRA 52 |
