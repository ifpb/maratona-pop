x = int(input())
y = list(map(int, input().split()))
def is_organized():
  for i in range(x - 1):
    if y[i] > y[i+1]:
      return "NAO"
  return "SIM" 
print(is_organized())