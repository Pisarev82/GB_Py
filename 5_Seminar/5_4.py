# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# 1245
# 12345
# with open('file.txt', 'r') as file:
#    listik = list(map(int, (file.read().split())))
# listik = list(map(int, (input("По просьбам").split())))
listik = list(map(int, ("1 6 7 5".split())))
i = 0
while i < len(listik)-1:
    if listik[i]+1 == listik[i+1]: 
        i += 1
    else:  listik.insert(i+1, listik[i]+1)
print(listik)