from django.shortcuts import render, redirect
from . import models, forms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


# register
def register_view(request):
    if request.method == "POST":
        if form.is_valid():
            form = forms.ResumeForm(request.POST, request.FILES)
            form.save()
            return redirect('/login/')
        else:
            form = forms.ResumeForm()

    return render(request, 'users/register.html', {'form': form})


# login
def auth_login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/user_list/')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


#logout
def auth_logout_view(request):
    logout(request)
    return redirect('/login/')


#user_list
def resume_list_view(request):
    if request.method == "GET":
        resume_list = models.Resume.objects.all()
    return render(request, 'users/resumes.html', {'res': resume_list})

# Create your views here.
