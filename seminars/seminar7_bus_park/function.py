def read_data_from_file(name):
    result = []
    with open(name, 'r', encoding='utf-8') as datafile:
        for line in datafile:
            result.append(line.strip('\n').split(','))
        return result


def save_data_to_file(name, datalist):
    with open(name, 'w', encoding='utf-8') as datafile:
        for rawdata in datalist:
            datafile.write(','.join(rawdata)+'\n')


def print_bus():
    return read_data_from_file('bus.txt')


def add_bus():
    return


def print_driver():
    return 


def add_driver():
    return


def print_route():
    return


def add_route():
    return
