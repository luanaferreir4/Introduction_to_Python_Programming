# 1) Desenvolver um algoritmo que efetue a soma de todos os números ímpares que são múltiplos de
# três e que se encontram no conjunto dos números de 1 até 500.


def soma_impares_mult_3(initial, end):
    count = 0
    for i in range(initial, end):
        if (i % 3 == 0) and (i % 2 != 0):
            count += i
    return count


print(soma_impares_mult_3(1, 10))