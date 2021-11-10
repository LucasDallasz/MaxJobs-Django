from django.shortcuts import render, redirect
from django.urls import reverse


def login_required(view):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse('Account:login')}?loginRequired=1")
        return view(request, *args, **kwargs)
    return wrapper


def object_exists(Model):
    def decorator(view):
        def wrapper(request, id, *args, **kwargs):
            try:
                (Model.objects.get(id=id)) is not None
            except Exception:
                return render(request, 'Utils/404.html')
            else:
                return view(request, id, *args, **kwargs)
        return wrapper
    return decorator


                
                

