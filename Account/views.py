from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

from .forms import UserRegisterForm, UserLoginForm
from Utils.decorators import login_required

# Create your views here.
def user_register(request):
    if request.user.is_authenticated:
        logout(request)
    
    form = UserRegisterForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect(f"{reverse('Account:login')}?newAccount=1")
    
    return render(request, 'Account/register.html', {'form': form})


def user_login(request):

    if request.user.is_authenticated:
        return redirect('Account:logout')
    
    form = UserLoginForm(request.POST or None)
    
    if form.is_valid():
        user = authenticate(
            request,
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password']
        )
        if user is not None:
            login(request, user)
            return redirect('Account:home')
        
        return redirect(f"{reverse('Account:login')}?errorLogin=1")
    
    return render(request, 'Account/login.html', {'form': form})


@login_required
def user_home(request):
    import django.apps
    for model in django.apps.apps.get_models():
        print(model)
    return render(request, 'Account/home.html')


def user_logout(request):
    logout(request)
    return redirect('Account:login')

