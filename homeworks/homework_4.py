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


# func()

# Задача 24:
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.

# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

#Input: 4
# (значения сгенерированы случайным образом
# 4 2 3 1)

#Output: 9


# Заполнение кустов случайным кол-вом ягод
def random_list(n):
    arr = []
    for i in range(n):
      # не нашел, сколько ягод на кусте, хардкодим
        arr.append(random.randint(1, 20))
    return arr

def karelia_farm():
    quantity = int(input('Введите количество кустов на ферме: '))
    capacity = int(input('Введите количество кустов за один заход: '))
    blueberry_arr = random_list(quantity)
    print(blueberry_arr)

    # чтобы не было ошибки списка
    # result = blueberry_arr[0] + \
    #    blueberry_arr[len(blueberry_arr)-1] + \
    #    blueberry_arr[len(blueberry_arr)-2]

    result = 0
    for i in range(capacity):
        result += blueberry_arr[-i]
    #print(result)
    
    # проходим по списку, исключая capacity последних элемента
    for i in range(len(blueberry_arr)-capacity+1):
        sum = 0
        #print(i)
        for j in range(i, i+capacity):
            sum += blueberry_arr[j]
        #print(sum)
        if sum > result:
            result = sum

    return result


#print(karelia_farm())
