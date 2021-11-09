from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Company


def owner_required(view):
    def wrapper(request, id, *args, **kwargs):
        company = Company.objects.get(id=id)
        if request.user != company.user:
            return redirect(f"{reverse('Company:all')}?userOwner=0")
        return view(request, id, *args, **kwargs)
    return wrapper
    