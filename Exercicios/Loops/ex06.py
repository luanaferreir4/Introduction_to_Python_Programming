# 6) Escrever um algoritmo que gera e escreve os números ímpares entre 100 e 200.

def impares(initial, end):
    impares_list = []
    for i in range(initial, end):
        if i % 2 != 0:
            impares_list.append(i)
    return impares_list


print(impares(100, 200))

