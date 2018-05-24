#----
# Готовка еды, использование инструментов, затраты труда:

metadict_detail['_-Потребление пищи (килограмм)'] = {
        # Исправить
            # Пони едят из мисок, но как-то это уныло
        '_-Потребление пищи (нормо-часов)':15/60,
        '_-Мытьё посуды (нормо-часов)':1/60,
        'Использование миски для еды (часов/килограмм)':1,
        'Использование ведра для мытья посуды (часов/килограмм)':1/60,
        'Вода для мытья посуды (литр)':1,
        }

metadict_detail['_-Потребление питья (литр)'] = {
        '_-Потребление пищи (нормо-часов)':15/60,
        '_-Мытьё посуды (нормо-часов)':1/60,
        'Использование кружки для питья (часов/литр)':1,
        'Использование ведра для мытья посуды (часов/килограмм)':1/60,
        'Вода для мытья посуды (литр)':1,
        }

metadict_detail['_-Кипячение воды (литр)'] = {
        # Исправить
            # Разберись уже, дома воду кипятатят, или горячее водоснабжение.
            # Дикая ведь разница в производительности труда.
        # Удельная теплоёмкость воды — 4.187 кДж/(кг*°C)
        # Необходимая_энергия = удельная_теплоёмкость * масса * температура_испарения
        # 4.187*1*100=418.7 кДж (0.419 МДж), чтобы вскипятить литр воды при 100% КПД.
        # КПД процесса -- 0.75
        '_-Кипячение воды (нормо-часов)':0.1/60,
        'Использование котла для кипячения воды (часов/литр)':20 / 60,
        'Дрова (МДж)':0.42 / 0.75,
        }

metadict_detail['_-Варка каши (килограмм)'] = {
        # Порция каши готовится около часа и отнимает 6 минут времени.
        '_-Варка каши (нормо-часов)':5/60,
        '_-Мытьё посуды (нормо-часов)':1/60,
        'Использование горшка для варки каши (часов/килограмм)':1,
        'Использование печи для варки каши (часов/килограмм)':1,
        'Вода для мытья посуды (литр)':1,
        }

metadict_detail['_-Варка компота (килограмм)'] = {
        '_-Мытьё сухофруктов (нормо-часов)':3/60,
        '_-Варка сухофруктов (нормо-часов)':2/60,
        '_-Мытьё посуды (нормо-часов)':1/60,
        'Использование ведра для мытья сухофруктов (часов/килограмм)':1/60,
        'Использование горшка для варки компота (часов/килограмм)':1,
        'Использование печи для варки компота (часов/килограмм)':1,
        'Вода для мытья сухофруктов (литр)':1,
        'Вода для мытья посуды (литр)':1,
        }

metadict_detail['_-Варка корнеплодов (килограмм)'] = {
        # Исправить
            # Помни -- копыта! Либо слоупочество, либо специальные ножи.
        # Расчеты производительности и количества персонала для овощного цеха:
        # https://www.pitportal.ru/chef2010/10921.html
        '_-Мытьё корнеплодов (нормо-часов)':1/60,
        '_-Сортировка корнеплодов (нормо-часов)':1/60,
        '_-Чистка корнеплодов (нормо-часов)':10/60,
        '_-Варка корнеплодов (нормо-часов)':1/60,
        'Использование ведра для мытья корнеплодов (часов/килограмм)':1/60,
        'Использование ножа для чистки корнеплодов (часов/килограмм)':10/60,
        'Использование стола для чистки корнеплодов (часов/килограмм)':10/60,
        'Использование горшка для варки корнеплодов (часов/килограмм)':30/60,
        'Использование печи для варки корнеплодов (часов/килограмм)':30/60,
        'Вода для мытья овощей (литр)':2,
        'Вода для мытья посуды (литр)':1,
        }

metadict_detail['Сбор кленового сока (килограмм)'] = {
        # Сезон длится 15 дней (март-апрель),
        # с дерева 40 литров; 4 отверстия, 2 литра/день (5 дней, 1/3 сезона).
        # Найти подходящее дерево и поставить уголки можно за 20 минут.
        '_-Сбор кленового сока (нормо-часов)':(20/60)/40 * 3,
        'Использование ведра для сбора кленового сока (часов/килограмм)':12,
        'Использование уголка для сбора кленового сока (часов/килограмм)':12,
        }

metadict_detail['_-Выварка кленового сиропа (килограмм)'] = {
        # Исправить
            # Лучше считай по кленовому соку.
            # А то ведь сорок литров на литр сиропа.
            # Укажи расход дров.
        '_-Выварка кленового сиропа (нормо-часов)':1,
        '_-Мытьё посуды (нормо-часов)':5/60,
        'Использование чана для выварки кленового сиропа (часов/килограмм)':15,
        'Вода для мытья посуды (литр)':10,
        }

metadict_detail['_-Варка яблочного джема (килограмм)'] = {
        '_-Сортировка фруктов (нормо-часов)':1/60,
        '_-Нарезка фруктов (нормо-часов)':10/60,
        '_-Варка яблочного джема (нормо-часов)':10/60,
        '_-Мытьё посуды (нормо-часов)':5/60,
        'Использование таза для варки яблочного джема (часов/килограмм)':2,
        'Вода для мытья посуды (литр)':2,
        }

metadict_detail['_-Выпечка хлеба (килограмм)'] = {
        # Исправить
            # Сельские пони выпекают 2.5 кг хлеба в день на семью.
            # Проблема в том, что у понек таки есть хлебозаводы.
            # Нужно разделить выпечку на фабричную и домашнюю.
            # Динки злится.
        # Бюджет времени русского крестьянина:
            # Производитлеьность хлебозаводов начала 20 века -- 10 кг/нормо-час
            # Выпечка хлеба в крестьянском хозяйстве -- 2.25 кг/нормо-час
        # Паршивые дрожжи -- тесто поднимается за 10-15 часов.
        # Выпечка длится -- 2 часа.
        '_-Подготовка теста (нормо-часов)':15/60,
        '_-Выпечка хлеба (нормо-часов)':5/60,
        '_-Мытьё посуды (нормо-часов)':5/60,
        'Использование кадки для брожения теста (часов/килограмм)':15,
        'Использование печи для выпечки хлеба (часов/килограмм)':2,
        'Вода для мытья посуды (литр)':1,
        }

metadict_detail['_-Выпечка медовых пряников (килограмм)'] = {
        # Заварное тесто готовится 15 дней.
            # http://www.hleb.net/prjanik/350/index-r.html#medovyeprjaniki
        '_-Подготовка теста (нормо-часов)':25/60,
        '_-Выпечка пряников (нормо-часов)':10/60,
        '_-Мытьё посуды (нормо-часов)':5/60,
        'Использование кадки для заваривания теста (часов/килограмм)':24*15,
        'Использование печи для выпечки пряников (часов/килограмм)':15/60,
        'Вода для мытья посуды (литр)':1,
        }

metadict_detail['_-Выпечка овсяного печенья (килограмм)'] = {
        '_-Подготовка теста (нормо-часов)':20/60,
        '_-Выпечка овсяного печенья (нормо-часов)':10/60,
        '_-Мытьё посуды (нормо-часов)':5/60,
        'Использование кадки для брожения теста (часов/килограмм)':15,
        'Использование печи для выпечки овсяного печенья (часов/килограмм)':15/60,
        'Вода для мытья посуды (литр)':1,
        }

metadict_detail['_-Домашняя консервация овощей (килограмм)'] = {
        '_-Мытьё овощей (нормо-часов)':1/60,
        '_-Сортировка овощей (нормо-часов)':1/60,
        '_-Чистка овощей (нормо-часов)':10/60,
        '_-Консервация овощей (нормо-часов)':1/60,
        'Использование ведра для мытья овощей (часов/килограмм)':1/60,
        'Использование ножа для чистки овощей (часов/килограмм)':10/60,
        'Использование стола для чистки овощей (часов/килограмм)':10/60,
        'Использование кадки для консервации овощей (часов/килограмм)':24*30 * 2,
        'Вода для мытья овощей (литр)':2,
        }

metadict_detail['_-Квашение капусты (килограмм)'] = {
        '_-Мытьё овощей (нормо-часов)':1/60,
        '_-Сортировка овощей (нормо-часов)':1/60,
        '_-Рубка овощей (нормо-часов)':10/60,
        '_-Квашение капусты (нормо-часов)':1/60,
        'Использование ведра для мытья овощей (часов/килограмм)':1/60,
        'Использование ножа для рубки овощей (часов/килограмм)':10/60,
        'Использование стола для рубки овощей (часов/килограмм)':10/60,
        'Использование кадки для квашения капусты (часов/килограмм)':24*14 * 2,
        'Вода для мытья овощей (литр)':2,
        }

metadict_detail['_-Домашняя консервация фруктов (килограмм)'] = {
        '_-Мытьё фруктов (нормо-часов)':1/60,
        '_-Сортировка фруктов (нормо-часов)':1/60,
        '_-Чистка фруктов (нормо-часов)':10/60,
        '_-Консервация фруктов (нормо-часов)':1/60,
        'Использование ведра для мытья фруктов (часов/килограмм)':1/60,
        'Использование ножа для чистки фруктов (часов/килограмм)':10/60,
        'Использование стола для чистки фруктов (часов/килограмм)':10/60,
        'Использование кадки для консервации фруктов (часов/килограмм)':24*30 * 2,
        'Вода для мытья фруктов (литр)':2,
        }

metadict_detail['_-Жарение и помол кофе (килограмм)'] = {
        # Исправить
            # Помол кофе, это работа мельницы/кофемолки
        '_-Обжаривание кофе (нормо-часов)':5/60,
        '_-Помол кофе (нормо-часов)':1,
        '_-Мытьё посуды (нормо-часов)':1/60,
        'Использование сковороды для обжаривания кофе (часов/килограмм)':10/60,
        'Использование немеханизированных жерновов (часов/килограмм)':1,
        'Вода для мытья посуды (литр)':1,
        }

metadict_detail['_-Помол корицы (килограмм)'] = {
        'Использование немеханизированных жерновов (часов/килограмм)':1,
        }

metadict_detail['_-Дробление кукурузных зёрен (килограмм)'] = {
        'Использование мельницы (часов/килограмм)':1,
        }

metadict_detail['_-Производство овсяной крупы (килограмм)'] = {
        # Исправить
            # Вообще-то это плющеный овёс
        'Использование мельницы (часов/килограмм)':1,
        }

metadict_detail['_-Помол пшеничной муки (килограмм)'] = {
        'Использование мельницы (часов/килограмм)':1,
        }

metadict_detail['_-Помол овсяной муки (килограмм)'] = {
        'Использование мельницы (часов/килограмм)':1,
        }

metadict_detail['_-Помол семян горчицы (килограмм)'] = {
        'Использование мельницы (часов/килограмм)':1,
        }

metadict_detail['_-Приготовление вина (килограмм)'] = {
        # Исправить
            # Разберись с затратами времени на техпроцессы:
        # Нормы технологического проектирования винодельческих заводов по переработке винограда:
        # http://www.norm-load.ru/SNiP/Data1/9/9947/index.htm
        # http://vinograd-vino.ru/tekhnologicheskie-skhemy/770-skhema-proizvodstva-vina-sedmoe-nebo-knyazya-golitsyna.html
        # https://ru.wikisource.org/wiki/ЭСБЕ/Виноделие
        '_-Сортировка фруктов (нормо-часов)':1/60,
        '_-Чистка фруктов (нормо-часов)':2/60,
        '_-Отжим фруктов (нормо-часов)':1/60,
        'Использование винтового пресса (часов/килограмм)':20/60,
        'Использование бочки для брожения виноградного сусла (часов/килограмм)':24*30*12,
        }

metadict_detail['_-Приготовление яблочного сидра (килограмм)'] = {
        '_-Сортировка фруктов (нормо-часов)':1/60,
        '_-Чистка фруктов (нормо-часов)':2/60,
        '_-Отжим фруктов (нормо-часов)':1/60,
        'Использование винтового пресса (часов/килограмм)':20/60,
        'Использование бочки для брожения яблочного сусла (часов/килограмм)':24*30*12,
        }

metadict_detail['_-Производство арахисовой пасты (килограмм)'] = {
        # Исправить
            # Очень медленные жернова.
            # Добавь механизации. Пусть хотя бы мельницу используют.
        '_-Обжаривание арахиса (нормо-часов)':5/60,
        '_-Мытьё посуды (нормо-часов)':1/60,
        'Использование сковороды для обжаривания арахиса (часов/килограмм)':10/60,
        'Использование мельницы (часов/килограмм)':1,
        'Вода для мытья посуды (литр)':1,
        }

metadict_detail['_-Производство конопляного масла (килограмм)'] = {
        # Исправить
            # Хау, да тут же целый техпроцесс.
            # Замени сковороды на фабричное оборудование.
        # НОРМЫ ТЕХНОЛОГИЧЕСКОГО ПРОЕКТИРОВАНИЯ ПРЕДПРИЯТИЙ МАЛОЙ МОЩНОСТИ
        # ПО ПРОИЗВОДСТВУ РАСТИТЕЛЬНЫХ МАСЕЛ ИЗ СЕМЯН ПОДСОЛНЕЧНИКА И РАПСА МЕТОДОМ ПРЕССОВАНИЯ
        # http://www.norm-load.ru/SNiP/Data1/10/10183/index.htm
        '_-Обжаривание семян (нормо-часов)':5/60,
        '_-Мытьё посуды (нормо-часов)':1/60,
        'Использование сковороды для обжаривания семян (часов/килограмм)':10/60,
        'Использование мельницы (часов/килограмм)':1,
        'Использование маслоотжимного пресса (часов/килограмм)':10/60,
        'Вода для мытья посуды (литр)':1,
        }

metadict_detail['_-Производство льняного масла (килограмм)'] = {
        '_-Обжаривание семян (нормо-часов)':5/60,
        '_-Мытьё посуды (нормо-часов)':1/60,
        'Использование сковороды для обжаривания семян (часов/килограмм)':10/60,
        'Использование мельницы (часов/килограмм)':1,
        'Использование маслоотжимного пресса (часов/килограмм)':10/60,
        'Вода для мытья посуды (литр)':1,
        }

metadict_detail['_-Производство подсолнечного масла (килограмм)'] = {
        '_-Обжаривание семян (нормо-часов)':5/60,
        '_-Мытьё посуды (нормо-часов)':1/60,
        'Использование сковороды для обжаривания семян (часов/килограмм)':10/60,
        'Использование мельницы (часов/килограмм)':1,
        'Использование маслоотжимного пресса (часов/килограмм)':10/60,
        'Вода для мытья посуды (литр)':1,
        }

metadict_detail['_-Производство соевого масла (килограмм)'] = {
        '_-Мытьё посуды (нормо-часов)':1/60,
        'Использование мельницы (часов/килограмм)':1,
        'Использование маслоотжимного пресса (часов/килограмм)':10/60,
        'Вода для мытья посуды (литр)':1,
        }

metadict_detail['_-Производство арахисового масла (килограмм)'] = {
        '_-Мытьё посуды (нормо-часов)':1/60,
        'Использование мельницы (часов/килограмм)':1,
        'Использование маслоотжимного пресса (часов/килограмм)':10/60,
        'Вода для мытья посуды (литр)':1,
        }

metadict_detail['_-Производство оливкового масла (килограмм)'] = {
        '_-Сортировка фруктов (нормо-часов)':1/60,
        '_-Отжим фруктов (нормо-часов)':1/60,
        '_-Мытьё посуды (нормо-часов)':1/60,
        'Использование винтового пресса (часов/килограмм)':20/60,
        'Вода для мытья посуды (литр)':1,
        }

metadict_detail['_-Производство масла какао (килограмм)'] = {
        # Первичная обработка какао-бобов включает очистку, сортировку, обжарку,
        # дробление какао, отделение оболочки какао-бобов (какаовеллы) от обрабатываемых бобов.
        '_-Обжаривание семян (нормо-часов)':5/60,
        '_-Мытьё посуды (нормо-часов)':1/60,
        'Использование мельницы (часов/килограмм)':1,
        'Использование винтового пресса (часов/килограмм)':20/60,
        'Вода для мытья посуды (литр)':1,
        }

metadict_detail['_-Производство какао-порошка (килограмм)'] = {
        'Использование мельницы (часов/килограмм)':1,
        }

metadict_detail['_-Производство пшеничного солода (килограмм)'] = {
        # https://bufetum.livejournal.com/51923.html
        '_-Приготовление пшеничного солода (нормо-часов)':5/60,
        '_-Мытьё посуды (нормо-часов)':1/60,
        'Использование посуды для замачивания пшеницы (часов/килограмм)':24,
        'Использование посуды для проращивания пшеницы (часов/килограмм)':2*24,
        'Использование листа для сушки солода (часов/килограмм)':2*24,
        'Использование немеханизированных жерновов (часов/килограмм)':1,
        'Вода для мытья посуды (литр)':1,
        }

metadict_detail['_-Сушка винограда (килограмм)'] = {
        '_-Сортировка фруктов (нормо-часов)':1/60,
        '_-Чистка фруктов (нормо-часов)':2/60,
        'Использование листа для сушки фруктов (часов/килограмм)':24*30,
        }

metadict_detail['_-Сушка вишни (килограмм)'] = {
        '_-Сортировка фруктов (нормо-часов)':1/60,
        '_-Чистка фруктов (нормо-часов)':2/60,
        'Использование листа для сушки фруктов (часов/килограмм)':24*30,
        }

metadict_detail['_-Сушка груши (килограмм)'] = {
        '_-Сортировка фруктов (нормо-часов)':1/60,
        '_-Нарезка фруктов (нормо-часов)':5/60,
        'Использование ножа для нарезки фруктов (часов/килограмм)':5/60,
        'Использование стола для нарезки фруктов (часов/килограмм)':5/60,
        'Использование листа для сушки фруктов (часов/килограмм)':24*30,
        }

metadict_detail['_-Сушка яблок (килограмм)'] = {
        '_-Сортировка фруктов (нормо-часов)':1/60,
        '_-Нарезка фруктов (нормо-часов)':5/60,
        'Использование ножа для нарезки фруктов (часов/килограмм)':5/60,
        'Использование стола для нарезки фруктов (часов/килограмм)':5/60,
        'Использование листа для сушки фруктов (часов/килограмм)':24*30,
        }

metadict_detail['_-Сушка дикорастущих растений (килограмм)'] = {
        '_-Сортировка растений (нормо-часов)':1/60,
        '_-Чистка растений (нормо-часов)':2/60,
        '_-Сушка растений (нормо-часов)':5/60,
        'Использование листа для сушки растений (часов/килограмм)':24*30,
        }

metadict_detail['_-Сушка чайных листьев (килограмм)'] = {
        # https://ahotcup.com/chai/prigotovlenie-chai/fermentaciya-chaya-glavnyjj-sekret-razno.html
        '_-Сортировка растений (нормо-часов)':1/60,
        '_-Прокатка чайных листьев (нормо-часов)':1/60,
        '_-Нарезка чайных листьев (нормо-часов)':5/60,
        '_-Сушка растений (нормо-часов)':5/60,
        'Использование листа для вяления чайных листьев (часов/килограмм)':24,
        'Использование стола для ферментации чайных листьев (часов/килограмм)':24,
        'Использование листа для сушки растений (часов/килограмм)':24*30,
        }

metadict_detail['_-Упаковка мёда в бочки (килограмм)'] = {
        # Исправить
            # Допилить
        }

metadict_detail['_-Чистка арахиса (килограмм)'] = {
        }

metadict_detail['_-Чистка и сушка кукурузы (килограмм)'] = {
        }

metadict_detail['_-Чистка и сушка фасоли (килограмм)'] = {
        }

metadict_detail['_-Ферметизация и сушка какао-бобов (килограмм)'] = {
        }

metadict_detail['_-Ферментизация и сушка стручков ванили (килограмм)'] = {
        }

metadict_detail['_-Чистка соевых бобов (килограмм)'] = {
        }

metadict_detail['_-Производство рафинированного сахара (килограмм)'] = {
        }

metadict_detail['_-Производство тростникового сахара-сырца (килограмм)'] = {
        # Технологическая схема тростниковосахарного производства
            # http://www.activestudy.info/texnologicheskaya-sxema-trostnikovosaxarnogo-proizvodstva/
            # 1) Отжим сока (вальцевый пресс)
            # 2) Очистка сока (0.07% извести от веса стеблей)
            # 3) Выпаривание сока в сироп
            # 4) Кристаллизация сиропа в сахар-сырец
        '_-Отжим стеблей сахарного тростника (нормо-часов)':5/60,
        '_-Очистка сока сахарного тростника (нормо-часов)':5/60,
        '_-Выпаривание сока сахарного тросника (нормо-часов)':10/60,
        '_-Кристаллизация сиропа в сахар-сырец (нормо-часов)':5/60,
        'Использование вальцевого пресса (часов/килограмм)':1,
        'Использование чана для выпаривания сахарного тростника (часов/килограмм)':5,
        }

metadict_detail['_-Приготовление чая (литр)'] = {
        # http://younapitki.ru/otvedajjte-chajj-iz-samovara/
        '_-Приготовление чая (нормо-часов)':1/60,
        'Использование самовара (часов/килограмм)':30/60,
        }

metadict_detail['_-Приготовление кофе (литр)'] = {
        '_-Приготовление кофе (нормо-часов)':1/60,
        'Использование самовара (часов/килограмм)':30/60,
        }

metadict_detail['_-Производство горького шоколада (килограмм)'] = {
        # Исправить
            # Слишком много копытной работы. Нужна механизация хотя бы для конширования.
            # Сейчас шоколад конширую в 300-литровых чана, так что 72/300=0.24 нормо-часа.
        # Технологическая линия производства плиточного шоколада и какао-порошка:
            # https://znaytovar.ru/s/Texnologicheskaya_liniya_proizvod6.html
            # 1) Вальцевание -- измельчение и перемешивание сахарной пудры и какао-порошка
            # 2) Разводка шоколадной массы -- разжижение смеси, добавление какао-масла
            # 3) Конширование -- перемешивание подогретой смеси с доступом воздуха (72 часа)
            # 4) Формирование шоколада -- быстрое охлаждение с +45°C до +33°C.
        # https://ru.wikisource.org/wiki/ЭСБЕ/Шоколад
        '_-Конширование горького шоколада (нормо-часов)':30/60,
        '_-Формирование горького шоколада (нормо-часов)':10/60,
        '_-Мытьё посуды (нормо-часов)':1/60,
        'Использование мельницы (часов/килограмм)':1,
        'Использование чана для конширования шоколада (часов/килограмм)':72,
        'Вода для мытья посуды (литр)':1,
        }

metadict_detail['_-Колка дров (кубометр)'] = {
        # ЕДИНЫЕ НОРМЫ ВЫРАБОТКИ И РАСЦЕНКИ НА ЛЕСОЗАГОТОВИТЕЛЬНЫЕ РАБОТЫ
            # http://pravo.levonevsky.org/baza/soviet/sssr1641.htm
            # 3.3.16. Колка дров вручную -- 0.686 нормо-часа на складской кубометр (около часа на тонну)
        # Бюджет времени русского крестьянина (1923 год):
            # http://istmat.info/node/27934
            # Домашний труд в крестьянской семье (7 человек, 3 работника):
            # Наколоть дрова на год -- 33 нормо-часа.
        '_-Колка дров (нормо-часов)':2,
        'Использование топора для колки дров (часов)':2,
        }
