from django.shortcuts import render, redirect
from django.urls import reverse


from Job.models import Job
from .functions import profileNotRegistered, validateApplication


def application_is_valid(view):
    def wrapper(request, id, *args, **kwargs):
        requerimets = [profileNotRegistered, validateApplication]
        for requeriment in requerimets:
            if not requeriment(request.user.get_profile(), Job.objects.get(id=id)):
                return redirect(f"{reverse('Profile:jobs_available')}?invalidApplication=1")
        return view(request, id, *args, **kwargs)
    return wrapper

        
                
