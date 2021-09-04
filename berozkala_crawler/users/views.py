from django.shortcuts import render
from django.views import generic
from .models import Profile

class ProfileListView(generic.ListView):
    template_name = 'users/profile_list.html'
    queryset = Profile.objects.all()
    context_object_name = 'profiles'

class ProfileDetailView(generic.DetailView):
    model = Profile
    template_name = 'users/profile_detail.html'
    context_object_name = 'profile'