from random import randint

computer = randint(0, 10)
input_user = int(input('Adivinhe um número de 0 a 5: '))

while computer != input_user:
    print('Errou, tente novamente!')
    input_user = int(input('Adivinhe um número de 0 a 5: '))
print('Acertou! Parabéns!')