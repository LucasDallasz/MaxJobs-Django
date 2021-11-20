from django.db import models

from Utils.choices import SCHOOLING_CHOICE
from Utils.functions import getSchooling

from Job.models import Job

# Create your models here.
class Profile(models.Model):
    full_name = models.CharField(max_length=60)
    age = models.IntegerField()
    about = models.TextField(max_length=700)
    email = models.EmailField(null=False, blank=False, unique=True, error_messages={'unique': 'Já existe um perfil vinculado a este email.'})
    schooling = models.IntegerField(choices=SCHOOLING_CHOICE)
    user = models.OneToOneField('Account.User', on_delete=models.CASCADE)
    
    
    def __str__(self) -> str:
        return self.full_name
    
    
    def get_attributes(self) -> dict:
        return {
            'Nome Completo': self.full_name,
            'Idade': self.age,
            'Sobre': self.about,
            'E-mail': self.email,
            'Escolaridade': getSchooling(self.schooling)
        }
        
    
    def get_jobs_available(self) -> list:
        jobs = Job.objects.filter(available=1, schooling__lte=self.schooling,).exclude(company__user=self.user)
        
        result = []
        
        for job in jobs:
            try:
                job.application_set.get(profile=self, job=job)
            except Exception:
                result.append(job)
        
        return result
                
        

        
    