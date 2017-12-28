#----
# Бронирование корпуса ОБТ:

metadict_detail['Верхняя лобовая деталь корпуса ОБТ'] = {
        # http://btvt.narod.ru/4/armor.htm
        # Комбинированная броня: 80-мм лист стали, два 50-мм листа стеклопластика, 20-мм лист стали.
        # Ширина корпуса -- 2 метра, длина плиты -- 1.2 метра, толщина -- 200 мм (наклон 68 градусов)
        'Броневая сталь 80-мм (квадратные метры)':2 * 1.2,
        'Броневой стеклопластик 50-мм (квадратные метры)':(2 * 1.2) * 2,
        'Броневая сталь 20-мм (квадратные метры)':2 * 1.2,
        }

metadict_detail['Нижняя лобовая деталь корпуса ОБТ'] = {
        # Комбинированная броня: 80-мм лист стали, два 50-мм листа стеклопластика, 20-мм лист стали.
        # Ширина корпуса -- 2 метра, длина плиты -- 0.5 метра, толщина -- 200 мм (наклон 60 градусов)
        'Броневая сталь 80-мм (квадратные метры)':2 * 0.5,
        'Броневой стеклопластик 50-мм (квадратные метры)':(2 * 0.5) * 2,
        'Броневая сталь 20-мм (квадратные метры)':2 * 0.5,
        }

metadict_detail['Бортовая бронеплита корпуса ОБТ'] = {
        # Длина корпуса -- 6.6 метра, высота корпуса -- 1 метр, толщина -- 80 мм (вертикально)
        'Броневая сталь 80-мм (квадратные метры)':6.6 * 1,
        }

metadict_detail['Верхний кормовой бронелист корпуса ОБТ'] = {
        # Ширина корпуса -- 2 метра, длина плиты -- 0.6 метра, толщина -- 45 мм (вертикально)
        'Броневая сталь 45-мм (квадратные метры)':2 * 0.6,
        }

metadict_detail['Нижний кормовой бронелист корпуса ОБТ'] = {
        # Ширина корпуса -- 2 метра, длина плиты -- 0.6 метра, толщина -- 16 мм (наклон 70 градусов)
        'Броневая сталь 16-мм (квадратные метры)':2 * 0.6,
        }

metadict_detail['Передний бронелист крыши корпуса ОБТ'] = {
        # Длина крыши до отсека МТО -- 3 метра, ширина корпуса -- 2 метра,
        # Радиус выреза башни -- 0.9 метра, толщина крыши -- 30 мм (горизонтально)
        'Броневая сталь 30-мм (квадратные метры)':3 * 2 - (3.14159265 * 0.9 ** 2),
        }

metadict_detail['Задний бронелист крыши корпуса ОБТ'] = {
        # Длина крыши МТО -- 3.6 метра, ширина корпуса -- 2 метра, толщина -- 16 мм (наклон 10 градусов)
        'Броневая сталь 16-мм (квадратные метры)':3.6 * 2,
        }

metadict_detail['Днище корпуса ОБТ'] = {
        # Длина днища -- 5.8 метров, ширина корпуса -- 2 метра, толщина -- 20 мм (горизонтально)
        'Броневая сталь 20-мм (квадратные метры)':5.8 * 2,
        }

metadict_detail['Динамическая защита корпуса ОБТ'] = {
        'Секция динамической защиты':18,
        }

#----
# Бронирование корпуса БМД:

metadict_detail['Верхняя лобовая деталь корпуса БМД'] = {
        # Стальная катаная броня, прозрачная бронекерамика, щитки на окнах.
        # Ширина корпуса -- 1.8 метра, длина листа -- 2 метра, толщина -- 10 мм (наклон 50 градусов)
        'Броневая сталь 10-мм (квадратные метры)':1.8 * 2,
        'Прозрачная бронекерамика 50-мм (квадратные метры)':1.8 * 0.4,
        }

metadict_detail['Нижняя лобовая деталь корпуса БМД'] = {
        # Ширина корпуса -- 1.8 метра, длина листа -- 0.5 метра, толщина -- 10 мм (наклон 60 градусов)
        'Броневая сталь 10-мм (квадратные метры)':1.8 * 0.5,
        }

metadict_detail['Бортовой бронелист корпуса БМД'] = {
        # Длина корпуса -- 4.2 метра, высота корпуса -- 1 метр, толщина -- 10 мм (вертикально)
        'Броневая сталь 10-мм (квадратные метры)':4.2 * 1,
        }

metadict_detail['Кормовой бронелист корпуса БМД'] = {
        # Ширина корпуса -- 1.8 метра, высота корпуса -- 1 метр, толщина -- 5 мм (вертикально)
        'Броневая сталь 5-мм (квадратные метры)':1.8 * 1,
        }

metadict_detail['Крыша корпуса БМД'] = {
        # Вырез под башню не учитываем, поскольку у машин разного назначения очень разные башни.
        # Ширина корпуса -- 1.8 метра, длина листа -- 2 метра, толщина -- 5 мм (горизонтально)
        'Броневая сталь 5-мм (квадратные метры)':1.8 * 2,
        }

metadict_detail['Днище корпуса БМД'] = {
        # Ширина корпуса -- 1.8 метра, длина машины -- 4.2 метра, толщина -- 5 мм (горизонтально)
        'Броневая сталь 5-мм (квадратные метры)':4.2 * 1.8,
        }

#----
# Бронирование корпуса БТР:

metadict_detail['Верхняя лобовая деталь корпуса БТР'] = {
        # Стальная катаная броня, прозрачная бронекерамика (да, пони умеют)
        # Ширина корпуса -- 2.8 метра, длина листа -- 2 метра, толщина -- 10 мм (наклон 50 градусов)
        'Броневая сталь 10-мм (квадратные метры)':2.8 * 2,
        'Прозрачная бронекерамика 50-мм (квадратные метры)':3 * 0.4,
        }

metadict_detail['Нижняя лобовая деталь корпуса БТР'] = {
        # Стальная катаная броня. 
        # Ширина корпуса -- 2.8 метра, длина листа -- 0.5 метра, толщина -- 5 мм (наклон 60 градусов)
        'Броневая сталь 5-мм (квадратные метры)':2.8 * 0.5,
        }

metadict_detail['Верхний бортовой бронелист корпуса БТР'] = {
        # Листы со значительными углами наклона, куда большими, чем в технике из мира людей.
        # Рост пони в холке -- 60 сантиметров, длина тела (от хвоста до груди) -- 45 см
        # В машине "ромбовидного" сечения поням удобнее поворачиваться и стрелять из бойниц.
        # Длина корпуса -- 7.5 метра, ширина листа -- 0.7 метра, толщина -- 5 мм (наклон 70 градусов)
        'Броневая сталь 5-мм (квадратные метры)':6.6 * 0.7,
        }

metadict_detail['Нижний бортовой бронелист корпуса БТР'] = {
        # Длина корпуса -- 7.5 метра, ширина листа -- 0.7 метра, толщина -- 5 мм (наклон 70 градусов)
        'Броневая сталь 5-мм (квадратные метры)':6.6 * 0.7,
        }

metadict_detail['Кормовой бронелист корпуса БТР'] = {
        # Ширина корпуса -- 2.8 метра, длина листа -- 1 метр, толщина -- 5 мм (вертикально)
        'Броневая сталь 5-мм (квадратные метры)':2.8 * 1,
        }

metadict_detail['Крыша корпуса БТР'] = {
        # Крыша узкая, поскольку пони маленькие создания, а сечение машины практически ромбовидное.
        # Вырез под башню не учитываем, поскольку у машин разного назначения очень разные башни.
        # Длина корпуса -- 7.5 метра, ширина листа -- 1.8 метра, толщина -- 5 мм (горизонтально)
        'Броневая сталь 5-мм (квадратные метры)':7.5 * 1.8,
        }

metadict_detail['Днище корпуса БТР'] = {
        # Днище широкое, поскольку вместо ДВС и дизеля пони используют широкие, плоские супермаховики.
        # Длина корпуса -- 7.5 метра, ширина листа -- 2.2 метра, толщина -- 5 мм (горизонтально)
        'Броневая сталь 5-мм (квадратные метры)':7.5 * 2.2,
        }

#----
# Бронирование кабины военного грузовика:

metadict_detail['Верхняя лобовая деталь кабины военного грузовика'] = {
        # Ширина кабины -- 2.5 метра, длина листа -- 1.2 метра, толщина -- 5 мм (наклон 70 градусов)
        'Броневая сталь 5-мм (квадратные метры)':(2.5 * 1.2) - (2.3 * 0.6),
        'Прозрачная бронекерамика 20-мм (квадратные метры)':2.3 * 0.6,
        }

metadict_detail['Нижняя лобовая деталь кабины военного грузовика'] = {
        # Ширина кабины -- 2.5 метра, длина листа -- 1.2 метра, толщина -- 5 мм (наклон 70 градусов)
        'Броневая сталь 5-мм (квадратные метры)':2.5 * 1.2,
        }

metadict_detail['Бортовой бронелист кабины военного грузовика'] = {
        # Длина кабины -- 2 метра, высота -- 1.2 метра, толщина -- 5 мм (вертикально)
        'Броневая сталь 5-мм (квадратные метры)':(2 * 1.2) - (0.6 * 0.3),
        'Прозрачная бронекерамика 20-мм (квадратные метры)':0.6 * 0.3,
        }

metadict_detail['Кормовой бронелист кабины военного грузовика'] = {
        # Ширина кабины -- 2.5 метра, высота -- 1.2 метра, толщина -- 5 мм (вертикально)
        'Броневая сталь 5-мм (квадратные метры)':2.5 * 1.2,
        }

metadict_detail['Крыша кабины военного грузовика'] = {
        # Ширина кабины -- 2.5 метра, длина листа -- 1.5 метра, толщина -- 5 мм (вертикально)
        'Броневая сталь 5-мм (квадратные метры)':2.5 * 1.5,
        }

metadict_detail['Днище кабины военного грузовика'] = {
        # Ширина кабины -- 2.5 метра, длина листа -- 1.5 метра, толщина -- 5 мм (вертикально)
        'Броневая сталь 5-мм (квадратные метры)':2.5 * 1.5,
        }

#----
# Бронирование башни ОБТ:

metadict_detail['Лобовая деталь броневой башни ОБТ'] = {
        # Радиус основания башни -- 0.9 метров, радиус крыши -- 0.3 метра, высота -- 0.6 метра.
        # Комбинированная броня: 80 мм сталь + 3x50 мм стеклопластик + 150 мм сталь.
        # Вычисляем через площадь усчённого конуса: S=Pi*(r1+r2)*l
        # (с каждым слоем брони радиус основания башни уменьшается)
        # (вычисленную площадь делим на 4, потому что детали лобовые и их две)
        'Броневая сталь 80-мм (квадратные метры)':3.14159265 * (0.9 + 0.3) * 0.6 / 4,
        'Броневой стеклопластик 50-мм (квадратные метры)':3.14159265 * (0.82 + 0.22) * 0.6 / 4 * 3,
        'Броневая сталь 150-мм (квадратные метры)':3.14159265 * (0.67 + 0.07) * 0.6 / 4,
        }

metadict_detail['Бортовая деталь броневой башни ОБТ'] = {
        # Радиус основания кормы башни -- 0.67 метров, радиус крыши -- 0.3 метра, высота -- 0.6 метра.
        # Вычисляем через площадь усчённого конуса: S=Pi*(r1+r2)*l
        # (вычисленную площадь делим на 2, потому что передняя половина башни, это лобовые детали)
        'Броневая сталь 60-мм (квадратные метры)':3.14159265 * (0.67 + 0.3) * 0.6 / 2,
        }

metadict_detail['Крыша броневой башни ОБТ'] = {
        # Радиус крыши 0.3 метра, вычисляем через площадь круга: S=Pi*r^2
        'Броневая сталь 60-мм (квадратные метры)':3.14159265 * (0.3 ** 2),
        }

#metadict_detail['Лобовая часть литой башни ОБТ'] = {
#        # Радиус башни -- 0.9 метров, высота -- 0.8 метра.
#        # Комбинированная броня: 90 мм сталь + 150 мм алюминий + 90 мм сталь.
#        # https://www.fxyz.ru/формулы_по_геометрии/формулы_объема/объем_шарового_сегмента/
#        'Броневая сталь (кубометров)':(3.14159265 * 0.8 ** 2 * (0.9 - 1 / 3 * 0.8) - 3.14159265 * 0.71 ** 2 * (0.81 - 1 / 3 * 0.71)) / 2,
#        'Броневой алюминий (кубометров)':(3.14159265 * 0.8 ** 2 * (0.9 - 1 / 3 * 0.8) - 3.14159265 * 0.55 ** 2 * (0.65 - 1 / 3 * 0.55)) / 2,
#        }
#
#metadict_detail['Бортовая часть литой башни ОБТ'] = {
#        # Радиус башни -- 0.9 метров, высота -- 0.8 метра, толщина брони -- 65 мм.
#        # https://www.fxyz.ru/формулы_по_геометрии/формулы_объема/объем_шарового_сегмента/
#        'Броневая сталь (кубометров)':(3.14159265 * 0.8 ** 2 * (0.9 - 1 / 3 * 0.8) - 3.14159265 * 0.735 ** 2 * (0.835 - 1 / 3 * 0.735)) / 2,
#        }

metadict_detail['Динамическая защита башни ОБТ'] = {
        'Секция динамической защиты':8,
        }

#----
# Бронирование башни САУ:

metadict_detail['Лобовая деталь башни САУ'] = {
        # Ширина парной детали -- 1 метр, длина листа -- 1.6 метра, толщина -- 10 мм (наклон 70 градусов)
        'Броневая сталь 20-мм (квадратные метры)':1 * 1.6,
        }

metadict_detail['Бортовая деталь башни САУ'] = {
        # Длина башни -- 3 метра, длина листа -- 1.6 метра, толщина -- 10 мм (наклон 70 градусов)
        'Броневая сталь 10-мм (квадратные метры)':3 * 1.6,
        }

metadict_detail['Кормовая деталь башни САУ'] = {
        # Ширина башни -- 2 метра, длина листа -- 1.6 метра, толщина -- 10 мм (наклон 70 градусов)
        'Броневая сталь 10-мм (квадратные метры)':2 * 1.6,
        }

metadict_detail['Крыша башни САУ'] = {
        # Ширина крыши -- 1.6 метра, длина листа -- 2.5 метра, толщина -- 10 мм (наклон 70 градусов)
        'Броневая сталь 10-мм (квадратные метры)':2.5 * 1.6,
        }

#----
# Бронирование башни БТР:

metadict_detail['Бортовой бронелист башни БТР'] = {
        # Радиус основания -- 0.8 метра, радиус крыши 0.4 метра, высота 0.6 метра
        # Вычисляем через площадь усчённого конуса: S=Pi*(r1+r2)*l
        'Броневая сталь 10-мм (квадратные метры)':3.14159265 * (0.8 + 0.4) * 0.6,
        }

metadict_detail['Крыша башни БТР'] = {
        # Радиус крыши 0.4 метра, вычисляем через площадь круга: S=Pi*r^2
        'Броневая сталь 5-мм (квадратные метры)':3.14159265 * (0.4 ** 2),
        }

#----
# Прочие элементы, отсортировать:

metadict_detail['Секция динамической защиты'] = {
        'Крепление элемента динамической защиты':14,
        'Элемент динамической защиты':14,
        }

metadict_detail['Комплект катков ОБТ'] = {
        'Направляющее колесо ОБТ':2,
        'Поддерживающий каток ОБТ':8,
        'Ведущее колесо ОБТ':2,
        'Опорный каток ОБТ':12,
        }

metadict_detail['Подвеска ОБТ'] = {
        # Связывает корпус танка с опорными катками
        # Не более 4-7% от массы машины, 6-8% от внутреннего объёма
        'Узел подвески ОБТ':12,
        }

metadict_detail['Узел подвески ОБТ'] = {
        'Торсион ОБТ':1,
        'Телескопический гидроамортизатор ОБТ':1,
        'Балансир ОБТ':1,
        }

metadict_detail['Подвеска БТР'] = {
        'Узел подвески БТР':8,
        }

metadict_detail['Подвеска военного грузовика'] = {
        'Мост военного грузовика':3,
        }

metadict_detail['Водомётный движитель БТР'] = {
        # От танка ПТ-76:
        # Удельная мощность -- 12.6 кВт; тяга 11 кН; скорость по воде 10.2 км/час
        # диаметр рабочего колеса 340 мм; гидравлическое сечение 0.181 кв. метра (пять лопастей)
        'Приёмный патрубок водомётного движителя БТР':1,
        'Редуктор водомётного движителя БТР':1,
        'Передний гребной винт БТР':1,
        'Задний гребной винт БТР':1,
        }

metadict_detail['Комплект колёс БТР'] = {
        'Колесо БТР':8,
        }

metadict_detail['Комплект колёс военного грузовика'] = {
        'Колесо военного грузовика':6,
        }

metadict_detail['Танковая система защиты от оружия массового поражения'] = {
        'Танковое электромеханическое оборудование (килограмм)':30,
        'Танковый прибор радиационной и химической разведки':1,
        'Танковая фильтровентиляционная установка':1,
        }

metadict_detail['Танковая система пожаротушения'] = {
        'Танковое электромеханическое оборудование (килограмм)':2,
        'Танковые гидроприводы (метры)':20,
        'Баллон огнегасящей смеси':4,
        'Термодатчики':7,
        }

metadict_detail['Вариатор танкового маховика'] = {
        '-Объём используемый (кубометров)':1,
        '-Допустимая масса деталей (тонн)':0.5,
        '-Допустимая стоимость оборудования ($)':30000,
        }

metadict_detail['Вариатор среднего маховика'] = {
        '-Объём используемый (кубометров)':0.3,
        '-Допустимая масса деталей (тонн)':0.3,
        '-Допустимая стоимость оборудования ($)':20000,
        }

metadict_detail['Вариатор лёгкого маховика'] = {
        '-Объём используемый (кубометров)':0.15,
        '-Допустимая масса деталей (тонн)':0.2,
        '-Допустимая стоимость оборудования ($)':15000,
        }

metadict_detail['Танковый маховик'] = {
        # Диаметр -- 1.8 метра; высота -- 0.18 метра.
        'Корпус танкового маховика':1,
        'Диск танкового маховика':1,
        'Магнитный подвес танкового маховика':1,
        '-Объём используемый (кубометров)':3.14159265 * 0.9 ** 2 * 0.18,
        }

metadict_detail['Система стабилизации танковой пушки'] = {
        '-Допустимая масса деталей (тонн)':0.5,
        '-Допустимая стоимость оборудования ($)':200000,
        }

metadict_detail['Механизм заряжания танковой пушки'] = {
        '-Допустимая масса деталей (тонн)':0.5,
        '-Допустимая стоимость оборудования ($)':100000,
        }

metadict_detail['Поворотный механизм танковой башни'] = {
        '-Допустимая масса деталей (тонн)':0.5,
        '-Допустимая стоимость оборудования ($)':50000,
        }

metadict_detail['Танковая система активной защиты'] = {
        'Комплекс оптико-электронного подавления':1,
        'Система постановки аэрозольных завес':1,
        }

metadict_detail['Туррель зенитного пулемёта'] = {
        'Зенитный 12-мм танковый пулемёт':1,
        'Приводы управления туррелью':1,
        }

metadict_detail['Туррель крупнокалиберного пулемёта'] = {
        'Крупнокалиберный 15-мм танковый пулемёт':1,
        'Единый пулемёт танковый':1,
        'Приводы управления туррелью':1,
        }

metadict_detail['Приводы управления туррелью'] = {
        '-Допустимая масса деталей (тонн)':0.05,
        '-Допустимая стоимость оборудования ($)':5000,
        }

metadict_detail['Комплекс оптико-электронного подавления'] = {
        'Датчики обнаружения лазерного излучения':4,
        'Инфракрасные прожекторы':2,
        }

metadict_detail['Система постановки аэрозольных завес'] = {
        # http://www.inetres.com/gp/military/cv/weapon/launchers.html
        '80-мм мортира системы аэрозольных завес':12,
        }

metadict_detail['Датчики обнаружения лазерного излучения'] = {
        '-Допустимая масса деталей (тонн)':0.001,
        '-Допустимая стоимость оборудования ($)':1000,
        }

metadict_detail['Инфракрасные прожекторы'] = {
        '-Допустимая масса деталей (тонн)':0.05,
        '-Допустимая стоимость оборудования ($)':3000,
        }

metadict_detail['Система перенаправления лазерного луча'] = {
        '-Допустимая масса деталей (тонн)':0.05,
        '-Допустимая стоимость оборудования ($)':50000,
        }

metadict_detail['Информационно-управляющая система'] = {
        'Оптические компьютеры (терминалы)':1,
        'Танковая навигационная аппаратура':1,
        'УКВ-радиостанция возимая':1,
        'КВ-радиостанция возимая':1,
        '-Допустимая масса деталей (тонн)':0.03,
        '-Допустимая стоимость оборудования ($)':500000,
        }

metadict_detail['Приборы наблюдения и наведения ОБТ'] = {
        'Прицел-дальномер прибор наведения':1,
        'Прицельно-наблюдательный комплекс командира':1,
        'Приборы наблюдения механика-водителя':1,
        }

metadict_detail['Приборы наблюдения и наведения БТР'] = {
        'Перископический прицел':2,
        'Перископический прибор наблюдения':6,
        'Активно-пассивный прибор ночного видения':2,
        }

metadict_detail['Прицел-дальномер прибор наведения'] = {
        'Перископический прицел':1,
        'Танковый лазерный дальномер':1,
        'Тепловизионный перископический ночной прицел':1,
        }

metadict_detail['Перископический прицел'] = {
        '-Допустимая масса деталей (тонн)':0.01,
        '-Допустимая стоимость оборудования ($)':5000,
        }

metadict_detail['Танковый лазерный дальномер'] = {
        '-Допустимая масса деталей (тонн)':0.01,
        '--Потребление энергии (кВт)':0.1,
        '-Допустимая стоимость оборудования ($)':20000,
        }

metadict_detail['Тепловизионный перископический ночной прицел'] = {
        'Охлаждаемая тепловизионная матрица':1,
        '-Допустимая масса деталей (тонн)':0.06,
        '--Потребление энергии (кВт)':1,
        '-Допустимая стоимость оборудования ($)':100000,
        }

metadict_detail['Прицельно-наблюдательный комплекс командира'] = {
        'Перископический прицел':1,
        'Танковый лазерный дальномер':1,
        'Тепловизионный перископический ночной прицел':1,
        }

metadict_detail['Приборы наблюдения механика-водителя'] = {
        'Перископический прибор наблюдения':3,
        'Активно-пассивный прибор ночного видения':1,
        }

metadict_detail['Перископический прибор наблюдения'] = {
        '-Допустимая масса деталей (тонн)':0.01,
        '-Допустимая стоимость оборудования ($)':500,
        }

metadict_detail['Активно-пассивный прибор ночного видения'] = {
        '-Допустимая масса деталей (тонн)':0.002,
        '-Допустимая стоимость оборудования ($)':5000,
        }

metadict_detail['Танковая система управления огнём'] = {
        'Цифровой баллистический вычислитель':1,
        'Телевизионная система кругового обзора':1,
        'Комплект автоматических датчиков условий стрельбы':1,
        }

metadict_detail['Цифровой баллистический вычислитель'] = {
        'Оптические компьютеры (терминалы)':1,
        '-Допустимая масса деталей (тонн)':0.02,
        '-Допустимая стоимость оборудования ($)':500000,
        }

metadict_detail['Телевизионная система кругового обзора'] = {
        '-Допустимая масса деталей (тонн)':0.05,
        '-Допустимая стоимость оборудования ($)':50000,
        }

metadict_detail['Комплект автоматических датчиков условий стрельбы'] = {
        '-Допустимая масса деталей (тонн)':0.02,
        '-Допустимая стоимость оборудования ($)':20000,
        }

metadict_detail['Танковая навигационная аппаратура'] = {
        '-Допустимая масса деталей (тонн)':0.01,
        '-Допустимая стоимость оборудования ($)':10000,
        }

metadict_detail['Авиагоризонт'] = {
        '-Допустимая масса деталей (тонн)':0.01,
        '-Допустимая стоимость оборудования ($)':10000,
        }

metadict_detail['Речной широкозахватный миноискатель'] = {
        '-Допустимая масса деталей (тонн)':0.05,
        '-Допустимая стоимость оборудования ($)':20000,
        }

metadict_detail['Танковое переговорное устройство'] = {
        'Ларингофон':4,
        '-Допустимая масса деталей (тонн)':0.03,
        '-Допустимая стоимость оборудования ($)':1000,
        }

metadict_detail['Маскировочный комплект танка'] = {
        'Маскировочная ткань (квадратные метры)':40,
        '-Допустимая масса деталей (тонн)':0.5,
        '-Допустимая стоимость оборудования ($)':20000,
        }

metadict_detail['Танковая система кондиционирования'] = {
        '-Допустимая масса деталей (тонн)':0.03,
        '--Потребление энергии (кВт)':3,
        '-Допустимая стоимость оборудования ($)':30000,
        }

metadict_detail['Станция ближней разведки танковая'] = {
        'Оптические компьютеры (терминалы)':1,
        '-Допустимая масса деталей (тонн)':0.2,
        '--Потребление энергии (кВт)':1,
        '-Допустимая стоимость оборудования ($)':500000,
        }

#----
# Авиационное оборудование:

metadict_detail['Планер истребителя'] = {
        'Гермокабина истребителя':1,
        'Внутренние системы истребителя':1,
        'Фюзеляж истребителя':1,
        'Крыло истребителя':1,
        'Хвостовой стабилизатор истребителя':1,
        'Шасси истребителя':1,
        }

metadict_detail['Топливная система истребителя'] = {
        'Топливный бак истребителя':12,
        '-Место под жидкое топливо (литры)':2880,
        }

metadict_detail['Турбореактивный двигатель истребителя'] = {
        '|-Производство турбореактивных двигателей (выпущено штук)':1,
        '--Потребление энергии (кВт)':20000,
        }

metadict_detail['Ядерный реактор транспортного экранолёта'] = {
        '|-Производство авиационных ядерных реакторов (выпущено штук)':1,
        '--Производство энергии (кВт)':100000,
        }

metadict_detail['Ядерный воздушно-реактивный двигатель'] = {
        '|-Производство воздушно-реактивных двигателей (выпущено штук)':1,
        '--Потребление энергии (кВт)':100000,
        }

metadict_detail['Грузовая кабина транспортного экранолёта'] = {
        # https://ru.wikipedia.org/wiki/Ил-76
        # Коэффициент полноты 0.2, полезный объём 0.3 (оценочно):
        '-Объём груза (кубометров)':(62.1 * 102 * 20.4) * 0.2 * 0.3,
        }

metadict_detail['Грузовая кабина тяжёлого планёра'] = {
        '-Объём груза (кубометров)':11 * 3 * 3,
        }

metadict_detail['Грузовая кабина лёгкого планёра'] = {
        '-Объём груза (кубометров)':3.14159265 * 0.25 ** 2 * 5,
        }

#----
# Элементы конструкции планёра:

metadict_detail['9-метровые шпангоуты фюзеляжа тяжёлого планёра'] = {
        # Кольца сечением 15x30мм
        'Конструкционный углепластик (кубометров)':9*0.015*0.03,
        }

metadict_detail['17-метровые стрингеры фюзеляжа тяжёлого планёра'] = {
        # К ним крепится обшивка. Профили сечением 5x60мм
        'Конструкционный углепластик (кубометров)':17*0.005*0.06,
        }

metadict_detail['17-метровые лонжероны фюзеляжа тяжёлого планёра'] = {
        # Основа конструкции, брусья толщиной 30x40 мм.
        'Конструкционный углепластик (кубометров)':17*0.03*0.04,
        }

metadict_detail['3-метровые стрингеры крыла тяжёлого планёра'] = {
        # К ним крепится обшивка. Профили сечением 5x60мм
        'Конструкционный углепластик (кубометров)':3*0.005*0.06,
        }

metadict_detail['9-метровые лонжероны крыла тяжёлого планёра'] = {
        # Основа конструкции, брусья толщиной 30x20 мм.
        'Конструкционный углепластик (кубометров)':9*0.03*0.02,
        }

metadict_detail['3.4-метровые лонжероны оперения тяжёлого планёра'] = {
        'Конструкционный углепластик (кубометров)':3.4*0.03*0.02,
        }

metadict_detail['1.8-метровые стрингеры оперения тяжёлого планёра'] = {
        'Конструкционный углепластик (кубометров)':1.8*0.005*0.06,
        }

metadict_detail['6-метровые стрингеры оперения тяжёлого планёра'] = {
        'Конструкционный углепластик (кубометров)':6*0.005*0.06,
        }

metadict_detail['Пол грузовой кабины тяжёлого планёра (квадратные метры)'] = {
        # Высокопрочные фанерные листы толщитой 3-мм
        # На самом деле очень тяжёлый материал. Нужна тканевая обшивка.
        'Бекелитовая фанера (кубометров)':17*0.03*0.03,
        }

metadict_detail['Обшивка фюзеляжа тяжёлого планёра (квадратные метры)'] = {
        # Фанера слишком тяжёлая. Нужна тканевая обшивка.
        'Синтетический брезент (квадратные метры)':1,
        }

metadict_detail['Обшивка крыла тяжёлого планёра (квадратные метры)'] = {
        # Нейлон?
        'Синтетический брезент (квадратные метры)':1,
        }

metadict_detail['Обшивка оперения тяжёлого планёра (квадратные метры)'] = {
        'Синтетический брезент (квадратные метры)':1,
        }

#----
# Переносные приборы:

metadict_detail['Станция ближней разведки'] = {
        'Компоненты переносной РЛС':1,
        'Ленточный супермаховик малогабаритный (килограмм)':1,
        '|-Производство станций ближней разведки (выпущено штук)':1,
        '--Потребление энергии (кВт)':0.1,
        '-Допустимая масса оборудования (тонн)':0.02,
        '-Допустимая стоимость оборудования ($)':200000,
        }

metadict_detail['Лазерный прибор разведки'] = {
        'Компоненты лазерного прибора разведки':1,
        'Ленточный супермаховик малогабаритный (килограмм)':1,
        '|-Производство лазерных приборов разведки (выпущено штук)':1,
        '--Потребление энергии (кВт)':0.1,
        '-Допустимая масса оборудования (тонн)':0.005,
        '-Допустимая стоимость оборудования ($)':10000,
        }

metadict_detail['Тепловизионный прибор разведки'] = {
        'Компоненты тепловизионного прибора разведки':1,
        'Ленточный супермаховик малогабаритный (килограмм)':10,
        '|-Производство тепловизионных приборов разведки (выпущено штук)':1,
        '--Потребление энергии (кВт)':1,
        '-Допустимая масса оборудования (тонн)':0.1,
        '-Допустимая стоимость оборудования ($)':100000,
        }

metadict_detail['Индукционный миноискатель полупроводниковый'] = {
        'Компоненты индукционного миноискателя':1,
        '|-Производство индукционных миноискателей (выпущено штук)':1,
        '--Потребление энергии (кВт)':0.1,
        '-Допустимая масса оборудования (тонн)':0.002,
        '-Допустимая стоимость оборудования ($)':100,
        }

metadict_detail['Переносной радиоволновый миноискатель'] = {
        # http://the-mostly.ru/misc/perenosnoy_radiovolnovyy_minoiskatel_rvm_2m.html
        'Компоненты радиоволнового миноискателя':1,
        '|-Производство радиоволновых миноискателей (выпущено штук)':1,
        '--Потребление энергии (кВт)':0.1,
        '-Допустимая масса оборудования (тонн)':0.003,
        '-Допустимая стоимость оборудования ($)':100,
        }

metadict_detail['Инженерный разведывательный эхолокатор'] = {
        'Компоненты инженерного разведывательного эхолокатора':1,
        '|-Производство инженерных разведывательных эхолокаторов (выпущено штук)':1,
        '--Потребление энергии (кВт)':0.1,
        '-Допустимая масса оборудования (тонн)':0.003,
        '-Допустимая стоимость оборудования ($)':200,
        }

metadict_detail['Прибор инженерной разведки (перископ)'] = {
        'Компоненты прибора инженерной разведки (перископа)':1,
        '|-Производство приборов инженерной разведки (выпущено штук)':1,
        '-Допустимая масса оборудования (тонн)':0.003,
        '-Допустимая стоимость оборудования ($)':200,
        }

metadict_detail['Пегасо-переносимая радиорелейная станция'] = {
        'Компоненты пегасо-переносимой радиорелейной станции':1,
        '|-Производство пегасо-переносимых радирелейных станций (выпущено штук)':1,
        '-Допустимая масса оборудования (тонн)':0.2,
        '-Допустимая стоимость оборудования ($)':10000,
        }

metadict_detail['Пегасо-переносимое устройство радиоподавления'] = {
        'Компоненты пегасо-переносимого устройства радиоподавления':1,
        'Ленточный супермаховик малогабаритный (килограмм)':50,
        '|-Производство пегасо-переносимых устройств радиоподавления (выпущено штук)':1,
        '--Потребление энергии (кВт)':5,
        '-Допустимая масса оборудования (тонн)':0.2,
        '-Допустимая стоимость оборудования ($)':200000,
        }

metadict_detail['Пегасо-переносимое устройство радиоразведки'] = {
        'Компоненты пегасо-переносимого устройства радиоразведки':1,
        'Ленточный супермаховик малогабаритный (килограмм)':1,
        '|-Производство пегасо-переносимых устройств радиоразведки (выпущено штук)':1,
        '--Потребление энергии (кВт)':0.1,
        '-Допустимая масса оборудования (тонн)':0.2,
        '-Допустимая стоимость оборудования ($)':200000,
        }

metadict_detail['Пегасо-переносимая станция звукометрической разведки'] = {
        'Компоненты пегасо-переносимого станции звукометрической разведки':1,
        'Ленточный супермаховик малогабаритный (килограмм)':1,
        '|-Производство пегасо-переносимых станций звукометрической разведки (выпущено штук)':1,
        '--Потребление энергии (кВт)':0.1,
        '-Допустимая масса оборудования (тонн)':0.2,
        '-Допустимая стоимость оборудования ($)':20000,
        }

metadict_detail['УКВ-радиостанция возимая'] = {
        # https://ru.wikipedia.org/wiki/Р-159
        # Дальность связи:
        # На штыревую антенну 1,5 м в режиме ТлФ до 12 км, в режиме ТлГ до 18 км;
        # На штыревую антенну 2,7 м в режиме ТлФ до 18 км, в режиме ТлГ до 27 км;
        # На антенну бегущей волны в режиме ТлФ до 35 км, в режиме ТлГ до 50 км;
        # При установке на автомобиле и антенне 1,5 м при скорости до 60 км/ч — до 8 км.
        'Ларингофон':1,
        'Наушники радиостанции':1,
        'Антенна бегущей волны':1,
        'Штыревая антенна 2.7 метров':1,
        'Штыревая антенна 1.5 метров':1,
        'Универсальный источник питания':1,
        'Компоненты возимой УКВ-радиостанции':1,
        '|-Производство возимых УКВ-радиостанций (выпущено штук)':1,
        '--Потребление энергии (кВт)':0.05,
        '-Допустимая масса оборудования (тонн)':0.04,
        '-Допустимая стоимость оборудования ($)':20000,
        }

metadict_detail['КВ-радиостанция возимая'] = {
        'Ларингофон':1,
        'Наушники радиостанции':1,
        'Антенна бегущей волны':1,
        'Штыревая антенна 2.7 метров':1,
        'Штыревая антенна 1.5 метров':1,
        'Универсальный источник питания':1,
        'Компоненты возимой КВ-радиостанции':1,
        '|-Производство возимых КВ-радиостанций (выпущено штук)':1,
        '--Потребление энергии (кВт)':0.1,
        '-Допустимая масса оборудования (тонн)':0.04,
        '-Допустимая стоимость оборудования ($)':20000,
        }

metadict_detail['УКВ-радиостанция переносная'] = {
        # https://ru.wikipedia.org/wiki/Р-159
        # Дальность связи:
        # На штыревую антенну 1,5 м в режиме ТлФ до 12 км, в режиме ТлГ до 18 км;
        # На штыревую антенну 2,7 м в режиме ТлФ до 18 км, в режиме ТлГ до 27 км;
        # На антенну бегущей волны в режиме ТлФ до 35 км, в режиме ТлГ до 50 км;
        # При установке на автомобиле и антенне 1,5 м при скорости до 60 км/ч — до 8 км.
        'Ларингофон':1,
        'Наушники радиостанции':1,
        'Штыревая антенна 2.7 метров':1,
        'Штыревая антенна 1.5 метров':1,
        'Универсальный источник питания':1,
        'Компоненты переносной УКВ-радиостанции':1,
        '|-Производство переносных УКВ-радиостанций (выпущено штук)':1,
        '--Потребление энергии (кВт)':0.05,
        '-Допустимая масса оборудования (тонн)':0.02,
        '-Допустимая стоимость оборудования ($)':20000,
        }

metadict_detail['КВ-радиостанция переносная'] = {
        'Ларингофон':1,
        'Наушники радиостанции':1,
        'Штыревая антенна 2.7 метров':1,
        'Штыревая антенна 1.5 метров':1,
        'Универсальный источник питания':1,
        'Компоненты переносной КВ-радиостанции':1,
        '|-Производство переносных УКВ-радиостанций (выпущено штук)':1,
        '--Потребление энергии (кВт)':0.1,
        '-Допустимая масса оборудования (тонн)':0.02,
        '-Допустимая стоимость оборудования ($)':40000,
        }

metadict_detail['Персональная электронно-вычислительная машина'] = {
        # https://en.wikipedia.org/wiki/Grid_Compass
        'Ларингофон':1,
        'Наушники радиостанции':1,
        'Универсальный источник питания':1,
        'Компоненты персональной электронно-вычислительной машины':1,
        '|-Производство персональных электронно-вычислительных машин (выпущено штук)':1,
        '--Потребление энергии (кВт)':0.05,
        '-Допустимая масса оборудования (тонн)':0.02,
        '-Допустимая стоимость оборудования ($)':20000,
        }
