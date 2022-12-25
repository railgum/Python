# Задача 22:
# Даны два неупорядоченных набора целых чисел(может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.

# Input: 11 6
# (значения сгенерированы случайным образом)
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18

# Output: 11 6
# 6 12
import random

# Функция заполнения списка случайными числами


def random_list(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(1, n))
    return arr

# Функция проверки пересечения двух списков


def intersection_arrays(arr_big, arr_small):
    result_arr = []
    for item in arr_small:
        if item in arr_big:
            result_arr.append(item)
    return result_arr


def func():
    n = int(input('Введите размер 1-го набора: '))
    m = int(input('Введите размер 2-го набора: '))

    # создаем список
    arr_n = random_list(n)  # создаем список
    # переводим в множество для удаления повторяющихся чисел
    arr_set_n = set(arr_n)
    arr_m = random_list(m)
    arr_set_m = set(arr_m)

    result = []
    if len(arr_set_n) > len(arr_set_m):
        result = intersection_arrays(arr_set_n, arr_set_m)
    else:
        result = intersection_arrays(arr_set_m, arr_set_n)

    print('Первый массив \n {} \nВторой массив \n {} \nПересечение \n {}'.format(
        arr_n, arr_m, result))


#func()
