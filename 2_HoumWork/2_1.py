# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:

# - 6782 -> 23
# - 0,56 -> 11

data1 = input("Введите число ")

#Короткое решение
print(sum([int(i) for i in data1 if i.isdigit()]))

#Стандартное решение
numbers = []
for i in data1:
    if i.isdigit(): numbers.append(int(i))
print(sum(numbers))