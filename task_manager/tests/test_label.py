import pytest
from rest_framework.test import APIClient
from django.core.management import call_command
from django.urls import reverse_lazy
from task_manager.apps.user.models import User

client = APIClient()


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'task_manager/tests/fixtures/labels.yaml')
        call_command('loaddata', 'task_manager/tests/fixtures/users.yaml')


def get_user(pk=1):
    return User.objects.get(pk=pk)


@pytest.mark.django_db
def test_unauth_access():
    response = client.get(reverse_lazy('label:list'))
    assert response.status_code == 401


@pytest.mark.django_db
def test_auth_access():
    user = get_user()

    client.force_authenticate(user=user)
    response = client.get(reverse_lazy('label:list'))

    assert response.status_code == 200
    assert len(response.json()) == 7


@pytest.mark.django_db
def test_create_label():
    label_name = 'new name label'

    response_before = client.get(reverse_lazy('label:list'))

    user = get_user()
    client.force_authenticate(user=user)

    response = client.post(reverse_lazy('label:list'), data={'name': label_name})
    assert response.status_code == 201

    response = client.get(reverse_lazy('label:list'))
    assert len(response.json()) == 8
    assert len(response_before.json()) + 1 == len(response.json())
    assert label_name in [labels['name'] for labels in response.json()]


@pytest.mark.django_db
def test_create_labels_non_unique_name():
    label_name = 'Оборона'
    error = 'label с таким name уже существует.'

    user = get_user()
    client.force_authenticate(user=user)

    response = client.post(reverse_lazy('label:list'), data={'name': label_name})
    assert response.status_code == 400
    errors = response.json()['name']
    assert error in errors


@pytest.mark.django_db
def test_create_label_empty_name():
    error = 'Это поле не может быть пустым.'

    user = get_user()
    client.force_authenticate(user=user)

    response = client.post(reverse_lazy('label:list'), data={'name': ''})
    errors = response.json()['name']
    assert error in errors
    assert response.status_code == 400


@pytest.mark.django_db
def test_create_label_without_name():
    error = 'Обязательное поле.'

    user = get_user()
    client.force_authenticate(user=user)

    response = client.post(reverse_lazy('label:list'), data={})
    errors = response.json()['name']
    assert error in errors
    assert response.status_code == 400


@pytest.mark.django_db
def test_patch_label():
    pk = 6
    label_name = 'New name'

    user = get_user()
    client.force_authenticate(user=user)

    response_before = client.get(reverse_lazy('label:list'))

    response = client.patch(reverse_lazy('label:sample',
                                         kwargs={'pk': pk}),
                            data={'name': label_name})
    assert response.status_code == 200
    assert label_name == response.json()['name']

    response = client.get(reverse_lazy('label:list'))
    assert len(response_before.json()) == len(response.json())


@pytest.mark.django_db
def test_delete_label():
    pk = 5

    user = get_user()
    client.force_authenticate(user=user)

    response_before = client.get(reverse_lazy('label:list'))

    response = client.delete(reverse_lazy('label:sample', kwargs={'pk': pk}))
    assert response.status_code == 204
    response = client.get(reverse_lazy('label:sample', kwargs={'pk': pk}))
    assert response.status_code == 404

    response = client.get(reverse_lazy('label:list'))
    assert len(response_before.json()) - 1 == len(response.json())


@pytest.mark.django_db
def test_delete_non_existent_label():
    pk = 100
    error = 'Страница не найдена.'

    user = get_user()
    client.force_authenticate(user=user)

    response_before = client.get(reverse_lazy('label:list'))

    response = client.delete(reverse_lazy('label:sample', kwargs={'pk': pk}))
    print(response.json())
    assert response.status_code == 404
    assert error == response.json()['detail']

    response = client.get(reverse_lazy('label:sample', kwargs={'pk': pk}))
    assert response.status_code == 404

    response = client.get(reverse_lazy('label:list'))
    assert len(response_before.json()) == len(response.json())