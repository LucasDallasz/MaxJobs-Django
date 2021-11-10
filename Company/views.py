from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import CompanyCreateForm, CompanyEditForm
from .models import Company
from .decorators import owner_required, job_is_valid

from Utils.decorators import login_required, object_exists
from Utils.functions import get_object
from Job.forms import JobCreateForm, JobEditForm
from Job.models import Job


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
        return redirect(f"{reverse('Company:detail', kwargs={'id':id})}?companyEdited={changed}")
    
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


@login_required
@object_exists(Company)
@owner_required
@job_is_valid
def company_jobDetail(request, id, job_id):
    company = Company.objects.get(id=id)
    job = company.get_job(job_id)
    context = {
        'company': company,
        'job': job,
        'job_fields': job.get_attributes()
    }
    return render(request, 'Company/jobDetail.html', context)


@login_required
@object_exists(Company)
@owner_required
@job_is_valid
def company_editJob(request, id, job_id):
    company = Company.objects.get(id=id)
    job = company.get_job(job_id)

    form = JobEditForm(request.POST or None, instance=job)
    if form.is_valid():
        changed = '0'
        if form.has_changed():
            changed = '1'
            form.save()
        return redirect(f"{reverse('Company:jobDetail', kwargs={'id': id, 'job_id': job_id})}?changedJob={changed}")
            
    context = {'company': company, 'job': job, 'form': form}
            
    return render(request, 'Company/jobEdit.html', context)    
    
    
    
    