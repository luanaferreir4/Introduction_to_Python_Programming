# 11) Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço
# normal de etiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a seguir
# para ler qual acondição de pagamento escolhida e efetuar o cálculo adequado.
# Código Condição de pagamento
# 1 À vista em dinheiro ou cheque, recebe 10% de desconto
# 2 À vista no cartão de crédito, recebe 15% de desconto
# 3 Em duas vezes, preço normal de etiqueta sem juros
# 4 Em duas vezes, preço normal de etiqueta mais juros de 10%

preco = float(input('Preço: '))
a_vista = input('A vista? ')
result = None

if a_vista.lower() == "sim" or a_vista.lower() == "s":
    condicao_de_pagamento = input('Condição de pagamento:\n1. Dinheiro ou cheque\n2. Cartão de crédito\n> ')
    if condicao_de_pagamento == "1":
        preco -= preco * .1
        result = preco
    elif condicao_de_pagamento == "2":
        preco -= preco * .15
        result = preco
    else:
        print('Valor desconhecido, tente novamente!')
elif a_vista.lower() == "não" or a_vista.lower() == "nao" or a_vista.lower() == "n":
    condicao_de_pagamento = input('Condição de pagamento:\n1. Sem juros\n2. Com juros\n> ')
    if condicao_de_pagamento == "1":
        result = preco
    elif condicao_de_pagamento == "2":
        preco += preco * .1
        result = preco
    else:
        print('Valor desconhecido, tente novamente!')
else:
    print('O algoritmo apenas aceita "sim/s" ou "não/nao/n", tente novamente!')

print("R$", result)