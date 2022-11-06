import datetime


def get_params(count_room, house_material, segment):
    now = datetime.datetime.now()
    if "панель" in house_material.lower():
        house_material = 3
    elif "монолит" in house_material.lower():
        house_material = 2
    elif "бло" in house_material.lower():
        house_material = 4
    elif "кирпич" in house_material.lower():
        house_material = 1
    else:
        raise ValueError("Ошибка неверно задан материал дома")
    if isinstance(count_room, str) and count_room.lower() == "студия":
        count_room = 9
    elif isinstance(count_room, str) and count_room.lower() == "свободная планировка":
        count_room = 7
    if segment.lower() == "новостройка":
        gte = now.year - 2
        lte = now.year
    elif segment.lower() == 'современное жилье':
        gte = 1989
        lte = now.year - 3
    else:
        gte = 0
        lte = 1989
    return [count_room, house_material, gte, lte]
