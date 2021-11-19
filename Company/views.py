from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.forms.formsets import formset_factory

from Application.models import Application
from .forms import CompanyCreateForm, CompanyEditForm
from .models import Company
from .decorators import owner_required, validate_job, validate_application

from Utils.decorators import login_required, object_exists
from Utils.functions import get_object
from Job.forms import JobCreateForm, JobEditForm, JobFinishFormSet, JobFinishForm


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
@object_exists('Company')
@owner_required
def company_detail(request, id):
    company = request.user.get_company(id=id)
    fields = company.get_attributes()
    context = {'company': company, 'fields': fields}
    return render(request, 'Company/detail.html', context)


@login_required
@object_exists('Company')
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
@object_exists('Company')
@owner_required
def company_jobs(request, id):
    company = Company.objects.get(id=id)
    pages = Paginator(company.get_jobs(), 5)
    
    try:
        page = pages.get_page(request.GET.get('page'))
    except Exception:
        page = pages.get_page(1)
        
    context = {'company': company, 'jobs': page}
    
    return render(request, 'Company/jobs.html', context)


@login_required
@object_exists('Company')
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
@object_exists('Company')
@owner_required
@validate_job
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
@object_exists('Company')
@owner_required
@validate_job
def company_editJob(request, id, job_id):
    company = Company.objects.get(id=id)
    job = company.get_job(job_id)

    if job.get_applications():
        return redirect(f"{reverse('Company:jobDetail', kwargs={'id': id, 'job_id': job_id})}?applicationExists=1")

    form = JobEditForm(request.POST or None, instance=job)
    if form.is_valid():
        changed = '0'
        if form.has_changed():
            changed = '1'
            form.save()
        return redirect(f"{reverse('Company:jobDetail', kwargs={'id': id, 'job_id': job_id})}?changedJob={changed}")
            
    context = {'company': company, 'job': job, 'form': form}
            
    return render(request, 'Company/jobEdit.html', context)


@login_required
@object_exists('Company')
@owner_required
@validate_job
def company_JobApplications(request, id, job_id):
    company = Company.objects.get(id=id)
    job = company.get_job(job_id)
    
    if job.available == 0:
        return redirect(f"{reverse('Company:jobFinished', kwargs={'id' : id, 'job_id': job_id})}")
    
    applications = job.get_applications()
    
    context = {'job': job, 'applications': applications}
    return render(request, 'Company/jobApplications.html', context)
    
        
    
@login_required
@object_exists('Company')
@owner_required
@validate_job
@validate_application
def company_JobApplicationDetail(request, id, job_id, app_id):
    company = Company.objects.get(id=id)
    job = company.get_job(job_id)
    application = job.get_application(app_id)
    profile = application.profile

    context = {'company': company, 'job': job, 'application': profile, 'app_fields': application.get_attributes()}
    return render(request, 'Company/jobApplicationDetail.html', context)


@login_required
@object_exists('Company')
@owner_required
@validate_job
def company_finishJob(request, id, job_id):
    company = Company.objects.get(id=id)
    job = company.get_job(id=job_id)
    applications = job.get_applications()
    
    if not applications:
        return redirect(f"{reverse('Company:jobDetail', kwargs={'id': id, 'job_id': job_id})}?applicationsExists=0")
    
    FormFactory = formset_factory(
        JobFinishForm,
        formset = JobFinishFormSet,
        extra = 0
    )
    
    formset = FormFactory(
        request.POST or None,
        initial = [{'profile': app.profile, 'app_id': app.id} for app in applications]
    )
    
    if formset.is_valid():
        validsApplications = []
        
        for app in formset.cleaned_data:
            validsApplications.append(
                {'application': Application.objects.get(id=app['app_id']), 'selected': app['selected']}
            )
    
        job.finish(validsApplications)
        return redirect(f"{reverse('Company:jobFinished', kwargs={'id': id, 'job_id': job_id})}?finishedJob=1")
    
    context = {'job': job, 'formset': formset}
    
    return render(request, 'Company/finishJob.html', context)


@login_required
@object_exists('Company')
@owner_required
@validate_job
def company_jobFinished(request, id, job_id):
    company = Company.objects.get(id=id)
    job = company.get_job(job_id)
    
    if job.available == 1:
        return redirect(f"{reverse('Company:jobDetail', kwargs={'id': id, 'job_id': job_id})}?jobFinished=0")
    
    applications = job.get_approvedApplications()
    context = {'job': job, 'applications': applications}
    
    return render(request, 'Company/jobFinished.html', context)
    

    