n = int(input())
v = list(map(int,input().split())
a = v.copy()
v.sort()
if a == v:
	print('SIM')
else:
	print('NAO')
