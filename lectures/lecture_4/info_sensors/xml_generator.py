from user_interface import temperature_view
from user_interface import wind_speed_view
from user_interface import preassure_view


def create(device=1):
    xml = '<xml>\n'
    xml += '    <temperature units = "c">{}</temperature>\n'\
        .format(temperature_view(device))
    xml += '    <wind_speed_view units = "m/s">{}</wind_speed_view>\n'\
        .format(wind_speed_view(device))
    xml += '    <pressure units = "mmHg">{}</pressure>\n'\
        .format(preassure_view(device))
    xml += '</xml>'

    with open('data.xml', 'w') as page:
        page.write(xml)

    return xml


def create(device=1):
    xml = '<xml>\n'
    xml += '    <temperature units = "c">{}</temperature>\n'\
        .format(temperature_view(device))
    xml += '    <wind_speed_view units = "m/s">{}</wind_speed_view>\n'\
        .format(wind_speed_view(device))
    xml += '    <pressure units = "mmHg">{}</pressure>\n'\
        .format(preassure_view(device))
    xml += '</xml>'

    with open('data.xml', 'w') as page:
        page.write(xml)

    return xml


def new_create(data, device=1):
    t, p, w = data
    t = int(t * 1.8 + 32)
    p = int(p * 1, 333)
    w = int(w // 0.45)
    xml = '<xml>\n'
    xml += '    <temperature units = "F">{}</temperature>\n'\
        .format(t)
    xml += '    <wind_speed_view units = "m/h">{}</wind_speed_view>\n'\
        .format(w)
    xml += '    <pressure units = "gPa">{}</pressure>\n'\
        .format(p)
    xml += '</xml>'

    with open('new_data.xml', 'w') as page:
        page.write(xml)

    return data
