#----
# 3. Infanterie-Division (mot.)
# https://rostislavddd.livejournal.com/280269.html
# http://www.niehorster.org/011_germany/symbols/_symbols_figures.html

#---
# Противник:

metadict_army['Ротная тактическая группа'] = {
        'Моторизованная стрелковая рота (Schützenkompanie c (mot))':1,
        'Приданные подразделения':1,
        'Поддерживающие подразделения':1,
        }

metadict_army['Приданные подразделения'] = {
        'Усиленный мотоциклетно-стрелковый взвод (Kraftradschützenzug)':1,
        'Противотанковый взвод (Ausführung A)':1,
        }

metadict_army['Поддерживающие подразделения'] = {
        'Боевая батарея 105-мм гаубиц (Gefechtsbatterie)':1,
        'Эскадрилья пикирующих бомбардировщиков (Junkers Ju 87B)':1,
        'Танковый взвод средних танков':1,
        }

#---
# Специальные подразделения:

metadict_army['Усиленный мотоциклетно-стрелковый взвод (Kraftradschützenzug)'] = {
        'Управление мотоциклетного стрелкового взвода':1,
        'Мотоциклетное стрелковое отделение (Kraftradschützengruppe)':3,
        'Мотоциклетное пулемётное отделение (s.M.G.Schützengruppe)':1,
        }

metadict_army['Усиленная моторизованная стрелковая рота (Schützenkompanie c (mot))'] = {
        'Управление моторизованной стрелковой роты (Gruppe Führer)':1,
        'Моторизованный стрелковый взвод (Schützenzug)':3,
        'Мотоциклетный пулемётный взвод (s.M.G.Halbzug)':1,
        'Тыл моторизованной стрелковой роты':1,
        }

metadict_army['Эскадрилья пикирующих бомбардировщиков (Junkers Ju 87B)'] = {
        'Пикирующий бомбардировщик (Junkers Ju 87B)':12,
        }

#---
# Роты:

metadict_army['Мотоциклетная стрелковая рота (Kraftradschützenkompanie (mot))'] = {
        # https://www.wwiidaybyday.com/kstn/kstn11111okt37.htm
        'Управление мотоциклетной стрелковой роты (Gruppe Führer)':1,
        'Мотоциклетный стрелковый взвод (Kraftradschützenzug)':3,
        'Мотоциклетный пулемётный взвод (s.M.G.Halbzug)':1,
        'Тыл мотоциклетной стрелковой роты':1,
        }

metadict_army['Моторизованная стрелковая рота (Schützenkompanie c (mot))'] = {
        # http://www.wwiidaybyday.com/kstn/kstn138c1nov41.htm
        'Управление моторизованной стрелковой роты (Gruppe Führer)':1,
        'Моторизованный стрелковый взвод (Schützenzug)':3,
        'Тыл моторизованной стрелковой роты':1,
        }

metadict_army['Стрелковая рота (Schützenkompanie c)'] = {
        # http://army.armor.kiev.ua/hist/rota-131c.shtml
        # http://www.wwiidaybyday.com/kstn/kstn131c1feb41.htm
        'Управление стрелковой роты (Gruppe Führer)':1,
        'Стрелковый взвод (Schützenzug)':3,
        'Тыл стрелковой роты':1,
        }

metadict_army['Моторизованная противотанковая рота (Infanteriepanzerjägerkompanie c)'] = {
        # Допилить тыл и управление
        # https://www.wwiidaybyday.com/kstn/kstn184c31jan41.htm
        'Управление противотанковой роты (Gruppe Führer)':1,
        'Противотанковый взвод (Ausführung A)':4,
        'Тыл противотанковой роты':1,
        }

metadict_army['Танковая рота (Infanteriepanzerjägerkompanie c)'] = {
        # Допилить управление роты со взводом лёгких танков и полувзводом средних
        # Допилить тыл
        # https://www.wwiidaybyday.com/kstn/kstn1171b1feb41.htm
        'Управление танковой роты (Gruppe Führer)':1,
        'Танковый взвод средних танков':2,
        'Танковый взвод огневой поддержки средних танков':1,
        'Тыл танковой роты':1,
        }

metadict_army['Лёгкая моторизованная артиллерийская батарея (Batterie leichte Feldhaubitze)'] = {
        # http://army.armor.kiev.ua/hist/artbatarea-457.shtml
        # https://www.wwiidaybyday.com/kstn/kstn4341okt38.htm
        'Управление артиллерийской батареи (Gruppe Führer)':1,
        'Команда связи (Nachrichtenstaffel)':1,
        'Боевая батарея 105-мм гаубиц (Gefechtsbatterie)':1,
        'Тыл моторизованной артиллерийской батареи':1,
        }

metadict_army['Боевая батарея 105-мм гаубиц (Gefechtsbatterie)'] = {
        'Управление боевой батареи':1,
        'Орудийная команда 105-мм гаубиц (Geschützstaffel)':1,
        'Первая команда боеприпасов (1.Munitionsstaffel)':1,
        'Вторая команда боеприпасов (2.Munitionsstaffel)':1,
        }

#---
# Взводы:

metadict_army['Первая команда боеприпасов (1.Munitionsstaffel)'] = {
        'Группа управления первой команды боеприпасов':1,
        'Группа подвоза боеприпасов':4,
        }

metadict_army['Вторая команда боеприпасов (2.Munitionsstaffel)'] = {
        'Группа управления второй команды боеприпасов':1,
        'Группа подвоза боеприпасов с прицепом':4,
        }

metadict_army['Управление артиллерийской батареи (Gruppe Führer)'] = {
        'Командование артиллерийской батареи':1,
        'Группа управления батареи (Batterietrupp)':1,
        }

metadict_army['Команда связи (Nachrichtenstaffel)'] = {
        'Управление командой связи':1,
        'Моторизованное телефонное отделение (mittlerer Fernsprechtrupp b (mot.))':1,
        'Моторизованное отделение ранцевых радиостанций (Tornisterfunktrupp f (mot.))':1,
        }

metadict_army['Управление стрелковой роты (Gruppe Führer)'] = {
        'Отделение управления роты (Kompanietrupp)':1,
        'Противотанковое отделение (Panzerabwehrbüchsentrupp)':1,
        }

metadict_army['Управление мотоциклетной стрелковой роты (Gruppe Führer)'] = {
        'Отделение управления мотоциклетной роты (Kompanietrupp)':1,
        }

metadict_army['Управление моторизованной стрелковой роты (Gruppe Führer)'] = {
        'Отделение управления моторизованной роты (Kompanietrupp)':1,
        'Противотанковое отделение (Panzerabwehrbüchsentrupp)':1,
        'Расчёт 28-мм тяжёлого противотанкового ружья':1,
        }

metadict_army['Тыл стрелковой роты'] = {
        'Отделение обеспечения (Gefechtstroß)':1,
        'Отделение подвоза продовольствия (Verpflegungstroß)':1,
        'Тыловое вещевое отделение конное (Gepäcktroß)':1,
        }

metadict_army['Тыл мотоциклетной стрелковой роты'] = {
        'Отделение обеспечения мотоциклетной роты (Gefechtstroß)':1,
        'Тыловое вещевое отделение моторизованное (Gepäcktroß)':1,
        }

metadict_army['Тыл моторизованной стрелковой роты'] = {
        'Отделение обеспечения моторизованное (Gefechtstroß)':1,
        'Тыловое вещевое отделение моторизованное (Gepäcktroß)':1,
        }

metadict_army['Тыл моторизованной артиллерийской батареи'] = {
        'Отделение обеспечения артиллерийское (Gefechtstroß)':1,
        'Тыловое вещевое отделение моторизованное (Gepäcktroß)':1,
        }

metadict_army['Стрелковый взвод (Schützenzug)'] = {
        # https://rostislavddd.livejournal.com/279899.html
        'Управление стрелкового взвода':1,
        'Стрелковое отделение (Schützengruppe)':4,
        'Отделение лёгкого миномёта (leichter Granatwerfertrupp)':1,
        }

metadict_army['Моторизованный стрелковый взвод (Schützenzug)'] = {
        # https://rostislavddd.livejournal.com/280269.html
        'Управление моторизованного стрелкового взвода':1,
        'Стрелковое отделение (Schützengruppe)':4,
        'Отделение лёгкого миномёта (leichter Granatwerfertrupp)':1,
        'Автомобильное отделение':1,
        }

metadict_army['Мотоциклетный стрелковый взвод (Kraftradschützenzug)'] = {
        'Управление мотоциклетного стрелкового взвода':1,
        'Мотоциклетное стрелковое отделение (Kraftradschützengruppe)':3,
        'Отделение лёгкого миномёта мотоциклетное (leichter Granatwerfertrupp)':1,
        }

metadict_army['Мотоциклетный пулемётный взвод (s.M.G.Halbzug)'] = {
        'Управление мотоциклетного пулемётного взвода':1,
        'Мотоциклетное пулемётное отделение (s.M.G.Schützengruppe)':2,
        }

metadict_army['Противотанковый взвод (Ausführung A)'] = {
        'Управление противотанкового взвода':1,
        'Расчёт 37-мм противотанковой пушки (3,7cm Pak)':3,
        'Расчёт лёгкого пулемёта (M.G.Schützengruppe)':1,
        'Отделение лёгких артиллерийских тягачей':1,
        }

metadict_army['Танковый взвод средних танков'] = {
        'Управление танкового взвода средних танков (Panzerkampfwagen III)':1,
        'Экипаж среднего танка (Panzerkampfwagen III)':4,
        }

metadict_army['Танковый взвод огневой поддержки средних танков'] = {
        'Управление танкового взвода огневой поддержки средних танков (Panzerkampfwagen IV)':1,
        'Экипаж среднего танка (Panzerkampfwagen IV)':4,
        }

metadict_army['Управление боевой батареи'] = {
        'Командир боевой батареи (nachführender Offizier)':1,
        }

metadict_army['Орудийная команда 105-мм гаубиц (Geschützstaffel)'] = {
        'Управление орудийной команды':1,
        'Огневой взвод 105-мм гаубиц':2,
        'Моторизованное зенитное пулемётное отделение':1,
        }

metadict_army['Огневой взвод 105-мм гаубиц'] = {
        'Управление огневого взвода':1,
        'Расчёт лёгкой гаубицы моторизованный':2,
        }

#---
# Отделения:

metadict_army['Командование артиллерийской батареи'] = {
        'Командир артиллерийской батареи (Batterieführer)':1,
        'Водитель легкового автомобиля (Kraftwagenfahrer für gl.Pkw)':1,
        'Легковой автомобиль (Kfz.11)':1,
        }

metadict_army['Управление командой связи'] = {
        'Командир команды связи (Fernsprecher u.Funker)':1,
        'Водитель легкового автомобиля (Kraftwagenfahrer für gl.Pkw)':1,
        'Легковой автомобиль с радиостанцией (Kfz.2)':1,
        }

metadict_army['Моторизованное телефонное отделение (mittlerer Fernsprechtrupp b (mot.))'] = {
        'Командир телефонного отделения (Fernsprecher, Tr.Führ.)':1,
        'Телефонист (Fernsprecher)':6,
        'Водитель легкового автомобиля (Kraftwagenfahrer für gl.Pkw)':1,
        'Водитель грузовика (Kraftwagenfahrer für Lkw.)':1,
        'Легковой автомобиль (Kfz.15)':1,
        'Автомобиль наблюдения за телефонными линиями (Kfz.76)':1,
        }

metadict_army['Моторизованное отделение ранцевых радиостанций (Tornisterfunktrupp f (mot.))'] = {
        'Командир отделения ранцевых радиостанций (Funker (zugl.Tr.Führ.))':1,
        'Радист-водитель (Funker (zugl.Kw.Fahr.für gl.Pkw.))':1,
        'Радист (Funker)':1,
        'Легковой автомобиль с радиостанцией (Kfz.2)':1,
        }

metadict_army['Управление огневого взвода'] = {
        'Командир огневого взвода (Zugführer)':1,
        'Водитель легкового автомобиля (Kraftwagenfahrer für gl.Pkw)':1,
        'Канонир (Kanoniere (für Rechentrupp))':1,
        'Канонир-слесарь (Kanoniere (Bttr.Schlosser))':1,
        'Легковой автомобиль (Kfz.12)':1,
        }

metadict_army['Расчёт лёгкой гаубицы моторизованный'] = {
        'Командир расчёта лёгкой гаубицы (Geschützführer)':1,
        'Канонир (Kanoniere (für Rechentrupp))':6,
        'Водитель артиллерийского тягача (Kraftwagenbegleiter für Zgkw.)':2,
        'Полугусеничный артиллерийский тягач (Sd.Kfz.6/1)':1,
        '??? Прицеп (Anhänger (1achs) für leichte Lasten (Sd.Ah.3), nur bei le.F.H.16)':1,
        '105-мм лёгкая полевая гаубица (10,5 cm leFH 18)':1,
        }

metadict_army['Группа управления батареи (Batterietrupp)'] = {
        'Офицер артиллерийской разведки (Beobachtungsoffizier)':1,
        'Теодолист (für Richtkreise)':2,
        '??? (für Scherenfernrohr)':1,
        '??? (Rechentruppführer (zuglGasuffz.))':1,
        'Мотоциклист-посыльный (Kraftradfahrer als Melder)':3,
        'Водитель легкового автомобиля (Kraftwagenfahrer für gl.Pkw)':1,
        'Легковой автомобиль (Kfz.12)':1,
        }

metadict_army['Отделение управления роты (Kompanietrupp)'] = {
        'Командир стрелковой роты (Kompanieführer)':1,
        'Командир отделения управления (Führer des Kp.Tr.)':1,
        'Начальник транспорта роты (Führer der Gefechtsfahrzeuge der Kp.)':1,
        'Вещевой унтер-офицер (Gerätunteroffizier zugl.Wg.Begl.)':1,
        'Посыльный (Melder)':4,
        'Велосипедист (Radfahrer)':2,
        'Кучер-верховой (Fahrer vom Sattel)':2,
        'Конюх офицерской лошади (Pferdewärter für 1 Offz.Pfd)':1,
        'Четырёхконная повозка':1,
        }

metadict_army['Отделение управления моторизованной роты (Kompanietrupp)'] = {
        'Командир моторизованной стрелковой роты (Kompanieführer)':1,
        'Командир отделения управления (Führer des Kp.Tr.)':1,
        'Начальник транспорта роты (Führer der Gefechtsfahrzeuge der Kp.)':1,
        'Вещевой унтер-офицер (Gerätunteroffizier zugl.Wg.Begl.)':1,
        'Посыльный (Melder)':4,
        'Мотоциклист-посыльный (Kraftradfahrer als Melder)':5,
        'Водитель грузовика (Kraftwagenfahrer für Lkw.)':4,
        '3-тонный грузовой автомобиль (Lkw. (3t))':4,
        'Легковой автомобиль (Kfz.15)':1,
        }

metadict_army['Отделение управления мотоциклетной роты (Kompanietrupp)'] = {
        'Командир мотоциклетной роты (Kompanieführer)':1,
        'Командир отделения управления (Führer des Kp.Tr.)':1,
        '??? (Führer der Kraftfahrzeugstaffel)':1,
        '??? (Scherenfernrohrträger)':1,
        'Посыльный (Melder)':2,
        'Носильщик раненых (Krankenträger)':1,
        'Мотоциклист-посыльный (Kraftradfahrer als Melder)':3,
        'Водитель легкового автомобиля (Kraftwagenfahrer für gl.Pkw)':2,
        'Легковой автомобиль (Kfz.11)':1,
        'Легковой автомобиль (Kfz.18)':1,
        }

metadict_army['Отделение обеспечения (Gefechtstroß)'] = {
        'Старшина роты (Hauptfeldwebel)':1,
        'Командир отделения обеспечения (Führer des Gefechtstrosses)':1,
        'Писарь (Schreiber)':1,
        'Помощник оружейного мастера (Waffenmeistergehilfe)':1,
        'Группа полевой кухни':1,
        'Обоз стрелковой роты':1,
        'Санитарная группа':1,
        }

metadict_army['Отделение обеспечения моторизованное (Gefechtstroß)'] = {
        'Старшина роты (Hauptfeldwebel)':1,
        'Командир отделения обеспечения (Führer des Gefechtstrosses)':1,
        'Писарь (Schreiber)':1,
        'Помощник оружейного мастера (Waffenmeistergehilfe)':1,
        'Водитель грузовика (Kraftwagenfahrer für Lkw.)':2,
        'Легковой автомобиль (leichter Pkw.)':1,
        'Группа обеспечения топливом':1,
        'Группа ремонта автомобилей':1,
        'Санитарная группа':1,
        }

metadict_army['Отделение обеспечения артиллерийское (Gefechtstroß)'] = {
        'Командир отделения обеспечения (Führer auf le.Krad)':1,
        'Старший механик (Schirrmeister)':1,
        'Слесарь-моторист (Motorenschlosser)':2,
        'Помощник оружейного мастера (Waffenmeistergehilfe)':1,
        'Повар (Köche)':2,
        'Водитель грузовика (Kraftwagenfahrer für Lkw.)':3,
        'Водитель артиллерийского тягача (Kraftwagenbegleiter für Zgkw.)':1,
        'Полугусеничный артиллерийский тягач (Sd.Kfz.6/1)':1,
        'Грузовой автомобиль (leichter gl.Lkw.)':2,
        'Грузовой автомобиль (Hf.11)':1,
        }

metadict_army['Отделение обеспечения мотоциклетной роты (Gefechtstroß)'] = {
        'Старшина роты (Oberfeldwebel)':1,
        'Старший механик (Schirrmeister)':1,
        'Специалист-оружейник (Waffenunteroffizier)':1,
        'Вещевой унтер-офицер (Gerätunteroffizier zugl.Wg.Begl.)':1,
        'Специалист по обслуживанию автомобилей (für den Kraftfahrdienst)':1,
        'Санитар (Sanitätsunteroffizier)':1,
        'Помощник оружейного мастера (Waffenmeistergehilfe)':1,
        'Водитель легкового автомобиля (Kraftwagenfahrer für gl.Pkw)':1,
        'Водитель грузовика (Kraftwagenfahrer für Lkw.)':5,
        'Писарь (Schreiber)':1,
        'Слесарь-моторист (Motorenschlosser)':1,
        'Повар (Köche)':2,
        'Легковой автомобиль (Kfz.15)':1,
        '3-тонный грузовой автомобиль (Lkw. (3t))':5,
        }

metadict_army['Тыловое вещевое отделение моторизованное (Gepäcktroß)'] = {
        'Командир отделения обеспечения (Rechnungsführer)':1,
        'Писарь (Schreiber)':1,
        'Портной (Schneider)':1,
        'Сапожник (Schuhmacher)':1,
        'Водитель грузовика (Kraftwagenfahrer für Lkw.)':1,
        '3-тонный грузовой автомобиль (Lkw. (3t))':1,
        }

metadict_army['Отделение подвоза продовольствия (Verpflegungstroß)'] = {
        'Ответственный за довольствие (Verpflegungsmann)':1,
        'Кучер (Fahrer vom Bock)':1,
        'Лошадь обозная':2,
        'Двуконная повозка':1,
        }

metadict_army['Тыловое вещевое отделение конное (Gepäcktroß)'] = {
        'Командир отделения обеспечения (Rechnungsführer)':1,
        'Портной (Schneider)':1,
        'Сапожник (Schuhmacher)':1,
        'Кучер (Fahrer vom Bock)':2,
        'Лошадь обозная':4,
        'Двуконная повозка':2,
        }

metadict_army['Управление стрелкового взвода'] = {
        'Группа управления взвода (Zugtrupp)':1,
        'Обоз стрелкового взвода':1,
        }

metadict_army['Управление моторизованного стрелкового взвода'] = {
        'Группа управления моторизованного взвода (Zugtrupp)':1,
        'Лёгкий пулемёт (MG.34) (запасной)':2,
        }

metadict_army['Управление мотоциклетного стрелкового взвода'] = {
        'Группа управления мотоциклетного взвода (Zugtrupp)':1,
        }

metadict_army['Управление мотоциклетного пулемётного взвода'] = {
        'Группа управления мотоциклетного пулемётного взвода (Halbzugtrupp)':1,
        }

metadict_army['Управление противотанкового взвода'] = {
        'Группа управления противотанкового взвода (Zugtrupp)':1,
        }

metadict_army['Управление танкового взвода средних танков (Panzerkampfwagen III)'] = {
        'Экипаж командирского среднего танка (Panzerkampfwagen III)':1,
        }

metadict_army['Управление танкового взвода огневой поддержки средних танков (Panzerkampfwagen IV)'] = {
        'Экипаж командирского среднего танка (Panzerkampfwagen IV)':1,
        }

metadict_army['Мотоциклетное стрелковое отделение (Kraftradschützengruppe)'] = {
        # Ружейных гранатометов - 1  (? возможно отсутствие)
        'Огневая группа мотоциклетного отделения':1,
        'Маневровая группа мотоциклетного отделения':1,
        'Мотоциклетная группа':1,
        }

metadict_army['Мотоциклетное пулемётное отделение (s.M.G.Schützengruppe)'] = {
        'Расчёт станкового пулемёта мотоциклетный':1,
        'Мотоциклетная группа станкового пулемёта':1,
        }

metadict_army['Стрелковое отделение (Schützengruppe)'] = {
        'Огневая группа':1,
        'Маневровая группа':1,
        }

metadict_army['Отделение лёгкого миномёта (leichter Granatwerfertrupp)'] = {
        'Командир миномётного расчёта (Truppführer)':1,
        'Миномётчик (Granatwerferschützen)':2,
        'Лёгкий миномёт (Granatenwerfer 36)':1,
        }

metadict_army['Отделение лёгкого миномёта мотоциклетное (leichter Granatwerfertrupp)'] = {
        'Командир миномётного расчёта (Truppführer)':1,
        'Миномётчик (Granatwerferschützen)':2,
        'Мотоциклист (Kraftradfahrer (s.Krad mit Beiwg.))':2,
        'Лёгкий миномёт (Granatenwerfer 36)':1,
        }

metadict_army['Противотанковое отделение (Panzerabwehrbüchsentrupp)'] = {
        'Командир противотанкового отделения (Obergefreiter)':1,
        'Стрелок противотанкового ружья (Schützen für Panzerabwehrbüchsen)':3,
        'Помощник стрелка противотанкового ружья (Schützen für Munition)':3,
        }

metadict_army['Автомобильное отделение'] = {
        'Водитель грузовика (Kraftwagenfahrer für Lkw.)':4,
        '3-тонный грузовой автомобиль (Lkw. (3t))':4,
        }

metadict_army['Отделение лёгких артиллерийских тягачей'] = {
        'Водитель легкового автомобиля (Kraftwagenfahrer für gl.Pkw)':7,
        'Легковой автомобиль (Kfz.12)':7,
        'Прицеп с боеприпасами (Sd.Ah.32)':3,
        }

metadict_army['Экипаж командирского среднего танка (Panzerkampfwagen IV)'] = {
        'Командир танкового взвода (zugl. Panzerführer)':1,
        'Радист танка (Funker z.b.V)':1,
        'Наводчик (Panzerschützen)':1,
        'Заряжающий (Panzerschützen)':1,
        'Водитель танка (Kraftwagenfahrer für gp.Kw)':1,
        'Командирский средний танк (Panzerkampfwagen IV)':1,
        }

metadict_army['Экипаж среднего танка (Panzerkampfwagen IV)'] = {
        'Командир танка (Panzerführer)':1,
        'Радист танка (Funker z.b.V)':1,
        'Наводчик (Panzerschützen)':1,
        'Заряжающий (Panzerschützen)':1,
        'Водитель танка (Kraftwagenfahrer für gp.Kw)':1,
        'Средний танк (Panzerkampfwagen IV)':1,
        }

metadict_army['Экипаж командирского среднего танка (Panzerkampfwagen III)'] = {
        'Командир танкового взвода (zugl. Panzerführer)':1,
        'Радист танка (Funker z.b.V)':1,
        'Наводчик (Panzerschützen)':1,
        'Заряжающий (Panzerschützen)':1,
        'Водитель танка (Kraftwagenfahrer für gp.Kw)':1,
        'Командирский средний танк (Panzerkampfwagen III)':1,
        }

metadict_army['Экипаж среднего танка (Panzerkampfwagen III)'] = {
        'Командир танка (Panzerführer)':1,
        'Радист танка (Funker z.b.V)':1,
        'Наводчик (Panzerschützen)':1,
        'Заряжающий (Panzerschützen)':1,
        'Водитель танка (Kraftwagenfahrer für gp.Kw)':1,
        'Средний танк (Panzerkampfwagen III)':1,
        }

metadict_army['Управление орудийной команды'] = {
        'Командир орудийной команды (Oberwachtmeister)':1,
        'Санитар (Sanitätsunteroffizier)':1,
        'Мотоциклист-посыльный (Kraftradfahrer als Melder)':1,
        'Водитель легкового автомобиля (Kraftwagenfahrer für gl.Pkw)':1,
        'Легковой автомобиль (Kfz.1)':1,
        }

metadict_army['Моторизованное зенитное пулемётное отделение'] = {
        'Командир зенитного отделения (le.M.G.Schützen (zugl.Führ. der M.G.))':1,
        'Пулемётчик с зенитным пулемётом (le.M.G.Schützen)':1,
        'Водитель легкового автомобиля (Kraftwagenfahrer für gl.Pkw)':1,
        'Легковой автомобиль с зенитным станком (Kfz.4)':1,
        }

#---
# Группы:

metadict_army['Группа управления первой команды боеприпасов'] = {
        'Командир команды боепипасов (Staffelführer im Beiwagen)':1,
        'Заместитель командира команды боепипасов (Uffz.auf le.Krad)':1,
        'Мотоциклист (Kraftradfahrer (s.Krad mit Beiwg.))':2,
        }

metadict_army['Группа управления второй команды боеприпасов'] = {
        'Командир команды боепипасов (Staffelführer auf le.Krad)':1,
        }

metadict_army['Группа подвоза боеприпасов'] = {
        'Подносчик боеприпасов (Munitionskanoniere)':3,
        'Водитель грузовика (Kraftwagenfahrer für Lkw.)':1,
        'Грузовой автомобиль для боеприпасов (leichter gl.Lkw.)':1,
        }

metadict_army['Группа подвоза боеприпасов с прицепом'] = {
        'Подносчик боеприпасов (Munitionskanoniere)':3,
        'Водитель грузовика (Kraftwagenfahrer für Lkw.)':1,
        'Грузовой автомобиль для боеприпасов (leichter gl.Lkw.)':1,
        'Прицеп для боеприпасов (Anhänger (mehrachs.) für Munition)':1,
        }

metadict_army['Группа управления взвода (Zugtrupp)'] = {
        'Командир стрелкового взвода (Zugführer)':1,
        'Заместитель командира стрелкового взвода (Führer des Zugtrupps)':1,
        'Посыльный (Melder)':1,
        'Посыльный-горнист (Melder zugl.Hornist)':1,
        'Посыльный-светосигнальщик (Melder zugl.für Blinkdienst)':1,
        }

metadict_army['Группа управления моторизованного взвода (Zugtrupp)'] = {
        'Командир стрелкового взвода (Zugführer)':1,
        'Заместитель командира стрелкового взвода (Führer des Zugtrupps)':1,
        'Посыльный (Melder)':1,
        'Посыльный-горнист (Melder zugl.Hornist)':1,
        'Посыльный-светосигнальщик (Melder zugl.für Blinkdienst)':1,
        'Мотоциклист-посыльный (Kraftradfahrer als Melder)':1,
        'Носильщик раненых (Krankenträger)':1,
        }

metadict_army['Группа управления мотоциклетного взвода (Zugtrupp)'] = {
        # https://rostislavddd.livejournal.com/280269.html
        # За состоящим из этих семи человек управлением взвода, закреплено легкое противотанковое ружье.
        'Командир мотоциклетного взвода (Zugführer)':1,
        'Посыльный (Melder)':1,
        'Мотоциклист-посыльный (Kraftradfahrer als Melder)':2,
        'Водитель легкового автомобиля (Kraftwagenfahrer für gl.Pkw)':2,
        'Носильщик раненых (Krankenträger)':1,
        'Легковой автомобиль (Kfz.11)':1,
        'Легковой автомобиль (Kfz.18)':1,
        }

metadict_army['Группа управления мотоциклетного пулемётного взвода (Halbzugtrupp)'] = {
        'Командир мотоциклетного пулемётного взвода (Halbzugführer)':1,
        'Посыльный (Melder)':1,
        'Мотоциклист-посыльный (Kraftradfahrer als Melder)':2,
        'Дальномерщик (Entfernungsmessmann)':1,
        }

metadict_army['Группа управления противотанкового взвода (Zugtrupp)'] = {
        'Командир противотанкового взвода (Zugführer)':1,
        'Артиллерийский корректировщик (Beobachtungsunteroffizier)':1,
        '??? (Führer der Kraftfahrzeugstaffel)':1,
        'Дальномерщик (Entfernungsmessmann)':1,
        'Мотоциклист (Kraftradfahrer (s.Krad mit Beiwg.))':3,
        'Водитель легкового автомобиля (Kraftwagenfahrer für gl.Pkw)':1,
        'Легковой автомобиль (Kfz.12)':1,
        }

metadict_army['Обоз стрелкового взвода'] = {
        'Конюх (Pferdewärter)':1,
        'Лошадь обозная':1,
        'Конная одноосная повозка':1,
        'Ручная тележка':1,
        }

metadict_army['Обоз стрелковой роты'] = {
        'Кучер (Fahrer vom Bock)':2,
        'Лошадь обозная':4,
        'Двуконная повозка':2,
        }

metadict_army['Санитарная группа'] = {
        'Санитар (Sanitätsunteroffizier)':1,
        'Носильщик раненых (Krankenträger)':4,
        }

metadict_army['Группа полевой кухни'] = {
        'Повар (Köche)':2,
        'Стрелок-верховой (Schütze zugl.Wg.Begl. für Gef.Wg)':2,
        'Кучер-верховой (Fahrer vom Sattel)':2,
        'Лошадь верховая':2,
        'Лошадь обозная':2,
        'Полевая кухня':1,
        }

metadict_army['Группа полевой кухни моторизованная'] = {
        'Старший повар (Feldkochunteroffizier)':1,
        'Повар (Feldkoch)':1,
        'Водитель грузовика (Kraftwagenfahrer für Lkw.)':1,
        '3-тонный грузовой автомобиль (Lkw. (3t))':1,
        }

metadict_army['Группа обеспечения топливом'] = {
        # https://de.wikipedia.org/wiki/Betriebsstoff
        'Водитель грузовика (Kraftwagenfahrer für Lkw.)':1,
        '1.5-тонный грузовой автомобиль (leichter Lkw. (1 1/2t))':1,
        }

metadict_army['Группа ремонта автомобилей'] = {
        # https://de.wikipedia.org/wiki/Instandsetzungsdienst
        # https://de.wikipedia.org/wiki/Schirrmeister
        'Старший механик (Schirrmeister)':1,
        'Слесарь-моторист (Motorenschlosser)':1,
        'Водитель грузовика (Kraftwagenfahrer für Lkw.)':1,
        'Мотоциклист-посыльный (Kraftradfahrer als Melder)':1,
        'Легковой автомобиль (Kfz.2/40)':1,
        }

metadict_army['Огневая группа'] = {
        'Командир стрелкового отделения (Gruppenführer)':1,
        'Пулемётчик лёгкого пулемёта (l.M.G.Oberschütze)':1,
        'Первый помощник пулемётчика (M.G.Schütze)':1,
        'Второй помощник пулемётчика (Gefreiter)':1,
        }

metadict_army['Огневая группа мотоциклетного отделения'] = {
        'Командир стрелкового отделения (Gruppenführer)':1,
        'Пулемётчик лёгкого пулемёта (l.M.G.Oberschütze)':1,
        'Первый помощник пулемётчика (M.G.Schütze)':1,
        }

metadict_army['Маневровая группа'] = {
        'Старший стрелок (Unteroffiziere ohne Portpeе)':1,
        'Стрелок (Schütze)':5,
        }

metadict_army['Маневровая группа мотоциклетного отделения'] = {
        'Старший стрелок (Unteroffiziere ohne Portpeе)':1,
        'Стрелок (Schütze)':2,
        }

metadict_army['Мотоциклетная группа'] = {
        # Мотоциклы с колясками.
        'Мотоциклист (Kraftradfahrer (s.Krad mit Beiwg.))':3,
        }

metadict_army['Мотоциклетная группа станкового пулемёта'] = {
        'Мотоциклист (Kraftradfahrer (s.Krad mit Beiwg.))':4,
        }

metadict_army['Расчёт лёгкого пулемёта (M.G.Schützengruppe)'] = {
        'Командир пулемётного отделения (M.G.Führer)':1,
        'Пулемётчик лёгкого пулемёта (l.M.G.Oberschütze)':1,
        'Первый помощник пулемётчика (M.G.Schütze)':1,
        }

metadict_army['Расчёт станкового пулемёта мотоциклетный'] = {
        'Командир пулемётного отделения (M.G.Führer)':1,
        'Пулемётчик станкового пулемёта (s.M.G.Oberschütze)':1,
        'Первый помощник пулемётчика (M.G.Schütze)':1,
        'Второй помощник пулемётчика (Gefreiter)':3,
        }

metadict_army['Расчёт 28-мм тяжёлого противотанкового ружья'] = {
        # https://ru.wikipedia.org/wiki/Тяжёлое_противотанковое_ружьё_2,8_см_PzB_41
        # https://de.wikipedia.org/wiki/2,8-cm-schwere_Panzerbüchse_41
        'Стрелок тяжёлого противотанкового ружья':1,
        'Помощник стрелка противотанкового ружья (Schützen für Munition)':3,
        '28-мм тяжёлое противотанковое ружьё (2,8 cm schwere Panzerbüchse 41)':1,
        }

metadict_army['Расчёт 37-мм противотанковой пушки (3,7cm Pak)'] = {
        # https://ru.wikipedia.org/wiki/Тяжёлое_противотанковое_ружьё_2,8_см_PzB_41
        # https://de.wikipedia.org/wiki/2,8-cm-schwere_Panzerbüchse_41
        'Командир противотанкового расчёта':1,
        'Канонир (Kanoniere)':2,
        'Канонир-стрелок':2,
        '37-мм противотанковая пушка (РАК.36)':1,
        }

#---
# Бойцы

metadict_detail['Командир стрелковой роты (Kompanieführer)'] = {
        '-Офицеры':1,
        'Пистолет (P.08)':1,
        'Лошадь верховая':1,
        }

metadict_detail['Командир моторизованной стрелковой роты (Kompanieführer)'] = {
        '-Офицеры':1,
        'Пистолет (P.08)':1,
        }

metadict_detail['Командир мотоциклетной роты (Kompanieführer)'] = {
        '-Офицеры':1,
        'Пистолет (P.08)':1,
        }

metadict_detail['Командир стрелкового взвода (Zugführer)'] = {
        '-Офицеры':1,
        'Пистолет (P.08)':1,
        'Пистолет-пулемёт (MP.40)':1,
        'Сигнальная ракетница':1,
        }

metadict_detail['Командир мотоциклетного взвода (Zugführer)'] = {
        '-Офицеры':1,
        'Пистолет (P.08)':1,
        }

metadict_detail['Командир мотоциклетного пулемётного взвода (Halbzugführer)'] = {
        '-Офицеры':1,
        'Пистолет (P.08)':1,
        }

metadict_detail['Заместитель командира стрелкового взвода (Führer des Zugtrupps)'] = {
        '-Унтер-офицеры':1,
        'Пистолет (P.08)':1,
        }

metadict_detail['Командир миномётного расчёта (Truppführer)'] = {
        '-Унтер-офицеры':1,
        'Винтовка (Karabiner 98k)':1,
        }

metadict_detail['Миномётчик (Granatwerferschützen)'] = {
        '-Рядовые':1,
        'Пистолет (P.08)':1,
        }

metadict_detail['Командир пулемётного отделения (M.G.Führer)'] = {
        '-Унтер-офицеры':1,
        'Винтовка (Karabiner 98k)':1,
        }

metadict_detail['Командир стрелкового отделения (Gruppenführer)'] = {
        '-Унтер-офицеры':1,
        'Пистолет-пулемёт (MP.40)':1,
        'Ручная граната (Stielhandgranaten 24)':4,
        #'Короб на 50 патронов 7.92x57 (Gurttrommel 34)':2,
        }

metadict_detail['Старший стрелок (Unteroffiziere ohne Portpeе)'] = {
        '-Рядовые':1,
        'Винтовка (Karabiner 98k)':1,
        'Ручная граната (Stielhandgranaten 24)':4,
        #'Короб на 50 патронов 7.92x57 (Gurttrommel 34)':2,
        }

metadict_detail['Стрелок (Schütze)'] = {
        '-Рядовые':1,
        'Винтовка (Karabiner 98k)':1,
        'Ручная граната (Stielhandgranaten 24)':4,
        #'Короб на 50 патронов 7.92x57 (Gurttrommel 34)':2,
        }

metadict_detail['Пулемётчик лёгкого пулемёта (l.M.G.Oberschütze)'] = {
        # http://orrelrkka.clan.su/forum/8-1044-1
        '-Рядовые':1,
        'Пистолет (P.08)':1,
        'Лёгкий пулемёт (MG.34)':1,
        'Короб на 50 патронов 7.92x57 (Gurttrommel 34)':4,
        }

metadict_detail['Пулемётчик станкового пулемёта (s.M.G.Oberschütze)'] = {
        '-Рядовые':1,
        'Пистолет (P.08)':1,
        'Станковый пулемёт (MG.34)':1,
        'Короб на 50 патронов 7.92x57 (Gurttrommel 34)':4,
        }

metadict_detail['Первый помощник пулемётчика (M.G.Schütze)'] = {
        # Узнать, сколько весит ЗИП пулемёта:
        '-Рядовые':1,
        'Пистолет (P.08)':1,
        'Короб на 50 патронов 7.92x57 (Gurttrommel 34)':4,
        'Короб на 300 патронов 7.92x57 (Patronenkasten 34/41)':1,
        'ЗИП пулемёта MG.34':1,
        }

metadict_detail['Второй помощник пулемётчика (Gefreiter)'] = {
        '-Рядовые':1,
        'Винтовка (Karabiner 98k)':1,
        'Короб на 300 патронов 7.92x57 (Patronenkasten 34/41)':2,
        }

metadict_detail['Стрелок противотанкового ружья (Schützen für Panzerabwehrbüchsen)'] = {
        '-Рядовые':1,
        'Пистолет (P.08)':1,
        'Противотанковое ружьё (Panzerbüchse 39)':1,
        }

metadict_detail['Стрелок тяжёлого противотанкового ружья'] = {
        '-Рядовые':1,
        'Пистолет (P.08)':1,
        }

metadict_detail['Помощник стрелка противотанкового ружья (Schützen für Munition)'] = {
        '-Рядовые':1,
        'Винтовка (Karabiner 98k)':1,
        }

metadict_detail['Посыльный (Melder)'] = {
        '-Рядовые':1,
        'Винтовка (Karabiner 98k)':1,
        }

metadict_detail['Посыльный-горнист (Melder zugl.Hornist)'] = {
        '-Рядовые':1,
        'Винтовка (Karabiner 98k)':1,
        }

metadict_detail['Посыльный-светосигнальщик (Melder zugl.für Blinkdienst)'] = {
        '-Рядовые':1,
        'Винтовка (Karabiner 98k)':1,
        }

metadict_detail['Конюх (Pferdewärter)'] = {
        '-Рядовые':1,
        'Винтовка (Karabiner 98k)':1,
        }

metadict_detail['Велосипедист (Radfahrer)'] = {
        '-Рядовые':1,
        'Винтовка (Karabiner 98k)':1,
        #'Велосипед':1,
        }

metadict_detail['Вещевой унтер-офицер (Gerätunteroffizier zugl.Wg.Begl.)'] = {
        '-Унтер-офицеры':1,
        'Винтовка (Karabiner 98k)':1,
        }

metadict_detail['Командир отделения обеспечения (Führer des Gefechtstrosses)'] = {
        '-Унтер-офицеры':1,
        'Винтовка (Karabiner 98k)':1,
        #'Велосипед':1,
        }

metadict_detail['Ответственный за довольствие (Verpflegungsmann)'] = {
        '-Рядовые':1,
        'Винтовка (Karabiner 98k)':1,
        }

metadict_detail['Командир отделения обеспечения (Rechnungsführer)'] = {
        '-Унтер-офицеры':1,
        'Винтовка (Karabiner 98k)':1,
        #'Велосипед':1,
        }

metadict_detail['Командир отделения управления (Führer des Kp.Tr.)'] = {
        '-Унтер-офицеры':1,
        'Винтовка (Karabiner 98k)':1,
        }

metadict_detail['Командир противотанкового отделения (Obergefreiter)'] = {
        '-Унтер-офицеры':1,
        'Винтовка (Karabiner 98k)':1,
        }

metadict_detail['Конюх офицерской лошади (Pferdewärter für 1 Offz.Pfd)'] = {
        '-Рядовые':1,
        'Винтовка (Karabiner 98k)':1,
        #'Велосипед':1,
        }

metadict_detail['Кучер (Fahrer vom Bock)'] = {
        '-Рядовые':1,
        'Винтовка (Karabiner 98k)':1,
        }

metadict_detail['Кучер-верховой (Fahrer vom Sattel)'] = {
        '-Рядовые':1,
        'Винтовка (Karabiner 98k)':1,
        }

metadict_detail['Начальник транспорта роты (Führer der Gefechtsfahrzeuge der Kp.)'] = {
        '-Унтер-офицеры':1,
        'Винтовка (Karabiner 98k)':1,
        #'Велосипед':1,
        }

metadict_detail['Носильщик раненых (Krankenträger)'] = {
        '-Рядовые':1,
        'Винтовка (Karabiner 98k)':1,
        }

metadict_detail['Писарь (Schreiber)'] = {
        '-Рядовые':1,
        'Винтовка (Karabiner 98k)':1,
        #'Велосипед':1,
        }

metadict_detail['Повар (Köche)'] = {
        '-Рядовые':1,
        'Винтовка (Karabiner 98k)':1,
        }

metadict_detail['Помощник оружейного мастера (Waffenmeistergehilfe)'] = {
        '-Рядовые':1,
        'Винтовка (Karabiner 98k)':1,
        }

metadict_detail['Портной (Schneider)'] = {
        '-Рядовые':1,
        'Винтовка (Karabiner 98k)':1,
        }

metadict_detail['Санитар (Sanitätsunteroffizier)'] = {
        '-Рядовые':1,
        'Винтовка (Karabiner 98k)':1,
        #'Велосипед':1,
        }

metadict_detail['Сапожник (Schuhmacher)'] = {
        '-Рядовые':1,
        'Винтовка (Karabiner 98k)':1,
        }

metadict_detail['Старшина роты (Hauptfeldwebel)'] = {
        '-Унтер-офицеры':1,
        'Винтовка (Karabiner 98k)':1,
        }

metadict_detail['Стрелок-верховой (Schütze zugl.Wg.Begl. für Gef.Wg)'] = {
        '-Рядовые':1,
        'Винтовка (Karabiner 98k)':1,
        }

metadict_detail['Мотоциклист-посыльный (Kraftradfahrer als Melder)'] = {
        '-Рядовые':1,
        'Винтовка (Karabiner 98k)':1,
        'Мотоцикл':1,
        }

metadict_detail['Мотоциклист (Kraftradfahrer (s.Krad mit Beiwg.))'] = {
        '-Рядовые':1,
        'Винтовка (Karabiner 98k)':1,
        'Мотоцикл с коляской':1,
        }

metadict_detail['Водитель грузовика (Kraftwagenfahrer für Lkw.)'] = {
        '-Рядовые':1,
        'Винтовка (Karabiner 98k)':1,
        }

metadict_detail['Водитель легкового автомобиля (Kraftwagenfahrer für gl.Pkw)'] = {
        '-Рядовые':1,
        'Винтовка (Karabiner 98k)':1,
        }

metadict_detail['Старший механик (Schirrmeister)'] = {
        '-Рядовые':1,
        'Пистолет (P.08)':1,
        }

metadict_detail['Слесарь-моторист (Motorenschlosser)'] = {
        '-Рядовые':1,
        'Винтовка (Karabiner 98k)':1,
        }

metadict_detail['Дальномерщик (Entfernungsmessmann)'] = {
        '-Рядовые':1,
        'Винтовка (Karabiner 98k)':1,
        }

#metadict_detail['??? (Führer der Kraftfahrzeugstaffel)'] = {
#        '-Унтер-офицер':1,
#        'Винтовка (Karabiner 98k)':1,
#        }
#
#metadict_detail['??? (Scherenfernrohrträger)'] = {
#        '-Рядовые':1,
#        'Винтовка (Karabiner 98k)':1,
#        }

metadict_detail['Специалист по обслуживанию автомобилей (für den Kraftfahrdienst)'] = {
        '-Унтер-офицеры':1,
        'Винтовка (Karabiner 98k)':1,
        }

metadict_detail['Специалист-оружейник (Waffenunteroffizier)'] = {
        '-Унтер-офицеры':1,
        'Пистолет (P.08)':1,
        }

metadict_detail['Старшина роты (Oberfeldwebel)'] = {
        '-Унтер-офицеры':1,
        'Винтовка (Karabiner 98k)':1,
        }

metadict_detail['Артиллерийский корректировщик (Beobachtungsunteroffizier)'] = {
        '-Унтер-офицеры':1,
        'Пистолет (P.08)':1,
        }

metadict_detail['Канонир (Kanoniere)'] = {
        '-Рядовые':1,
        'Пистолет (P.08)':1,
        }

metadict_detail['Канонир-стрелок'] = {
        '-Рядовые':1,
        'Винтовка (Karabiner 98k)':1,
        }

metadict_detail['Командир противотанкового взвода (Zugführer)'] = {
        '-Офицеры':1,
        'Пистолет (P.08)':1,
        }

metadict_detail['Командир противотанкового расчёта'] = {
        '-Унтер-офицеры':1,
        'Пистолет (P.08)':1,
        }


metadict_detail['Командир танкового взвода (zugl. Panzerführer)'] = {
        '-Офицеры':1,
        'Пистолет (P.08)':1,
        }

metadict_detail['Командир танка (Panzerführer)'] = {
        '-Унтер-офицеры':1,
        'Пистолет (P.08)':1,
        }

metadict_detail['Водитель танка (Kraftwagenfahrer für gp.Kw)'] = {
        '-Унтер-офицеры':1,
        'Пистолет (P.08)':1,
        }

metadict_detail['Заряжающий (Panzerschützen)'] = {
        '-Рядовые':1,
        'Пистолет (P.08)':1,
        }

metadict_detail['Наводчик (Panzerschützen)'] = {
        '-Рядовые':1,
        'Пистолет (P.08)':1,
        }

metadict_detail['Радист танка (Funker z.b.V)'] = {
        '-Рядовые':1,
        'Пистолет (P.08)':1,
        }




metadict_detail['Водитель артиллерийского тягача (Kraftwagenbegleiter für Zgkw.)'] = {
        '-Рядовые':1,
        'Винтовка (Karabiner 98k)':1,
        }

metadict_detail['Заместитель командира команды боепипасов (Uffz.auf le.Krad)'] = {
        '-Унтер-офицеры':1,
        'Винтовка (Karabiner 98k)':1,
        }

metadict_detail['Канонир (Kanoniere (für Rechentrupp))'] = {
        '-Рядовые':1,
        'Винтовка (Karabiner 98k)':1,
        }

metadict_detail['Канонир-слесарь (Kanoniere (Bttr.Schlosser))'] = {
        '-Рядовые':1,
        'Пистолет (P.08)':1,
        }

metadict_detail['Командир артиллерийской батареи (Batterieführer)'] = {
        '-Офицеры':1,
        'Пистолет (P.08)':1,
        }

metadict_detail['Командир боевой батареи (nachführender Offizier)'] = {
        '-Офицеры':1,
        'Пистолет (P.08)':1,
        }

metadict_detail['Командир зенитного отделения (le.M.G.Schützen (zugl.Führ. der M.G.))'] = {
        '-Рядовые':1,
        'Пистолет (P.08)':1,
        }

metadict_detail['Командир команды боепипасов (Staffelführer auf le.Krad)'] = {
        '-Унтер-офицеры':1,
        'Пистолет (P.08)':1,
        }

metadict_detail['Командир команды боепипасов (Staffelführer im Beiwagen)'] = {
        '-Унтер-офицеры':1,
        'Винтовка (Karabiner 98k)':1,
        }

metadict_detail['Командир команды связи (Fernsprecher u.Funker)'] = {
        '-Унтер-офицеры':1,
        'Пистолет (P.08)':1,
        }

metadict_detail['Командир огневого взвода (Zugführer)'] = {
        '-Унтер-офицеры':1,
        'Пистолет (P.08)':1,
        }

metadict_detail['Командир орудийной команды (Oberwachtmeister)'] = {
        '-Унтер-офицеры':1,
        'Пистолет (P.08)':1,
        }

metadict_detail['Командир отделения обеспечения (Führer auf le.Krad)'] = {
        '-Унтер-офицеры':1,
        'Винтовка (Karabiner 98k)':1,
        }

metadict_detail['Командир отделения ранцевых радиостанций (Funker (zugl.Tr.Führ.))'] = {
        '-Рядовые':1,
        'Винтовка (Karabiner 98k)':1,
        }

metadict_detail['Командир расчёта лёгкой гаубицы (Geschützführer)'] = {
        '-Унтер-офицеры':1,
        'Пистолет (P.08)':1,
        }

metadict_detail['Командир телефонного отделения (Fernsprecher, Tr.Führ.)'] = {
        '-Унтер-офицеры':1,
        'Винтовка (Karabiner 98k)':1,
        }

metadict_detail['Офицер артиллерийской разведки (Beobachtungsoffizier)'] = {
        '-Офицеры':1,
        'Пистолет (P.08)':1,
        }

metadict_detail['Подносчик боеприпасов (Munitionskanoniere)'] = {
        '-Рядовые':1,
        'Винтовка (Karabiner 98k)':1,
        }

metadict_detail['Пулемётчик с зенитным пулемётом (le.M.G.Schützen)'] = {
        '-Рядовые':1,
        'Пистолет (P.08)':1,
        'Зенитный пулемёт (MG.34)':1,
        }

metadict_detail['Радист (Funker)'] = {
        '-Рядовые':1,
        'Винтовка (Karabiner 98k)':1,
        }

metadict_detail['Радист-водитель (Funker (zugl.Kw.Fahr.für gl.Pkw.))'] = {
        '-Рядовые':1,
        'Винтовка (Karabiner 98k)':1,
        }

metadict_detail['Телефонист (Fernsprecher)'] = {
        '-Рядовые':1,
        'Винтовка (Karabiner 98k)':1,
        }

metadict_detail['Теодолист (für Richtkreise)'] = {
        '-Рядовые':1,
        'Винтовка (Karabiner 98k)':1,
        }

#---
# Бронетехника

metadict_detail['Средний танк (Panzerkampfwagen IV)'] = {
        '75-мм танковая пушка (7,5 cm KwK 40)':1,
        'Танковый пулемёт (MG.34)':2,
        '-Допустимая масса техники (тонн)':25,
        }

metadict_detail['Командирский средний танк (Panzerkampfwagen IV)'] = {
        '75-мм танковая пушка (7,5 cm KwK 40)':1,
        'Танковый пулемёт (MG.34)':2,
        '-Допустимая масса техники (тонн)':25,
        }

metadict_detail['Средний танк (Panzerkampfwagen III)'] = {
        '37-мм танковая пушка (3,7 cm KwK 36)':1,
        'Танковый пулемёт (MG.34)':2,
        '-Допустимая масса техники (тонн)':25,
        }

metadict_detail['Командирский средний танк (Panzerkampfwagen III)'] = {
        '37-мм танковая пушка (3,7 cm KwK 36)':1,
        'Танковый пулемёт (MG.34)':2,
        '-Допустимая масса техники (тонн)':25,
        }

#---
# Авиация:

metadict_detail['Пикирующий бомбардировщик (Junkers Ju 87B)'] = {
        # https://ru.wikipedia.org/wiki/Junkers_Ju_87#Ju_87B_(Берта)
        '-Допустимая масса техники (тонн)':2.3,
        '500-кг авиабомба':1,
        '50-кг авиабомба':4,
        }

#---
# Транспорт:

#metadict_army['3-тонный грузовой автомобиль (Lkw. (3t))'] = {
#        # http://www.figuren.miniatures.de/lkw-3t-s-typ.html
#        '-Допустимая масса техники (тонн)':2.5,
#        #'-Место под боеприпасы (тонн)':3,
#        }

metadict_army['Грузовой автомобиль для боеприпасов (leichter gl.Lkw.)'] = {
        # http://www.figuren.miniatures.de/lkw-3t-s-typ.html
        '-Допустимая масса техники (тонн)':2.5,
        '-Место под боеприпасы (тонн)':3,
        }

metadict_army['Прицеп для боеприпасов (Anhänger (mehrachs.) für Munition)'] = {
        '-Допустимая масса техники (тонн)':2.5,
        '-Место под боеприпасы (тонн)':2,
        }

metadict_army['Полугусеничный артиллерийский тягач (Sd.Kfz.6/1)'] = {
        # Тяговое усилие -- 5 тонн
        '-Допустимая масса техники (тонн)':7.5,
        '-Место под боеприпасы (тонн)':1,
        }

#---
# Оружие

metadict_detail['Противотанковое ружьё (Panzerbüchse 39)'] = {
        # https://ru.wikipedia.org/wiki/PzB_38
        # https://de.wikipedia.org/wiki/Panzerbüchse_39
        # Эффективная дальность -- 300 метров
        'Бронебойно-трассирующие химические патроны калибра 7.92x94':100,
        '-Допустимая масса вооружения (килограмм)':12.1,
        '-Боевая скорострельность (выстрелов/минуту)':10,
        }

metadict_detail['28-мм тяжёлое противотанковое ружьё (2,8 cm schwere Panzerbüchse 41)'] = {
        # https://warspot.ru/6814-vokrug-konicheskogo-stvola
        # https://ru.wikipedia.org/wiki/Тяжёлое_противотанковое_ружьё_2,8_см_PzB_41
        # Эффективная дальность -- 500 метров
        'Ящик с выстрелами калибра 28x188 мм бронебойными':8,
        '-Допустимая масса вооружения (килограмм)':223,
        '-Вероятность поражения цели снарядом (ББМ)':0.2,
        '-Боевая скорострельность (выстрелов/минуту)':10,
        }

metadict_detail['37-мм противотанковая пушка (РАК.36)'] = {
        # https://ru.wikipedia.org/wiki/Pak_35/36
        # https://de.wikipedia.org/wiki/3,7-cm-PaK_36
        'Выстрелы калибра 37-мм бронебойные (Panzergranate 39)':200,
        '-Допустимая масса вооружения (килограмм)':480,
        '-Вероятность поражения цели снарядом (ББМ)':0.2,
        '-Боевая скорострельность (выстрелов/минуту)':10,
        }

metadict_detail['37-мм танковая пушка (3,7 cm KwK 36)'] = {
        # Эффективная дальность -- 1000 метров
        'Выстрелы калибра 37-мм бронебойные (Panzergranate 39)':131,
        '-Боевая скорострельность (выстрелов/минуту)':10,
        }

metadict_detail['75-мм танковая пушка (7,5 cm KwK 40)'] = {
        # Эффективная дальность -- 2000 метров
        'Выстрелы калибра 75-мм бронебойные (Pzgr.Patr. 39)':122,
        '-Боевая скорострельность (выстрелов/минуту)':10,
        }

metadict_detail['Лёгкий миномёт (Granatenwerfer 36)'] = {
        'Миномётные мины 50-мм':50,
        '-Допустимая масса вооружения (килограмм)':14,
        '-Радиус поражения пехоты осколками (метров)':5,
        }

metadict_detail['105-мм лёгкая полевая гаубица (10,5 cm leFH 18)'] = {
        # Уточить возимый боекомплект:
            # Дожно быть 1 БК на тягачах, 2 БК в первой команде боеприпасов и 4 БК во второй.
        # https://topwar.ru/15914-bog-voyny-vermahta-legkaya-polevaya-gaubica-lefh18.html
        # https://de.wikipedia.org/wiki/10,5-cm-leichte_Feldhaubitze_18
        'Выстрелы 105-мм осколочно-фугасные (в таре)':30 + 30*2 + 30*4,
        '-Расчётное огневое средство (РОС)':0.6,
        '-Заградительный огонь (метров фронта)':30,
        '-Допустимая масса вооружения (килограмм)':3500,
        '-Боевая скорострельность (выстрелов/минуту)':5,
        }

metadict_detail['Винтовка (Karabiner 98k)'] = {        
        'Обойма на 5 патронов 7.92x57':12,
        '-Допустимая масса вооружения (килограмм)':4,
        '-Боевая скорострельность (выстрелов/минуту)':15,
        }

metadict_detail['Лёгкий пулемёт (MG.34)'] = {
        'Лента на 50 патронов 7.92x57':1,
        '-Допустимая масса вооружения (килограмм)':12.1,
        '-Боевая скорострельность (выстрелов/минуту)':250,
        }

metadict_detail['Танковый пулемёт (MG.34)'] = {
        'Лента на 50 патронов 7.92x57':20,
        '-Допустимая масса вооружения (килограмм)':12.1,
        '-Боевая скорострельность (выстрелов/минуту)':250,
        }

metadict_detail['Лёгкий пулемёт (MG.34) (запасной)'] = {
        '-Допустимая масса вооружения (килограмм)':12.1,
        }

metadict_detail['Станковый пулемёт (MG.34)'] = {
        # Уточнить:
            # Боевую скорострельность.
            # Оснащён оптическим прицелом.
            # Станок дороже пулемёта?
        'Лента на 50 патронов 7.92x57':1,
        '-Допустимая масса вооружения (килограмм)':19.2,
        '-Боевая скорострельность (выстрелов/минуту)':250,
        }

metadict_detail['Пистолет (P.08)'] = {
        'Магазин на 8 патронов 9x19':6,
        '-Допустимая масса вооружения (килограмм)':0.88,
        }

metadict_detail['Пистолет-пулемёт (MP.40)'] = {
        # https://de.wikipedia.org/wiki/Maschinenpistole_40
        'Магазин на 32 патрона 9x19':6,
        '-Боевая скорострельность (выстрелов/минуту)':100,
        '-Допустимая масса вооружения (килограмм)':3.97,
        }

#metadict_detail['Сигнальная ракетница'] = {
#        }

#---
# Боеприпасы. Магазины, обоймы, патронные коробы, ленты

metadict_detail['Выстрелы 105-мм осколочно-фугасные (в таре)'] = {
        # Исправить.
        # Дожно быть около 25 килограмм.
        'Ящик 105-мм осколочно-фугасных снарядов (2 снаряда)':1/2,
        }

metadict_detail['Ящик 105-мм осколочно-фугасных снарядов (2 снаряда)'] = {
        # Ящик от 122-мм снарядов:
        'Выстрелы 105-мм осколочно-фугасные':2,
        #'-Объём используемый (кубометров)':1 * 0.45 * 0.25,
        '-Допустимая масса боеприпасов (тонн)':0.022,
        }

metadict_detail['Ящик с выстрелами калибра 28x188 мм бронебойными'] = {
        # Уточнить.
        # Массу тары и количество снарядов в ней:
        'Выстрелы калибра 28x188 мм бронебойные':12,
        '-Допустимая масса боеприпасов (килограмм)':2,
        }

metadict_detail['Магазин на 32 патрона 9x19'] = {
        'Патроны 9x19':32,
        '-Допустимая масса боеприпасов (килограмм)':0.3,
        }

metadict_detail['Магазин на 8 патронов 9x19'] = {
        'Патроны 9x19':8,
        '-Допустимая масса боеприпасов (килограмм)':0.1,
        }

metadict_detail['Обойма на 5 патронов 7.92x57'] = {
        'Патроны 7.92x57':5,
        '-Допустимая масса боеприпасов (килограмм)':0.2,
        }

metadict_detail['Короб на 50 патронов 7.92x57 (Gurttrommel 34)'] = {
        'Лента на 50 патронов 7.92x57':1,
        '-Допустимая масса боеприпасов (килограмм)':1,
        }

metadict_detail['Короб на 300 патронов 7.92x57 (Patronenkasten 34/41)'] = {
        # http://www.mp44.nl/equipment/patronenkasten.htm
        'Лента на 100 патронов 7.92x57':1,
        'Лента на 200 патронов 7.92x57':1,
        '-Допустимая масса боеприпасов (килограмм)':2,
        }

metadict_detail['Лента на 200 патронов 7.92x57'] = {
        'Патроны 7.92x57':200,
        '-Допустимая масса боеприпасов (килограмм)':0.8,
        }

metadict_detail['Лента на 100 патронов 7.92x57'] = {
        'Патроны 7.92x57':100,
        '-Допустимая масса боеприпасов (килограмм)':0.4,
        }

metadict_detail['Лента на 50 патронов 7.92x57'] = {
        'Патроны 7.92x57':50,
        '-Допустимая масса боеприпасов (килограмм)':0.2,
        }

#---
# Боеприпасы. Миномётные мины, снаряды, патроны:

metadict_detail['Патроны 9x19'] = {
        # https://de.wikipedia.org/wiki/9_mm_Parabellum
        '-Вероятность поражения цели пулей (боец)':0.05,
        '-Допустимая масса боеприпасов (килограмм)':0.01265,
        }

metadict_detail['Патроны 7.92x57'] = {
        # https://de.wikipedia.org/wiki/7,92_×_57_mm
        '-Вероятность поражения цели пулей (боец)':0.1,
        '-Допустимая масса боеприпасов (килограмм)':0.027,
        }

metadict_detail['Бронебойно-трассирующие химические патроны калибра 7.92x94'] = {
        # https://de.wikipedia.org/wiki/7,92_×_94_mm
        '-Вероятность поражения цели снарядом (ББМ)':0.02,
        '-Допустимая масса боеприпасов (килограмм)':0.084,
        }

metadict_detail['Выстрелы калибра 28x188 мм бронебойные'] = {
        # https://ru.wikipedia.org/wiki/Тяжёлое_противотанковое_ружьё_2,8_см_PzB_41
        # https://warspot.ru/6814-vokrug-konicheskogo-stvola
        '-Вероятность поражения цели снарядом (ББМ)':0.2,
        '-Допустимая масса боеприпасов (килограмм)':0.63,
        }

metadict_detail['Выстрелы калибра 37-мм бронебойные (Panzergranate 39)'] = {
        '-Вероятность поражения цели снарядом (ББМ)':0.2,
        '-Допустимая масса боеприпасов (килограмм)':0.69,
        }

metadict_detail['Выстрелы калибра 75-мм бронебойные (Pzgr.Patr. 39)'] = {
        '-Вероятность поражения цели снарядом (танк)':0.1,
        '-Допустимая масса боеприпасов (килограмм)':11.52,
        }

metadict_detail['Ручная граната (Stielhandgranaten 24)'] = {
        # http://army.armor.kiev.ua/hist/granata-24.shtml
        # Дальность броска 35-60 метров
        # 160-180 грамм аммонала
        '-Радиус поражения пехоты осколками (метров)':5,
        '-Допустимая масса боеприпасов (килограмм)':0.5,
        }

metadict_detail['Миномётные мины 50-мм'] = {
        '-Радиус поражения пехоты осколками (метров)':6,
        '-Допустимая масса боеприпасов (килограмм)':0.9,
        }

metadict_detail['Выстрелы 105-мм осколочно-фугасные'] = {
        # Уточнить массу порохового заряда и гильзы, пока что взял от 122-мм гаубицы:
        # ОФС -- 14.81 кг, пороховой заряд -- 3.8 кг, гильза -- 3.66 кг
        '-Допустимая масса боеприпасов (килограмм)':14.81 + 3.8 + 3.66,
        '-Расчётный боеприпас (РБ)':0.6,
        '-Радиус поражения пехоты осколками (метров)':20,
        '-Радиус поражения бронетехники осколками (метров)':15,
        }

metadict_detail['50-кг авиабомба'] = {
        '-Допустимая масса боеприпасов (килограмм)':50,
        '-Расчётный боеприпас (РБ)':1,
        '-Радиус поражения пехоты осколками (метров)':26,
        '-Радиус поражения бронетехники осколками (метров)':20,
        }

metadict_detail['500-кг авиабомба'] = {
        # ФАБ-500 М-62 -- 213 кг ВВ (300 кг тротиловый эквивалент), 287 кг стали.
            # Диаметр воронки 5.6 метров, площадь поражения укрытой пехоты -- 50 м²
        # Ударная волна в радиусе 4 метров -- 27 кПа (контузия)
            # http://koi.tspu.ru/koi_books/sinogina/gl5_51.htm
        # 28 700 опасных осколков (в среднем 10 грамм), расчёт по площади сферы:
            # 15 метров, 10 осколков на каждый кв.метр цели;
            # 50 метров, 95% вероятности поражения цели 1 м²;
            # 80 метров, 35% вероятности поражения цели 1 м².
        '-Допустимая масса боеприпасов (килограмм)':500,
        '-Расчётный боеприпас (РБ)':7,
        '-Радиус поражения пехоты осколками (метров)':50,
        '-Радиус поражения бронетехники осколками (метров)':30,
        }
