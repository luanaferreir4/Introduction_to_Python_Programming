r = 200  # razao
t = 220  # termos, 220 é o primeiro termo
quantidade_de_termos = 10  # quantidade de termos
lista_termos = []  # lista com todos os termos
i = 0

while i < quantidade_de_termos:
    lista_termos.append(t)
    t += r
    i += 1

print(lista_termos)