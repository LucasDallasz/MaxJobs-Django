from django.urls import path

from .views import *

app_name = 'Profile'

urlpatterns = [
    path('', profile_home, name='home'),
    path('create/', profile_create, name='create'),
]