# 8) Escreva um algoritmo que leia um valor inicial A e uma razão R e imprima uma seqüência em
# P.A. contendo 10 valores.

def progressao_aritmetica(primeiro_termo, razao):
    seq_PA = [primeiro_termo]
    for i in range(0, 9):  # 1 + 9 termos = 10 termos
        primeiro_termo += razao
        seq_PA.append(primeiro_termo)
    return seq_PA


print(progressao_aritmetica(200, 220))