#----
# Боевые модули:

metadict_detail['Боевой модуль ОБТ'] = {
        # Исправить.
            # Нужно совместить установки и крепления с пулемётами.
        'Броневая башня ОБТ':1,
        'Оборудование башни ОБТ':1,
        'Автомат заряжания ОБТ':1,
        'Система стабилизации ОБТ':1,
        'Зенитная пулемётная установка ОБТ':1,
        'Система постановки аэрозольных завес':1,
        'Установка спаренного с пушкой пулемёта ОБТ':1,
        '125-мм гладкоствольная танковая пушка':1,
        'Зенитный 12-мм танковый пулемёт':1,
        'Единый пулемёт танковый':1,
        }

metadict_detail['Боевой модуль БМП'] = {
        'Броневая башня БМП':1,
        'Система стабилизации танковой пушки':1,
        'Система постановки аэрозольных завес':1,
        'Пусковая установка противотанковых ракет':1,
        '24-мм нарезная автоматическая пушка':1,
        'Единый пулемёт танковый':1,
        }

metadict_detail['Боевой модуль БМД'] = {
        # На понячьих БМД нет броневых башен, только туррель с приводом управления.
        'Система постановки аэрозольных завес':1,
        'Пусковая установка противотанковых ракет':1,
        'Туррель крупнокалиберного пулемёта':1,
        }

metadict_detail['Боевой модуль БТР'] = {
        # БПУ-1, масса не более 540 кг.
        'Броневая башня БТР':1,
        'Система постановки аэрозольных завес':1,
        'Возимый 40-мм автоматический гранатомёт':1,
        'Туррель крупнокалиберного пулемёта':1,
        }

metadict_detail['Боевой модуль 120-мм гаубицы'] = {
        # Вообще-то прицельные и противооткатные устройства, это элементы лафета.
        'Прицельные устройства гаубицы':1,
        'Противооткатные устройства гаубицы':1,
        'Ствол 120-мм гаубицы':1,
        }

metadict_detail['Боевой модуль 120-мм САУ'] = {
        'Броневая башня 120-мм САУ':1,
        'Прицельные устройства гаубицы':1,
        'Противооткатные устройства гаубицы':1,
        'Механизм заряжания танковой пушки':1,
        'Система постановки аэрозольных завес':1,
        'Ствол 120-мм гаубицы':1,
        'Единый пулемёт танковый':1,
        '-Допустимая стоимость оборудования ($)':1000000,
        }

metadict_detail['Боевой модуль 150-мм гаубицы'] = {
        # Вообще-то прицельные и противооткатные устройства, это элементы лафета.
        'Прицельные устройства гаубицы':1,
        'Противооткатные устройства гаубицы':1,
        'Ствол 150-мм гаубицы':1,
        }

metadict_detail['Боевой модуль 150-мм САУ'] = {
        # Исправить
        # 2С19 «Мста-С» башня без боекомплекта -- 13 500 кг
        'Броневая башня 150-мм САУ':1,
        'Прицельные устройства гаубицы':1,
        'Противооткатные устройства гаубицы':1,
        'Механизм заряжания танковой пушки':1,
        'Система постановки аэрозольных завес':1,
        'Ствол 150-мм гаубицы':1,
        'Единый пулемёт танковый':1,
        '-Допустимая стоимость оборудования ($)':2000000,
        }

metadict_detail['Боевой модуль буксируемой 120-мм РСЗО'] = {
        # Блоки направляющих не мешало бы объединить в модули с прицельными устройствами.
        'Блок направляющих буксируемой 120-мм РСЗО':1,
        }

metadict_detail['Боевой модуль самоходной 120-мм РСЗО'] = {
        'Блок направляющих самоходной 120-мм РСЗО':1,
        }

metadict_detail['Боевой модуль самоходной 220-мм РСЗО'] = {
        'Блок направляющих самоходной 220-мм РСЗО':1,
        }

metadict_detail['Боевой модуль ЗРК ближнего действия'] = {
        'Оборудование РЛС ЗРК ближнего действия':1,
        'Пусковая установка зенитных ракет ближнего действия':1,
        '-Допустимая стоимость оборудования ($)':3000000,
        }

metadict_detail['Боевой модуль ЗРК малой дальности'] = {
        'Оборудование РЛС ЗРК малкой дальности':1,
        'Пусковая установка зенитных ракет малой дальности':1,
        '-Допустимая стоимость оборудования ($)':6000000,
        }

metadict_detail['Боевой модуль ЗРК средней дальности'] = {
        'Оборудование РЛС ЗРК средней дальности':1,
        'Пусковая установка зенитных ракет средней дальности':1,
        '-Допустимая стоимость оборудования ($)':10000000,
        }

metadict_detail['Боевой модуль сторожевого робота'] = {
        'Стрелково-гранатомётный комплекс (боевого робота)':1,
        '-Допустимая стоимость оборудования ($)':100000,
        }

#----
# Основное оборудование техники:

metadict_detail['Оборудование мини-экскаватора'] = {
        # Объём ковша: 0.2 кубометра -- производительность 15 кубометров грунта/час
        'Ковш экскаватора (0.2 кубометра)':1,
        'Стрела экскаватора (1.5 метра)':1,
        '|-Производство мини-экскаваторов (выпущено штук)':1,
        '-Производительность по грунту (кубометров/час)':15,
        '-Допустимая масса оборудования (тонн)':0.5,
        '-Допустимая стоимость оборудования ($)':30000,
        }

metadict_detail['Оборудование мини-погрузчика'] = {
        # Фронтальный погрузчик ПУМ-500
            # Вместимость ковша 0.38 кубометра, грузоподъёмность 0.5 тонны
            # Мощность 30 кВт, скорость 9 км/час
                # Производительность погрузчика
                # http://www.gosthelp.ru/text/PosobieSpravochnikdorozhn.html
                # (3600*8*0.8*0.38*0.9*1.4) /
                # (1.1*(34.4+0.56*0.5))=289 кубометров за смену (36 в час)
        'Рабочий орган мини-погрузчика':1,
        'Гидропривод мини-погрузчика':1,
        '|-Производство мини-погрузчиков (выпущено штук)':1,
        '-Производительность по грунту (кубометров/час)':36,
        '-Допустимая масса оборудования (тонн)':0.5,
        '-Допустимая стоимость оборудования ($)':20000,
        }

metadict_detail['Оборудование мини-буксировщика'] = {
        'Лебёдка мини-буксировщика':1,
        'Стреловой кран мини-буксировщика':1,
        '|-Производство мини-буксировщиков (выпущено штук)':1,
        '-Допустимая масса оборудования (тонн)':0.5,
        '-Допустимая стоимость оборудования ($)':20000,
        }

metadict_detail['Оборудование одноковшового экскаватора'] = {
        # Объём ковша: 0.65 кубометра -- производительность 50-100 кубометров грунта/час
        'Ковш экскаватора (0.65 кубометра)':1,
        'Стрела экскаватора (3 метра)':1,
        'Кабина одноковшового экскаватора':1,
        '|-Производство одноковшовых экскаваторов (выпущено штук)':1,
        '-Производительность по грунту (кубометров/час)':50,
        '-Допустимая масса оборудования (тонн)':5,
        '-Допустимая стоимость оборудования ($)':100000,
        }

metadict_detail['Оборудование тяжёлого одноковшового экскаватора'] = {
        # Объём ковша: 1 кубометр -- производительность 100-200 кубометров грунта/час
        'Ковш экскаватора (1 кубометр)':1,
        'Стрела экскаватора (3 метра)':1,
        'Кабина одноковшового экскаватора':1,
        '|-Производство тяжёлых одноковшовых экскаваторов (выпущено штук)':1,
        '-Производительность по грунту (кубометров/час)':100,
        '-Допустимая масса оборудования (тонн)':10,
        '-Допустимая стоимость оборудования ($)':100000,
        }

metadict_detail['Оборудование 6-тонного стрелового крана'] = {
        'Стреловой кран (6 тонн)':1,
        'Кабина стрелового крана':1,
        '|-Производство 6-тонных стреловых кранов (выпущено штук)':1,
        '-Допустимая масса оборудования (тонн)':5,
        '-Допустимая стоимость оборудования ($)':50000,
        }

metadict_detail['Оборудование 25-тонного стрелового крана'] = {
        'Стреловой кран (25 тонн)':1,
        'Кабина стрелового крана':1,
        '|-Производство 25-тонных стреловых кранов (выпущено штук)':1,
        '-Допустимая масса оборудования (тонн)':15,
        '-Допустимая стоимость оборудования ($)':150000,
        }

metadict_detail['Оборудование установки строительства мостов'] = {
        # http://saper.isnet.ru/texnica-2/usm.html
        # http://saper.isnet.ru/texnica-2/kms.html
        # http://www.voentorg.by/catalog/431/25014/
        'Стреловой кран (1.5 тонны)':1,
        'Сваебойно-обстроечная площадка (4 молота 0.25 тонны)':1,
        '|-Производство установок строительства мостов (выпущено штук)':1,
        '-Допустимая масса оборудования (тонн)':5,
        '-Допустимая стоимость оборудования ($)':200000,
        }

metadict_detail['Оборудование автомобильной фильтровальной станции'] = {
        'Компоненты автомобильной фильтровальной станции':1,
        '|-Производство автомобильных фильтровальных станций (выпущено штук)':1,
        '-Очистка/дезактивация, опреснение воды (тонн/час)':5,
        '-Допустимая масса оборудования (тонн)':5,
        '-Допустимая стоимость оборудования ($)':50000,
        }

metadict_detail['Оборудование реактора мобильной АЭС'] = {
        # Исправить
            # Нужно учесть расход технической воды системой охлаждения
        'Компоненты реактора мобильной АЭС':1,
        'Мобильный атомный реактор (кВт)':50000,
        '|-Производство мобильных атомных электростанций (выпущено штук)':1,
        '-Допустимая масса оборудования (тонн)':50,
        '-Допустимая стоимость оборудования ($)':100000000,
        }

metadict_detail['Оборудование паровой турбины мобильной АЭС'] = {
        'Компоненты паровой турбины мобильной АЭС':1,
        'Паровая турбина (кВт)':50000,
        '|-Производство паровых турбин мобильных АЭС (выпущено штук)':1,
        '-Допустимая масса оборудования (тонн)':50,
        '-Допустимая стоимость оборудования ($)':2000000,
        }

metadict_detail['Оборудование турбогенератора мобильной АЭС'] = {
        'Компоненты турбогенератора мобильной АЭС':1,
        'Работа электрогенератора мобильной АЭС (кВт)':10000,
        'Высоковольтный электромотор (кВт)':10000,
        '|-Производство турбогенераторов мобильных АЭС (выпущено штук)':1,
        '-Допустимая масса оборудования (тонн)':50,
        '-Допустимая стоимость оборудования ($)':1000000,
        }

metadict_detail['Оборудование радиолокационного высотомера'] = {
        'Компоненты радиолокационного высотомера':1,
        '|-Производство радиолокационных высотомеров (выпущено штук)':1,
        '-Допустимая масса оборудования (тонн)':6,
        '-Допустимая стоимость оборудования ($)':2000000,
        }

metadict_detail['Оборудование радиолокационного дальномера'] = {
        # Состав высотомера ПРВ-16А из технического описания:
        'Устройство защиты от радиопомех':1,
        'Устройство защиты от самонаводящихся снарядов':1,
        'Устройство управления и защиты от перегрузок':1,
        'Устройство преобразования координат':1,
        'Устройства обогрева и вентиляции':1,
        'Контрольная и измерительная аппаратура':1,
        'Антенно-волноводное устройство':1,
        'Индикаторное устройство':1,
        'Передающее устройство':1,
        'Приводные устрйоства':1,
        'Приёмное устройство':1,
        '|-Производство радиолокационных дальномеров (выпущено штук)':1,
        '-Допустимая масса оборудования (тонн)':6,
        '-Допустимая стоимость оборудования ($)':2000000,
        }

metadict_detail['Оборудование РЛС ЗРК ближнего действия'] = {
        'Компоненты РЛС ЗРК ближнего действия':1,
        '|-Производство РЛС ближнего действия (выпущено штук)':1,
        '-Допустимая масса оборудования (тонн)':2,
        '-Допустимая стоимость оборудования ($)':3000000,
        }

metadict_detail['Оборудование РЛС ЗРК малкой дальности'] = {
        'Компоненты РЛС ЗРК малой дальности':1,
        '|-Производство РЛС малой дальности (выпущено штук)':1,
        '-Допустимая масса оборудования (тонн)':4,
        '-Допустимая стоимость оборудования ($)':10000000,
        }

metadict_detail['Оборудование РЛС ЗРК средней дальности'] = {
        'Компоненты РЛС ЗРК средней дальности':1,
        '|-Производство РЛС средней дальности (выпущено штук)':1,
        '-Допустимая масса оборудования (тонн)':4,
        '-Допустимая стоимость оборудования ($)':15000000,
        }

metadict_detail['Оборудование РЛС наведения'] = {
        'Компоненты РЛС наведения':1,
        '|-Производство РЛС наведения (выпущено штук)':1,
        '-Допустимая масса оборудования (тонн)':4,
        '-Допустимая стоимость оборудования ($)':15000000,
        }

metadict_detail['Оборудование РЛС обнаружения'] = {
        'Компоненты РЛС обнаружения':1,
        '|-Производство РЛС обнаружения (выпущено штук)':1,
        '-Допустимая масса оборудования (тонн)':6,
        '-Допустимая стоимость оборудования ($)':10000000,
        }

metadict_detail['Оборудование машины химической разведки'] = {
        # https://ru.wikipedia.org/wiki/РХМ-4
        'Прибор химической разведки':1,
        'Газосигнализатор':1,
        'Полуавтоматический газоопределитель':1,
        'Измеритель мощности дозы':1,
        'Приспособление отбора проб':1,
        'Установка запуска сигналов химической тревоги':1,
        'Комплект знаков огражения':6,
        '|-Производство машин химической разведки (выпущено штук)':1,
        '-Допустимая масса оборудования (тонн)':3,
        '-Допустимая стоимость оборудования ($)':300000,
        }

metadict_detail['Оборудование автогрейдера'] = {
        # http://www.kvsz.com/index.php?option=com_content&view=article&id=37&Itemid=336&lang=ru
        'Полноповоротный грейдерный отвал':1,
        '|-Производство автогрейдеров (выпущено штук)':1,
        '-Допустимая масса оборудования (тонн)':4,
        '-Допустимая стоимость оборудования ($)':20000,
        }

metadict_detail['Оборудование авторазливочной станции'] = {
        # http://www.mil.by/ru/forces/special/rhbz/461/8356/
        'Автомобильная водная цистерна':1,
        'Распылитель авторазливочной станции':1,
        '|-Производство авторазливочных станций (выпущено штук)':1,
        '-Допустимая масса оборудования (тонн)':2,
        '-Допустимая стоимость оборудования ($)':50000,
        }

metadict_detail['Оборудование инженерной разведывательной машины'] = {
        'Авиагоризонт':1,
        'Речной широкозахватный миноискатель':1,
        'Индукционный миноискатель полупроводниковый':1,
        'Переносной радиоволновый миноискатель':1,
        'Инженерный разведывательный эхолокатор':1,
        'Прибор инженерной разведки (перископ)':1,
        'Артиллерийская буссоль':1,
        'Оптический дальномер':1,
        '|-Производство инженерных разведывательных машин (выпущено штук)':1,
        '-Допустимая масса оборудования (тонн)':4,
        '-Допустимая стоимость оборудования ($)':500000,
        }

metadict_detail['Оборудование боевой разведывательной машины'] = {
        'Станция ближней разведки':1,
        'Лазерный прибор разведки':1,
        'Тепловизионный прибор разведки':1,
        'Прибор химической разведки':1,
        'Индукционный миноискатель полупроводниковый':1,
        'КВ-радиостанция':1,
        '|-Производство боевых разведывательных машин (выпущено штук)':1,
        '-Допустимая масса оборудования (тонн)':4,
        '-Допустимая стоимость оборудования ($)':1000000,
        }

metadict_detail['Оборудование бронированной ремонтно-эвакуационной машины'] = {
        # https://topwar.ru/87633-bronirovannaya-remontno-evakuacionnaya-mashina-brem-1.html
        # https://topwar.ru/46608-amerikanskaya-bronirovannaya-remontno-evakuacionnaya-mashina-m88.html
        'Бульдозер-сошник (3x0.5 метра)':1,
        'Стреловой кран (12 тонн)':1,
        'Лебёдка тяговая главная (25 тонно-сил)':1,
        'Силовой полиспаст (усиление до 100 тонно-сил)':1,
        'Лебёдка тяговая вспомогательная (0.6 тонно-сил)':1,
        '|-Производство бронированных ремонтно-эвакуационных машин (выпущено штук)':1,
        '-Допустимая масса оборудования (тонн)':10,
        '-Допустимая стоимость оборудования ($)':1000000,
        }

metadict_detail['Оборудование бурильной машины'] = {
        # Глубина скважины до 30 метров:
        # http://saper.isnet.ru/texnica/bgm.html
        'Компоненты бурильной машины':1,
        'Стреловой кран (1.5 тонны)':1,
        '|-Производство бурильных машин (выпущено штук)':1,
        '-Допустимая масса оборудования (тонн)':5,
        '-Допустимая стоимость оборудования ($)':200000,
        }

metadict_detail['Оборудование дезинфекционно-душевого комплекса'] = {
        # http://www.russianarms.ru/forum/index.php?topic=5957.0
        'Резервуар резинно-тканевый (5 кубометров)':1,
        'Дезинфекционная камера (3.5 кубометра)':4,
        'Палатка-санпропускник':1,
        'Электрогенератор (10 кВт)':1,
        'Отопительно-вентиляционная установка (7.5 киловатт)':3,
        'Водонагреватель-паровой котёл (7 кубометров 40+ град. воды/час)':1,
        'Душевая сетка (5 литров/минуту)':10,
        '-Помывка/дезинфекция личного состава (солдат/час)':160,
        '|-Производство дезинфекционно-душевых комплексов (выпущено штук)':1,
        '-Допустимая масса оборудования (тонн)':5,
        '-Допустимая стоимость оборудования ($)':100000,
        }

metadict_detail['Оборудование дезинфекционной установки'] = {
        'Душевая сетка (5 литров/минуту)':10,
        'Водонагреватель-паровой котёл (7 кубометров 40+ град. воды/час)':1,
        '-Допустимая масса оборудования (тонн)':7,
        }

metadict_detail['Оборудование бульдозера'] = {
        # http://saper.isnet.ru/texnica/bkt.html
        'Рабочий орган бульдозера':1,
        'Гидропривод бульдозера':1,
        '-Допустимая масса оборудования (тонн)':3,
        '-Производительность по грунту (кубометров/час)':60,
        '-Допустимая стоимость оборудования ($)':50000,
        }

metadict_detail['Оборудование скрепера'] = {
        'Рабочий орган скрепера':1,
        'Гидропривод скрепера':1,
        '-Допустимая масса оборудования (тонн)':3,
        '-Производительность по грунту (кубометров/час)':60,
        '-Допустимая стоимость оборудования ($)':20000,
        }

metadict_detail['Оборудование тяжёлого бульдозера'] = {
        'Рабочий орган тяжёлого бульдозера':1,
        'Гидропривод тяжёлого бульдозера':1,
        '-Допустимая масса оборудования (тонн)':6,
        '-Производительность по грунту (кубометров/час)':300,
        '-Допустимая стоимость оборудования ($)':100000,
        }

metadict_detail['Оборудование путепрокладчика'] = {
        # http://saper.isnet.ru/texnica/bat_m.html
        'Бульдозерное оборудование путепрокладчика':1,
        'Крановое оборудование путепрокладчика':1,
        'Лебёдка путепрокладчика':1,
        '-Производительность по расчистке завалов (километров/час)':0.2,
        '-Производительность по прокладке пути (километров/час)':5,
        '-Производительность по грунту (кубометров/час)':300,
        '-Допустимая масса оборудования (тонн)':5,
        '-Допустимая стоимость оборудования ($)':200000,
        }

metadict_detail['Оборудование инженерной машины разграждения'] = {
        # https://fireman.club/statyi-polzovateley/inzhenernaya-mashina-razgrazhdeniya-imr/
        'Бульдозерное оборудование инженерной машины разграждения':1,
        'Стреловое оборудование инженерной машины разграждения':1,
        '-Производительность по расчистке завалов (километров/час)':0.2,
        '-Производительность по прокладке пути (километров/час)':5,
        '-Производительность по грунту (кубометров/час)':100,
        '-Допустимая масса оборудования (тонн)':5,
        '-Допустимая стоимость оборудования ($)':1000000,
        }

metadict_detail['Оборудование машины для отрывки котлованов'] = {
        'Бульдозерное оборудование машины для отрывки котлованов':1,
        'Рабочий орган машины для отрывки котлованов':1,
        '-Производительность по грунту (кубометров/час)':500,
        '-Допустимая стоимость оборудования ($)':500000,
        }

metadict_detail['Оборудование быстроходной траншейной машины'] = {
        # В зависимости от грунта 265-800 метров 1.1x0.8 траншеи в час.
        'Ротор траншейного экскаватора':1,
        'Гидропривод траншейной машины':1,
        '|-Производство быстроходных траншейных машин (выпущено штук)':1,
        '-Производительность по грунту (кубометров/час)':500,
        '-Допустимая масса оборудования (тонн)':5,
        '-Допустимая стоимость оборудования ($)':200000,
        }

metadict_detail['Оборудование полковой землеройной машины'] = {
        'Ротор траншейного экскаватора':1,
        'Гидропривод траншейной машины':1,
        '|-Производство полковых землеройных машин (выпущено штук)':1,
        '-Производительность по грунту (кубометров/час)':140,
        '-Допустимая масса оборудования (тонн)':3,
        '-Допустимая стоимость оборудования ($)':200000,
        }

metadict_detail['Оборудование командно-штабной машины'] = {
        # http://www.rusarmy.com/svyaz/kshm/kshm_r-142n.html
        # https://www.snariad.ru/командно-штабная-машина-кшм-р-142н/
        'КВ-радиостанция возимая':2,
        'Аппаратура засекречивания':1,
        'Аппаратура определения свой-чужой':1,
        'Танковая навигационная аппаратура':1,
        'Терминал автоматической системы управления':1,
        '-Допустимая масса оборудования (тонн)':5,
        '-Допустимая стоимость оборудования ($)':500000,
        }

metadict_detail['Оборудование КВ-радиосвязи'] = {
        'Аппаратура засекречивания':1,
        'КВ-радиостанция возимая':2,
        }

metadict_detail['Оборудование автомастерской'] = {
        # http://www.gruzovikpress.ru/article/3222-masterskaya-tehnicheskogo-obslujivaniya-mto-at/
        'Электрогенератор (10 кВт)':1,
        'Стреловой кран (1.5 тонны)':1,
        'Слесарный верстак':1,
        'Станок точильно-шлифовальный':1,
        'Станок настольно-сверлильный':1,
        'Оборудование сварочно-зарядное':1,
        '|-Производство автомастерских (выпущено штук)':1,
        '-Допустимая масса оборудования (тонн)':4,
        '-Допустимая стоимость оборудования ($)':30000,
        }

metadict_detail['Оборудование мастерской'] = {
        # Исправить
        # На самом деле мастреские нифига не универсальные.
        'Электрогенератор (10 кВт)':1,
        'Стреловой кран (1.5 тонны)':1,
        'Слесарный верстак':1,
        'Станок точильно-шлифовальный':1,
        'Станок настольно-сверлильный':1,
        'Оборудование сварочно-зарядное':1,
        '|-Производство универсальных мастерских (выпущено штук)':1,
        '-Допустимая масса оборудования (тонн)':4,
        '-Допустимая стоимость оборудования ($)':30000,
        }

metadict_detail['Оборудование мастерской бронетехники'] = {
        'Электрогенератор (10 кВт)':1,
        'Тяжёлый стреловой кран':1,
        'Слесарный верстак':1,
        'Станок точильно-шлифовальный':1,
        'Станок настольно-сверлильный':1,
        'Оборудование сварочно-зарядное':1,
        '|-Производство универсальных мастерских (выпущено штук)':1,
        '-Допустимая масса оборудования (тонн)':4,
        '-Допустимая стоимость оборудования ($)':30000,
        }

metadict_detail['Оборудование пожарной машины'] = {
        'Тяжёлый стреловой кран':1,
        'Водомётная пушка пожарной машины':1,
        'Осветительная мачта пожарной машины':1,
        'Насосная станция пожарной машины':1,
        'Пеногенератор пожарной машины':1,
        }

metadict_detail['Оборудование передвижной хлебопекарной печи'] = {
        'Полевая хлебопекарная печь':1,
        'Переносная тестоотделительная машина':1,
        'Переносная тестоформовочная машина':1,
        '-Готовка хлеба (тонн/сутки)':1.5,
        }

metadict_detail['Оборудование передвижного тестоприготовительного агрегата'] = {
        'Полевой тестоприготовительный агрегат':1,
        'Переносная просеивательная машина':1,
        }

metadict_detail['Оборудование полевой бани'] = {
        'Резервуар резинно-тканевый (5 кубометров)':1,
        'Дезинфекционная камера (3.5 кубометра)':4,
        'Палатка-санпропускник':1,
        'Электрогенератор (10 кВт)':1,
        'Вентиляционно-отопительная установка':2,
        'Водонагреватель-паровой котёл (7 кубометров 40+ град. воды/час)':1,
        '-Помывка/банная личного состава (солдат/час)':32,
        '|-Производство полевых бань (выпущено штук)':1,
        '-Допустимая масса оборудования (тонн)':5,
        '-Допустимая стоимость оборудования ($)':50000,
        }

metadict_detail['Оборудование автомобильной полевой кухни'] = {
        'Компоненты автомобильной полевой кухни':1,
        '-Готовка горячей пищи (суточных пайков)':200,
        '|-Производство автомобильных полевых кухонь (выпущено штук)':1,
        '-Допустимая масса оборудования (тонн)':2,
        '-Допустимая стоимость оборудования ($)':7000,
        }

metadict_detail['Оборудование прицепной полевой кухни'] = {
        'Компоненты прицепной полевой кухни':1,
        '-Готовка горячей пищи (суточных пайков)':130,
        '|-Производство прицепных полевых кухонь (выпущено штук)':1,
        '-Допустимая масса оборудования (тонн)':1.5,
        '-Допустимая стоимость оборудования ($)':5000,
        }

metadict_detail['Оборудование полевой прачечной'] = {
        'Стиральная машина (35 кг белья/час)':1,
        '-Помывка и чистка униформы (килограмм/час)':35,
        '|-Производство прицепных полевых прачечных (выпущено штук)':1,
        }

metadict_detail['Оборудование сушильно-гладильной установки'] = {
        'Сушильно-гладильный станок (35 кг белья/час)':1,
        '-Сушка и глажка униформы (килограмм/час)':35,
        '|-Производство прицепных сушильно-гладильных установок (выпущено штук)':1,
        }

metadict_detail['Оборудование радиопеленгационного метеорологического комплекса'] = {
        # http://www.russianarms.ru/forum/index.php?topic=4193.0
        # https://topwar.ru/14707-ot-ulybki-stanet-nam-svetley-rpmk-1-ulybka.html
        }

metadict_detail['Оборудование станции радиоподавления'] = {
        }

metadict_detail['Оборудование станции радиоразведки'] = {
        }

metadict_detail['Оборудование радиотехнической разведки'] = {
        }

metadict_detail['Оборудование слесарной мастерской'] = {
        }

metadict_detail['Оборудование спутниковой связи'] = {
        }

metadict_detail['Оборудование станции дальней радиотехнической разведки'] = {
        }

metadict_detail['Оборудование станции зарядки маховиков'] = {
        }

metadict_detail['Оборудование станции помех наведению'] = {
        }

metadict_detail['Оборудование тепловой машины специальной обработки'] = {
        }

metadict_detail['Оборудование тяжёлого механизированного моста'] = {
        }

metadict_detail['Оборудование лесопильной рамы'] = {
        # http://saper.isnet.ru/texnica/lrv.html
        # Производительность (за 10 часов) -- 50-60 куб.м.
        'Зажимная тележка лесопильной рамы':2,
        'Поддерживающая тележка лесопильной рамы':2,
        'Транспортер лесопильной рамы':1,
        'Эстакада лесопильной рамы':1,
        'Пила лесопильной рамы':20,
        '-Производство досок и бруса (кубометров/час)':5,
        '|-Производство лесопильных рам (выпущено штук)':1,
        '-Допустимая масса оборудования (тонн)':3,
        '-Допустимая стоимость оборудования ($)':30000,
        }

metadict_detail['Оборудование станка заготовки свай'] = {
        # Не меньше 200 свай за смену, 100 кубометров стройматериалов.
        # https://vunivere.ru/work27880?screenshots=1
        '-Производство свай низководного моста (штук/час)':25,
        '|-Производство станков заготовки свай (выпущено штук)':1,
        '-Допустимая масса оборудования (тонн)':3,
        '-Допустимая стоимость оборудования ($)':30000,
        }

metadict_detail['Оборудование самоходного копера'] = {
        # Исправить
        # Молот УР-500; стреловой кран.
        # http://www.voentorg.by/catalog/527/9732/
        # ПСК-М-2x500
        'Сваебойный молот (0.5 тонны)':1,
        'Стреловой кран (6 тонн)':1,
        }

metadict_detail['Оборудование 60-квт газогенератора'] = {
        'Работа вариатора на синтез-газе (кВт)':60,
        '|-Производство 60-квт газогенераторов (выпущено штук)':1,
        '-Допустимая масса оборудования (тонн)':2,
        '-Допустимая стоимость оборудования ($)':10000,
        }

metadict_detail['Оборудование 200-квт газогенератора'] = {
        'Работа вариатора на синтез-газе (кВт)':200,
        '|-Производство 200-квт газогенераторов (выпущено штук)':1,
        '-Допустимая масса оборудования (тонн)':6,
        '-Допустимая стоимость оборудования ($)':30000,
        }

metadict_detail['Оборудование 60-квт электрогенератора'] = {
        'Работа электрогенератора на синтез-газе (кВт)':60,
        '|-Производство 60-квт электрогенераторов (выпущено штук)':1,
        '-Допустимая масса оборудования (тонн)':3,
        '-Допустимая стоимость оборудования ($)':20000,
        }

metadict_detail['Оборудование 200-квт дизель-электрической станции'] = {
        # ЭСДА-200Т/400 А1РКМ
        # https://www.d-system.ru/news/46/
        # http://www.200kilowatt.ru/generators/gsf-200/
        'Работа электрогенератора на дизельном топливе (кВт)':200,
        '|-Производство 200-квт дизель-электрических станций (выпущено штук)':1,
        '-Допустимая масса оборудования (тонн)':4,
        '-Допустимая стоимость оборудования ($)':100000,
        }

metadict_detail['Оборудование сервера АСУ'] = {
        }

metadict_detail['Оборудование установки разминирования'] = {
        }

metadict_detail['Оборудование центрального распределительного поста'] = {
        }

metadict_detail['Автомобильная водная цистерна'] = {
        '-Допустимая масса оборудования (тонн)':2,
        '-Место под воду (тонн)':5,
        '-Допустимая стоимость техники ($)':10000,
        }

metadict_detail['Автомобильная топливная цистерна'] = {
        '-Допустимая масса оборудования (тонн)':2,
        '-Место под жидкое топливо (литры)':7000,
        '-Допустимая стоимость техники ($)':10000,
        }

metadict_detail['Прицепная водная цистерна'] = {
        '-Допустимая масса оборудования (тонн)':0.7,
        '-Место под воду (тонн)':5,
        '-Допустимая стоимость техники ($)':5000,
        }

metadict_detail['Прицепная топливная цистерна'] = {
        '-Допустимая масса оборудования (тонн)':0.7,
        '-Место под жидкое топливо (литры)':5000,
        '-Допустимая стоимость техники ($)':5000,
        }

#----
# Навесное оборудование бронетехники:

metadict_detail['Оборудование для самоокапывания'] = {
        # Отвал шириной в 2.2 метра.
        'Танковый отвал':1,
        '-Производительность по грунту (кубометров/час)':20,
        '-Допустимая масса оборудования (тонн)':0.3,
        '-Допустимая стоимость оборудования ($)':5000,
        }

metadict_detail['Навесной танковый бульдозер'] = {
        # http://saper.isnet.ru/texnica/bty.html
        # Рабочий орган в 3.8x1 метра метра.
        'Рабочий орган навесного танкового бульдозера':1,
        'Гидропривод навесного танкового бульдозера':1,
        '-Производительность по грунту (кубометров/час)':130,
        '-Допустимая масса оборудования (тонн)':1.5,
        '-Допустимая стоимость оборудования ($)':100000,
        }

metadict_detail['Навесной дизельный двигатель (60 кВт)'] = {
        # Чисто понячье изобретение, чтобы поддерживать заряд в танковых маховиках:
        'Работа вариатора на дизельном топливе (кВт)':60,
        '|-Производство 60-квт дизельных двигателей (выпущено штук)':1,
        '-Допустимая масса оборудования (тонн)':1,
        '-Допустимая стоимость оборудования ($)':20000,
        }

metadict_detail['Навесной дизельный двигатель (120 кВт)'] = {
        'Работа вариатора на дизельном топливе (кВт)':120,
        '|-Производство 120-квт дизельных двигателей (выпущено штук)':1,
        '-Допустимая масса оборудования (тонн)':2,
        '-Допустимая стоимость оборудования ($)':50000,
        }
