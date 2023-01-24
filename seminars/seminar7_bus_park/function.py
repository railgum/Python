def read_data_from_file(name):
    result = []
    with open(name, 'r', encoding='utf-8') as datafile:
        for line in datafile:
            result.append(line.strip('\n').split(','))
        return result


def save_data_to_file(name, data):
    with open(name, 'a', encoding='utf-8') as datafile:
        datafile.write(data)


def print_bus():
    return read_data_from_file('bus.txt')


def add_bus():
    save_data_to_file('bus.txt', input('Введите номер автобуса: > '))


def print_driver():
    return


def add_driver():
    return


def print_route():
    return


def add_route():
    return
