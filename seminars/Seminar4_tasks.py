import math

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

#d = float(input('Введите точность для числа PI(0.1 ≤ d ≤ 0.00000000001): '))
# print(given_accuracy_pi(d))


