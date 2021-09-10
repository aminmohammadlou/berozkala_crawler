from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    #path('profile-list/', views.ProfileListView.as_view(), name='profile_list'),
    #path('profile-list/<int:pk>', views.ProfileDetailView.as_view(), name='profile_detail'),
    path('register', views.registeration_view, name='register'),
    #path('login', views.login_request, name='login'),
]