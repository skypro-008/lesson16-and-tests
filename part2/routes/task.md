# Skypro. Lesson 16. Part 1

# Дано
Таблица `guides`.

# Надо

Сделать несколько Flask роутов с логикой работы с БД и таблицей `guide` при помощи модели `Guide`

## Роут 1
Написать роут на фласке для поиска гида по полю tours_count

HTTP Method: `GET`

Example Request URL: `/guides?tours_count=1`

Response: JSON массив с гидами

## Роут 2
Написать роут на фласке для получения гида по id

HTTP Method: `GET`

Example Request URL: `/guides/1`

Response: JSON объект с гидом

## Роут 3
Написать роут на фласке для получения всех гидов

HTTP Method: `GET`

Example Request URL: `/guides`

Response: JSON массив с гидами

## Роут 4
Написать роут на фласке для удаления гида по id

HTTP Method: `POST`

Example Request URL: `/guides/2`

## Роут 5
Написать роут на фласке для частичного обновления гида по id
Обновление должно работать для следующих полей:
- `surname`
- `full_name`
- `tours_count`

Поля с обновленной информацией могут прийти как все, так и только одно поле.

Пример всех полей:
```json 
{
"surname": "changed",
"full_name": "changed",
"tours_count": 89
}
```

Пример 1 поля:
```json
{
"tours_count": 89
}
```

HTTP Method: `PUT`

Example Body:
```json
{
"surname": "changed",
"full_name": "changed",
"tours_count": 89
}
```

Example Request URL: `/guides/3`

Reponse: JSON объект с гидом

_Hint_: JSON обновления получать из request.data или request.json
