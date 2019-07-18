import datetime

from rest_framework import serializers, viewsets

from django.utils.timezone import make_aware
from django.conf import settings

from . import models



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, user, validated_data):
        user = super().update(user, validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer
