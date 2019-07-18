from django.urls import reverse

import pytest

from . import models

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
