import random

# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X
# в массиве A[1..N]. Пользователь вводит натуральное число N – количество
# элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.

# Ввод: 5
# Ввод: 1

# 1 2 1 2 2
# Вывод: 2


def random_list_half(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(1, n//2))
    return arr


def check_number_for_array():
    number_elements = int(input('Введите размер массива: '))
    number = int(input('Введите искомое число: '))
    example_list = random_list_half(number_elements)
    count = 0
    for i in range(len(example_list)):
        if example_list[i] == number:
            count += 1
    return (example_list, count)


#arr, count = check_number_for_array()
# print(arr)
# print(count)

# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в
# массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов,
# которые равноудалены от X, выведите наименьший по величине.

# Ввод: 10
# Ввод: 7
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6


def random_list(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(1, n))
    return arr


def get_nearest_number_for_array():
    number_elements = int(input('Введите размер массива: '))
    number = int(input('Введите искомое число: '))
    example_list = random_list(number_elements)
    print(example_list)
    #example_list = [1, 2, 1, 8, 9, 6, 5, 4, 3, 4]
    number_min = example_list[0]
    number_max = number_min
    for i in example_list:
        if i == number:
            return number
        else:
            if abs(i - number) < abs(number_max - number):
                number_max = i
            if i < number and i >= number_min:
                number_min = i
    if (number_max - number) < (number - number_min):
        return number_max
    else:
        return number_min


# print(get_nearest_number_for_array())

# Задача 20:
# В настольной игре Скрабл(Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко
# D, G – 2 очка
# B, C, M, P – 3 очка
# F, H, V, W, Y – 4 очка
# K – 5 очков
# J, X – 8 очков
# Q, Z – 10 очков.

# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко
# Д, К, Л, М, П, У – 2 очка
# Б, Г, Ё, Ь, Я – 3 очка
# Й, Ы – 4 очка
# Ж, З, Х, Ц, Ч – 5 очков
# Ш, Э, Ю – 8 очков
# Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово,
# которое содержит либо только английские, либо только русские буквы.

# Ввод: ноутбук
# Вывод: 12

def calculating_letter_cost(letter):
    if letter in ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R']:
        return 1
    elif letter in ['D', 'G']:
        return 2
    elif letter in ['B', 'C', 'M', 'P']:
        return 3
    elif letter in ['F', 'H', 'V', 'W', 'Y']:
        return 4
    elif letter in ['K']:
        return 5
    elif letter in ['J', 'X']:
        return 8
    elif letter in ['Q', 'Z']:
        return 10
    elif letter in ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']:
        return 1
    elif letter in ['Д', 'К', 'Л', 'М', 'П', 'У']:
        return 2
    elif letter in ['Б', 'Г', 'Ё', 'Ь', 'Я']:
        return 3
    elif letter in ['Й', 'Ы']:
        return 4
    elif letter in ['Ж', 'З', 'Х', 'Ц', 'Ч']:
        return 5
    elif letter in ['Ш', 'Э', 'Ю']:
        return 8
    elif letter in ['Ф', 'Щ', 'Ъ']:
        return 10


def Scrabble(word):
    cost = 0
    letters = list(word.upper())
    for letter in letters:
        cost += calculating_letter_cost(letter)
    return cost


w = input('Введите слово: ')
print(Scrabble(w))
