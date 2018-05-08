#----
# Производство дёгтя (смолокурение):

metadict_model['Производство дёгтя (килограмм)'] = {
        'Производство дёгтя (литр)':1.05,
        }

metadict_model['Производство дёгтя (литр)'] = {
        'Производство дёгтя (кубометр)':0.001,
        }

metadict_model['Производство дёгтя (кубометр)'] = {
        # Смоло-скипидарные аппараты — минские реторты емкостью 8 м³ (цикл 56 часов, восемь рабочих)
            # http://www.findpatent.ru/patent/257/2578695.html
        # Каждый аппарат производит по 330 литров смолы, требуется 3 аппарата (или цикла).
        'Смоляк (кубометр)':8 * 3,
        '_-Работа персонала смолокурни (нормо-часов)':8 * (56/2.4) * 3,
        'Использование 8-кубометровой смоляной печи (часов)':56 * 3,
        }

metadict_model['Корчёвка смоляка (кубометр)'] = {
        # Характеристика осмольного сырья, способы его получения
            # http://geolike.ru/page/gl_2140.htm
        # Смолокурение трудозатраты (на 0.1 кубометра смолы) -- 10 человеко-дней на сырьё (3-6 м³ смолья).
            # http://sanatatur.ru/forum/viewtopic.php?f=9&t=27691
        # Смолокурение в имении Красный бор:
            # http://vln.by/node/220
            # Штабель смоляка (локоть 0.5 метра): 1.5x1.25x1.25 (2.34 кубометра) -- 12 дней работы двора.
        # Сборник Е13 Расчистка трассы линейных сооружений от леса
        # http://www.gosthelp.ru/text/SbornikE13Raschistkatrass.html
        # §Е13-8. Корчевка пней
            # Нормы времени и расценки на 10 пней (около кубометра); диаметр пней, см 30;
            # Трактор Трактор Т-100М (тяговое усилие 6000 кгс, мощность 81 кВт)
            # Трудозатраты:
                # Для бульдозеристов: 0.81 нормо-часа
                # Для рабочих: 0.81 нормо-часа
        # В Россиии 2016 года пни на осмол стоят 6.6 рублей/килограмм, 3400 рублей/кубометр.
            # Взрывной способ -- 4 кубометра/смену
            # Корчеватель АКП-1 -- 25 кубометров/смену
        # ЕДИНЫЕ НОРМЫ ВЫРАБОТКИ И РАСЦЕНКИ НА ЛЕСОЗАГОТОВИТЕЛЬНЫЕ РАБОТЫ
            # http://pravo.levonevsky.org/baza/soviet/sssr1641.htm
            # 3.1.2. Спиливание пней заподлицо с землей
            # Диаметр комлей деревьев, см: св. 24 до 32
            # Трудозатраты -- 0.108 нормо-часа/пень (около часа на кубометр)
        '_-Корчёвка сосновых пней (нормо-часов)':20,
        '_-Колка пней на смоляк (нормо-часов)':5,
        '|-Сосновая вырубка (гектар)':10 / 250,
        'Использование топора для колки пней на смоляк (часов)':5,
        'Использование киркомотыги для корчёвки сосновых пней (часов)':20,
        }

#----
# Добыча песка:

metadict_model['Добыча песка (кубометр)'] = {
        'Земляные работы немеханизированные (кубометр)':1,
        }

#----
# Изготовление мебели:
    # Справочная книга столяра-строителя и мебельщика 4. Нормы и расценки
        # http://mebel.townevolution.ru/books/item/f00/s00/z0000010/st099.shtml
    # ТИПОВЫЕ НОРМЫ ВРЕМЕНИ НА ИЗГОТОВЛЕНИЕ СТОЛЯРНЫХ ИЗДЕЛИЙ
        # http://www.libussr.ru/doc_ussr/usr_15369.htm
        # http://www.up-pro.ru/library/production_management/productivity/schitajte_vremja_i_snizhajte_zatraty.html


#----
# Производство пиломатериалов:

metadict_model['Полевое производство пиломатериалов (кубометр)'] = {
        # Около 40% древесины отправляется в отходы:
            # http://baurum.ru/_library/?cat=wood_general_data&id=4864
        '_-Работа персонала лесопилки (нормо-часов)':20/60,
        'Использование механизированной лесопильной рамы (часов/кубометр)':1,
        'Круглый лес (кубометр)':1 / 0.6,
        #'|+Отходы лесопильные (кубометр)':1 / 0.4,
        }

#----
# Производство кирпича:
    # Основные технико-экономические показатели на выработку кирпича
    # http://www.arhplan.ru/materials/bricks/osnovnye-tehniko-ekonomicheskie-pokazateli-na-vyrabotku-kirpicha

metadict_model['Полевое производство кирпича (кубометр)'] = {
        # При ручной формовке и обжиге в напольных печах -- 8 человеко-дней на 1000 кирпичей (2 кубометра)
        # Влажность глины 30%
        'Глина (кубометр)':1.3,
        'Формирование сырца кирпича (кубометр)':1,
        'Сушка сырца кирпича (кубометр)':1,
        'Обжиг кирпича в штабелях (кубометр)':1,
        }

metadict_model['Формирование сырца кирпича (кубометр)'] = {
        # В Болгарии на изготовлении сырца работает бригада в составе семи человек:
            # на обработке глины — два человека,
            # на подноске глины к формовщику — один человек,
            # на формовке — один человек,
            # на укладке сырца для сушки — два человека
            # на прочих работах — один человек.
            # За рабочий день бригада вырабатывает около 4,5 тыс. шт. сырца (9 кубометров)
        # Используется глиномялка с прямоугольным мундшктуком и станок для резки кирпича.
            # http://www.arhplan.ru/materials/bricks/formovanie-syrca-kirpicha
        '_-Работа на производстве кирпича (нормо-часов)':16,
        'Использование прямоугольного мундштука для глиномялки (часов)':2,
        'Использование станка для резки кирпича (часов)':2,
        #'Опилки (кубометр)':0.01,
        }

metadict_model['Сушка сырца кирпича (кубометр)'] = {
        # Влажность падает от 25% к 8%, продолжительсность сушки 15 суток:
            # На поляне (в один ряд), кирпич сушится 10 часов, затем в штабелях
        # http://www.arhplan.ru/materials/bricks/sushka-syrca-kirpicha
        '_-Работа на производстве кирпича (нормо-часов)':4,
        #'Использование поляны для сушки кирпича (часов/кубометр)':10,
        'Использование штабелей для сушки кирпича (часов/кубометр)':24*15,
        }

metadict_model['Обжиг кирпича в штабелях (кубометр)'] = {
        # http://www.arhplan.ru/materials/bricks/obzhig-syrca-kirpicha
        # 196 часов кирпича находится в печи; дрова -- 0.3 кубометра на 1000 кирпичей
        '_-Работа на производстве кирпича (нормо-часов)':4,
        'Использование штабелей для обжига кирпича (часов/кубометр)':200,
        'Дрова (кубометр)':0.15,
        }

#----
# Добыча глины:

metadict_model['Полевое производство глины (кубометр)'] = {
        # Мощность пласта -- 2 метра, глубина -- 2 метра
        'Котлован (кубометр)':2 / 2,
        'Добыча глины (кубометр)':1,
        'Замачивание глины (кубометр)':1,
        'Уплотнение глины (кубометр)':1,
        }

metadict_model['Добыча глины (кубометр)'] = {
        # Исправить
            # Надо бы учесть перевозку глины от карьера до поля на замачивание/уплотнение.
        'Земляные работы немеханизированные (кубометр)':1,
        }

metadict_model['Замачивание глины (кубометр)'] = {
        # Процесс длится 5 суток. Глину выкладывают слоем в полметра и заливают водой.
            # На кубометр глины требуется 10-15 вёдер воды (0.15 кубометра)
        # Глину накрывают соломенным матом, чтобы не испарялась вода.
        '_-Работа в глиняном карьере (нормо-часов)':1,
        'Использование соломенного мата для замачивания глины (часов/кубометр)':1 * (24*5),
        'Вода для строительства (кубометр)':0.15,
        }

metadict_model['Уплотнение глины (кубометр)'] = {
        '_-Работа в глиняном карьере (нормо-часов)':1,
        'Использование граблей для перемешивания глины (часов)':1,
        'Использование тележки с отвалом для перемещения глины (часов)':1,
        'Использование механической глиномялки (часов/кубометр)':1,
        }

#----
# Строительные материалы (растворы):

metadict_model['Раствор кладочный М200 (кубометр)'] = {
        'Раствор кладочный М200 (100 кубометров)':0.01,
        }

metadict_model['Раствор отделочный цементно-известковый (кубометр)'] = {
        'Раствор отделочный цементно-известковый (100 кубометров)':0.01,
        }

metadict_model['Раствор кладочный М200 (100 кубометров)'] = {
        # Марка М200 (Пропорции: 0.2 - 1 - 3)
        # http://www.a-brick.ru/articles/view/8863F459/rashod-rastvora-na-kladku
        # Таблица ГЭСН 06-01-082 Приготовление тяжелых кладочных растворов:
            # http://www.norm-load.ru/SNiP/Data1/54/54267/index.htm#i984332
            # "06-01-082-07 (рабочие)": 241 нормо-час
            # "06-01-082-07 (машинисты)": 52 нормо-часа
        '_-Работа строительной бригады (нормо-часов)':300,
        'Известь негашёная (кубометр)':4.76,
        'Вода для строительства (кубометр)':31,
        'Цемент (кубометр)':23.8,
        'Песок (кубометр)':71.4,
        }

metadict_model['Раствор отделочный цементно-известковый (100 кубометров)'] = {
        # Таблица ГЭСН 06-01-083 Приготовление тяжелых отделочных растворов:
            # http://www.norm-load.ru/SNiP/Data1/54/54267/index.htm#i998199
            # цементно-известковых состава 1:1:6
            # "06-01-083-07 (рабочие)": 274 нормо-часа
            # "06-01-083-07 (машинисты)": 51 нормо-час
        '_-Работа строительной бригады (нормо-часов)':330,
        'Известь негашёная (кубометр)':11.7,
        'Вода для строительства (кубометр)':66,
        'Цемент (кубометр)':15.7,
        'Песок (кубометр)':110,
        }

#----
# Пчеловодство (трудозатраты):

metadict_model['Заготовка мёда (килограмм)'] = {
        # Исправить
            # Допилить. Или в фермерство перенести.
            # Пока что в фермерстве.
        # Организация труда в пчеловодстве
        # http://paseka.su/books/item/f00/s00/z0000047/index.shtml
        # ГЛАВА VII. НАУЧНАЯ ОРГАНИЗАЦИЯ ТРУДА В ПЧЕЛОВОДСТВЕ (нормативы)
        # http://paseka.su/books/item/f00/s00/z0000047/st029.shtml
        }

#----
# Водоснабжение (трудозатраты):

#metadict_model['Доставка воды потребителю (литр)'] = {
#        # Исправить
#            # Должно быть частью транспортной системы.
#        'Доставка воды потребителю (тонн)':0.001,
#        }
#
#metadict_model['Доставка воды потребителю (тонн)'] = {
#        # В деревнях вёдра-колодцы, в городах водопровод.
#        'Доставка воды от колодца (тонн)':1,
#        #'Доставка воды от колодца (тонн)':0.50,
#        #'Доставка воды от уличной колонки (тонн)':0.25,
#        #'Доставка воды трубопроводом (тонн)':0.25,
#        }
#
#metadict_model['Доставка воды от колодца (тонн)'] = {
#        # Бюджет времени русского крестьянина
#            # http://istmat.info/node/27934
#            # На 1.000 ведер воды в деревне затрачивается до 200 часов труда
#            # Тысяча вёдер, это 12.3 тонн воды, то есть 61.5 литров за час работы (16.26 нормо-часа/тонну)
#        # Тележка с кадкой, доставка на полкилометра.
#        'Набрать воды в колодце (тонн)':1,
#        'Везти воду в кадках (тонно-километр)':1 * 0.5,
#        'Погрузочно-разгрузочные работы (вода) (тонна)':1,
#        }
#
#metadict_model['Набрать воды в колодце (тонн)'] = {
#        # В тонне воды сотня вёдер, ведро поднимается за минуту (всего 2 часа).
#        # Исправить
#           # Слишком медленно! Есть же колодцы с противовесом.
#        '_-Работа с воротом колодца (нормо-часов)':2,
#        'Использование колодца (часов/тонн)':2,
#        }
#
#metadict_model['Везти воду в кадках (тонно-километр)'] = {
#        # Исправить
#            # Допиливай универсальную транспортную систему.
#        # Земнопони ползёт со скоростью 3 км/час, а тащит в тележке не больше 0.1 тонны груза.
#            # А может полтонны (задумайся, может пора земнопонькам чуть магии дать?)
#            # https://vignette.wikia.nocookie.net/mlp/images/1/1c/Plant_team_watering_ground_S1E11.png
#        '_-Работа водовоза (нормо-часов)':1 / 3 / 0.1,
#        'Использование 100-литровой кадки для воды (часов)':1 / 3 / 0.1,
#        'Использование грузовой тележки (часов)':1 / 3 / 0.1,
#        }

#metadict_model['Погрузочно-разгрузочные работы (вода) (тонна)'] = {
#        # Погрузочно - разгрузочные работы с применением простейших приспособлений
#        # http://www.6pl.ru/gost/pMt_76nvp3.htm
#            # Перемещение груза без механизации - 20 метров
#            # Грузы в кипах, тюках, ящиках, связках -- до 15 килограмм
#            # Трудозатраты -- 0.5 нормо-часа
#        '_-Работа водовоза (нормо-часов)':0.5,
#        'Использование 10-литрового ведра для воды (часов)':0.5,
#        }

#metadict_model['Доставка воды трубопроводом (тонн)'] = {
#        # Испрвить
#            # Должно быть больше. У понек ведь маленькие города и водокачки.
#        # На питерском водопроводе подача тысячи ведер воды потребителю поглощает
#        # не более 15 минут труда водопроводных рабочих (начало 20 века, Струмилин)
#        # Тысяча вёдер, это 12.3 тонн воды, 49.2 тонны/час работы (0.02 нормо-часа/тонну)
#        '_-Работа работников водопровода (нормо-часов)':0.02,
#        }

#----
# Производство корзин (трудозатраты):
    # ТИПОВЫЕ НОРМЫ ВЫРАБОТКИ НА МЕХАНИЗИРОВАННЫЕ И РУЧНЫЕ РАБОТЫ В САДОВОДСТВЕ
    # http://www.libussr.ru/doc_ussr/usr_14391.htm
    # Конструирование и производство плетеной мебели
    # http://splesti.ru/books/item/f00/s00/z0000004/index.shtml

metadict_model['Изготовление плетёных корзин объёмом 50 литров (штука)'] = {
        # Вес корзины:
            # Прутья диаметром 10 мм (75% объёма),
            # Площадь стенок 0.95 кв.метра (95 метров прутьев),
            # Объём прутьев: 0.95*0.01*0.75=0.007 кубометра.
        # http://www.junradio.com/olim2/korz.htm
        'Заготовка прутьев для плетения корзин (кубометр)':0.01,
        'Изготовление корзин из готовых ивовых прутьев (штука)':1,
        }

metadict_model['Изготовление корзин из готовых ивовых прутьев (штука)'] = {
        # 1) Подобрать прутья по размеру, поднести к месту работы,
        # 2) сплести корзины размером 50 х 50 х 35 см, изготовить и закрепить ручки
            # 4 корзины за 7 часов; 1.75 часа на корзину.
        # http://splesti.ru/books/item/f00/s00/z0000004/st027.shtml
            # Дзержинский лесхоз 930 корзин по 5.25 кг на мастера -- 1.72 часа на корзину.
        '_-Работа на плетении корзин (нормо-часов)':1.75,
        }

metadict_model['Заготовка прутьев для плетения корзин (кубометр)'] = {
        # http://splesti.ru/books/item/f00/s00/z0000004/st013.shtml
        # Нарезать прутья толщиной 8-12 мм, вынести на расстояние до 50 м, уложить в кучи
            # 0.25 кубометра за 7 часов, 0.036 кубометра/час, 28 нормо-часов/кубометр
        '_-Работа на заготовке ивовых прутьев (нормо-часов)':28,
        'Ивовые прутья диаметром 10 мм (метр)':10000,
        }

metadict_model['Ивовые прутья диаметром 10 мм (метр)'] = {
        'Ивовые прутья (кубометр)':0.0001,
        }

metadict_model['Ивовые прутья (кубометр)'] = {
        # Плотность при влажности 12% -- 490 кг/м³
        'Ивовые прутья (тонн)':0.49,
        }

#----
# Производство ящиков (трудозатраты):
    # Общесоюзные нормы технологического проектирования предприятий
    # машиностроения, приборостроения и металлообработки. Деревообрабатывающие цехи.
        # http://www.gosthelp.ru/text/ONTP0286Obshhesoyuznyenor2.html
    # ГОСТ 10198-91 Ящики деревянные для грузов массой свыше 200 до 20000 кг.
        # http://www.gosthelp.ru/text/GOST1019891YAshhikiderevy.html
    # ГОСТ 20463-75 Ящики деревянные проволокоармированные для овощей и фруктов.
        # http://docs.cntd.ru/document/1200011163

metadict_model['Изготовление щитовых деревянных ящиков под 50 кг груза (штука)'] = {
        'Изготовление щитовых деревянных ящиков под 50 кг груза (100 штук)':1 / 100,
        }

metadict_model['Изготовление решётчатых деревянных ящиков под 50 кг груза (штука)'] = {
        'Изготовление решётчатых деревянных ящиков под 50 кг груза (100 штук)':1 / 100,
        }

metadict_model['Изготовление щитовых деревянных ящиков под 50 кг груза (100 штук)'] = {
        # Исправить
            # Понячье производство не настолько автоматизированно.
        # Нормы расхода материалов на изготовление деревянных ящиков
        # http://www.gosthelp.ru/text/ONTP0286Obshhesoyuznyenor2.html
            # ГОСТ 2991-76, на 100 щитовых ящиков по 50 кг груза:
        '_-Работа бригады плотников (нормо-часов)':17,
        'Пиломатериалы (кубометр)':2.4,
        'Гвозди стальные (килограмм)':36,
        'Лента стальная (килограмм)':18,
        }

metadict_model['Изготовление решётчатых деревянных ящиков под 50 кг груза (100 штук)'] = {
        '_-Работа бригады плотников (нормо-часов)':17,
        'Пиломатериалы (кубометр)':1.2,
        'Гвозди стальные (килограмм)':18,
        'Лента стальная (килограмм)':9,
        }

metadict_model['Ремонт ящиков для упаковки яблок (штука)'] = {
        # http://www.libussr.ru/doc_ussr/usr_14391.htm
            # Прибить, заменить 2 - 3 дощечки (10 часов на 100 ящиков)
            # 70 ящиков за 7 часов, 0.1 часа/ящик.
        '_-Работа по ремонту ящиков (нормо-часов)':0.1,
        'Пиломатериалы (кубометр)':0.0012,
        'Гвозди стальные (килограмм)':0.018,
        'Лента стальная (килограмм)':0.009,
        }

#----
# Производство бочек (трудозатраты):
    # Дубовая бочка своими руками:
        # http://sam-stroy.info/plotnik/bondar-start.htm
        # https://dom-vinokura.ru/samogon/oborudovanie/dubovaya-bochka-svoimi-rukami.html#i-10
    # ЕДИНЫЕ НОРМЫ ВЫРАБОТКИ И ВРЕМЕНИ НА ИЗГОТОВЛЕНИЕ ДЕРЕВЯННЫХ БОЧЕК
        # http://www.libussr.ru/doc_ussr/usr_15368.htm
    # ГОСТ 8777-80 Бочки деревянные заливные и сухотарные.
        # http://docs.cntd.ru/document/1200011181

metadict_model['Изготовление деревянных бочек объёмом 100 литров (штука)'] = {
        # Исправить
            # На самом деле очень быстрый техпроцесс. Земнопони осуждают.
                # Так-то основные операции занимают где-то 50% времени.
                # Нужно отделить операции от ресурсов и ввести коэффициент.
            # Дерево требуется несколько месяцев сушить.
        # Габариты бочки: 0.675x0.515x0.515
        'Обруч стальной для бочки 1600x45x1.8 мм (штука)':6,
        'Клёпки боковика 700x70x20 мм (штука)':27,
        'Клёпки донника 450x70x20 мм (штука)':6 * 2,
        'Изготовление остовов бочек (100 штук)':1/100,
        'Изготовление донец (100 штук)':1/100,
        'Сборка бочек (100 штук)':1/100,
        #'Вощение бочки (штука)':1,
        }

metadict_model['Обруч стальной для бочки 1600x45x1.8 мм (штука)'] = {
        # 23 клёпки шириной 0.07 метра. Требуется 1600x45x1.8 стальная полоса:
        'Прокат из нержавеющей стали 1.8 мм (квадратный метр)':1.6 * 0.045,
        'Изготовление обручей (1000 штук)':1/1000,
        }

metadict_model['Клёпки донника 450x70x20 мм (штука)'] = {
        'Обработка заготовки клёпки донника (1000 штук)':1/1000,
        'Заготовки клёпки донника 450x70x20 мм (штука)':1,
        }

metadict_model['Клёпки боковика 700x70x20 мм (штука)'] = {
        'Обработка заготовки клёпки боковика (1000 штук)':1/1000,
        'Заготовки клёпки боковика 700x70x20 мм (штука)':1,
        }

metadict_model['Заготовки клёпки донника 450x70x20 мм (штука)'] = {
        # Дубовые клёпки: 450x70x20 мм (1600 на кубометр)
        'Изготовление заготовок клёпки (кубометр)':1/1600,
        }

metadict_model['Заготовки клёпки боковика 700x70x20 мм (штука)'] = {
        # Дубовые клёпки: 700x70x20 мм (1000 на кубометр)
        'Изготовление заготовок клёпки (кубометр)':1/1000,
        }

#----
# Производство бочек (технологические процессы):

metadict_model['Сборка бочек (100 штук)'] = {
        'Вставка доньев в остов бочки (100 штук)':1,
        'Осадка обручей на обручеосадочном прессе (100 штук)':1,
        'Зачистка бочек вручную (100 штук)':1,
        }

metadict_model['Изготовление остовов бочек (100 штук)'] = {
        'Сборка остовов бочек в сборочной форме (100 штук)':1,
        'Пропарка остовов бочек в пропарочной установке (100 штук)':1,
        'Стяжка остовов бочек в стяжном механическом винтовом вороте (100 штук)':1,
        'Выравнивание провесов (100 штук)':1,
        'Термическая обработка остовов (100 штук)':1,
        'Зауторка остовов бочек (100 штук)':1,
        }

metadict_model['Изготовление донец (100 штук)'] = {
        'Сортировка клёпок донника и подборка донных щитов (100 штук)':1,
        'Сшивка донных щитов (100 штук)':1,
        'Вырезка доньев на донновырезных станках (100 штук)':1,
        'Подборка комплектов доньев для бочки (100 штук)':1,
        'Сверление шкантовых отверстий в доньях (100 штук)':1,
        'Сверление отверстий в клепках и изготовление деревянных пробок (100 штук)':1,
        }

metadict_model['Изготовление обручей (1000 штук)'] = {
        'Резка и вальцовка обручей на бондарно-обручном станке (1000 штук)':1,
        'Сварка обручей на машинах для точечной сварки (1000 штук)':1,
        'Изготовление обручей из обрезков (1000 штук)':1,
        #'Окраска обручей бочек (100 штук)':10,
        }

metadict_model['Обработка заготовки клёпки боковика (1000 штук)'] = {
        'Сортировка клёпок (1000 штук)':1,
        'Фуговка клёпок боковика на клепкофуговальных станках (1000 штук)':1,
        'Строжка клёпок боковика на клепкострогальных станках (1000 штук)':1,
        'Двусторонняя торцовка черновых заготовок клёпок (1000 штук)':1,
        }

metadict_model['Обработка заготовки клёпки донника (1000 штук)'] = {
        'Сортировка клёпок (1000 штук)':1,
        'Фуговка клёпок донника на клепкофуговальных станках (1000 штук)':1,
        'Строжка клёпок донника на клепкострогальных станках (1000 штук)':1,
        }

#----
# Производство бочек (старомодное):

metadict_model['Вощение бочки (штука)'] = {
        # Бочка на 100 литров с площадью 1.3 кв.метра
        '_-Работа бригады бондарей (нормо-часов)':0.2,
        'Льняное масло (килограмм)':0.15,
        'Воск (килограмм)':0.25,
        }

#----
# Производство бочек (технологические процессы):

metadict_model['Зачистка бочек вручную (100 штук)'] = {
        # С зачисткой провесов
        '_-Работа бригады бондарей (нормо-часов)':1.55,
        }

metadict_model['Осадка обручей на обручеосадочном прессе (100 штук)'] = {
        '_-Работа бригады бондарей (нормо-часов)':1.19,
        }

metadict_model['Вставка доньев в остов бочки (100 штук)'] = {
        '_-Работа бригады бондарей (нормо-часов)':2.17,
        }

metadict_model['Окраска обручей бочек (100 штук)'] = {
        # Меделнно и аккуратно, кисточкой.
        '_-Работа бригады бондарей (нормо-часов)':5.13,
        }

metadict_model['Изготовление обручей из обрезков (1000 штук)'] = {
        '_-Работа бригады бондарей (нормо-часов)':1.94,
        }

metadict_model['Сварка обручей на машинах для точечной сварки (1000 штук)'] = {
        '_-Работа бригады бондарей (нормо-часов)':3.02,
        }

metadict_model['Резка и вальцовка обручей на бондарно-обручном станке (1000 штук)'] = {
        '_-Работа бригады бондарей (нормо-часов)':2.21,
        }

metadict_model['Сверление отверстий в клепках и изготовление деревянных пробок (100 штук)'] = {
        '_-Работа бригады бондарей (нормо-часов)':0.201 + 0.255,
        }

metadict_model['Сверление шкантовых отверстий в доньях (100 штук)'] = {
        '_-Работа бригады бондарей (нормо-часов)':0.233,
        }

metadict_model['Подборка комплектов доньев для бочки (100 штук)'] = {
        '_-Работа бригады бондарей (нормо-часов)':0.128,
        }

metadict_model['Вырезка доньев на донновырезных станках (100 штук)'] = {
        '_-Работа бригады бондарей (нормо-часов)':0.47,
        }

metadict_model['Сшивка донных щитов (100 штук)'] = {
        # 3.22. СШИВКА ДОННЫХ ЩИТОВ ВРУЧНУЮ
        '_-Работа бригады бондарей (нормо-часов)':2.13,
        }

metadict_model['Сортировка клёпок донника и подборка донных щитов (100 штук)'] = {
        # Сотня клёпок, или сотня щитов?
        '_-Работа бригады бондарей (нормо-часов)':0.6,
        }

metadict_model['Зауторка остовов бочек (100 штук)'] = {
        # 3.15. ЗАУТОРКА ОСТОВОВ БОЧЕК НА ДВУХСТОРОННЕМ БОНДАРНО-УТОРНОМ СТАНКЕ БУ
            # Вырезание уторов, пазов для донца.
        '_-Работа бригады бондарей (нормо-часов)':1.2,
        }

metadict_model['Термическая обработка остовов (100 штук)'] = {
        # Обжиг в электромангальной печи, 8 мангалов
        '_-Работа бригады бондарей (нормо-часов)':1.2,
        }

metadict_model['Выравнивание провесов (100 штук)'] = {
        '_-Работа бригады бондарей (нормо-часов)':1.5,
        }

metadict_model['Стяжка остовов бочек в стяжном механическом винтовом вороте (100 штук)'] = {
        '_-Работа бригады бондарей (нормо-часов)':1.1,
        }

metadict_model['Пропарка остовов бочек в пропарочной установке (100 штук)'] = {
        # Установка периодического действия на 8 остовов
        '_-Работа бригады бондарей (нормо-часов)':3,
        }

metadict_model['Сборка остовов бочек в сборочной форме (100 штук)'] = {
        # Бочки вместимостью 100 литров
        '_-Работа бригады бондарей (нормо-часов)':2,
        }

metadict_model['Сортировка клёпок (1000 штук)'] = {
        '_-Работа бригады бондарей (нормо-часов)':0.667,
        }

metadict_model['Фуговка клёпок донника на клепкофуговальных станках (1000 штук)'] = {
        '_-Работа бригады бондарей (нормо-часов)':0.876,
        }

metadict_model['Строжка клёпок донника на клепкострогальных станках (1000 штук)'] = {
        '_-Работа бригады бондарей (нормо-часов)':1.7,
        }

metadict_model['Фуговка клёпок боковика на клепкофуговальных станках (1000 штук)'] = {
        '_-Работа бригады бондарей (нормо-часов)':5.87,
        }

metadict_model['Строжка клёпок боковика на клепкострогальных станках (1000 штук)'] = {
        '_-Работа бригады бондарей (нормо-часов)':1.7,
        }

metadict_model['Двусторонняя торцовка черновых заготовок клёпок (1000 штук)'] = {
        # Прямоугольные доски в скруглённую форму для бочки.
        '_-Работа бригады бондарей (нормо-часов)':0.446,
        }

metadict_model['Изготовление заготовок клёпки (кубометр)'] = {
        # 3.2.1. Изготовление заготовок клёпок для деревянных заливных и сухотарных бочек
        # Норма расхода необрезных пиломатериалов на 1 куб. м клепки составляет:
            # хвойных пород - 1,62 куб. м, мягких пород - 1,93; твердых пород - 2,01 куб. м.
        'Пиломатериалы (кубометр)':2,
        '_-Работа бригады бондарей (нормо-часов)':15,
        }
