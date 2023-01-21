# 5) Faça um algoritmo estruturado que leia uma quantidade não determinada de números positivos.
# Calcule a quantidade de números pares e ímpares, a média de valores pares e a média geral dos
# números lidos. O número que encerrará a leitura será zero.

lista = [10, 3, 1, 2]


def quantidade_pares_impares(numeros):
    qntd_pares_impares = {'pares': 0, 'ímpares': 0}
    if min(numeros) > 0:
        for numero in numeros:
            if numero % 2 == 0:
                qntd_pares_impares['pares'] += 1
            else:
                qntd_pares_impares['ímpares'] += 1
        return qntd_pares_impares
    else:
        raise Exception('Apenas aceitamos números maiores que 0.')


def media_valores_pares(numeros):
    pares = []
    if min(numeros) <= 0:
        raise Exception('Apenas aceitamos números maiores que 0.')
    else:
        for numero in numeros:
            if numero % 2 == 0:
                pares.append(numero)
        return sum(pares)/len(pares)


def media_geral(numeros):
    if min(numeros) <= 0:
        raise Exception('Apenas aceitamos números maiores que 0.')
    else:
        return sum(numeros)/len(numeros)

print(media_valores_pares(lista))
print(quantidade_pares_impares(lista))
print(media_geral(lista))

