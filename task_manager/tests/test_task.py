"""Test task."""

import pytest
from rest_framework.test import APIClient
from django.core.management import call_command
from django.urls import reverse_lazy
from task_manager.apps.user.models import User

client = APIClient()


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'task_manager/tests/fixtures/tasks.yaml')
        call_command('loaddata', 'task_manager/tests/fixtures/users.yaml')
        call_command('loaddata', 'task_manager/tests/fixtures/statuses.yaml')


def get_user(pk=1):
    return User.objects.get(pk=pk)


@pytest.mark.django_db
def test_unauth_access():
    response = client.get(reverse_lazy('task:list'))
    assert response.status_code == 401


@pytest.mark.django_db
def test_auth_access():
    user = get_user()

    client.force_authenticate(user=user)
    response = client.get(reverse_lazy('task:list'))

    assert response.status_code == 200
    assert len(response.json()) == 24


@pytest.mark.django_db
def test_create_task():
    task_name = 'new name task'
    executor_id = 5

    response_before = client.get(reverse_lazy('task:list'))

    user = get_user()
    client.force_authenticate(user=user)

    response = client.post(reverse_lazy('task:list'), data={'name': task_name,
                                                            'author': user,
                                                            'executor_id': executor_id})
    assert response.status_code == 201

    response = client.get(reverse_lazy('task:list'))
    assert len(response.json()) == 25
    assert len(response_before.json()) + 1 == len(response.json())
    assert task_name in [tasks['name'] for tasks in response.json()]


@pytest.mark.django_db
def test_create_task_with_all_data():
    task_name = 'New name task'
    task_executor_id = 5
    task_status_id = 2
    task_description = 'New description task'
    task_label_ids = [2, 3]

    response_before = client.get(reverse_lazy('task:list'))

    user = get_user()
    client.force_authenticate(user=user)

    response = client.post(reverse_lazy('task:list'), data={'name': task_name,
                                                            'author': user,
                                                            'executor_id': task_executor_id,
                                                            'description': task_description,
                                                            'status_id': task_status_id,
                                                            'label_ids': task_label_ids,
                                                            })
    assert response.status_code == 201

    response = client.get(reverse_lazy('task:list'))
    assert len(response.json()) == 25
    assert len(response_before.json()) + 1 == len(response.json())
    assert task_name in [tasks['name'] for tasks in response.json()]


@pytest.mark.django_db
def test_create_task_with_status_ids():
    task_name = 'New name task'
    task_executor_id = 5
    task_status_id = [2, 5, 3, 4]
    task_description = 'New description task'
    task_label_ids = [2, 3]

    response_before = client.get(reverse_lazy('task:list'))

    user = get_user()
    client.force_authenticate(user=user)

    response = client.post(reverse_lazy('task:list'), data={'name': task_name,
                                                            'author': user,
                                                            'executor_id': task_executor_id,
                                                            'description': task_description,
                                                            'status_id': task_status_id,
                                                            'label_ids': task_label_ids,
                                                            })
    assert response.status_code == 201

    assert type(response.json()['status_id']) == int
    assert response.json()['status_id'] == task_status_id[-1]

    response = client.get(reverse_lazy('task:list'))
    assert len(response.json()) == 25
    assert len(response_before.json()) + 1 == len(response.json())
    assert task_name in [tasks['name'] for tasks in response.json()]


@pytest.mark.django_db
def test_executor_change_task():
    task_pk = 10
    # task_author_id = 5
    task_label_ids = [2, 3]
    # error = 'У вас недостаточно прав для выполнения данного действия.'

    user = get_user()
    client.force_authenticate(user=user)

    response_before = client.get(reverse_lazy('task:sample', kwargs={'pk': task_pk}))
    response = client.patch(reverse_lazy('task:sample', kwargs={'pk': task_pk}),
                            data={'label_ids': task_label_ids})

    # assert error == response.json()['detail']
    # assert response.status_code == 403
    response = client.get(reverse_lazy('task:sample', kwargs={'pk': task_pk}))
    assert response.json()['labels'][0]['id'] == response_before.json()['labels'][0]['id']


@pytest.mark.django_db
def test_executor_change_status_task():
    task_pk = 10

    user = get_user()
    client.force_authenticate(user=user)

    response_before = client.get(reverse_lazy('task:sample', kwargs={'pk': task_pk}))

    response = client.patch(reverse_lazy('task:sample', kwargs={'pk': task_pk}),
                            data={'status_id': 3})

    assert response.status_code == 200

    response = client.get(reverse_lazy('task:sample', kwargs={'pk': task_pk}))
    assert response_before.json()['status']['id'] != response.json()['status']['id']


@pytest.mark.django_db
def test_author_change_task():
    task_pk = 4
    task_name = 'New name task'

    user = get_user()
    client.force_authenticate(user=user)

    response = client.patch(reverse_lazy('task:sample', kwargs={'pk': task_pk}),
                            data={'name': task_name})
    assert response.status_code == 200


@pytest.mark.django_db
def test_executor_delete_task():
    task_pk = 10
    error = 'У вас недостаточно прав для выполнения данного действия.'

    user = get_user()
    client.force_authenticate(user=user)

    response_before = client.get(reverse_lazy('task:list'))

    response = client.delete(reverse_lazy('task:sample', kwargs={'pk': task_pk}))
    assert error == response.json()['detail']
    assert response.status_code == 403

    response = client.get(reverse_lazy('task:list'))
    assert len(response_before.json()) == len(response.json())


@pytest.mark.django_db
def test_author_delete_task():
    task_pk = 4

    user = get_user()
    client.force_authenticate(user=user)

    response_before = client.get(reverse_lazy('task:list'))

    response = client.delete(reverse_lazy('task:sample', kwargs={'pk': task_pk}))
    assert response.status_code == 204

    response = client.get(reverse_lazy('task:list'))
    assert len(response_before.json()) - 1 == len(response.json())


@pytest.mark.django_db
def test_delete_non_existent_task():
    task_pk = 100
    error = 'Страница не найдена.'

    user = get_user()
    client.force_authenticate(user=user)

    response_before = client.get(reverse_lazy('task:list'))

    response = client.delete(reverse_lazy('task:sample', kwargs={'pk': task_pk}))
    print(response.json())
    assert response.status_code == 404
    assert error == response.json()['detail']

    response = client.get(reverse_lazy('task:sample', kwargs={'pk': task_pk}))
    assert response.status_code == 404

    response = client.get(reverse_lazy('task:list'))
    assert len(response_before.json()) == len(response.json())


@pytest.mark.django_db
def test_add_observer_task():
    task_pk = 4
    task_observer_ids = [2, 10, 1]

    user = get_user()
    client.force_authenticate(user=user)

    response = client.patch(reverse_lazy('task:sample', kwargs={'pk': task_pk}),
                            data={'observer_ids': task_observer_ids})

    print(response.json())
    assert response.status_code == 200
