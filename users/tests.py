from django.urls import reverse

import pytest

from . import models, factories

pytestmark = pytest.mark.django_db

def test_create_user_and_set_password(django_app):
    PASSWORD = 'password'
    response = django_app.post_json(
        reverse('users-list'),
        {
            'username': 'username',
            'password': PASSWORD,
            'email': 'user@example.com',
        }
    )
    assert response.status_code == 201
    assert models.User.objects.count() == 1
    user = models.User.objects.get()
    assert user.password != PASSWORD

def test_change_my_password(django_app):
    PASSWORD = 'password'
    NEW_PASSWORD = 'new-password'
    user = factories.UserFactory(password=PASSWORD)

    assert user.password != PASSWORD

    response = django_app.patch_json(
        reverse('users-detail', args=[user.pk]),
        {
            'password': NEW_PASSWORD,
        }
    )
    assert response.status_code == 200
    assert response.json == {
        'email': None, 'username': 'username0'
    }

    user = models.User.objects.get()
    assert user.password != PASSWORD
    assert user.password != NEW_PASSWORD
