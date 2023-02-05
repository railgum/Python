import datetime


def ny_days():
    dt_now = datetime.date.today()
    new_year_date = datetime.date(2024, 1, 1)
    delta = new_year_date - dt_now
    return (f'До нового года осталось {delta.days} дней')
