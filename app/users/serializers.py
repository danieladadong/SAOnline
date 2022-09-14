from rest_framework import serializers
from app.users.models import UserProfile
from django.contrib.auth.models import User


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = UserProfile


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('is_superuser', 'is_staff','id')
        model = User
