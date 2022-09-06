import pytest
from rest_framework.test import APIClient, APITestCase


client = APIClient()


@pytest.mark.django_db
def test_status():

    register_url = "/api/v1/users/"
    activate_url = "/api/v1/users/activation/"
    login_url = "/api/v1/token/login/"

    user_data = {
        "email": "test@example.com",
        "username": "test_user",
        "password": "verysecret"
    }
    login_data = {
        "username": "test_user",
        "password": "verysecret"
    }

    response = client.post(register_url, user_data)
    print(response.data)

    response = client.post(login_url, login_data)
    print(response.data)

    '''Test status'''
    endpoint = '/api/v1/statuses/'
    # Обязательное поле name отсутствует
    status = dict(
        description='It is first test for status'
    )
    response = client.post(endpoint, status)

    assert response.status_code == 400

    # Успешное создание статуса
    status = dict(
        name='Test status',
        description='It is first test for status'
    )
    response = client.post(endpoint, status)
    assert response.status_code == 201

    # Получение списка статусов
    response = client.get(endpoint)
    assert response.status_code == 200

    # Создание статуса с неуникальным именем
    status = dict(
        name='Test status',
        description='It is first test for status'
    )
    response = client.post(endpoint, status)
    assert response.status_code == 400

    assert False
