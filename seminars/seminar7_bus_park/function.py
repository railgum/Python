import random as r


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
    return read_data_from_file('bus.txt')


def add_bus():
    number_bus = input('Введите порядковый номер автобуса: > ')
    car_number = input('Введите госномер: > ')
    save_data_to_file('bus.txt', number_bus, car_number)


def print_driver():
    return read_data_from_file('driver.txt')


def add_driver():
    number_driver = input('Введите условный номер водителя: > ')
    lastname_driver = input('Введите фамилию водителя: > ')
    save_data_to_file('driver.txt', number_driver, lastname_driver)


def print_route():
    return read_data_from_file('route.txt')


def add_route():
    count_route = len(read_data_from_file('route.txt'))
    list_route = read_data_from_file('route.txt')
    while True:
        number_route = r.randint(1, 50)
        for _ in list_route:
            if number_route != list_route[1]:
                break
            else:
                print('Доступных маршрутов нет!')
        break
    name = f'm{count_route+1}, {number_route}'
    rand_bus = # lambda x: 
    return name


print(add_route())
