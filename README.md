# Проект Api notes

## Описание

Api_notes простое REST приложение для создания заметок. На этом сервисе зарегистрированные пользователи смогут 
создавать, изменять и удалять заметки используя интерфейс REST API. Присутствуют два вида авторизации Basic и JWT.

Ознакомиться с интерфейсом приложения и самим приложением можно по ссылке: <br/>
[api.pkhludyw.beget.tech](http://api.pkhludyw.beget.tech)



Тестовый пользователь:

- login: test@gmail.com
- password: 123

Возможности сервиса:

- Регистрация пользователей.
- Создание, Изменение, Удаление записей.

- ### Установка

- Клонируйте репозиторий к себе на компьютер командой:

```
https://github.com/DamageHunter/api_notes
```

Перейдите в каталог проекта:

```
cd api_notes
```

Создайте файл окружений

```
python3 -m venv env
```

Активируйте его:

```
source env/bin/activate
```

Загрузите все пакеты из requirements.txt:

```
pip3 install -r requirements.txt
```
Создайте миграции для бд:

```
python3 manage.py makemigrations

python3 manage.py migrate
```

Загрузка начальные данные (фикстуру):

```
python3 manage.py loaddata initial_data.json
```

Запустите сервер
```
python3 manage.py runserver
```

После этого сайт будет доступен по адресу http://127.0.0.1:8000/api/




