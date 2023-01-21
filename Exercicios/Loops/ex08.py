# 8) Escreva um algoritmo que leia um valor inicial A e uma razão R e imprima uma seqüência em
# P.A. contendo 10 valores.

primeiro_termo = float(input('A: '))  # primeiro termo
razao = float(input('R (razão): '))

for i in range(0, 10):  # 10 termos
    print(primeiro_termo)
    primeiro_termo += razao