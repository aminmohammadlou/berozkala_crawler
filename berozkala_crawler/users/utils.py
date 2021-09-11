from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers

def create_user_account(phone_number, password, first_name='', last_name='', **kwargs):
    user = get_user_model().objects.create_user(
        phone_number=phone_number, password=password, first_name=first_name,
        last_name=last_name, **kwargs)
    return user

def get_and_authenticate_user(phone_number, password):
    user = authenticate(username=phone_number, password=password)
    if user is None:
        raise serializers.ValidationError('Invalid username/password. Please try again!')
    return user