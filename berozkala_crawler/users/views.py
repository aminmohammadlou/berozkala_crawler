from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views import generic
from .models import Profile

from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import UserSerializer

#django template function-base views
def homepage(request):
    return render(request=request, template_name='users/home.html')

# def register_request(request):
#     if request.method == 'POST':
#         form = NewUserForm(request.POST)
        
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, 'Registration successful')
#             return redirect('users:homepage')

#         messages.error(request, 'Unsuccessful registration')
#     form = NewUserForm()
#     return render(request=request, template_name='users/register.html', context={'register_form':form})

# def login_request(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
        
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)

#             if user is not None:
#                 login(request, user)
#                 messages.info(request, f'You are now logged in as {username}')
#                 return redirect('users:homepage')
#             else:
#                 messages.error(request, 'Invalid username or password')
#         else:
#             messages.error(request, 'Invalid username or password')

#     form = AuthenticationForm()
#     return render(request=request, template_name='users/login.html', context={'login_form':form})

# class ProfileListView(generic.ListView):
#     template_name = 'users/profile_list.html'
#     queryset = Profile.objects.all()
#     context_object_name = 'profiles'

# class ProfileDetailView(generic.DetailView):
#     model = Profile
#     template_name = 'users/profile_detail.html'
#     context_object_name = 'profile'

#django rest framework API view
# @api_view(['POST',])
# def registration_view(request):
#     if request.method == 'POST':
#         serializer = RegistrationSerializer(data=request.data)
#         data = {}
#         if serializer.is_valid():
#             user = serializer.save()
#             data['response'] = 'successfully registered a new user'
#             data['username'] = user.username
#         else:
#             data = serializer.errors
#         return Response(data)
User = get_user_model()


class UserRegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer