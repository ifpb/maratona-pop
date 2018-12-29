
n = int(input())
lista = []
for i in range (0, n):
  number = [int(x) for x in input().split('.')]
  number = number[0]*100 + number[1]
  lista.append(number)
maximo = str(max(lista))
minimo = str(min(lista))
maxmin = str(max(lista) - min(lista))
media = str(sum(lista)//(len(lista)))
minimo = minimo.rjust(3, '0')
maxmin = maxmin.rjust(3, '0')
maxmimo = maximo.rjust(3, '0')
media = media.rjust(3, '0')
print('{}.{}'.format(maximo[:len(maximo)-2], maximo[len(maximo)-2:]))
print('{}.{}'.format(minimo[:len(minimo)-2], minimo[len(minimo)-2:]))
print('{}.{}'.format(maxmin[:len(maxmin)-2], maxmin[len(maxmin)-2:]))
print('{}.{}'.format(media[:len(media)-2], media[len(media)-2:]))
