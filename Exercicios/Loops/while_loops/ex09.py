# Crie um programa que leia vários números inteiros pelo
# teclado. No final da execução, mostre a média entre todos
# os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não
# continuar a digitar valores.

numero = int(input('Número inteiro: '))
continuar = input('Continuar? ')

numeros = [numero]

while continuar.upper() == 'SIM':
    numero = int(input('Número inteiro: '))
    numeros.append(numero)
    continuar = input('Continuar? ')

print(numeros)

print("'Média' de todos os números:", sum(numeros) / len(numeros))
print("'Maior' de todos os números:", max(numeros))
print("'Menor' de todos os números:", min(numeros))