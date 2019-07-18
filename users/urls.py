
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
        )

from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet, 'users')

urlpatterns = router.urls + [
    path(r'^api/token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(r'^api/token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
]
