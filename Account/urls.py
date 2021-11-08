from django.urls import path
from .views import *

app_name = 'Account'

urlpatterns = [
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('home/', user_home, name='home'),
    path('logout/', user_logout, name='logout'),
]