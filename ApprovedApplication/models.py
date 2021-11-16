from django.db import models

# Create your models here.
class ApprovedApplication(models.Model):
    profile = models.ForeignKey('Profile.Profile', on_delete=models.CASCADE)
    job = models.ForeignKey('Job.Job', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.profile} / {self.job}'
    
    