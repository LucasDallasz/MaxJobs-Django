from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.urls import reverse


def login_required(view):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse('Account:login')}?loginRequired=1")
        return view(request, *args, **kwargs)
    return wrapper


def object_exists(obj):
    
    def _get_model_by_name(modelName) -> object or None:
        import django.apps
        models = django.apps.apps.get_models()
        for model in models:
            if modelName == model.__name__:
                return model
        return None
    
    def decorator(view):
        def wrapper(request, id, *args, **kwargs):
            Model = obj
            if isinstance(obj, str):
                model = _get_model_by_name(obj)
                if model is None:
                    raise ObjectDoesNotExist('Modelo inexistente.')
                Model = model
            try:
                (Model.objects.get(id=id)) is True
            except Exception:
                return render(request, 'Utils/404.html')
            else:
                return view(request, id, *args, **kwargs)          
        return wrapper
    
    return decorator



                
                

