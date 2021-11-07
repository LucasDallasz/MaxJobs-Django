from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserLoginForm(UserCreationForm):
    password1 = forms.CharField(
        label = 'Senha',
        max_length = 50,
        strip = False,
        widget = forms.PasswordInput()
    )
    password2 = forms.CharField(
        label = 'Confirmar Senha',
        max_length = 50,
        strip = False,
        widget = forms.PasswordInput()
    )
    
    class Meta:
        model = User
        fields = ['username']
        labels = {
            'username': 'Usuário'
        }