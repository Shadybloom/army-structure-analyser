#----
# Навесное вооружение истребителей и планёров:

metadict_detail['Точка подвески (ракеты воздух-воздух)'] = {
        # https://ru.wikipedia.org/wiki/К-13_(авиационная_ракета)
        'Зенитные ракеты ближнего действия':2,
        }

metadict_detail['Точка подвески (ракета воздух-поверхность)'] = {
        # https://ru.wikipedia.org/wiki/Х-66
        'Авиационные управляемые ракеты':1,
        }

metadict_detail['Точка подвески (противотанковая кассетная авиабомба 250 кг)'] = {
        'Противотанковая кассетная авиабомба (250 кг)':1,
        }

metadict_detail['Точка подвески (24-мм спаренная авиационная пушка)'] = {
        # Уточнить вероятность поражения:
        '24-мм спаренная авиационная пушка':1,
        }

metadict_detail['Точка подвески (реактивные снаряды)'] = {
        '57-мм неуправляемые авиационные ракеты':3,
        }

metadict_detail['Точка подвески (управляемая ракета)'] = {
        'Управляемые ракеты ПТРК':1,
        }

metadict_detail['Точка подвески (зенитная ракета ПЗРК)'] = {
        'Зенитные ракеты ПЗРК':1,
        }

metadict_detail['Точка подвески (противотанковая кассетная авиабомба 50 кг)'] = {
        'Противотанковая кассетная авиабомба (50 кг)':1,
        }

metadict_detail['Точка подвески (единый пулемёт)'] = {
        'Единый пулемёт':1,
        }

#----
# Вооружение:

metadict_detail['Переносной зенитный ракетный комплекс'] = {
        'Зенитные ракеты ПЗРК':1,
        '-Допустимая масса вооружения (тонн)':0.005,
        '-Допустимая стоимость вооружения ($)':25000,
        }

metadict_detail['Переносной противотанковый ракетный комплекс'] = {
        'Управляемые ракеты ПТРК':4,
        '-Допустимая масса вооружения (тонн)':0.015,
        '-Допустимая стоимость вооружения ($)':100000,
        }

metadict_detail['Пехотный 40-мм гранатомёт'] = {
        # http://modernfirearms.net/grenade/usa/m79-r.html
        'Выстрелы 40x46-мм ГП':20,
        '-Заградительный огонь (метров фронта)':5,
        '-Допустимая масса вооружения (тонн)':0.003,
        '-Допустимая стоимость вооружения ($)':1000,
        }

metadict_detail['Стрелково-гранатомётный комплекс'] = {
        'Выстрелы 40x46-мм ГП':20,
        'Магазин на 50 патронов 6x48':8,
        '-Заградительный огонь (метров фронта)':5,
        '-Боевая скорострельность (выстрелов/минуту)':150,
        '-Допустимая масса вооружения (тонн)':0.01,
        '-Допустимая стоимость вооружения ($)':10000,
        }

metadict_detail['Станковый 40-мм автоматический гранатомёт'] = {
        # https://en.wikipedia.org/wiki/Mk_19_grenade_launcher
        'Короб на 30 выстрелов 40x53 АГС':3,
        '--Устойчивость к подавлению (в наступлении, РБ)':50,
        '--Устойчивость к подавлению (в окопах, РБ)':25,
        '--Устойчивость к подавлению (на марше, РБ)':15,
        '-Заградительный огонь (метров фронта)':25,
        '-Допустимая масса вооружения (тонн)':0.05,
        '-Допустимая стоимость вооружения ($)':60000,
        }

metadict_detail['Возимый 40-мм автоматический гранатомёт'] = {
        'Короб на 30 выстрелов 40x53 АГС':13,
        '-Заградительный огонь (метров фронта)':25,
        '-Допустимая масса вооружения (тонн)':0.05,
        '-Допустимая стоимость вооружения ($)':60000,
        }

metadict_detail['Станковый 12-мм пехотный пулемёт'] = {
        # НСВС-12,7 "Утёс" 1980 года -- себестоимость 5000 рублей (среднемесячная зарплата 174 рубля)
        # Вероятно, производство крупнокалиберных пулемётов обходилось в 4640 нормо-часов.
        # M2 Browning стоит всего-то 14 000$ (467 нормо-часов).
        # http://www.globalsecurity.org/military/systems/ground/m2-50cal-specs.htm
        'Короб на 50 патронов 12x96':5,
        '--Устойчивость к подавлению (в наступлении, РБ)':50,
        '--Устойчивость к подавлению (в окопах, РБ)':25,
        '--Устойчивость к подавлению (на марше, РБ)':15,
        '-Боевая скорострельность (выстрелов/минуту)':150,
        '-Допустимая масса вооружения (тонн)':0.05,
        '-Допустимая стоимость вооружения ($)':80000,
        }

metadict_detail['Носимый 12-мм пехотный пулемёт'] = {
        'Короб на 50 патронов 12x96':5,
        '-Боевая скорострельность (выстрелов/минуту)':150,
        '-Допустимая масса вооружения (тонн)':0.025,
        '-Допустимая стоимость вооружения ($)':80000,
        }

metadict_detail['Крупнокалиберный 15-мм танковый пулемёт'] = {
        # https://ru.wikipedia.org/wiki/КПВТ
        'Короб на 50 патронов 15x120':10,
        '-Боевая скорострельность (выстрелов/минуту)':150,
        '-Допустимая масса вооружения (тонн)':0.15,
        '-Допустимая стоимость вооружения ($)':50000,
        }

metadict_detail['Зенитный 12-мм танковый пулемёт'] = {
        # http://www.inetres.com/gp/military/cv/weapon/M85.html
        'Короб на 50 патронов 12x96':5,
        '-Допустимая масса вооружения (тонн)':0.03,
        '-Боевая скорострельность (выстрелов/минуту)':150,
        '-Допустимая стоимость вооружения ($)':60000,
        }

metadict_detail['Электромагнитная снайперская пушка'] = {
        'Стреловидные пули':100,
        'Спарк-батареи':100,
        '-Допустимая масса вооружения (тонн)':0.015,
        '-Боевая скорострельность (выстрелов/минуту)':30,
        '-Допустимая стоимость вооружения ($)':200000,
        }

metadict_detail['Единый пулемёт'] = {
        'Короб на 300 патронов 6x48':2,
        '-Боевая скорострельность (выстрелов/минуту)':250,
        '-Допустимая масса вооружения (тонн)':0.008,
        '-Допустимая стоимость вооружения ($)':4000,
        }

metadict_detail['Единый пулемёт танковый'] = {
        'Короб на 300 патронов 6x48':7,
        '-Допустимая масса вооружения (тонн)':0.008,
        '-Боевая скорострельность (выстрелов/минуту)':250,
        '-Допустимая стоимость вооружения ($)':4000,
        }

metadict_detail['Автоматический карабин'] = {
        'Магазин на 50 патронов 6x48':8,
        '-Боевая скорострельность (выстрелов/минуту)':150,
        '-Допустимая масса вооружения (тонн)':0.005,
        '-Допустимая стоимость вооружения ($)':2000,
        }

metadict_detail['Пистолет-пулемёт'] = {
        # https://en.wikipedia.org/wiki/MAC-10
        'Магазин на 30 патронов 12x32':2,
        '-Допустимая масса вооружения (тонн)':0.003,
        '-Допустимая стоимость вооружения ($)':1000,
        }

metadict_detail['Реактивный противотанковый гранатомёт'] = {
        'Реактивные гранаты':3,
        '-Допустимая масса вооружения (тонн)':0.003,
        '-Допустимая стоимость вооружения ($)':5000,
        }

metadict_detail['Реактивный пехотный огнемёт'] = {
        'Реактивные гранаты (зажигательные)':3,
        '-Заградительный огонь (метров фронта)':25,
        '-Допустимая масса вооружения (тонн)':0.003,
        '-Допустимая стоимость вооружения ($)':5000,
        }

metadict_detail['Лёгкий пехотный огнемёт'] = {
        'Баллоны огнесмеси':3,
        '-Заградительный огонь (метров фронта)':25,
        '-Допустимая масса вооружения (тонн)':0.012,
        '-Допустимая стоимость вооружения ($)':5000,
        }

metadict_detail['Электролазерная пушка'] = {
        # Рассчитай мощность электронного луча:
        'Спарк-батареи':100,
        '-Боевая скорострельность (выстрелов/минуту)':30,
        '-Допустимая масса вооружения (тонн)':0.02,
        '-Допустимая стоимость вооружения ($)':200000,
        }

metadict_detail['Электролазерная пушка танковая'] = {
        'Спарк-батареи':1000,
        '-Допустимая масса вооружения (тонн)':0.05,
        '-Боевая скорострельность (выстрелов/минуту)':30,
        '-Допустимая стоимость вооружения ($)':200000,
        }

metadict_detail['24-мм нарезная автоматическая пушка'] = {
        # http://www.inetres.com/gp/military/cv/weapon/M242.html
        'Выстрелы 24x120 осколочно-фугасные (в таре)':700,
        'Выстрелы 24x120 бронебойно-зажигательные (в таре)':300,
        '-Заградительный огонь (метров фронта)':25,
        '-Допустимая масса вооружения (тонн)':0.11,
        '-Допустимая стоимость вооружения ($)':100000,
        }

metadict_detail['24-мм спаренная авиационная пушка'] = {
        # https://ru.wikipedia.org/wiki/ГШ-23
        'Выстрелы 24x120 бронебойно-зажигательные (в таре)':200,
        '-Допустимая масса вооружения (тонн)':0.050,
        '-Допустимая стоимость вооружения ($)':200000,
        }

metadict_detail['Станковый 80-мм миномёт'] = {
        # http://bastion-karpenko.ru/2b14-podnos/
        'Миномётные мины 80-мм (в таре)':60,
        '-Расчётное огневое средство (РОС)':0.2,
        '-Заградительный огонь (метров фронта)':15,
        '-Допустимая масса вооружения (тонн)':0.042,
        '-Допустимая стоимость вооружения ($)':20000,
        }

metadict_detail['Автоматический 80-мм миномёт'] = {
        # http://bastion-opk.ru/2b9-vasilek/
        # https://ru.wikipedia.org/wiki/2Б9
        'Миномётные мины 80-мм (в таре)':240,
        '--Устойчивость к подавлению (в наступлении, РБ)':100,
        '--Устойчивость к подавлению (в окопах, РБ)':50,
        '--Устойчивость к подавлению (на марше, РБ)':25,
        '-Расчётное огневое средство (РОС)':0.5,
        '-Заградительный огонь (метров фронта)':30,
        '-Допустимая масса вооружения (тонн)':0.63,
        '-Допустимая стоимость вооружения ($)':200000,
        }

metadict_detail['Станковый 120-мм миномёт'] = {
        'Миномётные мины 120-мм (в таре)':30,
        '--Устойчивость к подавлению (в наступлении, РБ)':100,
        '--Устойчивость к подавлению (в окопах, РБ)':50,
        '--Устойчивость к подавлению (на марше, РБ)':25,
        '-Расчётное огневое средство (РОС)':0.5,
        '-Заградительный огонь (метров фронта)':30,
        '-Допустимая масса вооружения (тонн)':0.15,
        '-Допустимая стоимость вооружения ($)':50000,
        }

metadict_detail['120-мм гладкоствольная танковая пушка'] = {
        'Выстрелы 120-мм подкалиберные (в таре)':20,
        'Выстрелы 120-мм осколочно-фугасные (в таре)':20,
        '-Расчётное огневое средство (РОС)':0.7,
        '-Заградительный огонь (метров фронта)':30,
        '-Допустимая масса вооружения (тонн)':2.4,
        '-Допустимая стоимость вооружения ($)':200000,
        }

metadict_detail['Ствол 120-мм гаубицы'] = {
        'Выстрелы 120-мм осколочно-фугасные (в таре)':30,
        '-Расчётное огневое средство (РОС)':0.7,
        '-Заградительный огонь (метров фронта)':30,
        '-Допустимая стоимость вооружения ($)':200000,
        }

metadict_detail['Ствол 150-мм гаубицы'] = {
        'Выстрелы 150-мм осколочно-фугасные (в таре)':50,
        '-Расчётное огневое средство (РОС)':1,
        '-Заградительный огонь (метров фронта)':50,
        '-Допустимая стоимость вооружения ($)':200000,
        }

metadict_detail['Блок направляющих буксируемой 120-мм РСЗО'] = {
        'Реактивные снаряды 120-мм (в таре)':20,
        '-Расчётное огневое средство (РОС)':0.3,
        '-Заградительный огонь (метров фронта)':20,
        '-Допустимая стоимость вооружения ($)':50000,
        }

metadict_detail['Блок направляющих 120-мм РСЗО'] = {
        'Реактивные снаряды 120-мм (в таре)':40,
        '-Расчётное огневое средство (РОС)':0.7,
        '-Заградительный огонь (метров фронта)':30,
        '-Допустимая стоимость вооружения ($)':100000,
        }

metadict_detail['Направляющая тактической ракеты'] = {
        'Тактические ракеты':1,
        '-Расчётное огневое средство (РОС)':5.8,
        '-Допустимая стоимость вооружения ($)':50000,
        }

metadict_detail['Ложемент тактической ракеты'] = {
        'Тактические ракеты':1,
        }

metadict_detail['Направляющая оперативно-тактической ракеты'] = {
        'Оперативно-тактические ракеты':1,
        '-Расчётное огневое средство (РОС)':5.8,
        '-Допустимая стоимость вооружения ($)':50000,
        }

metadict_detail['Ложемент оперативно-тактической ракеты'] = {
        'Оперативно-тактические ракеты':1,
        }

metadict_detail['Ложемент зенитной ракеты большой дальности'] = {
        'Зенитные ракеты большой дальности':1,
        }

metadict_detail['80-мм мортира системы аэрозольных завес'] = {
        'Аэрозольные гранаты 80-мм':1,
        '-Допустимая масса вооружения (тонн)':0.01,
        '-Допустимая стоимость вооружения ($)':500,
        }

metadict_detail['Пусковая установка противотанковых ракет'] = {
        'Управляемые ракеты ПТРК':6,
        '-Допустимая масса вооружения (тонн)':0.15,
        '-Допустимая стоимость вооружения ($)':100000,
        }

metadict_detail['Пусковая установка зенитных ракет ближнего действия'] = {
        'Зенитные ракеты ближнего действия':6,
        '-Допустимая масса вооружения (тонн)':1,
        '-Допустимая стоимость вооружения ($)':500000,
        }

metadict_detail['Пусковая установка зенитных ракет малой дальности'] = {
        'Зенитные ракеты малой дальности':3,
        '-Допустимая масса вооружения (тонн)':1,
        '-Допустимая стоимость вооружения ($)':500000,
        }

metadict_detail['Пусковая установка зенитных ракет средней дальности'] = {
        'Зенитные ракеты средней дальности':2,
        '-Допустимая масса вооружения (тонн)':1,
        '-Допустимая стоимость вооружения ($)':500000,
        }

#----
# Снаряды в таре:

metadict_detail['Выстрелы 24x120 осколочно-фугасные (в таре)'] = {
        'Ящик 24-мм осколочно-фугасных снарядов (50 снарядов)':1/50,
        }

metadict_detail['Выстрелы 24x120 бронебойно-зажигательные (в таре)'] = {
        'Ящик 24-мм бронебойно-зажигательных снарядов (50 снарядов)':1/50,
        }

metadict_detail['Миномётные мины 80-мм (в таре)'] = {
        'Ящик 80-мм миномётных мин (8 мин)':1/8,
        }

metadict_detail['Миномётные мины 120-мм (в таре)'] = {
        'Ящик 120-мм миномётных мин (2 мины)':1/2,
        }

metadict_detail['Выстрелы 120-мм осколочно-фугасные (в таре)'] = {
        'Ящик 120-мм осколочно-фугасных снарядов (2 снаряда)':1/2,
        }

metadict_detail['Выстрелы 120-мм подкалиберные (в таре)'] = {
        'Ящик 120-мм подкалиберных снарядов (2 снаряда)':1/2,
        }

metadict_detail['Выстрелы 150-мм осколочно-фугасные (в таре)'] = {
        'Ящик 150-мм осколочно-фугасных снарядов (1 снаряд)':1,
        }

metadict_detail['Реактивные снаряды 120-мм (в таре)'] = {
        'Ящик 120-мм реактивных снарядов (1 снаряд)':1,
        }

#----
# Снарядные ящики, укупорки:

metadict_detail['Ящик 24-мм осколочно-фугасных снарядов (50 снарядов)'] = {
        'Выстрелы 24x120 осколочно-фугасные':50,
        '-Допустимая масса боеприпасов (тонн)':0.009,
        '-Допустимая стоимость боеприпасов ($)':5,
        }

metadict_detail['Ящик 24-мм бронебойно-зажигательных снарядов (50 снарядов)'] = {
        'Выстрелы 24x120 бронебойно-зажигательные':50,
        '-Допустимая масса боеприпасов (тонн)':0.009,
        '-Допустимая стоимость боеприпасов ($)':5,
        }

metadict_detail['Ящик 80-мм миномётных мин (8 мин)'] = {
        'Миномётные мины 80-мм':8,
        '-Допустимая масса боеприпасов (тонн)':0.022,
        '-Допустимая стоимость боеприпасов ($)':10,
        }

metadict_detail['Ящик 120-мм миномётных мин (2 мины)'] = {
        'Миномётные мины 120-мм':2,
        '-Допустимая масса боеприпасов (тонн)':0.022,
        '-Допустимая стоимость боеприпасов ($)':10,
        }

metadict_detail['Ящик 120-мм осколочно-фугасных снарядов (2 снаряда)'] = {
        'Выстрелы 120-мм осколочно-фугасные':2,
        '-Допустимая масса боеприпасов (тонн)':0.022,
        '-Допустимая стоимость боеприпасов ($)':10,
        }

metadict_detail['Ящик 120-мм подкалиберных снарядов (2 снаряда)'] = {
        'Выстрелы 120-мм подкалиберные':2,
        '-Допустимая масса боеприпасов (тонн)':0.022,
        '-Допустимая стоимость боеприпасов ($)':10,
        }

metadict_detail['Ящик 150-мм осколочно-фугасных снарядов (1 снаряд)'] = {
        'Выстрелы 150-мм осколочно-фугасные':1,
        '-Допустимая масса боеприпасов (тонн)':0.022,
        '-Допустимая стоимость боеприпасов ($)':10,
        }

metadict_detail['Ящик 120-мм реактивных снарядов (1 снаряд)'] = {
        'Реактивные снаряды 120-мм':1,
        '-Допустимая масса боеприпасов (тонн)':0.026,
        '-Допустимая стоимость боеприпасов ($)':10,
        }

#----
# Артиллерийские выстрелы, пороховые заряды:

metadict_detail['Выстрелы 120-мм осколочно-фугасные'] = {
        # http://www.russianarms.ru/forum/index.php/topic,11950.0.html
        'Снаряды 120-мм осколочно-фугасные':1,
        '-Допустимая масса боеприпасов (тонн)':0.007,
        '-Допустимая стоимость боеприпасов ($)':100,
        }

metadict_detail['Выстрелы 120-мм подкалиберные'] = {
        # http://www.russianarms.ru/forum/index.php/topic,9634.0.html
        'Снаряды 120-мм подкалиберные':1,
        '-Допустимая масса боеприпасов (тонн)':0.014,
        '-Допустимая стоимость боеприпасов ($)':100,
        }

metadict_detail['Выстрелы 150-мм осколочно-фугасные'] = {
        # http://www.russianarms.ru/forum/index.php/topic,11923.0.html
        'Снаряды 150-мм осколочно-фугасные':1,
        '-Допустимая масса боеприпасов (тонн)':0.017,
        '-Допустимая стоимость боеприпасов ($)':100,
        }

#----
# Магазины, короба, кассеты:

metadict_detail['Противотанковая кассетная авиабомба (50 кг)'] = {
        'Противотанковые кассетные суббоеприпасы':40,
        '-Допустимая масса боеприпасов (тонн)':0.012,
        '-Допустимая стоимость боеприпасов ($)':100,
        }

metadict_detail['Противотанковая кассетная авиабомба (250 кг)'] = {
        'Противотанковые кассетные суббоеприпасы':250,
        '-Допустимая масса боеприпасов (тонн)':0.012,
        '-Допустимая стоимость боеприпасов ($)':500,
        }

metadict_detail['Короб на 30 выстрелов 40x53 АГС'] = {
        'Лента на 30 выстрелов 40x53 АГС':1,
        '-Допустимая масса боеприпасов (тонн)':0.002,
        '-Допустимая стоимость боеприпасов ($)':5,
        }

metadict_detail['Короб на 50 патронов 12x96'] = {
        'Лента на 50 патронов 12x96':1,
        '-Допустимая масса боеприпасов (тонн)':0.001,
        '-Допустимая стоимость боеприпасов ($)':5,
        }

metadict_detail['Короб на 50 патронов 15x120'] = {
        'Лента на 50 патронов 15x120':1,
        '-Допустимая масса боеприпасов (тонн)':0.001,
        '-Допустимая стоимость боеприпасов ($)':5,
        }

metadict_detail['Короб на 300 патронов 6x48'] = {
        'Лента на 50 патронов 6x48':6,
        '-Допустимая масса боеприпасов (тонн)':0.001,
        '-Допустимая стоимость боеприпасов ($)':5,
        }

metadict_detail['Короб на 300 патронов 6x48 (запасной)'] = {
        'Лента на 50 патронов 6x48':6,
        '-Допустимая масса боеприпасов (тонн)':0.001,
        '-Допустимая стоимость боеприпасов ($)':5,
        }

metadict_detail['Магазин на 50 патронов 6x48'] = {
        'Патроны 6x48':50,
        '-Допустимая масса боеприпасов (тонн)':0.0003,
        '-Допустимая стоимость боеприпасов ($)':10,
        }

metadict_detail['Магазин на 30 патронов 12x32'] = {
        'Патроны 12x32':30,
        '-Допустимая масса боеприпасов (тонн)':0.0003,
        '-Допустимая стоимость боеприпасов ($)':10,
        }

#----
# Патронные ленты:

metadict_detail['Лента на 30 выстрелов 40x53 АГС'] = {
        'Выстрелы 40x53-мм АГС':30,
        '-Допустимая масса боеприпасов (тонн)':0.001,
        '-Допустимая стоимость боеприпасов ($)':5,
        }

metadict_detail['Лента на 50 патронов 12x96'] = {
        'Патроны 12x96':50,
        '-Допустимая масса боеприпасов (тонн)':0.001,
        '-Допустимая стоимость боеприпасов ($)':5,
        }

metadict_detail['Лента на 50 патронов 15x120'] = {
        'Патроны 15x120':50,
        '-Допустимая масса боеприпасов (тонн)':0.001,
        '-Допустимая стоимость боеприпасов ($)':5,
        }

metadict_detail['Лента на 50 снарядов 24x120 бронебойно-зажигательных'] = {
        'Выстрелы 24x120 бронебойно-зажигательные':50,
        '-Допустимая масса боеприпасов (тонн)':0.001,
        '-Допустимая стоимость боеприпасов ($)':5,
        }

metadict_detail['Лента на 50 снарядов 24x120 осколочно-фугасных'] = {
        'Выстрелы 24x120 осколочно-фугасные':50,
        '-Допустимая масса боеприпасов (тонн)':0.001,
        '-Допустимая стоимость боеприпасов ($)':5,
        }

metadict_detail['Лента на 50 патронов 6x48'] = {
        'Патроны 6x48':50,
        '-Допустимая масса боеприпасов (тонн)':0.0001,
        '-Допустимая стоимость боеприпасов ($)':1,
        }

#----
# Боеприпасы: патроны, снаряды, ракеты, авиабомбы.

metadict_detail['Наступательные гранаты'] = {
        # Пони используют "самонаводящиеся" единорожьей левитацией гранаты.
        '-Радиус поражения пехоты осколками (метров)':5,
        '-Допустимая масса боеприпасов (тонн)':0.00035,
        '-Допустимая стоимость боеприпасов ($)':50,
        }

metadict_detail['Светошумовые гранаты'] = {
        '-Допустимая масса боеприпасов (тонн)':0.00035,
        '-Допустимая стоимость боеприпасов ($)':100,
        }

metadict_detail['Дымовые гранаты'] = {
        # Гранаты вдвое меньше РДГ-2, дымовыделение 60-75 секунд.
        # https://ru.wikipedia.org/wiki/РДГ-2
        '-Длина дымовой завесы (метров)':10,
        '-Допустимая масса боеприпасов (тонн)':0.00035,
        '-Допустимая стоимость боеприпасов ($)':25,
        }

metadict_detail['Баллоны огнесмеси'] = {
        '-Допустимая масса боеприпасов (тонн)':0.003,
        '-Допустимая стоимость боеприпасов ($)':25,
        }

metadict_detail['Выстрелы 40x46-мм ГП'] = {
        # 40-мм граната M406 HE: выстрел 230 г; взрывчатка 33 г; радиус поражения -- 5 м.
        # http://www.inetres.com/gp/military/infantry/grenade/40mm_ammo.html#M406
        # http://www.russianarms.ru/forum/index.php/topic,855.0.html
        '-Радиус поражения пехоты осколками (метров)':4,
        '-Допустимая масса боеприпасов (тонн)':0.00023,
        '-Допустимая стоимость боеприпасов ($)':50,
        }

metadict_detail['Выстрелы 40x46-мм ГП (запасные)'] = {
        '-Радиус поражения пехоты осколками (метров)':4,
        '-Допустимая масса боеприпасов (тонн)':0.00023,
        '-Допустимая стоимость боеприпасов ($)':50,
        }

metadict_detail['Выстрелы 40x46-мм ГП (светошумовые)'] = {
        '-Допустимая масса боеприпасов (тонн)':0.00023,
        '-Допустимая стоимость боеприпасов ($)':50,
        }

metadict_detail['Выстрелы 40x46-мм ГП (дымовые)'] = {
        '-Длина дымовой завесы (метров)':10,
        '-Допустимая масса боеприпасов (тонн)':0.00023,
        '-Допустимая стоимость боеприпасов ($)':50,
        }

metadict_detail['Выстрелы 40x53-мм АГС'] = {
        # 40-мм граната M430 HE-DP: выстрел 330 г; взрывчатка 33г; радиус поражения -- 5 м.
        # http://www.navweaps.com/Weapons/WNUS_40mm_Mortar_mk19.php
        '-Радиус поражения пехоты осколками (метров)':4,
        '-Допустимая масса боеприпасов (тонн)':0.00033,
        '-Допустимая стоимость боеприпасов ($)':50,
        }

metadict_detail['Выстрелы 40x53-мм АГС (светошумовые)'] = {
        '-Допустимая масса боеприпасов (тонн)':0.00033,
        '-Допустимая стоимость боеприпасов ($)':50,
        }

metadict_detail['Выстрелы 40x53-мм АГС (дымовые)'] = {
        '-Длина дымовой завесы (метров)':10,
        '-Допустимая масса боеприпасов (тонн)':0.00033,
        '-Допустимая стоимость боеприпасов ($)':50,
        }

metadict_detail['Авиационные управляемые ракеты'] = {
        # Ракета Х-23 "Гром", дальность 3-10 километров, радиокомандное наведение:
        # http://rbase.new-factoria.ru/missile/wobb/x23/x23.shtml
        '-Вероятность поражения цели снарядом (танк)':0.6,
        '-Допустимая масса боеприпасов (тонн)':0.29,
        '-Допустимая стоимость боеприпасов ($)':50000,
        }

metadict_detail['Управляемые ракеты ПТРК'] = {
        # Ракета 9М14 ПТРК "Малютка", дальность до 3 километров, управление по проводам:
        # Бронепробиваемость 200-400 миллиметров, вероятность пробития брони М60 -- 0.6
        # http://rbase.new-factoria.ru/missile/wobb/malutka/malutka.shtml
        '-Вероятность поражения цели снарядом (танк)':0.7,
        '-Допустимая масса боеприпасов (тонн)':0.011,
        '-Допустимая стоимость боеприпасов ($)':25000,
        }

metadict_detail['Зенитные ракеты ПЗРК'] = {
        # Ракета 9М32 ПЗРК "Стрела", дальность до 3.4 километров, пассивная тепловая ГСН:
        # http://rbase.new-factoria.ru/missile/wobb/strela_2m/shema.htm
        '-Вероятность поражения цели ракетой (самолёт)':0.35,
        '-Допустимая масса боеприпасов (тонн)':0.01,
        '-Допустимая стоимость боеприпасов ($)':25000,
        }

metadict_detail['Зенитные ракеты ближнего действия'] = {
        # Твердотопливная ракета 9М33 комплекса "Оса", дальность до 9 километров, пассивная тепловая ГСН:
        '-Вероятность поражения цели ракетой (самолёт)':0.35,
        '-Допустимая масса боеприпасов (тонн)':0.128,
        '-Допустимая стоимость боеприпасов ($)':100000,
        }

metadict_detail['Зенитные ракеты малой дальности'] = {
        # Твердотопливная ракета 3М9 комплекса "Куб", дальность 5-25 километров, полуактивна РГСН:
        # https://ru.wikipedia.org/wiki/3М9
        '-Вероятность поражения цели ракетой (самолёт)':0.7,
        '-Допустимая масса боеприпасов (тонн)':0.6,
        '-Допустимая стоимость боеприпасов ($)':500000,
        }

metadict_detail['Зенитные ракеты средней дальности'] = {
        # Жидкотопливная ракета 3М8 комплекса "Круг", дальность 25-50 километров, полуактивная РГСН:
        # https://ru.wikipedia.org/wiki/3М8
        '-Вероятность поражения цели ракетой (самолёт)':0.7,
        '-Допустимая масса боеприпасов (тонн)':2.5,
        '-Допустимая стоимость боеприпасов ($)':1000000,
        }

metadict_detail['Зенитные ракеты большой дальности'] = {
        # Жидкотопливная ракета 5В21А комплекса С-200, дальность до 240 километров, активная РГСН:
        # http://armyman.info/rakety/zenitnye/21519-5v21.html
        'Ядерный заряд зенитной ракеты':1/10,
        '-Вероятность поражения цели ракетой (самолёт)':0.9,
        '-Допустимая масса боеприпасов (тонн)':7.1,
        '-Допустимая стоимость боеприпасов ($)':3000000,
        }

metadict_detail['Стреловидные пули'] = {
        # Для электромагнитных снайперских винтовок:
        # Урановые ломы в миниатюре (посчитай калибр/длину/плотность, не ленись)
        '-Вероятность поражения цели снарядом (ББМ)':0.9,
        '-Допустимая масса боеприпасов (тонн)':0.00002,
        '-Допустимая стоимость боеприпасов ($)':20,
        }

metadict_detail['Спарк-батареи'] = {
        # Хм, кажется, батарейкам среди боеприпасов делать нечего:
        '-Допустимая масса боеприпасов (тонн)':0.00002,
        '-Допустимая стоимость боеприпасов ($)':20,
        }

metadict_detail['Патроны 12x32'] = {
        # Для оружия самообороны, боевые показатели не учитываются.
        # Патрон: 22 г; пуля: 14 г; нач.скорость 260 м/с; энергия 473 Дж:
        # https://ru.wikipedia.org/wiki/.45_ACP
        # http://www.gewehr.ru/ammo/184-patron-.45-acp.html
        '-Допустимая масса боеприпасов (тонн)':0.000022,
        '-Допустимая стоимость боеприпасов ($)':0.2,
        }

metadict_detail['Патроны 6x48'] = {
        # Патрон: 15 г; пуля: 5 г; нач.скорость 1100 м/с; энергия 3000 Дж:
        # http://sniper-weapon.ru/boepripasy/370-patron-6kh49-mm
        '-Вероятность поражения цели пулей (боец)':0.1,
        '-Допустимая масса боеприпасов (тонн)':0.000015,
        '-Допустимая стоимость боеприпасов ($)':0.5,
        }

metadict_detail['Патроны 12x96'] = {
        # Патрон: 110 г; пуля 40 г; нач.скорость 900 м/с; энергия 16 200 Дж.
        # Бронепробиваемость: 20 мм гомогенной стальной брони с дистанции 300 метров.
        # http://www.militaryparitet.com/nomen/russia/strel/patroni/data/ic_nomenrussiastrelpatroni/1/
        # http://www.smallarms.ru/carticle?ammo=50br
        '-Вероятность поражения цели снарядом (ББМ)':0.02,
        '-Допустимая масса боеприпасов (тонн)':0.00011,
        '-Допустимая стоимость боеприпасов ($)':10,
        }

metadict_detail['Патроны 15x120'] = {
        # Патрон: 200 г; пуля 64 г; нач.скорость 1000 м/с; энергия 32 000 Дж.
        # Бронепробиваемость: 20 мм гомогенной стальной брони с дистанции 800 метров.
        # http://www.militaryparitet.com/nomen/russia/strel/patroni/data/ic_nomenrussiastrelpatroni/1/
        # https://ru.wikipedia.org/wiki/Крупнокалиберный_пулемёт_Владимирова
        '-Вероятность поражения цели снарядом (ББМ)':0.02,
        '-Допустимая масса боеприпасов (тонн)':0.0002,
        '-Допустимая стоимость боеприпасов ($)':10,
        }

metadict_detail['Реактивные гранаты'] = {
        # Выстрел ПГ-7ВМ для РПГ-7, головной калибр 70-мм, дальность -- 500 метров.
        # Бронепробиваемость 300 миллиметров, вероятность пробития брони М60 -- 0.6
        '-Вероятность поражения цели снарядом (танк)':0.3,
        '-Допустимая масса боеприпасов (тонн)':0.002,
        '-Допустимая стоимость боеприпасов ($)':500,
        }

metadict_detail['Реактивные гранаты (запасные)'] = {
        '-Вероятность поражения цели снарядом (танк)':0.3,
        '-Допустимая масса боеприпасов (тонн)':0.002,
        '-Допустимая стоимость боеприпасов ($)':500,
        }

metadict_detail['Реактивные гранаты (зажигательные)'] = {
        # Старый добрый напалм. Как бы его эффективность рассчитать?
        '-Вероятность поражения цели снарядом (ББМ)':0.3,
        '-Допустимая масса боеприпасов (тонн)':0.003,
        '-Допустимая стоимость боеприпасов ($)':1000,
        }

metadict_detail['57-мм неуправляемые авиационные ракеты'] = {
        # Эффективная дальность пуска: 800—1800 м
        # Круговое вероятное отклонение: 0.35% от дальности
        # https://ru.wikipedia.org/wiki/С-5_(НАР)
        # http://www.aveaprom.ru/oruzie-nurs-s5.php
        '-Вероятность поражения цели снарядом (ББМ)':0.3,
        '-Допустимая масса боеприпасов (тонн)':0.0037,
        '-Допустимая стоимость боеприпасов ($)':1000,
        }

metadict_detail['Элемент динамической защиты'] = {
        # ДЗ не место среди боеприпасов:
        '-Допустимая масса боеприпасов (тонн)':0.0015,
        '-Допустимая стоимость боеприпасов ($)':500,
        }

metadict_detail['Выстрелы 24x120 осколочно-фугасные'] = {
        # 23-мм ОФЗ: выстрел 435 г; снаряд: 184 г:
        # http://armsdata.net/russia/0673.html
        '-Радиус поражения пехоты осколками (метров)':2,
        '-Допустимая масса боеприпасов (тонн)':0.00045,
        '-Допустимая стоимость боеприпасов ($)':100,
        }

metadict_detail['Выстрелы 24x120 бронебойно-зажигательные'] = {
        # 23-мм БЗТ: выстрел 450 г; снаряд: 190 г; нач.скорость 970 м/с; энергия 89 000 Дж:
        # Бронепробиваемость (угол 30, скорость втречи 530 м/с) — 10 мм стали (лоб БТР, борт БМП)
        # http://armsdata.net/russia/0673.html
        '-Вероятность поражения цели снарядом (ББМ)':0.04,
        '-Допустимая масса боеприпасов (тонн)':0.00045,
        '-Допустимая стоимость боеприпасов ($)':100,
        }

metadict_detail['Аэрозольные гранаты 80-мм'] = {
        # http://www.inetres.com/gp/military/cv/weapon/launchers.html
        '-Длина дымовой завесы (метров)':30,
        '-Допустимая масса боеприпасов (тонн)':0.003,
        '-Допустимая стоимость боеприпасов ($)':200,
        }

metadict_detail['Миномётные мины 80-мм'] = {
        # http://www.russianarms.ru/forum/index.php/topic,4403.0.html
        '-Расчётный боеприпас (РБ)':0.1,
        '-Радиус поражения пехоты осколками (метров)':6,
        '-Радиус поражения бронетехники осколками (метров)':1,
        '-Допустимая масса боеприпасов (тонн)':0.0031,
        '-Допустимая стоимость боеприпасов ($)':300,
        }

metadict_detail['Миномётные мины 120-мм'] = {
        # http://www.russianarms.ru/forum/index.php/topic,12101.0.html
        '-Расчётный боеприпас (РБ)':0.6,
        '-Радиус поражения пехоты осколками (метров)':20,
        '-Радиус поражения бронетехники осколками (метров)':16,
        '-Допустимая масса боеприпасов (тонн)':0.016,
        '-Допустимая стоимость боеприпасов ($)':500,
        }

metadict_detail['Снаряды 120-мм осколочно-фугасные'] = {
        '-Расчётный боеприпас (РБ)':0.7,
        '-Радиус поражения пехоты осколками (метров)':23,
        '-Радиус поражения бронетехники осколками (метров)':18,
        '-Допустимая масса боеприпасов (тонн)':0.022,
        '-Допустимая стоимость боеприпасов ($)':700,
        }

metadict_detail['Снаряды 120-мм подкалиберные'] = {
        # ЗБМ-16, Длина 410 мм, диаметр стержня 36 мм, масса — 3.6 кг, начальная скорость 1780 м/с.
        # Вероятность попадания Т-62 в М60А1 на дистанции 1 500 м составляет 50%:
        # http://fofanov.armor.kiev.ua/Tanks/ARM/apfsds/ammo_r.html
        # http://btvt.narod.ru/4/t-62/v2.jpg
        # http://btvt.narod.ru/4/t-62/v1.jpg
        '-Вероятность поражения цели снарядом (танк)':0.5 * 0.5,
        '-Допустимая масса боеприпасов (тонн)':0.006,
        '-Допустимая стоимость боеприпасов ($)':10000,
        }

metadict_detail['Снаряды 150-мм осколочно-фугасные'] = {
        '-Расчётный боеприпас (РБ)':1,
        '-Радиус поражения пехоты осколками (метров)':26,
        '-Радиус поражения бронетехники осколками (метров)':20,
        '-Допустимая масса боеприпасов (тонн)':0.044,
        '-Допустимая стоимость боеприпасов ($)':1000,
        }

metadict_detail['Реактивные снаряды 120-мм'] = {
        '-Расчётный боеприпас (РБ)':0.6,
        '-Допустимая масса боеприпасов (тонн)':0.056,
        '-Допустимая стоимость боеприпасов ($)':1000,
        }

metadict_detail['Противотанковые кассетные суббоеприпасы'] = {
        # http://armor.kiev.ua/ptur/weapon/ptab1m.html
        # http://www.warmech.ru/war_weapon/ptab2.html
        '-Вероятность поражения цели авиабомбой (боец)':0.02,
        '-Вероятность поражения цели авиабомбой (танк)':0.01,
        '-Допустимая масса боеприпасов (тонн)':0.00035,
        '-Допустимая стоимость боеприпасов ($)':30,
        }

metadict_detail['Тактические ракеты'] = {
        # Кумулятивная кассетная боевая часть:
        '-Расчётный боеприпас (РБ)':300,
        '-Допустимая масса боеприпасов (тонн)':2.5,
        '-Допустимая стоимость боеприпасов ($)':1000000,
        }

metadict_detail['Оперативно-тактические ракеты'] = {
        'Ядерный заряд тактической ракеты':1/3,
        '-Расчётный боеприпас (РБ)':300,
        '-Допустимая масса боеприпасов (тонн)':6,
        '-Допустимая стоимость боеприпасов ($)':1000000,
        }

metadict_detail['Стратегические ядерные ракеты'] = {
        # https://ru.wikipedia.org/wiki/УР-100
        # https://ru.wikipedia.org/wiki/УР-100К
        'Ядерный заряд стратегической ракеты':6,
        '-Допустимая масса боеприпасов (тонн)':50,
        '-Допустимая стоимость боеприпасов ($)':50000000,
        }

metadict_detail['Ракета-носитель'] = {
        '-Допустимая масса боеприпасов (тонн)':50,
        '-Допустимая стоимость боеприпасов ($)':50000000,
        }

metadict_detail['Ядерный заряд тактической ракеты'] = {
        'Ядерные заряды (25 килотонн)':1,
        '-Расчётный боеприпас (РБ)':2400,
        '-Допустимая масса боеприпасов (тонн)':0.2,
        '-Допустимая стоимость боеприпасов ($)':5000000,
        }

metadict_detail['Ядерный заряд зенитной ракеты'] = {
        'Ядерные заряды (25 килотонн)':1,
        '--Противовоздушные возможности (по самолётам)':2,
        '-Допустимая масса боеприпасов (тонн)':0.2,
        '-Вероятность поражения цели ракетой (самолёт)':2,
        '-Допустимая стоимость боеприпасов ($)':5000000,
        }

metadict_detail['Ядерный заряд стратегической ракеты'] = {
        'Ядерные заряды (500 килотонн)':1,
        '-Допустимая масса боеприпасов (тонн)':0.2,
        '-Допустимая стоимость боеприпасов ($)':10000000,
        }
