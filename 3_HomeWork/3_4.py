# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
x = 5
y = str(bin(x))
print("Я строка: ", y[2:])
print("Я число: ", int(y[2:]))

