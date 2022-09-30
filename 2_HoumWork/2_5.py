# Реализуйте алгоритм перемешивания списка.
import random
order_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#Короткое решение

random.shuffle(order_list)
print(order_list)

#Стандартное решение 
count = 0
while count<len(order_list)*5:
    random_index_1 = random.randrange(len(order_list))
    random_index_2 = random.randrange(len(order_list)-1)
    order_list[random_index_1], order_list[random_index_2] = order_list[random_index_2], order_list[random_index_1]
    count += 1
print(order_list)