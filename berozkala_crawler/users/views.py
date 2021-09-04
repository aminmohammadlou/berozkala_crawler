from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.views import generic
from .models import Profile

def homepage(request):
    return render(request=request, template_name='users/home.html')

def register_request(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful')
            return redirect('users:homepage')

        messages.error(request, 'Unsuccessful registration')
    form = NewUserForm()
    return render(request=request, template_name='users/register.html', context={'register_form':form})

class ProfileListView(generic.ListView):
    template_name = 'users/profile_list.html'
    queryset = Profile.objects.all()
    context_object_name = 'profiles'

class ProfileDetailView(generic.DetailView):
    model = Profile
    template_name = 'users/profile_detail.html'
    context_object_name = 'profile'