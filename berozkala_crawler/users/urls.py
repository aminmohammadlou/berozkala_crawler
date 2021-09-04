from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('profile-list/', views.ProfileListView.as_view(), name='profile_list'),
    path('profile-list/<int:pk>', views.ProfileDetailView.as_view(), name='profile_detail'),
]