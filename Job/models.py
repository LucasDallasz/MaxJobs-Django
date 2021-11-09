from django.db import models

from Utils.choices import SCHOOLING_CHOICE

# Create your models here.
class Job(models.Model):
    office = models.CharField(max_length=50)
    description = models.TextField(max_length=455)
    remuneration = models.DecimalField(max_digits=9, decimal_places=2)
    available = models.BooleanField(default=True)
    schooling = models.IntegerField(choices=SCHOOLING_CHOICE)
    company = models.ForeignKey('Company.Company', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.office
    
    