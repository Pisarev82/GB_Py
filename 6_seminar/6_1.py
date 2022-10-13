# 1.Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа. 
# Реализовать программу с использованием функции filter. 
# Результат отобразить на экране в виде последовательности оставшихся чисел в одну строчку через пробел.

# input_list = list(map(int, "1 25 2 32 3 33 1".split()))
# print(input_list)
# def ser (x):
#     if 0 < x < 100: return True

# result = filter(ser, data)
# print(*list(result))

# result_1 = filter(lambda x: x > 9, input_list)
# print(*list(result_1))

e = lambda x: len(x) == 2
st = '2 32 34 5 43 2 4 34'.split()
res = list(filter(e, st))
print(*res)


st = '2 32 34 5 43 2 4 34'.split()
res = [x for x in st if len(x) == 2]
print(*res)