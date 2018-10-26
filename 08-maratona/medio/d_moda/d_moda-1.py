'''
Tempo para execução: 2 segundos
----------

Descrição
----------
O milésimo octogésimo terceiro desfile de moda fashion do IFPB contou com mais	
de quinhentas pessoas desfilando durante os seus dois dias e meio, tendo como	
tema “roupas inspiradas na natureza”. Foi uma explosão de criatividade e de novas 
ideias, como a belíssima blusa inspirada nas asas das borboletas que parecem 
mariposas do cariri, ou a saia feita de orquídeas silvestres migrantes do Panamá. 
A belíssima modelo supersimétrica HannaH MiriM assistiu os desfiles diretamente 
do seu camarote privativo. Todos os anos ela anota cada tipo de roupa que foi usada 
na passarela e compra aquela que mais se repetiu para usar durante o ano inteiro. 
Seu trabalho é ajudar HannaH MiriM a descobrir qual a roupa que mais se repetiu 
neste desfile.

Entrada
----------
A primeira linha da entrada possui um número inteiro N (1<=N<=500), 
representando o número de roupas usadas no evento. Cada uma das N linhas 
seguintes apresentam um número inteiro x n  (1<=x n <=500) representando o 
identificador único da roupa usada no desfile número n. 

Saída
----------
A saída deve ser o identificador único da roupa que mais se repetiu no desfile. Em 
caso de empate, o menor identificador (entre as roupas que empataram) deve ser 
impresso. 
'''

# A classe Counter funciona como um MapList onde a chave de acesso
# é o item passado e o valor é a quantidade de vezes que o item
# é repetido dentro de uma lista
from collections import Counter

quantidade = input()
roupas = []

for n in range(quantidade):
    numero = int(input())
    roupas.append(numero)

# Capturamos a lista com a quantidade de repetições dos items
contagem = Counter(roupas).most_common()

# Elegemos o menor item como sendo o primerio da lista e seu valor
menor_numero = contagem[0][0]
menor_numero_qtd = contagem[0][1]

# Verificamos qual é o menor item que mais se repete na contagem
for numero, qtd in contagem:
    if menor_numero > numero and menor_numero_qtd == qtd:
        menor_numero = numero

print(menor_numero)