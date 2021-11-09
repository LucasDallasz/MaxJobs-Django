from django.db import models
from django.contrib.auth.models import AbstractUser

from Company.models import Company

# Create your models here.
class User(AbstractUser):
    
    def __str__(self) -> str:
        return self.username


    def get_companies(self) -> list:
        return self.company_set.all()
    
    
    def get_company(self, id) -> object or None:
        try:
            model = Company.objects.get(id=id)
        except Exception:
            return None
        else:
            return model
    

    def set_company(self, fields) -> None:
        Company.objects.create(
            name = fields['name'],
            about = fields['about'],
            user = self
        )
        
        
    def edit_company(self, formModel) -> None:
        formModel.save()
