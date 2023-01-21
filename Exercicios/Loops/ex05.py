# 5) Faça um algoritmo estruturado que leia uma quantidade não determinada de números positivos.
# Calcule a quantidade de números pares e ímpares, a média de valores pares e a média geral dos
# números lidos. O número que encerrará a leitura será zero.

n = float(input('Digite um número: '))
qntd_pares_impares = {'pares': 0, 'ímpares': 0}
valores = []
pares = []

while n > 0:
    valores.append(n)
    if n % 2 == 0:
        qntd_pares_impares['pares'] += 1
    else:
        qntd_pares_impares['ímpares'] += 1
    n = float(input('Digite um número: '))

print('Quantidade de pares e ímpares = ', qntd_pares_impares)

for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)

print('Média de valores pares = {}'.format(sum(pares)/ len(pares)))

print('Media geral de valores lidos = {}'.format(sum(valores)/len(valores)))
