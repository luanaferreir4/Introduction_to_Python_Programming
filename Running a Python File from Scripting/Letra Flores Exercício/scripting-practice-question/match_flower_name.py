# Write your code here

# HINT: create a dictionary from flowers.txt
with open('flowers.txt') as arquivo:
    delimitador = ': '
    flores = {}
    for linha in arquivo:
        lista = linha.rstrip('\n').split(delimitador)
        flores[lista[0]] = lista[1]
    print(flores)
# HINT: create a function to ask for user's first and last name
if __name__ == '__main__':
    name = input('Coloque seu primeiro [espaço] e último nome apenas: ')
    for letra, flor in flores.items():
        if name[0].upper() == letra:
            print('Unico nome de flor com a primeira letra:', flor)

# print the desired output 

