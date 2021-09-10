from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'confirm_password')
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):
        user = User(
            username=self.validated_data['username']
        )
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError({'password': 'Passwords must match'})
        user.set_password(password)
        user.save()
        return user
