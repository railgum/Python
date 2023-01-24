import os
import time
from sys import platform

PHONEBOOKFILE = "phonebook.txt"  # имя файла справочника
VERSION = "1.1"


def clear_screen():
    '''очистка экрана (кроссплатформенная)'''
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        os.system("clear")  # для Linux & MacOS
    else:
        os.system("cls")    # для Windows


def search_data():
    '''диалог поиска '''
    clear_screen()
    while True:
        answer = input("Строка поиска(Еnter - выход) >:")
        if answer == "":
            return
        result = search_in_file(answer)
        for printdata in result:
            output_data_string(printdata)
        print("всего найдено записей: {} \n".format(len(result)))


def search_in_file(request):
    '''поиск с возвратом списка найденых записей'''
    result = []
    with open(PHONEBOOKFILE, "r", encoding="utf8") as datafile:
        for line in datafile:
            result.append(line.strip("\n"))
        result = list(filter(lambda line: request in line, result))
    return result


def output_data_string(printdata):
    '''форматированный вывод строки записи'''
    parse_data = printdata.split(",")
    template = "{0:<30} Тел.: {1:<13}"
    print(template.format(
        parse_data[0]+' ' + parse_data[1]+' '+parse_data[2], parse_data[3]))


def save_data_to_file(data_to_save):
    '''запись строки данных в конец файла'''
    data_to_save = ",".join(data_to_save) + "\n"
    print(data_to_save)
    with open(PHONEBOOKFILE, "a", encoding="utf8") as datafile:
        datafile.write(data_to_save)


def print_data():
    '''вывод записей с возвратом числа записей'''
    count = 0
    with open(PHONEBOOKFILE, "r", encoding="utf8") as datafile:
        for line in datafile:
            count += 1
            print(":{:<3} ".format(count), end='')
            output_data_string(line.strip('\n'))
    return count


def print_all_data():
    '''обертка вывод всех записей'''
    clear_screen()
    count = print_data()
    input(">:Всего {} Записей.  Enter для выхода".format(count))


def add_data():
    '''добавление записи'''
    clear_screen()
    while True:
        print('Добавление записи(""-выход)>:')
        last_name = input("Фамилия: ")
        if last_name == "":
            return
        first_name = input("Имя: ")
        patronymic = input("Отчество: ")
        phone_number = input("Номер Телефона: ")
        data_to_save = [last_name, first_name, patronymic, phone_number]
        if "" in data_to_save:
            return
        save_data_to_file(data_to_save)


def del_data():
    '''диалог удаления'''
    while True:
        clear_screen()
        print("N - удаление по номеру записи\n"
              "S - удаление по поиску\n"
              "Q - выход")
        answer = input(">:").upper()
        match answer:
            case "N":
                del_data_by_number()
            case "S":
                del_data_by_search()
            case "Q":
                return
            case _:
                print("неверный ввод")
                time.sleep(1)


def del_data_by_search():
    '''удаление по строке поиска'''
    clear_screen()
    while True:
        answer = input("Строка поиска для удаления(''-выход)>:")
        if answer == "":
            return
        found_records = search_in_file(answer)
        if len(found_records) == 0:
            print("нет записей для удаления")
        else:
            print("найдены записи:")
            for printdata in found_records:
                output_data_string(printdata)
            if input('удаляем [Y-да/..-нет]').upper() == "Y":
                phonedata = ""
                with open(PHONEBOOKFILE, "r", encoding="utf8") as datafile:
                    for line in datafile:
                        if answer in line:
                            continue
                        phonedata += line

                with open(PHONEBOOKFILE, "w", encoding="utf8") as datafile:
                    datafile.write(phonedata)


def del_data_by_number():
    '''удаление по порядковому номеру записи'''
    while True:
        clear_screen()
        print_data()
        answer = input("Номер записи для удаления(Q - выход)>: ")
        if answer.upper() == "Q":
            return
        if not answer.isnumeric():
            continue
        answer = int(answer)
        print(answer)
        phonedata = ""
        count = 0
        with open(PHONEBOOKFILE, "r", encoding="utf8") as datafile:
            for line in datafile:
                count += 1
                if answer == count:
                    continue
                phonedata += line

        with open(PHONEBOOKFILE, "w", encoding="utf8") as datafile:
            datafile.write(phonedata)


if __name__ == "__main__":
    # основной блок
    menu = (f"Телефонный справочник. v.{VERSION}\n\n"
            "Введите команду\n"
            "P - Вывод данных\n"
            "A - Добавление записи\n"
            "S - Поиск\n"
            "D - Удаление записи\n"
            "Q - Выход\n")
    while True:
        clear_screen()
        print(menu)
        answer = input(">:").upper()
        match answer:
            case "P":
                # вывод данных
                print_all_data()

            case "A":
                # добавление данных
                add_data()

            case "S":
                # поиск
                search_data()

            case "D":
                # удаление данных
                del_data()

            case "Q":
                # выход
                exit(0)

            case _:
                print("неверный ввод")
                time.sleep(2)
