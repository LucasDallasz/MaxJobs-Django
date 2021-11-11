from django.db import models

# Create your models here.
class Application(models.Model):
    profile = models.ForeignKey('Profile.Profile', on_delete=models.CASCADE)
    job = models.ForeignKey('Job.Job', on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='Em espera')
    resolution = models.CharField(max_length=50, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return f'{self.profile} / {self.job}'
    
    
    