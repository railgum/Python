# Улитка по столбу днём вверх, ночью вниз

def snail(height, speed_down=1, speed_up=2):
    first_height = height
    day = 0
    height_old = height
    while (True):
        day += 1
        height -= speed_up
        if height <= 0:
            return day
        height += speed_down
        if height > first_height or height == height_old:
            return ('Улитка никогда не заползет на столб')

# print(snail(12,1,1))

# Записная книжка


def read_date_from_file() -> list[str]:
    with open('dateBD.txt', 'r', encoding='utf-8') as datafile:
        result = datafile.read().split('\n')
        print(result)
        lib: dict = {}
        for item in result:
          lib[item[1]] = item[0]


read_date_from_file()
