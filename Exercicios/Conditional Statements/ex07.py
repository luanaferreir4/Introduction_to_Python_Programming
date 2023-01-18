# 8) Escreva um algoritmo que leia três valores inteiros e diferentes e mostre-os em ordem
# decrescente

a, b, c = 2, 2, 3

if (a >= b) and (a >= c):
    if b >= c:
        result = a, b, c
    else:
        result = a, c, b
elif (b >= a) and (b >= c):
    if a >= c:
        result = b, a, c
    else:
        result = b, c, a
else:
    if a >= b:
        result = c, a, b
    else:
        result = c, b, a




