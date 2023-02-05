import datetime

# Формула Харви


def moon_phase(day, month, year):
    
    moon_month = 29.5
    # print(datetime.date(year, month, day))
    # Если месяц -январь или февраль, из года вычесть единицу
    if month == 1 or month == 2:
        year -= 1
    # print(year)
    # 1) 2)
    temp = round((year/19 - year//19)*209)
    # print(a)
    # 3)
    if month == 1 or month == 2:
        temp += month + 12
    else:
        temp += month
    # 4)
    century_ratio = ((year//100//3 + (year//100//4)) + 6) - (year//100)
    temp += century_ratio + day
    age_moon = round((temp/30 - temp//30)*30)

    if age_moon > moon_month*0.95 and age_moon < moon_month*0.15:
        return (f'{age_moon} лунный день, новолуние')
    elif age_moon > moon_month*0.15 and age_moon < moon_month*0.35:
        return (f'{age_moon} лунный день, 1-я четверть')
    elif age_moon > moon_month*0.35 and age_moon < moon_month*0.45:
        return (f'{age_moon} лунный день, нарастающая луна')
    elif age_moon > moon_month*0.45 and age_moon < moon_month*0.55:
        return (f'{age_moon} лунный день, полнолуние')
    elif age_moon > moon_month*0.55 and age_moon < moon_month*0.65:
        return (f'{age_moon} лунный день, убывающая луна')
    elif age_moon > moon_month*0.65 and age_moon < moon_month*0.85:
        return (f'{age_moon} лунный день, последняя четверть')
    else:
        return (f'{age_moon} лунный день, старая луна')


# print(moon_phase(2023, 2, 13))
