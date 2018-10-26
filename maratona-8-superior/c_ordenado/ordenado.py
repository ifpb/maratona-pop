num = int(input())
valores = input().split(" ")[:num]

result = True

for i in range(len(valores)-1):
    if int(valores[i]) > int(valores[i+1]):
        result = False
        break


if result:
    print("SIM")
else:
    print("NAO")
