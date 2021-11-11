from django.urls import path

from .views import *

app_name = 'Profile'

urlpatterns = [
    path('', profile_home, name='home'),
    path('create/', profile_create, name='create'),
    path('edit/', profile_edit, name='edit'),
    path('jobs_available/', profile_jobs_available, name='jobs_available'),
    path('<id>/job_detail/', profile_job_detail, name='job_detail'),
]