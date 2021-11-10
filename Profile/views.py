from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import ProfileCreateForm

from Utils.decorators import login_required

# Create your views here.
@login_required
def profile_home(request):
    profile = request.user.get_profile()
    return render(request, 'Profile/home.html', {'profile': profile})


@login_required
def profile_create(request):
    form = ProfileCreateForm(request.POST or None)
    
    if form.is_valid():
        request.user.set_profile(form.cleaned_data)
        return redirect(f"{reverse('Profile:home')}?newProfile=1")
    
    return render(request, 'Profile/create.html', {'form': form})

