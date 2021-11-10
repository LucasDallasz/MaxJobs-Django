from django.db import models

from Utils.choices import SCHOOLING_CHOICE
from Utils.functions import getSchooling

# Create your models here.
class Profile(models.Model):
    full_name = models.CharField(max_length=60)
    age = models.IntegerField()
    about = models.TextField(max_length=700)
    schooling = models.IntegerField(choices=SCHOOLING_CHOICE)
    user = models.OneToOneField('Account.User', on_delete=models.CASCADE)
    
    
    def __str__(self) -> str:
        return self.full_name
    
    
    def get_attributes(self) -> dict:
        return {
            'Nome Completo': self.full_name,
            'Idade': self.age,
            'Sobre': self.about,
            'Escolaridade': getSchooling(self.schooling)
        }
        
    
    