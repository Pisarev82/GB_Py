#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

list = [5, 6, 8, 5, 8, 10, 5]
list1 = []
count = 0
for i in range(len(list)):
    while count < len(list):
        if list[count] == list[i] and count != i:
            count = 0
            break
        count +=1
    else:
        list1.append(list[i])
        count = 0
print(list1)

# для дз 6 
list = [5, 6, 8, 5, 8, 10, 5]
print(list(filter(lambda x: spisok.count(x) == 1, list)))





