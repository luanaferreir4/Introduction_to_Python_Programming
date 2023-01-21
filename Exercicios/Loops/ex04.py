# 4) Escrever um algoritmo que leia uma quantidade desconhecida de números e conte quantos deles
# estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deve
# terminar quando for lido um número negativo.

def entre_intervalos(numeros):
    qntd_intervalos = {'0-25': 0, '26-50': 0, '51-75': 0, '76-100': 0}

    for numero in numeros:
        if numero <= 25:
            qntd_intervalos['0-25'] += 1
        elif numero <= 50:
            qntd_intervalos['26-50'] += 1
        elif numero <= 75:
            qntd_intervalos['51-75'] += 1
        elif numero <= 100:
            qntd_intervalos['76-100'] += 1
        else:
            return 'Nesse algoritmo apenas são aceitos números de 0 a 100.'
    return qntd_intervalos


print(entre_intervalos([100, 100]))