## Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]

## write your code here
## HINT: You can use the modulo operator to find a factor

for numero in check_prime:
    count = 0
    for i in range(1, numero+1):
        if numero >= 2:
            if numero % i == 0:
                count += 1

    if count == 2:
        print(True)
    else:
        print(False)


# n = 2
#
# def eh_primo(n):
#     count = 0
#     for i in range(1, n+1):
#         if n >= 2:
#             if n % i == 0:
#                 count += 1
#     return True if count == 2 else False
#
# for i in range(1, 100):
#     is_primo = eh_primo(i)
#     if(is_primo):
#         print(f"{i} é primo")
#     else:
#         print(f"{i} não é primo")
