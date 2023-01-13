import random as r

# Задача 106 Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента? (Добавьте игру против бота)

number_candies = 2021

def game(pl1, pl2, who_going):
    global number_candies
    game_over = False
    player = 0
    arr_players = [pl1, pl2]
    print('Первый ход делает - ', arr_players[who_going])
    while number_candies>0:
        user_number = int(input('Сколько конфет вы берёте? '))
        if (user_number > 28 and user_number < 1):
          print('Можно брать не более 28 и не менее 1 конфеты')
          break
        else:
          number_candies -= user_number
            

def init_game_candy():
    game_start = 'y'
    answer_user = input('Хотите начать игру(y/n)?')
    if answer_user.lower() == game_start:
        print('На столе лежит 2021 конфета. \nЗа один ход можно забрать не более чем 28 конфет и не менее 1 конфеты. \nВсе конфеты достаются сделавшему последний ход.')
        player_1 = input('Введите имя 1-го игрока - ')
        player_2 = input('Введите имя 2-го игрока - ')
        step = r.random()
        # if step == 1:
        #    print('первый ход делает - ', player_1)

        # else:
        #    print('первый ход делает - ', player_2)

        game(player_1, player_2, step)
    else:
        print('Ну, тогда пока!')
        return
# init_game_candy(5)
