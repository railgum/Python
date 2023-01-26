import random as r
import os


def read_data_from_file(name):
    result = []
    with open(name, 'r', encoding='utf-8') as datafile:
        for line in datafile:
            result.append(line.strip('\n').split(','))
        return result


def save_data_to_file(name, data1, data2):
    with open(name, 'a', encoding='utf-8') as datafile:
        datafile.write(f'{data1}, {data2}\n')


def print_bus():
    os.system('cls')
    for i in read_data_from_file('bus.txt'):
        print(i)
    input('Enter для продолжения')


def add_bus():
    number_bus = input('Введите порядковый номер автобуса: > ')
    car_number = input('Введите госномер: > ')
    save_data_to_file('bus.txt', 'bus'+number_bus, car_number)
    print_bus()


def print_driver():
    os.system('cls')
    for i in read_data_from_file('driver.txt'):
        print(i)
    input('Enter для продолжения')


def add_driver():
    number_driver = input('Введите условный номер водителя: > ')
    lastname_driver = input('Введите фамилию водителя: > ')
    save_data_to_file('driver.txt', 'driver'+number_driver, lastname_driver)
    print_driver()


def print_route():
    os.system('cls')
    for i in read_data_from_file('route.txt'):
        print(i)
    input('Enter для продолжения')


def add_route():
    count_route = len(read_data_from_file('route.txt'))
    list_route = read_data_from_file('route.txt')
    list_bus = print_bus()
    list_driver = print_driver()
    while True:
        number_route = r.randint(1, 50)
        for _ in list_route:
            if number_route != list_route[1]:
                break
            else:
                print('Доступных маршрутов нет!')
        break
    name = f'm{count_route+1}, {number_route}'
    rand_bus = list_bus[r.randint(0, len(list_bus)-1)][0]
    rand_driver = list_driver[r.randint(0, len(list_driver)-1)][0]
    save_data_to_file('route.txt', f'{name}, {rand_bus}', rand_driver)
    print_route()


# print(add_route())
