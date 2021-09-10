from django.contrib.auth import get_user_model, authenticate
from django.db.models import fields
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = authenticate(**validated_data)
        if not user:
            raise ValidationError('Wrong Credentials')

        token, created = Token.objects.get_or_create(user=user)
        return user

    def to_representation(self, instance):
        data = super(UserSerializer, self).to_representation(instance)
        data['token'] = instance.auth_token.key

        return data