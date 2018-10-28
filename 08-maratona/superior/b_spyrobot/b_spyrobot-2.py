for i in range(int(input())):
    x = int(input())
    y = list(map(int, input().split()))
    z = list(map(int, input().split()))
    contador = 0
    for j in range(x):
        if y[j] == z[j]:
            contador += 1

print(contador)