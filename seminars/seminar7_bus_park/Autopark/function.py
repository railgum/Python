def print_bus():
    bus = read_data_from_file('bus.txt')
    print('|    Имя|Госномер|')
    print('-'*19)
    for name, number in bus:
        print('|{:>7s}|{:>9s}|'.format(name, number))
    input("Enter>")


def add_bus():
    name, number = input('Название автобуса:'), input("Госномер: ")
    add_item_to_file('bus.txt', [name, number])


def print_driver():
    drivers = read_data_from_file('driver.txt')
    print('|         Имя|     Фамилия|')
    print('-'*27)
    for firstname, lastname in drivers:
        print('|{:>12s}|{:>12s}|'.format(firstname, lastname))
    input("Enter>")


def add_driver():
    firstname = input('Имя:')
    lastname = input("Фамилия: ")
    add_item_to_file('driver.txt', [firstname, lastname])


def print_route():        
    routes = read_data_from_file('marshrut.txt')
    buses = read_data_from_file('bus.txt')
    drivers = read_data_from_file('driver.txt')
    print('|Маршрут|   №|    Водитель| Госномер|')
    print('-'*37)
    for r_name,r_number,r_bus,r_driver in routes:
        bus_number = get_item_by_id(r_bus,buses)
        driver_name = get_item_by_id(r_driver,drivers)
        print('|{:>7}|{:>4}|{:>12}|{:>9}|'.format(r_name,r_number,driver_name,bus_number))    
    input("Enter>")
    

def add_route():
    route_id = input('Id маршрута:')
    route_number = input("Номер маршрута: ")
    driver_id = input("id водителя: ")
    bus_id = input("id автобуса: ")
    add_item_to_file('marshrut.txt', [route_id,route_number,driver_id,bus_id])



def read_data_from_file(name):
    rawdata_list = []
    with open(name, 'r', encoding='utf8') as datafile:
        for line in datafile:
            rawdata_list.append(line.strip('\n').split(','))
        return rawdata_list


def save_data_to_file(name, rawdata_list):
    with open(name, 'w', encoding='utf8') as datafile:
        for rawdata in rawdata_list:
            datafile.write(','.join(rawdata)+'\n')


def add_item_to_file(name, rawdata):
    with open(name, 'a', encoding='utf8') as datafile:
        datafile.write(','.join(rawdata)+'\n')


def get_item_by_id(id,records):
    for id_record,item_record in records:
        if id==id_record:
            return item_record
            break
    return None        
