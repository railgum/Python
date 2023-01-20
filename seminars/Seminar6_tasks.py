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


def write_file(file_name, text):
    text = ','.join(text)
    with open(file_name, 'a', encoding='utf8') as data:
        data.writelines(text + '\n')


def read_file(file_name):
    result = []
    with open(file_name, 'r', encoding="utf-8") as data:
        for line in data:
            result.append(line.strip('\n').split(','))
    return result


def search_user_name(user_list, name):
    result = []
    for user in user_list:
        for j in user:
            # print(j)
            if j.find(name) != -1:
                result.append(user)
                count += 1
                break
    return (result, count)


def search_user_phone(user_list, number):
    result = ''
    for user in user_list:
        if user[3] == number:
            result += '{0} {1} {2}'.format(user[0], user[1], user[2])
    if result == '':
        print('Абонентов с таким номером нет')
    else:
        print(result)


def delete_user(user_list, name):

    #write_file(file_name, 'daer ghfj kdlf')
print(read_file(file_name))
search_user_phone(read_file(file_name), '+6461653')
