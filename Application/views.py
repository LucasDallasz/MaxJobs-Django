from django.shortcuts import render, redirect
from django.urls import reverse

from Utils.decorators import login_required, object_exists
from Profile.decorators import profile_exists
from Job.models import Job

from .decorators import application_is_valid
from .models import Application

# Create your views here.
@login_required
@profile_exists
def application_all(request):
    applications = Application.objects.filter(profile=request.user.get_profile()).order_by('-date_created')
    return render(request, 'Application/all.html', {'applications': applications})



@login_required
@object_exists('Job')
@profile_exists
@application_is_valid
def application_confirm(request, id):
    job = Job.objects.get(id=id)
    
    if request.method == 'POST':
        job.set_application(request.user.get_profile())
        return redirect(f"{reverse('Profile:jobs_available')}?newApplication=1")
    
    return render(request, 'Application/confirm.html', {'job': job})


@login_required
@object_exists('Application')
@profile_exists
def application_detail(request, id):
    application = Application.objects.get(id=id)
    print(application.resolution)
    if application.profile != request.user.get_profile():
        return redirect(f"{reverse('Application:all')}?applicationInvalid=1")
    context = {'application': application, 'app_fields': application.get_attributes()}
    return render(request, 'Application/detail.html', context)

