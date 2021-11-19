from django import forms

from .models import Job


class JobCreateForm(forms.ModelForm):
    error_messages = {
        'officeMinLength': 'Nome do cargo muito pequeno',
        'descriptionMinLength': 'Você deve escrever mais sobre a vaga de emprego.',
        'remunerationMinMaxValue': 'Valor de remuneração inválido.',
    }
    
    
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['company', 'available']
        labels = {
            'office': 'Cargo',
            'description': 'Descrição',
            'remuneration': 'Remuneração',
            'schooling': 'Escolaridade',
        }
        widgets = {
            'office': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'form3Example1c'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'form3Example1c',
                'cols': 5, 'rows': 2,
            }),
            'remuneration': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'form3Example1c'
            }),
        }
        
    def clean_office(self):
        office = self.cleaned_data['office']
        OFFICE_MIN_LENGTH = 5
        if len(office) < OFFICE_MIN_LENGTH:
            raise forms.ValidationError(
                self.error_messages['officeMinLength'],
                code = 'officeMinLength'
            )
        return office
    
    
    def clean_description(self):
        description = self.cleaned_data['description']
        DESCRIPTION_MIN_LENGTH = 10
        if len(description) < DESCRIPTION_MIN_LENGTH:
            raise forms.ValidationError(
                self.error_messages['descriptionMinLength'],
                code = 'descriptionMinLength'
            )
        return description
    
    
    def clean_remuneration(self):
        remuneration = self.cleaned_data['remuneration']
        MIN_VALUE, MAX_VALUE = 449, 100000
        if remuneration < MIN_VALUE or remuneration > MAX_VALUE:
            raise forms.ValidationError(
                self.error_messages['remunerationMinMaxValue'],
                code = 'remunerationMinMaxValue'
            )
        return remuneration


class JobEditForm(JobCreateForm):
    pass