import pandas as pd

def perfectObj(i, pullFile):
    excel_data = pd.read_excel(pullFile)
    dataPull = pd.DataFrame(excel_data, columns=[
                                    'Удаленность от станции метро, мин. пешком',
                                    'Этажность дома', 
                                    'Этаж расположения', 
                                    'Площадь квартиры, кв.м',
                                    'Площадь кухни, кв.м',
                                    'Наличие балкона/лоджии',
                                    'Состояние (без отделки, муниципальный ремонт, с современная отделка)'
    ])
    perfectObj = dataPull.iloc[i]
    return perfectObj

def analogs(analogFile):

    excel_data = pd.read_excel(analogFile)

    dataAnalogs = pd.DataFrame(excel_data, columns=[
                                    'Удаленность от станции метро, мин. пешком',
                                    'Этажность дома', 
                                    'Этаж расположения', 
                                    'Площадь квартиры, кв.м',
                                    'Площадь кухни, кв.м',
                                    'Наличие балкона/лоджии',
                                    'Состояние (без отделки, муниципальный ремонт, с современная отделка)',
                                    'Стоимость',
    ])
    return dataAnalogs



