
from django.urls import reverse

import pytest


pytestmark = pytest.mark.django_db

def test_smoke(django_app):
    response = django_app.get('/')
    assert response.status_code == 200
