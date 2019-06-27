n = int(input())
for i in range (0, n):
  k = int(input())
  mark = [False]*k
  for j in range (0, k-1):
    mark[int(input())-1] = True
  for j in range(0, len(mark)):
    if mark[j] == False:
      print(j+1)
      break
