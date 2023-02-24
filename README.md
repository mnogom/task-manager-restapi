# Task manager API

[![Maintainability](https://api.codeclimate.com/v1/badges/049761a29c96d7314d29/maintainability)](https://codeclimate.com/github/mnogom/task_manager/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/049761a29c96d7314d29/test_coverage)](https://codeclimate.com/github/mnogom/task_manager/test_coverage)
[![python-ci](https://github.com/mnogom/task_manager/actions/workflows/python-ci.yaml/badge.svg)](https://github.com/mnogom/task_manager/actions/workflows/python-ci.yaml)

_Simple APi for simple task manager_

---
## Installation
```shell
pip3 install --upgrade poetry
git clone https://github.com/mnogom/task-manager-restapi
cd task-manager-restapi
make install
```

## Run
```shell
make run
```

## Endpoints

### Auth
> [POST] /api/v1/auth/token/login/ - Token Based Authentication

Request body
```json
{
    "email": "djon.snow@wall.com",
    "password": "1"
}
```
Response body
```json
{
    "auth_token": "1234abcd"
}
```
Place in token to headers:
```
Authorization: Token 1234abcd
```

---
> [GET] /api/v1/auth/users/me/ - Get auth user *(auth required)*
Response body
```json
{
    "username": "EjikVTumane",
    "id": 1,
    "email": "djon.snow@wall.com"
}
```

---
> [POST] /api/v1/auth/users/set_password/ - Update password *(auth required)*

Request body
```json
{
    "new_password": "a",
    "current_password": "1"
}
```

---
> [POST] /api/v1/auth/token/logout/ - Logout *(auth required)*

---

> [ ] /api/v1/auth/users/reset_password/

> [ ] /api/v1/auth/users/reset_password_confirm/

> [ ] /api/v1/auth/users/set_username/

> [ ] /api/v1/auth/users/reset_username/

> [ ] /api/v1/auth/users/reset_username_confirm/

---

### Users
> [GET] /api/v1/users/ - List users *(auth required)*

Response body
```json
[
    {
        "id": 1,
        "email": "djon.snow@wall.com",
        "username": "EjikVTumane",
        "first_name": "Джон",
        "last_name": "Сноу"
    },
    {
        "id": 2,
        "email": "tirion.lannister@vesteross.it",
        "username": "Karlson",
        "first_name": "Тирион",
        "last_name": "Ланнистер"
    }
]
```

---
> [GET] /api/v1/users/1/ - Get user by id *(auth required)* 

Response body
```json
{
    "id": 6,
    "email": "serseya.lannister@vesteross.it",
    "username": "Vinnie-The-Puh",
    "first_name": "Серсея",
    "last_name": "Ланистер"
}
```

### Labels
> [GET] /api/v1/labels/ - List labels *(auth required)*

Response body
```json
[
    {
        "id": 1,
        "name": "Оборона"
    },
    {
        "id": 2,
        "name": "Атака"
    }
]
```

---
> [POST] /api/v1/labels/ - Create labels *(auth required)*

Request body
```json
{
    "name": "АСАП"
}
```
Response body
```json
{
    "id": 8,
    "name": "АСАП"
}
```


---
> [GET] /api/v1/labels/\<int:pk>/ - Read label by id *(auth required)*

Response body
```json
{
    "id": 6,
    "name": "Внешнее"
}
```

---
> [PATCH] /api/v1/labels/\<int:pk>/ - Update label by id *(auth required)*

Request body
```json
{
    "id": 8,
    "name": "АСАП"
}
```
Response body
```json
{
    "id": 8,
    "name": "ASAP"
}
```

---
> [DELETE] /api/v1/labels/\<int:pk>/ - Delete label by id *(auth required)*

---

### Statuses
* [GET] /api/v1/statuses/ - List statuses *(auth required)*
* [POST] /api/v1/statuses/ - Create statuses *(auth required)*
* [GET] /api/v1/statuses/\<int:pk>/ - Read status by id *(auth required)*
* [PATCH] /api/v1/statuses/\<int:pk>/ - Update status by id *(auth required)*
* [DELETE] /api/v1/statuses/\<int:pk>/ - Delete status by id *(auth required)*

READ list response example:
```json
[
    {
        "id": 1,
        "name": "неначато",
        "description": "This is the worst status. Make it in progress"
    },
    {
        "id": 2,
        "name": "в процессе",
        "description": ""
    }
]
```

READ by id response example:
```json
{
    "id": 4,
    "name": "потеряно",
    "description": ""
}
```

POST / PATCH request data example:
```json
{
    "name": "завершено",
    "description": ""
}
```

### Tasks
> [GET] /api/v1/tasks/ - List tasks *(auth required)*

Response body
```json
[
    {
        "id": 1,
        "name": "Проверить создание задач",
        "description": "Создай, измени, удали... ну ты понял",
        "status": {
            "id": 4,
            "name": "потеряно",
            "description": ""
        },
        "author": {
            "id": 6,
            "email": "serseya.lannister@vesteross.it",
            "username": "Vinnie-The-Puh",
            "first_name": "Серсея",
            "last_name": "Ланистер"
        },
        "executor": {
            "id": 8,
            "email": "teon.greyjoy@enjoy.com",
            "username": "VolkIZayac",
            "first_name": "Теон",
            "last_name": "Грейджой"
        },
        "observer": [],
        "labels": [
            {
                "id": 4,
                "name": "Диверсия"
            },
            {
                "id": 6,
                "name": "Внешнее"
            },
            {
                "id": 7,
                "name": "Внутреннее"
            }
        ]
    },
    {
        "id": 2,
        "name": "Выдать ноутбук",
        "description": "",
        "status": {
            "id": 3,
            "name": "завершено",
            "description": ""
        },
        "author": {
            "id": 3,
            "email": "ramsi.bolton@gmail.com",
            "username": "Trubadoor",
            "first_name": "Рамси",
            "last_name": "Болтон"
        },
        "executor": {
            "id": 5,
            "email": "varis007@master.tv",
            "username": "Cheburaka",
            "first_name": "Варис",
            "last_name": ""
        },
        "observer": [],
        "labels": [
            {
                "id": 5,
                "name": "Переговоры"
            },
            {
                "id": 6,
                "name": "Внешнее"
            },
            {
                "id": 7,
                "name": "Внутреннее"
            }
        ]
    }
]
```

---

> [POST] /api/v1/tasks/ - Create tasks *(auth required)*
Request body
```json
{
    "name": "Составить документацию к проекту",
    "description": "Пора уже полностью описать проект",
    "executor_id": 3,
    "observer_ids": [
      4,
      5
    ],
    "label_ids": [
      1,
      2
    ],
    "status_id": 1
}
```
Response body
```json
{
    "id": 26,
    "name": "Составить документацию к проекту",
    "description": "Пора уже полностью описать проект",
    "executor_id": 3,
    "observer_ids": [
        4,
        5
    ],
    "status_id": 1,
    "label_ids": [
        1,
        2
    ]
}
```

---

> [GET] /api/v1/tasks/\<int:pk>/ - Read task by id *(auth required)*

Response body
```json
{
    "id": 1,
    "name": "Проверить создание задач",
    "description": "Создай, измени, удали... ну ты понял",
    "status": {
        "id": 4,
        "name": "потеряно",
        "description": ""
    },
    "author": {
        "id": 6,
        "email": "serseya.lannister@vesteross.it",
        "username": "Vinnie-The-Puh",
        "first_name": "Серсея",
        "last_name": "Ланистер"
    },
    "executor": {
        "id": 8,
        "email": "teon.greyjoy@enjoy.com",
        "username": "VolkIZayac",
        "first_name": "Теон",
        "last_name": "Грейджой"
    },
    "observer": [],
    "labels": [
        {
            "id": 4,
            "name": "Диверсия"
        },
        {
            "id": 6,
            "name": "Внешнее"
        },
        {
            "id": 7,
            "name": "Внутреннее"
        }
    ]
}
```

---

> [PATCH] /api/v1/tasks/\<int:pk>/ - Update task by id *(only author or executor)*

Request body:
```json
{
    "name": "Скорректировать задачу",
    "description": "Ради примера",
    "executor_id": 3,
    "observer_ids": [
      9
    ],
    "label_ids": [
      3
    ],
    "status_id": 2
}
```
Response body:
```json
{
    "id": 28,
    "name": "Скорректировать задачу",
    "description": "Ради примера",
    "executor_id": 3,
    "observer_ids": [
        9
    ],
    "status_id": 2,
    "label_ids": [
        3
    ]
}
```

---

> [DELETE] /api/v1/tasks/\<int:pk>/ - Delete task by id *(only author or executor)*

---

## Object Relations


```
user_user
---------
PK | id      
   | username
   | first_name
   | last_name
   | email
   | ...
```

```
status_status
-------------
PK | id
   | name
   | description
   | created_at
```

```
label_label
-----------
PK | id
   | name
   | created_at
```

```
task_task
---------
PK | id
   | name
   | description
   | created_at
FK | author_id
FK | executor_id
FK | status_id
```

```
task_task_observer
------------------
PK | id
FK | task_id
FK | user_id
```

```
task_task_label
---------------
PK | id
FK | label_id
FK | task_id
```