from django.contrib.auth import get_user_model, password_validation
from rest_framework.authtoken.models import Token
from rest_framework import serializers

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'phone_number', 'password', 'first_name', 'last_name')

    def validate_phone_number(self, value):
        user = User.objects.filter(phone_number=value)
        if user:
            raise serializers.ValidationError("phone number is used")
        return value

    def validate_password(self, value):
        password_validation.validate_password(value)
        return value


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=100, required=True)
    password = serializers.CharField(required=True, write_only=True)


class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError('Current password does not match')
        return value

    def validate_new_password(self, value):
        password_validation.validate_password(value)
        return value


class AuthUserSerializer(serializers.ModelSerializer):
    auth_token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'phone_number', 'first_name', 'last_name', 'is_active', 'is_staff', 'auth_token')
        read_only_fields = ('id', 'is_active', 'is_staff','auth_token')

    def get_auth_token(self, obj):
        try:
            token = Token.objects.get(user_id=obj.id)
        except Token.DoesNotExist:
            token = Token.objects.create(user=obj)
            return token


class EmptySerializer(serializers.Serializer):
    pass
