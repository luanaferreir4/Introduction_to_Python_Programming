# 4) Escrever um algoritmo que leia uma quantidade desconhecida de números e conte quantos deles
# estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deve
# terminar quando for lido um número negativo.

num = int(input('Digite um número: '))
qntd_intervalos = {'0-25': 0, '26-50': 0, '51-75': 0, '76-100': 0}

while num >= 0:
    if num <= 25:
        qntd_intervalos['0-25'] += 1
    elif num <= 50:
        qntd_intervalos['26-50'] += 1
    elif num <= 75:
        qntd_intervalos['51-75'] += 1
    elif num <= 100:
        qntd_intervalos['76-100'] += 1
    else:
        print('0 - 100')
    num = int(input('Digite um número: '))

print(qntd_intervalos)

