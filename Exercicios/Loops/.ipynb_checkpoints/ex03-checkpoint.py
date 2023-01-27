# 3) Desenvolver um algoritmo que leia um número não determinado de valores e calcule e escreva a
# média aritmética dos valores lidos, a quantidade de valores positivos, a quantidade de valores
# negativos e o percentual de valores negativos e positivos.

ls_valores = [-1, 2, 3, 2]


def media_aritmetica(valores):
    return {'Media aritmetica': sum(valores)/len(valores)}


def quantidade_positivos_negativos(valores):
    count_neg = 0
    count_pos = 0
    for valor in valores:
        if valor < 0:
            count_neg += 1
        else:
            count_pos += 1
    return {'Quantidade de valores positivos': count_pos, 'Quantidade de valores negativos': count_neg}


def percentual_valores_negativos_positivos(valores):
    positivos_negativos = quantidade_positivos_negativos(valores)
    count_pos = positivos_negativos['Quantidade de valores positivos']
    count_neg = positivos_negativos['Quantidade de valores negativos']
    total = count_neg + count_pos
    return {
        'Percentual de valores positivos': 100 * count_pos/total,
        'Percentual de valores negativos': 100 * count_neg/total
    }


print(media_aritmetica(ls_valores))
print(quantidade_positivos_negativos(ls_valores))
print(percentual_valores_negativos_positivos(ls_valores))

