'''
Tempo para execução: 2 segundos
----------

Descrição
----------
O processo de transmissão consiste em enviar informação de um ponto a outro 
(origem para um destino). Na origem, a informação é codificada para uma forma 
apropriada para sua transmissão, chamados sinais, os quais são enviados por um 
meio adequado que interliga origem e destino. No destino, os elementos recebidos 
são decodificados e tornados adequados para sua interpretação pela entidade 
destinatária. 
Uma forma muito utilizada para codificar a informação se dá em transformá-la em 
uma sequência de bits (zeros e uns). O problema deste tipo de codificação é quando 
existem grandes sequências de zeros, que podem fazem parecer que a transmissão 
parou. Sua tarefa é escrever um programa que identifique a maior sequência de 
zeros de um sinal com codificação binária.

Entrada
----------
A entrada é composta apenas por uma linha. Nesta linha, há uma sequência de zeros 
e uns (sem nenhuma separação entre eles) representando um sinal em codificação 
binária. O sinal terá no máximo 5000 bits. Haverá pelo menos um zero no sinal.

Saída
----------
A saída deve ser as posições inicial e final da maior sequência de zeros do sinal. O 
primeiro bit está na posição zero. Em caso de empate, a sequência que apareceu 
primeiro deve ser impressa. 
'''

bits = input()
splited_bits = bits.split('1')

splited_bits.sort(key=len, reverse=True)

maior = splited_bits[0]
index = bits.index(maior)

print("{} {}".format(index, index+len(maior)-1))

