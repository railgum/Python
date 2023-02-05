import os

matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def show_matrix():
    return (f'{matrix[0]} {matrix[1]} {matrix[2]}\n{matrix[3]} {matrix[4]} {matrix[5]}\n{matrix[6]} {matrix[7]} {matrix[8]}')
    # print(matrix[0], matrix[1], matrix[2])
    # print(matrix[3], matrix[4], matrix[5])
    # print(matrix[6], matrix[7], matrix[8])


def check_win():
    if matrix[0] == matrix[1] == matrix[2]:
        print(f'Победили {matrix[0]}!')
        return 1
    elif matrix[3] == matrix[4] == matrix[5]:
        print(f'Победили {matrix[3]}!')
        return 1
    elif matrix[6] == matrix[7] == matrix[8]:
        print(f'Победили {matrix[6]}!')
        return 1
    elif matrix[0] == matrix[3] == matrix[6]:
        print(f'Победили {matrix[0]}!')
        return 1
    elif matrix[1] == matrix[4] == matrix[7]:
        print(f'Победили {matrix[1]}!')
        return 1
    elif matrix[2] == matrix[5] == matrix[8]:
        print(f'Победили {matrix[2]}!')
        return 1
    elif matrix[0] == matrix[4] == matrix[8]:
        print(f'Победили {matrix[0]}!')
        return 1
    elif matrix[2] == matrix[4] == matrix[6]:
        print(f'Победили {matrix[2]}!')
        return 1
    else:
        return 0


def player(text):
    while True:
        try:
            number = int(text)

            if (matrix[number-1] != 'X') and (matrix[number-1] != '0'):
                matrix[number-1] = 'X'
                break
            else:
                print('Ячейка занята')
                # break
        except:
            print('Неверный ввод')
            break


def comp(matrix):
    for i in range(len(matrix)):
        if matrix[i] != 'X' and matrix[i] != '0':
            matrix[i] = '0'
            return


# while True:
#    os.system('cls')
#    show_matrix()
#    player(text)
#    os.system('cls')
#    show_matrix()
#    if check_win():
#        break
#    comp(matrix)
#    os.system('cls')
#    show_matrix()
#    if check_win():
#        break
