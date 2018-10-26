valor = int(input())

maior = -1
maior_time = None

for i in range(valor):
    time, valor = input().split(" ")
    time = int(time)
    valor = int(valor)
    if maior < valor:
        maior_time = time
        maior = valor

print(maior_time)