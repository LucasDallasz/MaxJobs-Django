from django import forms
from django.forms import widgets

from .models import Company


class CompanyCreateForm(forms.ModelForm):
    
    error_messages = {
        'aboutMinLength': 'Você precisa falar mais sobre a empresa...'
    }
    
    class Meta:
        model = Company
        fields = ['name', 'about']
        labels = {
            'name': 'Nome',
            'about': 'Sobre',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'inputName'
            }),
            'about': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'form3Example4c',
                'cols': 10, 'rows': 7,
            })
        }
        
    def clean_about(self):
        about = self.cleaned_data['about']
        ABOUT_MIN_LENGTH = 5
        if len(about) < ABOUT_MIN_LENGTH:
            raise forms.ValidationError(
                self.error_messages['aboutMinLength'],
                code = 'aboutMinLength'
            )
        return about
    
    
class CompanyEditForm(CompanyCreateForm):
    pass
        