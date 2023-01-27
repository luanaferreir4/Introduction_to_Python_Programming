v1, v2 = float(input('valor 1: ')), float(input('valor 2: '))
choose = int(input('[1]somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair do programa\n> '))

while choose != 5:
    if choose == 1:
        print(v1+v2)
    elif choose == 2:
        print(v1*v2)
    elif choose == 3:
        print(max(v1, v2))
    elif choose == 4:
        v1, v2 = float(input('valor 1: ')), float(input('valor 2: '))
    else:
        print('Número não utilizado, reveja o menu:')
    v1, v2 = float(input('valor 1: ')), float(input('valor 2: '))
    choose = int(input('[1]somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair do programa\n> '))
