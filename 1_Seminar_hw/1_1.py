# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
number_day_of_week = int(input("Введите день недели: "))
print(f"- {number_day_of_week} -> ", end='')
if 6<=number_day_of_week<=7: print('да')
elif 1<=number_day_of_week<=5: print('нет')
else: print("Не является числовым обозначением дня недели.:-(")