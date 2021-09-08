# Where-to-go Service
Сервис, который позволяет выбрать на интерактивной карте интересные места в Москве, 
просмотреть фото и выбрать место для отдыха.

Администратор может добавлять новые места на карту, изменять данные мест,
а так же загружать фото, редактировать их или удалять.

[Демо сайта](https://wheretogoservice.pythonanywhere.com/)

[Админка сайта](https://wheretogoservice.pythonanywhere.com/admin)

Тестовый пользователь (права контент-менеджера):
* Пользователь `test_user`
* Пароль `7CYpd$cu`

![App screenshot](https://i.ibb.co/xmZYWBb/P3tcn1g-SYKHYDWht6qr3-A.png)

## Установка
1. Скачать репозиторий `git clone https://github.com/post1blues/where_to_go.git`
2. Перейти в папку с проектом (внутри папки должен лежать файл `manage.py`)
3. Установить нужные библиотеки `pip install -r requirements.txt`
4. Установить свой `SECRET_KEY` в файле `.env`
5. Выполнить миграции `python manage.py migrate`
6. Создать суперпользователя `python manage.py createsuperuser`

## Переменные окружения в `.env`
Приложение уже имеет настройки по-умолчанию, но при необходимости можно
настроить приложение под свои требования.

Для настройки приложения необходимо создать файл `.env` и положить его в 
корень проекта (рядом с файлом `manage.py`).

В файл можно прописать следующие переменные окружения:
1. `SECRET_KEY` - секретный ключ приложения. В приложении уже сгенерирован
секретный ключ по умолчанию, но очень рекомендуется сгенерироваться новый
и держать его в секрете;
2. `DEBUG` - булевое значение, которое включает режим дебага. По-умолчанию `true`.
3. `ALLOWED_HOSTS` - список доменных имен\хостов, которые сервис будет
обслуживать. По-умолчанию это `127.0.0.1`.
4. `DB_SQLITE3_NAME` - название базы данных, которое будет использоваться. 
По-умолчанию `db.sqlite3`;
5. `STATIC_ROOT` - относительный путь к папке, куда будет складываться 
статика после команды `collectstatic`.

## Запуск в development режиме
Выполнять нужно после предыдущего пункта
1. Установить `DEBUG=true` в файле `.env`;
2. Выполнить миграции командой `python manage.py migrate`
3. Создать при необходимости суперпользователя `python manage.py createsuperuser`
4. Запустить `python manage.py runserver`.

## Запуск в production режиме
1. Прописать `STATIC_ROOT`, куда будет собираться вся статика, в файле `.env`;
2. Прописать в `ALLOWED_HOSTS` в файле `.env` название домена, которое будет обслуживать сервис;
3. Собрать статические файлы в одну папку `python manage.py collectstatic`;
4. Установить `DEBUG=false` в файле `.env`;
5. Создать при необходимости суперпользователя `python manage.py createsuperuser`
6. Подключить нужный вам сервер - Apache\Nginx.

## Заполнение данными
Сервис позволяет добавлять новые места двумя путями:
* Через админку Django;
* Через специальную команду `load_place`.

Каждая локация содержит:
1. Заголовок - название места;
2. Короткое описание (необязательно;
3. Полное описание (необязательно);
4. Координаты (долгота и широта);
5. Изображения.

### Заполнение через админку
Для заполнения сайта через админку, необходимо перейти по адресу `<your_site>/admin` и авторизоваться.
После этого в админке можно будет добавлять новые локации.

### Заполнение данных через команду `load_place`
Для быстрого заполнения сервиса данными есть возможность использовать команду `load_place`.
Команда имеет один обязательный параметр - `url`, 
и один параметр необязательный `-a` или `--attempts`,
в котором пользователь может выбрать сколько попыток загрузить данные 
будет делать программа (по-умолчанию - 3)

```
python manage.py load_place https://url.json --attempts 10
```

Данные по `url` должны быть только в формате `json` и содержать такие поля:
1. `title` - заголовок;
2. `imgs` - массив с ссылками на изображения;
3. `description_short` - короткое описание;
4. `description_long` - полное описание;
5. `coordinates` - обьект с полями `lat` и `lng`.

Пример json-данных:

```json
{
    "title": "Экскурсионный проект «Крыши24.рф»",
    "imgs": [
        "https://kudago.com/media/images/place/d0/f6/d0f665a80d1d8d110826ba797569df02.jpg",
        "https://kudago.com/media/images/place/66/23/6623e6c8e93727c9b0bb198972d9e9fa.jpg",
        "https://kudago.com/media/images/place/64/82/64827b20010de8430bfc4fb14e786c19.jpg"
    ],
    "description_short": "Хотите увидеть Москву с высоты птичьего полёта?",
    "description_long": "<p>Проект «Крыши24.рф» проводит экскурсии ...</p>",
    "coordinates": {
        "lat": 55.753676,
        "lng": 37.64
    }
}
```

## Тестовые данные
Для теста работы сервисов вы можете использовать эти данные (уже подготовленные в нужном формате json)
* [Антикафе Bizone](https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json)
* [Арт-пространство «Бункер 703»](https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%90%D1%80%D1%82-%D0%BF%D1%80%D0%BE%D1%81%D1%82%D1%80%D0%B0%D0%BD%D1%81%D1%82%D0%B2%D0%BE%20%C2%AB%D0%91%D1%83%D0%BD%D0%BA%D0%B5%D1%80%20703%C2%BB.json)
* [Водопад Радужный](https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%92%D0%BE%D0%B4%D0%BE%D0%BF%D0%B0%D0%B4%20%D0%A0%D0%B0%D0%B4%D1%83%D0%B6%D0%BD%D1%8B%D0%B9.json)
* [Воробьёвы горы](https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%92%D0%BE%D1%80%D0%BE%D0%B1%D1%8C%D1%91%D0%B2%D1%8B%20%D0%B3%D0%BE%D1%80%D1%8B.json)
* [Генератор Маркса или «Катушка Тесла»](https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%93%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D1%82%D0%BE%D1%80%20%D0%9C%D0%B0%D1%80%D0%BA%D1%81%D0%B0%20%D0%B8%D0%BB%D0%B8%20%C2%AB%D0%9A%D0%B0%D1%82%D1%83%D1%88%D0%BA%D0%B0%20%D0%A2%D0%B5%D1%81%D0%BB%D0%B0%C2%BB.json)

## Используемые технологии
1. Django - бекенд
2. VueJS - фронтенд
3. Sqlite3 - база данных
4. [GeoJSON](https://en.wikipedia.org/wiki/GeoJSON) - для работы с гео-данными
5. [OpenStreetMap](https://www.openstreetmap.org/copyright)

## Цель проекта
Код написан в учебных целях в рамках модуля Django проекта [Devman](https://dvmn.org/).

Тестовые данные для сервиса взяты с сайта [KudaGo](https://kudago.com/).


