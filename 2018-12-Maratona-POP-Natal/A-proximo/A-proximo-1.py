normal = [31, 28, 31, 30, 31, 30, 31, 31,30,31, 30, 31]
bissexto = [31, 29, 31, 30, 31, 30, 31, 31,30,31, 30, 31]
n = int(input())
for i in range (0, n):
  dados = [int(x) for x in input().split()]
  isNormal = True
  if dados[2]%400==0:
    isNormal = False
  elif dados[2]%100==0:
    isNormal = True
  elif dados[2]%4==0:
    isNormal = False
  else:
    isNormal = True
  data = 0
  if isNormal:
    natal = sum(normal)-6
    for j in range (0, dados[1]-1):
      data+=normal[j]
    data+=dados[0]
    if data<=natal:
      print(natal-data)
    else:
      print(sum(normal)+data-natal-1)
  else:
    natal = sum(bissexto)-6
    for j in range (0, dados[1]-1):
      data+=bissexto[j]
    data+=dados[0]
    if data<=natal:
      print(natal-data)
    else:
      print(sum(bissexto)+data-natal-3)
