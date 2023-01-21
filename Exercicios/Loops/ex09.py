# 9) Escreva um algoritmo que leia um valor inicial A e uma razão R e imprima uma seqüência em
# P.G. contendo 10 valores. (Progressão Geométrica)

def progressao_geometrica(primeiro_termo, razao):
    seq_PG = []
    for i in range(0, 10):
        seq_PG.append(primeiro_termo)
        primeiro_termo *= razao
    return seq_PG


print(progressao_geometrica(2, 5))
