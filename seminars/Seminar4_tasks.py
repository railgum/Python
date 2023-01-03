import re
import math
import random

# Напишите программу, которая принимает на вход строку,
# и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2


def counting_char_string(string):
    char_dict = {}
    char_arr = string.split()
    print(char_arr)
    res = ''
    for symbol in char_arr:
        if symbol in char_dict:   # ключи словаря - символы(буквы)
            char_dict[symbol] += 1  # если в словаре есть ключ, добавляем ему
            # новое значение
            # составляем строку из новых значений словаря
            res += symbol + '_' + str(char_dict[symbol]) + ' '
        else:
            char_dict[symbol] = 0  # если ключа нет - добавляем его
            res += symbol + ' '   # ноль не выводим

    return res

# print(counting_char_string('a a a b c a a d c d d'))


# Пользователь вводит текст(строка). Словом считается последовательность
# непробельных символов идущих подряд, слова разделены одним или большим
# числом пробелов. Определите, сколько различных слов содержится в этом тексте.

# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells

# Output: 13
# import re

# def delete_point(string):
#    while True:
#        if string.endswith('.'):
#            string = string[0:len(string) - 1]
#        else:
#            return string

def count_words(string):
    string = string.replace('.', ' ').replace(';', ' ').replace(',', ' ')
    # string = string.replace(';', ' ')

    print(string)
    words_arr = set(string.lower().split())  # (' |;|.')

    # for word in words_arr:
    #    delete_point(word)   # не работает
    print(words_arr)
    return len(words_arr)


s = "She sells sea shells on the sea shore; \
  The shells that she sells are sea shells I'm sure. \
    So if she sells sea shells on the sea shore. \
    I'm sure that the shells are sea shore shells."

# print(count_words(s))


# Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность неотрицательных целых чисел. Требуется определить значение наибольшего элемента последовательности, которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”. Однако 2 друга оказались не такими смышлеными. Никто из ребят не смог до конца сделать это задание. Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. За помощью товарищи обратились к Вам, студентам.

# Ваня

def max_number_sequence():
    result_arr = []
    n = int(input('Введите целое положительное число: '))
    while n != 0:
        n = int(input('Введите следующее число: '))
        if n < 0:
            print('Число должно быть положительным!')
        else:
            result_arr.append(n)
    return result_arr


# print(max(max_number_sequence()))

# Петя
def max_number_sequence_2():
    n = int(input('Введите целое положительное число: '))
    max_number = n
    while n != 0:
        if max_number < n:
            max_number = n
        n = int(input('Введите следующее число: '))
    return max_number

# print(max_number_sequence_2())


# Задача 101 Вычислить число π c заданной точностью d

# Пример:
# при d = 0.001, π = 3.141    0.1 ≤ d ≤ 0.00000000001


def given_accuracy_pi(d):
    if (d > 0.1 or d < 0.00000000001):
        print('Точность вне установленного диапазона')
    else:
        discharge = len(str(1-d))
        result = ''
        for digit in range(discharge):
            result += str(math.pi)[digit]
        return result

# d = float(input('Введите точность для числа PI(0.1 ≤ d ≤ 0.00000000001): '))
# print(given_accuracy_pi(d))


# Задача 102
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.



# Задача 103
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл file1.txt многочлен степени k.

# Пример:  k=2

# Возможные варианты многочленов:
# 2*x*x + 4*x + 5 = 0
# x*x + 5 = 0
# 10*x*x = 0

# функция рандомных значений множителя многочленов
def random_list_digit(k):
    arr = []
    for i in range(k+1):
        arr.append(random.randint(0, 100))
    return arr

# функция рандомных значений знаков многочленов


def random_list_operator(k):
    arr = []
    for i in range(k):
        arr.append(round(random.random()))
        if arr[i] == 1:
            arr[i] = '+'
        else:
            arr[i] = '-'
    return arr


# словарь многочленов по степеням


def polinomial():
    k = int(input('Введите степень многочлена: '))
    poli_digit = random_list_digit(k)
    # print(poli_digit)
    poli_operator = random_list_operator(k)
    # print(poli_operator)

    result = {}
    for item in range(len(poli_digit)):
        if poli_digit[item] == 0:
            result[item] = ''
        elif poli_digit[item] == 1 and len(poli_digit)-1 != item \
                and len(poli_digit)-2 != item:
            result[item] = 'x^' + str(len(poli_digit)-item-1)
        elif len(poli_digit)-2 != item and len(poli_digit)-1 != item:
            result[item] = str(poli_digit[item])+'*x^' + \
                str(len(poli_digit)-item-1)
        elif len(poli_digit)-2 == item and poli_digit[item] != 1:
            result[item] = str(poli_digit[item]) + '*x'
        elif len(poli_digit)-2 == item and poli_digit[item] == 1:
            result[item] = 'x'
        elif len(poli_digit)-1 == item and poli_digit[(len(poli_digit)-1)] != 0:
            result[item] = str(poli_digit[item])
        else:
            result[item] = ''
    # print(result)
  # составление строки многочлена (можно сделать отдельную функцию)
    result_poli_string = ''
    for i in range(len(result)):
        if result[i] == '':
            result_poli_string += ''
        elif i == (len(result)-1):
            result_poli_string += result[i]
        else:
            result_poli_string += result[i] + poli_operator[i]

    # убираем знак, если после него ничего нет
    # print(result_poli_string[-1])
    if (result_poli_string[-1] == '-') or (result_poli_string[-1] == '+'):
        result_poli_string = result_poli_string[:-1]
    return (result_poli_string+'=0')


# записываем в два файла
with open('seminars/file1.txt', 'w+') as f1:
    f1.write(polinomial())
with open('seminars/file2.txt', 'w+') as f2:
    f2.write(polinomial())

# Задача 104
# Даны два файла file1.txt и file2.txt, в каждом из которых находится запись многочлена(полученные в результате работы программы из задачи 103). Необходимо сформировать файл file_sum.txt, содержащий сумму многочленов.

# функция разделения многочлена на составляющие


def extract_polinomial_from_file(file):

  # читаем из файла
    with open(file) as f:
        str_file = f.readline()
        print(str_file)

        # с помощью регулярного выражения разделяем
        arr_file = re.split(r"(\*x\^\d)|(\*x)|(\=)|(x\^\d)|x", str_file)

        # удаляем None
        result_arr = []
        for i in arr_file:
            if i != None:
                result_arr.append(i)

        # добавляем множители в случае их отсутствия
        for index, item in enumerate(result_arr):
            if item == '' and index != (len(result_arr)-3):
                result_arr[index] = '1'
            elif item == '-':
                result_arr[index] = '-1'
            elif item == '+':
                result_arr[index] = '+1'

        # print(result_arr)
        # преобразуем в словарь (можно работать со списком)
        result_dict = {}
        for i in range(1, int(len(result_arr)/2+1)):
            result_dict[result_arr[(i*2)-1]] = result_arr[(i-1)*2]
        # print(str(result_dict))
        return result_dict


list_1 = extract_polinomial_from_file('seminars/file1.txt')
list_2 = extract_polinomial_from_file('seminars/file2.txt')

# функция сложения многочленов


def sum_polinomial(list_1, list_2):
  # если в каком-либо многочлене отсутствуют элементы, добавляем
    for key in list_1.keys():
        if key in list_2.keys():
            list_1[key] = str(int(list_1[key]) + int(list_2[key]))
    # print(list_1)

    # суммируем
    result_sum = ''
    key_list = list(list_1)
    for key, value in list_1.items():
        # print(key_list.index(key))
        if key_list.index(key) == 0 or value[0] == '-':
            result_sum += value + key
        else:
            result_sum += '+' + value + key

    # если сумма последних элементов равна 0, удаляем
    if list(list_1.values())[-1] == '0':
        result_sum = result_sum[:-3]
        result_sum += '=0'
        return result_sum
    else:
        return (result_sum + '0')


print(sum_polinomial(list_1, list_2))

# записываем в файл
with open('seminars/file_sum.txt', 'w+') as f3:
    f3.write(sum_polinomial(list_1, list_2))



#Задача 105 Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

#Задача 106 Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента? (Добавьте игру против бота)

#Задача 107 Создайте программу для игры в ""Крестики-нолики"" (Добавьте игру против бота)

#Задача 108 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных (модуль в отдельном файле, импортируется как библиотека)
#метод Упаковка: на вход подается текстовый файл, на выходе текстовый файл со сжатием.
#метод Распаковка: на вход подается сжатый текстовый файл, на выходе текстовый файл восстановленный.
#Прикинуть достигаемую степень сжатия (отношение количества байт сжатого к исходному).