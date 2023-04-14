from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    profile_picture = serializers.ImageField(required= False)
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ("id", "email", "first_name", "last_name", "password", "profile_picture")

class UserUpdate(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField(max_length = 100)
    last_name = serializers.CharField(max_length = 100)
    profile_picture = serializers.ImageField(required= False)
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ("id","first_name", "last_name", "profile_picture")