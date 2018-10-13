from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    login
)
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    template = 'registration/login.html'
    return render(request, template)

 
def register(request):
    template = 'registration/register.html'
    if request.method == "POST":
       form = UserCreationForm(request.POST or None)
       if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    context = {"form": form}

    return render(request, template, context)


def home(request):
    template = 'registration/views/index.html'
    context = locals()
    return render(request, template, context)