# 2) Desenvolver um algoritmo que leia a altura de 15 pessoas. Este programa deverá calcular e
# mostrar :
# a. A menor altura do grupo;
# b. A maior altura do grupo;

alturas = []

for i in range(1, 16):
    altura = float(input('altura {}: '.format(i)))
    alturas.append(altura)

print('maior altura:', max(alturas))
print('menor altura:',  min(alturas))