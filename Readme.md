# RickAndMorti

RickAndMorti - PyQt5-приложение, основными функциями которого
является получение, визуализация и взаимодействие с персонажами вселенной.

## Возможности
- Получение изображения с персонажами по API.
- Увидеть характеристики персонажей
- Самостоятельное добавление персонажей в базу данных
- Взаимодействие с базой данных без необходимости писать SQL-запросы вручную
- Загрузка изображений персонажей

## Пользовательское руководство

1. Скачайте содержимое ветки ```release``` и открыть папку pick_app
2. Запустите ```pick_app.exe```
3. Перед вами педстанет профиль персонажа.
4. При нажатии Следующий или Предыдущий персонаж вы будете перемещаться между персонажами в базе данных
5. Нажав кнопку Изменение базы данных вы перейдёте в меню управление базой данных
6. Перед вами будет простое меню. Верхняя строчка предназначена для написания команд в базу данных, если такие имеются. 
Кнопка Запустить по запросу выполнит данную команду, но в случае отсутствия желания просто выведет все данные в базе в таблицу.
Её можно самолично редактировать и после редакции нажав Сохранить изменения будет отправлен запрос в базу и изменения сохранятся.
7. В базе не очень много персонажей, но мы можем её пополнить, достаточно ввести в нижнем поле Id от 1 до 250 и нажать нижнюю кнопку
8. Кнопка Запустить по запросу и таблица обновляется с пополнением. Можно добавлять не по 1 персонажу, нужно лишь писать номера через пробел
9. Для удаления всех данных в базе данных достаточно нажать нижнюю кнопочку Очистить базу данных

## Руководство разработчика

1. Клонируйте репозиторий:

   ```git clone https://github.com/TheVitRub/sem```
2. Установите зависимости:
   ```pip install -r requirements.txt```

3. Описание модулей приложения:
- ```rick_app.py``` - главный модуль приложения
- ```rick_api.py``` - модуль взаимодействия с API
- ```change.py``` - модуль меню взаимодействия с SQL-базой данных,
отображаемой в виде виджета-таблицы.
- ```exceptc.py``` - данный модуль содержит в себе
исключения, вызываемые в различных частях программыы