# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и 
# записать в файл многочлен степени k.
# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import *

k=2

a = round(random()*10, )
b = round(random()*10, )
c = round(random()*10, )
print(a, b, c)
result = ''
if b == 0: result = f"{a}*x**{k} + {c}*x**{k-2} = 0"
if b == 0 and c == 0: result =  f"{a}*x**{k} = 0"
# if c == 0: result = f"{a}*x**{k} + {b}*x**{k-1} = 0 "
else: result =  f"{a}*x**{k} + {b}*x**{k-1} + {c}*x**{k-2} = 0 "

with open("file444.txt", "w") as file44:
    file44.write(result)



# b = int(input('Введите число заначений:'))
# a = [random.randint(0,10) for _ in range(b)]
