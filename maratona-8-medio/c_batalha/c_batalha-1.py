'''
Tempo para execução: 2 segundos
----------

Descrição
----------
O inglês Paul Oftarso é um fã incondicional do jogo Batalha Naval. Ele passa horas e
mais horas do seu dia planejando novas táticas e estratégias para ludibriar seus rivais
e vencer. A sua maior fonte de jogadas, como não poderia deixar de ser, é o site
www.JogosAntigosDeBatalhaNavalDosCampeoes.net. Certo dia, Paul Oftarso
percebeu que caso ele não precisasse computar os acertos de cada jogo, ele 
conseguiria analisar muito mais jogos por dia, e assim ficar muito melhor. Então, ele 
contratou você para programar um calculador automático de acertos. O formato de 
dados do site é composto por duas matrizes quadradas NxN. A matriz A contém a 
posição dos navios (0 para não tem navio e 1 para tem navio). A matriz B contém as 
jogadas (0 para não teve jogada nessa posição, ou um inteiro x >= 1, o número da 
jogada que tentou acertar naquela posição). A pontuação consiste no número de 
jogadas da matriz B que acertou em uma posição com navio na matriz A. Obs.: Todos 
os navios tem tamanho 1x1.

Entrada
----------
A primeira linha da entrada possui um número inteiro N (1<=N<=100), 
representando o tamanho das matrizes. As N linhas seguintes apresentam a matriz 
A, cada uma possuindo exatamente N 0s ou 1s. As N linhas seguintes apresentam a 
matriz B. Cada linha apresenta N números, sendo que 0 representa que não houve 
jogada naquela posição, e um número maior que zero representa que houve alguma 
jogada nesta posição. 

Saída
----------
A saída deve ser o número de acertos.
'''
tamanho = int(input())

navios = []
jogadas = []
score = 0

# Captura a matriz de navios
for n in range(tamanho):
    nav = [int(n) for n in input().split()]
    navios.append(nav)

# Captura a matriz de jogadas
for n in range(tamanho):
    jogada = [int(n) for n in input().split()]
    jogadas.append(jogada)

# Ler todas as linhas da matriz de navios
for i, linha in enumerate(navios):
    # Ler todos os navios de uma linha
    for j, navio in enumerate(linha):
        # Verifica se houve uma jogada correta na posição do navio
        if navio == 1 and jogadas[i][j] > 0:
            score += 1

print(score)
