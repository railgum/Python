from user_interface import temperature_view
from user_interface import preassure_view
from user_interface import wind_speed_view


def create(device=1):
    style = 'style="font-size:30px;"'
    html = '<html>\n <head></head>\n  <body>\n'
    html += f'   <p {style}>Temperature: {temperature_view(device)} C</p>\n'
    html += f'   <p {style}>Preassure: {preassure_view(device)} mmHg</p>\n'
    html += f'   <p {style}>Wind speed: {wind_speed_view(device)} m/s</p>\n'
    html += '  </body>\n</html>'

    with open('index.html', 'w') as page:
        page.write(html)

    return html


def new_create(data, device=1):
    t, p, w = data
    t = int(t * 1.8 + 32)
    p = p * 1, 333
    w = int(w // 0.45)
    style = 'style="font-size:30px;"'
    html = '<html>\n <head></head>\n  <body>\n'
    html += f'   <p {style}>Temperature: {t} F</p>\n'
    html += f'   <p {style}>Preassure: {p} gPa</p>\n'
    html += f'   <p {style}>Wind speed: {w} m/h</p>\n'
    html += '  </body>\n</html>'

    with open('new_index.html', 'w') as page:
        page.write(html)

    return data
