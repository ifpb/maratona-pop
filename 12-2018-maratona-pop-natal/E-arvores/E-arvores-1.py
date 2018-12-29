n = int(input())
for i in range (0, n):
  lista = [int(x) for x in input().split()]
  mark = [False]*len(lista)
  lista.sort()
  maior = lista[len(lista)-1]
  first = False
  second = False
  mark[len(lista)-1] = True
  for i in range (0, len(lista)):
    for j in range (0, len(lista)):
      if lista[i]+lista[j] == maior and i!=j:
        mark[i] = True
        mark[j] = True
        first = True
        break
    if first:
      break
  s = 0
  for i in range(0, len(lista)):
    if lista[i]!=maior and mark[i] == False:
      s+=lista[i]
  #print(mark)
  if s == maior:
    second = True
  if second == True and first == True:
    print('ARVORE DE NATAL DE NATAL')
  else:
    print('ARVORE DE NATAL')