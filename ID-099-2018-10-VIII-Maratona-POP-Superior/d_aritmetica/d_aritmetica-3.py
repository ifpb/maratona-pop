my_dict = {"um": 1, "dois": 2, "três": 3, "quatro": 4, "cinco": 5, 
           "seis": 6, "sete": 7, "oito": 8, "nove": 9, "dez": 10,
           "onze": 11, "doze": 12, "treze": 13, "catorze": 14, "quatorze": 14, "quinze": 15,
           "dezesseis": 16, "dezessete": 17, "dezoito": 18, "dezenove": 19, "vinte": 20}
my_dict_reversed = {k: j for j, k in my_dict.items()}

entry = input().split()
calc = [my_dict[j] if i%2 == 0 else j for i, j in enumerate(entry)]
my_operand, my_operators, skip = [], [], False
#Vezes
for i in range(len(calc)):
  if skip:
    skip = False
    continue
  if calc[i] not in ("mais", "menos", "vezes"):
    my_operand.append(calc[i])
  else:
    if calc[i] == "vezes":
      my_operand.append(my_operand.pop(-1) * calc[i+1])
      skip = True
    else:
      my_operators.append(calc[i])
#Mais / Menos
for i in my_operators:
  if i == "mais":
    my_operand.append(my_operand.pop() + my_operand.pop())
  else:
    my_operand.append(abs(my_operand.pop() - my_operand.pop()))
print(my_dict_reversed[my_operand[0]])