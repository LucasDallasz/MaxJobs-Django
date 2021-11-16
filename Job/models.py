from django.db import models

from Utils.choices import SCHOOLING_CHOICE
from Utils.functions import getSchooling

from Application.models import Application
from ApprovedApplication.models import ApprovedApplication

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
    
    
    def get_attributes(self) -> dict:
        return {
            'Cargo': self.office,
            'Descrição': self.description,
            'Remuneração': self.remuneration,
            'Escolaridade': getSchooling(self.schooling),
            'Empresa': self.company
        }
    
    
    def get_applications(self) -> list:
        return self.application_set.all()
    
    

    
    def get_application(self, id) -> object or None:
        try: 
            application = self.application_set.get(id=id)
        except Exception: 
            return None
        else:
            return application
    
    
    def get_approvedApplications(self) -> list:
        return self.approvedapplication_set.all()
        
        
    def set_application(self, profile) -> None:
        Application.objects.create(
            profile=profile,
            job=self
        )
        
        
    def finish(self, applications) -> None:
        self.available = 0
        
        for application in applications:
            if application['selected']:
                application['application'].finish('Aprovado')
                ApprovedApplication.objects.create(
                    profile = application['application'].profile,
                    job = self
                )
            else:
                application['application'].finish('Reprovado')
                
        self.save()
        
        
        
    
        