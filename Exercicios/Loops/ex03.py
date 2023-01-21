# 3) Desenvolver um algoritmo que leia um número não determinado de valores e calcule e escreva a
# média aritmética dos valores lidos, a quantidade de valores positivos, a quantidade de valores
# negativos e o percentual de valores negativos e positivos.

n = int(input('Quantidade de valores: '))
valores = list()
count_pos = 0
count_neg = 0

for i in range(n):
    valor = float(input('valor {}: '.format(i)))
    valores.append(valor)
    if valor < 0:
        count_neg += 1
    else:
        count_pos += 1

total = count_neg + count_pos

print('media aritmetica: {}'.format(sum(valores)/len(valores)))
print('quantidade de valores positivos: {} valores.'.format(count_pos))
print('quantidade de valores negativos: {} valores'.format(count_neg))
print('{}%'.format(count_pos / total * 100))
