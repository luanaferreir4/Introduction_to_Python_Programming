# 2) Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. Caso sexo seja “F” e
# estado civil seja “CASADA”, solicitar o tempo de casada (anos).

nome = 'Luana'
sexo = 'F'
estado_civil = 'casada'

if sexo.upper() == 'F' and estado_civil.upper() == 'CASADA':
    tempo_de_casamento = float(input('Tempo de casada (em anos): '))