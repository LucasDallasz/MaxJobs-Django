from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import ProfileCreateForm, ProfileEditForm
from .decorators import profile_exists

from Utils.decorators import login_required, object_exists
from Job.models import Job

# Create your views here.
@login_required
def profile_home(request):
    profile = request.user.get_profile()
    profile = profile.get_attributes() if profile else profile
    return render(request, 'Profile/home.html', {'profile': profile})


@login_required
def profile_create(request):
    form = ProfileCreateForm(request.POST or None)
    
    if form.is_valid():
        request.user.set_profile(form.cleaned_data)
        return redirect(f"{reverse('Profile:home')}?newProfile=1")
    
    return render(request, 'Profile/create.html', {'form': form})


@login_required
@profile_exists
def profile_edit(request):
    profile = request.user.get_profile()
    form = ProfileEditForm(request.POST or None, instance = profile)
    
    if form.is_valid():
        form.save()
        return redirect(f"{reverse('Profile:home')}?changed={'1' if form.has_changed() else '0'}")
    
    context = {'profile': profile, 'form': form}
    
    return render(request, 'Profile/edit.html', context)


@login_required
@profile_exists
def profile_jobs_available(request):
    profile = request.user.get_profile()
    jobs = profile.get_jobs_available()
    context = {'profile': profile, 'jobs': jobs}
    return render(request, 'Profile/jobs_available.html', context)


@login_required
@profile_exists
@object_exists(Job)
def profile_job_detail(request, id):
    job = Job.objects.get(id=id)
    job_fields = job.get_attributes()
    application_isValid = job in request.user.get_profile().get_jobs_available()
    context = {'job': job, 'job_fields': job_fields, 'applicationIsValid': application_isValid}
    return render(request, 'Profile/job_detail.html', context)

