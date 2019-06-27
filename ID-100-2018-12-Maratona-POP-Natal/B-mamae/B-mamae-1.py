def is_Equal(a):
  nums = ['1', '0', '8','6','9']
  new_a = ''
  for i in range (0, len(a)):
    if a[i] not in nums:
      return False
  for i in range (0, len(a)):
    if a[i]=='6':
      new_a+='9'
    elif a[i]=='9':
      new_a+='6'
    else:
      new_a+=a[i]
  if new_a == a[::-1]:
    return True
  else:
    return False

n = int(input())
for i in range (0, n):
  a = int(input())
  while True:
    if is_Equal(str(a)):
      print(a)
      break
    a+=1
