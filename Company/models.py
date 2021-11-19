from django.db import models

from Job.models import Job

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
        
        
    def get_jobs(self) -> list:
        print(self.job_set.all().order_by('date_created'))
        return self.job_set.all().order_by('-date_created')


    def get_job(self, id) -> object or None:
        try:
            job = self.job_set.get(id=id)
        except Exception:
            return None
        else:
            return job

    
    def set_job(self, form_fields) -> None:
        f = form_fields
        Job.objects.create(
            office = f['office'],
            description = f['description'],
            remuneration = f['remuneration'],
<<<<<<< HEAD
            available = 1,
=======
            available = True,
>>>>>>> RecuperandoBranch1811
            schooling = f['schooling'],
            company = self
        )