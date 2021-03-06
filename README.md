# Army structure analyser

Это древовидная база данных воинских формирований.  
Словарь армии определяет её состав и вооружение, рассчитывает возможности.  
Словарь деталей показывает, из каких элементов состоит вооружение, включены твёрдые цены.  
Модель военной экономики Эквестрии оценивает стоимость проектирования и производства.  

## Загрузка & компиляция

Нужен питон третьей версии, например Python 3.6.1  
Так-то скрипт должен работать независимо от системы, но на Шиндошс™ не проверялся.  
`git clone https://github.com/Shadybloom/army-structure-analyser ; cd ./army-structure-analyser`  

## Использование

Встроенная помощь:  
`./army-structure-analyser.py -h`  
`./army-structure-analyser.py --help`  
Встроенный поисковик:  
`./army-structure-analyser.py танк`  
Вывод скрипта зависит от подключённых словарей:  
`./army-structure-analyser.py танковая дивизия`  
`./army-structure-analyser.py -s танковая дивизия`  
`./army-structure-analyser.py -sm танковая дивизия`  
Можно ограничить вывод верхними уровнями:  
`./army-structure-analyser.py -sm -d 0 танковая дивизия`  
`./army-structure-analyser.py -sm -d 1 танковая дивизия`  
`./army-structure-analyser.py -sm -d 2 танковая дивизия`  
Поиск определённого объекта:  
`./army-structure-analyser.py -sm 'Вооружённые силы Эквестрии' -e 'Танковая дивизия'`  
`./army-structure-analyser.py -sm 'Танковая дивизия' -e 'Выстрелы 120-мм подкалиберные'`  
`./army-structure-analyser.py -sm жилой дом -e кирпич`  
Выбор числа объектов:  
`./army-structure-analyser.py -sm -n 100 'Хлеб (тонн)' -e 'Гектар (пшеница)'`  
`./army-structure-analyser.py -sm -n 1000 'Прокатка стали (тонн)' -e 'Электроэнергия (ГДж)'`  
`./army-structure-analyser.py -sm -n 1000 'Синтетическое топливо (тонн)' -e торф`  

## Методы

Древо графов, функция обхода в ширину, модель COCOMO2, таблицы ГЭСН.  

![Схема](/img/army-structure-analyser-scheme.png)

Скрипт работает с иерархической базой данных. Выбор названия, это выбор ветви, далее начинается последовательный обход узлов и умножение значений. Одна рота > 3 взвода > 9 отделений > 100+ бойцов. Простейший пример здесь:  
`./army-structure-analyser.py -D dict-test 'Пехотная рота'`  
`./army-structure-analyser.py -D dict-test -d 0 'Пехотная рота'`  
`./army-structure-analyser.py -D dict-test -d 1 'Пехотная рота'`  
`./army-structure-analyser.py -D dict-test -d 2 'Пехотная рота'`  
`./army-structure-analyser.py -D dict-test -d 3 'Пехотная рота'`  

Если выбрана танковая дивизия, значит на уровне -d 1 будет взят состав полков из неё, на уровне -d 2 состав батальонов и дивизионов, а дальше всё начинает смешиваться, отдельно скрипт идёт по ветви штабов, отдельно по ветвям подразделений. Когда ветвь заканчивается, ключ последнего узла сохраняется, а если на новых ветвях попадается такой же ключ, то значения суммируются. Так из кучи различных рот, взводов и отделений вычисляется число офицеров и солдат, определяется потребность в боекомплекте и стоимость вооружения.  

Формат базы данных, это питоновские словари, очень напоминающие json:  
`metadict_detail['Командир мотострелковой роты'] = {`  
`        'Капитан':1,`  
`        'Пистолет-пулемёт':1,`  
`        'Комплект боевой экипировки командира':1,`  
`        '-Управление ротами (часов/день)':12,`  
`        '===Тактический знак роты (передовой)':1,`  
`        }`  
В этом примере звание «Капитан» дальше усредняется до «Офицера», определяется зарплата, страховка и потребности (в пище и в воде); а вооружение с боевой экипровкой делится по элементам и в конце концов для каждого из них вычисляется цена. Но ключи «Управление ротами» и «Тактический знак роты» — конечные. Они появятся в выводе скрипта, потому что словарей с такими названиями в базе данных нет.  

Это главное преимущество иерархической базы данных: любая ошибка в словаре всего лишь делает его неработоспособным, а ключ к нему становится конечным и попадает в вывод. Как следствие, отладка становится элементарной задачей, а базу данных можно пополнять в полуавтоматическом режиме, пользуясь всеми возможностями регулярных выражений и макросов Vim.  

## Заметки

### Расчётные орудия и расчётные боеприпасы

РОС — расчётное огневое средство, это 152-мм гаубица [Д-20](https://ru.wikipedia.org/wiki/152-мм_пушка-гаубица_Д-20).  
РБ — расчётный боеприпас, это снаряд повышенного могущества [3ОФ25 «Гриф»](http://www.russianarms.ru/forum/index.php?topic=11923.0).  
*РОС и РБ, или ЕСОС (единое среднерасчётное огневое средство) и ЕРБ (единый расчётный боеприпас), это метод сопостовления возможностей артиллерии, авиации, танков, любых огневых средств.*  

#### Артиллерийские орудия к РОС
- 122 мм ГД-30 (М-30) — 0,85  
- 122 мм СГ 2С1 — 0,7  
- 152 мм СГ 2С3 — 0,8  
- 152 мм СП 2С5 — 1,0  
- 203 мм ГБ-4М — 0,35  
- 203 мм СП-2С7 — 0,75  
- 120 мм М — 0,5  
- БМ — 21 — 0,7  
- БМ — "УРАГАН" — 2,8  
- ТРК — 5,8 (КБЧ)  

#### Артиллерийские снаряды к РБ
- 122 мм ГД-30 (М-30) — 0,7  
- 122 мм СГ 2С1 — 0,7  
- 152 мм СГ 2С3 — 1,0  
- 152 мм СП 2С5 — 1,0  
- 203 мм ГБ-4М — 1,2  
- 203 мм СП-2С7 — 1,6  
- 120 мм М — 0,6  
- БМ — 21 — 0,6  
- БМ — "УРАГАН" — 6,0  
- ТРК — 300,0  

#### Боекомплект армейской авиации к РБ
- Ми-24П — 150  
- Ка-52 — 300  

#### Боекомплект фронтовой авиации к РБ
- Су-24? — 280  
- Ту-22М? — 400  

#### Эффективность артиллерии, РОС и РБ

*Подавление, это гибель или ранение 30% личного состава и повреждение техники: приборов наведения, гусениц танков, стволов орудий. Подавленное подразделение не может двигаться и атаковать. Уничтожение, это потеря более 50% личного состава и техники. "Уничтоженное" подразделение небоеспособно.*  

- Открытая пусковая установка тактических ракет на стартовой позиции (уничтожение) — 18 РОС; 360 РБ  
- Укрытая батарея самоходных бронированных орудий на огневых позициях (уничтожение) — 41 РОС; 1250 РБ  
- Открытая батарея самоходных бронированных орудий (подавление) — 11 РОС; 330 РБ  
- Взвод открытых самоходных бронированных минометов (подавление) — 7 РОС; 230 РБ  
- Взвод укрытых самоходных бронированных минометов (подавление) — 11 РОС; 340 РБ  
- Мотопехотная рота в районе сосредоточения (живая сила в открытых окопах) (подавление) — 32 РОС; 1920 РБ  
- Мотопехотная рота второго эшелона в открытых окопах (подавление) — 32 РОС; 1920 РБ  
- Мотопехотная рота в ходе выдвижения (на марше) — 36 РОС; 220 РБ  
- Мотопехотный взвод в боевом порядке (живая сила в БМП, БТР) (подавление) — 21 РОС; 1090 РБ  
- Взводный опорный пункт 6 га на заблаговременно подготовленных позициях (подавление) — 16 РОС; 690 РБ  
- Взводный опорный пункт 6 га на заблаговременно подготовленных позициях (уничтожение) — 24 РОС; 2600 РБ  
- Танковая рота в районе сосредоточения (подавление) — 49 РОС; 3000 РБ  
- Танковый взвод в боевом порядке (подавление) — 22 РОС; 1100 РБ  
- КП дивизии в блиндажах (подавление) — 25 РОС; 1290 РБ  
- КП бригады в блиндажах (подавление) — 23 РОС; 1150 РБ  
- КП бригады (передвижной КП дивизии) или элементы КП дивизии (живая сила в автомобилях, либо батарея буксируемых ЗУР) (подавление) — 3 РОС; 130 РБ  
- КНП батальона в блиндажах (подавление) — 8 РОС; 360 РБ  

### Противотанковые возможности

#### Танки
- Т-72 — 0.88  
- Т-72А — 1  
- Т-72Б — 1.65  
- Т-80 — 1.06  
- Т-80Б — 1.65  
- M1A1 Abrams — 1.87  
- Leopard 2 — 1.9  

#### Боевые машины пехоты
- БМП-1 — 0.47  
- БМП-2 — 0.43  
- БМП-3 — 0.65  
- M2 Bradley — 0.55  
- Marder A1 — 0.45  

#### Противотанковые ракетные комплексы
- ПТРК Штурм — 0.58  
- Конкурс — 0.45  
- Фаланга — 0.41  
- Фагот — 0.36  
- BGM-71 TOW — 0.56  
- M47 Dragon — 0.32  

#### Реактивные противотанковые гранаты
- СПГ-9 — 0.15  
- РПГ-16 — 0.09  
- РПГ-7В — 0.07  
- РПГ-7В (тандемная ПГ) — 0.2  

### Источники
 
#### Расчёты
- [Обоснование боевых возможностей мотострелкового взвода со средствами усиления в обороне](http://otherreferats.allbest.ru/war/00001229_0.html)  
- [Виктор Мураховский "О роли артиллерии в борьбе с бронецелями"](http://otvaga2004.ru/kaleydoskop/kaleydoskop-art/artillerii-v-borbe-s-br/)  
- [БОЕВЫЕ ВОЗМОЖНОСТИ МОТОСТРЕЛКОВОГО (ТАНКОВОГО) ВЗВОДА, ОТДЕЛЕНИЯ (ТАНКА) И ИХ РАСЧЕТ](http://rep.bntu.by/bitstream/handle/data/832/Основной_текст.pdf?sequence=7)  
- [Стоимость оружия (неточно, упрощённо, начало 2000-х)](http://monster-igstab.livejournal.com/42346.html)  

#### Основы
- [Иерархия воинских формирований](http://army.armor.kiev.ua/hist/ierarx.shtml)  
- [Воинские звания](http://army.armor.kiev.ua/titul/titul_1.shtml)  
- [Армейская вертикаль власти](http://army.armor.kiev.ua/hist/struktura.shtml)  
- [Что такое "штаб"](http://army.armor.kiev.ua/hist/stab.shtml)  
- [Структура армий различный стран и периодов (pdf, en, wargame)](http://www.fireandfury.com/extra/ordersofbattle.shtml)  

#### Вооружённые силы СССР и России
- [Вооруженные Силы СССР после Второй Мировой войны: от Красной армии к Советской (подробно, 1945-1991 годы)](http://coollib.com/b/333978/read)  
- [Части и соединения 40-й армии (Афганистан 1979-1989)](http://artofwar.ru/s/sukonkin_a_s/text_0130-1.shtml)  
- [Список всех войсковых соединений ГСВГ (Группа советских войск в Германии конец 1980-х)](https://ru.wikipedia.org/wiki/Список_соединений_и_частей_советских_войск_в_Германии)  
- [Список всех войсковых соединений ГСВГ (Группа советских войск в Германии конец 1980-х)](http://gsvg88.narod.ru/gsvg/army_gsvg.htm)  
- [20-я гвардейская общевойсковая армия (ГСВГ 1991 год)](https://ru.wikipedia.org/wiki/20-я_гвардейская_общевойсковая_армия)  
- [Штаты Танковых, Мотострелковых полков (Отдельных батальонов) и Парашютно-Десантных полков](http://yv-gontar.io.ua/s204359/shtaty_tankovyh_motostrelkovyh_polkov_otdelnyh_batalonov_i_parashyutno-desantnyh_polkov)  
- [Штаты артиллерии Сухопутных войск и ВДВ](http://yv-gontar.io.ua/s204353/shtaty_artillerii_suhoputnyh_voysk_i_vdv)  
- [Штаты ПВО МСП и ТП Советской Армии](http://yv-gontar.io.ua/s204347/shtaty_pvo_msp_i_tp_sovetskoy_armii)  
- [Вооружённые силы России (организация, вооружение, 2015 год)](https://web.archive.org/web/20170419224859/http://www.milkavkaz.net/2015/12/vooruzhjonnye-sily-rossii.html)  
- [Бригады сухопутных войск РФ (2008, в картинках, en)](http://shipbucket.com/forums/viewtopic.php?f=20&t=1941&start=40#p81071)  
- Перспективы развития организационно-штатной структуры общевойсковых формирований Сухопутных войск [(глава первая)](https://web.archive.org/web/20160826043433/http://samlib.siwatcher.ru/a/aleksandr_walerxewich_girin/struktura_glava_1.shtml), [(глава вторая)](https://web.archive.org/web/20160828045833/http://samlib.siwatcher.ru/a/aleksandr_walerxewich_girin/struktura_glava_2.shtml), [(глава третья)](https://web.archive.org/web/20160828172831/http://samlib.siwatcher.ru/a/aleksandr_walerxewich_girin/struktura_glava_3.shtml)  
- [Список оружия и военной техники сухопутных войск Российской Федерации](https://ru.wikipedia.org/wiki/Список_оружия_и_военной_техники_сухопутных_войск_Российской_Федерации)  

#### Вооружённые силы НАТО
- [Организация соединений ВС США (1945-1991 г.г.)](http://commi.narod.ru/mforce/usa46.htm)  
- [Лёгкая пехотная дивизия США](http://pentagonus.ru/publ/3-1-0-186)  
- [Организация армии США (в картинках, en)](http://shipbucket.com/forums/viewtopic.php?f=27&t=3119)  
- [Взгляды командования сухопутных войск США на реорганизацию боевых бригад (2016)](http://pentagonus.ru/publ/vzgljady_komandovanija_sukhoputnykh_vojsk_ssha_na_reorganizaciju_boevykh_brigad_2016/3-1-0-2675)  
- [Equipment of the United States Armed Forces](https://en.wikipedia.org/wiki/Equipment_of_the_United_States_Armed_Forces)  

#### Тыловое обеспечение
- [Артиллерийские тыловые органы](http://www.soldat.ru/doc/mobilization/mob/chapter6_2.html)  
- [Состав, структура и построение оперативного тыла Советских войск в Афганистане](http://www.oboznik.ru/?p=18867)  
- [Тыловое обеспечение войск в условиях боевых действий на территории Афганистана](http://www.oboznik.ru/?p=18949)  
- [ТЫЛОВОЕ ОБЕСПЕЧЕНИЕ МЕХАНИЗИРОВАННОЙ ДИВИЗИИ СУХОПУТНЫХ ВОЙСК США](http://www.commi.narod.ru/txt/1990/0306.htm)  

#### Ракетные войска стратегического назначения
- [Формирование и развертывание в боевой порядок дивизии, вооруженной ракетными комплексами с отдельными стартами (ОС) (1966-1983 г.г.)](http://rvsn.ruzhany.info/10rd_book_04.html)  
- [ВЛАДИМИРСКАЯ РАКЕТНАЯ СТРАТЕГИЧЕСКАЯ АРМИЯ](http://rvsn.ruzhany.info/27ra_p00.html)  
- [ВИННИЦКАЯ КРАСНОЗНАМЕННАЯ РАКЕТНАЯ АРМИЯ (Исторический очерк)](http://rvsn.ruzhany.info/43ra_00.html)  

#### Военно-воздушные силы
- [Назначение, организационная структура и вооружение авиационного полка](http://vunivere.ru/work9621)  
- [Отдельный батальон аэродромно-технического обеспечения](http://transport.kaketoustroeno.ru/a_transport&otdelniy-batalon-aerodromno-tehnicheskogo-obespecheniya&0.htm)  
- [Организация типовой бригады армейской авиации США](http://www.rulit.me/books/borba-s-vertoletami-read-240535-9.html)  

#### Военно-морской флот
- [Классификации кораблей ВМФ России](https://ru.wikipedia.org/wiki/Классификации_кораблей_ВМФ_России)  
- [Корабельный устав военно-Морского Флота Российской Федерации (2001)](http://militera.lib.ru/regulations/russr/2001_ku/01.html)  
- [Организация службы на кораблях ВМС США](http://pentagonus.ru/publ/organizacija_sluzhby_na_korabljakh_vms_ssha_1977/26-1-0-2284)  
