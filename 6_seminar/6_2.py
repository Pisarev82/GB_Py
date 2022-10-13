# 2. Дан список, вывести отдельно буквы и цифры.


input_str = "привет 2 раза ты поел в 3 часа 4 порции пельменей".split()
# print(type(input_str[0].isdigit()))
# def ser (x):
#     if x.isdigit(): 
#         print("Тут")
#         return True

# result_str = filter(ser, input_str)
# print(*list(result_str))

result_str = filter(lambda x: x.isdigit(), input_str)
print(*list(result_str))

result_str = filter(lambda x: not x.isdigit(), input_str)
print(*list(result_str))