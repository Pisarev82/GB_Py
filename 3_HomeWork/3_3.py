# Задайте список из вещественных чисел. Напишите программу, которая 
# найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
list1 = [1.1, 1.2, 3.1, 5.0, 10.01]
# list3 = []
# for i in range(len(list1)):
#     if round((list1[i] - int(list1[i])), 2) != 0:
#         list3.append(round((list1[i] - int(list1[i])), 2))
# print(max(list3) -  min(list3))

list2 = [round((list1[i] - int(list1[i])), 2) for i in range(len(list1)) if round((list1[i] - int(list1[i])), 2) != 0]
print(max(list2) -  min(list2))