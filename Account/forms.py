from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserRegisterForm(UserCreationForm):
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
    
    error_messages = UserCreationForm.error_messages
    error_messages['usernameMinLength'] = 'Nome de usuário deve conter no mínimo 4 caracteres.'
    
    class Meta:
        model = User
        fields = ['username']
        labels = {
            'username': 'Usuário'
        }
        
        
    def clean_username(self):
        username = self.cleaned_data['username']
        USERNAME_MIN_LENGTH = 4
        
        if len(username) < USERNAME_MIN_LENGTH:
            raise forms.ValidationError(
                self.error_messages['usernameMinLength'],
                code='usernameMinLength'
            )
            
        return username       
    
     
class UserLoginForm(forms.Form):
    username = forms.CharField(
        label='Usuário',
        max_length = 150
    )
    password = forms.CharField(
        label = 'Senha',
        max_length = 50,
        widget = forms.PasswordInput()
    )