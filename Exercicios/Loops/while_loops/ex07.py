def fibonacci(n):

    fibonacci_list = [0, 1]
    i = 0

    while i < n:
        ult = fibonacci_list[-1]
        penult = fibonacci_list[-2]
        fibonacci_list.append(penult + ult)
        i += 1
    return fibonacci_list

print(fibonacci(10))

