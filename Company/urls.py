from django.urls import path

from .views import *

app_name = 'Company'

urlpatterns = [
    path('my-companies/', company_all, name='all'),
    path('create/', company_create, name='create'),
    path('<id>/detail/', company_detail, name='detail'),
    path('<id>/edit/', company_edit, name='edit'),
    path('<id>/jobs/', company_jobs, name='jobs'),
    path('<id>/setJob/', company_setJob, name='setJob'),
    path('<id>/jobDetail/<job_id>/', company_jobDetail, name='jobDetail'),
    path('<id>/editJob/<job_id>/', company_editJob, name='editJob'),
    path('<id>/job/<job_id>/applications/', company_JobApplications, name='JobApplications'),
    path('<id>/job/<job_id>/applications/<app_id>/detail/', company_JobApplicationDetail, name='JobApplicationDetail'),
    path('<id>/job/<job_id>/finishJob/', company_finishJob, name='finishJob'),
    path('<id>/job/<job_id>/finished/', company_jobFinished, name='jobFinished'),
]
