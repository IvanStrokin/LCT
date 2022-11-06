import requests
import pandas
from pandas import ExcelWriter
from geopy.distance import geodesic as GD


def save_excel(data, file_name):
    df_data = pandas.DataFrame(data)
    writer = ExcelWriter(f'{file_name}.xlsx')
    df_data.to_excel(writer, f'{file_name}')
    writer.save()
    print(f'Данные сохранены в файл "{file_name}.xlsx"')


def get_offers(params, page):
    url = 'https://api.cian.ru/search-offers/v2/search-offers-desktop/'
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
    payload = {
        "jsonQuery": {
            "region": {"type": "terms", "value": [1]},
            "_type": "flatsale",
            "engine_version": {"type": "term", "value": 2},
            "room": {"type": "terms", "value": [params[0]]},
            "page": {"type": "term", "value": page},
            "house_material": {"type": "terms", "value": [params[1]]},
            "house_year": {"type": "range", "value": {"gte": params[2], "lte": params[3]}}
        }
    }
    r = requests.post(url, headers=headers, json=payload)
    offers = r.json()['data']['offersSerialized']
    return offers


def get_content(offers, location, r, params):
    data = []
    for offer in offers:
        data_dict = {}
        location_address = (offer['geo']['coordinates']['lat'], offer['geo']['coordinates']['lng'])
        if GD(location, location_address).km <= r:
            if offer['building']['buildYear'] is not None:
                data_dict['Местоположение'] = offer['geo']['userInput']
                data_dict['Стоимость'] = offer['bargainTerms']['priceRur']
                data_dict['Площадь квартиры, кв.м'] = offer['totalArea']
                data_dict['Площадь кухни, кв.м'] = offer['kitchenArea']

                if isinstance(offer['balconiesCount'], int) and offer['balconiesCount'] > 0 or isinstance(offer['loggiasCount'],int) and offer['loggiasCount'] > 0:
                    data_dict["Наличие балкона/лоджии"] = "да"
                else:
                    data_dict["Наличие балкона/лоджии"] = "нет"

                data_dict['Этажность дома'] = offer['building']['floorsCount']
                data_dict['Этаж расположения'] = offer['floorNumber']
                for i_address in offer['geo']['address']:
                    if i_address['type'] == 'metro':
                        data_dict['Удалённость от метро (мин пешком)'] = None
                data_dict['Количество комнат'] = params[0]
                data_dict['Сегмент (Новостройка, современное жилье, старый жилой фонд)'] = f"{params[2]}-{params[3]}"
                data_dict["Материал стен (Кипич, панель, монолит)"] = params[1]
                data_dict['Состояние (без отделки, муниципальный ремонт, с современная отделка)'] = None
                data.append(data_dict)
                print("Квартира добавлена в список аналогов")
    return data


def parse(params, location, r):
    try:
        data = []
        for page in range(1, 100):
            print(page)
            offers = get_offers(params, page)
            data.extend(get_content(offers, location, r, params))
        if len(data) < 3:
            r += 0.5
            parse(params,location,r)
        else:
            save_excel(data, "analogs")
    except Exception as ex:
        print(ex)

