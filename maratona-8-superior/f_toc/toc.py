valores = input().split(" ")
valores = [int(valor) for valor in valores]
valores.sort()
possible = False

for i in range(len(valores)):
    total = valores[i]
    for j in range(i+1, len(valores)):
        if total + valores[j] <= 7:
            total += valores[j]
        else:
            break
    if total == 7:
        possible = True
        break

if possible:
    print("SIM")
else:
    print("NAO")
