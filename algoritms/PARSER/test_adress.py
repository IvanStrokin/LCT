from geopy import Nominatim
import re


def get_location(address):
    app = Nominatim(user_agent='tutorial')
    address_replaces = {" ал\.": " аллея ", " б-р": " бульвар ", " взд\.": " въезд ", " дор\. ": " дорога ", " ззд\. ": " заезд ",
        " к-цо": " кольцо ", " лн\.": " линия ", " мгстр\.": " магистраль ", " наб\.": " набережная ", " пер-д": " переезд", " пер\.":
         " переулок ", " пл-ка": " площадка ", " пл\.": " площадь", " пр-кт\.": " проспект", " проул\.": " проулок ", " рзд\.":
         " разъезд ", " с-р": " сквер ", " с-к": " спуск ",  " сзд\.": " съезд ", " туп\.": " тупик ", " ул\.": " улица ",
         " ш\.": " шоссе ", " пр-д": " проезд ", " бул\.": " бульвар ", " просп\.": " проспект ", "д\.": " ", "г\.": ""}

    address = address.lower()
    address = address.replace(',', '')

    for word in address_replaces.keys():
        address = re.sub(r'%s' % word, address_replaces[word], address)
    address_list = address.split()

    position_c = address_list[-1].find('с')
    position_k = address_list[-1].find('к')

    if position_c != -1:
        address_list[-1] = f'{address_list[-1][:position_c]} {address_list[-1][position_c:]}'

    if position_k != -1:
        address_list[-1] = f'{address_list[-1][:position_k]} {address_list[-1][position_k:]}'

    new_address_list = []
    match = re.search(r'\d+-[а-я]+', address)
    if 'москва' in address_list:
        del address_list[0]
    if match:
        del address_list[address_list.index(match[0])]
        new_address_list.append(match[0])
        new_address_list.extend(address_list)
        reformat_address = "Москва " + ' '.join(new_address_list)
    else:
        reformat_address = 'Москва ' + ' '.join(address_list)
    location = app.geocode(reformat_address)
    while not location:
        reformat_address = reformat_address.split()
        del reformat_address[-1]
        reformat_address = ' '.join(reformat_address)
        location = app.geocode(reformat_address)
    return location[1]


def get_area(address_list):
    area = address_list[address_list.index('район') + 1]
    return area


