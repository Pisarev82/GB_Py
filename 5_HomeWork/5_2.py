# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
import time

candies = 100
count = 0
turn_player =  round(time.time())%2 == 0
player_name = input("Введите имя игрока: ")

bot_name = "Д.Ж.А.Р.В.И.С."

print("Первым ходит ", player_name if turn_player else bot_name)

def checking_move (number, name):
    if 0 < number < 29: return number
    else: 
        print(name, "загадал недопустумое значение. Ход приравнен к 1 кофете.")
        return 1

while candies > 0:
    print("Осталось конфет ", candies)
    if turn_player:
        candies -= checking_move(int(input(player_name + ", введите колличество конфет ")), player_name)
        turn_player = not turn_player
    else:
        print(f"{bot_name} забирает {candies%29} конфет " )
        candies -= checking_move(candies%29, player_name)
        turn_player = not turn_player

print("Выиграл ", bot_name if turn_player else player_name)
