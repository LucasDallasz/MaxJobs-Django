from django.db import models

# Create your models here.
class Application(models.Model):
    profile = models.ForeignKey('Profile.Profile', on_delete=models.CASCADE)
    job = models.ForeignKey('Job.Job', on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='Em espera')
    resolution = models.CharField(max_length=50, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return f'{self.profile} / {self.job}'
    
    
    def get_attributes(self) -> dict:
        profile = self.profile
        return {
            'Nome': profile.full_name,
            'Idade': profile.age,
            'Sobre': profile.about,
            'Escolaridade': profile.schooling,
            'Data da Aplicação': self.date_created,
        }
    
    
    