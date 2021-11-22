from django.db import models

# Create your models here.
class Notification(models.Model):
    viewd = models.BooleanField(default=False)
    message = models.TextField(max_length=455)
    date_created = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey('Profile.Profile', on_delete=models.CASCADE)
    
    
    def __str__(self) -> str:
        return f'{self.message} >> {self.profile}'
    
    
    def visited(self) -> None:
        setattr(self, 'viewd', True)
        self.save()
    


        