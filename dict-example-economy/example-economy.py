# Вычисляем стоимость хлеба в Понивиле (заодно можем определить число пекарен и годовую потребность в муке):
metadict_model['Понивиль (дневная торговля хлебом)'] = {
        'Пони (покупатель хлеба)':3700,
        }

metadict_model['Пони (покупатель хлеба)'] = {
        'Хлеб (килограмм)':0.5,
        }

metadict_model['Хлеб (килограмм)'] = {
        # Простой перевод величин:
        'Хлеб (тонн)':1/1000,
        }

metadict_model['Хлеб (тонн)'] = {
        # А здесь уже берётся доля от годового оборота:
        'Пекарня (годовой оборот)':1/200,
        }

metadict_model['Пекарня (годовой оборот)'] = {
        # Десять пекарей, 200 тонн хлеба в год, окупаемость -- 10 лет.
        'Пекарня (капитализация)':1/10,
        'Выпечка хлеба (тонн)':200,
        'Работа пекаря (год)':10,
        }

metadict_model['Пекарня (капитализация)'] = {
        # Цены взяты из экономической модели "Янтаря"
        'Стоимость (бит)':100000,
        }

metadict_model['Выпечка хлеба (тонн)'] = {
        'Мука (тонн)':0.7,
        }

metadict_model['Мука (тонн)'] = {
        'Стоимость (бит)':1000,
        }

metadict_model['Работа пекаря (год)'] = {
        'Стоимость (бит)':9000,
        }