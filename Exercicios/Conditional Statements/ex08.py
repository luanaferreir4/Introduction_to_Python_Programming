# 9) Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que
# calcule seu peso ideal, utilizando as seguintes fórmulas:
# ● para homens: (72.7 * h) – 58;
# ● para mulheres: (62.1 * h) – 44.7.

altura = 1.58
sexo = 'X'

if sexo.upper() == 'F':
    r = 62.1*altura - 44.7
elif sexo.upper() == 'M':
    r = 72.7*altura - 58
else:
    r = 'O sexo nesse caso precisa ser (M - masculino) ou (F - feminino).'

print(r)