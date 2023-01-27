
def PA(qt):  # quantidade de termos
    r = 200  # razão
    a1 = 100  # primeiro termo
    lista_termos = []  # lista de termos
    i = 0
    while i < qt:
        lista_termos.append(a1)
        a1 += r
        i += 1
    return lista_termos


print(PA(10))

qt = int(input("Quer ver mais alguns termos? Quantos: ")) # quantidade de termos.

while qt != 0:
    lista_termos = PA(qt)
    print(lista_termos)
    qt = int(input("Quer ver mais alguns termos? Quantos: "))