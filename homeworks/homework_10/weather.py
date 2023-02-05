import requests
import datetime
from pprint import pprint
from config import open_weather_token as wt


def get_weather(city, wt):
    code_to_smile = {
      "Clear": ""
    }
    try:
        r = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={wt}&units=metric')

        data = r.json()
        pprint(data)

        city = data['name']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        length_day = sunset - sunrise

        print(f'******{datetime.datetime.now().strftime("%d %b %Y %H: %M")}*******\n'
              f'Погода в городе {city}:\nТемпература: {temperature} C\n'
              f'Влажность: {humidity} %\nДавление: {pressure} гПа\n'
              f'Ветер: {wind} м/с\nВосход солнца: {sunrise}\n'
              f'Закат солнца: {sunset}\nПродолжительность дня: {length_day}')
    except Exception as ex:
        print(ex)
        print('Проверьте название города')


def main():
    city = input('Введите город: ')
    get_weather(city, wt)


if __name__ == '__main__':
    main()
