# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


n = int(input("Введите число "))

#Короткое решение
from math import factorial
print([factorial(i) for i in range(1,n+1)])

#Стандартное решение
numbers = []
for i in range(n):
    if i == 0: numbers.append(1)
    else: numbers.append(numbers[i-1]*(i+1))
print((numbers))

