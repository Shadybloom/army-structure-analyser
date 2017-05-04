#----
# Наборы компонентов устройств, машинокомплекты:

metadict_model['Компоненты универсального источника питания'] = {
        '|-Производство универсальных источников питания (выпущено штук)':1,
        'Работа приборостроительного завода (нормо-часов)':1,
        'Изолированные проводники (килограмм)':0.1,
        'Интегральные схемы (килограмм)':0.1,
        'Маломощный электрогенератор':1,
        'Маломощный вариатор':1,
        'Ленточный супермаховик малогабаритный (килограмм)':0.5,
        'Корпус малогабаритного устройства':1,
        }

metadict_model['Компоненты малогабаритной радиостанции'] = {
        '|-Производство малогабаритных радиостанций (выпущено штук)':1,
        'Работа приборостроительного завода (нормо-часов)':3,
        'Изолированные проводники (килограмм)':0.2,
        'Интегральные схемы (килограмм)':0.4,
        'Корпус малогабаритного устройства':1,
        }

metadict_model['Компоненты переносной радиостанции'] = {
        '|-Производство переносных радиостанций (выпущено штук)':1,
        'Работа приборостроительного завода (нормо-часов)':20,
        'Изолированные проводники (килограмм)':1,
        'Интегральные схемы (килограмм)':5,
        'Корпус переносного устройства':1,
        }

metadict_model['Компоненты персональной электронно-вычислительной машины'] = {
        '|-Производство персональных электронно-вычислительных машин (выпущено штук)':1,
        'Работа приборостроительного завода (нормо-часов)':40,
        'Оптические компьютеры (терминалы)':1,
        'Электронно-лучевые приборы (килограмм)':2,
        'Изолированные проводники (килограмм)':1,
        'Интегральные схемы (килограмм)':5,
        'Корпус переносного устройства':1,
        }

metadict_model['Компоненты возимой радиостанции'] = {
        '|-Производство возимых радиостанций (выпущено штук)':1,
        'Работа приборостроительного завода (нормо-часов)':40,
        'Изолированные проводники (килограмм)':3,
        'Интегральные схемы (килограмм)':9,
        'Корпус возимого устройства':1,
        }

metadict_model['Танковый прибор радиационной и химической разведки'] = {
        # http://fofanov.armor.kiev.ua/Tanks/EQP/go-27_r.html
        'Работа приборостроительного завода (нормо-часов)':40,
        'Изолированные проводники (килограмм)':3,
        'Интегральные схемы (килограмм)':7,
        'Корпус возимого устройства':1,
        }

metadict_model['Танковая фильтровентиляционная установка'] = {
        # Аналог ФВУ-200/100, 100 куб/метров в час в режиме фильтрования
        'Работа приборостроительного завода (нормо-часов)':10,
        'Изолированные проводники (килограмм)':3,
        'Нагнетатель-сепаратор танковый':1,
        'Вытяжной вентилятор танковый':1,
        'Танковый фильтр-поглотитель':1,
        '--Потребление энергии (кВт)':0.26,
        }

metadict_model['Секция динамической защиты'] = {
        'Крепление элемента динамической защиты':14,
        'Элемент динамической защиты':14,
        }

metadict_model['Комплект катков ОБТ'] = {
        'Направляющее колесо ОБТ':2,
        'Поддерживающий каток ОБТ':8,
        'Ведущее колесо ОБТ':2,
        'Опорный каток ОБТ':12,
        }

metadict_model['Подвеска ОБТ'] = {
        # Связывает корпус танка с опорными катками
        # Не более 4-7% от массы машины, 6-8% от внутреннего объёма
        'Узел подвески ОБТ':12,
        }

metadict_model['Узел подвески ОБТ'] = {
        'Торсион ОБТ':1,
        'Телескопический гидроамортизатор ОБТ':1,
        'Балансир ОБТ':1,
        }

metadict_model['Подвеска БТР'] = {
        'Узел подвески БТР':8,
        }

metadict_model['Подвеска военного грузовика'] = {
        'Узел подвески БТР':4,
        }

metadict_model['Узел подвески БТР'] = {
        'Танковые механические устройства (килограмм)':20,
        'Танковые детали (килограмм)':30,
        }

metadict_model['Водомётный движитель БТР'] = {
        # От танка ПТ-76:
        # Удельная мощность -- 12.6 кВт; тяга 11 кН; скорость по воде 10.2 км/час
        # диаметр рабочего колеса 340 мм; гидравлическое сечение 0.181 кв. метра (пять лопастей)
        'Приёмный патрубок водомётного движителя БТР':1,
        'Редуктор водомётного движителя БТР':1,
        'Передний гребной винт БТР':1,
        'Задний гребной винт БТР':1,
        }

metadict_model['Комплект колёс БТР'] = {
        'Колесо БТР':8,
        }

metadict_model['Комплект колёс военного грузовика'] = {
        'Колесо БТР':8,
        }

metadict_model['Колесо БТР'] = {
        'Колёсный диск БТР':1,
        'Шина БТР':1,
        }

metadict_model['Гусеничная лента ОБТ'] = {
        'Танковые траки':78,
        }

metadict_model['Бортовая коробка передач ОБТ'] = {
        # Семь передач переднего хода, одна заднего
        # 5 км/час, 10 км/час, 15 км/час,
        # 25 км/час, 40 км/час, 60 км/час
        # нейтральная передача, задний ход 5 км/час
        'Планетарный ряд':4,
        'Фрикционное устройство':6,
        'Гидросервоприводы управления':1,
        'Бортовой редуктор':1,
        }

#----
# Элементы устройств, элементарные устройства:

metadict_model['Маломощный электрогенератор'] = {
        'Электронные устройства (килограмм)':0.05,
        }

metadict_model['Маломощный вариатор'] = {
        'Механические устройства (килограмм)':0.05,
        }

metadict_model['Ларингофон'] = {
        'Электромеханические устройства (килограмм)':0.2,
        }

metadict_model['Наушники радиостанции'] = {
        'Электромеханические устройства (килограмм)':0.5,
        }

metadict_model['Штыревая антенна 1.5 метров'] = {
        'Механические устройства (килограмм)':0.2,
        }

metadict_model['Штыревая антенна 2.7 метров'] = {
        'Механические устройства (килограмм)':0.5,
        }

metadict_model['Антенна бегущей волны'] = {
        'Механические устройства (килограмм)':10,
        }

metadict_model['Корпус малогабаритного устройства'] = {
        # Габариты: 77×120×45 мм; объём: 0.42 литра
        # Площадь (дециметры): 0.77*0.77*2+1.2*1.2*2+0.45*0.45*2=4.5
        'Броневая сталь первого класса защиты (квадратные дециметры)':0.5,
        '-Объём используемый (кубометров)':0.0004158,
        }

metadict_model['Корпус переносного устройства'] = {
        # Габариты: 305×180×410 мм; объём: 22 литра
        # Площадь (дециметры): 3.05*3.05*2+1.8*1.8*2+4.1*4.1*2=59
        'Броневая сталь первого класса защиты (квадратные дециметры)':60,
        '-Объём используемый (кубометров)':0.0225,
        }

metadict_model['Корпус возимого устройства'] = {
        # Габариты: 305×360×410 мм; объём: 44 литра
        # Площадь (дециметры): 3.05*3.05*2+3.6*3.6*2+4.1*4.1*2=78
        'Броневая сталь первого класса защиты (квадратные дециметры)':80,
        '-Объём используемый (кубометров)':0.0450,
        }

metadict_model['Корпус воздушного фильтра'] = {
        # ФПУ-200 Габариты (цилиндр): диаметр - 515 мм; высота - 410; объём: 86 литров
        # Объём: 3.14159265*0.258^2*0.41=0.086 (86 литров)
        # Площадь: 2*3.14159265*0.258*(0.41+0.258)=1.1 (101 дециметров)
        'Броневая сталь первого класса защиты (квадратные дециметры)':101,
        '-Объём используемый (кубометров)':0.086,
        }

metadict_model['Охлаждаемая тепловизионная матрица'] = {
        # С активным охлаждением. Разрешение: 1,1 мрад. Обнаружение танка: 500-3000 метров.
        '---Стоимость вооружения (оценочно)':100000,
        }

metadict_model['Крепление элемента динамической защиты'] = {
        'Танковые детали (килограмм)':3,
        }

metadict_model['Танковые траки'] = {
        'Танковые детали (килограмм)':18,
        }

metadict_model['Торсион ОБТ'] = {
        # Пружина в виде вала, работающего на кручение.
        'Танковые детали (килограмм)':40,
        }

metadict_model['Балансир ОБТ'] = {
        'Танковые детали (килограмм)':90,
        }

metadict_model['Телескопический гидроамортизатор ОБТ'] = {
        'Танковые механические устройства (килограмм)':60,
        }

metadict_model['Поддерживающий каток ОБТ'] = {
        'Танковые детали (килограмм)':35,
        }

metadict_model['Направляющее колесо ОБТ'] = {
        'Танковые детали (килограмм)':220,
        }

metadict_model['Ведущее колесо ОБТ'] = {
        'Танковые детали (килограмм)':200,
        }

metadict_model['Опорный каток ОБТ'] = {
        'Танковые детали (килограмм)':200,
        }

metadict_model['Колёсный диск БТР'] = {
        'Танковые детали (килограмм)':60,
        }

metadict_model['Шина БТР'] = {
        '-Грузовики, бронетехника, тяжёлое оружие (тонн)':0.080,
        'Резина протекторная (тонн)':0.080,
        }

metadict_model['Приёмный патрубок водомётного движителя БТР'] = {
        'Броневая сталь (килограмм)':100,
        }

metadict_model['Редуктор водомётного движителя БТР'] = {
        'Танковые механические устройства (килограмм)':50,
        }

metadict_model['Передний гребной винт БТР'] = {
        'Танковые детали (килограмм)':10,
        }

metadict_model['Задний гребной винт БТР'] = {
        'Танковые детали (килограмм)':10,
        }

metadict_model['Оптические датчики'] = {
        'Электронные устройства (килограмм)':0.1,
        }

metadict_model['Термодатчики'] = {
        'Электронные устройства (килограмм)':0.1,
        }

metadict_model['Баллон огнегасящей смеси'] = {
        # Аналог ОУ-12, Габариты: 528x110x314
        'Броневая сталь (килограмм)':5,
        'Огнегасящая смесь (килограмм)':2,
        }

metadict_model['Бак машинного масла (20 литров)'] = {
        'Броневая сталь первого класса защиты (квадратные дециметры)':60,
        'Машинное масло (литры)':20,
        }

metadict_model['Бортовой фрикцион ОБТ'] = {
        # Уточнить, взял с Т-34
        'Танковые механические устройства (килограмм)':140,
        }

metadict_model['Входной редуктор ОБТ'] = {
        # Уточнить
        'Танковые механические устройства (килограмм)':50,
        }

metadict_model['Главный фрикцион ОБТ'] = {
        # Уточнить, взял с Т-34
        'Танковые механические устройства (килограмм)':120,
        }

metadict_model['Карданный вал ОБТ'] = {
        # Уточнить
        'Танковые детали (килограмм)':200,
        }

metadict_model['Планетарный ряд'] = {
        # Уточнить
        'Танковые механические устройства (килограмм)':50,
        }

metadict_model['Фрикционное устройство'] = {
        # Уточнить
        'Танковые механические устройства (килограмм)':50,
        }

metadict_model['Бортовой редуктор'] = {
        # Уточнить, взял с Т-34
        'Танковые механические устройства (килограмм)':280,
        }

metadict_model['Гидросервоприводы управления'] = {
        # Уточнить
        'Танковое электромеханическое оборудование (килограмм)':3,
        'Танковые гидроприводы (метры)':20,
        }

metadict_model['Оборудование для самоокапывания'] = {
        # Отвал шириной 2100 мм и передача на трансмиссию:
        'Танковые механические устройства (килограмм)':100,
        'Танковые детали (килограмм)':200,
        }

metadict_model['Оборудование подводного вождения танка'] = {
        # Съёмное, две трубы:
        'Танковые детали (килограмм)':80,
        }

metadict_model['Нагнетатель-сепаратор танковый'] = {
        'Танковые механические устройства (килограмм)':5,
        }

metadict_model['Вытяжной вентилятор танковый'] = {
        'Танковые механические устройства (килограмм)':3,
        }

metadict_model['Танковый фильтр-поглотитель'] = {
        'Активированный уголь (кубические дециметры)':86,
        'Корпус воздушного фильтра':1,
        }

#----
# Составные материалы, листовые материалы, покрытия:

metadict_model['Комбинированная танковая броня (тонн)'] = {
        '-Грузовики, бронетехника, тяжёлое оружие (тонн)':1,
        '---Стоимость вооружения (оценочно)':20000,
        }

metadict_model['Керамическая броня боевых машин (квадратные дециметры)'] = {
        # Защита от калибра 14.5 мм (не проверено).
        'Корундровая керамика бронемашин (килограмм)':1,
        }

metadict_model['Бронекерамика шестого класса защиты (квадратные дециметры)'] = {
        # Корундровая керамика, защита 6а класса -- 400 грамм/кв.дециметр
        # Защита от 2-3 попаданий бронебойной пули калибра 7.62x54, сильное заброневое действие.
        'Корундровая керамика (килограмм)':0.4,
        }

metadict_model['Броневая сталь пятого класса защиты (квадратные дециметры)'] = {
        # 6 мм стали, аналог С44, прочность: 2000 МПа, пятый класс защиты.
        'Броневая сталь (килограмм)':0.45,
        }

metadict_model['Бронепластины СВМПЭ третьего класса защиты (квадратные дециметры)'] = {
        # Сверхвысокомолекулярный полиэтилен прессованный.
        # Третий класс защиты, поверхностная плотность 210 грамм/кв.дециметр.
        # Непробитие 90% обычных пуль 7.62x39 с 10 метров.
        'Сверхвысокомолекулярный полиэтилен прессованный (килограмм)':0.21,
        }

metadict_model['Баллистическая ткань второго класса защиты (квадратные дециметры)'] = {
        # Многослойная арамидная ткань 3 кг/кв.метр.
        # Непробитие: сфера с диаметром 6,35 мм, массой 1,1 г, скоростью 550 м/с.
        'Арамидная ткань (килограмм)':0.03,
        }

metadict_model['Броневая сталь первого класса защиты (квадратные дециметры)'] = {
        # 1 мм стали, аналог С44 Прочность: 2000 МПа, противоосколочная защита.
        'Броневая сталь листовая (килограмм)':0.075,
        }

metadict_model['Конвекционно-амортизационный подпор (квадратные дециметры)'] = {
        # Защита от запреградной травмы, циркуляция воздуха под бронёй.
        # 30 мм высокомолекулярной полиэтиленовой ткани с плотностью в 300 килограмм на кубометр.
        'Сверхвысокомолекулярный полиэтилен прессованный (килограмм)':0.1,
        }

metadict_model['Маскировочная ткань (квадратные дециметры)'] = {
        # Изолирующая, с защитой от тепловизионных приборов и РЛС.
        'Капроновая ткань (килограмм)':0.004,
        }

#----
# Устройства смешанных технологических уровней:

metadict_model['Интегральные схемы (килограмм)'] = {
        'Электронные компоненты (килограмм)':0.2,
        'Печатные платы (килограмм)':0.8,
        }

metadict_model['Изолированные проводники (килограмм)'] = {
        'Электромеханические устройства (килограмм)':1,
        }

metadict_model['Огнегасящая смесь (килограмм)'] = {
        # Фреон 114В2
        '-КУНГи, прицепы, расходники, инструменты (тонн)':0.001,
        'Фреон (тонн)':0.001,
        }

metadict_model['Машинное масло (литры)'] = {
        # МТ-8п
        '-КУНГи, прицепы, расходники, инструменты (тонн)':0.00091,
        'Машинное масло (тонн)':0.00091,
        }

metadict_model['Активированный уголь (кубические дециметры)'] = {
        '-КУНГи, прицепы, расходники, инструменты (тонн)':0.0005,
        'Активированный уголь (тонн)':0.0005,
        }

metadict_model['Оцинкованная труба (метров)'] = {
        # Внутренний диаметр 20 мм (1 кг/метр);
        '-Грузовики, бронетехника, тяжёлое оружие (тонн)':0.001,
        'Прокат (тонн)':0.001,
        }

metadict_model['Алюминиевый силовой кабель (метров)'] = {
        # Сечение проводника: 25 кв.мм; максимальная мощность (при 220V) -- 18.7 кВт;
        # http://remont220.ru/s_cab.php
        # Вес проводника: 8930/10^9*25*1000=0.22 кг (с изоляцией 1 кг)
        '-Грузовики, бронетехника, тяжёлое оружие (тонн)':0.001,
        'Изолированные проводники алюминиевые (тонн)':0.001,
        }

metadict_model['Медный силовой кабель 100 мм (метров)'] = {
        # Для контактной сети железной дороги (неизолированные):
        # http://www.gosthelp.ru/text/GOST83980Provodaneizoliro.html
        # 19 проволок диаметром 2.51 мм
        # Вес проводника: 8930/10^9*100*1000=0.9 кг
        '-Грузовики, бронетехника, тяжёлое оружие (тонн)':0.001,
        'Медь (тонн)':0.001,
        }

metadict_model['Медный силовой кабель 25 мм (метров)'] = {
        # Сечение проводника: 25 кв.мм; максимальная мощность (при 220V) -- 25 кВт;
        # http://remont220.ru/s_cab.php
        # Вес проводника: 8930/10^9*25*1000= 0.22 кг (с изоляцией 1 кг)
        '-Грузовики, бронетехника, тяжёлое оружие (тонн)':0.001,
        'Изолированные проводники медные (тонн)':0.001,
        }

metadict_model['Танковые детали (килограмм)'] = {
        '-Грузовики, бронетехника, тяжёлое оружие (тонн)':0.001,
        'Прокат (тонн)':0.001,
        }

metadict_model['Танковые механические устройства (килограмм)'] = {
        '-Грузовики, бронетехника, тяжёлое оружие (тонн)':0.001,
        'Механические изделия (тонн)':0.001,
        }

metadict_model['Танковые гидроприводы (метры)'] = {
        # Рукава высокого давления ДУ-10 (армированные):
        # http://ladspb.ru/hydro_hose/gost_6286-73/
        '-Грузовики, бронетехника, тяжёлое оружие (тонн)':0.0008,
        'Резина протекторная (тонн)':0.0008,
        }

#----
# Носимые устройства:

metadict_model['Электронные компоненты (килограмм)'] = {
        '-Оружие, боеприпасы, экипировка, солдаты (тонн)':0.001,
        '---Стоимость вооружения (оценочно)':1000,
        }

metadict_model['Электронно-лучевые приборы (килограмм)'] = {
        '-Оружие, боеприпасы, экипировка, солдаты (тонн)':0.001,
        '---Стоимость вооружения (оценочно)':500,
        }

metadict_model['Корундровая керамика (килограмм)'] = {
        # http://www.unionexpert.ru/index.php/2011-07-25-15-56-33/item/287-alumina-bronekeramika-experience-of-production-and-use
        '-Оружие, боеприпасы, экипировка, солдаты (тонн)':0.001,
        '---Стоимость вооружения (оценочно)':50,
        }

metadict_model['Сверхвысокомолекулярный полиэтилен прессованный (килограмм)'] = {
        '-Оружие, боеприпасы, экипировка, солдаты (тонн)':0.001,
        '---Стоимость вооружения (оценочно)':250,
        }

metadict_model['Капроновая ткань (килограмм)'] = {
        '-Оружие, боеприпасы, экипировка, солдаты (тонн)':0.001,
        '---Стоимость вооружения (оценочно)':250,
        }

metadict_model['Арамидная ткань (килограмм)'] = {
        # Изрядная часть стоимости, это шитьё.
        '-Оружие, боеприпасы, экипировка, солдаты (тонн)':0.001,
        '---Стоимость вооружения (оценочно)':200,
        }

metadict_model['Ленточный супермаховик малогабаритный (килограмм)'] = {
        '-Оружие, боеприпасы, экипировка, солдаты (тонн)':0.001,
        '--Запас энергии (МДж)':10,
        '---Стоимость вооружения (оценочно)':200,
        }

metadict_model['Электронные устройства (килограмм)'] = {
        '-Оружие, боеприпасы, экипировка, солдаты (тонн)':0.001,
        '---Стоимость вооружения (оценочно)':280,
        }

metadict_model['Электромеханические устройства (килограмм)'] = {
        '-Оружие, боеприпасы, экипировка, солдаты (тонн)':0.001,
        '---Стоимость вооружения (оценочно)':140,
        }

metadict_model['Печатные платы (килограмм)'] = {
        '-Оружие, боеприпасы, экипировка, солдаты (тонн)':0.001,
        '---Стоимость вооружения (оценочно)':100,
        }

metadict_model['Механические устройства (килограмм)'] = {
        '-Оружие, боеприпасы, экипировка, солдаты (тонн)':0.001,
        '---Стоимость вооружения (оценочно)':100,
        }

metadict_model['Броневая сталь листовая (килограмм)'] = {
        '-Оружие, боеприпасы, экипировка, солдаты (тонн)':0.001,
        '---Стоимость вооружения (оценочно)':10,
        }

metadict_model['Рукав высокого давления (метры)'] = {
        # РВД Ду5 Тип II 0,34 кг/метр, рабочее давление 35 МПа
        # http://ladspb.ru/hydro_hose/gost_6286-73/
        '-Оружие, боеприпасы, экипировка, солдаты (тонн)':0.00034,
        'Резина протекторная (тонн)':0.00034,
        }

#----
# Возимые устройства, материалы:

metadict_model['Танковое электромеханическое оборудование (килограмм)'] = {
        '-Грузовики, бронетехника, тяжёлое оружие (тонн)':0.001,
        '---Стоимость вооружения (оценочно)':140,
        }

metadict_model['Корундровая керамика бронемашин (килограмм)'] = {
        # http://www.unionexpert.ru/index.php/2011-07-25-15-56-33/item/287-alumina-bronekeramika-experience-of-production-and-use
        '-Грузовики, бронетехника, тяжёлое оружие (тонн)':0.001,
        '---Стоимость вооружения (оценочно)':50,
        }

metadict_model['Ленточный супермаховик (кубометров)'] = {
        'Ленточный супермаховик (килограмм)':1400,
        }

metadict_model['Ленточный супермаховик (килограмм)'] = {
        # https://ru.wikipedia.org/wiki/Супермаховик
        # http://nurbejgulia.ru/wp-content/uploads/2013/03/d0b3d180d0b0d184d0b5d0bdd0bed0b2d0b0d18f-d0b1d183d0bcd0b0d0b3d0b0.pdf
        # Формула плотности энергии:
        # E/m=K*(a/p)
        # Где:
            # E — энергия в джоулях
            # m — масса в килограммах
            # K — коэффициент, зависящий от формы диска
            # a — прочность материала на разрыв, в паскалях
            # p — плотность материала, в килограммах на кубометр
        # Коэффицинет плотности энергии:
            # Диск равной прочности: K = 0.6-1 (в зависимости от формы и толщины обода).
            # Диск без отверстия (равной толщины) — 0.6
            # Тонкий обод (колесо со спицами) — 0.5
            # Диск с центральным отверстием (гончарный круг) — 0.3
        # На 10 МДж/кг плотности энергии требуется 30 ГПа прочности диска при K = 0.6.
        'Графеновая лента (килограмм)':1,
        '--Запас энергии (МДж)':10,
        }

metadict_model['Графеновая лента (килограмм)'] = {
        '-Грузовики, бронетехника, тяжёлое оружие (тонн)':0.001,
        '---Стоимость вооружения (оценочно)':50,
        }

metadict_model['Нитинол (кубометров)'] = {
        '-Грузовики, бронетехника, тяжёлое оружие (тонн)':6.5,
        'Нитинол (тонн)':6.5,
        }

metadict_model['Броневой углепластик (кубометров)'] = {
        # Предел прочности ~10-66 ГПа, модуль Юнга ~0,62-1,2 ТПа.
        # Таки почему мы не делаем броню из углепластика, если он в Эквестрии настолько крут?
        'Броневое углеволокно (килограмм)':1800,
        '-Объём используемый (кубометров)':1,
        }

metadict_model['Броневое углеволокно (килограмм)'] = {
        '-Грузовики, бронетехника, тяжёлое оружие (тонн)':0.001,
        '---Стоимость вооружения (оценочно)':50,
        }

metadict_model['Броневой стеклопластик (кубометров)'] = {
        'Броневое стекловолокно (килограмм)':2264,
        }

metadict_model['Броневое стекловолокно (килограмм)'] = {
        '-Грузовики, бронетехника, тяжёлое оружие (тонн)':0.001,
        '---Стоимость вооружения (оценочно)':25,
        }

metadict_model['Броневая сталь (кубометров)'] = {
        'Броневая сталь (килограмм)':7800,
        '-Объём используемый (кубометров)':1,
        }

metadict_model['Броневая сталь (килограмм)'] = {
        '-Грузовики, бронетехника, тяжёлое оружие (тонн)':0.001,
        '---Стоимость вооружения (оценочно)':10,
        }

metadict_model['Броневой алюминий (кубометров)'] = {
        'Броневой алюминий (килограмм)':2264,
        }

metadict_model['Броневой алюминий (килограмм)'] = {
        '-Грузовики, бронетехника, тяжёлое оружие (тонн)':0.001,
        '---Стоимость вооружения (оценочно)':16,
        }
