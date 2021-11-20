from django.shortcuts import render, redirect
from django.urls import reverse


def profile_exists(view):
    def wrapper(request, *args, **kwargs):
        profile = request.user.get_profile()
        if profile is None:
            return redirect(f"{reverse('Profile:home')}?profileExists=0")
        return view(request, *args, **kwargs)
    return wrapper


