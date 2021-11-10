from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Company
from Job.models import Job


def owner_required(view):
    def wrapper(request, id, *args, **kwargs):
        company = Company.objects.get(id=id)
        if request.user != company.user:
            return redirect(f"{reverse('Company:all')}?userOwner=0")
        return view(request, id, *args, **kwargs)
    return wrapper


def job_is_valid(view):
    def wrapper(request, id, job_id, *args, **kwargs):
        try:
            job = Job.objects.get(id=job_id) 
        except Exception:
            return redirect(f"{reverse('Company:jobs', kwargs={'id': id})}?jobExists=0")
        else:
            company = Company.objects.get(id=id)
            if job.company != company:
                return redirect(f"{reverse('Company:jobs', kwargs={'id': id})}?invalidJob=1")
            return view(request, id, job_id, *args, **kwargs)
    return wrapper