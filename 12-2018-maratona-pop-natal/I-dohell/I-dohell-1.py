lista = [[16,3, 2,13], [5, 10, 11, 8], [9, 6, 7, 12], [4, 15, 14, 1]]
for i in range (0, len(lista)):
  for j in range (0, len(lista[i])):
    if j!=0:
      print('',end=' ')
    print(lista[i][j], end='')
  print('')