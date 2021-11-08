from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import CompanyCreateForm
from Utils.decorators import login_required, object_exists


# Create your views here.
@login_required
def company_all(request):
    print(dir(request))
    companies = request.user.get_companies()
    return render(request, 'Company/all.html', {'companies': companies})


@login_required
def company_create(request):
    form = CompanyCreateForm(request.POST or None)
    
    if form.is_valid():
        request.user.set_company(form.cleaned_data)
        return redirect(f"{reverse('Company:all')}?newCompany=1")
    
    return render(request, 'Company/create.html', {'form': form})
    