# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
with open("delete_abv.txt", "w") as file:
    file.write('Напабвишите программу, удаляющую абвиз текста все слоабвва, содержащие ""абв"".') 
with open("delete_abv.txt", "r") as file:
    text = file.read()
print(text)
data_list = text.split()
result = " ".join([i for i in data_list if "абв" not in i])
with open("delete_abv.txt", "a") as file:
    file.write("\n Результат \n" + result) 
print(result)