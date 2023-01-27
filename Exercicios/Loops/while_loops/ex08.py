num = float(input('Digite um numero: '))
soma = 0
count = 0

while num != 999:
    soma += num
    count += 1
    num = float(input('Digite um numero: '))

print("Soma dos números:", soma)
print("Quantidade de números:", count)