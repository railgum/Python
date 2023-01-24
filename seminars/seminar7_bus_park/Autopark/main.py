from menu import Menu
import function as fn

if __name__ == "__main__":
    # основной блок
    menuitems = [
        ("1", "Вывод автобусов", fn.print_bus),
        ("2", "Добавление автобуса", fn.add_bus),
        ("3", "Вывод водителей", fn.print_driver),
        ("4", "Добавление водителей", fn.add_driver),
        ("5", "Вывод маршрута", fn.print_route),
        ("6", "Добавление маршрута", fn.add_route),
        ("7", "Выход", lambda: exit())]

    menu = Menu(menuitems)
    menu.run('>:')