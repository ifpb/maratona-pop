'''
Tempo para execução: 2 segundos
----------

Descrição
----------
O professor Louis Charles é uma pessoa muito econômica. Ele conta até os centavos 
de cada salário que recebe, e sabe exatamente onde vai gastar cada pedacinho do 
dinheiro  que  ganha.  Na  última  segunda-feira,  a  PenseNaoCompreAgora.com,  uma 
loja da Internet, lançou uma grande promoção: compre um item e escolha se quer 
um  desconto  absoluto  ou  em  porcentagem.  Por  exemplo,  digamos  que  uma  calça 
custa 200 reais e o desconto é de 15. Vale mais à pena pegar o desconto de 15 reais 
ou de 15% de 200, que dá 30 reais? Sua missão é ajudar Louis Charles a tomar esta 
decisão.

Entrada
----------
A entrada contém apenas uma linha. Esta linha contém dois números inteiros X e D, 
de modo que 1<=X<=50000 e 0<=D<=100. X é o preço do objeto que está sendo 
vendido e D é o desconto que pode ser absoluto ou em porcentagem. 

Saída
----------
Caso seja melhor optar pelo desconto absoluto, a saída deve ser ABSOLUTO. Caso 
seja mais vantajoso optar pelo desconto em porcentagem, a saída deve ser 
PORCENTAGEM. Caso dê no mesmo, o programa deve imprimir TANTO FAZ COMO 
TANTO FEZ. 
Obs.: Caso a diferença seja menor que 0.01, o resultado deve ser TANTO FAZ COMO 
TANTO FEZ, pois não existe quantia menor que 1 centavo no Brasil! ; - )	
'''
entrada = input().split()
valor, desconto = [int(n) for n in entrada]


valor_com_desconto_subtracao = valor - desconto
valor_com_desconto_porcentagem = valor - (valor * (float(desconto)/100))


if valor_com_desconto_subtracao < valor_com_desconto_porcentagem:
    print("ABSOLUTO")
elif valor_com_desconto_subtracao > valor_com_desconto_porcentagem:
    print("PORCENTAGEM")
else:
    print("TANTO FAZ COMO TANTO FEZ")
