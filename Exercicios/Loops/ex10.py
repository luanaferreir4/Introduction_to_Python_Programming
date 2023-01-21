# 10) Escreva um algoritmo que leia um valor inicial A e imprima a seqüência de valores do cálculo de
# A! e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120

fatorial = int(input('fatorial de: '))
result = 1

for i in range(fatorial, 0, -1):
    result *= i
print(result)
