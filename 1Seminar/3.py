
# Напишите программу, которая будет принимать на вход дробь и 
# показывать первую цифру дробной части числа.
#     *Примеры:*   
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3
# 3. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

input_n = int(input("Введите N "))

if input_n < 0: n = -input_n
else: n = input_n
for i in range(-n,n+1):
    print(f"{i} ", end='')
