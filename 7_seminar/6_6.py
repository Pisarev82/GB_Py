# 5. Напишите функцию triangle(a, b, c), которая принимает на вход три длины отрезков и определяет, можно ли из этих отрезков составить треугольник. 
# Входные данные
# Выходные данные
# triangle(1, 1, 2)
# Это не треугольник
# triangle(7, 6, 10)

triangle = lambda a,b,c: print('Это треугольник') if a+b>c and c+b>a and a+c>b else print('Как говорил Шарик: индийский дом')

triangle(7,6,10)


phone_book = read_csv('phonebook.csv')

def read_csv(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)

    return data

контролер
вью
майн
модель



def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Закончить работу")
    choice = int(input())
    return choice
