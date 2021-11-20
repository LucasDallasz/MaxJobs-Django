from django.db import models
from django.contrib.auth.models import AbstractUser

from Company.models import Company
from Profile.models import Profile

# Create your models here.
class User(AbstractUser):
    
    def __str__(self) -> str:
        return self.username


    def get_companies(self) -> list:
        return self.company_set.all().order_by
    
    
    def get_company(self, id) -> object or None:
        try:
            model = Company.objects.get(id=id)
        except Exception:
            return None
        else:
            return model
    

    def get_profile(self) -> object or None:
        try:
            return self.profile
        except Exception:
            return None


    def set_company(self, fields) -> None:
        Company.objects.create(
            name = fields['name'],
            about = fields['about'],
            user = self
        )
        
        
    def edit_company(self, formModel) -> None:
        formModel.save()


    def set_profile(self, form_data) -> None:
        f = form_data
        Profile.objects.create(
            full_name = f['full_name'],
            age = f['age'],
            about = f['about'],
            schooling = f['schooling'],
            email = f['email'],
            user = self
        )
        

    