import pandas as pd
from parser_cian import parse
from test_adress import get_location
from payload_generator import get_params


df = pd.read_excel("Пример для конкурса_пул_03.11.2022_ (2).xlsx")
standard = df.loc[0]
location = get_location(standard['Местоположение'])
print(location)
params = get_params(standard['Количество комнат'], standard['Материал стен (Кипич, панель, монолит)'], standard['Сегмент (Новостройка, современное жилье, старый жилой фонд)'])

parse(params, location, 1)







