from django.urls import path

from .views import *

app_name = 'Company'

urlpatterns = [
    path('my-companies/', company_all, name='all'),
    path('create/', company_create, name='create'),
    path('<id>/detail/', company_detail, name='detail'),
    path('<id>/edit/', company_edit, name='edit'),
]
