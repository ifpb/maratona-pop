map = {
    "um": 1,
    "dois": 2,
    "tres": 3,
    "quatro": 4,
    "cinco": 5,
    "seis": 6,
    "sete": 7,
    "oito": 8,
    "nove": 9,
    "dez": 10,
    "onze": 11,
    "doze": 12,
    "treze": 13,
    "catorze": 14,
    "quatorze": 14,
    "quinze": 15,
    "dezesseis": 16,
    "dezesete": 17,
    "dezoito": 18,
    "dezenove": 19,
    "vinte": 20,
    "vezes": "*",
    "mais": "+",
    "menos": "-",
}
reverse_map = {
    1: "um",
    2: "dois",
    3: "três",
    4: "quatro",
    5: "cinco",
    6: "seis",
    7: "sete",
    8: "oito",
    9: "nove",
    10: "dez",
    11: "onze",
    12: "doze",
    13: "treze",
    14: "catorze",
    15: "quinze",
    16: "dezesseis",
    17: "dezesete",
    18: "dezoito",
    19: "dezenove",
    20: "vinte",
}


operacoes = ["*", "+", "-"]

calculo = input().strip().split(" ")

for i in range(len(calculo)):
    calculo[i] = map[calculo[i]]

for i in operacoes:
    while i in calculo:
        try:
            index_op = calculo.index(i)
        except:
            break
        if i == "*":
            calculo[index_op-1] = calculo[index_op-1] * calculo[index_op+1]
        elif i == "+":
            calculo[index_op-1] = calculo[index_op-1] + calculo[index_op+1]
        elif i == "-":
            calculo[index_op-1] = calculo[index_op-1] - calculo[index_op+1]
        calculo.pop(index_op)
        calculo.pop(index_op)

result = reverse_map[calculo[0]]
print(result)