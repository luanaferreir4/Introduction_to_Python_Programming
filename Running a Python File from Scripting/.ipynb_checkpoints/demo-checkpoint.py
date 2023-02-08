# while True:
#     try:
#         x = int(input('Digite um número: '))
#     except KeyboardInterrupt:
#         print('Encerramento do programa...')
#         break
#     except:  # Não é uma boa prática usar o except vazio senão ele não vai parar em nenhum tipo e não saberemos qual tipo de erro está ocorrendo no programa.
#         print('Esse não é um número válido!')
#     else:
#         print('Sem exceções aqui!')
#         break
#     finally:
#         print('Sempre vai executar!')
        
        
while True:
    try:
        x = float(input('Digite um número: '))
    except ValueError:
        print('Tipo de dado errado! Insira um número: ')
    except KeyboardInterrupt:
        print('Encerrando o programa...')
    else:
        print('Prosseguindo o código...')
        break
    finally:
        print('Executa sempre!')
    