import os
# Задача
# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Структура данных:
# Фамилия, имя, отчество, номер телефона.

# Пример данных:
#Ivanov, Ivan, Ivanovich, +79111234567
#Petrov, Petr, Petrovich, +79119876543

# Функции справочника:
# - Показать все записи
# - Найти запись по вхождению частей имени
# - Найти запись по телефону
# - Добавить новый контакт
# - Удалить контакт
# - Изменить номер телефона у контакта

# Пример работы программы:

# При запуске программы пользователю выдается меню:

# Введите номер действия:
# 1 - Показать все записи
# 2 - Найти запись по вхождению частей имени
# 3 - Найти запись по телефону
# 4 - Добавить новый контакт
# 5 - Удалить контакт
# 6 - Изменить номер телефона у контакта
#7 - Выход

# После выбора действия выполняется функция, реализующая это действие.
# После завершения работы функции пользователь возвращается в меню.


file_name = 'phone_book.txt'


def read_file():
    result = []
    with open(file_name, 'r', encoding='utf-8') as data:
        for line in data:
            result.append(line.strip('\n').split(','))
    return result


def search_user_name(user_list, name):
    result = []
    count = 0
    for user in user_list:
        for j in user:
            if j.find(name) != -1:
                result.append(user)
                count += 1
                break
    return (result, count)


def search_user_phone(user_list, number):
    result = []
    for user in user_list:
        if user[3] == number:
            result.append(user)
    return result


def add_user():
    last_name = input('Введите фамилию')
    first_name = input('Введите имя')
    patronymic = input('Введите отчество')
    phone_number = input('Введите номер')

    data_collection = [last_name, first_name, patronymic, phone_number]
    write_file(data_collection)


def write_file(text):
    text = ','.join(text)
    with open(file_name, 'a', encoding='utf8') as data:
        data.writelines(text + '\n')


def delete_user():
    with open(file_name, 'r', encoding='utf-8') as r:
        data = r.readlines()
        data_num = list(enumerate(data))
        for line in data_num:
            print('>> {0} : {1}'.format(line[0]+1, line[1].strip('\n')))
        print('Всего: {0} записей'.format(len(data_num)))
        num_del = int(
            input('Введите номер записи, которую хотите удалить? > '))

    with open(file_name, 'w', encoding='utf-8') as w:
        for line in data_num:
            if line[0]+1 != num_del:
                w.write(line[1])
    return ('Осталось : {0} записей'. format(len(data_num)))


def change_number():
    with open(file_name, 'r', encoding='utf-8') as r:
        data = r.readlines()
        data_num = list(enumerate(data))
        # print(type(data_num))
        for line in data_num:
            print('>> {0} : {1}'.format(line[0]+1, line[1].strip('\n')))
        print('Всего: {0} записей'.format(len(data_num)))
        num_change = int(
            input('Введите номер записи, которую хотите изменить? > '))
        data_user = data_num[num_change-1][1].strip('\n').split(',')
        print(data_user)
        phone_change = input('Введите новый номер > ')
        data_user_change = data_user[0] + ',' + \
            data_user[1] + ',' + data_user[2] + ',' + phone_change
        print(data_user_change)

    with open(file_name, 'w', encoding='utf-8') as w:
        for line in data_num:
            if line[0]+1 != num_change:
                w.write(line[1])
            else:
                w.write(data_user_change + '\n')

    return

# def menu():


#write_file(file_name, 'daer ghfj kdlf')
# print(read_file(file_name))
#print(search_user_name(read_file(file_name), 'Иван'))
#print(search_user_phone(read_file(file_name), '+7125478541'))
#w, u = search_user_name(read_file(file_name), 'Иван')
# print(w)
# print(delete_user(read_file(file_name)))
change_number()
