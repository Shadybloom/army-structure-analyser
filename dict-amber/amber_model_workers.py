#----
# Работа (экипажей):

metadict_model['_-Работа экипажа грузового поезда (часов)'] = {
        # Исправить
            # Уточнить численность экипажа
        '_-Работа железнодорожника (нормо-часов)':4,
        }

metadict_model['_-Работа экипажа грузового барка (часов)'] = {
        # 50 пони, из них 24 пегаски вместо движков
        '_-Работа капитана грузового барка (нормо-часов)':1,
        '_-Работа пегаса-моряка (нормо-часов)':24,
        '_-Работа моряка (нормо-часов)':25,
        }

metadict_model['_-Работа экипажа грузовой баржи (часов)'] = {
        # 10 пони, из них 8 пегасок вместо движков
        '_-Работа капитана грузовой баржи (нормо-часов)':1,
        '_-Работа пегаса-моряка (нормо-часов)':8,
        '_-Работа моряка (нормо-часов)':1,
        }

#----
# Процессы (упрощение):

metadict_model['_-Варка каши (нормо-часов)'] = {
        # Исправить
            # Хау, здесь мы считаем число рабочих (по числу рабочих дней)
            # Проблема в том, что многие работы, это чистое домохозяйство.
            # Но их тоже нужно учитывать.
        '_-Приготовление пищи (нормо-часов)':1,
        }

metadict_model['_-Варка корнеплодов (нормо-часов)'] = {
        '_-Приготовление пищи (нормо-часов)':1,
        }

metadict_model['_-Варка сухофруктов (нормо-часов)'] = {
        '_-Приготовление пищи (нормо-часов)':1,
        }

metadict_model['_-Варка яблочного джема (нормо-часов)'] = {
        '_-Приготовление пищи (нормо-часов)':1,
        }

metadict_model['_-Кипячение воды (нормо-часов)'] = {
        '_-Обработка сырья (нормо-часов)':1,
        }

metadict_model['_-Выварка кленового сиропа (нормо-часов)'] = {
        '_-Обработка сырья (нормо-часов)':1,
        }

metadict_model['_-Выпечка хлеба (нормо-часов)'] = {
        '_-Приготовление пищи (нормо-часов)':1,
        }

metadict_model['_-Выпечка пряников (нормо-часов)'] = {
        '_-Приготовление пищи (нормо-часов)':1,
        }

metadict_model['_-Выпечка овсяного печенья (нормо-часов)'] = {
        '_-Приготовление пищи (нормо-часов)':1,
        }

metadict_model['_-Квашение капусты (нормо-часов)'] = {
        '_-Приготовление пищи (нормо-часов)':1,
        }

metadict_model['_-Мытьё корнеплодов (нормо-часов)'] = {
        '_-Обработка пищи (нормо-часов)':1,
        }

metadict_model['_-Мытьё овощей (нормо-часов)'] = {
        '_-Обработка пищи (нормо-часов)':1,
        }

metadict_model['_-Мытьё растений (нормо-часов)'] = {
        '_-Обработка сырья (нормо-часов)':1,
        }

metadict_model['_-Мытьё сухофруктов (нормо-часов)'] = {
        '_-Обработка пищи (нормо-часов)':1,
        }

metadict_model['_-Мытьё фруктов (нормо-часов)'] = {
        '_-Обработка пищи (нормо-часов)':1,
        }

metadict_model['_-Нарезка фруктов (нормо-часов)'] = {
        '_-Обработка пищи (нормо-часов)':1,
        }

metadict_model['_-Нарезка чайных листьев (нормо-часов)'] = {
        '_-Обработка сырья (нормо-часов)':1,
        }

metadict_model['_-Обжаривание арахиса (нормо-часов)'] = {
        '_-Приготовление пищи (нормо-часов)':1,
        }

metadict_model['_-Обжаривание семян (нормо-часов)'] = {
        '_-Обработка сырья (нормо-часов)':1,
        }

metadict_model['_-Обжаривание кофе (нормо-часов)'] = {
        '_-Обработка сырья (нормо-часов)':1,
        }

metadict_model['_-Отжим фруктов (нормо-часов)'] = {
        '_-Обработка сырья (нормо-часов)':1,
        }

metadict_model['_-Подготовка теста (нормо-часов)'] = {
        '_-Приготовление пищи (нормо-часов)':1,
        }

metadict_model['_-Помол бобов на масло (нормо-часов)'] = {
        '_-Обработка сырья (нормо-часов)':1,
        }

metadict_model['_-Помол кофе (нормо-часов)'] = {
        '_-Обработка сырья (нормо-часов)':1,
        }

metadict_model['_-Помол семян на масло (нормо-часов)'] = {
        '_-Обработка сырья (нормо-часов)':1,
        }

metadict_model['_-Приготовление кофе (нормо-часов)'] = {
        '_-Приготовление пищи (нормо-часов)':1,
        }

metadict_model['_-Конширование горького шоколада (нормо-часов)'] = {
        '_-Приготовление пищи (нормо-часов)':1,
        }

metadict_model['_-Формирование горького шоколада (нормо-часов)'] = {
        '_-Приготовление пищи (нормо-часов)':1,
        }

metadict_model['_-Приготовление пшеничного солода (нормо-часов)'] = {
        '_-Обработка сырья (нормо-часов)':1,
        }

metadict_model['_-Приготовление чая (нормо-часов)'] = {
        '_-Приготовление пищи (нормо-часов)':1,
        }

metadict_model['_-Прокатка чайных листьев (нормо-часов)'] = {
        '_-Обработка сырья (нормо-часов)':1,
        }

metadict_model['_-Работа на заготовке ивовых прутьев (нормо-часов)'] = {
        '_-Обработка сырья (нормо-часов)':1,
        }

metadict_model['_-Работа на плетении корзин (нормо-часов)'] = {
        '_-Обработка сырья (нормо-часов)':1,
        }

metadict_model['_-Рубка овощей (нормо-часов)'] = {
        '_-Обработка пищи (нормо-часов)':1,
        }

metadict_model['_-Сортировка корнеплодов (нормо-часов)'] = {
        '_-Обработка пищи (нормо-часов)':1,
        }

metadict_model['_-Сортировка овощей (нормо-часов)'] = {
        '_-Обработка пищи (нормо-часов)':1,
        }

metadict_model['_-Сортировка растений (нормо-часов)'] = {
        '_-Обработка сырья (нормо-часов)':1,
        }

metadict_model['_-Сортировка фруктов (нормо-часов)'] = {
        '_-Обработка пищи (нормо-часов)':1,
        }

metadict_model['_-Сушка растений (нормо-часов)'] = {
        '_-Обработка сырья (нормо-часов)':1,
        }

metadict_model['_-Чистка корнеплодов (нормо-часов)'] = {
        '_-Обработка пищи (нормо-часов)':1,
        }

metadict_model['_-Чистка овощей (нормо-часов)'] = {
        '_-Обработка пищи (нормо-часов)':1,
        }

metadict_model['_-Чистка растений (нормо-часов)'] = {
        '_-Обработка сырья (нормо-часов)':1,
        }

metadict_model['_-Сбор кленового сока (нормо-часов)'] = {
        '_-Обработка сырья (нормо-часов)':1,
        }

metadict_model['_-Чистка фруктов (нормо-часов)'] = {
        '_-Обработка пищи (нормо-часов)':1,
        }

metadict_model['_-Консервация овощей (нормо-часов)'] = {
        '_-Приготовление пищи (нормо-часов)':1,
        }

metadict_model['_-Консервация фруктов (нормо-часов)'] = {
        '_-Приготовление пищи (нормо-часов)':1,
        }

metadict_model['_-Работа с воротом колодца (нормо-часов)'] = {
        # Исправить
            # Вообще-то фермеры часто нанимают местных пегасов.
        '_-Обработка сырья (нормо-часов)':1,
        }

metadict_model['_-Работа водовоза (нормо-часов)'] = {
        '_-Обработка сырья (нормо-часов)':1,
        }

metadict_model['_-Работа водопроводчика (нормо-часов)'] = {
        '_-Обработка сырья (нормо-часов)':1,
        }

metadict_model['_-Мытьё посуды (нормо-часов)'] = {
        '_-Обработка сырья (нормо-часов)':1,
        }

metadict_model['_-Работа землекопа (нормо-часов)'] = {
        '_-Строительство (нормо-часов)':1,
        }

metadict_model['_-Работа разнорабочего (нормо-часов)'] = {
        '_-Строительство (нормо-часов)':1,
        }

metadict_model['_-Работа пегаса-разнорабочего (нормо-часов)'] = {
        '_-Строительство (нормо-часов)':1,
        }

metadict_model['_-Работа единорога-волшебника (нормо-часов)'] = {
        # Исправить
            # В этом случае единорожку используют как газовую горелку и дуговую сварку.
            # А ведь они гораздо универсальнее.
        '_-Строительство (нормо-часов)':1,
        }

metadict_model['_-Корчёвка пней (нормо-часов)'] = {
        '_-Строительство (нормо-часов)':1,
        }

metadict_model['_-Работа печника (нормо-часов)'] = {
        'Использование инструментов каменщика (часов)':1,
        '_-Строительство (нормо-часов)':1,
        }

metadict_model['_-Работа каменщика (нормо-часов)'] = {
        'Использование инструментов каменщика (часов)':1,
        '_-Строительство (нормо-часов)':1,
        }

metadict_model['_-Работа штукатура (нормо-часов)'] = {
        'Использование инструментов штукатура (часов)':1,
        '_-Строительство (нормо-часов)':1,
        }

metadict_model['_-Работа маляра (нормо-часов)'] = {
        'Использование инструментов маляра (часов)':1,
        '_-Строительство (нормо-часов)':1,
        }

metadict_model['_-Работа плотника (нормо-часов)'] = {
        '_-Строительство (нормо-часов)':1,
        }

metadict_model['_-Работа строительной бригады (нормо-часов)'] = {
        '_-Строительство (нормо-часов)':1,
        }

metadict_model['_-Работа на дорожном строительстве (нормо-часов)'] = {
        '_-Строительство (нормо-часов)':1,
        }

metadict_model['_-Работа путевого смотрителя (нормо-часов)'] = {
        'Использование инструментов железнодорожника (часов)':1,
        '_-Строительство (нормо-часов)':1,
        }

metadict_model['_-Работа на производстве бетона (нормо-часов)'] = {
        '_-Строительство (нормо-часов)':1,
        }

metadict_model['_-Работа на производстве кладочного раствора (нормо-часов)'] = {
        '_-Строительство (нормо-часов)':1,
        }

metadict_model['_-Работа на производстве отделочного раствора (нормо-часов)'] = {
        '_-Строительство (нормо-часов)':1,
        }

metadict_model['_-Работа на производстве мятой глины (нормо-часов)'] = {
        '_-Обработка сырья (нормо-часов)':1,
        }

metadict_model['_-Работа на производстве кирпича (нормо-часов)'] = {
        '_-Обработка сырья (нормо-часов)':1,
        }

metadict_model['_-Работа вьючного пони (часов)'] = {
        '_--Транспортировка (нормо-часов)':1,
        }

metadict_model['_-Работа грузчика (нормо-часов)'] = {
        '_--Транспортировка (нормо-часов)':1,
        }

metadict_model['_-Работа пегаса с планёром (часов)'] = {
        '_--Транспортировка (нормо-часов)':1,
        }

metadict_model['_-Работа пегаса с телегой (часов)'] = {
        '_--Транспортировка (нормо-часов)':1,
        }

metadict_model['_-Работа железнодорожника (нормо-часов)'] = {
        'Использование инструментов железнодорожника (часов)':1,
        '_--Транспортировка (нормо-часов)':1,
        }

metadict_model['_-Работа капитана грузового барка (нормо-часов)'] = {
        '_--Транспортировка (нормо-часов)':1,
        }

metadict_model['_-Работа капитана грузовой баржи (нормо-часов)'] = {
        '_--Транспортировка (нормо-часов)':1,
        }

metadict_model['_-Работа моряка (нормо-часов)'] = {
        '_--Транспортировка (нормо-часов)':1,
        }

metadict_model['_-Работа пегаса-моряка (нормо-часов)'] = {
        '_--Транспортировка (нормо-часов)':1,
        }

#----
# Сельскохозяйственные работы (группировка)

metadict_model['_-Работа в саду (нормо-часов)'] = {
        '_--Полевые работы (нормо-часов)':1,
        }

metadict_model['_-Работа зебр на плантациях (нормо-часов)'] = {
        '_--Полевые работы зебр (нормо-часов)':1,
        }

metadict_model['_-Работа лесника (нормо-часов)'] = {
        '_--Полевые работы (нормо-часов)':1,
        }

metadict_model['_-Работа на огороде (нормо-часов)'] = {
        '_--Полевые работы (нормо-часов)':1,
        }

metadict_model['_-Работа на полях бобовых (нормо-часов)'] = {
        '_--Полевые работы (нормо-часов)':1,
        }

metadict_model['_-Работа на полях зерновых (нормо-часов)'] = {
        '_--Полевые работы (нормо-часов)':1,
        }

metadict_model['_-Работа на полях технических культур (нормо-часов)'] = {
        '_--Полевые работы (нормо-часов)':1,
        }

metadict_model['_-Работа на сборе дикорастущих трав (нормо-часов)'] = {
        '_--Полевые работы (нормо-часов)':1,
        }

metadict_model['_-Работа пчеловода (нормо-часов)'] = {
        '_--Полевые работы (нормо-часов)':1,
        }

metadict_model['_-Работа бригады лесорубов (нормо-часов)'] = {
        '_-Обработка сырья (нормо-часов)':1,
        }

metadict_model['_-Колка дров (нормо-часов)'] = {
        '_-Обработка сырья (нормо-часов)':1,
        }

metadict_model['_-Колка пней на смоляк (нормо-часов)'] = {
        '_-Обработка сырья (нормо-часов)':1,
        }

metadict_model['_-Корчёвка сосновых пней (нормо-часов)'] = {
        '_-Обработка сырья (нормо-часов)':1,
        }

metadict_model['_-Работа персонала лесопилки (нормо-часов)'] = {
        '_-Обработка сырья (нормо-часов)':1,
        }

metadict_model['_-Работа персонала смолокурни (нормо-часов)'] = {
        '_-Обработка сырья (нормо-часов)':1,
        }

metadict_model['_-Отжим стеблей сахарного тростника (нормо-часов)'] = {
        '_-Обработка сырья зебрами (нормо-часов)':1,
        }

metadict_model['_-Очистка сока сахарного тростника (нормо-часов)'] = {
        '_-Обработка сырья зебрами (нормо-часов)':1,
        }

metadict_model['_-Выпаривание сока сахарного тросника (нормо-часов)'] = {
        '_-Обработка сырья зебрами (нормо-часов)':1,
        }

metadict_model['_-Кристаллизация сиропа в сахар-сырец (нормо-часов)'] = {
        '_-Обработка сырья зебрами (нормо-часов)':1,
        }

#----
# Хозяйственные работы (группировка)

metadict_model['_-Строительство (нормо-часов)'] = {
        '_--Хозяйственные работы (нормо-часов)':1,
        }

metadict_model['_-Обработка пищи (нормо-часов)'] = {
        '_--Хозяйственные работы (нормо-часов)':1,
        }

metadict_model['_-Обработка сырья (нормо-часов)'] = {
        '_--Хозяйственные работы (нормо-часов)':1,
        }

metadict_model['_-Обработка сырья зебрами (нормо-часов)'] = {
        '_--Хозяйственные работы зебр (нормо-часов)':1,
        }

metadict_model['_-Приготовление пищи (нормо-часов)'] = {
        '_--Хозяйственные работы (нормо-часов)':1,
        }

#----
# Отдых (группировка)

metadict_model['_-Потребление пищи (нормо-часов)'] = {
        # Исправить
            # Вообще-то отдых тоже нужно учитывать
        #'_--Домашние дела (нормо-часов)':1,
        }
