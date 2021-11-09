from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import CompanyCreateForm, CompanyEditForm
from .models import Company
from .decorators import owner_required

from Utils.decorators import login_required, object_exists
from Job.forms import JobCreateForm


# Create your views here.
@login_required
def company_all(request):
    companies = request.user.get_companies()
    return render(request, 'Company/all.html', {'companies': companies})


@login_required
def company_create(request):
    form = CompanyCreateForm(request.POST or None)
    
    if form.is_valid():
        request.user.set_company(form.cleaned_data)
        return redirect(f"{reverse('Company:all')}?newCompany=1")
    
    return render(request, 'Company/create.html', {'form': form})



@login_required
@object_exists(Company)
@owner_required
def company_detail(request, id):
    company = request.user.get_company(id=id)
    fields = company.get_attributes()
    context = {'company': company, 'fields': fields}
    return render(request, 'Company/detail.html', context)


@login_required
@object_exists(Company)
@owner_required
def company_edit(request, id):
    company = Company.objects.get(id=id)
    form = CompanyEditForm(request.POST or None, instance = company)
    
    if form.is_valid():
        changed = '0'
        if form.has_changed():
            changed = '1'
            request.user.edit_company(form)
        return redirect(f"{reverse('Company:all')}?companyEdited={changed}")
    
    context = {'company': company,'form': form}
    
    return render(request, 'Company/edit.html', context)


@login_required
@object_exists(Company)
@owner_required
def company_jobs(request, id):
    company = Company.objects.get(id=id)
    context = {'company': company,'jobs': company.get_jobs()}
    return render(request, 'Company/jobs.html', context)


@login_required
@object_exists(Company)
@owner_required
def company_setJob(request, id):
    company = Company.objects.get(id=id)
    form = JobCreateForm(request.POST or None)
    
    if form.is_valid():
        company.set_job(form.cleaned_data)
        return redirect(
            f"{reverse('Company:jobs', kwargs={'id': id})}?newJob=1"
        )
    
    context = {'company': company, 'form': form}
    
    return render(request, 'Company/setJob.html', context)
        
    
    
    