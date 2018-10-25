'''
Tempo para execução: 2 segundos
----------

Descrição
----------
Para entrar no clube dos programadores avançados da segunda dinastia de
Val Wouldread, a grande rainha, é preciso saber de todas as
contrassenhas do império lunar. Não é difícil lembrar: 
Se a senha é A, a contrassenha é 1. 
Se a senha é B, a contrassenha é 2.
Se a senha é C, a contrassenha é 0.
Se a senha é D, a contrassenha é 3.
Se a senha é E, a contrassenha é 4.
Se a senha é F, a contrassenha é 6. 
Finalmente, se a senha não for nenhuma dessas letras, a contrassenha é 9.

Entrada
----------
A entrada contém apenas uma letra maiúscula, representando a senha apresentada.

Saída
----------
A saída deve ser a contrassenha correspondente (seguida por um <enter>).
'''

letra = input()

def contra_senha(letra):
    '''Função para detectar a contra senha correta
    para a letra lida durante a execução'''
    retorno = 9

    if letra == 'A':
        retorno = 1

    elif letra == 'B':
        retorno = 2

    elif letra == 'C':
        retorno = 0

    elif letra == 'D':
        retorno = 3

    elif letra == 'E':
        retorno = 4

    elif letra == 'F':
        retorno = 6

    return retorno


print(contra_senha(letra))
