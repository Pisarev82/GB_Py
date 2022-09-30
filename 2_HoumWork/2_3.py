# Задайте список из n чисел последовательности (1+ 1 / n)**n и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 2, 2: 2, 3: 2, 4:2, 5: 2, 6: 3} -> 13

n = int(input("Введите число: "))

# Короткое решение

sequence_list = {i:round((1+ 1 / i)**i) for i in range(1, n+1)}
print(sequence_list, "Сумма значений: ", sum(sequence_list.values()))

# Стандартное решение
sequence_list = {}
sum_of_sequence_list_valio = 0
for i in range(1, n+1):
    sequence_list[i] = round((1+ 1 / i)**i)
    sum_of_sequence_list_valio += sequence_list[i]
print(sequence_list, "Сумма значений: ", sum_of_sequence_list_valio)