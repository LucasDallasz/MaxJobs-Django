from django.urls import path

from .views import *

app_name = 'Application'

urlpatterns = [
    path('my-applications/', application_all, name='all'),
    path('<id>/confirm/', application_confirm, name='confirm'),
    path('<id>/detail/', application_detail, name='detail'),
]