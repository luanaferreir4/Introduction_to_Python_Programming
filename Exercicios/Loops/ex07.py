# 7) Escrever um algoritmo que leia um valor para uma variável N de 1 a 10 e calcule a tabuada de
# N. Mostre a tabuada na forma: 0 x N = 0, 1 x N = 1N, 2 x N = 2N, ..., 10 x N = 10N.

def tabuada(num, start=1, end=11):
    tabuada_ls = []
    for i in range(start, end):
        tabuada_ls.append('{} x {} = {}'.format(num, i, num*i))
    return tabuada_ls


expected = []
for i in range(1, 11):
    num = 10
    expected.append('{} x {} = {}'.format(num, i, num*i))

assert (tabuada(10) == expected)