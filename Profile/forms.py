from django import forms

from .models import Profile


class ProfileCreateForm(forms.ModelForm):
    
    error_messages = {
        'minLengthFullName': 'Nome completo deve ser maior',
        'minValueMaxValueAge': 'Idade deve ser maior que 14 e menor que 65.',
        'minLengthAbout': 'Fale mais sobre você...'
    }
    
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']
        labels = {
            'full_name': 'Nome Completo',
            'age': 'Idade',
            'about': 'Sobre',
            'schooling': 'Escolaridade',
        }
        
    def clean_full_name(self):
        full_name = self.cleaned_data['full_name']
        FULL_NAME_MIN_LENGTH = 10
        if len(full_name) < FULL_NAME_MIN_LENGTH:
            raise forms.ValidationError(
                self.errors['minLengthFullName'],
                code='minLengthFullName'
            )
        return full_name
    
    
    def clean_age(self):
        age = self.cleaned_data['age']
        MIN_AGE, MAX_AGE = 14, 65
        if age < MIN_AGE or age > MAX_AGE:
            raise forms.ValidationError(
                self.error_messages['minValueMaxValueAge'],
                code='minValueMaxValueAge'
            )
        return age
    
    
    def clean_about(self):
        about = self.cleaned_data['about']
        ABOUT_MIN_LENGTH = 10
        if len(about) < ABOUT_MIN_LENGTH:
            raise forms.ValidationError(
                self.error_messages['minLengthAbout'],
                code='minLengthAbout'
            )
        return about
    

class ProfileEditForm(ProfileCreateForm):
    pass
