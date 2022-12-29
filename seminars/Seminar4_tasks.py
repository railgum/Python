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


# Задача 102 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


# Задача 103 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл file1.txt многочлен степени k.

# Пример:  k=2

# Возможные варианты многочленов:
# 2*x*x + 4*x + 5 = 0
# x*x + 5 = 0
# 10*x*x = 0

def random_list_digit(k):
    arr = []
    for i in range(k+1):
        arr.append(random.randint(0, 100))
    return arr


def random_list_operator(k):
    arr = []
    for i in range(k):
        arr.append(round(random.random()))
        if arr[i] == 1:
            arr[i] = '+'
        else:
            arr[i] = '-'
    return arr


# print(random_list_operator(4))

def polinomial():
    k = int(input('Введите степень многочлена: '))
    poli_digit = random_list_digit(k)
    poli_digit_end = poli_digit[len(poli_digit)-1]
    print(poli_digit)
    poli_operator = random_list_operator(k)
    print(poli_operator)
    #result = ''
    # for item in range(len(poli_operator)):
    #    result += ' ' + str(poli_digit[item])+'*x^' + \
    #        str(len(poli_digit)-item-1) + ' ' + poli_operator[item]
    # return (result + str(poli_digit_end)+' = 0')
    result = {}
    for item in range(len(poli_operator)):
        if poli_digit[item] == 0:
            result[item] = ''
        elif str(len(poli_digit)-item-1) == '1':
            result[item] = str(poli_digit[item])+'*x' + poli_operator[item]
        else:
            result[item] = str(poli_digit[item])+'*x^' + \
                str(len(poli_digit)-item-1) + poli_operator[item]
    return result


print(polinomial())
