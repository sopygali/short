from rest_framework import serializers
from .models import Logins, User

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logins
        fields = ('id', 'user', 'link')

class LoginAPISerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'