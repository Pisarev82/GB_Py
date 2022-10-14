# Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, значения — списки,
# содержащие имена, начинающиеся с соответствующей буквы.
# in "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
# out {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}

# input_list = ["Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"]
# # x = lambda i: i[0]
# # input_list.sort()
# # print(type(input_list))
# out_dict = {i[0]: [j for j in input_list if j[0] == i[0] ]  for i in input_list.sort()}
# print(out_dict)

# input_list = [2, 1, 3]
# # input_list.sort()
# # out_list = [i+i for i in input_list]
# # print(out_list)
# out_list = [i+i for i in list.sort(input_list)]
# print(out_list)

for i in range(3):
    print(i)