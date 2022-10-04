# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
k=8
list_negafib = [1, 0]
for i in range(k):
    list_negafib.insert(0, list_negafib[1] - list_negafib[0])
for i in range(k+1):
    list_negafib.append(list_negafib[-2] + list_negafib[-1])

print(list_negafib)