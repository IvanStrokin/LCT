import filesRead as f

analogs = "algoritms/PARSER/analogs.xlsx"
pull = "algoritms/data/pull.xlsx"
index = 0

dataAnalogs = f.analogs(analogs)

perfectObj = f.perfectObj(index, pull) 

##Коректировка по удаленносити от метро через поочередное проверки значений для эталона для аналога

metroCor = [  #матрица процентов корректировки по удаленности от метро
    [0, 7, 12, 17, 24, 29],
    [-7, 0, 4, 9, 15, 20],
    [-11, -4, 0, 5, 11, 15],
    [-15, -8, -5, 0, 6, 10],
    [-19, -13, -10, -6, 0, 4],
    [-22, -17, -13, -9, -4, 0],
]

def metro(i):
    parName = "Удаленность от станции метро, мин. пешком"
    corect = 0
    analog = dataAnalogs.iloc[i][parName]
    perfect = perfectObj[:][parName]

    if perfect < 5:
        if analog >= 5 and analog < 10:
            return metroCor[0][1]
        elif analog >= 10 and analog < 15:
            return metroCor[0][2]
    
    if perfect >=5 and perfect < 10:
        if analog < 5:
            return metroCor[1][0]
        elif analog >=10 and analog < 15:
            return metroCor[1][2]
        elif analog >= 15 and analog < 30:
            return metroCor[1][3]
    
    if perfect >= 10 and perfect < 15:
        if analog < 5:
            return metroCor[2][0]
        elif analog >=5 and analog < 10:
            return metroCor[2][1]
        elif analog >= 15 and analog < 30:
            return metroCor[2][2]
        elif analog >= 30 and analog < 60:
            return metroCor[2][4]
    
    if perfect >=15 and perfect < 30:
        if analog >= 5 and analog < 10:
            return metroCor[3][1]
        elif analog >=10 and analog < 15:
            return metroCor[3][2]
        elif analog >= 30 and analog < 60:
            return metroCor[3][4]
        elif analog >= 60 and analog < 90:
            return metroCor[3][5]

    if perfect >=30 and perfect < 60:
        if analog >= 10 and analog < 15:
            return metroCor[4][2]
        elif analog >=15 and analog < 30:
            return metroCor[4][3]
        elif analog >= 60 and analog < 90:
            return metroCor[4][5]
    
    if perfect >=60 and perfect < 90:
        if analog >= 15 and analog < 30:
            return metroCor[5][3]
        elif analog >=30 and analog < 60:
            return metroCor[5][4]
    
    return corect

 ##Корректировка по площади квартры через сравнение значений аналога по отношению к эталону

flSqCor = [   #матрица процентов корректировки по площади квартиры
    [0, 6, 14, 21, 28, 31],
    [-6, 0, 7, 14, 21, 24],
    [-12, -7, 0, 6, 13, 16],
    [-17, -12, -6, 0, 6, 9],
    [-22, -17, -11, -6, 0, 3],
    [-24, -17, -13, -8, -3, 0],
]

def flatSqr(i):
    parName = "Площадь квартиры, кв.м"
    analog = dataAnalogs.iloc[i][parName]
    perfect = perfectObj[:][parName]

    if perfect < 30:
        if analog >= 30 and analog < 50:
            return flSqCor[0][1]
        elif analog >= 50 and analog < 65:
            return flSqCor[0][2]
    
    if perfect >=30 and perfect < 50:
        if analog < 30:
            return flSqCor[1][0]
        elif analog >=50 and analog < 65:
            return flSqCor[1][2]
        elif analog >= 65 and analog < 90:
            return flSqCor[1][3]
    
    if perfect >= 50 and perfect < 65:
        if analog < 30:
            return flSqCor[2][0]
        elif analog >=30 and analog < 50:
            return flSqCor[2][1]
        elif analog >= 65 and analog < 90:
            return flSqCor[2][2]
        elif analog >= 90 and analog < 120:
            return flSqCor[2][4]
    
    if perfect >=65 and perfect < 90:
        if analog >= 30 and analog < 50:
            return flSqCor[3][1]
        elif analog >=50 and analog < 65:
            return flSqCor[3][2]
        elif analog >= 90 and analog < 120:
            return flSqCor[3][4]
        elif analog >120:
            return flSqCor[3][5]

    if perfect >=90 and perfect < 120:
        if analog >= 50 and analog < 65:
            return flSqCor[4][2]
        elif analog >=65 and analog < 90:
            return flSqCor[4][3]
        elif analog >120:
            return flSqCor[4][5]
    
    if perfect >120:
        if analog >= 65 and analog < 90:
            return flSqCor[5][3]
        elif analog >=90 and analog < 120:
            return flSqCor[5][4]
    
    return 0.0


#Корреткировка по площади кухни 

kitSqrCorr = [  #матрица процентов корректировки по площади кухни
    [0, -2.9, -8.3, -15,2],
    [3, 0, -5.5, -11.2],
    [9, 5.8, 0, -6.1],
    [15, 9, 5.8, 0],
]

def kitSqr(i):
    parName = "Площадь кухни, кв.м"
    analog = dataAnalogs.iloc[i][parName]
    perfect = perfectObj[:][parName]

    if perfect < 7:
        if analog >= 7 and analog < 10:
            return kitSqrCorr[0][1]
        elif analog >= 10 and analog < 15:
            return kitSqrCorr[0][2]
        elif analog >=15:
           return kitSqrCorr[0][3] 


    if perfect >=7 and perfect < 10:
        if analog < 7:
            return kitSqrCorr[1][0]
        elif analog >= 10 and analog < 15:
            return kitSqrCorr[1][2]
        elif analog >=15:
           return kitSqrCorr[1][3]
      
    if perfect >=10 and perfect < 15:
        if analog < 7:
            return kitSqrCorr[2][0]
        elif analog >= 7 and analog < 10:
            return kitSqrCorr[2][1]
        elif analog >=15:
           return kitSqrCorr[2][3]
    
    if perfect >= 15:
        if analog < 7:
            return kitSqrCorr[3][0]
        elif analog >= 7 and analog < 10:
            return kitSqrCorr[3][1]
        elif analog >=10 and analog < 15:
            return kitSqrCorr[3][2]
    
    return 0.0


##Корректировка по наличию балкона/лоджии

balcExisCorr = [
    [0, -5],
    [5.3, 0]
]

def balcony(i):
    parName = "Наличие балкона/лоджии"
    analog = dataAnalogs.iloc[i][parName]
    perfect = perfectObj[:][parName]

    if perfect == "Да" or perfect == "ДА" or perfect == "да":
        if analog == "Нет" or analog == "НЕТ" or analog == "нет":
            return balcExisCorr[1][0]
    elif perfect == "Нет" or perfect == "НЕТ" or perfect == "нет":
        if analog == "Да" or analog == "ДА" or analog == "да":
            return balcExisCorr[0][1]
    return 0.0

###Корректировка п оэтажу расположения

floorCorr = [
    [0, -7, -3.1],
    [7.5, 0, 4.2],
    [3.2, -4, 0]
]

def floor(i):
    parName = "Этаж расположения"
    parMax = "Этажность дома"
    analogMax = dataAnalogs.iloc[i][parMax]
    perfectMax = perfectObj[:][parMax]
    analog = dataAnalogs.iloc[i][parName]
    perfect = perfectObj[:][parName]

    if perfect == 1:
        if analog == analogMax:
            return floorCorr[0][2]
        elif analog > 1:
            return floorCorr[0][1]
    elif perfect == perfectMax:
        if analog == 1:
            return floorCorr[2][0]
        elif analog < analogMax:
            return floorCorr[2][1]
    else:
        if analog == 1:
            return floorCorr[1][0]
        elif analog == analogMax:
            return floorCorr[1][2]
    return 0


##Корректировка по ремонту

repairTypes = ["Без отделки", "Муниципальный ремонт", "Современный"]

repCorr = [
    [0, -13400, -20100],
    [13400, 0, -6700],
    [20100, 6700, 0]
]

def repair(i):
    parName = "Состояние (без отделки, муниципальный ремонт, с современная отделка)"
    analog = dataAnalogs.iloc[i][parName]
    perfect = perfectObj[:][parName]
    
    if perfect == repairTypes[0]:
        if analog == repairTypes[1]:
            return repCorr[0][1]
        elif analog == repairTypes[2]:
            return repCorr[0][2]
    elif perfect == repairTypes[1]:
        if analog == repairTypes[0]:
            return repCorr[1][0]
        elif analog == repairTypes[2]:
            return repCorr[1][2]
    elif perfect == repairTypes[2]:
        if analog == repairTypes[0]:
            return repCorr[2][0]
        elif analog == repairTypes[1]:
            return repCorr[2][1]
    return 0

def sellCor():
    return -4.5

def correctiveAnalog(index):
    valueCol = "Стоимость"
    sqrCol = "Площадь квартиры, кв.м"
    analogVal = dataAnalogs.iloc[index][valueCol]
    midval = analogVal/dataAnalogs.iloc[index][sqrCol]

    values = []
    procCorr = 0
    
    procCorr += abs(sellCor())
    midval += midval*sellCor()/100

    procCorr += abs(flatSqr(index))
    midval += midval*flatSqr(index)/100

    procCorr += abs(metro(index))
    midval += midval*metro(index)/100

    procCorr += abs(floor(index))
    midval += midval*floor(index)/100

    procCorr += abs(kitSqr(index))
    midval += midval*kitSqr(index)/100

    procCorr += abs(balcony(index))
    midval += midval*balcony(index)/100

    procCorr += abs(repair(index)/midval)
    midval += repair(index)

    values.append(midval)
    values.append(procCorr)
    values.append(0)

    return  values

def corrValue():
    corrList = []
    corrSum = 0
    resValue = 0
    for i in range(len(dataAnalogs)):
        corrList.append(correctiveAnalog(i))
        corrSum += corrList[i][1]
        corrList[i][2] = 100/corrList[i][1]

    splitter = 0
    for i in range (len(corrList)):
        splitter += corrList[i][2]

    for i in range (len(corrList)):
        corrList[i][1] = corrList[i][2]/splitter

    for i in range (len(corrList)):
        resValue += corrList[i][0]*corrList[i][1]

    return resValue*perfectObj["Площадь квартиры, кв.м"]