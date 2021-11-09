from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        error_messages={
            'unique': 'Já existe uma empresa vinculada a este nome.'
        }
    )
    about = models.CharField(
        max_length=750,
        help_text='Máximo 750 caracteres.'
    )
    user = models.ForeignKey(
        'Account.User', 
        on_delete=models.CASCADE,
    )
    
    
    def __str__(self) -> str:
        return self.name


    def get_attributes(self) -> dict:
        return {
            'Nome': self.name,
            'Sobre': self.about
        }