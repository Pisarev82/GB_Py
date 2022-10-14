# Создайте программу для игры в ""Крестики-нолики"".
import time
game_field_size = 3
game_field = [["_" for i in range(game_field_size)] for i in range(game_field_size)]

print(*game_field, sep="\n")
turn = round(time.time())%2 == 0
print("Ход игрока? ", turn)

cr_player = "x" if turn else "o"
cr_ai = "x" if not turn else "o"

win = False

print(f"Игрок ходит {cr_player}")

def cheak_row (cr, row):
    count = 0
    for i in range(game_field_size):
        if game_field[row][i] == cr: count += 1
    return count

def cheak_col (cr, col):
    count = 0
    for i in range(game_field_size):
        if game_field[i][col] == cr: count += 1
    return count

def cheak_diag_1 (cr):
    count_list = [1 for i in range(game_field_size) if game_field[i][i] == cr]
    return sum(count_list)

def cheak_diag_2 (cr):
    count_list = [1 for i in range(game_field_size) if game_field[-i-1][i] == cr]
    return sum(count_list)

def find_winer (cr):
    for i in range(game_field_size):
        if cheak_col(cr, i) == game_field_size or \
           cheak_row (cr, i) == game_field_size or \
           cheak_diag_1 (cr) == game_field_size or \
           cheak_diag_2 (cr) == game_field_size:
            print(*game_field, sep="\n")
            print("Выиграл ", cr )
            return True
    print(cheak_diag_2 (cr))
    count = 0
    for i in game_field:
        for j in i:
            if j == "_": count += 1
    if count == 0:
        print(*game_field, sep="\n")
        print("Ничья")
        return True
    

def find_empty_in_row (row_or_col):
    for i in range(game_field_size):
        if game_field[row_or_col][i] == "_": return [row_or_col, i]

def find_empty_in_col (row_or_col):
    for i in range(game_field_size):
        if game_field[i][row_or_col] == "_": return [i, row_or_col]

def find_empty_in__diag_1 ():
    for i in range(game_field_size):
        if game_field[i][i] == "_": return [i, i]

def find_empty_in__diag_2 ():
    for i in range(game_field_size):
        if game_field[i][-i-1] == "_": return [i, -i-1]

def find_empty ():
    for i in range(game_field_size):
        for j in range(game_field_size):
            if game_field[i][j] == "_":
                return [i, j]
def ai_turn ():
    x = game_field_size - 1
    for i in range(game_field_size):
        if cheak_row(cr_ai, i) == x \
            and cheak_row(cr_player, i) == 0:
            return find_empty_in_row(i)
        if cheak_col(cr_ai, i) == x \
            and cheak_col(cr_player, i) == 0:
            return find_empty_in_col(i)
        if cheak_row(cr_player, i) == x \
            and cheak_row(cr_ai, i) == 0 :
            return find_empty_in_row(i)
        if cheak_col(cr_player, i) == x \
            and cheak_col(cr_ai, i) == 0:
            return find_empty_in_col(i)
        if cheak_diag_1 (cr_player) == x  \
            and cheak_diag_1 (cr_ai) == 0:
            return find_empty_in__diag_1()
        if cheak_diag_2 (cr_player) == x  \
            and cheak_diag_2 (cr_ai) == 0:
            return find_empty_in__diag_2()

    return find_empty ()
            # Добавить проверку выиграшей и проигрышей по диагоналям!!!!
            # cheak_row (cr, i) == game_field_size or \
            # cheak_diag_1 (cr) == game_field_size or \
            # cheak_diag_2 (cr) == game_field_size:
while not win:
    if turn: 
        user_input = list(map(int, input("Введите координаты ").split()))
        if game_field[user_input[0]-1][user_input[1]-1] == '_':
            game_field[user_input[0]-1][user_input[1]-1] = cr_player
            win = find_winer(cr_player)
        else: 
            print("Введена уже заполненния ячейка. \nПопробуйте ввести координаты еще раз: ")
            turn = not turn
    elif not turn:
        bot_input = ai_turn()
        print("Бот вводит координаты ", *bot_input)
        game_field[bot_input[0]][bot_input[1]] = cr_ai
        win = find_winer(cr_ai)
    
    if not win: print(*game_field, sep="\n")
    turn = not turn
 

