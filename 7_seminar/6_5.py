# Вводится строка. Требуется, используя введенную строку, сформировать N=10 пар кортежей в формате:

# (символ, порядковый индекс)

# Первый индекс имеет значение 0. Строка может быть короче 10 символов, а может быть и длиннее. 
# То есть, число пар может быть 10 и менее. Используя функцию zip сформируйте указанные кортежи и сохраните в список с именем lst.

inp_string=input('')

zipper = [i for i in range(11)]

result = list(zip(inp_string, zipper))

print(*result)
