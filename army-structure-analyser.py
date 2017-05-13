#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------
# Модули:

# Парсер аргументов командной строки:
import argparse
# Переменные операционной системы:
import os
# Регулярные выражения:
import re

#-------------------------------------------------------------------------
# Опции:

# Состав какого отряда исследуем по умолчанию:
SQUAD = 'Вооружённые силы Эквестрии'
# Глубина исследования:
DEPTH = 99
# Каталог словарей:
METADICT_DIR = 'dict'

#-------------------------------------------------------------------------
# Аргументы командной строки:

def create_parser():
    """Список доступных параметров скрипта."""
    parser = argparse.ArgumentParser()
    parser.add_argument('squad',
                        nargs='*',
                        help='Название отряда (в "кавычках")'
                        )
    parser.add_argument('-d', '--depth',
                        action='store', dest='depth', type=int,
                        help='Глубина исследования (0-999)'
                        )
    parser.add_argument('-s', '--short',
                        action='store_true', default='False',
                        help='Краткий вывод, обобщение, расчёты'
                        )
    parser.add_argument('-m', '--model',
                        action='store_true', default='False',
                        help='Моделирование, затраты времени'
                        )
    return parser

#-------------------------------------------------------------------------
# Функции:

def metadict_path ():
    """Возвращает абсолютный путь к каталогу словарей."""
    # Получаем абсолютный путь к каталогу скрипта:
    script_path = os.path.dirname(os.path.abspath(__file__))
    # Добавляем к пути каталог словарей:
    metadict_path = script_path + '/' + METADICT_DIR
    return metadict_path

def find_files (directory):
    """Возвращает список путей ко всем файлам каталога, включая подкаталоги."""
    path_f = []
    for d, dirs, files in os.walk(directory):
        for f in files:
                # Формирование адреса:
                path = os.path.join(d,f)
                # Добавление адреса в список:
                path_f.append(path)
    return path_f

#-------------------------------------------------------------------------
# База данных, двумерный массив, структура армии:

# Словарь армии:
metadict_army = {}

# Словарь деталей:
metadict_detail = {}

# Модель:
metadict_model = {}

#-------------------------------------------------------------------------
# Загрузка словарей в базу данных:

dicts_list = find_files(metadict_path())
for file_path in dicts_list:
    with open(file_path) as f:
        code = compile(f.read(), file_path, 'exec')
        exec(code, globals(), locals())

#-------------------------------------------------------------------------
# Обработка аргументов командной строки:

# Создаётся список аргументов скрипта:
parser = create_parser()
namespace = parser.parse_args()

# Проверка, введено ли название:
if namespace.squad != None:
    squad = ' '.join(namespace.squad)
else:
    # Если нет, мспользовать стандартное:
    squad = SQUAD

# Проверка, указана ли глубина исследования:
if namespace.depth != None:
    depth = namespace.depth
else:
    # Если нет, мспользовать стандартную:
    depth = DEPTH

# Проверка, выбран ли словарь деталей:
if namespace.short is True:
    # Объединяем словари
    metadict_army.update(metadict_detail)

# Проверка, выбран ли словарь модели:
if namespace.model is True:
    # Объединяем словари
    metadict_army.update(metadict_model)

#-------------------------------------------------------------------------
# Встроенный поисковик:

# Словарь найденных совпадений:
dict_search = {}

# Создаём словарь совпадений:
p = re.compile(squad, re.I)
counter = 0
if squad not in metadict_army.keys():
    for line in sorted(metadict_army.keys()):
        if p.findall(line):
            dict_search[counter] = line
            search_string = line
            counter = counter + 1
    # Если искомое не найдено, тогда выход:
    if len(dict_search) == 0:
        print('---Совпадений не найдено')
        exit(0)
    # Если несколько совпадений, тогда выбор по номеру:
    if len(dict_search) > 1:
        for key in dict_search:
            print(key,dict_search[key])
        string_number = input('---Найдено несколько совпадений (введите номер): ')
        search_string = dict_search[int(string_number)]
        squad = search_string
        print('-----------------------------------------------------')
        print(squad)
    # Если найден один варинт, тогда срабатывает скрипт:
    else:
        squad = search_string
        print(squad)

#-------------------------------------------------------------------------
# Исполняемый код:

# Рабочий словарь:
dict_crew = {}

# Обход в ширину, функция:
def bfd(vertex, number):
    # Проверка, является ли объект составным:
    #print ('    vertex:', vertex, number)
    if vertex in metadict_army:
        # Определяется состав объекта:
        for key,value in sorted(metadict_army[vertex].items()):
            #print ('        key:', key, value)
            if vertex in dict_crew:
                value = value * dict_crew[vertex]
            else:
                value = value * number
            # Если объект уже есть в рабочем словаре, прибавить:
            if key in dict_crew:
                dict_crew[key] = dict_crew[key] + value
            # Иначе создать новый объект:
            else:
                dict_crew[key] = value
    # Если объект цельный:
    else:
        # Проверка, есть ли такие объекты в рабочем словаре:
        if vertex in dict_crew:
            # Если да, суммировать:
            dict_crew[vertex] = dict_crew[vertex] + number
        else:
            dict_crew[vertex] = number

# Многоуровневый обход в ширину:
if depth == 0:
    for key,value in sorted(metadict_army[squad].items()):
        print(key,round(value))
else:
    cycles = depth - 1
    # Формируется временный словарь
    for key,value in sorted(metadict_army[squad].items()):
        # Первый уровень исследования
        #print ('-----------------')
        #print ('cycle:',cycles)
        bfd(key, value)
        #print ('    dict:', dict_crew)
    # Цикл исследования временного словаря
    while cycles > 0:
        #print ('-----------------')
        #print ('cycle:',depth)
        for key,value in sorted(dict_crew.items()):
            if key in metadict_army:
                # Функция извлекает состав объекта:
                bfd(key, value)
                # Удаляется обработанный объект из словаря:
                dict_crew.pop(key)
                #print ('    dict:', dict_crew)
        cycles -= 1
        depth -= 1

# Вывод данных:
for key,value in sorted(dict_crew.items()):
    print(key,round(value))
    #print(key)
