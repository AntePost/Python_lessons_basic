
"""
== OpenWeatherMap ==

OpenWeatherMap — онлайн-сервис, который предоставляет бесплатный API
 для доступа к данным о текущей погоде, прогнозам, для web-сервисов
 и мобильных приложений. Архивные данные доступны только на коммерческой основе.
 В качестве источника данных используются официальные метеорологические службы
 данные из метеостанций аэропортов, и данные с частных метеостанций.

Необходимо решить следующие задачи:

== Получение APPID ==
    Чтобы получать данные о погоде необходимо получить бесплатный APPID.

    Предлагается 2 варианта (по желанию):
    - получить APPID вручную
    - автоматизировать процесс получения APPID,
    используя дополнительную библиотеку GRAB (pip install grab)

        Необходимо зарегистрироваться на сайте openweathermap.org:
        https://home.openweathermap.org/users/sign_up

        Войти на сайт по ссылке:
        https://home.openweathermap.org/users/sign_in

        Свой ключ "вытащить" со страницы отсюда:
        https://home.openweathermap.org/api_keys

        Ключ имеет смысл сохранить в локальный файл, например, "app.id"


== Получение списка городов ==
    Список городов может быть получен по ссылке:
    http://bulk.openweathermap.org/sample/city.list.json.gz

    Далее снова есть несколько вариантов (по желанию):
    - скачать и распаковать список вручную
    - автоматизировать скачивание (ulrlib) и распаковку списка
     (воспользоваться модулем gzip
      или распаковать внешним архиватором, воспользовавшись модулем subprocess)

    Список достаточно большой. Представляет собой JSON-строки:
{"_id":707860,"name":"Hurzuf","country":"UA","coord":{"lon":34.283333,"lat":44.549999}}
{"_id":519188,"name":"Novinki","country":"RU","coord":{"lon":37.666668,"lat":55.683334}}


== Получение погоды ==
    На основе списка городов можно делать запрос к сервису по id города. И тут как раз понадобится APPID.
        By city ID
        Examples of API calls:
        http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=b1b15e88fa797225412429c1c50c122a

    Для получения температуры по Цельсию:
    http://api.openweathermap.org/data/2.5/weather?id=520068&units=metric&appid=b1b15e88fa797225412429c1c50c122a

    Для запроса по нескольким городам сразу:
    http://api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric&appid=b1b15e88fa797225412429c1c50c122a


    Данные о погоде выдаются в JSON-формате
    {"coord":{"lon":38.44,"lat":55.87},
    "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],
    "base":"cmc stations","main":{"temp":280.03,"pressure":1006,"humidity":83,
    "temp_min":273.15,"temp_max":284.55},"wind":{"speed":3.08,"deg":265,"gust":7.2},
    "rain":{"3h":0.015},"clouds":{"all":76},"dt":1465156452,
    "sys":{"type":3,"id":57233,"message":0.0024,"country":"RU","sunrise":1465087473,
    "sunset":1465149961},"id":520068,"name":"Noginsk","cod":200}


== Сохранение данных в локальную БД ==
Программа должна позволять:
1. Создавать файл базы данных SQLite со следующей структурой данных
   (если файла базы данных не существует):

    Погода
        id_города           INTEGER PRIMARY KEY
        Город               VARCHAR(255)
        Дата                DATE
        Температура         INTEGER
        id_погоды           INTEGER                 # weather.id из JSON-данных

2. Выводить список стран из файла и предлагать пользователю выбрать страну
(ввиду того, что список городов и стран весьма велик
 имеет смысл запрашивать у пользователя имя города или страны
 и искать данные в списке доступных городов/стран (регуляркой))

3. Скачивать JSON (XML) файлы погоды в городах выбранной страны
4. Парсить последовательно каждый из файлов и добавлять данные о погоде в базу
   данных. Если данные для данного города и данного дня есть в базе - обновить
   температуру в существующей записи.


При повторном запуске скрипта:
- используется уже скачанный файл с городами;
- используется созданная база данных, новые данные добавляются и обновляются.


При работе с XML-файлами:

Доступ к данным в XML-файлах происходит через пространство имен:
<forecast ... xmlns="http://weather.yandex.ru/forecast ...>

Чтобы работать с пространствами имен удобно пользоваться такими функциями:

    # Получим пространство имен из первого тега:
    def gen_ns(tag):
        if tag.startswith('{'):
            ns, tag = tag.split('}')
            return ns[1:]
        else:
            return ''

    tree = ET.parse(f)
    root = tree.getroot()

    # Определим словарь с namespace
    namespaces = {'ns': gen_ns(root.tag)}

    # Ищем по дереву тегов
    for day in root.iterfind('ns:day', namespaces=namespaces):
        ...

"""


# Version 1
# Списал с чужого форка. В коде постарался разобраться. Здесь видимо неполная
# версия, так как не прописано создание файла "city.list.json".
import json
from ulrlib.request import urlopen

# Читаем список городов
with open("lesson08/home_work/city.list.json", encoding="UTF-8") as f:
    cities_list = json.load(f)

# Ищем подходящие варианты
city_name = input("Введите название города на английском: ")
variants = []
for city in cities_list:
    if city["name"].find(city_name) >= 0:
        variants.append(city)

# Если городов несколько, предлагаем выбрать из подходящих.
if len(variants) > 1:
    print("Город с таким названием есть в нескольких странах:")
    for i, city in enumerate(variants):
        print("{}. {} ({})".format(i + 1, city["country"], city["name"]))
    city = variants[int(input("Введите номер страны: ")) - 1]
elif len(variants) = 1:
    city = variants[0]
else:
    print("Город с таким названием не найден.")
    exit()

# Скачиваем и показываем данные о погоде для выбранного города.
with open('lesson08/home_work/app.id', encoding="UTF-8") as f:
    appid = f.readline()

url = "http://api.openweathermap.org/data/2.5/weather?units=metric&id={}&appid={}".format(city["id"], appid)
city_data = json.load(urlopen(url))
print("{} {}: {}C".format(
    city_data["name"],
    city_data["sys"]["country"]
    city_data["main"]["temp"]
))


# Version 2
# Списал с чужого форка. В коде постарался разобраться.
import requests
import sqlite3
import os


a = open("app.id")
my_app_id = a.read().splitlines()
api_url = "http://api.openweathermap.org/data/2.5/weather"
city = input("Пожалуйста введите город на английском языке: ")
data_list = {'q': city, 'appid': my_app_id, "units": "metric"}
a.close()

inquiry = requests.get(api_url, params = data_list) #Отправим запрос на получение данных

data = inquiry.json() #Сохраним полученные данные
conclusion = "Температура в городе {} сейчас {} градус(ов)"
print(conclusion.format(city, data["main"]["temp"])) #Вытаскиваем градусы из данных

save_data = input("Хотите сохранить данные в SQLite? y/n: ")
if save_data == 'y' or 'Y':
    weather = [(data["sys"]["id"], city, data["dt"], data["main"]["temp"], data["main"]["temp"])] #Записываем необходимые данные
    connect = sqlite3.connect("{}.db".format(city))
    c = connect.cursor()
    if os.path.isfile("{}.db".format(city)): #Если БД уже есть - обновляем
        c.execute("""REPLACE INTO weather (id_города, Город, Дата, Температура, id_погоды) VALUES (?, ?, ?, ?, ?)""", (data["sys"]["id"], city, data["dt"], data["main"]["temp"], data["main"]["temp"])) # Обновляем значения в БД
        connect.commit() # UPDATE weather SET id_города=?, Город=?, Дата=?, Температура=?, id_погоды=? WHERE ?
        c.close()
        connect.close()
        print("Такая база уже существует. Мы её обновили!")
    else:
        c.execute('''CREATE TABLE weather (id_города INTEGER PRIMARY KEY, Город VARCHAR(255), Дата DATE, Температура INTEGER, id_погоды INTEGER)''')
        c.executemany("INSERT INTO weather VALUES (?, ?, ?, ?, ?)", weather) # Добавляем значения в БД
        connect.commit()
        c.close()
        connect.close()
        print("База данных {}.db создана!".format(city))
else:
    print("Хорошо, создавать БД не будем. Приятного дня!")
