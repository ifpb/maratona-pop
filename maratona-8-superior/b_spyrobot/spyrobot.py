num = int(input())
counts = [0 for i in range(num)]

for i in range(num):
    teclas = int(input())
    list_1 = input().split(" ")[:teclas]
    list_2 = input().split(" ")[:teclas]
    for a, b in zip(list_1, list_2):
        if a == b:
            counts[i] += 1

for count in counts:
    print(count)
