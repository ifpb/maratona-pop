eq = input().split()
num = ['um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte']
v = []
i = 0
while i < len(eq):
  if eq[i] == 'vezes':
    try:
      val1 = int(eq[i-1])
    except:
      val1 = num.index(eq[i-1])+1
    try:
      val2 = int(eq[i+1])
    except:
      val2 = num.index(eq[i+1])+1
    eq[i-1] = str(val1*val2)
    del eq[i]
    del eq[i] 
    i-=1
  
  i+=1
try:
  acc = int(eq[0])
except:
  acc = num.index(eq[0])+1
for i in range(1,len(eq)):
  if eq[i] == 'mais':
    try:
      val2 = int(eq[i+1])
    except:
      val2 = num.index(eq[i+1])+1
    acc+=val2

  if eq[i] == 'menos':
    try:
      val2 = int(eq[i+1])
    except:
      val2 = num.index(eq[i+1])+1
    acc-=val2

print(num[acc-1])

