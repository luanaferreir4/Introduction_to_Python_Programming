# Raw input para strings (trechos de textos):

# 1
name = input('Enter a name: ')
print('Hello,', name.title())

# 2
name = input('Enter a name: ')
print('Hello,', name.title())

# Raw input para números inteiros:
number = int(input('Enter a number: '))
number += 20
print(number)

# Raw input para números flutuantes:
number = float(input('Enter a number: '))
number += 20
print(number)

# para repetir a mesma frase quantas vezes quiser:
print(name * 10)

# Também podemos interpretar a entrada do usuário como
# uma expressão Python usando a função integrada eval.
# Esta função avalia uma string como uma linha do Python.

result = eval(input('Enter an expression: '))
print(result)

# Também podemos usar eval assim:
num = 30
x = eval('num + 42')
print(x)