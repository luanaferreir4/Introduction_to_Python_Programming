num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
impares = []
i = 0

while len(impares) < 5:
    if num_list[i] % 2 != 0:
        impares.append(num_list[i])
    i += 1
print(impares)