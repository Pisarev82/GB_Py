# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input("Введите число "))
elements = list(range(-n, n+1))
print("список для умнажения ", elements)
positions = [1, 6, 7]
def composition_few_element(elements, positions):
    result = 1
    for i in positions:
        if 0<i<len(elements): result *=elements[i]
    return result
print(f"Произведение элементов на позициях заданных вручную: {positions}  = {composition_few_element(elements, positions)}")

file1 = open("file.txt", 'r') #
positions = file1.readlines()
file1.close()
positions = [int(i) for i in positions]
print(f"Произведение элементов на позициях прочитанных из файла: {positions}  = {composition_few_element(elements, positions)}")