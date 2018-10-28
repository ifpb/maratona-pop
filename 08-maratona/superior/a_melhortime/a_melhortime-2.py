a, b = 0, 0

for i in range(int(input())):
    c, d = map(int, input().split())
    if d > b:
        a, b = c, d

print(a)