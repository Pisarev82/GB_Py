# Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников.
#  Теперь он использует их в качестве серверов "Пегого дудочника". Помогите владельцу фирмы отыскать все зараженные холодильники.
# Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, и если в ней присутствует слово "anton" 
# (необязательно рядом стоящие буквы, главное наличие последовательности букв),
# то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы
# Формат входных данных
# В первой строке подаётся число 
# n
# n – количество холодильников. В последующих 
# n
# n строках вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке от 
# 5
# 5 до 
# 100
# 100 символов.

# Формат выходных данных
# Программа должна вывести номера зараженных холодильников через пробел. Если таких холодильников нет, ничего выводить не нужно.

data_list  = ['osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen', 'anton', 'aoooooooooontooooo', 'elelelelelelelelelel', 'ntoneeee', 'tonee', '253235235a5323352n25235352t253523523235oo235523523523n', 'antoooooooooooooooooooooooooooooooooooooooooooooooooooon', 'unton']
name1 = "anton"

def find_word(name1, data):
    result = []
    count = 0
    for i in data:
        for j in range(count, len(name1)):
            count += 1
            if i == name1[j]:
                result.append(i)
                break
    print(result)
    if result == list(data) :
        return True
    else: 
        return False

for i in range(len(data_list)):
    if find_word(data_list[i], name1): print(i+1, end=", ")

# print(find_word('aoooooooooontooooo', name1))


