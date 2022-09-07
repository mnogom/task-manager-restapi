# email feature: https://www.django-rest-framework.org/api-guide/testing/#force_authenticateusernone-tokennone
# https://djangostars.com/blog/django-pytest-testing/ // 7. Test Mail Outbox with Pytest


import pytest
from rest_framework.test import APIClient
from django.core.management import call_command
from django.urls import reverse_lazy
from task_manager.apps.user.models import User

client = APIClient()


# Solution: https://djangostars.com/blog/django-pytest-testing/
@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'task_manager/tests/fixtures/statuses.yaml')
        call_command('loaddata', 'task_manager/tests/fixtures/users.yaml')


def get_user(pk=1):
    return User.objects.get(pk=pk)


@pytest.mark.django_db
def test_unauth_access():
    response = client.get(reverse_lazy('status:list'))
    assert response.status_code == 401


@pytest.mark.django_db
def test_auth_access():
    user = get_user()
    # https://www.django-rest-framework.org/api-guide/testing/#force_authenticateusernone-tokennone
    client.force_authenticate(user=user)
    response = client.get(reverse_lazy('status:list'))

    assert response.status_code == 200
    assert len(response.json()) == 6


@pytest.mark.django_db
def test_create_status():
    status_name = 'new name'

    response_before = client.get(reverse_lazy('status:list'))

    user = get_user()
    client.force_authenticate(user=user)
    response = client.post(reverse_lazy('status:list'), data={'name': status_name})
    assert response.status_code == 201

    response = client.get(reverse_lazy('status:list'))
    assert len(response.json()) == 7
    assert len(response_before.json()) + 1 == len(response.json())
    assert status_name in [statuses['name'] for statuses in response.json()]


@pytest.mark.django_db
def test_create_status_non_unique_name():
    status_name = 'заморожено'
    error = 'status с таким name уже существует.'

    user = get_user()
    client.force_authenticate(user=user)

    response = client.post(reverse_lazy('status:list'), data={'name': status_name})
    assert response.status_code == 400
    assert error in [statuses for statuses in response.json()['name']]


@pytest.mark.django_db
def test_create_status_without_name():
    status_description = 'This status without name'
    error = 'Обязательное поле.'

    user = get_user()
    client.force_authenticate(user=user)

    response = client.post(reverse_lazy('status:list'), data={'description': status_description})
    assert error in [statuses for statuses in response.json()['name']]
    assert response.status_code == 400


@pytest.mark.django_db
def test_patch_status():
    pk = 6
    status_description = 'This status with new description'

    user = get_user()
    client.force_authenticate(user=user)

    response_before = client.get(reverse_lazy('status:list'))

    response = client.patch(reverse_lazy('status:sample',
                                         kwargs={'pk': pk}),
                            data={'description': status_description})
    assert response.status_code == 200
    assert status_description == response.json()['description']

    response = client.get(reverse_lazy('status:list'))
    assert len(response_before.json()) == len(response.json())


@pytest.mark.django_db
def test_delete_status():
    pk = 5

    user = get_user()
    client.force_authenticate(user=user)

    response_before = client.get(reverse_lazy('status:list'))

    response = client.delete(reverse_lazy('status:sample', kwargs={'pk': pk}))
    assert response.status_code == 204
    response = client.get(reverse_lazy('status:sample', kwargs={'pk': pk}))
    assert response.status_code == 404

    response = client.get(reverse_lazy('status:list'))
    assert len(response_before.json()) - 1 == len(response.json())


@pytest.mark.django_db
def test_delete_non_existent_status():
    pk = 100
    error = 'Страница не найдена.'

    user = get_user()
    client.force_authenticate(user=user)

    response_before = client.get(reverse_lazy('status:list'))

    response = client.delete(reverse_lazy('status:sample', kwargs={'pk': pk}))
    print(response.json())
    assert response.status_code == 404
    assert error == response.json()['detail']

    response = client.get(reverse_lazy('status:sample', kwargs={'pk': pk}))
    assert response.status_code == 404

    response = client.get(reverse_lazy('status:list'))
    assert len(response_before.json()) == len(response.json())


# @pytest.mark.django_db
# def test_status():
#
#     register_url = "/api/v1/users/"
#     activate_url = "/api/v1/users/activation/"
#     login_url = "/api/v1/token/login/"
#
#     user_data = {
#         "email": "test@example.com",
#         "username": "test_user",
#         "password": "verysecret"
#     }
#     login_data = {
#         "username": "test_user",
#         "password": "verysecret"
#     }
#
#     response = client.post(register_url, user_data)
#     print(response.data)
#
#     response = client.post(login_url, login_data)
#     print(response.data)
#
#     '''Test status'''
#     endpoint = '/api/v1/statuses/'
#     # Обязательное поле name отсутствует
#     status = dict(
#         description='It is first test for status'
#     )
#     response = client.post(endpoint, status)
#
#     assert response.status_code == 400
#
#     # Успешное создание статуса
#     status = dict(
#         name='Test status',
#         description='It is first test for status'
#     )
#     response = client.post(endpoint, status)
#     assert response.status_code == 201
#
#     # Получение списка статусов
#     response = client.get(endpoint)
#     assert response.status_code == 200
#
#     # Создание статуса с неуникальным именем
#     status = dict(
#         name='Test status',
#         description='It is first test for status'
#     )
#     response = client.post(endpoint, status)
#     assert response.status_code == 400
#
#     assert False
