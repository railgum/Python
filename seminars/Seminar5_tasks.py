import math
import random as r
# Задача
# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
#transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.


def check_list():
    values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    transormed_values = list(map(lambda x: x, values))
    if values == transormed_values:
        print('ok')
    else:
        print('fail')
    # print(values)
    # print(transormed_values)

# check_list()


# Задача
# Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту, по которой вращается самая далекая планета. Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, зато искусственные спутники были запущены на круговые орбиты. Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса. При решении задачи используйте списочные выражения. Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс, имеющий такую площадь. Гарантируется, что самая далекая планета ровно одна


def find_farthest_orbit(list_of_orbits):
    # убираем круглые орбиты
    res = [x for x in list_of_orbits if x[0] != x[1]]
    # 1 вариант
    #list_area_max = max(map(lambda x: math.pi*x[0]*x[1], res))
    #res = [x for x in res if math.pi*x[0]*x[1]==list_area_max]
    # return res

    # 2 вариант
    #list_area = list(map(lambda x: math.pi*x[0]*x[1], res))
    #index_max = list_area.index(max(list_area))
    # return res[index_max]


#print(*find_farthest_orbit([(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]))


# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True, если это так. Если значение характеристики для разных объектов отличается - то False. Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.

values = [0, 4, 8, 2, 12, 6]


def same_by(characteristic, objects):
    res_list = set(map(characteristic, objects))
    return len(res_list) <= 1

# print(values)
#print(same_by(lambda x: x % 2, values))

# if same_by(lambda x: x % 3, values):
#    print('same')
# else:
#    print('different')


# for i in range(21):

#    player = (r.randint(0, 1))
#    print(player)
