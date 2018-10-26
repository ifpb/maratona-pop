'''
Tempo para execução: 2 segundos
----------

Descrição
----------
Um grafo é uma estrutura de dados abstrata composta por um conjunto de vértices 
e um conjunto arestas, que são as ligações entre estes vértices. Na figura abaixo, o 
conjunto dos vértices do grafo é V={ 1, 2, 3, 4, 5, 6 e 7 } e o conjunto de arestas é 
E={ a, b, c, d, e, f, g, h, i, j }.

Um modo simples de representar um grafo é utilizando uma matriz de adjacências. 
Esta é uma matriz NxN, onde N é o número de vértices do grafo, na qual um valor 0 
na  célula x,y indica que não há conexão entre os vértices x e y, enquanto que um 
valor maior que zero na posição x,y indica que há conexão entre os vértices x e y. 
Por sua vez, o grau de um vértice é o número de vizinhos que ele possui. Igualmente, 
o grau de um vértice pode ser descrito como o número de arestas que incidem sobre 
este. Dado um grafo, com sua representação em matriz de adjacências, sua tarefa é 
descobrir se este é um grafo Tom ou um grafo Jerry. Um grafo Tom é aquele cujo 
maior grau é um número ímpar. Enquanto que um grafo Jerry é aquele cujo maior 
grau é um número par. O grafo da figura é um grafo Jerry, pois seu maior grau é 4 
(vértices 4 e 7). 

Entrada
----------
A primeira linha da entrada possui um número inteiro N (1<=N<=20), que representa 
o número de vértices do grafo. As N linhas seguintes representam a matriz de 
adjacências do grafo de entrada. Cada uma destas linhas possui N números inteiros 
(entre 0 e 100) separados por um espaço. 

Saída
----------
A saída deve ter apenas uma letra: T, caso o grafo seja TOM, ou J, caso seja Jerry.
'''

n = int(input())
adj = []
maior = 0

for i in range(n):
    adj.append(input())

for i in adj:
    if i.count("1")> maior:
        maior = i.count("1")
  
if maior % 2 == 0:
    print("J")
else:
    print("T")
