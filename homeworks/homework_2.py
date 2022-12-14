import random
import math

# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2


def coins(n):
    heads = 0
    coin = []
    for i in range(n):
        coin.append(round(random.random()))  # бросаем монетки
        if coin[i] == 0:
            heads += 1                      # считаем решки
    print(n, '-->', coin)
    if heads < n//2:                        # проверяем, чего меньше
        return heads                        # орлов или решек и
    else:                                   # возвращаем результат
        return (n - heads)

# print(coins(5))

# Задача 12
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.


def equation_system(s, p):
    if (p >= 1000000 and p < 0):
        print('Числа не соответствуют диапазону(0-1000)')
    else:
      # решение через систему уравнений:
      # x + y = s и x * y = p
      # x^2 - sx + p = 0
      # проверка дискриминант > 0 - 2 корня
      # d = 0 - 1 корень(числа равны)
      # d < 0 - не чисел, удовлетв. условию
      # корни - ответы
        discriminant = (math.pow(s, 2) - 4*p)
        if discriminant > 0:
            number_1 = round((s+math.sqrt(discriminant))/2)
            number_2 = round((s-math.sqrt(discriminant))/2)
        elif discriminant == 0:
            number_1 = round((s+math.sqrt(discriminant))/2)
            number_2 = number_1
        else:
            print('Числа невозможно получить')
    return number_1, number_2

#print(equation_system(115, 1500))

# Задача 14
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.


def degree_two(n):
    arr = []
    if n < 0:
        print('Введите целое положительное число')
    else:
        i = 0
        while math.pow(2, i) < n:
            arr.append(i)
            i += 1
    return arr
# print(degree_two(100))
