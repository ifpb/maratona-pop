'''
Tempo para execução: 2 segundos
----------

Descrição
----------
Pitucca	é um garçom novato do famoso restaurante Flores do Mar do IFPB. Apesar 
de ser meio desajeitado, em pouco tempo ele conseguiu conquistar o carinho e a 
confiança dos clientes, dos outros garçons e dos patrões. 
Certo dia, VelociRápido, o Office Boy da empresa, adoeceu e não pôde ir trabalhar. 
Então, Pitucca se ofereceu para fazer o trabalho dele neste dia, e claro ganhar 
pontos com a chefia! O trabalho era imprimir o novo cardápio do restaurante 
ordenado pelo preço. Como Pitucca é muito desligado, ele mandou imprimir em 
ordem alfabética!!! “Mas não era em ordem alfabética?”. Você consegue ajudar 
Pitucca a consertar o cardápio para que ele não seja demitido? 

Entrada
----------
A primeira linha da entrada possui um número inteiro N (1<=N<=2000), que 
representa o número de itens no cardápio. As N linhas seguintes apresentam cada 
item, em ordem alfabética. Cada uma destas linhas possui o nome do produto 
(apenas uma palavra, sem espaços) seguido pelo seu preço, um número inteiro 
maior que zero e menor que 500.

Saída
----------
A saída deve ser o conjunto de preços ordenado de forma crescente (estritamente 
falando, ordem não decrescente, pois pode haver preços iguais). 
'''

quantidade = int(input())

items = []

for n in range(quantidade):
    _, valor = input().split()
    items.append(int(valor))

items.sort()

for numero in items:
    print(numero, end=" ")
print("")
