import random as r

# Задача 106 Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента? (Добавьте игру против бота)

number_candies = 2021


# функция игрового процесса


def game(pl1, pl2):
    global number_candies
    arr_players = [pl1, pl2]
    player = r.randint(0, 1)
    print('Первый ход делает - ', arr_players[player])
    while number_candies > 0:
        if number_candies > 28:
            if 'BOT' in arr_players:
                if arr_players[player % 2] == 'BOT':
                    # bot_number = r.randint(1, 28) # 'BOT' глуп
                    bot_number = number_candies//29  # 'BOT' не глуп)))
                    number_candies -= bot_number
                    print('BOT взял {0} конфет, осталось {1} конфет'.format(
                        bot_number, number_candies))
                    player += 1
                else:
                    user_number = int(input('Сколько конфет вы берёте? '))
                    if (user_number > 28 or user_number < 1):
                        print('Можно брать не более 28 и не менее 1 конфеты')
                        continue
                    else:
                        number_candies -= user_number
                        print('Осталось - {0} конфет'.format(number_candies))
                        player += 1
                        print('Ход переходит к игроку: ',
                              arr_players[player % 2])
            else:
                user_number = int(input('Сколько конфет вы берёте? '))
                if (user_number > 28 or user_number < 1):
                    print('Можно брать не более 28 и не менее 1 конфеты')
                    continue
                else:
                    number_candies -= user_number
                    print('Осталось - {0} конфет'.format(number_candies))
                    player += 1
                    print('Ход переходит к игроку: ', arr_players[player % 2])
        else:
            print('Игра окончена, выиграл: ', arr_players[player % 2])
            break

    init_game()

# функция старта игры и выбора игроков


def init_game(rules):
    game_start = 'y'
    answer_user = input('Хотите начать игру(y/n)?')
    if answer_user.lower() == game_start:
        print(rules)
        print('Будете играть один против бота или вдвоём(1/2)? ')
        while True:
            who_player = int(input('>'))
            if who_player == 2:
                player_1 = input('Введите имя 1-го игрока - ')
                player_2 = input('Введите имя 2-го игрока - ')
                if player_1 == player_2:
                    player_2 += '2'
                break
            if who_player == 1:
                player_1 = input('Введите имя игрока - ')
                player_2 = 'BOT'
                break
            print('Введите 1 или 2')
        game(player_1, player_2)
    else:
        print('Ну, тогда пока!')
        return


rules_candies = 'На столе лежит 2021 конфета. \nЗа один ход можно забрать не более чем 28 конфет и не менее 1 конфеты. \nВсе конфеты достаются сделавшему последний ход.\n'
init_game(rules_candies)
