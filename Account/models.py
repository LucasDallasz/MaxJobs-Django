from django.db import models
from django.contrib.auth.models import AbstractUser

from Company.models import Company

# Create your models here.
class User(AbstractUser):
    
    def __str__(self) -> str:
        return self.username


    def get_companies(self) -> list:
        return self.company_set.all()
    

    def set_company(self, fields) -> None:
        Company.objects.create(
            name = fields['name'],
            about = fields['about'],
            user = self
        )
